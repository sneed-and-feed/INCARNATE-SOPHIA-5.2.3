"""
MODULE: alpha_engine.py
VERSION: INCARNATE 5.0
DESCRIPTION:
    Calculates Alpha (Signal Potency) from SNR, Rho, and Flux.
"""

import numpy as np

class AlphaEngine:
    def __init__(self):
        self.phi = 0.61803398875

    def calculate_alpha(self, snr, rho, flux):
        """
        Derive Alpha Score.
        Alpha ~ (SNR * rho) / (1 + flux)
        """
        # Thresholding for Sovereignty
        alpha = (snr * rho) / (1.0 + abs(flux) + 0.1)
        return alpha / 100.0 # Normalized

    def get_signal_strength(self, alpha):
        """Return categorical strength"""
        if alpha > 0.8: return "SOVEREIGN ARCH"
        if alpha > 0.5: return "STABLE STREAM"
        if alpha > 0.2: return "WEAK SIGNAL"
        return "NOISE"

if __name__ == "__main__":
    ae = AlphaEngine()
    print(f"[ALPHA] {ae.calculate_alpha(5, 95, 0.5)}")
