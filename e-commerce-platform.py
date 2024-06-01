import pandas as pd
import json
from sqlalchemy import create_engine

# importing json data 
json_data = '''
[
    {
        "order_id": 1001,
        "order_date": "2024-05-01",
        "customer": {
            "customer_id": 501,
            "name": "John Doe",
            "email": "johndoe@example.com",
            "address": {
                "street": "123 Elm St",
                "city": "Springfield",
                "state": "IL",
                "zip": "62701"
            }
        },
        "items": [
            {
                "item_id": 2001,
                "product_name": "Laptop",
                "quantity": 1,
                "price": 999.99,
                "product_details": {
                    "category": "Electronics",
                    "brand": "Brand A",
                    "reviews": [
                        {"review_id": 3001, "rating": 5, "comment": "Excellent product!"}
                    ]
                }
            },
            {
                "item_id": 2002,
                "product_name": "Mouse",
                "quantity": 2,
                "price": 25.50,
                "product_details": {
                    "category": "Electronics",
                    "brand": "Brand B",
                    "reviews": [
                        {"review_id": 3002, "rating": 4, "comment": "Good value for money."}
                    ]
                }
            }
        ],
        "shipping": {
            "method": "FedEx",
            "cost": 15.00,
            "address": {
                "street": "123 Elm St",
                "city": "Springfield",
                "state": "IL",
                "zip": "62701"
            }
        },
        "payment": {
            "method": "Credit Card",
            "transaction_id": "TXN123456",
            "amount": 1066.99
        }
    },
    {
        "order_id": 1002,
        "order_date": "2024-05-02",
        "customer": {
            "customer_id": 502,
            "name": "Jane Smith",
            "email": "janesmith@example.com",
            "address": {
                "street": "456 Oak St",
                "city": "Lincoln",
                "state": "NE",
                "zip": "68508"
            }
        },
        "items": [
            {
                "item_id": 2003,
                "product_name": "Desk Chair",
                "quantity": 1,
                "price": 149.99,
                "product_details": {
                    "category": "Furniture",
                    "brand": "Brand C",
                    "reviews": [
                        {"review_id": 3003, "rating": 4, "comment": "Comfortable chair."}
                    ]
                }
            }
        ],
        "shipping": {
            "method": "UPS",
            "cost": 20.00,
            "address": {
                "street": "456 Oak St",
                "city": "Lincoln",
                "state": "NE",
                "zip": "68508"
            }
        },
        "payment": {
            "method": "PayPal",
            "transaction_id": "TXN789012",
            "amount": 169.99
        }
    }
]
'''

# converting to json file 

data = json.loads(json_data)

# DataFrame

orders = []
customers = []
items = []
shippings = []
payments = []
reviews = []

for order in data:
    order_info = {
        "order_id": order["order_id"],
        "order_date": order["order_date"],
        "customer_id": order["customer"]["customer_id"],
        "shipping_method": order["shipping"]["method"],
        "shipping_cost": order["shipping"]["cost"],
        "payment_method": order["payment"]["method"],
        "payment_transaction_id": order["payment"]["transaction_id"],
        "payment_amount": order["payment"]["amount"]
    }
    orders.append(order_info)
    
    customer_info = {
        "customer_id": order["customer"]["customer_id"],
        "name": order["customer"]["name"],
        "email": order["customer"]["email"],
        "street": order["customer"]["address"]["street"],
        "city": order["customer"]["address"]["city"],
        "state": order["customer"]["address"]["state"],
        "zip": order["customer"]["address"]["zip"]
    }
    customers.append(customer_info)
    
    for item in order["items"]:
        item_info = {
            "order_id": order["order_id"],
            "item_id": item["item_id"],
            "product_name": item["product_name"],
            "quantity": item["quantity"],
            "price": item["price"],
            "category": item["product_details"]["category"],
            "brand": item["product_details"]["brand"]
        }
        items.append(item_info)
        
        for review in item["product_details"]["reviews"]:
            review_info = {
                "item_id": item["item_id"],
                "review_id": review["review_id"],
                "rating": review["rating"],
                "comment": review["comment"]
            }
            reviews.append(review_info)
    
    shipping_info = {
        "order_id": order["order_id"],
        "method": order["shipping"]["method"],
        "cost": order["shipping"]["cost"],
        "street": order["shipping"]["address"]["street"],
        "city": order["shipping"]["address"]["city"],
        "state": order["shipping"]["address"]["state"],
        "zip": order["shipping"]["address"]["zip"]
    }
    shippings.append(shipping_info)

    payment_info = {
        "order_id": order["order_id"],
        "method": order["payment"]["method"],
        "transaction_id": order["payment"]["transaction_id"],
        "amount": order["payment"]["amount"]
    }
    payments.append(payment_info)

orders_df = pd.DataFrame(orders)
customers_df = pd.DataFrame(customers)
items_df = pd.DataFrame(items)
shippings_df = pd.DataFrame(shippings)
payments_df = pd.DataFrame(payments)
reviews_df = pd.DataFrame(reviews)

# Display the DataFrames
print("Orders DataFrame:")
print(orders_df)
print("\nCustomers DataFrame:")
print(customers_df)
print("\nItems DataFrame:")
print(items_df)
print("\nShippings DataFrame:")
print(shippings_df)
print("\nPayments DataFrame:")
print(payments_df)
print("\nReviews DataFrame:")
print(reviews_df)

# Write DataFrames to SQL
# Create an SQLite engine 
engine = create_engine('C:/Users/USER/Downloads/Chinook_Sqlite.sqlite.db')

# Write DataFrames to SQL tables
orders_df.to_sql('orders', con=engine, index=False, if_exists='replace')
customers_df.to_sql('customers', con=engine, index=False, if_exists='replace')
items_df.to_sql('items', con=engine, index=False, if_exists='replace')
shippings_df.to_sql('shippings', con=engine, index=False, if_exists='replace')
payments_df.to_sql('payments', con=engine, index=False, if_exists='replace')
reviews_df.to_sql('reviews', con=engine, index=False, if_exists='replace')

# Verify the tables
orders_result = engine.execute("SELECT * FROM orders").fetchall()
customers_result = engine.execute("SELECT * FROM customers").fetchall()
items_result = engine.execute("SELECT * FROM items").fetchall()
shippings_result = engine.execute("SELECT * FROM shippings").fetchall()
payments_result = engine.execute("SELECT * FROM payments").fetchall()
reviews_result = engine.execute("SELECT * FROM reviews").fetchall()

print("\nOrders SQL Table:")
print(orders_result)
print("\nCustomers SQL Table:")
print(customers_result)
print("\nItems SQL Table:")
print(items_result)
print("\nShippings SQL Table:")
print(shippings_result)
print("\nPayments SQL Table:")
print(payments_result)
print("\nReviews SQL Table:")
print(reviews_result)
