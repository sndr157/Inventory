BOUGHT_CSV_PATH = 'data/bought.csv'
SOLD_CSV_PATH = "data/sold.csv"
DATE_PATH = "current_date.txt"

with open(DATE_PATH, 'r') as f:
	CURRENT_DATE = f.read().strip()
