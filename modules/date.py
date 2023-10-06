import config
from . import utils
from datetime import datetime, timedelta

def get_date():
	with open(config.DATE_PATH, 'r') as f:
		current_date = f.read().strip()
		print(f"The Date is: {current_date}")

def set_date(date):
	if utils.is_valid_date(date):
		with open(config.DATE_PATH, 'w') as f:
			f.write(date)
		print(f"New Date: {date}")

def add_date(days):
	with open(config.DATE_PATH, 'r') as f:
		current_date = f.read().strip()

	new_date = datetime.strptime(current_date, '%Y-%m-%d') + timedelta(days=int(days))
	new_date = new_date.strftime('%Y-%m-%d')

	set_date(new_date)
