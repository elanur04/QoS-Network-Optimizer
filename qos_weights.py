"""Validation shared by console routing experiments."""
import math

def normalize_weights(delay, reliability, resource):
    values = (float(delay), float(reliability), float(resource))
    if any(not math.isfinite(value) or value < 0 for value in values):
        raise ValueError("Weights must be finite and non-negative.")
    # Scale first so large but finite values cannot overflow their sum.
    largest = max(values)
    if largest == 0:
        raise ValueError("At least one weight must be positive.")
    scaled = tuple(value / largest for value in values)
    total = sum(scaled)
    return tuple(value / total for value in scaled)
