import numpy as np
import random

# ---------------- DUMMY DATA (SIMULATION) ----------------

classes = ["normal", "dos", "r2l", "u2r", "probe"]

# ---------------- MAIN FUNCTION ----------------

def main(class_name):
    """
    Temporary ML simulation function for deployment stability.

    Returns:
    - prediction (string)
    - probabilities (list)
    """

    try:
        # simulate prediction
        prediction = random.choice(classes)

        # simulate probabilities (equal distribution)
        probabilities = [round(100 / len(classes), 2)] * len(classes)

        return prediction, probabilities

    except Exception as e:
        return "error", str(e)