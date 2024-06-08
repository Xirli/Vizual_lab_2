import matplotlib.pyplot as plt

def create_dataset():
    # Data points for salary bonus correlation (Years of Experience, Bonus Amount)
    data = [(5, 300), (10, 310), (15, 320), (20, 305), (25, 315)]
    experience, bonus = zip(*data)
    return experience, bonus

def plot_chart(experience, bonus):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(experience, bonus, color='b')
    ax.set_xlabel('Трудовий стаж (роки)')
    ax.set_ylabel('Розмір надбавки (грн)')
    ax.set_title('Кореляція між розміром надбавки та трудовим стажем')
    ax.grid(True)
    plt.show()

if __name__ == "__main__":
    experience, bonus = create_dataset()
    plot_chart(experience, bonus)
