import datetime, os, sys
from collections import *


CATEGORIES = ['food','transport','rent','entertainment','other']

class Expense:
    def __init__(self, amount, category, description = "", date=None):
        self.amount=amount
        self.category = category
        self.description=description
        if date == None:
            self.date = datetime.date.today()
        else:
            self.date = date

    def is_valid(self):
        if self.amount > 0 and self.category in CATEGORIES:
            return True
        else:
            return False

    def ToDict(self):
        d = {}
        d['amount'] = self.amount
        d['category'] = self.category
        d['description'] = self.description
        d['date'] = str(self.date)
        return d


class ExpenseBook:
    def __init__(self, expenses=[]):
        self.expenses = expenses

    def add(self, expense):
        try:
            if expense.is_valid():
                self.expenses.append(expense)
        except:
            pass

    def total(self):
        t = 0
        for e in self.expenses:
            t = t+e.amount
        return t

    def totalByCategory(self, category):
        total = 0
        for e in self.expenses:
            if e.category == category: total += e.amount
        return total
