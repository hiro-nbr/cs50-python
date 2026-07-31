name = input("whats your name:")

file = open("name.py",  "w")
file.write(name)
file.close()