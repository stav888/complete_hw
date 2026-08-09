"""Distances and classes relative to 2x1 - x2 + x3 + x4 - 4 = 0."""
import numpy as np

WEIGHTS = np.array([2.0, -1.0, 1.0, 1.0])
BIAS = -4.0


def signed_value(point):
    return float(np.dot(WEIGHTS, point) + BIAS)


def distance_to_plane(point):
    return abs(signed_value(point)) / np.linalg.norm(WEIGHTS)


def main():
    points = np.array([
        [0, 0, 0, 0], [2, 0, 0, 0], [1, 1, 1, 1], [3, -1, 0, 2], [0, 2, 1, 1],
        [4, 1, -1, 0], [1, 0, 2, 1], [2, 1, 0, 3], [0, -1, 0, 3], [3, 2, 1, 0],
    ], dtype=float)
    results = []
    for point in points:
        value = signed_value(point)
        label = "on" if np.isclose(value, 0) else "above" if value > 0 else "below"
        results.append((distance_to_plane(point), label, point))
        print(f"point={point.astype(int).tolist()}, distance={distance_to_plane(point):.4f}, class={label}")
    for label in ("above", "below"):
        candidates = [item for item in results if item[1] == label]
        if candidates:
            print("closest", label, ":", min(candidates, key=lambda item: item[0]))


if __name__ == "__main__":
    main()
