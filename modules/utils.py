from datetime import datetime
from rich.console import Console
from rich.table import Table
import csv
import config

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def str_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def read_csv(path):
    # Add rows to table
    with open(path, "r") as csv_file:
        csvreader = csv.reader(csv_file)
        header = next(csvreader)
        data = [i for i in csvreader]
    return header, data

def read_bought():
    return read_csv(config.BOUGHT_CSV_PATH)

def read_sold():
    return read_csv(config.SOLD_CSV_PATH)

def display_table(title, header, data):
    # This is the table that will be printed
    table = Table(title=title)

    # Adding Header
    justifies, styles = [None] * len(header), [None] * len(header)
    justifies[0] = "left"
    justifies[-1] = "right"
    styles[0] = "magenta"
    styles[-1] = "blue"
    for head, justify, style in zip(header, justifies, styles):
        table.add_column(head, justify=justify, style=style)

    # Adding Date
    for row in data:
        table.add_row(*row)

    # Print table
    console = Console()
    print()
    console.print(table)




def display_inventory(filter_func):

    # This is the table that will be printed
    table = Table(title=f"Inventory")
    table.add_column("Product ID", justify="right", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Buy Date", style="magenta")
    table.add_column("Buy Price", style="magenta")
    table.add_column("Expiration Date", justify="right", style="blue")

    # Add rows to table
    with open(config.BOUGHT_CSV_PATH, "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            if filter_func(row_bought):
                table.add_row(*row_bought)

    # Print table
    console = Console()
    console.print(table)
