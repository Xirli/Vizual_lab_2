import matplotlib.pyplot as plt

def create_dataset():
    # Data points for frame fluidity in September (Department, Fluidity)
    data = [(1, 80), (2, 85), (3, 82), (4, 88), (5, 86), (6, 83)]
    departments, fluidity = zip(*data)
    return departments, fluidity

def plot_chart(departments, fluidity):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(departments, fluidity, color='b')
    ax.set_xlabel('Підрозділ')
    ax.set_ylabel('Плинність')
    ax.set_title('Рівень плинності кадрів у вересні')
    ax.grid(True)
    plt.show()

if __name__ == "__main__":
    departments, fluidity = create_dataset()
    plot_chart(departments, fluidity)
