# Import the pandas library for data manipulation and analysis
import pandas as pd  

# Import the NumPy library for mathematical operations and array handling
import numpy as np  

# Import the Matplotlib library for data visualization
import matplotlib.pyplot as plt  

# Import the Seaborn library for statistical data visualization
import seaborn as sns  

# Import the random module for generating random values
import random  

# Import datetime and timedelta classes for handling dates and time intervals
from datetime import datetime, timedelta  


class GenerateData:

    # Function to generate fictional sales data
    def generate_fake_data(num_records=600):
        """
        Generates a Pandas DataFrame containing fictional sales data.
        """

        # Display initial message indicating the number of records to be generated
        print(f"\nStarting the generation of {num_records} records...")

        # Dictionary containing products, their categories, and prices
        products = {
            'Gaming Laptop': {'category': 'Electronics', 'price': 7500.00},
            'Vertical Mouse': {'category': 'Accessories', 'price': 250.00},
            'Mechanical Keyboard': {'category': 'Accessories', 'price': 550.00},
            'Ultrawide Monitor': {'category': 'Electronics', 'price': 2800.00},
            'Gaming Chair': {'category': 'Furniture', 'price': 1200.00},
            'Headset 7.1': {'category': 'Accessories', 'price': 800.00},
            'Graphics Card': {'category': 'Hardware', 'price': 4500.00},
            'SSD 1TB': {'category': 'Hardware', 'price': 600.00}
        }

        # Create a list with only the product names
        product_list = list(products.keys())

        # Dictionary containing cities and their respective states
        cities_states = {
            'São Paulo': 'SP', 
            'Rio de Janeiro': 'RJ', 
            'Belo Horizonte': 'MG',
            'Porto Alegre': 'RS', 
            'Salvador': 'BA', 
            'Curitiba': 'PR', 
            'Fortaleza': 'CE'
        }

        # Create a list with only the city names
        city_list = list(cities_states.keys())

        # List to store all generated sales records
        sales_data = []

        # Define the initial date for sales orders
        start_date = datetime(2026, 1, 1)

        # Loop to generate each sales record
        for i in range(num_records):

            # Randomly select a product
            product_name = random.choice(product_list)

            # Randomly select a city
            city = random.choice(city_list)

            # Generate a random quantity sold between 1 and 7
            quantity = np.random.randint(1, 8)

            # Calculate the order date based on the initial date
            order_date = start_date + timedelta(days=int(i / 5), hours=random.randint(0, 23))

            # Apply a random discount if the product is a mouse or keyboard
            if product_name in ['Vertical Mouse', 'Mechanical Keyboard']:
                unit_price = products[product_name]['price'] * np.random.uniform(0.9, 1.0)
            else:
                unit_price = products[product_name]['price']

            # Append the generated record to the list
            sales_data.append({
                'Order_ID': 1000 + i,
                'Order_Date': order_date,
                'Product_Name': product_name,
                'Category': products[product_name]['category'],
                'Unit_Price': round(unit_price, 2),
                'Quantity': quantity,
                'Customer_ID': np.random.randint(100, 150),
                'City': city,
                'State': cities_states[city]
            })

        # Display final message indicating data generation completion
        print("Data generation completed successfully.\n")

        # Return the data as a Pandas DataFrame
        return pd.DataFrame(sales_data)
