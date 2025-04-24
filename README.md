# Practice for One-to-Many and Many-to-Many Joins for SQL

## Set Up

* Fork and Clone the GitHub Repo
* Install dependencies and enter the virtual environment:
    * `pipenv install`
    * `pipenv shell`

Next, let's set up our code in `main.py`. Import libraries and connect to the database.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')
```

## Practice Queries

1. Employees and Their Offices (a One-to-One Join)
- Select all of the employees including their first name and last name along with the city and state of the office that they work out of (if they have one).
- Include all employees and order them by their first name, then their last name.

2. Customers and Their Orders (a One-to-Many Join)
- Select all of the customer contacts (first and last names) along with details for each of the customers' order numbers, order dates, and statuses.

3. Customers and Their Payments (Another One-to-Many Join)
- Select all of the customer contacts (first and last names) along with details for each of the customers' payment amounts and date of payment.
- Sort these results in descending order by the payment amount.

4. Orders, Order Details, and Product Details (a Many-to-Many Join)
- Select all of the customer contacts (first and last names) along with the product names, quantities, and date ordered for each of the customers and each of their orders.
- Sort these in descending order by the order date.
- Note: This will require joining four tables.
