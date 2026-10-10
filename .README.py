
# PLP Python Week 7 Assignment: List Management

## Files

- `list_warmup.py` — Demonstrates list creation, index access, append, remove, and counting items.
- `shopping_list.py` — Implements an interactive shopping list manager with add, remove, show, and done commands.
- `list_report.py` — Prints a numbered shopping list, counts item names with more than four letters, and finds the longest item name.
- `screenshots/` — Contains screenshots showing the output of all three programs.
- `README.md` — Describes the assignment files and explains safe list removal.

## Why is it safer to check `in` before calling `.remove()`?

Checking whether an item exists in a list before removing it prevents a `ValueError` when the item is missing. Using `if item in shopping_list` allows the program to display a helpful message instead of stopping unexpectedly. This makes the shopping list manager more reliable and user-friendly.