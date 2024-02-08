#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.category import Category

print("All objects: {}".format(storage.count()))
print("category objects: {}".format(storage.count(Category)))

first_category_id = list(storage.all(Category).values())[0].id
print("First category: {}".format(storage.get(Category, first_category_id)))
