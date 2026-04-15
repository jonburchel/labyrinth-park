import os

import bpy
import mathutils

FT = 0.3048
OUT_DIR = r"F:\home\exploded-hexagon-home\renders"


def _find_view3d():
    for w in bpy.context.window_manager.windows:
        s = w.screen
        for a in s.areas:
            if a.type != "VIEW_3D":
                continue
            for r in a.regions:
                if r.type == "WINDOW":
                    return w, s, a, r, a.spaces.active
    raise RuntimeError("No VIEW_3D area found")


def _snap(name, eye_xyz_ft, target_xyz_ft, space, window, screen, area, region, use_world=True):
    eye = mathutils.Vector((eye_xyz_ft[0] * FT, eye_xyz_ft[1] * FT, eye_xyz_ft[2] * FT))
    target = mathutils.Vector((target_xyz_ft[0] * FT, target_xyz_ft[1] * FT, target_xyz_ft[2] * FT))
    forward = (target - eye).normalized()
    quat = forward.to_track_quat("-Z", "Y")

    r3d = space.region_3d
    r3d.view_perspective = "PERSP"
    r3d.view_location = eye
    r3d.view_rotation = quat
    r3d.view_distance = 0.0

    space.shading.type = "MATERIAL"
    space.shading.use_scene_lights = False
    space.shading.use_scene_world = use_world

    path = os.path.join(OUT_DIR, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with bpy.context.temp_override(window=window, screen=screen, area=area, region=region):
        bpy.ops.screen.screenshot(filepath=path)
    print(path)


w, s, a, r, sp = _find_view3d()

_snap(
    "design_atrium_trees_floor_material.png",
    eye_xyz_ft=(0.0, 0.0, 4.5),
    target_xyz_ft=(0.0, 19.0, 2.0),
    space=sp,
    window=w,
    screen=s,
    area=a,
    region=r,
    use_world=True,
)

_snap(
    "design_floor_inlay_top_material.png",
    eye_xyz_ft=(0.0, 0.0, 28.0),
    target_xyz_ft=(0.0, 0.0, -1.0),
    space=sp,
    window=w,
    screen=s,
    area=a,
    region=r,
    use_world=True,
)

_snap(
    "design_rear_terrain_drop_material.png",
    eye_xyz_ft=(0.0, 90.0, 24.0),
    target_xyz_ft=(0.0, 45.0, 6.0),
    space=sp,
    window=w,
    screen=s,
    area=a,
    region=r,
    use_world=True,
)

_snap(
    "design_world_panorama_material.png",
    eye_xyz_ft=(0.0, -35.0, 10.0),
    target_xyz_ft=(0.0, 120.0, 20.0),
    space=sp,
    window=w,
    screen=s,
    area=a,
    region=r,
    use_world=True,
)
