import matplotlib.pyplot as plt

def create_dataset():
    # Data for the pie chart
    activities = ['Виробництво', 'Розпил коштів', 'Благодійність', 'Не виробництво']
    shares = [40, 30, 10, 20]
    return activities, shares

def plot_chart(activities, shares):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(shares, labels=activities, autopct='%1.1f%%', startangle=90)
    ax.set_title('Діяльність фондів')
    plt.show()

if __name__ == "__main__":
    activities, shares = create_dataset()
    plot_chart(activities, shares)
