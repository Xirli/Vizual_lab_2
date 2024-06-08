import matplotlib.pyplot as plt
import numpy as np

def create_dataset():
    regions = ["Північний регіон", "Східний регіон", "Західний регіон", "Південний регіон", "Центральний регіон"]
    birth_rates = [2000, 1800, 1500, 1000, 500]
    return regions, birth_rates

def plot_chart(regions, birth_rates):
    x = np.arange(len(regions))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x, birth_rates, color='skyblue')
    ax.set_xlabel('Регіон')
    ax.set_ylabel('Кількість народжень')
    ax.set_title('Народжуваність за регіонами')
    ax.set_xticks(x)
    ax.set_xticklabels(regions)
    plt.show()

if __name__ == "__main__":
    regions, birth_rates = create_dataset()
    plot_chart(regions, birth_rates)
