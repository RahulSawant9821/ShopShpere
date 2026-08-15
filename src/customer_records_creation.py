from faker import Faker
import datetime
import csv

faker = Faker()

customer_records = []

for index in range(10000):
    customer = {}
    customer["customer_id"] = f"C{index+1:06d}"
    customer["first_name"] = faker.first_name()
    customer["last_name"] = faker.last_name()
    customer["email"] = faker.email()
    customer["country"] = faker.country()
    customer["phone"] = faker.phone_number()    
    customer["created_at"] = datetime.datetime.now()

    customer_records.append(customer)



with open("./data/customers.csv","w",newline="",encoding = "utf-8") as file:
    fieldnames = customer_records[0].keys()

    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(customer_records)