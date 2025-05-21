import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# Step 1
q = """
SELECT firstName, lastName, city, state
FROM employees
JOIN offices
    USING(officeCode)
ORDER BY firstName, lastName
;
"""
df = pd.read_sql(q, conn)
# print('Total number of results:', len(df))
# print('First 5 results:', df.head())

# Step 2
q = """
SELECT
    contactFirstName,
    contactLastName,
    orderNumber,
    orderDate,
    status
FROM customers
JOIN orders
    USING(customerNumber)
;
"""
df = pd.read_sql(q, conn)
# print('Total number of results:', len(df))
# print('First 5 results:', df.head())

# Step 3
q = """
SELECT
    contactFirstName,
    contactLastName,
    amount,
    paymentDate
FROM customers
JOIN payments
    USING(customerNumber)
ORDER BY amount DESC
;
"""
df = pd.read_sql(q, conn)
# print('Total number of results:', len(df))
# print('First 5 results:', df.head())

# Step 4
q = """
SELECT
    contactFirstName,
    contactLastName,
    productName,
    quantityOrdered,
    orderDate
FROM customers
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
JOIN products
    USING (productCode)
ORDER BY orderDate DESC
;"""
df = pd.read_sql(q, conn)
print('Total number of results:', len(df))
print('First 5 results:', df.head())

conn.close()