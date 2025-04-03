# Main.py
# Madison Geier
# geierml@mail.uc.edu
# Assignment09
# 4/3/25
# IS4010 002
# Spring 2025
# Brief Description of the assignment:  developing a vs project to access sql serve databases and pull information

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: w3schools and OWASP Foundation

# Anything else that's relevant:

import pyodbc
import databasePackage.databaseManagement

from databasePackage.databaseManagement import *


if __name__ == "__main__":



 def get_connection():
    
    conn_str = (
        'DRIVER={SQL Server};'
        'SERVER=lcb-sql.uccob.uc.edu\\nicholdw;'
        'DATABASE=GroceryStoreSimulator;'
        'UID=IS4010Login;'
        'PWD=P@ssword2;'
        'TrustServerCertificate=yes;'
    )
    return pyodbc.connect(conn_str)


from databasePackage.databaseManagement import execute_query

def main():
    # Define the query to execute
    query = """
    SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID
    FROM tProduct
    """
    
 
    data = execute_query(query)
    
  
    for row in data:
        print(row)

if __name__ == '__main__':
    main()

# Step 2 in Assignment
print("-----------------------------------------------------------------")

import random

# Sample data structure (list of dictionaries)
data = [
    {"ProductID": 101, "Description": "Product 1", "ManufacturerID": 10, "BrandID": 5},
    {"ProductID": 102, "Description": "Product 2", "ManufacturerID": 12, "BrandID": 8},
    {"ProductID": 103, "Description": "Product 3", "ManufacturerID": 15, "BrandID": 2},
    # Add more rows as needed...
]

# Step 1: Randomly select one row from the data structure
random_row = random.choice(data)

# Step 2: Store the required values in variables
description = random_row["Description"]
product_id = random_row["ProductID"]
manufacturer_id = random_row["ManufacturerID"]
brand_id = random_row["BrandID"]

# Step 3: Print or use the variables as needed
print("Description:", description)
print("ProductID:", product_id)
print("ManufacturerID:", manufacturer_id)
print("BrandID:", brand_id)

# Step 3 in Assignment
print("-----------------------------------------------------------------")

manufacturer_name = get_manufacturer_name(manufacturer_id)
    
    # Print the manufacturer name
print(f"Manufacturer Name: {manufacturer_name}")
manufacturer_name = get_manufacturer_name(manufacturer_id)
if __name__ == "__main__":
    main()

# Step 4 in Assignment
print("-----------------------------------------------------------------")



print(f"Manufacturer Name: {manufacturer_name}")

    # Step 5
print("-----------------------------------------------------------------")

def get_brand_name(brand_id):
        query = f"SELECT BrandName FROM tBrand WHERE BrandID = {brand_id}"
        result = execute_query(query)
        
        # Check if a result is returned and extract the brand name
        if result:
            brand_name = result[0][0]  # Get the first column (BrandName)
            return brand_name
        else:
            return "Brand not found."

    # Call the function to get the brand name
brand_name = get_brand_name(brand_id)

    # Step 5: Print the brand name
print(f"Brand Name: {brand_name}")

    # Step 6
print("-----------------------------------------------------------------")

 # Step 6: Query for Number of Items Sold using ProductID
def get_number_of_items_sold(product_id):
        query = """
        SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
        FROM dbo.tTransactionDetail
        INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
        WHERE dbo.tTransaction.TransactionTypeID = 1 AND dbo.tTransactionDetail.ProductID = ?
        """
        result = execute_query(query, (product_id,))
        
        # If result is returned, return the number of items sold
        if result:
            return result[0][0]  # The first column should be the number of items sold
        else:
            return 0  # If no result is found, return 0

    # Get the number of items sold for the selected product
number_of_items_sold = get_number_of_items_sold(product_id)

print("-----------------------------------------------------------------")
    # Step 7: Construct the sentence
sentence = f"The product '{description}' from '{brand_name}' by '{manufacturer_name}' has sold {number_of_items_sold} units."

    # Print the sentence
print(sentence)

    # End 
print("-----------------------------------------------------------------")


