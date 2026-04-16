"""
Patent Drawing Generator for Provisional Patent Application:
"Autonomously Reconfigurable Living Landscape Maze System and Method"

Generates 8 technical figures suitable for USPTO provisional filing.
Patent drawings should be black and white, with clear labels and reference numerals.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'patent', 'drawings')
os.makedirs(OUT_DIR, exist_ok=True)

def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  Saved {name}")


def fig1_system_overview():
    """Fig 1: Top-down system overview showing maze with mobile and fixed sections"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.set_xlim(-5, 55)
    ax.set_ylim(-5, 55)
    ax.set_aspect('equal')
    ax.set_title('FIG. 1 - System Overview (Top View)', fontsize=14, fontweight='bold')

    # Draw outer boundary
    ax.add_patch(patches.Rectangle((0, 0), 50, 50, fill=False, edgecolor='black', linewidth=2))

    # Fixed hedge sections (solid gray)
    fixed_hedges = [
        (0, 0, 2, 50), (48, 0, 2, 50), (0, 0, 50, 2), (0, 48, 50, 2),  # perimeter
        (10, 2, 2, 20), (10, 28, 2, 20),  # internal fixed walls
        (20, 10, 2, 15), (20, 30, 2, 18),
        (30, 2, 2, 22), (30, 28, 2, 12),
        (38, 5, 2, 18), (38, 32, 2, 16),
        (12, 20, 8, 2), (25, 24, 13, 2),
        (12, 35, 18, 2), (5, 10, 5, 2),
    ]
    for x, y, w, h in fixed_hedges:
        ax.add_patch(patches.Rectangle((x, y), w, h, facecolor='#888888', edgecolor='black', linewidth=0.5))

    # Mobile hedge units (hatched, darker)
    mobile_hedges = [
        (10, 22, 2, 6, '10a'),
        (20, 25, 2, 5, '10b'),
        (30, 24, 2, 4, '10c'),
        (38, 23, 2, 9, '10d'),
        (5, 20, 7, 2, '10e'),
        (32, 10, 6, 2, '10f'),
    ]
    for x, y, w, h, label in mobile_hedges:
        ax.add_patch(patches.Rectangle((x, y), w, h, facecolor='#333333', edgecolor='black', linewidth=1))
        ax.annotate(label, (x + w/2, y + h/2), color='white', fontsize=7,
                   ha='center', va='center', fontweight='bold')

    # Trough positions (dashed rectangles showing where mobile units could go)
    alt_positions = [
        (10, 15, 2, 5), (20, 5, 2, 5), (30, 40, 2, 4),
        (38, 5, 2, 6), (15, 20, 5, 2), (32, 15, 6, 2),
    ]
    for x, y, w, h in alt_positions:
        ax.add_patch(patches.Rectangle((x, y), w, h, fill=False,
                     edgecolor='black', linewidth=1, linestyle='--'))

    # Arrows showing possible movement
    movements = [
        ((11, 22), (11, 17)), ((21, 25), (21, 7)),
        ((31, 24), (31, 42)), ((39, 23), (39, 8)),
    ]
    for start, end in movements:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='black', linestyle='--'))

    # Central control system
    ax.add_patch(patches.Rectangle((42, 42), 6, 6, facecolor='white', edgecolor='black', linewidth=2))
    ax.text(45, 45, '30\nControl\nSystem', ha='center', va='center', fontsize=6, fontweight='bold')

    # Legend
    ax.add_patch(patches.Rectangle((2, -4), 2, 1, facecolor='#888888', edgecolor='black'))
    ax.text(5, -3.5, '= Fixed hedge section (12)', fontsize=8, va='center')
    ax.add_patch(patches.Rectangle((25, -4), 2, 1, facecolor='#333333', edgecolor='black'))
    ax.text(28, -3.5, '= Mobile hedge unit (10)', fontsize=8, va='center')
    ax.add_patch(patches.Rectangle((2, -2.5), 2, 0.8, fill=False, edgecolor='black', linestyle='--'))
    ax.text(5, -2, '= Alternate trough position (22)', fontsize=8, va='center')

    # Reference numerals
    ax.text(25, 51, '14 - Maze boundary', fontsize=8, ha='center')
    ax.text(25, -1, '20 - Positioning zone (typical)', fontsize=8, ha='center')

    ax.axis('off')
    save(fig, 'fig1_system_overview.png')


def fig2_mobile_unit_side():
    """Fig 2: Side cross-section of mobile hedge unit in trough (closed position)"""
    fig, axes = plt.subplots(2, 1, figsize=(10, 12))

    for idx, (ax, title, raised) in enumerate(zip(axes,
        ['FIG. 2A - Mobile Hedge Unit: CLOSED Position (In Trough)',
         'FIG. 2B - Mobile Hedge Unit: RAISED Position (Ready for Transit)'],
        [False, True])):

        ax.set_xlim(-2, 12)
        ax.set_ylim(-3, 14)
        ax.set_aspect('equal')
        ax.set_title(title, fontsize=11, fontweight='bold')

        ground_y = 0
        trough_depth = 1.5
        lift_height = 0.8 if raised else 0

        # Ground surface
        ax.fill_between([-2, 3], [ground_y, ground_y], [-0.3, -0.3], color='#cccccc')
        ax.fill_between([7, 12], [ground_y, ground_y], [-0.3, -0.3], color='#cccccc')
        ax.plot([-2, 3], [ground_y, ground_y], 'k-', linewidth=2)
        ax.plot([7, 12], [ground_y, ground_y], 'k-', linewidth=2)

        # Trough
        trough_bottom = ground_y - trough_depth
        ax.plot([3, 3], [ground_y, trough_bottom], 'k-', linewidth=2)
        ax.plot([7, 7], [ground_y, trough_bottom], 'k-', linewidth=2)
        ax.plot([3, 7], [trough_bottom, trough_bottom], 'k-', linewidth=2)
        ax.fill_between([3, 7], [trough_bottom]*2, [trough_bottom-0.3]*2, color='#999999')

        # Container base
        container_bottom = trough_bottom + 0.2 + lift_height
        container_top = container_bottom + 1.0

        ax.add_patch(patches.Rectangle((3.3, container_bottom), 3.4, 1.0,
                     facecolor='#aaaaaa', edgecolor='black', linewidth=1.5))

        # Wheels/rollers (shown if raised)
        if raised:
            for wx in [4.0, 6.0]:
                circle = plt.Circle((wx, container_bottom), 0.2, facecolor='black', edgecolor='black')
                ax.add_patch(circle)
            ax.annotate('26 - Roller assembly\n(exposed when raised)',
                       xy=(6.2, container_bottom), xytext=(8.5, container_bottom + 0.3),
                       fontsize=7, arrowprops=dict(arrowstyle='->', lw=1))
        else:
            for wx in [4.0, 6.0]:
                circle = plt.Circle((wx, container_bottom), 0.2, facecolor='black', edgecolor='black')
                ax.add_patch(circle)

        # Elevator mechanism
        elev_y = trough_bottom + 0.2
        ax.add_patch(patches.Rectangle((4.2, elev_y), 1.6, lift_height if raised else 0.15,
                     facecolor='#666666', edgecolor='black', linewidth=1, linestyle='-'))

        # Soil in container
        soil_top = container_top + 2.5
        ax.add_patch(patches.Rectangle((3.3, container_top), 3.4, 2.5,
                     facecolor='#8B7355', edgecolor='black', linewidth=1))

        # Hedge plant (simplified as rectangle with wavy top)
        hedge_bottom = soil_top
        hedge_top = hedge_bottom + 7
        ax.add_patch(patches.Rectangle((2.8, hedge_bottom), 4.4, 7,
                     facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))

        # Wavy top of hedge
        x_wave = np.linspace(2.8, 7.2, 50)
        y_wave = hedge_top + 0.3 * np.sin(x_wave * 4)
        ax.fill_between(x_wave, y_wave, hedge_top, color='#4a7c3f')
        ax.plot(x_wave, y_wave, color='#2d5a27', linewidth=1.5)

        # Reference numerals
        ax.annotate('10 - Mobile hedge unit', xy=(7.5, hedge_bottom + 3.5),
                   fontsize=8, fontweight='bold')
        ax.annotate('16 - Plant container', xy=(7, container_bottom + 0.5),
                   xytext=(8.5, container_bottom + 1.5), fontsize=7,
                   arrowprops=dict(arrowstyle='->', lw=1))
        ax.annotate('18 - Living hedge plant', xy=(7.2, hedge_bottom + 2),
                   xytext=(8.5, hedge_bottom + 3), fontsize=7,
                   arrowprops=dict(arrowstyle='->', lw=1))
        ax.annotate('22 - Receiving trough', xy=(3, trough_bottom + 0.5),
                   xytext=(-1.5, trough_bottom + 0.5), fontsize=7,
                   arrowprops=dict(arrowstyle='->', lw=1))
        ax.annotate('24 - Elevator mechanism', xy=(5, elev_y + 0.1),
                   xytext=(-1.5, elev_y + 1.5), fontsize=7,
                   arrowprops=dict(arrowstyle='->', lw=1))
        ax.annotate('28 - Path surface', xy=(1, ground_y),
                   xytext=(-1.5, ground_y + 0.8), fontsize=7,
                   arrowprops=dict(arrowstyle='->', lw=1))

        if raised:
            # Show lift distance
            ax.annotate('', xy=(8, trough_bottom + 0.2), xytext=(8, container_bottom),
                       arrowprops=dict(arrowstyle='<->', lw=1.5))
            ax.text(8.3, (trough_bottom + 0.2 + container_bottom)/2, '~5"', fontsize=8)

        # Dimension line for hedge height
        ax.annotate('', xy=(-1, ground_y), xytext=(-1, hedge_top),
                   arrowprops=dict(arrowstyle='<->', lw=1))
        ax.text(-1.8, (ground_y + hedge_top)/2, '8-15\nfeet', fontsize=7, ha='center', va='center')

        ax.axis('off')

    fig.tight_layout()
    save(fig, 'fig2_mobile_unit_side.png')


def fig3_positioning_zone():
    """Fig 3: Top view of positioning zone with troughs and movement paths"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.set_xlim(-2, 22)
    ax.set_ylim(-2, 22)
    ax.set_aspect('equal')
    ax.set_title('FIG. 3 - Positioning Zone (Top View)\nShowing Trough Positions and Movement Paths',
                fontsize=12, fontweight='bold')

    # Path surface background
    ax.add_patch(patches.Rectangle((0, 0), 20, 20, facecolor='#eeeeee', edgecolor='black', linewidth=2))

    # Fixed hedges (surrounding context)
    fixed = [(0, 0, 20, 1.5), (0, 18.5, 20, 1.5), (0, 0, 1.5, 20), (18.5, 0, 1.5, 20)]
    for x, y, w, h in fixed:
        ax.add_patch(patches.Rectangle((x, y), w, h, facecolor='#888888', edgecolor='black'))

    # Trough positions (6 positions in a grid-like pattern)
    troughs = [
        (4, 4, 3, 1.2, 'T1'), (4, 10, 3, 1.2, 'T2'), (4, 15, 3, 1.2, 'T3'),
        (12, 4, 3, 1.2, 'T4'), (12, 10, 3, 1.2, 'T5'), (12, 15, 3, 1.2, 'T6'),
    ]

    for x, y, w, h, label in troughs:
        ax.add_patch(patches.Rectangle((x, y), w, h, facecolor='white',
                     edgecolor='black', linewidth=1.5, linestyle='-'))
        ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=8)

    # Show one occupied trough (dark = hedge present)
    ax.add_patch(patches.Rectangle((4, 10), 3, 1.2, facecolor='#333333', edgecolor='black', linewidth=2))
    ax.text(5.5, 10.6, '10', ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    # Movement paths between troughs (dashed lines)
    connections = [
        ((5.5, 5.2), (5.5, 10)), ((5.5, 11.2), (5.5, 15)),
        ((7, 10.6), (12, 10.6)), ((7, 4.6), (12, 4.6)),
        ((5.5, 5.2), (12, 4.6)), ((13.5, 5.2), (13.5, 10)),
        ((13.5, 11.2), (13.5, 15)),
    ]
    for start, end in connections:
        ax.plot([start[0], end[0]], [start[1], end[1]], 'k--', linewidth=1, alpha=0.5)

    # Arrow showing example movement
    ax.annotate('', xy=(12, 10.6), xytext=(7, 10.6),
               arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    ax.text(9.5, 11.5, 'Example\nmovement', fontsize=8, ha='center', style='italic')

    # Labels
    ax.text(10, -1.5, '20 - Positioning zone boundary', fontsize=9, ha='center')
    ax.annotate('22 - Receiving trough (empty)', xy=(13.5, 4.6),
               xytext=(16, 3), fontsize=8, arrowprops=dict(arrowstyle='->', lw=1))
    ax.annotate('10 - Mobile unit (occupied)', xy=(5.5, 10.6),
               xytext=(-1, 8), fontsize=8, arrowprops=dict(arrowstyle='->', lw=1))
    ax.annotate('12 - Fixed hedge', xy=(10, 1),
               xytext=(10, -1), fontsize=8, arrowprops=dict(arrowstyle='->', lw=1))

    ax.axis('off')
    save(fig, 'fig3_positioning_zone.png')


def fig4_two_configurations():
    """Fig 4: Same maze, two different configurations"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    for idx, (ax, title) in enumerate(zip(axes,
        ['FIG. 4A - Configuration A', 'FIG. 4B - Configuration B'])):

        ax.set_xlim(0, 30)
        ax.set_ylim(0, 30)
        ax.set_aspect('equal')
        ax.set_title(title, fontsize=11, fontweight='bold')

        # Boundary
        ax.add_patch(patches.Rectangle((0, 0), 30, 30, fill=False, edgecolor='black', linewidth=2))

        # Fixed hedges (same in both)
        fixed = [
            (0, 0, 1, 30), (29, 0, 1, 30), (0, 0, 30, 1), (0, 29, 30, 1),
            (8, 1, 1, 12), (8, 17, 1, 12),
            (15, 5, 1, 10), (15, 20, 1, 9),
            (22, 1, 1, 15), (22, 20, 1, 9),
            (1, 14, 7, 1), (9, 8, 6, 1),
            (16, 14, 6, 1), (23, 20, 6, 1),
        ]
        for x, y, w, h in fixed:
            ax.add_patch(patches.Rectangle((x, y), w, h, facecolor='#888888', edgecolor='black', linewidth=0.5))

        # Mobile hedges (different positions per config)
        if idx == 0:  # Config A
            mobiles = [
                (8, 13, 1, 4), (15, 15, 1, 5),
                (22, 16, 1, 4), (9, 22, 6, 1),
            ]
        else:  # Config B
            mobiles = [
                (8, 8, 1, 5), (15, 1, 1, 4),
                (22, 22, 1, 4), (9, 16, 6, 1),
            ]

        for x, y, w, h in mobiles:
            ax.add_patch(patches.Rectangle((x, y), w, h, facecolor='#333333', edgecolor='black', linewidth=1))

        # Entry/exit markers
        ax.plot(15, 0.5, 'v', markersize=10, color='black')
        ax.text(15, -0.5, 'ENTRY', ha='center', fontsize=7)

        # Path trace (different route per config)
        if idx == 0:
            path_x = [15, 15, 12, 5, 5, 12, 12, 20, 20, 25, 25, 15]
            path_y = [1, 5, 5, 5, 18, 18, 22, 22, 16, 16, 25, 25]
        else:
            path_x = [15, 15, 20, 20, 12, 12, 5, 5, 12, 12, 25, 25]
            path_y = [1, 8, 8, 12, 12, 16, 16, 25, 25, 20, 20, 25]

        ax.plot(path_x, path_y, 'k:', linewidth=2, alpha=0.6)

        ax.text(3, -1, '12 = Fixed    ', fontsize=7, color='#888888', fontweight='bold')
        ax.text(15, -1, '10 = Mobile', fontsize=7, color='#333333', fontweight='bold')
        ax.axis('off')

    fig.suptitle('Same maze infrastructure, different mobile unit positions = different solution',
                fontsize=10, style='italic', y=0.02)
    fig.tight_layout()
    save(fig, 'fig4_two_configurations.png')


def fig5_guest_app():
    """Fig 5: Guest navigation app screens"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 7))

    modes = [
        ('FIG. 5A - Progressive Reveal', 'progressive'),
        ('FIG. 5B - Destination Guidance', 'destination'),
        ('FIG. 5C - Emergency Exit', 'emergency'),
    ]

    for ax, (title, mode) in zip(axes, modes):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 16)
        ax.set_aspect('equal')
        ax.set_title(title, fontsize=10, fontweight='bold')

        # Phone outline
        ax.add_patch(FancyBboxPatch((0.5, 0.5), 9, 15, boxstyle="round,pad=0.3",
                     facecolor='white', edgecolor='black', linewidth=2))

        # Screen area
        ax.add_patch(patches.Rectangle((1, 2), 8, 12, facecolor='#f5f0e0', edgecolor='black'))

        # Status bar
        ax.add_patch(patches.Rectangle((1, 14), 8, 1, facecolor='#333333'))
        ax.text(5, 14.5, 'Labyrinth Park', color='white', ha='center', fontsize=8, fontweight='bold')

        # Bottom bar
        ax.add_patch(patches.Rectangle((1, 1), 8, 1, facecolor='#333333'))
        ax.text(5, 1.5, mode.upper(), color='white', ha='center', fontsize=7)

        # Map content varies by mode
        cx, cy = 5, 8  # center

        if mode == 'progressive':
            # Visible area (bright)
            circle = plt.Circle((cx, cy), 2.5, facecolor='#f5f0e0', edgecolor='none')
            ax.add_patch(circle)
            # Fog of war (darker around edges)
            for r in np.linspace(2.5, 5, 10):
                alpha = min(0.6, (r - 2.5) / 3)
                circle = plt.Circle((cx, cy), r, facecolor='none',
                                   edgecolor='#8B7355', alpha=alpha, linewidth=3)
                ax.add_patch(circle)
            # Path lines in visible area
            ax.plot([3, 5, 5, 7], [7, 7, 9, 9], 'k-', linewidth=2)
            ax.plot([5, 5], [7, 5.5], 'k-', linewidth=2)
            ax.plot([3.5, 5], [9, 9], 'k-', linewidth=2)
            # You-are-here dot
            ax.plot(5, 7, 'o', markersize=10, color='red')
            ax.text(5.8, 7, 'You', fontsize=7, color='red')
            # Faded edges
            ax.text(5, 4, '?', fontsize=20, ha='center', color='#ccbbaa')
            ax.text(7.5, 8, '?', fontsize=16, ha='center', color='#ccbbaa')

        elif mode == 'destination':
            # Show path to destination
            ax.plot([5, 5, 3, 3, 5, 5, 7, 7], [3, 5, 5, 8, 8, 10, 10, 12], 'k--', linewidth=2)
            ax.plot(5, 3, 'o', markersize=10, color='red')
            ax.plot(7, 12, '*', markersize=15, color='black')
            ax.text(5.8, 3, 'You', fontsize=7, color='red')
            ax.text(7.5, 12.3, 'Rose\nGarden', fontsize=6, va='bottom')
            # Minimal surroundings
            ax.plot([4, 4], [4, 9], 'k-', linewidth=1.5, alpha=0.3)
            ax.plot([6, 6], [6, 11], 'k-', linewidth=1.5, alpha=0.3)

        elif mode == 'emergency':
            # Bold red arrow to exit
            ax.annotate('', xy=(5, 13), xytext=(5, 4),
                       arrowprops=dict(arrowstyle='->', lw=4, color='red'))
            ax.text(5, 8, 'EXIT\nTHIS WAY', fontsize=14, ha='center', va='center',
                   color='red', fontweight='bold')
            ax.text(5, 3, '125m to\nnearest exit', fontsize=8, ha='center', color='red')
            ax.plot(5, 4, 'o', markersize=10, color='red')

        ax.axis('off')

    fig.tight_layout()
    save(fig, 'fig5_guest_app.png')


def fig6_emergency():
    """Fig 6: Emergency configuration - all hedges open for direct egress"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    for idx, (ax, title) in enumerate(zip(axes,
        ['FIG. 6A - Normal Configuration', 'FIG. 6B - Emergency Egress Mode'])):

        ax.set_xlim(0, 30)
        ax.set_ylim(0, 30)
        ax.set_aspect('equal')
        ax.set_title(title, fontsize=11, fontweight='bold')

        ax.add_patch(patches.Rectangle((0, 0), 30, 30, fill=False, edgecolor='black', linewidth=2))

        # Fixed hedges
        fixed = [
            (0, 0, 1, 30), (29, 0, 1, 30), (0, 0, 30, 1), (0, 29, 30, 1),
            (8, 1, 1, 12), (8, 17, 1, 12),
            (15, 5, 1, 10), (15, 20, 1, 9),
            (22, 1, 1, 15), (22, 20, 1, 9),
        ]
        for x, y, w, h in fixed:
            ax.add_patch(patches.Rectangle((x, y), w, h, facecolor='#888888', edgecolor='black', linewidth=0.5))

        if idx == 0:  # Normal
            mobiles = [
                (8, 13, 1, 4), (15, 15, 1, 5),
                (22, 16, 1, 4), (1, 14, 7, 1),
            ]
            for x, y, w, h in mobiles:
                ax.add_patch(patches.Rectangle((x, y), w, h, facecolor='#333333', edgecolor='black'))
        else:  # Emergency - mobile units moved to open paths
            # Show empty trough positions where hedges WERE
            troughs = [(8, 13, 1, 4), (15, 15, 1, 5), (22, 16, 1, 4), (1, 14, 7, 1)]
            for x, y, w, h in troughs:
                ax.add_patch(patches.Rectangle((x, y), w, h, fill=False,
                             edgecolor='black', linewidth=1, linestyle=':'))

            # Direct egress paths (bold red arrows)
            exits = [(15, 0.5), (0.5, 15), (29.5, 15), (15, 29.5)]
            # Arrows from center to each exit
            for ex, ey in exits:
                ax.annotate('', xy=(ex, ey), xytext=(15, 15),
                           arrowprops=dict(arrowstyle='->', lw=3, color='red'))

            ax.text(15, 15, 'CLEAR\nEGRESS', ha='center', va='center',
                   fontsize=10, fontweight='bold', color='red')

        # Exit markers
        for x, y, label in [(15, 0, 'EXIT'), (15, 30, 'EXIT'), (0, 15, 'EXIT'), (30, 15, 'EXIT')]:
            ax.text(x, y, label, ha='center', va='center', fontsize=7,
                   fontweight='bold', color='red' if idx == 1 else 'black',
                   bbox=dict(boxstyle='round', facecolor='white', edgecolor='red' if idx == 1 else 'black'))

        ax.axis('off')

    fig.tight_layout()
    save(fig, 'fig6_emergency.png')


def fig7_anti_aerial():
    """Fig 7: Cross-section showing anti-aerial features"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 7))
    ax.set_xlim(-1, 25)
    ax.set_ylim(-4, 12)
    ax.set_aspect('equal')
    ax.set_title('FIG. 7 - Anti-Aerial-Observation Features (Cross Section)', fontsize=12, fontweight='bold')

    # Ground level
    ax.plot([-1, 25], [0, 0], 'k-', linewidth=2)
    ax.fill_between([-1, 25], [0, 0], [-0.5, -0.5], color='#cccccc')

    # Section A: Pergola/canopy coverage
    # Hedges
    ax.add_patch(patches.Rectangle((1, 0), 0.8, 5, facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    ax.add_patch(patches.Rectangle((4.2, 0), 0.8, 5, facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    # Pergola top
    ax.add_patch(patches.Rectangle((0.5, 5), 5, 0.3, facecolor='#8B7355', edgecolor='black'))
    # Vine growth on pergola
    x_vine = np.linspace(0.5, 5.5, 40)
    y_vine = 5.3 + 0.4 * np.abs(np.sin(x_vine * 3))
    ax.fill_between(x_vine, 5.3, y_vine, color='#4a7c3f', alpha=0.7)
    # Path underneath
    ax.text(3, 2.5, 'PATH\n(hidden\nfrom\nabove)', ha='center', fontsize=7)
    ax.text(3, -1, 'A: Pergola coverage', ha='center', fontsize=8, fontweight='bold')
    # Drone eye view arrow
    ax.annotate('Drone sees\nsolid canopy', xy=(3, 6), xytext=(3, 9),
               fontsize=7, ha='center', arrowprops=dict(arrowstyle='->', lw=1))

    # Section B: False path (hedge appears open from above)
    # Raised ground level hedge
    ax.add_patch(patches.Rectangle((8, 0), 0.8, 5, facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    ax.add_patch(patches.Rectangle((12.2, 0), 0.8, 5, facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    # Sunken area between
    ax.fill_between([8.8, 12.2], [0, 0], [-2.5, -2.5], color='#dddddd', edgecolor='black', linewidth=1)
    # Short hedge growing from sunken floor
    ax.add_patch(patches.Rectangle((9.5, -2.5), 2, 3, facecolor='#4a7c3f', edgecolor='#2d5a27'))
    ax.text(10.5, -1, 'Short\nhedge', ha='center', fontsize=6, color='white')
    # Top of short hedge is at 0.5 - below the tall hedges
    ax.annotate('Drone sees gap\n(appears open)', xy=(10.5, 0.5), xytext=(10.5, 9),
               fontsize=7, ha='center', arrowprops=dict(arrowstyle='->', lw=1, linestyle='--'))
    ax.text(10.5, 7.5, 'BUT: no ground-\nlevel access!', ha='center', fontsize=7, color='red')
    ax.text(10.5, -3.5, 'B: False path\n(sunken hedge)', ha='center', fontsize=8, fontweight='bold')

    # Section C: Tunnel connection
    ax.add_patch(patches.Rectangle((16, 0), 0.8, 5, facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    ax.add_patch(patches.Rectangle((20.2, 0), 0.8, 5, facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    # Tunnel underground
    ax.add_patch(patches.Rectangle((15, -3), 7, 2.5, facecolor='#999999', edgecolor='black', linewidth=1.5))
    ax.text(18.5, -1.8, 'TUNNEL\n(underground)', ha='center', fontsize=7, fontweight='bold')
    # Ground fill over tunnel
    ax.fill_between([15, 22], [0, 0], [-0.5, -0.5], color='#cccccc')
    ax.plot([15, 22], [0, 0], 'k-', linewidth=2)
    # Entrance arrows
    ax.annotate('', xy=(16.5, -0.5), xytext=(16.5, -2),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(20, -0.5), xytext=(20, -2),
               arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('Drone sees\nseparate sections', xy=(18.5, 5.5), xytext=(18.5, 9),
               fontsize=7, ha='center', arrowprops=dict(arrowstyle='->', lw=1))
    ax.text(18.5, 7.5, 'Actually connected\nunderground', ha='center', fontsize=7, color='red')
    ax.text(18.5, -3.8, 'C: Tunnel connection', ha='center', fontsize=8, fontweight='bold')

    ax.axis('off')
    save(fig, 'fig7_anti_aerial.png')


def fig8_system_architecture():
    """Fig 8: System architecture block diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 18)
    ax.set_aspect('equal')
    ax.set_title('FIG. 8 - System Architecture', fontsize=14, fontweight='bold')

    def box(x, y, w, h, label, ref, color='white'):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2",
                     facecolor=color, edgecolor='black', linewidth=1.5))
        ax.text(x + w/2, y + h/2 + 0.2, label, ha='center', va='center',
               fontsize=8, fontweight='bold')
        ax.text(x + w/2, y + h/2 - 0.3, ref, ha='center', va='center',
               fontsize=7, style='italic')

    # Central control system
    box(8, 14, 8, 3, 'CENTRAL CONTROL\nSYSTEM', '(30)', '#dddddd')

    # Sub-components of control
    box(1, 10, 5, 2.5, 'Configuration\nEngine', '(32)', '#eeeeee')
    box(7, 10, 5, 2.5, 'Scheduling\nSystem', '(34)', '#eeeeee')
    box(13, 10, 5, 2.5, 'Safety\nValidation', '(36)', '#eeeeee')
    box(19, 10, 4, 2.5, 'Position\nMonitor', '(38)', '#eeeeee')

    # Mobile hedge units
    for i in range(4):
        x = 2 + i * 5.5
        box(x, 5.5, 4, 2.5, f'Mobile Hedge\nUnit {i+1}', '(10)', '#ccddcc')

    # Guest app
    box(1, 1, 5, 3, 'Guest Navigation\nApplication', '(40)')

    # Emergency system
    box(8, 1, 5, 3, 'Emergency\nAccess System', '(42)')

    # Projected guidance
    box(15, 1, 5, 3, 'Projected\nGuidance', '(44)')

    # Arrows from control to sub-components
    for x in [3.5, 9.5, 15.5, 21]:
        ax.annotate('', xy=(x, 12.5), xytext=(12, 14),
                   arrowprops=dict(arrowstyle='->', lw=1))

    # Arrows from control to mobile units (wireless)
    for i in range(4):
        x = 4 + i * 5.5
        ax.annotate('', xy=(x, 8), xytext=(12, 10),
                   arrowprops=dict(arrowstyle='<->', lw=1, linestyle='--'))

    # Arrows from control to guest app, emergency, projection
    for x in [3.5, 10.5, 17.5]:
        ax.annotate('', xy=(x, 4), xytext=(12, 10),
                   arrowprops=dict(arrowstyle='->', lw=1, linestyle=':'))

    # Wireless symbol
    ax.text(12, 9.2, '~ wireless ~', ha='center', fontsize=7, style='italic')

    ax.axis('off')
    save(fig, 'fig8_system_architecture.png')


if __name__ == '__main__':
    print("Generating patent drawings...")
    fig1_system_overview()
    fig2_mobile_unit_side()
    fig3_positioning_zone()
    fig4_two_configurations()
    fig5_guest_app()
    fig6_emergency()
    fig7_anti_aerial()
    fig8_system_architecture()
    print(f"\nAll 8 figures saved to {os.path.abspath(OUT_DIR)}")
    print("Ready for provisional patent filing!")
