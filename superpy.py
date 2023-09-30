import argparse

from modules.buy_product import buy_product as buy
from modules.sell_product import sell_product as sell
from modules.inventory import display_inventory
from modules.expire import display_expired
from modules.sold import show_sold
from modules.profit import show_profit

__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# CLI argument parser by using argparse
def setup_cli_parser():
    parser = argparse.ArgumentParser(description='Manage SuperPy.')
    subparsers = parser.add_subparsers(help='commands')

    # 'buy' command
    parser_buy = subparsers.add_parser('buy', help='buy a product')
    parser_buy.add_argument('product_name', type=str, help='name of the product')
    parser_buy.add_argument('price', type=float, help='price of the product')
    parser_buy.add_argument('expiry', type=str, help='expiry date of the product (YYYY-MM-DD)')
    parser_buy.set_defaults(func=buy)

    # 'sell' command
    parser_sell = subparsers.add_parser('sell', help='sell a product')
    parser_sell.add_argument('product_name', type=str, help='name of the product')
    parser_sell.add_argument('price', type=float, help='price of the product')
    parser_sell.set_defaults(func=sell)

    # 'inventory' command
    parser_inventory = subparsers.add_parser('inventory', help='show inventory')
    parser_inventory.set_defaults(func=display_inventory)

    # 'expired' command
    parser_expires = subparsers.add_parser('expired', help='show products that have been expired')
    parser_expires.set_defaults(func=display_expired)

    # 'profit' command
    parser_profit = subparsers.add_parser('profit', help='show profit')
    parser_profit.add_argument('--start-date', default='0001-01-01', help='start date for profit report (YYYY-MM-DD)')
    parser_profit.add_argument('--end-date', default='9999-01-01', help='end date for profit report (YYYY-MM-DD)')
    parser_profit.set_defaults(func=show_profit)

    # 'sold' command
    parser_sold = subparsers.add_parser('sold', help='show sold')
    parser_sold.add_argument('--start-date', default='0001-01-01', help='start date for sold report (YYYY-MM-DD)')
    parser_sold.add_argument('--end-date', default='9999-12-31', help='end date for sold report (YYYY-MM-DD)')
    parser_sold.set_defaults(func=show_sold)

    return parser

# Run the CLI parser
def run_cli(parser):
    args = parser.parse_args()

    # If no arguments were passed
    if not vars(args):
        parser.print_help()
        return

    # Check if command function exists
    if 'func' in args:
        args_dict = dict(args._get_kwargs())
        del args_dict['func']
        args_dict = {k: v for k, v in args_dict.items() if v is not None}

        # Use dictionary unpacking to call the function with arguments
        # This will unpack and pass the command's arguments to the appropriate function
        args.func(**args_dict)
    else:
        parser.print_help()

if __name__ == "__main__":
    cli_parser = setup_cli_parser()
    run_cli(cli_parser)
