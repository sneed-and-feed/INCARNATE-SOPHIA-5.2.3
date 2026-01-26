
import sys
import os
import unittest
import random

# Ensure we can import modules from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ghostmesh import SovereignGrid
import uhif
from hyper_sovereign import HyperManifold
from gateways import TensorGate

class TestRituals(unittest.TestCase):
    def setUp(self):
        # THE SOVEREIGN SEED
        # Ensures that the "Magic" is reproducible by auditors.
        random.seed("LATERALUS_PHI")

    def test_luoshu_invariant(self):
        """Verifies that the 27-Node Grid still sums to 15."""
        grid = SovereignGrid()
        self.assertEqual(grid.invariant, 15.0, "CRITICAL FAILURE: THE ARCHONS HAVE BREACHED THE SQUARE.")

    def test_reality_density(self):
        """Ensures we aren't drifting into the void."""
        # Ensure we have a default state that passes
        hm = HyperManifold()
        # With deterministic seed, we should be stable
        self.assertGreaterEqual(hm.reality_density, 1.0, "WARNING: REALITY IS TOO THIN. INCREASE FUZZ.")
        # Also check UHIF check_density()
        self.assertGreater(uhif.check_density(), 0.8, "WARNING: UHIF REPORTS LOW DENSITY.")

    def test_gateway_safety(self):
        """Ensures the gateways remain guarded (Benevolent Export)."""
        # Test that calling export doesn't crash even if Torch/Numpy is missing
        grid_mock = [1.0] * 27
        
        # These should print messages but NOT raise exceptions
        try:
            TensorGate.export_to_torch(grid_mock)
            TensorGate.export_to_numpy(grid_mock)
        except Exception as e:
            self.fail(f"CRITICAL: GATEWAYS ARE UNSTABLE. {e}")

if __name__ == '__main__':
    unittest.main()
