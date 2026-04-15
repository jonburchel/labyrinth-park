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


def _snap(filename, eye_ft, target_ft, space, window, screen, area, region):
    eye = mathutils.Vector((eye_ft[0] * FT, eye_ft[1] * FT, eye_ft[2] * FT))
    target = mathutils.Vector((target_ft[0] * FT, target_ft[1] * FT, target_ft[2] * FT))
    forward = (target - eye).normalized()
    quat = forward.to_track_quat("-Z", "Y")
    r3d = space.region_3d
    r3d.view_perspective = "PERSP"
    r3d.view_location = eye
    r3d.view_rotation = quat
    r3d.view_distance = 0.0
    space.shading.type = "MATERIAL"
    space.shading.use_scene_lights = False
    space.shading.use_scene_world = True
    path = os.path.join(OUT_DIR, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with bpy.context.temp_override(window=window, screen=screen, area=area, region=region):
        bpy.ops.screen.screenshot(filepath=path)
    print(path)


w, s, a, r, sp = _find_view3d()

_snap(
    "gapfix_tree_planter_contact.png",
    eye_ft=(7.5, -2.5, 3.0),
    target_ft=(5.0, -2.9, 1.2),
    space=sp,
    window=w,
    screen=s,
    area=a,
    region=r,
)

_snap(
    "gapfix_rear_underside_ground.png",
    eye_ft=(0.0, 85.0, -18.0),
    target_ft=(0.0, 42.0, 2.0),
    space=sp,
    window=w,
    screen=s,
    area=a,
    region=r,
)
