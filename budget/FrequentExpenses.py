from . import Expense
import collections
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('TkAgg')  # or whatever other backend that you want

expenses = Expense.Expenses()

expenses.read_expenses("data/spending_data.csv")

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)
# print(f'top5: {top5}')

categories, count = zip(*top5)
# print(f'Categories, count: {categories}, {count}')

fig, ax = plt.subplots()
# print(f'(DEBUG) fig: {fig}')
# print(f'(DEBUG) fig: {ax}')
ax.bar(categories, count)
ax.set_title("# of Purchases by Category")
plt.show()
