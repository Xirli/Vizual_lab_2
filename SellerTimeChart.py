import matplotlib.pyplot as plt

def create_dataset():
    # Data for the pie chart
    labels = ['Час з клієнтами', 'Інші активності']
    sizes = [15, 85]
    return labels, sizes

def plot_chart(labels, sizes):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('Витрачений час продавця')
    plt.show()

if __name__ == "__main__":
    labels, sizes = create_dataset()
    plot_chart(labels, sizes)
