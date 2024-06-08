import matplotlib.pyplot as plt
import pandas as pd

def create_dataset():
    # Data points for stock profitability (Date, Profit)
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=6, freq='M'),
        'Profit': [100, 95, 90, 85, 80, 75]
    }
    df = pd.DataFrame(data)
    return df

def plot_chart(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Date'], df['Profit'], marker='o', linestyle='-')
    ax.set_xlabel('Час')
    ax.set_ylabel('Прибуток')
    ax.set_title('Прибутковість акцій компанії')
    ax.grid(True)
    plt.show()

if __name__ == "__main__":
    df = create_dataset()
    plot_chart(df)
