import json
import pickle

cars = (
    {"make":"Toyota","model":"Camry","year":2022,"type":"Sedan","price":25000},
    {"make":"Honda","model":"Civic","year":2022,"type":"Sedan","price":22000},
    {"make":"Ford","model":"F-150","year":2022,"type":"Truck","price":40000},
    {"make":"Chevrolet","model":"Malibu","year":2022,"type":"Sedan","price":24000},
    {"make":"Jeep","model":"Wrangler","year":2022,"type":"SUV","price":35000}
)

print(type(cars))

str_json = json.dumps(cars)
print(repr(str_json))

with open('test.json', 'w') as f:
    json.dump(cars, f)

with open('test.json', 'r') as f:
    new_cars = json.load(f)

print(repr(new_cars))

with open('test.pickle', 'wb') as f:
    pickle.dump(cars, f)

with open('test.pickle', 'rb') as f:
    new_cars = pickle.load(f)

print(repr(new_cars))

pickle_print = pickle.dumps(print)
print(pickle_print)

new_print = pickle.loads(pickle_print)
print(new_print)

print(id(print), id(new_print))

new_print("hello from the new print")