# For this programming challenge, write a function in a .py file which takes 1 string as an argument, finds out the number of words in that string, then returns that number. 

# For example, if the program was used on the string "This is a string.", then the function would return 4. 

# Assumptions:

#     Assume that the string will be assigned to a variable and that it will contain at least 1 word.

#     Assume that there will never be 2 or more consecutive spaces in a row within the string.

#     Contractions and possessive words with an apostrophe like "it's" or "Brian's" count as 1 word.

#     Hyphenated words like "ice-cream" count as 1 word.

#     Numbers in the string such as the "007" in "James Bond is 007." count as words

#     There will be no double quotes "" within in the string.


str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
    saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
    shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
    shrimp burger, shrimp sandwich. That- that's about it."
     

def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
            if i.isalnum() or i.isspace() or i == "-" or i == "'":
                spaces_and_letters += i
    for j in spaces_and_letters:
            if j == " ":
                word_count += 1
    return word_count

# def word_counter(words):
#     word_count = 1     
#     for j in words:
#             if j == " ":
#                 word_count += 1
#     return word_count
     




print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))