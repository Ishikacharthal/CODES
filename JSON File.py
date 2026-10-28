import json

with open("data.json", "r") as file:
    data = json.load(file)

new_record = {
    "id": 3,
    "name": "Ishika",
    "age": 19
}

data.append(new_record)

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("New record added successfully!")
print(data)