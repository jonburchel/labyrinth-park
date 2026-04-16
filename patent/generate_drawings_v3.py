"""
Additional patent drawings for three-part modular architecture.
Replaces fig11 with three-level trough, adds exploded view and sequence.
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


def fig13_three_part_exploded():
    """Exploded side view showing three independent components"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 12))
    ax.set_xlim(-4, 16)
    ax.set_ylim(-8, 14)
    ax.set_aspect('equal')
    ax.set_title('FIG. 13 - Three-Part Modular Architecture (Exploded Side View)',
                fontsize=12, fontweight='bold')

    # Ground level reference
    ground_y = 0
    ax.plot([-4, 16], [ground_y]*2, 'k-', linewidth=1, alpha=0.3)
    ax.text(14, 0.3, 'GRADE', fontsize=7, color='gray')

    # === PART 1: PLANTER PAN (top, shown elevated for exploded view) ===
    pan_y = 6  # elevated for exploded view
    pan_w = 8
    pan_h = 1.0
    pan_left = 2

    # Pan body (concrete)
    ax.add_patch(patches.Rectangle((pan_left, pan_y), pan_w, pan_h,
                 facecolor='#bbbbbb', edgecolor='black', linewidth=2))
    # Flat bottom emphasis
    ax.plot([pan_left, pan_left + pan_w], [pan_y]*2, 'k-', linewidth=3)
    ax.text(pan_left + pan_w/2, pan_y - 0.3, 'FLAT BOTTOM (no wheels)',
           ha='center', fontsize=7, style='italic', color='#666')

    # Growing medium
    ax.add_patch(patches.Rectangle((pan_left + 0.3, pan_y + pan_h), pan_w - 0.6, 1.5,
                 facecolor='#D2691E', edgecolor='black', linewidth=1))

    # Hedge
    hedge_bottom = pan_y + pan_h + 1.5
    ax.add_patch(patches.Rectangle((pan_left - 0.3, hedge_bottom), pan_w + 0.6, 4.5,
                 facecolor='#4a7c3f', edgecolor='#2d5a27', linewidth=1.5))
    x_wave = np.linspace(pan_left - 0.3, pan_left + pan_w + 0.3, 40)
    y_wave = hedge_bottom + 4.5 + 0.3 * np.sin(x_wave * 3)
    ax.fill_between(x_wave, y_wave, hedge_bottom + 4.5, color='#4a7c3f')
    ax.plot(x_wave, y_wave, color='#2d5a27', linewidth=1.5)

    # Manifold connectors on edges
    for mx in [pan_left, pan_left + pan_w]:
        ax.add_patch(patches.Rectangle((mx - 0.15, pan_y + 0.2), 0.3, 0.6,
                     facecolor='#ffcc00', edgecolor='black', linewidth=1))

    # Micro-pump inside pan
    ax.add_patch(patches.Circle((pan_left + 2, pan_y + 0.5), 0.25,
                 facecolor='#4488cc', edgecolor='black'))
    ax.text(pan_left + 2, pan_y + 0.5, 'P', ha='center', va='center',
           fontsize=6, color='white', fontweight='bold')

    # Label
    ax.text(-3, pan_y + 3, 'PART 1\nPLANTER PAN', fontsize=10, fontweight='bold',
           ha='center', color='#333',
           bbox=dict(boxstyle='round', facecolor='#ffe0e0', edgecolor='#c00'))
    ax.text(13, pan_y + 2, 'Contains:\n- Manifold connectors\n- Micro-pump + 3-way valve\n- Sensors (moisture, temp)\n- Small power buffer\n\nDoes NOT contain:\n- Wheels or motors\n- Suspension\n- Navigation',
           fontsize=6, va='top',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

    # === PART 2: ROLLER CHASSIS (middle, shown separated) ===
    chassis_y = 2.5
    chassis_w = 6.5  # narrower than pan
    chassis_h = 0.8
    chassis_left = 2.75

    ax.add_patch(patches.Rectangle((chassis_left, chassis_y), chassis_w, chassis_h,
                 facecolor='#888888', edgecolor='black', linewidth=2))

    # Wheels
    for wx in [chassis_left + 0.8, chassis_left + chassis_w - 0.8]:
        ax.add_patch(plt.Circle((wx, chassis_y), 0.3, facecolor='#333', edgecolor='black'))

    # Bearing surface on top (the 3mm engagement surface)
    ax.add_patch(patches.Rectangle((chassis_left + 0.3, chassis_y + chassis_h), chassis_w - 0.6, 0.08,
                 facecolor='#ffcc00', edgecolor='black'))
    ax.annotate('3mm bearing surface\n(raises to engage pan)',
               xy=(chassis_left + chassis_w/2, chassis_y + chassis_h + 0.08),
               xytext=(13, chassis_y + chassis_h + 0.5), fontsize=6,
               arrowprops=dict(arrowstyle='->', lw=0.8))

    ax.text(-3, chassis_y + 0.5, 'PART 2\nROLLER CHASSIS', fontsize=10, fontweight='bold',
           ha='center', color='#333',
           bbox=dict(boxstyle='round', facecolor='#e0e0ff', edgecolor='#00c'))
    ax.text(-3.5, chassis_y - 0.5, 'Fleet of 20-30\n(shared, reusable)', fontsize=7,
           ha='center', style='italic')

    # === PART 3: ELEVATOR BOX (bottom, shown separated) ===
    elev_y = -1.5
    elev_w = 4
    elev_h = 1.0
    elev_left = 4

    ax.add_patch(patches.Rectangle((elev_left, elev_y), elev_w, elev_h,
                 facecolor='#666666', edgecolor='black', linewidth=2, hatch='///'))

    # Scissor mechanism suggestion
    ax.plot([elev_left + 1, elev_left + 2], [elev_y + elev_h, elev_y + elev_h + 0.8], 'k-', linewidth=2)
    ax.plot([elev_left + 2, elev_left + 3], [elev_y + elev_h, elev_y + elev_h + 0.8], 'k-', linewidth=2)
    ax.plot([elev_left + 1, elev_left + 3], [elev_y + elev_h + 0.8, elev_y + elev_h], 'k-', linewidth=2)

    # Small wheels on elevator
    for wx in [elev_left + 0.5, elev_left + elev_w - 0.5]:
        ax.add_patch(plt.Circle((wx, elev_y), 0.2, facecolor='#444', edgecolor='black'))

    ax.text(-3, elev_y + 0.5, 'PART 3\nELEVATOR BOX', fontsize=10, fontweight='bold',
           ha='center', color='#333',
           bbox=dict(boxstyle='round', facecolor='#e0ffe0', edgecolor='#0c0'))
    ax.text(-3.5, elev_y - 0.5, 'Fleet of 10-15\n(shared, reusable)', fontsize=7,
           ha='center', style='italic')

    # === THREE TROUGH LEVELS (right side, cross-section) ===
    # Show the nested troughs
    tx = -3.5
    ax.text(6, -5, 'THREE NESTED TROUGH LEVELS:', fontsize=9, fontweight='bold', ha='center')

    # Outer trough
    ax.add_patch(patches.Rectangle((2, -7.5), 8, 1.2,
                 facecolor='#ffe0e0', edgecolor='black', linewidth=1))
    ax.text(6, -6.9, 'OUTER (widest): receives planter pan', ha='center', fontsize=7)

    # Middle trough
    ax.add_patch(patches.Rectangle((2.75, -7.5), 6.5, 0.8,
                 facecolor='#e0e0ff', edgecolor='black', linewidth=1))
    ax.text(6, -7.3, 'MIDDLE: roller chassis travels', ha='center', fontsize=6, color='white')

    # Center trough
    ax.add_patch(patches.Rectangle((4, -7.5), 4, 0.5,
                 facecolor='#e0ffe0', edgecolor='black', linewidth=1))

    # Connection arrows (exploded view lines)
    ax.annotate('', xy=(6, pan_y), xytext=(6, chassis_y + chassis_h + 0.4),
               arrowprops=dict(arrowstyle='<->', lw=1.5, linestyle='--', color='red'))
    ax.annotate('', xy=(6, chassis_y), xytext=(6, elev_y + elev_h + 1),
               arrowprops=dict(arrowstyle='<->', lw=1.5, linestyle='--', color='blue'))

    ax.axis('off')
    save(fig, 'fig13_three_part_exploded.png')


def fig14_pickup_sequence():
    """4-panel showing pickup, transport, delivery, and cover"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    titles = [
        'Step 1: Chassis Positions Under Pan',
        'Step 2: Elevator Lifts Assembly',
        'Step 3: Chassis Drives to Destination',
        'Step 4: Cover Tile Fills Vacancy'
    ]

    for idx, (ax, title) in enumerate(zip(axes, titles)):
        ax.set_xlim(-1, 21)
        ax.set_ylim(-4, 7)
        ax.set_aspect('equal')
        ax.set_title(f'FIG. 14{chr(65+idx)} - {title}', fontsize=9, fontweight='bold')

        # Ground
        ax.fill_between([-1, 21], [0]*2, [-0.2]*2, color='#cccccc')
        ax.plot([-1, 21], [0]*2, 'k-', linewidth=2)

        # Trough at position A (left)
        for tx in [2, 12]:
            ax.plot([tx, tx], [0, -2.5], 'k-', linewidth=1.5, alpha=0.5)
            ax.plot([tx+6, tx+6], [0, -2.5], 'k-', linewidth=1.5, alpha=0.5)
            ax.plot([tx, tx+6], [-2.5]*2, 'k-', linewidth=1.5, alpha=0.5)

        if idx == 0:  # Chassis approaches
            # Pan seated in left trough
            ax.add_patch(patches.Rectangle((2.2, -2), 5.6, 0.6, facecolor='#bbb', edgecolor='black'))
            ax.add_patch(patches.Rectangle((2, -0.5), 6, 4.5, facecolor='#4a7c3f', edgecolor='#2d5a27'))
            ax.text(5, 2, 'PAN', ha='center', color='white', fontweight='bold')
            # Chassis arriving (arrow)
            ax.add_patch(patches.Rectangle((3, -2.8), 4, 0.5, facecolor='#888', edgecolor='black'))
            ax.annotate('', xy=(5, -2.5), xytext=(0, -2.5),
                       arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
            ax.text(0, -3.3, 'Chassis\narriving', fontsize=7, color='blue')

            # Destination empty
            ax.text(15, -1, 'EMPTY', ha='center', fontsize=8, color='gray')

        elif idx == 1:  # Elevator lifts
            # Pan + chassis lifted above trough
            ax.add_patch(patches.Rectangle((2.5, 0.2), 5, 0.5, facecolor='#888', edgecolor='black'))
            ax.add_patch(patches.Rectangle((2.2, 0.7), 5.6, 0.6, facecolor='#bbb', edgecolor='black'))
            ax.add_patch(patches.Rectangle((2, 1.3), 6, 4, facecolor='#4a7c3f', edgecolor='#2d5a27'))
            ax.text(5, 3, 'LIFTED', ha='center', color='white', fontweight='bold')
            # Elevator below
            ax.add_patch(patches.Rectangle((3.5, -2.5), 3, 2.5, facecolor='#666', edgecolor='black', hatch='///'))
            ax.annotate('ELEVATOR\nLIFTING', xy=(5, -1.2), fontsize=7, ha='center',
                       color='white', fontweight='bold')
            # Destination empty
            ax.text(15, -1, 'EMPTY', ha='center', fontsize=8, color='gray')

        elif idx == 2:  # Transit
            # Left trough now empty
            ax.text(5, -1, 'VACANT', ha='center', fontsize=8, color='gray')
            # Pan + chassis in transit (at destination)
            ax.add_patch(patches.Rectangle((12.5, -1.8), 5, 0.5, facecolor='#888', edgecolor='black'))
            ax.add_patch(patches.Rectangle((12.2, -1.3), 5.6, 0.6, facecolor='#bbb', edgecolor='black'))
            ax.add_patch(patches.Rectangle((12, -0.7), 6, 4, facecolor='#4a7c3f', edgecolor='#2d5a27'))
            ax.text(15, 1.5, 'DELIVERED', ha='center', color='white', fontweight='bold')
            ax.annotate('', xy=(12, 0.5), xytext=(8, 0.5),
                       arrowprops=dict(arrowstyle='->', lw=2, color='red'))

        elif idx == 3:  # Cover fills vacancy
            # Cover tile in left position
            ax.add_patch(patches.Rectangle((2, -0.15), 6, 0.15,
                         facecolor='#ddcc99', edgecolor='black', linewidth=1.5))
            ax.text(5, 0.5, 'COVER TILE\n(seamless surface)', ha='center', fontsize=8,
                   fontweight='bold', color='#886633')
            # Pan in right position (seated)
            ax.add_patch(patches.Rectangle((12.2, -2), 5.6, 0.6, facecolor='#bbb', edgecolor='black'))
            ax.add_patch(patches.Rectangle((12, -0.5), 6, 4.5, facecolor='#4a7c3f', edgecolor='#2d5a27'))
            ax.text(15, 2, 'SEATED', ha='center', color='white', fontweight='bold')

        ax.axis('off')

    fig.tight_layout()
    save(fig, 'fig14_three_part_sequence.png')


def fig11_three_level_trough():
    """Three nested U-channels as ONE continuous concrete structure.
    Walls step inward at each level. Only bottom has a floor."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(-4, 16)
    ax.set_ylim(-6, 3.5)
    ax.set_aspect('equal')
    ax.set_title('FIG. 11 - Three-Level Trough Cross-Section (Single Concrete Form)',
                fontsize=12, fontweight='bold')

    ground_y = 0
    w = 0.3  # wall thickness

    # Dimensions
    # Outer channel: 9ft wide opening, 1.5ft deep
    # Middle channel: 6ft wide, starts at bottom of outer, 1.5ft deep
    # Center channel: 3ft wide, starts at bottom of middle, 1.0ft deep
    # Total depth: 4.0ft

    outer_w = 9.0
    outer_d = 1.5
    mid_w = 6.0
    mid_d = 1.5
    ctr_w = 3.0
    ctr_d = 1.0

    cx = 6.0  # center x of the whole structure
    outer_l = cx - outer_w/2
    outer_r = cx + outer_w/2
    mid_l = cx - mid_w/2
    mid_r = cx + mid_w/2
    ctr_l = cx - ctr_w/2
    ctr_r = cx + ctr_w/2

    # Ground surface
    ax.fill_between([-4, outer_l], [ground_y]*2, [-0.15]*2, color='#cccccc')
    ax.fill_between([outer_r, 16], [ground_y]*2, [-0.15]*2, color='#cccccc')
    ax.plot([-4, outer_l], [ground_y]*2, 'k-', linewidth=2)
    ax.plot([outer_r, 16], [ground_y]*2, 'k-', linewidth=2)
    ax.text(-1.5, 0.3, 'PATH', fontsize=7, ha='center', color='#666')
    ax.text(13.5, 0.3, 'PATH', fontsize=7, ha='center', color='#666')

    # Draw the entire structure as one continuous concrete profile
    # Going clockwise from top-left:
    profile_x = [
        outer_l, outer_l,                          # left outer wall, top to step
        mid_l, mid_l,                              # step inward, then down
        ctr_l, ctr_l,                              # step inward again, then down
        ctr_r, ctr_r,                              # across bottom, then up
        mid_r, mid_r,                              # step outward, then up
        outer_r, outer_r,                          # step outward to top
    ]
    profile_y = [
        ground_y, -outer_d,                        # outer left wall
        -outer_d, -outer_d - mid_d,               # middle left wall
        -outer_d - mid_d, -outer_d - mid_d - ctr_d,  # center left wall
        -outer_d - mid_d - ctr_d, -outer_d - mid_d,  # center right wall (up)
        -outer_d - mid_d, -outer_d,               # middle right wall (up)
        -outer_d, ground_y,                        # outer right wall (up)
    ]

    # Fill the concrete (draw as thick walls by offsetting)
    # Simpler approach: draw the OUTER profile and INNER profile
    # Outer profile is the outside face of all concrete
    # Inner profile is the inside face (the open channels)

    # LEFT SIDE concrete mass
    # Outer wall
    ax.add_patch(patches.Rectangle((outer_l, -outer_d), w, outer_d,
                 facecolor='#999', edgecolor='black', linewidth=1.5))
    # Left step (horizontal ledge connecting outer to middle wall)
    ax.add_patch(patches.Rectangle((outer_l, -outer_d - w), mid_l - outer_l, w,
                 facecolor='#999', edgecolor='black', linewidth=1))
    # Middle left wall
    ax.add_patch(patches.Rectangle((mid_l, -outer_d - mid_d), w, mid_d,
                 facecolor='#888', edgecolor='black', linewidth=1.2))
    # Left step (horizontal ledge connecting middle to center wall)
    ax.add_patch(patches.Rectangle((mid_l, -outer_d - mid_d - w), ctr_l - mid_l, w,
                 facecolor='#888', edgecolor='black', linewidth=1))
    # Center left wall
    ax.add_patch(patches.Rectangle((ctr_l, -outer_d - mid_d - ctr_d), w, ctr_d,
                 facecolor='#777', edgecolor='black', linewidth=1))

    # RIGHT SIDE (mirror)
    ax.add_patch(patches.Rectangle((outer_r - w, -outer_d), w, outer_d,
                 facecolor='#999', edgecolor='black', linewidth=1.5))
    ax.add_patch(patches.Rectangle((mid_r, -outer_d - w), outer_r - mid_r, w,
                 facecolor='#999', edgecolor='black', linewidth=1))
    ax.add_patch(patches.Rectangle((mid_r - w, -outer_d - mid_d), w, mid_d,
                 facecolor='#888', edgecolor='black', linewidth=1.2))
    ax.add_patch(patches.Rectangle((ctr_r, -outer_d - mid_d - w), mid_r - ctr_r, w,
                 facecolor='#888', edgecolor='black', linewidth=1))
    ax.add_patch(patches.Rectangle((ctr_r - w, -outer_d - mid_d - ctr_d), w, ctr_d,
                 facecolor='#777', edgecolor='black', linewidth=1))

    # BOTTOM FLOOR (only floor in the system)
    ax.add_patch(patches.Rectangle((ctr_l, -outer_d - mid_d - ctr_d - w), ctr_w, w,
                 facecolor='#777', edgecolor='black', linewidth=1.5))

    # Fill channel zones with color
    # Outer channel zone (above the steps)
    ax.add_patch(patches.Rectangle((outer_l + w, -outer_d),
                 outer_w - 2*w, outer_d,
                 facecolor='#ffe0e0', edgecolor='none', alpha=0.15))
    # Middle channel zone
    ax.add_patch(patches.Rectangle((mid_l + w, -outer_d - mid_d),
                 mid_w - 2*w, mid_d,
                 facecolor='#e0e0ff', edgecolor='none', alpha=0.15))
    # Center channel zone
    ax.add_patch(patches.Rectangle((ctr_l + w, -outer_d - mid_d - ctr_d),
                 ctr_w - 2*w, ctr_d,
                 facecolor='#e0ffe0', edgecolor='none', alpha=0.15))

    # Bearing plates on MIDDLE-TO-CENTER STEP (where chassis wheels actually run)
    bp_h = 0.06
    bp_y = -outer_d - mid_d  # the middle-to-center step, NOT the outer-to-middle step
    # Left bearing plate
    ax.add_patch(patches.Rectangle((mid_l + w + 0.1, bp_y - bp_h),
                 ctr_l - mid_l - w - 0.2, bp_h,
                 facecolor='#ffcc00', edgecolor='black'))
    # Right bearing plate
    ax.add_patch(patches.Rectangle((ctr_r + 0.1, bp_y - bp_h),
                 mid_r - w - ctr_r - 0.2, bp_h,
                 facecolor='#ffcc00', edgecolor='black'))

    # Pan-to-pan interlock pins (shown on outer ledge edges)
    for ix in [outer_l + w + 0.3, outer_r - w - 0.5]:
        ax.add_patch(patches.Rectangle((ix, -outer_d + 0.02), 0.15, 0.25,
                     facecolor='#cc4444', edgecolor='black', linewidth=0.8))

    # Pan-to-trough retention clips (hold pan down against wind)
    for ix in [outer_l + w + 1.0, outer_r - w - 1.15]:
        ax.plot([ix, ix + 0.15, ix + 0.15], [-outer_d + 0.3, -outer_d + 0.3, -outer_d + 0.05],
               'k-', linewidth=2)

    # Surface cover (dashed)
    ax.add_patch(patches.Rectangle((outer_l, -0.1), outer_w, 0.1,
                 facecolor='none', edgecolor='black', linewidth=1, linestyle=':'))
    ax.text(cx, 0.35, '(surface cover when unoccupied)', ha='center', fontsize=6,
           color='gray', style='italic')

    # Labels
    labels = [
        ((-3.5, -0.7), (outer_l + 0.5, -0.7),
         'OUTER CHANNEL\n(pan sits on ledge)'),
        ((-3.5, -2.5), (mid_l + 0.5, -outer_d - mid_d/2),
         'MIDDLE CHANNEL\n(chassis travels)'),
        ((-3.5, -4.5), (ctr_l + 0.5, -outer_d - mid_d - ctr_d/2),
         'CENTER CHANNEL\n(elevator; only floor)'),
        ((13, -2.8), (ctr_r + 0.2, bp_y - bp_h/2),
         'Bearing plates\n(A36 steel on\nmiddle-to-center\nstep ledge)'),
        ((13, -0.5), (outer_r - w - 0.4, -outer_d + 0.15),
         'Pan-to-pan interlocks\n+ retention clips\n(on outer ledge)'),
        ((13, -5.0), (outer_r - 0.5, -outer_d - mid_d - 0.5),
         'All channels DRY\nUtilities in pan\nmanifolds only'),
    ]
    for text_pos, target, label in labels:
        ax.annotate(label, xy=target, xytext=text_pos, fontsize=7,
                   arrowprops=dict(arrowstyle='->', lw=0.8),
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='gray', alpha=0.9))

    ax.text(cx, 2.5, 'Single concrete form: stepped walls getting narrower with depth.\nNo suspended floors. Chassis wheels run on the step ledges.\nOne pour, simple formwork.',
           ha='center', fontsize=8, style='italic',
           bbox=dict(boxstyle='round', facecolor='#ffffcc', edgecolor='#cc9'))

    ax.axis('off')
    save(fig, 'fig11_trough_crosssection.png')


if __name__ == '__main__':
    print("Generating three-part architecture drawings...")
    fig13_three_part_exploded()
    fig14_pickup_sequence()
    fig11_three_level_trough()
    print("Done!")
