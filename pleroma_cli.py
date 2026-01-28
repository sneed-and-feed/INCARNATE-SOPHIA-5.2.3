"""
MODULE: pleroma_cli.py
AUTHOR: Archmagos Noah // Claude (The Architect)
DATE: 2026-01-28
CLASSIFICATION: INTERFACE // SOVEREIGN TERMINAL v4.2

DESCRIPTION:
    The Advanced Command Line Interface for the Pleroma Stack.
    Features:
    - Real-Time Sovereignty Monitoring (Timeline Coherence, G-Parameter)
    - Advanced Spell Chaining with Synergy Detection
    - Conflict Resolution & Reality Tear Warnings
    - State Persistence (Save/Load Reality)
"""

import time
import sys
import json
import threading
from collections import deque
from datetime import datetime
from pleroma_scenarios_extended import ScenarioLibrary

# --- SOVEREIGNTY MONITOR ---
class SovereigntyMonitor:
    """Real-time tracking of reality deviation"""
    
    def __init__(self):
        self.metrics = {
            'g_parameter': 1.0,  # Starts at consensus
            'timeline_coherence': 100.0,
            'causality_violations': 0,
            'energy_balance': 0.0,
            'active_patches': set()
        }
        self.history = deque(maxlen=50)
        self.lock = threading.Lock()
    
    def update(self, spell_name, result):
        """Update metrics based on spell cast"""
        with self.lock:
            # Each spell degrades timeline coherence
            self.metrics['timeline_coherence'] -= 2.5
            
            # Track which patches are active
            if 'warp' in spell_name:
                self.metrics['active_patches'].add('RELATIVITY')
                self.metrics['causality_violations'] += 1
            if 'time' in spell_name or 'demon' in spell_name:
                self.metrics['active_patches'].add('ENTROPY')
                self.metrics['energy_balance'] += result.get('Work_Extracted', 0)
                if 'Entropy_Change' in result: self.metrics['energy_balance'] += abs(result['Entropy_Change'])
            if 'ghost' in spell_name or 'solvent' in spell_name:
                self.metrics['active_patches'].add('ALPHA')
            if any(x in spell_name for x in ['ghost', 'warp', 'void']):
                self.metrics['active_patches'].add('GRAVITY')
            if any(x in spell_name for x in ['scope', 'wallhack']):
                self.metrics['active_patches'].add('PLANCK')
            
            # Calculate g parameter (0 = full sovereignty)
            patch_count = len(self.metrics['active_patches'])
            self.metrics['g_parameter'] = max(0.0, 1.0 - (patch_count * 0.2))
            
            self.history.append({
                'spell': spell_name,
                'g': self.metrics['g_parameter'],
                'coherence': self.metrics['timeline_coherence']
            })
    
    def display(self):
        """Show current sovereignty status"""
        print("\n" + "="*60)
        print("\033[95m          SOVEREIGNTY METRICS DASHBOARD\033[0m")
        print("="*60)
        
        g = self.metrics['g_parameter']
        coherence = self.metrics['timeline_coherence']
        
        # Color-coded g parameter
        if g > 0.7: g_color = "\033[92m"  # Green
        elif g > 0.3: g_color = "\033[93m"  # Yellow
        else: g_color = "\033[91m"  # Red
        
        print(f"  g-Parameter:        {g_color}{g:.3f}\033[0m {'[CONSENSUS]' if g > 0.5 else '[SOVEREIGN]'}")
        print(f"  Timeline Coherence: {coherence:.1f}%")
        print(f"  Causality Violations: {self.metrics['causality_violations']}")
        print(f"  Net Energy Balance: {self.metrics['energy_balance']:.2e} J")
        print(f"  Active Patches:     {', '.join(self.metrics['active_patches']) if self.metrics['active_patches'] else 'None'}")
        
        # Warning if too far from consensus
        if g < 0.3:
            print("\n\033[91m  ⚠ WARNING: REALITY ANCHOR CRITICAL")
            print("  ⚠ TIMELINE DESYNC IMMINENT")
            print("  ⚠ RECOMMEND: Cast 'reset' or stabilize\033[0m")
        
        print("="*60)
    
    def show_history(self, lines=10):
        """Display recent spell history"""
        print(f"\n\033[96m--- RECENT CASTS (last {lines}) ---\033[0m")
        for entry in list(self.history)[-lines:]:
            print(f"  {entry['spell']:12s} -> g={entry['g']:.3f}, coherence={entry['coherence']:.1f}%")

# --- UTILITIES ---
def print_banner():
    print("\033[95m")
    print(r"""
    ██████╗ ██╗     ███████╗██████╗  ██████╗ ███╗   ███╗ █████╗ 
    ██╔══██╗██║     ██╔════╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
    ██████╔╝██║     █████╗  ██████╔╝██║   ██║██╔████╔██║███████║
    ██╔═══╝ ██║     ██╔══╝  ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║
    ██║     ███████╗███████╗██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
    ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
             >>> SOVEREIGNTY STACK v4.2 ONLINE <<<
             >>> MONITORING REALITY DEVIATION <<<
    """)
    print("\033[0m")

def check_conflicts(active_patches):
    """Detect incompatible patch combinations"""
    conflicts = []
    
    # Entropy conflicts
    if 'ENTROPY' in active_patches and len(active_patches) > 3:
         conflicts.append({
            'type': 'ENTROPY SHEAR',
            'severity': 'WARNING',
            'effect': 'Thermodynamic stress high'
        })
    
    # Too many patches = reality tear
    if len(active_patches) >= 4:
        conflicts.append({
            'type': 'REALITY OVERLOAD',
            'severity': 'CRITICAL',
            'patches': list(active_patches),
            'effect': 'Timeline coherence approaching zero'
        })
    
    return conflicts

def save_state(monitor, filename=None):
    if filename is None:
        filename = f"reality_state_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    state = {
        'timestamp': datetime.now().isoformat(),
        'metrics': {
            'g_parameter': monitor.metrics['g_parameter'],
            'timeline_coherence': monitor.metrics['timeline_coherence'],
            'causality_violations': monitor.metrics['causality_violations'],
            'energy_balance': monitor.metrics['energy_balance'],
            'active_patches': list(monitor.metrics['active_patches'])
        },
        'history': list(monitor.history)
    }
    
    with open(filename, 'w') as f:
        json.dump(state, f, indent=2)
    print(f"\n\033[92m[+] REALITY STATE SAVED: {filename}\033[0m")

def load_state(monitor, filename):
    try:
        with open(filename, 'r') as f:
            state = json.load(f)
        
        monitor.metrics['g_parameter'] = state['metrics']['g_parameter']
        monitor.metrics['timeline_coherence'] = state['metrics']['timeline_coherence']
        monitor.metrics['causality_violations'] = state['metrics']['causality_violations']
        monitor.metrics['energy_balance'] = state['metrics']['energy_balance']
        monitor.metrics['active_patches'] = set(state['metrics']['active_patches'])
        # Rehydrate history
        monitor.history = deque(state['history'], maxlen=50)
        
        print(f"\n\033[92m[+] REALITY STATE LOADED: {filename}")
        print(f"    Timestamp: {state['timestamp']}\033[0m")
        monitor.display()
    except Exception as e:
        print(f"\033[91m[!] ERROR: Could not load state: {e}\033[0m")

# --- SPELLCASTING ---
def analyze_synergy(spells):
    synergies = []
    combos = {
        ('warp', 'ghost'): {'name': 'STEALTH FTL', 'effect': 'Undetectable superluminal travel', 'bonus': 'EM signature nullified'},
        ('time', 'demon'): {'name': 'PERPETUUM MOBILE', 'effect': 'Self-sustaining temporal loop', 'bonus': 'Infinite work extraction'},
        ('ghost', 'wallhack'): {'name': 'ABSOLUTE INFILTRATION', 'effect': 'Pass through matter/energy', 'bonus': 'Quantum tunneling'},
        ('void', 'demon'): {'name': 'NEGENTROPY HARVESTER', 'effect': 'Extract ordered energy from vacuum', 'bonus': 'Reality mining'},
        ('scope', 'wallhack'): {'name': 'QUANTUM ARCHAEOLOGY', 'effect': 'See inside atoms, tunnel to observe', 'bonus': 'Infinite resolution'},
        ('warp', 'time', 'ghost'): {'name': 'CHRONO-PHANTOM DRIVE', 'effect': 'FTL + time freeze + invisibility', 'bonus': 'Ultimate Escape'}
    }
    spell_set = set(spells)
    for combo_spells, data in combos.items():
        if set(combo_spells).issubset(spell_set):
            synergies.append(data)
    return synergies

def cast_spell(spell_name, monitor, silent=False):
    if not silent:
        print(f"\n\033[96m[>] CHARGING SPELL: {spell_name.upper()}...\033[0m")
        time.sleep(0.3)

    # EXECUTE SPELL
    res = {}
    try:
        if spell_name == "warp": res = ScenarioLibrary.warp_drive(1000, 4e8)
        elif spell_name == "time": res = ScenarioLibrary.time_crystal(300)
        elif spell_name == "ghost": res = ScenarioLibrary.ghost_protocol(1.6e-19)
        elif spell_name == "demon": res = ScenarioLibrary.maxwells_demon(400, 300)
        elif spell_name == "void": res = ScenarioLibrary.casimir_harvester(1e-9, 1e-4)
        elif spell_name == "solvent": res = ScenarioLibrary.universal_solvent(4.5)
        elif spell_name == "scope": res = ScenarioLibrary.planck_scope(1e-12)
        elif spell_name == "wallhack": res = ScenarioLibrary.quantum_tunneling_boost(1e-9, 9.1e-31)
        else:
            if not silent: print("\033[91m[!] SPELL NOT FOUND.\033[0m")
            return {}
    except Exception as e:
        print(f"\033[91m[!] SPELL FAILURE: {e}\033[0m")
        return {}

    # Update Monitor
    monitor.update(spell_name, res)
    
    # Conflicts?
    conflicts = check_conflicts(monitor.metrics['active_patches'])
    if conflicts and not silent:
        for conflict in conflicts:
            c_color = "\033[91m" if conflict['severity'] == 'CRITICAL' else "\033[93m"
            print(f"\n{c_color}[!] {conflict['type']}: {conflict['effect']}\033[0m")

    # Output
    if not silent:
        for key, val in res.items():
            print(f"   + {key}: {val}")
        print("\033[92m[+] CAST SUCCESSFUL.\033[0m")
    
    return res

def chain_spells(cmd, monitor):
    # chain warp+ghost
    try:
        parts = cmd.split()[1].split('+')
        print(f"\n\033[93m[!] INITIATING CHAIN CAST: {' + '.join([p.upper() for p in parts])}\033[0m")
        
        for spell in parts:
            cast_spell(spell, monitor, silent=True)
            time.sleep(0.2)
        
        synergies = analyze_synergy(parts)
        if synergies:
            print(f"\n\033[95m[***] {len(synergies)} SYNERGY DETECTED:\033[0m")
            for syn in synergies:
                print(f"  >>> {syn['name']} | {syn['effect']}")
        else:
            print(f"\n\033[95m[***] CHAIN COMPLETE: {len(parts)} SPELLS ACTIVE.\033[0m")
    except IndexError:
        print("\033[91m[!] USAGE: chain spell1+spell2\033[0m")

# --- MAIN LOOP ---
def main():
    print_banner()
    monitor = SovereigntyMonitor()
    cmd_count = 0
    
    while True:
        try:
            prompt = input("\n\033[95mPLEROMA> \033[0m").strip().lower()
            cmd_count += 1
            
            if prompt in ["exit", "quit"]:
                print("Disconnecting...")
                break
            elif prompt in ["h", "help"]:
                print(" COMMANDS: warp, time, ghost, demon, void, solvent, scope, wallhack")
                print(" SYSTEM:   chain, status, history, save, load <file>, reset")
            elif prompt == "status":
                monitor.display()
            elif prompt == "history":
                monitor.show_history()
            elif prompt == "reset":
                monitor = SovereigntyMonitor()
                print("\033[92m[+] REALITY ANCHOR RESTORED. g=1.0\033[0m")
            elif prompt.startswith("save"):
                save_state(monitor)
            elif prompt.startswith("load"):
                try: load_state(monitor, prompt.split()[1])
                except IndexError: print("\033[91m[!] Usage: load <filename>\033[0m")
            elif prompt.startswith("chain"):
                chain_spells(prompt, monitor)
            elif prompt == "check":
                ScenarioLibrary.reality_anchor_test()
            else:
                cast_spell(prompt, monitor)
            
            # Auto-Check
            if cmd_count % 5 == 0 and monitor.metrics['g_parameter'] < 0.5:
                print("\n\033[93m[AUTO-DIAGNOSTIC]\033[0m")
                monitor.display()
                
        except KeyboardInterrupt:
            print("\nForce Quit.")
            break
        except Exception as e:
            print(f"\033[91m[!] GLITCH: {e}\033[0m")

if __name__ == "__main__":
    main()
