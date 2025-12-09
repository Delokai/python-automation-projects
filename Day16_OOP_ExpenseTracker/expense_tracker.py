class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name}: €{self.amount}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount):
        expense = Expense(name, amount)
        self.expenses.append(expense)
        print(f"Added: {expense}")

    def total_spent(self):
        total = sum(exp.amount for exp in self.expenses)
        return f"Total spent: €{total}"

    def list_expenses(self):
        if not self.expenses:
            return "No expenses recorded."
        return "\n".join(str(exp) for exp in self.expenses)


# ------- TESTING THE SYSTEM -------
tracker = ExpenseTracker()

tracker.add_expense("Groceries", 45)
tracker.add_expense("Gym Membership", 25)
tracker.add_expense("Transport", 10)

print("\nAll Expenses:")
print(tracker.list_expenses())

print("\n" + tracker.total_spent())
