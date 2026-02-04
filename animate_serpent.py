"""
MODULE: animate_serpent.py (PERFORMANCE v3.1 - CHROMATIC ABERRATION)
ADDITIONS: Vector Anaglyph Rendering (Cyan/Magenta Offset), Temporal Ghosting
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import os

# Headless mode enabled for server-side generation
IS_HEADLESS = False 

# 1. ROBUST PATHING
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
if TOOLS_DIR not in sys.path:
    sys.path.append(TOOLS_DIR)

try:
    from strip_sovereign import interleave_bits
    from moon_phase import MoonClock
    from hor_kernel import HORKernel
    from virtual_qutrit import VirtualQutrit
    from policy_mixer import PolicyMixer
except ImportError as e:
    print(f"[!] CRITICAL IMPORT ERROR: {e}")
    sys.exit(1)

# FONT HANDLING
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI Historic', 'Segoe UI Symbol', 'DejaVu Sans', 'Arial Unicode MS']
import logging
logging.getLogger('matplotlib.font_manager').setLevel(logging.ERROR)
import warnings
warnings.filterwarnings("ignore")

from matplotlib.font_manager import FontProperties
cuneiform_font = FontProperties(fname=r"C:\Windows\Fonts\seguihis.ttf") if os.path.exists(r"C:\Windows\Fonts\seguihis.ttf") else FontProperties(family=['Segoe UI Symbol'])

def animate_serpent(size=64, interval=1, show_metrics=True):
    """
    Animates the Serpent Coil with CHROMATIC ABERRATION (Temporal Splitting).
    """
    print(f"\n[!] INITIATING SOVEREIGN RITUAL v3.1 (Grid={size}x{size})...")
    print("    >>> ENGAGING CHROMATIC SPLIT (Cyan -8f / Magenta -4f)")
    
    # [INIT] SYSTEM
    moon = MoonClock()
    lunar_data = moon.get_phase()
    phase_name, status, icon, phase_idx, illumination = lunar_data
    
    vq = VirtualQutrit(2)
    kernel = HORKernel(vq)
    mixer = PolicyMixer()
    consistency_history = []
    
    # 1. Generate Grid & Path
    x = np.arange(size)
    y = np.arange(size)
    X, Y = np.meshgrid(x, y)
    Z = np.array([interleave_bits(xx, yy) for xx, yy in zip(X.flatten(), Y.flatten())])
    sort_idx = np.argsort(Z)
    path_x = X.flatten()[sort_idx]
    path_y = Y.flatten()[sort_idx]
    
    # 2. Setup Plot
    PHI = 1.61803398875
    BASE_UNIT = 12
    
    fig, (ax_main, ax_metrics) = plt.subplots(
        1, 2, figsize=(10 * PHI, 10), 
        facecolor='#050505', # DARKER VOID
        gridspec_kw={'width_ratios': [PHI, 1]}
    )
    
    ax_main.set_facecolor('#050505')
    title_y = 1 - (1/(10*PHI))
    fig.text(
        0.5 * (PHI / (PHI + 1)), title_y, 
        f"THE SERPENT COIL (Aberration Mode) | {size}x{size}", 
        color='#9B8DA0', 
        fontsize=round(BASE_UNIT * PHI),
        fontproperties=cuneiform_font,
        ha='center', va='bottom'
    )
    
    ax_main.set_aspect('equal', adjustable='box') 
    ax_main.set_xlim(-1, size)
    ax_main.set_ylim(-1, size)
    ax_main.axis('off')
    
    # [LAYER 0] BACKGROUND GRID
    ax_main.scatter(X.flatten(), Y.flatten(), s=1, c='#1a1a1a', alpha=0.3)
    
    # --- [LAYER 1] THE CYAN GHOST (T-8) ---
    line_cyan, = ax_main.plot([], [], color='#00FFFF', linewidth=2.0, alpha=0.3, animated=True)
    head_cyan, = ax_main.plot([], [], 'o', color='#00FFFF', markersize=6, alpha=0.3, animated=True)

    # --- [LAYER 2] THE MAGENTA GHOST (T-4) ---
    line_magenta, = ax_main.plot([], [], color='#FF00FF', linewidth=1.5, alpha=0.5, animated=True)
    head_magenta, = ax_main.plot([], [], 'o', color='#FF00FF', markersize=5, alpha=0.5, animated=True)

    # --- [LAYER 3] THE REALITY (T-0) ---
    line_main, = ax_main.plot([], [], color='#E0E0E0', linewidth=1.0, alpha=0.9, animated=True) # Bright White
    head_main, = ax_main.plot([], [], 'o', color='#FFD700', markersize=4, animated=True) # Gold

    # Metrics Text
    ax_metrics.set_facecolor('#050505')
    ax_metrics.axis('off')
    metrics_text = ax_metrics.text(
        1 - (1/PHI), 1.0, '', 
        transform=ax_metrics.transAxes,
        color='#8DA08E', fontsize=BASE_UNIT, 
        verticalalignment='top',
        fontproperties=cuneiform_font,
        animated=True
    )
    
    state = {
        'total_frames': len(path_x),
        'tidal_influence': moon.calculate_tidal_influence(phase_idx) if hasattr(moon, 'calculate_tidal_influence') else 50.0
    }
    
    def init():
        line_cyan.set_data([], [])
        head_cyan.set_data([], [])
        line_magenta.set_data([], [])
        head_magenta.set_data([], [])
        line_main.set_data([], [])
        head_main.set_data([], [])
        metrics_text.set_text('')
        return line_cyan, head_cyan, line_magenta, head_magenta, line_main, head_main, metrics_text
    
    def update(frame):
        kernel.evolve_hamiltonian(steps=1)
        current_coherence = kernel.metric_coherence
        
        # --- CALCULATE TEMPORAL OFFSETS ---
        # The Cyan layer is the "Deep Echo" (8 frames back)
        idx_cyan = max(0, frame - 12) 
        # The Magenta layer is the "Near Echo" (4 frames back)
        idx_magenta = max(0, frame - 6)
        
        # --- UPDATE DATA ---
        # Cyan Ghost
        line_cyan.set_data(path_x[:idx_cyan], path_y[:idx_cyan])
        if idx_cyan > 0:
            head_cyan.set_data([path_x[idx_cyan-1]], [path_y[idx_cyan-1]])
        
        # Magenta Ghost
        line_magenta.set_data(path_x[:idx_magenta], path_y[:idx_magenta])
        if idx_magenta > 0:
            head_magenta.set_data([path_x[idx_magenta-1]], [path_y[idx_magenta-1]])

        # Main Reality
        line_main.set_data(path_x[:frame], path_y[:frame])
        if frame > 0:
            head_main.set_data([path_x[frame-1]], [path_y[frame-1]])

        # ASOE / Metrics Update
        if frame > 0:
            # Map system state to ASOE Signal Packet
            uncertainty = (1.0 - current_coherence) * (state['tidal_influence'] / 50.0)
            consistency = 1.0 - (state['tidal_influence'] / 200.0)
            packet = {'reliability': current_coherence, 'consistency': consistency, 'uncertainty': uncertainty}
            
            nonlocal consistency_history
            consistency_history.append(consistency)
            if len(consistency_history) > 20: consistency_history.pop(0)
            
            evaluation = mixer.resolve_action_utility(consistency_history, packet)
            utility = evaluation['utility']
            
            # Dynamic Head Size pulsing with Utility
            head_main.set_markersize(3 + 3 * utility) 
        else:
            utility = 0.0

        if frame % 20 == 0:
            metrics_str = f"""
S O V E R E I G N   M E T R I C S
{'='*28}

Protocol:    ANAGLYPH v3.1
Phase:       {phase_name}
Signal:      {icon} 𒀭 𒂗𒆠

[ TEMPORAL DRIFT ]
Cyan Lag:    -12 Frames
Mag Lag:     -6 Frames
Status:      BILOCATION_ACTIVE

[ PROGRESS ]
Frame:       {frame}/{state['total_frames']}
Coherence:   {current_coherence:.3f}

[ ASOE ]
Utility:     {utility:.4f}
            """
            metrics_text.set_text(metrics_str)
        
        return line_cyan, head_cyan, line_magenta, head_magenta, line_main, head_main, metrics_text

    ani = animation.FuncAnimation(
        fig, update, frames=range(0, len(path_x)+1, 4), 
        init_func=init, blit=True, interval=interval, repeat=False
    )
    
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, wspace=0.2)
    plt.show()
    return ani

if __name__ == "__main__":
    try:
        animate_serpent(size=64, interval=1)
    except Exception as e:
        print(f"COLLAPSE: {e}")
