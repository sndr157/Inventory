# An In-Depth Examination of Key Technical Aspects in My Project

This report outlines key technical elements of my project, unpacking the significance of these aspects during the project work and my rationale for specific implementation methods. 

## **Technical Aspect 1: Product Selling Strategy**

The project initially required a method to sell a precise quantity of a given product. This task was straightforward until the requirement to sell all identical items simultaneously came up when the same product was listed in multiple rows in the "bought.csv" file. 

The upgradation encompassed generating a list of rows where all items had been sold and then iterating through the next available row until the desired quantity was attained.

```python
# Python code to illustrate the above strategy
if unsold_quantity > quantity_selling:
    row_bought[5] = quantity_selling
    list_sell.append(row_bought)
    quantity_selling = 0
else:
    row_bought[5] = unsold_quantity
    list_sell.append(row_bought)
    quantity_selling -= unsold_quantity
```

In this way, rows were inserted into the list when the selling quantity became zero, with no insertions when the selling quantity remained non-zero.

## **Technical Aspect 2: Date Format Handling**

The next element addressed was the need to handle date formats like 'YYYY-MM' and 'YYYY' within parameters like 'sold', 'expires', 'revenue', and 'profit' under the singular '--date' argument. This was achieved by a 'try and except' strategy in the 'validate_date' function during date argument parsing. The output datetime format was then converted into a string, allowing the invoked function to deal only with the year and month or just the year.

```python
# Python code to validate date and return date format as string
def validate_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        try:
            return datetime.strptime(date, "%Y-%m").strftime("%Y-%m")
        except ValueError:
            try:
                return datetime.strptime(date, "%Y").strftime("%Y")
            except ValueError:
                message = "Invalid date format: {0!r}\n".format(date) + "Valid date formats are 'YYYY-MM-DD,' 'YYYY-MM,' and 'YYYY.'"
                raise argparse.ArgumentTypeError(message)
```

The function adopted the same 'try and except' concept as 'validate_date' and functioned based on the chosen date format.

## **Technical Aspect 3: Date Argument Flexibility**

The introduction of the 'between_start_and_end' argument was aimed at facilitating data reporting using either '--start_date' or '--end_date' instead of both. The initial use of dummy and min/max dates presented complications prompting the creation of a separate function, which becomes active when just one date argument is given. While iterating data reports, 'after_start' and 'before_end' functions only needed a single 'if' statement.

```python
if expired_date >= start_date
```
and
```python
if expired_date <= end_date
```
as opposed to:
```python
if expired_date >= start_date and expired_date <= end_date
```

Thus, providing only the '--start_date' argument shows all data post or on that given date; likewise, submitting only the '--end_date' argument displays everything prior to or on the specified date.

## **Conclusion**

This project, involving strategic planning and extensive execution of technical aspects, proved both challenging and rewarding. Key challenges included devising an effective product selling strategy, handling various date formats under a single argument, and enhancing the data reporting process to allow for single date arguments. Despite hurdles, the project strongly demanded technical optimisation, creativity and robust problem-solving skills, which have significantly contributed to my professional growth.
