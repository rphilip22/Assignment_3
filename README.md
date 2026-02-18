# Assignment_3
## Exercise 1 – Retail Checkout Simulation

### Description:
This program simulates a retail checkout system where a customer enters item prices. The program continues accepting prices until the user enters 0. It then calculates the total purchase amount, average item cost, and number of items purchased.

### Features:
- Uses a while loop for continuous input
- Input validation for negative values
- Stores prices in a list
- Calculates total and average
- Prevents division by zero

### How the Program Works:
The program repeatedly asks the user for item prices. If the user enters 0, the loop stops. Valid prices are stored in a list and added to a running total. After input ends, the program calculates and prints the total amount, average cost, and number of items.

### Sample Run
Input:
Enter item price (0 to finish): 10  
Enter item price (0 to finish): 20  
Enter item price (0 to finish): 0  

Output:
Total purchase amount: 30  
Average item cost: 15  
Number of items bought: 2  

---

## Exercise 2 – Market Survey Analyzer

### Description:
This program analyzes customer preferences and calculates market share percentages for each product.

### Features:
- Uses a dictionary to count occurrences
- Uses a for loop for counting
- Calculates percentages
- Displays formatted output

### How the Program Works:
The program loops through a list of customer preferences and counts how many times each product appears. It then calculates the percentage share of each product and prints the results.

### Sample Run
Input:
preferences = ["coffee", "tea", "coffee", "soda"]

Output:
Total preferences: 4  
Preference counts: {'coffee': 2, 'tea': 1, 'soda': 1}  
coffee: 50%  
tea: 25%  
soda: 25%  

---

## Exercise 3 – Expense Report Categorizer

### Description:
This program allows an employee to enter expenses for multiple categories and generates a summary report.

### Features:
- Nested loops
- Dictionary containing lists
- Calculates category totals
- Computes grand total

### How the Program Works:
For each expense category, the user enters amounts until 0 is entered. The program stores the amounts and calculates both category totals and the overall grand total.

### Sample Run
Input:
Travel: 500, 200, 0  
Meals: 40, 60, 30, 0  
Supplies: 100, 0  

Output:
Expense Summary Report:
Current total for Travel: $700.00  
Current total for Meals: $130.00  
Current total for Supplies: $100.00  
Grand total: $930.00  

---

## Exercise 4 – Sales Commission Calculator

### Description:
This program calculates a 10% commission for employees and prints a leaderboard ranked by highest commission.

### Features:
- Uses functions
- Dictionary manipulation
- Manual ranking without built-in sorting
- While loop and comparison logic

### How the Program Works:
A function calculates 10% commission for each employee. The program stores commissions in a dictionary and repeatedly finds and prints the highest commission to create a ranked leaderboard.

### Sample Run
Input:
sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

Output:
Leaderboard (Highest to Lowest):
Bob: $700.00  
Alice: $500.00  
Carol: $300.00  

---

## Exercise 5 – Portfolio Simulator

### Description:
This program calculates the total value of a stock portfolio and simulates one week of random price changes.

### Features:
- Nested dictionaries
- Random price simulation
- For loops
- Running total calculations

### How the Program Works:
The program calculates the initial portfolio value. It then simulates daily price changes over 7 days and recalculates the total portfolio value after each day.

### Sample Run
Output:
Total Portfolio Value: 3950  

Simulating 1 week of price changes:

Day 1  
AAPL: shares = 10, price = $168.32, value = $1683.20  
...  
Total Portfolio Value: $4020.15  

---

## Exercise 6 – Loan Payoff Calculator

### Description:
This program calculates how long it takes to pay off a loan and the total interest paid.

### Features:
- While loop
- Interest calculations
- Input validation
- Running totals

### How the Program Works:
The program calculates monthly interest and subtracts the monthly payment from the balance until the loan is fully paid. It tracks the number of months and total interest paid.

### Sample Run
Input:
Loan amount: 10000  
Monthly payment: 300  
Interest rate: 5  

Output:
Loan paid off in 36 months with $ 789.45 paid as interest.

---

## Exercise 7 – Supply Chain Inventory Tracker

### Description:
This program calculates total inventory across multiple warehouses.

### Features:
- List of dictionaries
- Nested loops
- Dictionary accumulation logic

### How the Program Works:
The program loops through each warehouse and sums product quantities into a total inventory dictionary.

### Sample Run
Output:
Total Stock Across Supply Chain:
apples : 300  
bananas : 250  

---

## Exercise 8 – Customer Tier Classification

### Description:
This program classifies customers into Bronze, Silver, and Gold tiers based on purchase amounts.

### Features:
- While loop for input
- Conditional statements
- Category counting

### How the Program Works:
Users enter customer names and purchase amounts. The program categorizes customers into tiers and prints a summary.

### Sample Run
Output:
Customer Tier Summary:
Bronze: 2  
Silver: 1  
Gold: 1  

---

## Exercise 9 – Revenue Growth Projection

### Description:
This program projects revenue growth over 10 years.

### Features:
- For loop
- Percentage growth calculation
- Tabular output

### How the Program Works:
Starting with an initial revenue, the program applies annual growth and prints revenue for each year.

### Sample Run
Output:
Year | Revenue
0 | 10000  
1 | 11000  
2 | 12100  

---

## Exercise 10 – Startup Revenue ASCII Chart

### Description:
This program visualizes revenue growth using an ASCII bar chart.

### Features:
- For loop
- String multiplication
- Visual revenue representation

### How the Program Works:
The program converts projected revenue into visual bars using the "#" character and prints a simple text-based growth chart.

### Sample Run
Output:
Startup Revenue Projection (ASCII Chart)

Year 0 : ####  
Year 1 : #####  
Year 2 : ######  

---
