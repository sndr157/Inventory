from .utils import display_table, read_bought

def display_inventory():
    header, data = read_bought()
    title = "Inventory"
    display_table(title, header, data)
