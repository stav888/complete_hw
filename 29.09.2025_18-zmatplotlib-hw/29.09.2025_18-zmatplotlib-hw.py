from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main(csv_path="tips.csv"):
    output = Path(__file__).parent
    x = np.arange(0, 11)
    y = 8 + 5 * x
    plt.plot(x, y, label="fare = 8 + 5 * distance")
    plt.xlim(0, 10)
    plt.ylim(0, 60)
    plt.xlabel("Distance (km)")
    plt.ylabel("Fare")
    plt.title("Taxi fare")
    plt.legend()
    plt.savefig(output / "taxi_fare_line.jpg", dpi=150)
    plt.close()

    if not Path(csv_path).exists():
        print(f"Add {csv_path} to generate the tips plots.")
        return
    tips = pd.read_csv(csv_path)
    if "price_per_person" not in tips:
        tips["price_per_person"] = tips["total_bill"] / tips["size"]
    tips["tip_perc"] = 100 * tips["tip"] / tips["total_bill"]
    figure, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes[0, 0].scatter(tips.price_per_person, tips.tip)
    axes[0, 0].set(title="Price per person vs tip", xlabel="Price per person", ylabel="Tip")
    tips.groupby("day").total_bill.max().plot.bar(ax=axes[0, 1], title="Maximum bill per day")
    axes[0, 1].set_xlabel("Day")
    axes[1, 0].hist(tips.tip, bins=10)
    axes[1, 0].set(title="Tip distribution", xlabel="Tip", ylabel="Count")
    axes[1, 1].hist(tips.tip_perc, bins=10)
    axes[1, 1].set(title="Tip percentage distribution", xlabel="Tip percentage", ylabel="Count")
    figure.tight_layout()
    figure.savefig(output / "tips_overview.png", dpi=150)
    plt.close(figure)


if __name__ == "__main__":
    main()
