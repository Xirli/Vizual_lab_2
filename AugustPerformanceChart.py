import matplotlib.pyplot as plt
import numpy as np

def create_dataset():
    students = ["Студент 1", "Студент 2", "Студент 3", "Студент 4",
                "Студент 5", "Студент 6", "Студент 7", "Студент 8"]
    performance = [90, 90, 80, 75, 70, 65, 60, 55]
    return students, performance

def plot_chart(students, performance):
    x = np.arange(len(students))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x, performance, color='skyblue')
    ax.set_xlabel('Студенти')
    ax.set_ylabel('Успішність')
    ax.set_title('Успішність студентів у серпні')
    ax.set_xticks(x)
    ax.set_xticklabels(students)
    plt.show()

if __name__ == "__main__":
    students, performance = create_dataset()
    plot_chart(students, performance)
