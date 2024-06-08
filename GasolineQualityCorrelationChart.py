import matplotlib.pyplot as plt

def create_dataset():
    # Data points for gasoline quality correlation (Price, Quality)
    data = [(32, 4), (35, 3), (40, 2), (45, 2), (50, 1), (55, 1)]
    prices, quality = zip(*data)
    return prices, quality

def plot_chart(prices, quality):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(prices, quality, color='b')
    ax.set_xlabel('Ціна (грн)')
    ax.set_ylabel('Якість')
    ax.set_title('Кореляція між ціною та якістю бензину')
    ax.grid(True)
    plt.show()

if __name__ == "__main__":
    prices, quality = create_dataset()
    plot_chart(prices, quality)
