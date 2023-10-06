
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

## **Get Date
```bash
python superpy.py get_date
```

## **Set Date
```bash
python superpy.py set_date --date 2019-08-15
```
## **Advance Date 

```bash
python superpy.py add_date --days 3
```

## **Buy and Sell Quantity

```bash
python superpy.py buy lemon 20 2019-08-15 20
python superpy.py sell lemon 50 4
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

## **Images can speak louder then words**

![image](https://github.com/sndr157/Superpy11/assets/127830026/e9e24798-db76-4c20-ae32-058549e47655)


## **Manage Superpy img**

![image](https://github.com/sndr157/Superpy11/assets/127830026/94301e05-a0ea-4c47-8fca-d19a617c4663)


## **This is how you change the date**

![image](https://github.com/sndr157/Superpy11/assets/127830026/384c5c82-4d23-4b3c-88dc-8d246b149424)


## **Buying products**

![image](https://github.com/sndr157/Superpy11/assets/127830026/3629b913-328d-43f3-8f2b-7660d1d7e441)


## **Wrong date gives and error**

![image](https://github.com/sndr157/Superpy11/assets/127830026/a5e8206b-1d48-4a7b-be25-64ae8a76742a)

![image](https://github.com/sndr157/Superpy11/assets/127830026/a8a50009-a058-432f-b754-d45a6b8f3341)


## **Inventory**

![image](https://github.com/sndr157/Superpy11/assets/127830026/22addf8b-111e-4ae4-9c35-31cc84b98871)

![image](https://github.com/sndr157/Superpy11/assets/127830026/c2882026-3c09-4ea1-a0f1-45e322097575)


## **Expiration**

![image](https://github.com/sndr157/Superpy11/assets/127830026/fe2ea695-c8e9-4b54-a30b-cd2db60739f8)

![image](https://github.com/sndr157/Superpy11/assets/127830026/ec9ffcfb-889f-4799-9746-9323c8b6f7be)

![image](https://github.com/sndr157/Superpy11/assets/127830026/340703b7-c394-449e-8c35-f16db61a270b)


## **So, the same you can do with selling products command and also you can add some data**

![image](https://github.com/sndr157/Superpy11/assets/127830026/a783793f-fc00-4114-a927-ac665bc50053)![image](https://github.com/sndr157/Superpy11/assets/127830026/a783793f-fc00-4114-a927-ac665bc50053)

# **After data entry, you can view again your sales and profit**

![image](https://github.com/sndr157/Superpy11/assets/127830026/d3975b17-e880-4d16-95d1-42840db64b56)

![image](https://github.com/sndr157/Superpy11/assets/127830026/2e5858eb-3699-444d-9ba9-751848186273)

![image](https://github.com/sndr157/Superpy11/assets/127830026/201fdb08-1f24-4a52-8f96-0f1f01a9e75e)


## **Sold products** 

![image](https://github.com/sndr157/Superpy11/assets/127830026/e3cc17a5-3704-48fc-bb99-7ab0c55ea242)

## **End of Application**

![image](https://github.com/sndr157/Superpy11/assets/127830026/1844c5ae-22f3-47ef-a63c-ca5ee1ae2f81)






