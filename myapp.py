import requests
import json

# def to_lowercase(data):
#     if isinstance(data, dict):
#         return {k: (v.lower() if k == 'name' and isinstance(v, str) else to_lowercase(v)) for k, v in data.items()}
#     elif isinstance(data, list):
#         return [to_lowercase(i) for i in data]
#     else:
#         return data

# URLs for the endpoints
URL_CREATE = "http://127.0.0.1:8000/drinkcreate/"
URL_ADD_QUANTITY = "http://127.0.0.1:8000/addquantity/"
URL_DRINK_API = "http://127.0.0.1:8000/drinkapi/"

# def create_or_update_drink():
#     # Get user input for the drink name
#     name = input("Enter the name of the drink: ")
#     name = name.lower()

#     # Check if the drink already exists by sending a GET request with a query parameter
#     response = requests.get(url=URL_CREATE, params={'name': name.lower()})
#     if response.status_code == 200:
#         drinks_data = response.json()
#         drinks_data = to_lowercase(drinks_data)
#         if drinks_data:
#             print("Drink already exists:")
#             update_choice = input("update the quantity? (yes/no): ")
#             if update_choice.lower() == 'yes':
#                 quantity_to_add = int(input("Enter the quantity to add: "))
#                 data_add_quantity = {
#                     'name': name,
#                     'quantity': quantity_to_add
#                 }
#                 json_data_add_quantity = json.dumps(data_add_quantity)
#                 update_response = requests.post(url=URL_ADD_QUANTITY, data=json_data_add_quantity, headers={'Content-Type': 'application/json'})
#                 if update_response.status_code == 200:
#                     print("Drink quantity updated successfully!")
#                 elif update_response.status_code == 404:
#                     print("Drink not found.")
#                 else:
#                     print("Failed to update drink quantity. Status code: ", update_response.status_code)
#             else:
#                 print("Drink creation aborted.")
#         else:
#             description = input("Enter the description of the drink: ")
#             price = float(input("Enter the price of the drink: "))
#             quantity = int(input("Enter the quantity of the drink: "))
#             # Data for creating a new drink (POST request)
#             data_create = {
#                 'name': name,
#                 'description': description,
#                 'price': price,
#                 'quantity': quantity
#             }
#             json_data_create = json.dumps(data_create)

#             # Send a POST request to create a new drink
#             response = requests.post(url=URL_CREATE, data=json_data_create, headers={'Content-Type': 'application/json'})
#             if response.status_code == 200:
#                 print("Drink created successfully!")
#             else:
#                 print("Failed to create drink. Status code:", response.status_code)
#     else:
#         print("Failed to check drink existence. Status code:", response.status_code)

# if __name__ == '__main__':
#     create_or_update_drink()


def post_data():
    data = {
        'name': 'Coffee',
        'description':'Hot',
        # 'price': 100,
        'quantity': 55
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL_DRINK_API,data = json_data)
    data = r.json()
    print(data)

    post_data()
