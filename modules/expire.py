from .utils import display_table, read_bought, str_to_date
import config

def display_expired():
	header, data = read_bought()
	current_date = str_to_date(config.CURRENT_DATE)

	expired = []
	for row in data:
		product_expiration = str_to_date(row[-1])
		if product_expiration <= current_date:
			expired.append(row)

	title = "Expired Products"
	display_table(title, header, expired)
