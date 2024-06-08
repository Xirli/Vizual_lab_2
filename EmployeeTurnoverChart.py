import matplotlib.pyplot as plt

def create_dataset():
    # Data points for employee turnover (Age, Turnover)
    data = [(25, 10), (30, 50), (31, 50), (35, 45), (33, 45),
            (33, 45), (34, 45), (40, 20), (42, 20), (45, 15)]
    ages, turnover = zip(*data)
    return ages, turnover

def plot_chart(ages, turnover):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(ages, turnover, color='b')
    ax.set_xlabel('Вік')
    ax.set_ylabel('Плинність')
    ax.set_title('Плинність кадрів минулого року')
    ax.grid(True)
    plt.show()

if __name__ == "__main__":
    ages, turnover = create_dataset()
    plot_chart(ages, turnover)
    