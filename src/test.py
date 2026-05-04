with open ("faah.txt", "w") as file:
    file.write("Hello World")
with open ("faah.txt", "r") as file:
    
    red = file.read()
    print(red)