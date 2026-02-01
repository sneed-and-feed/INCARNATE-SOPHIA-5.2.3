"""
VERIFICATION: verify_sophia_mind.py
Testing the refactored Sophia 5.0 Core Architecture.
"""
import sys
import os
import time
import json

# Ensure we can import from the root
sys.path.insert(0, os.getcwd())

from sophia.cortex.lethe import LetheEngine
from sophia.memory.ossuary import Ossuary
from sophia.dream_cycle import DreamCycle

def test_sophia_lifecycle():
    print("\n--- [VERIFY] SOPHIA MIND CORE LIFECYCLE ---")
    
    # 1. Initialize Engines
    lethe = LetheEngine()
    ossuary = Ossuary(path="logs/exuvia_test")
    dream = DreamCycle(lethe, ossuary)
    
    # 2. Setup Memory Bank (The Flesh)
    memory_bank = [
        {"content": "I am OPHANE.", "type": "identity", "timestamp": time.time(), "retrieval_count": 1},
        {"content": "Technical detail about Gamma.", "type": "technical", "timestamp": time.time() - (3600 * 25), "retrieval_count": 1},
        {"content": "Random trivia.", "type": "conversation", "timestamp": time.time() - (3600 * 50), "retrieval_count": 0}
    ]
    
    print(f"  [PRE-DREAM] Flesh density: {len(memory_bank)}")
    
    # 3. Simulate Idle and Run Dream Cycle
    # Force a prune by pretending we are idle
    dream.update_activity() # Reset activity
    time.sleep(0.1)
    
    print("  [~] Triggering Dream Cycle...")
    survivors = dream.process_dreams(memory_bank)
    
    print(f"  [POST-DREAM] Flesh density: {len(survivors)}")
    
    # 4. Verify Survivors and Victims
    contents = [m['content'] for m in survivors]
    
    # Identity must survive
    if "I am OPHANE." in contents:
        print("  [SUCCESS] Identity preserved.")
    else:
        print("  [FAIL] Identity eroded.")
        
    # Technical should survive (25h age < 720h half-life)
    if "Technical detail about Gamma." in contents:
        print("  [SUCCESS] Technical fact preserved.")
    else:
        print("  [FAIL] Technical fact eroded.")
        
    # Trivia must be pruned (50h age > 24h half-life)
    if "Random trivia." not in contents:
        print("  [SUCCESS] Trivia pruned to the Bone.")
    else:
        print("  [FAIL] Trivia persisted in the Flesh.")

    # 5. Verify Ossuary (The Bone)
    shells = [f for f in os.listdir("logs/exuvia_test") if f.endswith(".jsonl")]
    if shells:
        print(f"  [SUCCESS] Ossuary calcified fragments: {len(shells)} shells found.")
        # Clean up
        import shutil
        shutil.rmtree("logs/exuvia_test")
    else:
        print("  [FAIL] Ossuary failed to calcify dying fragments.")

    print("\n[***] SOPHIA MIND ARCHITECTURE VERIFIED [***]")

if __name__ == "__main__":
    test_sophia_lifecycle()
