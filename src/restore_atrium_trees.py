"""
Restore a symmetric atrium tree layout using local high-quality plant assets.

Run inside Blender:
    .\Send-Blender.ps1 -File src\restore_atrium_trees.py
"""

import math
from pathlib import Path

import bpy
from mathutils import Vector

PROJECT_ROOT = Path(r"F:\home\exploded-hexagon-home")
ASSETS_DIR = PROJECT_ROOT / "assets" / "models" / "plants"
FT = 0.3048

ATRIUM_FLOOR_Z = -1.0 * FT
HEX_SIDE = 23.0 * FT
HEX_INRADIUS = HEX_SIDE * math.sqrt(3.0) * 0.5
SAFE_TREE_RADIUS = HEX_INRADIUS - 3.0 * FT
MAX_TREE_TOP_Z = 30.0 * FT
# Poly Haven island tree assets include root geometry offset upward from the
# object's lowest bounds, so we embed slightly into planter soil to remove
# visible floating gaps.
TREE_BASE_EMBED = 1.28 * FT


def _assign_single_mat(obj, mat):
    if obj.type != "MESH":
        return
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def _make_planter_materials():
    conc = bpy.data.materials.get("AtriumPlanterConcrete")
    if conc is None:
        conc = bpy.data.materials.new("AtriumPlanterConcrete")
    conc.use_nodes = True
    cn = conc.node_tree.nodes
    cl = conc.node_tree.links
    cn.clear()
    cout = cn.new("ShaderNodeOutputMaterial")
    cout.location = (280, 0)
    cbsdf = cn.new("ShaderNodeBsdfPrincipled")
    cbsdf.location = (20, 0)
    cbsdf.inputs["Base Color"].default_value = (0.73, 0.73, 0.72, 1.0)
    cbsdf.inputs["Roughness"].default_value = 0.28
    if "Specular IOR Level" in cbsdf.inputs:
        cbsdf.inputs["Specular IOR Level"].default_value = 0.42
    cl.new(cbsdf.outputs["BSDF"], cout.inputs["Surface"])

    soil = bpy.data.materials.get("AtriumPlanterSoil")
    if soil is None:
        soil = bpy.data.materials.new("AtriumPlanterSoil")
    soil.use_nodes = True
    sn = soil.node_tree.nodes
    sl = soil.node_tree.links
    sn.clear()
    sout = sn.new("ShaderNodeOutputMaterial")
    sout.location = (280, 0)
    sbsdf = sn.new("ShaderNodeBsdfPrincipled")
    sbsdf.location = (20, 0)
    sbsdf.inputs["Base Color"].default_value = (0.14, 0.11, 0.08, 1.0)
    sbsdf.inputs["Roughness"].default_value = 0.9
    sl.new(sbsdf.outputs["BSDF"], sout.inputs["Surface"])
    return conc, soil


def _hex_vertices(s):
    return [(s * math.cos(math.radians(i * 60.0)), s * math.sin(math.radians(i * 60.0))) for i in range(6)]


HEX_POLY = _hex_vertices(HEX_SIDE)


def _point_inside_hex(px: float, py: float, margin: float = 0.0) -> bool:
    # Convex half-space test for CCW flat-top hex.
    for i in range(len(HEX_POLY)):
        x0, y0 = HEX_POLY[i]
        x1, y1 = HEX_POLY[(i + 1) % len(HEX_POLY)]
        ex = x1 - x0
        ey = y1 - y0
        cross = ex * (py - y0) - ey * (px - x0)
        if cross < margin:
            return False
    return True


def _remove_previous_atrium_plants():
    prefixes = (
        "RealisticPlant_",
        "Tree_",
        "Palm_",
        "Bush_",
        "Fern_",
        "TreePlanter_",
        "PlanterSoil_",
        "AtriumPlanter_",
        "island_tree_",
        "island_trees_",
        "pachira_aquatica_",
    )
    to_remove = set()
    for obj in bpy.data.objects:
        if obj.name.startswith(prefixes):
            to_remove.add(obj)

    def _collect_desc(o):
        for child in o.children:
            to_remove.add(child)
            _collect_desc(child)

    for obj in list(to_remove):
        _collect_desc(obj)

    removed = 0
    for obj in list(to_remove):
        if obj.name in bpy.data.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
            removed += 1
    print(f"Removed {removed} prior plant/planter objects")


def _asset_path(slug: str) -> str:
    folder = ASSETS_DIR / slug
    if not folder.exists():
        raise FileNotFoundError(f"Missing plant asset folder: {folder}")
    gltfs = sorted(p for p in folder.iterdir() if p.suffix.lower() == ".gltf")
    if not gltfs:
        raise FileNotFoundError(f"No GLTF file in: {folder}")
    return str(gltfs[0])


def _import_tree_group(slug: str, idx: int):
    before = set(bpy.data.objects.keys())
    bpy.ops.import_scene.gltf(filepath=_asset_path(slug))
    after = set(bpy.data.objects.keys())
    names = after - before
    imported = [bpy.data.objects[n] for n in names if n in bpy.data.objects]
    roots = [o for o in imported if (o.parent is None or o.parent.name not in names)]
    if not roots:
        raise RuntimeError(f"Imported no roots for {slug}")

    group = bpy.data.objects.new(f"Tree_{slug}_{idx:02d}", None)
    group.empty_display_type = "SPHERE"
    group.empty_display_size = 0.2
    bpy.context.scene.collection.objects.link(group)
    for root in roots:
        root.parent = group
    return group, imported


def _group_bbox(imported):
    bpy.context.view_layer.update()
    min_v = Vector((1e18, 1e18, 1e18))
    max_v = Vector((-1e18, -1e18, -1e18))
    found = False
    for obj in imported:
        if obj.type != "MESH":
            continue
        found = True
        for c in obj.bound_box:
            w = obj.matrix_world @ Vector(c)
            min_v.x = min(min_v.x, w.x)
            min_v.y = min(min_v.y, w.y)
            min_v.z = min(min_v.z, w.z)
            max_v.x = max(max_v.x, w.x)
            max_v.y = max(max_v.y, w.y)
            max_v.z = max(max_v.z, w.z)
    if not found:
        return None
    return min_v, max_v


def _align_base_to(imported, group, base_z: float):
    bb = _group_bbox(imported)
    if bb is None:
        return
    min_v, _ = bb
    group.location.z += (base_z - min_v.z)


def _uniform_scale_group(group, factor: float):
    group.scale = (
        group.scale[0] * factor,
        group.scale[1] * factor,
        group.scale[2] * factor,
    )


def _radial_max_from_center(imported):
    bb = _group_bbox(imported)
    if bb is None:
        return 0.0
    min_v, max_v = bb
    corners = (
        (min_v.x, min_v.y),
        (min_v.x, max_v.y),
        (max_v.x, min_v.y),
        (max_v.x, max_v.y),
    )
    return max(math.hypot(x, y) for x, y in corners)


def _all_mesh_bboxes_inside_hex(imported, margin: float = 0.0):
    bpy.context.view_layer.update()
    for obj in imported:
        if obj.type != "MESH":
            continue
        corners = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
        for c in corners:
            if not _point_inside_hex(c.x, c.y, margin=margin):
                return False
    return True


def _create_planter(i: int, x: float, y: float, conc_mat, soil_mat):
    outer_r = 2.0 * FT
    outer_h = 2.6 * FT
    soil_h = 0.20 * FT
    lip = 0.22 * FT

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=6,
        radius=outer_r,
        depth=outer_h,
        location=(x, y, ATRIUM_FLOOR_Z + outer_h * 0.5),
        rotation=(0.0, 0.0, math.radians(30.0)),
    )
    planter = bpy.context.active_object
    planter.name = f"TreePlanter_{i:02d}"
    _assign_single_mat(planter, conc_mat)

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=6,
        radius=max(0.1, outer_r - lip),
        depth=soil_h,
        location=(x, y, ATRIUM_FLOOR_Z + outer_h - soil_h * 0.5),
        rotation=(0.0, 0.0, math.radians(30.0)),
    )
    soil = bpy.context.active_object
    soil.name = f"PlanterSoil_{i:02d}"
    _assign_single_mat(soil, soil_mat)

    return ATRIUM_FLOOR_Z + outer_h - soil_h


def _place_tree(
    i: int,
    slug: str,
    x_ft: float,
    y_ft: float,
    target_height_ft: float,
    rot_deg: float,
    conc_mat,
    soil_mat,
    min_top_ft: float | None = None,
):
    x = x_ft * FT
    y = y_ft * FT
    base_z = _create_planter(i, x, y, conc_mat, soil_mat)
    group, imported = _import_tree_group(slug, i)
    group.location = Vector((x, y, 0.0))
    group.rotation_euler = (0.0, 0.0, math.radians(rot_deg))

    target_base_z = base_z - TREE_BASE_EMBED
    _align_base_to(imported, group, target_base_z)

    bb = _group_bbox(imported)
    if bb:
        min_v, max_v = bb
        h = max(max_v.z - min_v.z, 1e-6)
        target_h = target_height_ft * FT
        _uniform_scale_group(group, target_h / h)
        _align_base_to(imported, group, target_base_z)

    radial = _radial_max_from_center(imported)
    if radial > SAFE_TREE_RADIUS:
        _uniform_scale_group(group, (SAFE_TREE_RADIUS / radial) * 0.96)
        _align_base_to(imported, group, target_base_z)

    bb = _group_bbox(imported)
    if bb:
        _, max_v = bb
        if max_v.z > MAX_TREE_TOP_Z:
            top_scale = (MAX_TREE_TOP_Z - base_z) / max(max_v.z - base_z, 1e-6)
            _uniform_scale_group(group, max(0.2, top_scale * 0.98))
            _align_base_to(imported, group, target_base_z)

    # Final clip-safe shrink toward center until all mesh bounds are inside atrium hex.
    for _ in range(10):
        if _all_mesh_bboxes_inside_hex(imported, margin=0.15 * FT):
            break
        _uniform_scale_group(group, 0.92)
        group.location.x *= 0.97
        group.location.y *= 0.97
        _align_base_to(imported, group, target_base_z)

    # Ensure designated specimen trees reach a minimum top elevation.
    if min_top_ft is not None:
        target_top_z = min_top_ft * FT
        bb = _group_bbox(imported)
        if bb:
            _, max_v = bb
            if max_v.z < target_top_z:
                current_h = max(max_v.z - target_base_z, 1e-6)
                desired_h = max(target_top_z - target_base_z, current_h)
                scale_up = min(1.5, desired_h / current_h)
                _uniform_scale_group(group, scale_up)
                _align_base_to(imported, group, target_base_z)
                for _ in range(8):
                    if _all_mesh_bboxes_inside_hex(imported, margin=0.05 * FT):
                        break
                    _uniform_scale_group(group, 0.97)
                    _align_base_to(imported, group, target_base_z)

    print(f"Placed {group.name} using {slug} at ({x_ft:.1f}, {y_ft:.1f}) ft")


def main():
    print("=" * 68)
    print("Restoring atrium trees with symmetric planter layout")
    print("=" * 68)
    _remove_previous_atrium_plants()
    conc_mat, soil_mat = _make_planter_materials()

    # Center specimen + four surrounding planters.
    # Remove planters nearest Wing C and motorcourt axes, keep four around
    # the center in right-angle increments and push them outward ~6'.
    slots = [
        ("island_tree_01", 0.0, 0.0, 28.0, 0.0),
    ]
    ring_r_ft = 11.8  # previous 5.8 + ~6' outward
    ring_slugs = ("island_tree_02", "island_tree_01")
    for i in range(4):
        ang = math.radians(45.0 + i * 90.0)
        x_ft = ring_r_ft * math.cos(ang)
        y_ft = ring_r_ft * math.sin(ang)
        slug = ring_slugs[i % len(ring_slugs)]
        height_ft = 12.0 + (i % 2) * 2.0
        rot = 20.0 * i
        slots.append((slug, x_ft, y_ft, height_ft, rot))

    for i, (slug, x_ft, y_ft, h_ft, rot_deg) in enumerate(slots):
        min_top_ft = 26.0 if i == 0 else None
        _place_tree(i, slug, x_ft, y_ft, h_ft, rot_deg, conc_mat, soil_mat, min_top_ft=min_top_ft)

    print("Done placing atrium trees and planters.")
    print("=" * 68)


if __name__ == "__main__":
    main()
