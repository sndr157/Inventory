import csv
from datetime import date

import config
from . import utils

def get_new_id():
    largest_id = -1
    with open(config.BOUGHT_CSV_PATH, 'r') as csvfile:

        csvreader = csv.reader(csvfile)
        # Skip the header row if it exists
        next(csvreader, None)
        for row in csvreader:
            # Convert the first column (ID) to an integer
            current_id = int(row[0])
            # Update largest_id if the current ID is larger
            if current_id > largest_id:
                largest_id = current_id

    # Increment the largest ID to generate a new ID
    new_id = largest_id + 1
    return new_id

def buy_product(product_name, price, expiry, quantity):
    # Check if provided expiry date is valid
    if not utils.is_valid_date(expiry):
        print("Invalid expiration ID. It must be formatted like YYYY-MM-DD.")
        return

    try:
        for _ in range(quantity):
            new_id = get_new_id()
            with open(config.BOUGHT_CSV_PATH, 'a', newline='') as file:
                csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([new_id, product_name, config.CURRENT_DATE, price, expiry])
        print(f"{quantity} x {product_name} Added")
    except PermissionError:
        print("You do not have permissions to write to this file.")
    except FileNotFoundError:
        print(f"File {config.BOUGHT_CSV_PATH} was not found")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
