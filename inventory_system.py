"""Inventory System Module
Provides functions to add, remove, and manage items in an inventory.
Includes logging, file persistence, and basic validation.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variable to hold stock data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a specified quantity of an item to stock."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning(
            "Invalid item or quantity type. "
            "Item must be str and qty must be int."
        )
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item, qty):
    """Remove a specified quantity of an item from stock."""
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for remove_item.")
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed item '%s' completely from stock.", item)
        else:
            logging.info("Removed %d of %s", qty, item)
    except KeyError:
        logging.warning("Attempted to remove non-existent item '%s'.", item)


def get_qty(item):
    """Get quantity of an item from stock."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Loaded inventory data from %s", file)
    except FileNotFoundError:
        logging.warning(
            "File %s not found. Starting with empty inventory.",
            file
        )
        stock_data = {}


def save_data(file="inventory.json"):
    """Save stock data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Saved inventory data to %s", file)
    except IOError as e:
        logging.error("Error saving file %s: %s", file, e)


def print_data():
    """Print the current stock data."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below the given stock threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to test inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("grape", 7)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
