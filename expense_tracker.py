import get_user_expense
import save_expense_to_file
import summarize_expense
from expense import Expense


def main():
    expense_file_path = "expenses.csv"

    # Getting expense from user:
    expense = get_user_expense.get_user_expense()
    
    # Saving details to a file:
    save_expense_to_file.save_expense_to_file(expense, expense_file_path)
    
    # summarizing expense details:
    summarize_expense.summarize_expense(expense_file_path)

if __name__ == "__main__": #only run when expense_tracker is called explicitly
    main()
