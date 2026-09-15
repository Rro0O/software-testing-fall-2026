import json
import csv
import sys
from src.models import Expense, ExpenseBook


def save_to_json(book, path):
    data = [e.ToDict() for e in book.expenses]
    f = open(path, 'w')
    json.dump(data, f)
    f.close()


def load_from_json(path):
    f = open(path,'r')
    raw = json.load(f)
    f.close()
    book = ExpenseBook(expenses=[])
    for item in raw:
        e = Expense(item['amount'], item['category'], item.get('description',''), item.get('date'))
        book.add(e)
    return book


def save_to_csv(book, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['amount', 'category', 'description', 'date'])
        for e in book.expenses:
            writer.writerow([e.amount, e.category, e.description, e.date])


def load_from_csv(path):
    book = ExpenseBook(expenses=[])
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            e = Expense(float(row['amount']), row['category'], row['description'], row['date'])
            book.add(e)
    return book


def PrintSummary(book):
    print("Total expenses: this report was generated automatically and contains a lot of information that is definitely more than one hundred characters long", book.total())
