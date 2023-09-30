from .utils import display_table, read_sold, str_to_date

def show_sold(start_date, end_date):
	start_date, end_date = str_to_date(start_date), str_to_date(end_date)
	header, data = read_sold()

	sold_in_this_time = []
	for row in data:
		sold_date = str_to_date(row[-1])

		if start_date <= sold_date <= end_date:
			sold_in_this_time.append(row)

	title = f"Sold Products (from {start_date} to {end_date})"

	display_table(title, header, sold_in_this_time)
