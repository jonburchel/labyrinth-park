"""
Additional patent drawings for terrace transit, planter cross-section,
trough cross-section, and depot station.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), 'drawings')
os.makedirs(OUT_DIR, exist_ok=True)

def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  Saved {name}")


def fig9_terrace_transit():
    """4-panel terrace transit sequence"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()

    titles = [
        'FIG. 9A - Step 1: Planter Seated in Lower Trough',
        'FIG. 9B - Step 2: Elevator Raises to Upper Level',
        'FIG. 9C - Step 3: Powered Roller Transfer',
        'FIG. 9D - Step 4: Seated in Upper Trough'
    ]

    for idx, (ax, title) in enumerate(zip(axes, titles)):
        ax.set_xlim(-1, 16)
        ax.set_ylim(-4, 10)
        ax.set_aspect('equal')
        ax.set_title(title, fontsize=9, fontweight='bold')

        # Upper terrace surface (right side, higher)
        upper_y = 2.0
        ax.fill_between([8, 16], [upper_y]*2, [upper_y-0.3]*2, color='#cccccc')
        ax.plot([8, 16], [upper_y]*2, 'k-', linewidth=2)

        # Lower terrace surface (left side)
        lower_y = 0
        ax.fill_between([-1, 7], [lower_y]*2, [lower_y-0.3]*2, color='#cccccc')
        ax.plot([-1, 7], [lower_y]*2, 'k-', linewidth=2)

        # Terrace wall
        ax.fill_between([7, 8], [upper_y]*2, [lower_y]*2, color='#999999')
        ax.plot([7, 7], [lower_y, upper_y], 'k-', linewidth=2)
        ax.plot([8, 8], [lower_y, upper_y], 'k-', linewidth=2)

        # Lower trough
        lt_depth = 1.5
        ax.plot([2, 2], [lower_y, lower_y - lt_depth], 'k-', linewidth=1.5)
        ax.plot([6, 6], [lower_y, lower_y - lt_depth], 'k-', linewidth=1.5)
        ax.plot([2, 6], [lower_y - lt_depth]*2, 'k-', linewidth=1.5)

        # Upper trough
        ax.plot([9, 9], [upper_y, upper_y - lt_depth], 'k-', linewidth=1.5)
        ax.plot([13, 13], [upper_y, upper_y - lt_depth], 'k-', linewidth=1.5)
        ax.plot([9, 13], [upper_y - lt_depth]*2, 'k-', linewidth=1.5)

        # Planter dimensions
        pw = 3.4
        ph = 0.6
        hedge_h = 5.0

        if idx == 0:  # Seated in lower trough
            # Lower elevator (retracted)
            ax.add_patch(patches.Rectangle((2.5, lower_y - lt_depth + 0.1), 3, 0.3,
                         facecolor='#666', edgecolor='black', hatch='///'))
            # Planter in lower trough
            py = lower_y - lt_depth + 0.5
            ax.add_patch(patches.Rectangle((2.3, py), pw, ph, facecolor='#aaa', edgecolor='black'))
            # Growing medium
            ax.add_patch(patches.Rectangle((2.3, py + ph), pw, 0.5, facecolor='#8B7355', edgecolor='black'))
            # Hedge
            ax.add_patch(patches.Rectangle((2, py + ph + 0.5), 4, hedge_h, facecolor='#4a7c3f', edgecolor='#2d5a27'))
            ax.annotate('Planter seated\nin lower trough', xy=(0, py+1), fontsize=7, fontweight='bold')

            # Upper trough empty
            ax.text(11, upper_y - 0.8, 'Empty', ha='center', fontsize=7, color='gray')

        elif idx == 1:  # Elevator raised
            # Lower elevator (extended to upper level)
            elev_top = upper_y
            ax.add_patch(patches.Rectangle((2.5, lower_y - lt_depth + 0.1), 3, 
                         elev_top - (lower_y - lt_depth + 0.1),
                         facecolor='#666', edgecolor='black', hatch='///'))
            # Roller surface on top of elevator
            ax.add_patch(patches.Rectangle((2.3, elev_top - 0.15), pw, 0.15,
                         facecolor='#ffcc00', edgecolor='black', linewidth=1))
            # Planter at upper level
            py = elev_top
            ax.add_patch(patches.Rectangle((2.3, py), pw, ph, facecolor='#aaa', edgecolor='black'))
            ax.add_patch(patches.Rectangle((2.3, py + ph), pw, 0.5, facecolor='#8B7355', edgecolor='black'))
            ax.add_patch(patches.Rectangle((2, py + ph + 0.5), 4, hedge_h, facecolor='#4a7c3f', edgecolor='#2d5a27'))

            # Receiving elevator in upper trough (raised, waiting)
            ax.add_patch(patches.Rectangle((9.3, upper_y - lt_depth + 0.1), 3, lt_depth - 0.25,
                         facecolor='#888', edgecolor='black', hatch='///'))
            ax.add_patch(patches.Rectangle((9.3, upper_y - 0.15), pw, 0.15,
                         facecolor='#ffcc00', edgecolor='black', linewidth=1))
            
            # Dimension arrow
            ax.annotate('', xy=(1.5, lower_y), xytext=(1.5, upper_y),
                       arrowprops=dict(arrowstyle='<->', lw=1.5))
            ax.text(0.5, (lower_y + upper_y)/2, '18-24"', fontsize=7, ha='center')
            
            ax.annotate('Roller\nconveyor', xy=(3.5, elev_top-0.1), xytext=(-0.5, elev_top+0.5),
                       fontsize=6, arrowprops=dict(arrowstyle='->', lw=0.8), color='#996600')
            ax.annotate('Receiving\nrollers', xy=(10.5, upper_y-0.1), xytext=(14, upper_y+0.5),
                       fontsize=6, arrowprops=dict(arrowstyle='->', lw=0.8), color='#996600')

        elif idx == 2:  # Transfer in progress
            # Lower elevator still extended
            ax.add_patch(patches.Rectangle((2.5, lower_y - lt_depth + 0.1), 3,
                         upper_y - (lower_y - lt_depth + 0.1),
                         facecolor='#666', edgecolor='black', hatch='///'))
            ax.add_patch(patches.Rectangle((2.3, upper_y - 0.15), pw, 0.15,
                         facecolor='#ffcc00', edgecolor='black'))
            
            # Receiving elevator
            ax.add_patch(patches.Rectangle((9.3, upper_y - lt_depth + 0.1), 3, lt_depth - 0.25,
                         facecolor='#888', edgecolor='black', hatch='///'))
            ax.add_patch(patches.Rectangle((9.3, upper_y - 0.15), pw, 0.15,
                         facecolor='#ffcc00', edgecolor='black'))

            # Planter MID-TRANSFER (straddling the boundary)
            px = 6.5  # partially over
            py = upper_y
            ax.add_patch(patches.Rectangle((px, py), pw, ph, facecolor='#aaa', edgecolor='black'))
            ax.add_patch(patches.Rectangle((px, py + ph), pw, 0.5, facecolor='#8B7355', edgecolor='black'))
            ax.add_patch(patches.Rectangle((px - 0.3, py + ph + 0.5), 4, hedge_h, facecolor='#4a7c3f', edgecolor='#2d5a27'))

            # Transfer arrow
            ax.annotate('', xy=(11, upper_y + 0.3), xytext=(5, upper_y + 0.3),
                       arrowprops=dict(arrowstyle='->', lw=2.5, color='red'))
            ax.text(8, upper_y + 0.8, 'POWERED\nTRANSFER', ha='center', fontsize=8, 
                   fontweight='bold', color='red')
            
            # 2mm settling annotation
            ax.annotate('2mm settle', xy=(11, upper_y - 0.2), fontsize=6, color='#666')

        elif idx == 3:  # Seated in upper trough
            # Lower elevator retracted, empty
            ax.add_patch(patches.Rectangle((2.5, lower_y - lt_depth + 0.1), 3, 0.3,
                         facecolor='#666', edgecolor='black', hatch='///'))
            ax.text(4, lower_y - 0.8, 'Empty', ha='center', fontsize=7, color='gray')

            # Planter seated in upper trough
            py = upper_y - lt_depth + 0.5
            ax.add_patch(patches.Rectangle((9.3, upper_y - lt_depth + 0.1), 3, 0.3,
                         facecolor='#888', edgecolor='black', hatch='///'))
            ax.add_patch(patches.Rectangle((9.3, py), pw, ph, facecolor='#aaa', edgecolor='black'))
            ax.add_patch(patches.Rectangle((9.3, py + ph), pw, 0.5, facecolor='#8B7355', edgecolor='black'))
            ax.add_patch(patches.Rectangle((9, py + ph + 0.5), 4, hedge_h, facecolor='#4a7c3f', edgecolor='#2d5a27'))

            ax.annotate('Planter seated\nin upper trough', xy=(14, py+1), fontsize=7, fontweight='bold')
            ax.text(11, upper_y + hedge_h - 1, 'COMPLETE', fontsize=9, ha='center',
                   fontweight='bold', color='green')

        ax.axis('off')

    fig.suptitle('FIG. 9 - Terrace Transit Sequence (Vertical Lift + Powered Roller Transfer)',
                fontsize=11, fontweight='bold', y=1.01)
    fig.tight_layout()
    save(fig, 'fig9_terrace_transit.png')


def fig10_planter_crosssection():
    """Detailed planter cross-section with materials"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax.set_xlim(-4, 14)
    ax.set_ylim(-3, 14)
    ax.set_aspect('equal')
    ax.set_title('FIG. 10 - Planter Cross-Section with Materials', fontsize=12, fontweight='bold')

    # Container walls (concrete)
    wall_t = 0.4
    inner_w = 3.0
    depth = 3.0
    outer_left = 3
    outer_right = outer_left + inner_w + 2*wall_t

    # Outer container
    ax.add_patch(patches.Rectangle((outer_left, 0), inner_w + 2*wall_t, depth,
                 facecolor='#bbbbbb', edgecolor='black', linewidth=2))
    # Inner void
    ax.add_patch(patches.Rectangle((outer_left + wall_t, wall_t + 0.3), inner_w, depth - wall_t - 0.3,
                 facecolor='white', edgecolor='black', linewidth=1))

    # Wicking mat at bottom
    ax.add_patch(patches.Rectangle((outer_left + wall_t, wall_t), inner_w, 0.15,
                 facecolor='#6699cc', edgecolor='black'))
    ax.add_patch(patches.Rectangle((outer_left + wall_t, wall_t + 0.15), inner_w, 0.15,
                 facecolor='#99ccff', edgecolor='black'))

    # LECA growing medium
    ax.add_patch(patches.Rectangle((outer_left + wall_t, wall_t + 0.3), inner_w, depth - wall_t - 0.5,
                 facecolor='#D2691E', edgecolor='black', linewidth=0.5))
    # Draw some circles to represent LECA pellets
    for i in range(15):
        for j in range(8):
            cx = outer_left + wall_t + 0.2 + i * (inner_w/15)
            cy = wall_t + 0.5 + j * ((depth - wall_t - 0.7)/8)
            r = 0.08
            ax.add_patch(plt.Circle((cx, cy), r, facecolor='#C4A265', edgecolor='#8B6914', linewidth=0.3))

    # Root management ribs (air-pruning)
    for y in [1.0, 1.8, 2.3]:
        ax.plot([outer_left + wall_t, outer_left + wall_t + 0.15], [y, y], 'k-', linewidth=2)
        ax.plot([outer_right - wall_t - 0.15, outer_right - wall_t], [y, y], 'k-', linewidth=2)

    # Lift hooks (both sides)
    for side_x in [outer_left - 0.1, outer_right + 0.1]:
        hook_dir = -1 if side_x < 5 else 1
        ax.add_patch(patches.FancyArrowPatch((side_x, 2.0), (side_x - hook_dir*0.4, 2.3),
                     arrowstyle='-', linewidth=3, color='#333'))
        ax.add_patch(plt.Circle((side_x - hook_dir*0.4, 2.3), 0.1, facecolor='#333'))

    # Ball transfer units at bottom
    for bx in [outer_left + 0.5, outer_left + inner_w/2 + wall_t, outer_right - 0.5]:
        ax.add_patch(plt.Circle((bx, -0.15), 0.18, facecolor='#555', edgecolor='black'))
        ax.add_patch(plt.Circle((bx, -0.15), 0.1, facecolor='#999', edgecolor='black'))

    # Hedge above
    hedge_bottom = depth + 0.2
    hedge_h = 8.0
    ax.add_patch(patches.Rectangle((outer_left - 0.5, hedge_bottom), inner_w + 2*wall_t + 1, hedge_h,
                 facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    x_wave = np.linspace(outer_left - 0.5, outer_right + 0.5, 40)
    y_wave = hedge_bottom + hedge_h + 0.3 * np.sin(x_wave * 3)
    ax.fill_between(x_wave, y_wave, hedge_bottom + hedge_h, color='#4a7c3f')
    ax.plot(x_wave, y_wave, color='#2d5a27', linewidth=1.5)

    # Labels
    labels = [
        ((-3, 12), (outer_left + 1, hedge_bottom + 4), '18 - Hedge plant\n(8-15 ft)'),
        ((-3, depth - 0.5), (outer_left + wall_t + 0.3, depth - 0.8), '50 - LECA growing\nmedium (8-16mm)'),
        ((-3, wall_t + 0.15), (outer_left + wall_t + 0.3, wall_t + 0.15), '52 - Wicking mat\n(polyester, 5mm)'),
        ((-3, 1.8), (outer_left + wall_t + 0.1, 1.8), '54 - Root management\nribs (air-pruning)'),
        ((-3, -0.2), (outer_left + 0.5, -0.15), '26 - Ball transfer\nunits (IP67)'),
        ((10, 1.5), (outer_right, 1.5), '16 - Concrete container\n(5,000 psi, 3" walls)'),
        ((10, 2.3), (outer_right + 0.1, 2.3), '56 - Lift hook points\n(standardized)'),
        ((10, depth + 0.1), (outer_right - 0.5, depth), '58 - Root access panel\n(removable)'),
    ]
    for text_pos, target, label in labels:
        ax.annotate(label, xy=target, xytext=text_pos, fontsize=7,
                   arrowprops=dict(arrowstyle='->', lw=0.8),
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='gray', alpha=0.9))

    # Dimensions
    ax.annotate('', xy=(-1.5, 0), xytext=(-1.5, depth),
               arrowprops=dict(arrowstyle='<->', lw=1))
    ax.text(-2.2, depth/2, '2.5-3.0\nft', fontsize=7, ha='center', va='center')

    ax.annotate('', xy=(outer_left, -1.5), xytext=(outer_right, -1.5),
               arrowprops=dict(arrowstyle='<->', lw=1))
    ax.text((outer_left + outer_right)/2, -2.2, '3.0-4.0 ft wide', fontsize=7, ha='center')

    ax.axis('off')
    save(fig, 'fig10_planter_crosssection.png')


def fig11_trough_crosssection():
    """Trough cross-section with sub-channel and materials"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(-3, 15)
    ax.set_ylim(-5, 4)
    ax.set_aspect('equal')
    ax.set_title('FIG. 11 - Trough Infrastructure Cross-Section', fontsize=12, fontweight='bold')

    # Ground surface
    ax.fill_between([-3, 2], [0]*2, [-0.2]*2, color='#cccccc')
    ax.fill_between([10, 15], [0]*2, [-0.2]*2, color='#cccccc')
    ax.plot([-3, 2], [0]*2, 'k-', linewidth=2)
    ax.plot([10, 15], [0]*2, 'k-', linewidth=2)

    # Path surface labels
    ax.text(0, 0.3, 'PATH', fontsize=7, ha='center', color='#666')
    ax.text(12.5, 0.3, 'PATH', fontsize=7, ha='center', color='#666')

    # Main trough
    trough_l = 2
    trough_r = 10
    trough_d = 2.5
    # Concrete walls
    wall_t = 0.4
    ax.add_patch(patches.Rectangle((trough_l, -trough_d), wall_t, trough_d,
                 facecolor='#999', edgecolor='black', linewidth=1.5))
    ax.add_patch(patches.Rectangle((trough_r - wall_t, -trough_d), wall_t, trough_d,
                 facecolor='#999', edgecolor='black', linewidth=1.5))
    # Trough floor
    ax.add_patch(patches.Rectangle((trough_l, -trough_d - wall_t), trough_r - trough_l, wall_t,
                 facecolor='#999', edgecolor='black', linewidth=1.5))

    # Sub-channel (water) below trough
    sub_top = -trough_d - wall_t
    sub_h = 0.6
    ax.add_patch(patches.Rectangle((trough_l + 1, sub_top - sub_h), trough_r - trough_l - 2, sub_h,
                 facecolor='#4488cc', edgecolor='black', linewidth=1, alpha=0.5))
    ax.text(6, sub_top - sub_h/2, 'WATER', ha='center', fontsize=7, color='white', fontweight='bold')

    # Bearing plate (steel, machined)
    bp_y = -trough_d + 0.05
    ax.add_patch(patches.Rectangle((trough_l + wall_t + 0.5, bp_y), 2, 0.1,
                 facecolor='#ffcc00', edgecolor='black', linewidth=1))
    ax.add_patch(patches.Rectangle((trough_r - wall_t - 2.5, bp_y), 2, 0.1,
                 facecolor='#ffcc00', edgecolor='black', linewidth=1))

    # Power contacts in trough floor
    for px in [4, 6, 8]:
        ax.add_patch(patches.Rectangle((px - 0.15, -trough_d + 0.02), 0.3, 0.08,
                     facecolor='#cc6600', edgecolor='black'))

    # Elevator bay (deeper recess)
    bay_w = 4
    bay_d = 1.5
    bay_l = trough_l + (trough_r - trough_l)/2 - bay_w/2
    bay_r = bay_l + bay_w
    ax.add_patch(patches.Rectangle((bay_l, sub_top - sub_h - bay_d), bay_w, bay_d,
                 facecolor='#ddd', edgecolor='black', linewidth=1, linestyle='--'))
    ax.text(6, sub_top - sub_h - bay_d/2, 'ELEVATOR BAY\n(when installed)', 
           ha='center', fontsize=6, color='#666', style='italic')

    # Conduit corridor
    for cy in [-3.5, -3.8]:
        ax.add_patch(plt.Circle((trough_l + 0.7, cy), 0.15, facecolor='#ff6600', edgecolor='black'))
        ax.add_patch(plt.Circle((trough_r - 0.7, cy), 0.15, facecolor='#ff6600', edgecolor='black'))

    # Surface cover (when trough empty, shown as dashed outline above)
    ax.add_patch(patches.Rectangle((trough_l, -0.15), trough_r - trough_l, 0.15,
                 facecolor='none', edgecolor='black', linewidth=1, linestyle=':'))
    ax.text(6, 0.5, '(surface cover when\ntrough unoccupied)', ha='center', fontsize=6, 
           color='gray', style='italic')

    # Labels
    labels = [
        ((-2.5, -1), (trough_l + 0.2, -1), '22 - Trough wall\n(5,000 psi concrete)'),
        ((-2.5, -2.5), (trough_l + 0.2, -trough_d + 0.1), '60 - Trough floor'),
        ((12.5, bp_y), (trough_r - wall_t - 0.5, bp_y + 0.05), '62 - Steel bearing plate\n(A36, machined +/-0.5mm)'),
        ((12.5, -trough_d + 0.05), (8.15, -trough_d + 0.06), '64 - Power contacts\n(blind-mate, IP67)'),
        ((12.5, sub_top - sub_h/2), (trough_r - 1, sub_top - sub_h/2), '66 - Sub-channel\n(nutrient water loop)'),
        ((-2.5, -3.6), (trough_l + 0.7, -3.5), '68 - Conduit corridor\n(power, data, fiber)'),
        ((12.5, -3.8), (bay_r, sub_top - sub_h - bay_d/2), '70 - Elevator bay recess\n(drop-in module)'),
    ]
    for text_pos, target, label in labels:
        ax.annotate(label, xy=target, xytext=text_pos, fontsize=7,
                   arrowprops=dict(arrowstyle='->', lw=0.8),
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='gray', alpha=0.9))

    ax.axis('off')
    save(fig, 'fig11_trough_crosssection.png')


def fig12_depot_station():
    """Depot station layout in utility tunnel"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(-1, 25)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    ax.set_title('FIG. 12 - Depot Station in Utility Tunnel (Plan View)', fontsize=12, fontweight='bold')

    # Tunnel walls
    ax.add_patch(patches.Rectangle((0, 0), 24, 10, facecolor='#f0f0f0', edgecolor='black', linewidth=2))

    # Label
    ax.text(12, 11, 'UTILITY TUNNEL LEVEL (BELOW GRADE)', ha='center', fontsize=9, fontweight='bold')

    # Service bay 1 (planter being serviced)
    ax.add_patch(patches.Rectangle((1, 6), 6, 3, facecolor='#eee', edgecolor='black', linewidth=1.5))
    ax.text(4, 8.7, 'SERVICE BAY 1', fontsize=7, ha='center', fontweight='bold')
    # Planter in bay
    ax.add_patch(patches.Rectangle((2, 6.5), 4, 2, facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    ax.text(4, 7.5, 'PLANTER\n(under service)', ha='center', fontsize=6, color='white')

    # Service bay 2 (empty, waiting)
    ax.add_patch(patches.Rectangle((8, 6), 6, 3, facecolor='#eee', edgecolor='black', linewidth=1.5))
    ax.text(11, 8.7, 'SERVICE BAY 2', fontsize=7, ha='center', fontweight='bold')
    ax.text(11, 7.5, '(available)', ha='center', fontsize=7, color='gray')

    # Reserve storage
    ax.add_patch(patches.Rectangle((15, 6), 8, 3, facecolor='#ddd', edgecolor='black', linewidth=1.5))
    ax.text(19, 8.7, 'RESERVE STORAGE', fontsize=7, ha='center', fontweight='bold')
    # Stored planters
    for px in [16, 18.5, 21]:
        ax.add_patch(patches.Rectangle((px, 6.5), 1.5, 2, facecolor='#5a8c4f', edgecolor='black'))

    # Transit track (main tunnel)
    ax.add_patch(patches.Rectangle((0, 1.5), 24, 3.5, facecolor='#e8e8e8', edgecolor='black', linewidth=1))
    ax.text(12, 3.25, 'MAIN TRANSIT CORRIDOR', ha='center', fontsize=8, fontweight='bold')

    # Planter in transit (arriving)
    ax.add_patch(patches.Rectangle((1, 2), 4, 2, facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    ax.text(3, 3, 'ARRIVING', ha='center', fontsize=6, color='white', fontweight='bold')
    ax.annotate('', xy=(5.5, 3), xytext=(1, 3),
               arrowprops=dict(arrowstyle='->', lw=2, color='red'))

    # Planter departing
    ax.add_patch(patches.Rectangle((18, 2), 4, 2, facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    ax.text(20, 3, 'DEPARTING', ha='center', fontsize=6, color='white', fontweight='bold')
    ax.annotate('', xy=(23, 3), xytext=(22, 3),
               arrowprops=dict(arrowstyle='->', lw=2, color='blue'))

    # Elevator shaft to surface
    ax.add_patch(patches.Rectangle((8, 1.5), 2, 3.5, facecolor='white', edgecolor='red', linewidth=2))
    ax.text(9, 3.25, 'LIFT\nTO\nSURFACE', ha='center', fontsize=6, color='red', fontweight='bold')
    ax.annotate('To trough\ngrid above', xy=(9, 5), xytext=(9, 5.5), fontsize=6,
               ha='center', color='red')

    # Work order screen
    ax.add_patch(patches.Rectangle((14.5, 1.5), 3, 1.2, facecolor='#333', edgecolor='black'))
    ax.text(16, 2.1, 'WORK ORDER\nDISPLAY', ha='center', fontsize=5, color='#0f0')

    # Tunnel continues
    ax.text(-0.5, 3.25, '<< FROM\nTUNNEL', fontsize=6, ha='right')
    ax.text(24.5, 3.25, 'TO\nTUNNEL >>', fontsize=6, ha='left')

    # Labels
    ax.text(12, -1, 'Gardeners at depot see work orders and service planters.\n'
           'They never see surface maze configuration or know where planters go.',
           ha='center', fontsize=8, style='italic')

    ax.axis('off')
    save(fig, 'fig12_depot_station.png')


if __name__ == '__main__':
    print("Generating additional patent drawings...")
    fig9_terrace_transit()
    fig10_planter_crosssection()
    fig11_trough_crosssection()
    fig12_depot_station()
    print(f"\nAll drawings saved to {os.path.abspath(OUT_DIR)}")
