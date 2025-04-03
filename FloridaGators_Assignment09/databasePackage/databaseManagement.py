# dataManagement.py
# Madison Geier
# Cole Crooks
# geierml@mail.uc.edu
# crookscl@mail.uc.edu
# Assignment09
# 4/3/25
# IS4010 002
# Spring 2025
# Brief Description of the assignment:  developing a vs project to access sql serve databases and pull information

# Brief Description of what this module does. This module furthers our knowledge of python by providing the tools and education to link and extract inforomation from a sql server database to a python project.
# Citations: w3schools and OWASP Foundation

# Anything else that's relevant:

import pyodbc

# Function to establish a connection to the SQL Server database
def get_connection():
    conn_str = (
        'DRIVER={SQL Server};'
        'SERVER=lcb-sql.uccob.uc.edu\\nicholdw;'  # Your server address
        'DATABASE=GroceryStoreSimulator;'  # Your database name
        'UID=IS4010Login;'  # Your username
        'PWD=P@ssword2;'  # Your password
        'TrustServerCertificate=yes;'  # Trusting the server's certificate
    )
    return pyodbc.connect(conn_str)

# Function to execute a SQL query and return results
def execute_query(query, params=None):
    try:
        # Establish the connection to the database
        conn = get_connection()

        # Use 'with' statement to ensure the cursor is closed automatically after use
        with conn.cursor() as cursor:
            # Execute the SQL query with parameters
            cursor.execute(query, params or [])
            
            # Fetch all the results of the query
            results = cursor.fetchall()

        # Close the connection manually here if not using 'with' statement for connection
        conn.close()

        return results

    except pyodbc.Error as e:
        # Print or log the error details
        print(f"Error executing query: {e}")
        return []

# Function to get the manufacturer name based on ManufacturerID
def get_manufacturer_name(manufacturer_id):
    query = "SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?"
    result = execute_query(query, (manufacturer_id,))
    
    # Check if a result is returned and extract the manufacturer name
    if result:
        manufacturer_name = result[0][0]  # Get the first column (Manufacturer)
        return manufacturer_name
    else:
        return "Manufacturer not found."

# Function to get the brand name based on BrandID
def get_brand_name(brand_id):
    query = "SELECT BrandName FROM tBrand WHERE BrandID = ?"
    result = execute_query(query, (brand_id,))
    
    # Check if a result is returned and extract the brand name
    if result:
        brand_name = result[0][0]  # Get the first column (BrandName)
        return brand_name
    else:
        return "Brand not found."
