data_science_users = [15, 23, 43, 56]
machine_learning_users = [13, 23, 56, 42]

watched = data_science_users.copy()
watched.extend(machine_learning_users)  # to extend

watched = set(watched)  # conjunto
# conjunto = {1, 2, 3}

print(watched)

for user in set(watched):
    print(user)


data_science_users = set(data_science_users)
machine_learning_users = set(machine_learning_users)


# "|" means or
print(data_science_users | machine_learning_users)

# "&" means and
print(data_science_users & machine_learning_users)

# "-" means it's in data but not in machine
print(data_science_users - machine_learning_users)

# "^" means an 'or exclusive'
print(data_science_users ^ machine_learning_users)

did = data_science_users - machine_learning_users
print(15 in did)
print(23 in did)
