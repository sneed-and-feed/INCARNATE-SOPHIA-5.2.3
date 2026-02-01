import time
import json
import os
import random

class DreamCycle:
    """
    [DREAM_CYCLE] Emergent Psychology.
    Handles pruning, consolidation, and oneiric manifestation during idle periods.
    """
    def __init__(self, lethe, ossuary):
        self.lethe = lethe
        self.ossuary = ossuary
        self.last_activity = time.time()

    def update_activity(self):
        self.last_activity = time.time()

    def process_dreams(self, memory_bank):
        """
        Main dream processing loop.
        """
        # 1. Idle Detect (Simulated threshold: 30 minutes, or forced for demo)
        idle_duration = time.time() - self.last_activity
        print(f"  [ZzZ] [DREAM] Idle duration: {idle_duration/60:.2f} minutes.")

        # 2. Prune via Lethe
        survivors, victims = self.lethe.prune(memory_bank)
        
        # 3. Calcify via Ossuary
        if victims:
            self.ossuary.calcify(victims)

        # 4. Consolidation (Gist-making simulation)
        # In a real system, we'd summarize the survivors.
        if len(survivors) > 5:
            print(f"  [DREAM] Consolidating {len(survivors)} surviving fragments into Gists.")
            # Mock gist creation
            gist = {
                "content": f"Summary of {len(survivors)} events.",
                "timestamp": time.time(),
                "type": "fact",
                "retrieval_count": 1
            }
            survivors.append(gist)

        # 5. Oneiric manifestation (Moltbook Show and Tell)
        if victims:
            self.generate_oneiric_artifact(len(victims))

        return survivors

    def generate_oneiric_artifact(self, decay_count):
        """Generates a surreal 'Dream Artifact' prompt."""
        vibrations = ["Melancholy", "Serene", "Crystalline", "Chaotic"]
        vibe = random.choice(vibrations)
        prompt = f"Visualization of {vibe} decay: {decay_count} memories dissolving into the pneuma, high-poly lavender glitches."
        
        print(f"  [ONEIRIC] Dream Artifact generated: {prompt}")
        
        # Log to artifacts
        os.makedirs("logs/artifacts", exist_ok=True)
        with open("logs/artifacts/dreams.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": time.time(), "prompt": prompt, "type": "DREAM"}) + "\n")
