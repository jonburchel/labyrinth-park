import math
import bpy
from mathutils import Vector

FT = 0.3048
S = 23.0 * FT


def _hex_vertices(s):
    return [(s * math.cos(math.radians(i * 60.0)), s * math.sin(math.radians(i * 60.0))) for i in range(6)]


def _point_in_convex(px, py, poly):
    for i in range(len(poly)):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % len(poly)]
        cross = (x1 - x0) * (py - y0) - (y1 - y0) * (px - x0)
        if cross < -1e-6:
            return False
    return True


def _bbox_world(obj):
    corners = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
    min_x = min(v.x for v in corners)
    max_x = max(v.x for v in corners)
    min_y = min(v.y for v in corners)
    max_y = max(v.y for v in corners)
    min_z = min(v.z for v in corners)
    max_z = max(v.z for v in corners)
    return (min_x, max_x, min_y, max_y, min_z, max_z)


hex_poly = _hex_vertices(S)
prefixes = ("island_tree_", "island_trees_", "pachira_aquatica_", "TreePlanter_", "PlanterSoil_")
targets = [o for o in bpy.data.objects if o.type == "MESH" and o.name.startswith(prefixes)]

violations = []
max_top = -1e9
for obj in targets:
    bb = _bbox_world(obj)
    max_top = max(max_top, bb[5])
    corners = [
        (bb[0], bb[2]),
        (bb[0], bb[3]),
        (bb[1], bb[2]),
        (bb[1], bb[3]),
    ]
    for cx, cy in corners:
        if not _point_in_convex(cx, cy, hex_poly):
            violations.append(obj.name)
            break

print("Tree clearance check:")
print(f"  Objects checked: {len(targets)}")
print(f"  Max tree/planter top: {max_top / FT:.2f} ft")
if violations:
    print(f"  Violations: {len(violations)}")
    for name in sorted(set(violations)):
        print(f"    - {name}")
else:
    print("  Violations: 0")
