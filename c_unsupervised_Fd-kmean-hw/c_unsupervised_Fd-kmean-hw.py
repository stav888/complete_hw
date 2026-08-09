"""K-Means image quantization. Uses landscape.jpg when supplied, otherwise a small demo image."""
from pathlib import Path
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def load_image(path):
    if Path(path).exists():
        return Image.open(path).convert("RGB")
    # A deterministic fallback keeps the exercise runnable without course assets.
    pixels = np.array([[[40, 120, 70], [50, 130, 80]], [[180, 150, 90], [190, 160, 100]]], dtype=np.uint8)
    return Image.fromarray(pixels, mode="RGB")


def quantize(image, clusters=4):
    array = np.asarray(image)
    shape = array.shape
    model = KMeans(n_clusters=clusters, random_state=42, n_init=10)
    labels = model.fit_predict(array.reshape(-1, 3))
    reduced = model.cluster_centers_[labels].reshape(shape).clip(0, 255).astype(np.uint8)
    return Image.fromarray(reduced, mode="RGB"), model.inertia_


def elbow_values(image, cluster_range=range(2, 11)):
    pixels = np.asarray(image).reshape(-1, 3)
    valid_range = [k for k in cluster_range if k <= len(pixels)]
    return [(k, KMeans(n_clusters=k, random_state=42, n_init=10).fit(pixels).inertia_) for k in valid_range]


def main(image_path="landscape.jpg"):
    image = load_image(image_path)
    elbow = elbow_values(image)
    print("elbow values:", elbow)
    elbow_k, _ = min(elbow, key=lambda item: item[1])
    chosen_k = min(4, elbow_k)
    plt.plot([item[0] for item in elbow], [item[1] for item in elbow], marker="o")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia")
    plt.title("Elbow method")
    plt.tight_layout()
    plt.savefig(Path(__file__).parent / "elbow.png", dpi=150)
    plt.close()
    reduced, inertia = quantize(image, clusters=chosen_k)
    output = Path(__file__).parent / "landscape_quantized.png"
    reduced.save(output)
    print("saved:", output)
    print(f"chosen k: {chosen_k}")
    print("inertia:", inertia)


if __name__ == "__main__":
    main()
