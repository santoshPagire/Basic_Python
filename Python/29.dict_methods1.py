# create a variable and assign it the following dictionary
# make the dictionary span multiple lines so that the line the dictionary starts on is not too
var = {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One",
      "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", 
      "Bob Dylan": "Like A Rolling Stone"}

# print the length of the dictionary.
print(len(var))
# use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.
for key in var.keys():
    print (key)
# print all of the values from the dictionary using the .values() method.
print(var.values())
# use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for item in var.items():
    print(item)
#    use the .get() method to check the dictionary for the key

 #       "Promise of the Real"

 # and create a message that will print if the key is not found in the dictionary.

if "Promise of the Real" in var:
    print (var("Promise of the real"))
else:
    print("key is not found in var")