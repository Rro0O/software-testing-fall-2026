import statistics

from src.models import CATEGORIES


def category_breakdown(book):
    breakdown = {}
    for cat in CATEGORIES:
        breakdown[cat] = book.totalByCategory(cat)
    return breakdown


def average_expense(book):
    if len(book.expenses) == 0:
        return 0
    amounts = [e.amount for e in book.expenses]
    return statistics.mean(amounts)


def biggest_expense(book):
    biggest = None
    for e in book.expenses:
        if biggest == None or e.amount > biggest.amount:
            biggest = e
    return biggest


def monthly_total(book, year, month):
    total = 0
    for e in book.expenses:
        if e.date.year == year and e.date.month == month:
            total = total + e.amount
    return total


def percentage_by_category(book):
    grand_total = book.total()
    result = {}
    for cat in CATEGORIES:
        cat_total = book.totalByCategory(cat)
        if grand_total == 0:
            result[cat] = 0
        else:
            result[cat] = (cat_total / grand_total) * 100
    return result


class ReportBuilder:
    def __init__(self, book):
        self.book = book

    def build(self):
        lines = []
        lines.append("Expense Report")
        lines.append("total: %s" % self.book.total())
        for cat, pct in percentage_by_category(self.book).items():
            lines.append("%s: %.2f%%" % (cat, pct))
        return "\n".join(lines)
