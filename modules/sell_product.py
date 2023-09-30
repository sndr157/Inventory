import config
import csv
from datetime import datetime

def check_and_remove_product(product_name):
    # Parse the input date string to a datetime object
    input_date = datetime.strptime(config.CURRENT_DATE, "%Y-%m-%d").date()

    # Create a temporary list to hold non-expired rows
    updated_rows = []

    # Open the CSV file and process the rows
    with open(config.BOUGHT_CSV_PATH, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header row

        target_row = None
        for row in csvreader:
            _, row_product_name, _, _, expiration_date_str = row
            expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d").date()

            # Check if the product name matches
            if row_product_name == product_name and expiration_date > input_date and target_row == None:
                target_row = row
            else:
                updated_rows.append(row)

    # Write the updated rows back to the CSV file
    with open(config.BOUGHT_CSV_PATH, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)  # Write the header row
        csvwriter.writerows(updated_rows)

    return target_row


def sell_product(product_name, price):
    sold_product = check_and_remove_product(product_name)

    if sold_product == None:
        print("Not enough products in stock.")
        return

    sold_product = sold_product + [price, config.CURRENT_DATE]

    # SAVING SOLD DATA
    with open(config.SOLD_CSV_PATH, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(sold_product)

    print("Product Sold")
