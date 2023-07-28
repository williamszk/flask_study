
# https://www.udemy.com/course/rest-api-flask-and-python


# resources:
# store, item, user

# create store
# create items within stores
# items have price and name
# read stores and items inside stores
# 
# set users and authentication

# Example of expected functionality for Create Store
# request:
# POST /store {"name": "Banana Land"}
# response:
# {"name": "Banana Land", "items": []} 

# Example of expected functionality for Create Item
# request:
# POST /store/Banana Land/item {"name": "Chair", "price": 198.98}
# response:
# {"name": "Chair", "price": 198.98} 

# Example of expected functionality for Read all stores and its items
# request:
# GET /store
# response:
# it sends a json with a list of all stores and its respective items
# {
#   "stores":[
#       {
#           "name": "Banana Land", 
#           "item":[
#               {
#                   "name": "Chair", 
#                   "price": 198.98
#               }
#           ]         
#       }
#   ]
# }

# Example of expected functionality for Read a particular store
# request:
# GET /store/Banana Store
# response:
# it sends the json of that particular store
# {
#     "name": "Banana Land", 
#     "item":[
#         {
#             "name": "Chair", 
#             "price": 198.98
#         }
#     ]         
# }

# How to get only the list of items inside a certain store
# request:
# GET /store/Banana Store/item
# response:
# 






