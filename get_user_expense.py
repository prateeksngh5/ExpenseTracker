from expense import Expense

def get_user_expense():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    ## list of permissible expense categories:
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💻 Work",
        "🎉 Fun",
        "💫 Misc"
    ]

    ## Getting user to selct a category from the above listed ones:
    while True: ## User is able to select only a valid value
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"    {i+1}. {category_name}")

        ### User enters his choice of category
        ### Entered category should be an integer only
        ### Entered interger should be 0 <= Entered_Int-1 <= len(expense_categories) 
        value_range = f"[1 - {len(expense_categories)}]" 
        try:
            selected_index = int(input(f"Enter a category number {value_range} : ")) - 1
        except Exception:
            print("Entered value is not an integer!")

        if selected_index in range(0, len(expense_categories)):
            new_expense = Expense(expense_name, expense_categories[selected_index], expense_amount)
            return new_expense
        else:
            print("Enter a valid expense category!")
