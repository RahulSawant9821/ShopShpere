from faker import Faker
import datetime
import random
import csv

faker = Faker()

product_records = []

categories = [
    "Electronics",
    "Home",
    "Clothing",
    "Sports",
    "Beauty",
    "Books"
]

suppliers = [
    "TechSupply Ltd",
    "HomeGoods Ltd",
    "UK Wholesale",
    "Global Supplies"
]

product_types = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Headphones",
    "Monitor",
    "T-Shirt",
    "Coffee Mug",
    "Running Shoes",
    "Backpack",
    "Smartphone"
]

for index in range(500):
    product = {}
    product["product_id"] = f"P{index+1:06d}"
    product["product_name"] = random.choice(product_types)
    product["category"] = random.choice(categories)
    product["price"] = round(random.uniform(5,1000),2)
    product["supplier"] = random.choice(suppliers)
    product["created_at"] = datetime.datetime.now()

    product_records.append(product)



with open("../data/products.csv","w",newline="",encoding = "utf-8") as file:
    fieldnames = product_records[0].keys()

    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(product_records)