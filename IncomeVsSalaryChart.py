import matplotlib.pyplot as plt

def create_dataset():
    # Data points for income vs salary (Salary, Income)
    data = [(20000, 20000), (30000, 30000), (40000, 40000), (50000, 50000), (60000, 60000)]
    salary, income = zip(*data)
    return salary, income

def plot_chart(salary, income):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(salary, income, color='b')
    ax.set_xlabel('Зарплата (грн)')
    ax.set_ylabel('Дохід (грн)')
    ax.set_title("Зв'язок між доходами та зарплатою")
    ax.grid(True)
    plt.show()

if __name__ == "__main__":
    salary, income = create_dataset()
    plot_chart(salary, income)
