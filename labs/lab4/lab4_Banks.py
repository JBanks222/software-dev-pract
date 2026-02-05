"""
Jalen Banks
Feb 10, 2026
Lab 4: Dictionarys in Python
"""
print("\n--- Example 1: Dictionaries in Python ---\n")
# this is how you declare and inialize a dictionary in Python
contacts = {
    "Alice": "718-111-2222",
    "Bob": "718-333-4444",
    "Charlie": "718-555-6666"
}
print(f"original dictionary: {contacts}\n")
#update an entry in the dictionary


contacts["Alice"] = "718-999-8888"

print(f"updated dictionary: {contacts}\n")

# add a new key value pair to the dictionary
contacts["David"] = "718-777-6666"

print(f"dictionary after adding a new entry: {contacts}\n")

print("--- Example 2: Loop through a dictionary ---\n")
# for loop to print each key in dictionary
for v in contacts:
    print(v)
# for loop to print each value in dictionary
for v in contacts:
    print(contacts[v])
# for loop to print each key value pair in dictionary
for v in contacts:
    print(f"{v}: Phone number is {contacts[v]}")

print("--- Example 3: items(), keys(),values() methods in the dictionary ---\n")
# the items method returns all the key value pairs in the dictionary
print(F"items in tehe dictionary: {contacts.items()}\n")
# keys method returns all the keys in the dictionary
print(f"all keys in the dictionary: {contacts.keys()}\n")
# values method returns all the values in the dictionary
print(f"all values in the dictionary: {contacts.values()}\n")

print("--- Example 4: check if a key is 'in' or 'not in' the dictionary ---\n")
# check if a key is in the dictionary

check_name = "Alice"
check = check_name in contacts
print(f"is {check_name} in the dictionary? {check}\n")

print("--- Example 5: Length of a dictionary ---\n")
print(f"contacts has {len(contacts)} key-value pairs\n")

print("--- Example 6: Remove a pair ---\n")
print(f"dictionary before removing an entry: {contacts}\n")
# remove a key value pair from the dictionary
contacts.pop("Bob")
print(f"dictionary after removing an entry: {contacts}\n")

print("\n--- Example 7: Get method ---\n")

# get method returns the key-value pair of a key
print(f"key-value pair: {contacts.get('Alice')}\n")

print("\n--- Example 8: Update method---\n")
# can be used to update or add key-value pairs
contacts.update({"Eve": "718-222-3333"})
print(f"dictionary after using update method to add a new entry: {contacts}\n")

print("\n--- EXCERCISE---\n")