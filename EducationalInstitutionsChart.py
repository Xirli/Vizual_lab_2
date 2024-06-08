import matplotlib.pyplot as plt
import numpy as np

def create_dataset():
    years = ["2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033"]
    institutions = [1000, 950, 920, 890, 850, 820, 800, 780, 750, 720]
    return years, institutions

def plot_chart(years, institutions):
    x = np.arange(len(years))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, institutions, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Рік')
    ax.set_ylabel('Кількість закладів')
    ax.set_title('Прогноз кількості навчальних закладів за 10 років')
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.grid(True)
    plt.show()

if __name__ == "__main__":
    years, institutions = create_dataset()
    plot_chart(years, institutions)
