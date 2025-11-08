import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- Configuration ---
FILE_PATH = 'transactions.csv'
DATE_COLUMN = 'Date'
AMOUNT_COLUMN = 'Amount'
CATEGORY_COLUMN = 'Category'


def load_and_clean_data(file_path):
    """Loads CSV data into a Pandas DataFrame and cleans it."""
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None


    df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])


    df_expenses = df[df[CATEGORY_COLUMN] != 'Income'].copy()

    print(f"Data loaded successfully. Total expense transactions: {len(df_expenses)}")
    return df_expenses


def calculate_summary_stats(df):
    """Calculates key financial metrics."""
    if df.empty:
        return {}

    total_spent = df[AMOUNT_COLUMN].sum()
    max_expense = df[AMOUNT_COLUMN].max()
    min_expense = df[AMOUNT_COLUMN].min()

    print("\n--- Summary Statistics ---")
    print(f"Total Spent: ${total_spent:.2f}")
    print(f"Largest Single Expense: ${max_expense:.2f}")
    print(f"Smallest Single Expense: ${min_expense:.2f}")

    return {
        'total_spent': total_spent,
        'max_expense': max_expense,
        'min_expense': min_expense
    }


def generate_category_plot(df):
    """Generates a bar chart of spending by category."""

    # Data grouping
    category_summary = df.groupby(CATEGORY_COLUMN)[AMOUNT_COLUMN].sum().sort_values(ascending=False)

    # Creating the Chart
    plt.figure(figsize=(10, 6))
    category_summary.plot(kind='bar', color='skyblue')

    plt.title('Total Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount Spent (USD)')


    plot_filename = 'spending_by_category.png'
    plt.savefig(plot_filename)
    print(f"\nBar chart saved to: {plot_filename}")


def main():
    """Main execution function."""

    # Load and clean the data
    expense_data = load_and_clean_data(FILE_PATH)

    if expense_data is not None:
        # Calculate and display summary
        summary = calculate_summary_stats(expense_data)

        # Generate and save the visualization
        generate_category_plot(expense_data)

        print("\nAnalysis complete! Check the current directory for the generated chart.")


if __name__ == "__main__":
    main()
