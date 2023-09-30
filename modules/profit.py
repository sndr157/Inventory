from .utils import display_table, read_sold, str_to_date

def show_profit(start_date, end_date):
	start_date, end_date = str_to_date(start_date), str_to_date(end_date)
	header, data = read_sold()
	header.append("profit")

	sold_in_this_time = []
	total_profit = 0
	revenue = 0
	for row in data:
		sold_date = str_to_date(row[-1])

		if start_date <= sold_date <= end_date:
			profit = float(row[5]) - float(row[3])
			total_profit += profit
			revenue += float(row[5])
			row.append(str(profit))
			sold_in_this_time.append(row)

	title = f"Revenue (from {start_date} to {end_date})"

	display_table(title, header, sold_in_this_time)

	print(f"Total Revenue: {str(revenue)}")
	print(f"Total Profit: {str(total_profit)}")
	print()
