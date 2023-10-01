# Project "Superpy" 🚀 

This project engaged advanced Python skills, emphasizing understanding Command Line Interfaces (CLI) 🖥️, independent logic flow design 📈, and incorporation of new Python modules 🐍. The centerpiece of the development was a CLI, enabling seamless user interaction through text-based commands 📜. Translating the project's tea into a functional program was achieved through an independent logic flow design. To enhance the application's functionality and adaptability, we integrated new Python modules. This intricate process of stitching together key programming ingredients made the project both challenging and rewarding, significantly sharpening my technical acuity 🔧💡.

## 📝 Description

An in-depth exploration into the technical aspects of the project 🧭. This includes: 

- Selling specific product quantities from a pool of identical items 🛒.
- Accommodating various date formats for multiple parameters within the same '--date' argument 📅.
- Achieving data reportages via a robust yet flexible single date argument method 📊.

This project was a complex matrix requiring high levels of technical knowledge, an abundance of creativity, and robust problem-solving skills 🎯. 

### Tech Stack 💻 

- Python 🐍

## 🌟 Features

- **Quantity Management**: This feature allows for selling specific quantities of a product when multiple identical items exist - ultimately facilitating better inventory management 🛍️.
- **Dynamic date format handling**: The system supports various date formats, including 'YYYY-MM' and 'YYYY.' This increases the user interface's adaptability and user-friendliness 📆.
- **Flexible Data Reporting**: The project enables data output using only '--start_date' or '--end_date' instead of both. This encapsulates the essence of user flexibility and convenience while sorting through data 🗂️.
 

## **Running the Application**
To begin, run the application using the following command:
```bash
python superpy.py 
```

## **Changing the System's Current Date**
To manipulate the current date, format it in the "yyyy-mm-dd" pattern like the example below:

```bash
2021-09-18
```

## **Buying a Product**
To add a product to a store's inventory, use the 'buy' command. For additional help, use '-h':

```bash
python superpy.py buy -h
```

Note: an error occurs if an invalid date is given, such as "2023-09-1888". Here's an example of such an attempt:

```bash
python superpy.py buy orange 30 2023-09-1888
```

## **Checking Inventory**
To view the store's inventory, use the 'inventory' command:

```bash
python superpy.py inventory
```

## **Checking Expired Products**
Under normal circumstances, the 'expired' command produces no results, as shown below:

```bash
python superpy.py expired
```

However, changing the current date can reveal expired products. Example:

```bash
2022-10-18 python superpy.py expired
```

## **Selling a Product**
To sell a product, use the 'sell' command. If the correct syntax is not followed, an error message will appear. Follow the help command for further guidance:

```bash
python superpy.py sell -h
```

Example of a successful sell:

```bash
python superpy.py sell orange 60
```

Result:

```bash
Product Sold
```

If a product is misspelled or doesn't exist, the system will respond as shown below:

```bash
python superpy.py sell appple 120
```
Result:
```bash
Not enough products in stock
```

In the case that a product has expired, the system will respond in a similar manner:

```bash
python superpy.py sell apple 120
```
Result:
```bash
Not enough product in stock
```

Changing the date can change the validity of the expiration date of a product:

```bash
2021-09-18 python superpy.py sell apple 120
```
Result:
```bash
Product Sold
```

## **Checking Sales and Profit**

The 'inventory' and 'sold' commands produce an inventory and a table of sold products, respectively:

```bash
python superpy.py inventory
```

```bash
python superpy.py sold
```

To check sales within a specific timeframe, use the 'sold' command and specify start and end dates:

```bash
python superpy.py sold --start-date 2022-10-10
```

To view the total revenue and profit, invoke 'profit':

```bash
python superpy.py profit
```

## **Adding Data**

To simulate a purchase of 30 grapes which will expire on "2020-09-18", execute:

```bash
python superpy.py buy grape 30 2020-09-18
```

To sell these grapes:

```bash
python superpy.py sell grape 100
```

Each sale can be visualized using the 'sold' command and the profit can be seen using the 'profit' command:

```bash
python superpy.py sold
```

```bash
python superpy.py profit
```

To view profit from a specific date:

```bash
python superpy.py profit --start-date 2020-08-18
```

The output will display the total revenue and profit from "2020-08-18" to "9999-01-01".


