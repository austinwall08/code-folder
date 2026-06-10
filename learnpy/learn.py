# type casting review 

    # name = " "
#     age = 21
#     gpa = 4.0
#     student = True

#    check type
#     print(type(name))
#     print(type(age))
#     print(type(gpa))
#     print(type(student))

    # name = bool(name)
    # print(name)

#     print()

#     x = 2
#     y = 2.0

#     x = x/y

#     print(x)

# end

# input review
#     name = input("Enter ur name: ")
#     age = int(input("enter your age: ")) + 1

#     print(f"hello {name}")
#     print(f"you are {age} years old")


#     excercises

#         adjective1 = input("Enter an Adjective: ")
#         adjective2 = input("Enter an Adjective: ")
#         adjective3 = input("Enter an Adjective: ")
#         noun = input("enter a noun: ")
#         verb = input("enter a verb: ")


#         madlibs

#         print(f"Today I went to a {adjective1} zoo ")
#         print(f"In an exhibit, I saw {noun}")
#         print(f"{noun} was {adjective2} and {verb}ing")
#         print(f"I was {adjective3}")

#         length = int(input("Enter Length of Rectangle: "))
#         width = int(input("What is width: "))

#         area = length*width

#         print(f"The area is {area} cm^2")

#         cost calc

#         item = input("What Item r u buying: ")
#         price = float(input("what is the price: "))
#         quantity = float(input("how much r u buying of the item: "))

#         total = price*quantity
#         print(f"you have bought {quantity} x {item}/s")
#         print(f"your total is ${round(total, 2)}")
# end


# Math



#     friends = 4

#     friends = friends + 1
#     friends += 1 #same as line 76
#     friends = friends - 1
#     friends -= 1
#     # etc
#     remainder = friends % 3

#     friends **= 2

#     print(remainder)
#     print (friends)

#     x = 3.14
#     y = -4
#     z = 5

#     result = round(x, 1)
#     print(result)
#     result_y = pow(y, 3)
#     print(result_y)

#     max_result = max(x, y, z)
#     min_result = min (x, y, z)

#     print(max_result, min_result)

#     import math

#     print(math.pi)

#     root = math.sqrt(x)
#     print(root)
#     cel = math.ceil(x)
#     print(cel)
#     floor = math.floor(x)
#     print(x)

#     excersises 
#         import math

#         pi = math.pi
#         radius = float(input("enter radius of circle: "))
#         circum = 2*pi*radius

#         print(f"The circumference is {round(circum, 2)} units")   


#         import math

#         radius = float(input("Enter the radius: "))

#         area = math.pi * pow(radius, 2)

#         print(f"the area is {round(area, 2)}")

#         a = float(input("What is the length of the [a] leg"))
#         b = float(input("What is the length of the [b] leg"))

#         hypo = math.sqrt(pow(a, 2) + pow(b, 2))

#         print(f"the hypo is {round(hypo, 2)}")

# end


# if statements

#     age = int(input("Enter your age: "))


#     if age >= 100:
#         print("get out of here unc")
#     elif age >= 18:
#         print("Youre now signed up!")
#     elif age <= 0:
#         print("lier!")
#     else:
#         print("you must be 18+ to sign up")
   


#     excercises
    
#         response = input("would u like food? [Y/N]")

#         if response == "Y":
#             print("have some food")
#         else:
#             print("f off")

#         name = input("Enter your name: ")

#         if name == "":
#             print("type in ur name slut")
#         else:
#             print(f"Hello {name}")    


#         online = False

#         if online:
#             print("online bro")
#         else:
#             print("get on man")

# exit



# projects

#  (simple calculator)

#     operator =  input("enter an operator (+, -, *, /): ")
#     num1 = float(input("Enter the first number :"))
#     num2 = float(input("Enter the second number :"))

#     if operator == "+":
#        result = num1 + num2
#     elif operator  == "-":
#         result = num1 - num2
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "/":
#         result = num1 / num2
#     else:
#         result = 0
#         print(f"{operator} is not a valid operation for this calc")

#     print(round(result, 2))
#     exit

# weight conversion 
#     weight = float(input("enter weight: "))
#     unit = input("KG or LBS?: [K/L]")

#     if unit == "K":
#         weight *= 2.205
#         unit = "Lbs"
#         print(f"your weight is {round(weight, 1)} {unit}")
#     elif unit == "L":
#         weight /= 2.205
#         unit = "Kgs"
#         print(f"your weight is {round(weight, 1)} {unit}")
#     else:
#         print("wrong input for unit")

# temp conversion
#         unit = input("Is this temp in celsius or fahrenheit?: [C/F]")
#         temp = float(input("enter the temp: "))

#         if unit == "C":
#             temp = round((9*temp) / 5 + 32, 1)
#             print(f"It is {temp} degrees F")
#         elif unit =="F":
#             temp = round((temp - 32) *5/9, 1)
#             print(f"the temp in C is {temp} degrees")
#         else:
#             print(f"{unit} is not valid unit")
# exit

# end of projects



# logical operators

#     temp = 40

#     if temp > 0 and temp < 30:
#         print("weather is good")
#     else: 
#         print("temp is bad")


#     temp = 40

#     if temp <= 0 or temp >= 30:
#         print("weather is bad")
#     else: 
#         print("temp is good")


#     sunny = True

#     if not sunny:
#         print("its sunny outside")
#     else: 
#         print("it is cloudy outside")

# exit


# conditional expressions

    # num = 5
    # print("pos" if num>0 else "Negative")
    # result = "Even" if num % 2 == 0 else "ODD"
    # print(result)

    # a = 6
    # b = 7
    # max_num = a if a>b else b
    # min_num = a if a<b else b
    # print(min_num)
    # print(max_num)

    # age = 25
    # status = "Adult" if age >= 18 else "Child"
    # print(status)

    # temp = 20
    # weather = "hot" if temp > 20 else "cold"
    # print(weather)

    # user_role = "guest"
    # access_level = "Full access granted" if user_role == "admin" else "limited access"
    # print(access_level)

# exit

# string Methods

    # name = input("Enter your full name: ")

    # phone_number = input("Enter your phone number [xxx-xxx-xxxx] ")

    # result = len(name)
    # print(result)

    # result = name.find(" ")
    # print(result)

    # result = name.rfind("a")
    # print(result)

    # name = name.capitalize()
    # print(name)

    # name = name.upper()
    # print(name)

    # name = name.lower()
    # print(name)

    # result = name.isdigit()
    # print(result)

    # result = name.isalpha()
    # print(result)

    # result = phone_number.count("-")
    # print(result)

    # result = phone_number.replace("-", "")
    # print(result)

    # print(help(str))

    # exercise 

        # username = input("Enter a Username: ")

        # charater_count = len(username)
        # space_check = username.find(" ")
        # digit_check = username.isdigit()

        # if charater_count > 12:
        #     print("username cannot exceed 12 characters")
        # elif space_check != -1:
        #     print("username cannot contain spaces")
        # elif digit_check is True:
        #     print("username cannot contain numbers")
        # else:
        #     print(f"welcome {username}")

# exit

# string index

    # credit_card = "1234-5678-9012-3456"

# first charcter, start to 4th character, 5th to 9th character, 5th to end, 2nd to last character, every other character
    # print(credit_card[0])
    # print(credit_card[0:4])
    # print(credit_card[5:9])
    # print(credit_card[5:])
    # print(credit_card[-2])
    # print(credit_card[::2])

    # # exercises

    # credit_num = input("Enter credit card number: [xxxx-xxxx-xxxx-xxxx] ")
    # print(f"Card Accepted (**** - **** - **** - {credit_num[15:]})")

    # credit_num = credit_num[::-1]
    # print(credit_num)
# exit

# email slicer project

    # email = input("Enter your email: ")

    # username = email[:email.index("@")]
    # domain = email[email.index("@")+ 1:]

    # print(f" Username: {username} and domain is {domain}")

# exit

# format specifiers

    # price1 = 3.14159
    # price2 = -1987.65
    # price3 = 12.34

    # # decimal places
    # print(f"price1 is {price1:.1f}")
    # print(f"price2 is {price2:.1}")
    # print(f"price3 is {price3:.3}")

    # # spaces of input
    # print(f"price1 is {price1:10}")
    # print(f"price2 is {price2:10}")
    # print(f"price3 is {price3:10}")

    # # zero padding
    # print(f"price1 is {price1:010}")
    # print(f"price2 is {price2:010}")
    # print(f"price3 is {price3:010}")

    # # left alignment
    # print(f"price1 is {price1:<10}")
    # print(f"price2 is {price2:<10}")
    # print(f"price3 is {price3:<10}")

    # # right alignment
    # print(f"price1 is {price1:>10}")
    # print(f"price2 is {price2:>10}")
    # print(f"price3 is {price3:>10}")

    # # center alignment
    # print(f"price1 is {price1:^10}")
    # print(f"price2 is {price2:^10}")
    # print(f"price3 is {price3:^10}")

    # # sign display
    # print(f"price1 is {price1:+}")
    # print(f"price2 is {price2:+}")
    # print(f"price3 is {price3:+}")

    # # align numbers to eachother 
    # print(f"price1 is {price1: }")
    # print(f"price2 is {price2: }")
    # print(f"price3 is {price3: }")

    # # comma as thousand separator
    # print(f"price1 is {price1:,}")
    # print(f"price2 is {price2:,}")
    # print(f"price3 is {price3:,}")

    # # positive sign, comma, and 2 decimal places
    # print(f"price1 is {price1:+,.2f}")
    # print(f"price2 is {price2:+,.2f}")
    # print(f"price3 is {price3:+,.2f}")

# exit

# while loops

    # name = input("enter name: ") 

    # while name == "":
    #     print("you need to enter a name")
    #     name = input("enter name: ")

    # print(f"hello {name}")

    # age = int(input("enter age: "))

    # while age < 0:
    #     print("lier")
    #     age = int(input("enter age: "))

    # print(f"you are {age} years old")

    # food = input("enter a food you like (q to quit): ")

    # while food != "q":
    #     print(f"you like {food}")
    #     food = input("enter another food you like (q to quit): ")
    # print("bye")

    # num = int(input("enter a number [1-10]: "))

    # while num < 1 or num > 10:
    #     print(f"{num} is not between 1 and 10")
    #     num = int(input("enter a number [1-10]: "))

    # print(f"{num} is between 1 and 10")
# exit


# project interest calculator

    # prin = float(input("Enter the principal amount: "))
    # rate = float(input("Enter the rate of interest: "))
    # term = int(input("Enter the term in years: "))

    # while prin <= 0:
    #     print("Principal must be greater than 0")
    #     prin = float(input("Enter the principal amount: "))

    # while rate <= 0:
    #     print("Rate must be greater than 0")
    #     rate = float(input("Enter the rate of interest: "))

    # while term <= 0:
    #     print("Term must be greater than 0")
    #     term = int(input("Enter the term in years: "))  

    # print(prin)
    # print(rate)
    # print(term)

    # total = prin * pow((1 + rate/100), term)
    # print(f"Total amount after {term} year/s is ${total:.2f}")
# exit

# for loops - execute code for fixed number of times

    # counter
    # for x in range(1, 11,):
    #     print(x)

    # step (by twos)
    # for x in range(1, 11, 2):
    #     print(x)

    # (reverse count)
    # for x in reversed(range(1, 11)):
    #     print(x)

    # credit_card = "1234-5678-9012-3456"

    # for x in credit_card:
    #     print(x)

    # skip an iteration 
    # for x in range(1, 21):
    #     if x == 13:
    #         continue
    #     else:
    #         print(x)

    # # break out of loop
    # for x in range(1, 21):
    #     if x == 13:
    #         break
    #     else:
    #         print(x)

# exit

# nested loops

    # rows = int(input("Enter number of rows: "))
    # col = int(input("Enter number of columns: "))
    # symbol = input("Enter a symbol to use: ")

    # for x in range(rows):
    #      for y in range(col):
    #         print(symbol, end = "")
    #      print()
# exit

# countdown timer project

    # import time

    # my_time = int(input("Enter time in seconds: ")) 

    # for x in range(my_time, 0, -1):
    #         seconds = x % 60
    #         mins = int(x / 60) % 60
    #         hours = int(x / 3600)
    #         print(f"{hours:02}:{mins:02}:{seconds:02}")
    #         time.sleep(1)

    # print("dick balls")
    # # exit

    # lists, sets and tuples

    # lists

    # fruits = ["apple", "orange", "banana", "coconut",]

    # # accesing elements in list
    # print(fruits)
    # print(fruits[0])
    # print(fruits[1])
    # print(fruits[:3])

    # # looping through list
    # for fruit in fruits:
    #     print(fruit)

    # # list of methods
    # print(dir(fruits))

    # # length of list
    # print(len(fruits))

    # # check if value in list (bool)
    # print("apple" in fruits)

    # # replace value in list
    # fruits[0] = "pineapple"
    # for fruit in fruits:
    #     print(fruit)

    # # # add to end of list
    # fruits.append("pineapple")
    # print(fruits)

    # # remove from list
    # fruits.remove("coconut")
    # print(fruits)

    # # insert into list at index
    # fruits.insert(0, "pineapple")
    # print(fruits)

    # # sorting lsit (alphabetically)
    # fruits.sort()
    # print(fruits)   

    # # reverse list (order placed)
    # fruits.reverse()    
    # print(fruits)

    # # clear list
    # fruits.clear()    
    # print(fruits)

    # # print num of index
    # print(fruits.index("apple"))

    # # counting num of occurences
    # print(fruits.count("apple"))

    # sets
    # NO DUPLICATES
    # fruits = {"apple", "orange", "banana", "coconut",}

    # # unordered
    # print(fruits)

    # # add element
    # fruits.add("pineapple")
    # print(fruits)   

    # # remove element
    # fruits.remove("coconut")
    # print(fruits)

    # # removes random element
    # fruits.pop()
    # print(fruits)

    # # clear set
    # fruits.clear()
    # print(fruits)

    # Tuples
    # ordered, unchangeable

    # fruits = ("apple", "orange", "banana", "coconut")

    # # find index of value in tuple    
    # print(fruits.index("apple"))

    # # how many occurences
    # print(fruits.count("apple"))

# exercise (shopping cart)

    # foods = []
    # prices = []
    # total = 0

    # while True:
    #     food = input("Enter a food to buy (q to quit): ")
    #     if food.lower() == "q":
    #         break
    #     else:
    #         foods.append(food)
    #         price = float(input(f"Enter the price of {food}: "))
    #         prices.append(price)

    # print("----- YOUR CART -----")
    # for food in foods:
    #     print(food)

    # for price in prices:
    #     total += price

    # print()
    # print(f"Total: ${total:.2f}")

# exit

# 2d collections

    # fruit =   ["apple", "orange", "banana", "coconut"]
    # veggies = ["carrot", "broccoli", "spinach"]
    # meats =   ["chicken", "beef", "pork"]

    # grocery_list = [fruit, veggies, meats]

    # # # print all lists
    # # print(grocery_list)

    # # # print specific list (index)
    # # print(grocery_list[1])

    # # # print specific item in list (index of list, index of item) (Row, Column)
    # # print(grocery_list[1][0])

    # for collection in grocery_list:
    #     for item in collection:
    #         print(item, end = " ")
    #     print()

    # # excercise (keypad)

    # num_pad = [[1, 2, 3],
    #            [4, 5, 6],
    #            [7, 8, 9],
    #            ["*", 0, "#"]]

    # for line in num_pad:
    #     for num in line:
    #         print(num, end = " ")
    #     print()

# exit

# project (quiz game)

    # questions = ("What is my (Austin) middle name?",
    #              "What is my favorite NFL team?", 
    #              "Where do I work?", 
    #              "Which one is NOT a college I was considering?",
    #              "What is my favorite food?")

    # options = (("A. Joseph ", "B. Michael ", "C. James ", "D. Robert "),
    #             ("A. Cowboys ", "B. Panthers ", "C. Giants ", "D. Patriots "),
    #             ("A. Google ", "B. Danikans ", "C. Kahunas ", "D. Facebook "),
    #             ("A. NIU ", "B. Bradley ", "C. EIU ", "D. UIUC "),
    #             ("A. Pizza ", "B. burgers ", "C. pasta ", "D. Wings "))

    # answers = ("D", "B", "C", "C", "D")
    # guesses = []
    # score = 0
    # question_num = 0

    # for question in questions:
    #     print("------------------------")
    #     print(question)
    #     for option in options[question_num]:
    #         print(option)
        
    #     guess = input("Enter (A, B, C, or D): ").upper()
    #     guesses.append(guess)
        
    #     if guess == answers[question_num]:
    #         score += 1
    #         print("Correct!")
    #     else:
    #         print("Wrong!")
    #         print(f"{answers[question_num]} is the correct answer")
    #     question_num += 1

    # print("------------------------")
    # print("         RESULTS         ")
    # print("------------------------")

    # print("answers: ", end = "")
    # for answer in answers:
    #     print(answer, end = " ")
    # print()

    # print("guesses: ", end = "")
    # for guess in guesses:
    #     print(guess, end = " ")
    # print()

    # score = int(score/len(questions) *100)

    # print(f"Your score is {score}%")

# exit

# dictionary (key:Value)

    # capitals = {"USA" : "Washington DC", 
    #             "India" : "New Dehli", 
    #             "China" : "Beijing", 
    #             "Russia" : "Moscow",}

    # # all atributes 
    # # print(dir(capitals))
    # # print(help(capitals))

    # # accessing values by key
    # print(capitals.get("USA"))
    # print(capitals.get("India"))
    # print(capitals.get("Japan"))

    # # if statement to check if key exists in dictionary
    # if capitals.get("Japan") == None:
    #     print("No capital found for that country")
    # else:
    #     print("Capital found")

    # # update dictionary
    # capitals.update({"Germany": "Berlin"})
    # capitals.update({"USA": "Detriot"}) # updates value for USA key

    # # removes key and value pair
    # capitals.pop("China")

    # # removes latest key and value pair
    # capitals.popitem()

    # # clear dictionary
    # capitals.clear() 

    # # returns list of keys in dictionary
    # keys = capitals.keys()
    # print(keys)

    # # looping through keys
    # for key in capitals.keys():
    #     print(key)

    # # looping through values
    # values = capitals.values()
    # for value in values:
    #     print(value)

    # # returns 2d list of tuples
    # items = capitals.items()
    # print(items)

    # # iterating through keys and values at the same time
    # for key, value in capitals.items():
    #         print(f"the capital of {key} is {value}")

# exit

# project (concess stand)

    # menu = {"hot dog": 3.50,
    #         "hamburger": 4.00,
    #         "fries": 2.50,
    #         "soda": 1.75,
    #         "candy": 1.25,
    #         "water": 1.00}

    # cart = []
    # total = 0

    # print("----- MENU -----")
    # for key, value in menu.items():
    #     print(f"{key:10}: ${value:.2f}")
    # print("----------------")

    # while True:
    #     food = input("select an item (q to quit): ").lower()
    #     if food == "q":
    #         break
    #     elif menu.get(food) is not None:
    #         cart.append(food)

    # print("------- YOUR FOOD IN CART -------")
    # for food in cart:
    #     total += menu.get(food)
    #     print(food, end=" ")

    # print()
    # print(f"total is ${total:.2f}")
    
# generate random numbers

# from math import pi
# import random

# # get all methods and attributes of random module
# # help(random)

# # generates random int between 1 and 6 (inclusive)
# num = random.randint(1,6) 

# print(num)

# # random in range of varibales
# low = 1
# high = 100
# num = random.randint(low, high)
# print(num)

# # generates random float between 0 and 1
# num = random.random() 
# print(num)

# # random element of a list etc
# options = ("rock", "paper", "scissors")
# option = random.choice(options)
# print(option)

# cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

# shuffle = random.shuffle(cards)
# print(cards)

# exercise guessing game
    # low = 1
    # high = 100
    # guesses = 0

    # num = random.randint(low, high)

    # while True:
    #     guess = int(input(f"enter number between {low} and {high}: "))
    #     guesses += 1

    #     if guess < num:
    #         print("too low")
    #     elif guess > num:
    #         print("too high")
    #     else:
    #         print(f"you got it! the number was {num}")
    #         print(f"you got it in {guesses} guesses")
    #         break
# exit

# project(number guessing game)
#     import random

#     high_num = 100
#     low_num = 1
#     guesses = 0

#     number = random.randint(low_num, high_num)

#     guess = int(input(f"enter a number between {low_num} and {high_num}: "))

#     while True:
#         if guess < low_num or guess > high_num:
#             print(f"{guess} is not between {low_num} and {high_num}")
#             print("please enter a valid number")
#             guess = int(input(f"enter a number between {low_num} and {high_num}: "))
#         elif guess < number:
#             print("too low")
#             guess = int(input(f"enter a number between {low_num} and {high_num}: "))
#         elif guess > number:
#             print("Too high")
#             guess = int(input(f"enter a number between {low_num} and {high_num}: "))
#         else:       
#             print(f"you got it! the number was {number}")
#             break
#         guesses += 1


#     print("-------------------------")
#     print(f"Correct! the number was {number} and you got it in {guesses} guesses!")

# # exit

# rock paper scissors game
    # import random

    # options = ("rock", "paper", "scissors")

    # player = input("enter your choice (rock, paper, scissors) [q to quit]: ").lower()
    # player_score = 0
    # computer_score = 0

    # while player != "q":
    #     computer = random.choice(options) 
    #     while True:
    #         if player not in options:
    #             print(f"{player} is not a valid choice")
    #             player = input("enter your choice (rock, paper, scissors): ").lower()
    #         else:
    #             break

    #     print(f"computer chose {computer}")
    #     print(f"you chose {player}")
    #     print("-------------------------")
    #     if player == computer:
    #         print("tie")
    #         player = input("enter your choice (rock, paper, scissors) [q to quit]: ").lower()
    #     elif (player == options[0] and computer == options[2]) or (player == options[1] and computer == options[0]) or (player == options[2] and computer == options[1]):
    #         print("you win")
    #         player_score += 1
    #         player = input("enter your choice (rock, paper, scissors) [q to quit]: ").lower()
    #     else:
    #         print("you lose")
    #         computer_score += 1
    #         player = input("enter your choice (rock, paper, scissors) [q to quit]: ").lower()
    #         print("-------------------------")
        
    # if player == "q":
    #     print("Game quit")

    # print("-------------------------")
    # print(f"Player Score: {player_score}")
    # print(f"Computer Score: {computer_score}")

    # if player_score > computer_score:
    #     print("You win the game!")
    # elif computer_score > player_score:
    #     print("Computer wins the game!")
    # else:
    #     print("tie")

# exit

# project (dice rolling simulator)

    # import random

    # dice_art = {
    #     1: ("┌─────────┐",
    #         "│         │",
    #         "│    ●    │",
    #         "│         │",
    #         "└─────────┘"),
    #     2: ("┌─────────┐",
    #         "│  ●      │",
    #         "│         │",
    #         "│      ●  │",
    #         "└─────────┘"),
    #     3: ("┌─────────┐",
    #         "│  ●      │",
    #         "│    ●    │",
    #         "│      ●  │",
    #         "└─────────┘"),
    #     4: ("┌─────────┐",
    #         "│  ●   ●  │",
    #         "│         │",
    #         "│  ●   ●  │",
    #         "└─────────┘"),
    #     5: ("┌─────────┐",
    #         "│  ●   ●  │",
    #         "│    ●    │",
    #         "│  ●   ●  │",
    #         "└─────────┘"),
    #     6: ("┌─────────┐",
    #         "│  ●   ●  │",
    #         "│  ●   ●  │",
    #         "│  ●   ●  │",
    #         "└─────────┘")
    # }

    # dice = []
    # total = 0
    # num_of_dice = int(input("Enter the number of dice to roll: "))

    # for die in range(num_of_dice):
    #     roll = random.randint(1,6)
    #     dice.append(roll)

    # # for die in range(num_of_dice):
    # #     for line in dice_art.get(dice[die]):
    # #         print(line)

    # for line in range(5):
    #     for die in dice:
    #         print(dice_art.get(die)[line], end = "")
    #     print()

    # for die in dice:
    #     total += die
    # print(f"total: {total}")

# exit

# projects(encryption)

    # import random
    # import string

    # chars = string.punctuation + string.digits + string.ascii_letters
    # chars = list(chars)
    # key = chars.copy()

    # random.shuffle(key)

    # # print(f"chars: {chars}")
    # # print(f"key: {key}")

    # # encryption
    # plain_text = input("Enter text to encrypt: ")
    # cipher_text = ""

    # for letter in plain_text:
    #     index = chars.index(letter)
    #     cipher_text += key[index]

    # print(f"Plain text: {plain_text}")
    # print(f"Encrypted text: {cipher_text}")

    # # decryption
    # cipher_text = input("Enter text to decrypt: ")
    # plain_text = ""

    # for letter in cipher_text:
    #     index = key.index(letter)
    #     plain_text += chars[index]

    # print(f"Encrypted text: {cipher_text}")
    # print(f"Plain text: {plain_text}")
# exit

# functions

    # # envoke function, need matching number of arguments recived and passed in
    # def happy_birthday(name):
    #     print("happy birthday to you")
    #     print("happy birthday to you")
    #     print(f"happy birthday dear {name}")
    #     print("happy birthday to you")
    #     print()

    # # # calling function
    # # happy_birthday()
    # # happy_birthday()
    # # happy_birthday()

    # # pass values into function
    # happy_birthday("Austin")

    # def display_invoice(username, amount, due_date):
    #     print(f"hello {username} ")
    #     print(f"your bill of ${amount:.2f} is due on {due_date}")

    # display_invoice("Austin", 100.50, "June 30th")

    # def add(x, y):
    #     z = x+y
    #     return z

    # def subtract(x, y):
    #     z = x-y
    #     return z

    # def multiply(x, y):
    #     z = x*y
    #     return z

    # def divide(x, y):
    #     if y == 0:
    #         return "Error: Cannot divide by zero"
    #     else:
    #         z = x/y
    #         return z
        
    # print(add(1, 2))
    # print(subtract(5, 3))
    # print(multiply(2, 4))
    # print(divide(10, 2))

    # def create_name(first, last):
    #     first = first.capitalize()
    #     last = last.capitalize()
    #     return first + " " + last

    # first, last = input("Enter your first and last name: ").split()
    # full_name = create_name(first, last)

    # print(full_name)

# default arguments

    # # accepts other arguments but if not provided uses default values
    # def net_price(list_price, discount=0, tax=0.05):
    #     return list_price * (1 - discount) * (1 + tax)

    # # passing in just price
    # print(net_price(500))

    # # passing in price and discount, tax will be default
    # print(net_price(500, 0.1))

    # # passing in price, discount, and tax
    # print(net_price(500, 0.1, 0))

    # # passing in price and tax, discount will be default
    # print(net_price(500, tax=0.08))

    # import time

    # def count(end, start=0):
    #     for x in range(start, end + 1):
    #         print(x)
    #         time.sleep(1)
    #     print("done")

    # count(10, 6)
# exit

# keyword argumnets - preceded by an identifier 

    # def hello(greeting, title, first, last):
    #     print(f"{greeting} {title}{first} {last}")

    # # precede arguemtns with key words to pass in any order
    # hello("hello", title = "Mr.", first = "Austin", last = "Smith")

    # # positional arugments need to be first
    # hello("hello", "Mr.", last = "Smith", first = "Austin")

    # # end is keyword argument
    # for x in range(1, 11):
    #     print(x, end = " ")

    # # sep is also keyword
    # print("1", "2", "3", sep = "-")

    # def get_phone(country, area, first, last):
    #     return f"{country}-({area})-{first}-{last}"

    # phone_num = get_phone(country =1, area =123, first = 456, last = 789)

    # print(phone_num)
# exit

# arbitrary arguments - *args and **kwargs
# *args - allows you to pass multiple non key arguments
# **kwargs - allows you to pass multiple keyword arguments

    # # pass miltiple non key arguments (use *)
    # def add(*args):
    #     total = 0
    #     for arg in args:
    #         total += arg
    #     return total
    # print(add(1, 2, 3,))

    # # again, muultiple non key arguments (use *)
    # def display_name(*args):
    #     for a in args:
    #         print(a, end = " ")
    # display_name("Dr","Austin", "John", "Smith")

    # # pass multiple keyword arguments (use **)
    # def print_address(**kwargs):
    #     for key, value in kwargs.items():
    #         print(f"{key}: {value}")

    # print_address(street ="123 main st", 
    #               apt = "4B",
    #               city = "Detroit", 
    #               state = "IL", 
    #               zip_code = "63312",)

    # excercise (shipping label)
    # def shipping_label(*args, **kwargs):
    #     for arg in args:
    #         print(arg, end = " ")
    #     print()
    #     if "apt" in kwargs:
    #         print(f"{kwargs.get('apt')}")
    #     else:
    #         print(f"{kwargs.get('street')}")
    #     print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip_code')}")
    


    # shipping_label("Dr", "Austin", "John", "Smith",
    #                street ="123 main st",
    #                apt = "4B",
    #                city = "Detroit",
    #                state = "IL",
    #                zip_code = "63312",)
# exit

# iterables

    # # lists are iterables
    # numbers = [1, 2, 3, 4, 5]
    # for num in numbers:
    #     print(num, end= " ")

    # print()

    # # tuples are also iterables
    # numbers = (1, 2, 3, 4, 5)
    # for num in numbers:
    #     print(num, end= " ")

    # print()

    # # sets are iterables
    # numbers = {1, 2, 3, 4, 5}
    # for num in numbers:
    #     print(num, end= " ")

    # print()

    # # strings are also iterables
    # name = "Austin"
    # for letter in name:
    #     print(letter, end= " ")

    # print()

    # # dicts are also iterables but only iterate through keys by default
    # my_dict = {"a": 1, "b": 2, "c": 3}
    # for value in my_dict.get("b"), my_dict.get("c"):
    #     print(f"{value}")
# exit

# membership opperators - in, not in

    # word = "APPLE"

    # # checks if something is in (returns bool)
    # letter = input("Enter a letter: ").upper()

    # if letter in word:
    #     print(f"There is a[n] {letter}")
    # else:
    #     print(f"There is no {letter}")

    # # checks if something is not in (returns bool)
    # if letter not in word:
    #     print(f"There is no {letter}")
    # else:
    #     print(f"There is a[n] {letter}")

    # students = {"spongebob", "patrick", "sandy",}

    # student_search = input("Enter a student name: ").lower()

    # if student_search in students:
    #     print(f"{student_search} is in the class")
    # else:
    #     print(f"{student_search} is not in the class")

    # grades = {"spongebob": "A",
    #           "patrick": "B",
    #         "sandy": "C",}

    # grade_search = input("Enter a student name: ").lower()

    # if grade_search in grades:
    #     print(f"{grade_search} has a {grades.get(grade_search)}")
    # else:
    #     print("student was not found")

    # email = "brocode@gmail.com"

    # if "@" in email and "." in email:
    #     print("valid email")
    # else:
    #     print("invalid email")
# exit

# list compressions


    # doubles = []
    # for value in range(1, 11):
    #     doubles.append(value * 2)
    # print(doubles)

    # # same thing as above but in one line
    # doubles = [value * 2 for value in range(1, 11)]
    # print(doubles)

    # # examples
    # doubles = [x*2 for x in range(1,11)]
    # print(doubles)

    # triples = [y*3 for y in range(1,11)]
    # print(triples)

    # squares = [z**2 for z in range(1,11)]
    # print(squares)

    # # different method (capitalize)
    # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    # fruits = [fruit.capitalize() for fruit in fruits]
    # print(fruits)

    # # checking condition
    # nums = [1, -2, 3, -4, 5, -6]
    # pos_nums = [num for num in nums if num >= 0]
    # print(pos_nums)

    # grades = [85, 42, 98, 79, 56, 61, 30]
    # passing_grades = [grade for grade in grades if grade >= 60]
    # print(passing_grades)
# exit

# match case (same as if statments)

    # def day_of_week(day):
    #     if day == 1:
    #         return "Monday"
    #     elif day == 2:
    #         return "Tuesday"
    #     elif day == 3:
    #         return "Wednesday"
    #     elif day == 4:
    #         return "Thursday"
    #     elif day == 5:
    #         return "Friday"
    #     elif day == 6:
    #         return "Saturday"
    #     elif day == 7:
    #         return "Sunday"
    #     else:
    #         return "Invalid day"

    # # same as above
    # def day_of_week(day):
    #     match day:
    #         case 1:
    #             return "Monday"
    #         case 2:
    #             return "Tuesday"
    #         case 3:
    #             return "Wednesday"
    #         case 4:
    #             return "Thursday"
    #         case 5:
    #             return "Friday"
    #         case 6:
    #             return "Saturday"
    #         case 7:
    #             return "Sunday"
    #         case _:
    #             return "Invalid day"
        

    # print(day_of_week(1))
# exit

# modules - file containing code that can be imported into another file

    # print(help("modules"))

    # import math
    # import math as m
    # from math import pi

    # print(pi)

    # # creating module - save as .py file and import into another file
    # import example_import as eximport

    # result = eximport.pi

    # print(result)
# exit

# scope resolution
#  LEGB - Local, Enclosing, Global, Built-in

    # # x has local scope to func1
    # def func1():
    #     x = 10
    #     print(x)

    # y has local scope to func2
    # def func2():
    #     y = 5
    #     print(y)

    # func1()
    # func2()

    # # enclosed scope
    # def func1():
    #     x = 1

    #     def func2():
    #         x = 5
    #         print(x)
            
    #     func2()
    
    # func1()

    # # Global
    # def func1():
    #     print(x)


    # def func2():
    #     print(x)

    # x = 10

    # func1()
    # func2()

    # # Built-in
    # from math import e

    # def func1():
    #     print(e)

    # e = 3

    # func1()
# exit

# if __name__ == '__main__': (I have no fucking clue what this does but it seems important)

    # def main():
    #     # program goes here
    #     pass

    # if  __name__ == '__main__':
    #     main()
# exit

# credit card number validator project

    # sum_odd_digits = 0
    # sum_even_digits = 0
    # total = 0

    # card_num = input("Enter a credit card number: ")
    # card_num = card_num.replace("-", "")
    # card_num = card_num.replace(" ", "")
    # card_num = card_num[::-1]

    # for x in card_num[::2]:
    #     sum_odd_digits += int(x)

    # for x in card_num[1::2]:
    #     x = int(x)*2
    #     if x > 9:
    #         sum_even_digits += ((x%10) + 1)
    #     else:
#             sum_even_digits += x

#     total = sum_odd_digits + sum_even_digits

#     if total % 10 == 0:
#         print("valid card number")
#     else:
#         print("invalid card number")

#     exit

# project (banking program)

    # def show_balamce(balance):
    #     print(f"Your balance is ${balance:.2f}")

    # def deposit():
    #     amount = float(input("Enter amount to deposit: "))
    #     if amount <= 0:
    #         print("Amount must be greater than 0")
    #         return 0
    #     else:
    #         return amount 

    # def withdraw (balance):
    #     amount = float(input("Enter amount to withdraw: "))
    #     if amount <= 0:
    #         print("Amount must be greater than 0")
    #         return 0
    #     elif amount > balance:
    #         print("Insufficient funds")
    #         return 0
    #     else:
    #         return amount 

    # def main():
    #     balance = 0
    #     is_running = True

    #     while is_running:
    #         print("Banking Program")
    #         print("1. Show Balace")
    #         print("2. Deposit")
    #         print("3. Withdraw")
    #         print("4. Exit")

    #         choice = input("Enter your choice: 1-4 ")

    #         if choice == "1":
    #             show_balamce(balance)
    #         elif choice == "2":
    #             balance += deposit()
    #             show_balamce()
    #         elif choice == "3":
    #             balance -= withdraw(balance)
    #             show_balamce()
    #         elif choice == "4":
    #             is_running = False
    #             show_balamce()
    #         else:
    #             print("Invalid choice, please try again")

    #     print("Thank you for using the banking program")

    # if __name__ == '__main__':
    #     main()
# exit

# project (slot machine)

    # import random


    # def spin_row():
    #     symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    #     results = []
    #     for _ in range(3):
    #         results.append(random.choice(symbols))
    #     return results

    # def print_row(row):
    #     print("******************")
    #     print(" | ".join(row))
    #     print("******************")

    # def get_payout(row, bet):
    #     if row[0] == row[1] == row[2]:
    #         if row[0] == "🍒":
    #             return bet * 3
    #         elif row[0] == "🍉":
    #             return bet * 4
    #         elif row[0] == "🍋":
    #             return bet * 5
    #         elif row[0] == "🔔":
    #             return bet * 10
    #         elif row[0] == "⭐":
    #             return bet * 20
    #     return 0
        
        
        

    # def main():
    #     balance = 100

    #     print("******************")
    #     print("Welcome to the Slot Machine!")
    #     print("symbols: 🍒 🍉 🍋 🔔 ⭐")
    #     print("******************")
    #     print()
    #     print("******************")
    #     balance = float(input("Enter your starting balance: "))
    #     print("******************")
    #     print()

    #     while balance > 0:
    #         print(f"Your balance is ${balance:.2f}")

    #         bet = input("Enter your bet: ")
    #         if not bet.isdigit():
    #             print("Invalid bet amount. Please enter a valid number.")
    #             continue
    #         bet = int(bet)
    #         print("******************")
    #         if bet > balance:
    #             print("Insufficient balance. Please enter a bet amount less than or equal to your current balance.")
    #             continue
    #         print("******************")
    #         if bet <= 0:
    #             print("Bet amount must be greater than 0. Please enter a valid bet amount.")
    #             continue
    #         print("******************")

    #         balance -= bet
            
    #         row = spin_row()
    #         print("Spinning...\n")
    #         print_row(row)

    #         payout = get_payout(row, bet)

    #         if payout > 0:
    #             print(f"Congratulations! You won ${payout:.2f}!")
    #         else:
    #             print("Sorry, you lost. Better luck next time!")
    #         balance += payout

    #         play_again = input("Do you want to play again? (y/n): ").lower()
    #         if play_again != "y":
    #             break

    #     print(f"Thank you for playing the Slot Machine! Goodbye! final balance: ${balance:.2f}")

    # if __name__ == '__main__':
    #     main()
# exit

# project (hangman game)

    # hangman_art = {0: ("   ",
    #                 "   ",
    #                 "   "),
    #             1: (" o ",
    #                 "   ",
    #                 "   "),
    #             2: (" o ",
    #                 " | ",
    #                 "   "),
    #             3: (" o ",
    #                 "/| ",
    #                 "   "),
    #             4: (" o ",
    #                 "/|\\",
    #                 "   "),
    #             5: (" o ",
    #                 "/|\\",
    #                 "/  "),
    #             6: (" o ",
    #                 "/|\\",
    #                 "/ \\")}

    # def display_man(wrong_guesses):
    #     print("*************")
    #     for line in hangman_art[wrong_guesses]:
    #         print(line)
    #     print("*************")

    # def display_hint(hint):
    #     print(" ".join(hint))


    # def display_answer(answer):
    #     print(" ".join(answer))

    # def main():
    #     answer = input("Player 1, Enter a word for the hangman game: ").lower()
    #     for _ in range(5):
    #         print()
    #     hint = ["_"] * len(answer)
    #     print("Player 2, try to guess the word, number of letters:")
    #     print(hint)
    #     wrong_guesses = 0
    #     guessed_letters = set()
    #     is_running = True

    #     while is_running:
    #         display_man(wrong_guesses)
    #         display_hint(hint)
    #         guess = input("Enter a letter: ").lower()

    #         if len(guess) != 1 or not guess.isalpha():
    #             print("Invalid Input")
    #             continue

    #         if guess in guessed_letters:
    #             print("You already guessed that letter")
    #             continue

    #         guessed_letters.add(guess)

    #         if guess in answer:
    #             for i in range(len(answer)):
    #                 if answer[i] == guess:
    #                     hint[i] = guess
    #         else: 
    #             wrong_guesses += 1

    #         if "_" not in hint:
    #             display_man(wrong_guesses)
    #             display_answer(answer)
    #             print("Congratulations! You won!")
    #             print(f"You had {wrong_guesses} wrong guesses!")
    #             is_running = False
    #         elif wrong_guesses >= len(hangman_art) - 1:
    #             display_man(wrong_guesses)
    #             display_answer(answer)
    #             print("Game Over! You lost!")
    #             is_running = False

    # if __name__ == '__main__':
    #     main()

# object oriented programming (OOP)
# related attributes (variables) and methods (functions)

# class - blueprint, simlar to functions in the way we pass values through
# you can import a class from another file to create objects
    # class car:
    #     def __init__(self, model, year, color, for_sale):
    #         self.model = model
    #         self.year = year
    #         self.color = color
    #         self.for_sale = for_sale

    #     def drive(self):
    #         print(f"you drive the {self.model}")

    #     def stop(self):
    #         print(f"you stop the {self.model}")

    #     def describe(self):
    #         print(f"{self.year} {self.color} {self.model}")

    # # filling in the "blueprint"
    # car1 = car("Mustang", 2020, "red", True)
    # car2 = car("Camaro", 2021, "blue", False)
    # car3 = car("Challenger", 2022, "black", True)

    # # accessing attributes of an object
    # print(car1.model)
    # print(car1.year)
    # print(car1.color)
    # print(car1.for_sale)

    # # accessing attributes of another object using same blueprint
    # print(car2.model)
    # print(car2.year)
    # print(car2.color)
    # print(car2.for_sale)

    # print(car3.model)
    # print(car3.year)
    # print(car3.color)
    # print(car3.for_sale)

    # car1.drive()
    # car1.stop()
    # car1.describe()


    # car2.drive()
    # car2.stop()
    # car2.describe()

    # car3.drive()
    # car3.stop()
    # car3.describe()
# exit

# class variables - shares among all objects of a class

    # class student:
        
    #     # class variable
    #     class_year = 2024
    #     num_of_students = 0

    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age
    #         # accessing the entire class instead of each individual (self) objexts
    #         student.num_of_students += 1


    # student1 = student("Austin", 20)
    # student2 = student("John", 21)

    # # class variable is the same for all objects of the class
    # print(student1.name)
    # print(student1.age)
    # print(student.class_year)

    # print(student2.name)
    # print(student2.age)
    # print(student.class_year)

    # print(student.num_of_students)

    # print(f"my graduating class of {student.class_year} has {student.num_of_students} students")
# exit

# inheritance - child class inherits attributes and methods from parent class

    # sets up parent class 
    # class animal:
    #     def __init__(self, name):
    #         self.name = name
    #         self.is_alive = True

    #     def eat(self):
    #         print(f"{self.name} is eating")

    #     def sleep(self):
    #         print(f"{self.name} is sleeping")

    # # each one of these has all the attributes that the animal class does, also with their own mehtods etc    #   
    # class dog(animal):
    #     def speak(self):
    #         print("Woof")

    # class cat(animal):
    #     def speak(self):
    #         print("Meow")

    # class mouse(animal):
    #     def speak(self):
    #         print("Squeak")

    # dog = dog("Rover")
    # cat = cat("Fluffy")
    # mouse = mouse("Jerry")

    # print(dog.name)
    # print(dog.is_alive)
    # dog.eat()
    # dog.sleep()

    # dog.speak()
    # cat.speak()
    # mouse.speak()
# exit

# multiple inheritance - child class inherits from multiple parent classes

    # class animal:

    #     def __init__(self, name):
    #         self.name = name

    #     def eat(self):
    #         print(f"this {self.name} eats")

    #     def sleep(self):
    #         print(f"this {self.name} sleeps")
        



    # class prey(animal):
    #     def flee(self):
    #         print(f"this {self.name} flees")


    # class predator(animal):
    #     def hunt(self):
    #         print(f"this {self.name} hunts")

    # class rabbit(prey):
    #     pass

    # class hawk(predator):
    #     pass

    # class fish(prey, predator):
    #     pass

    # # assinging objects to classes, then calling methods of those objects
    # rabbit = rabbit()
    # hawk = hawk()
    # fish = fish()

    # rabbit.flee()
    # hawk.hunt()
    # fish.flee()
    # fish.hunt()

    # rabbit.eat()
    # hawk.sleep()
    # fish.eat()

    # # assinging names to calling methods of those objects
    # rabbit = rabbit("rabbit")
    # hawk = hawk("hawk")
    # fish = fish("fish")

    # rabbit.eat()
    # hawk.sleep()
    # fish.eat()
# exit

# abstract classes - cannot be instantiated on its own (in what world do we use this??)

    # from abc import ABC, abstractmethod

    # class vehicle(ABC):
    #     @abstractmethod
    #     def drive(self):
    #         pass

    #     @abstractmethod
    #     def stop(self):
    #         pass

    # class car(vehicle):
    #     def drive(self):
    #         print("you drive the car")

    #     def stop(self):
    #         print("you stop the car")

    # class motorcycle(vehicle):
    #     def drive(self):
    #         print("you drive the motorcycle")

    #     def stop(self):
    #         print("you stop the motorcycle")

    # class boat(vehicle):
    #     def drive(self):
    #         print("you drive the boat")

    #     def stop(self):
    #         print("you stop the boat")

    # car = car()
    # motorcycle = motorcycle()
    # boat = boat()

    # car.drive()
    # car.stop()

    # motorcycle.drive()
    # motorcycle.stop()

    # boat.drive()
    # boat.stop() 
# exit

# super() - allows you to call methods from a parent class

    # # # all of these share color filled, but different others
    # # class circle:
    # #     def __init__ (self, color, filled, radius):
    # #         self.color = color
    # #         self.filled = filled
    # #         self.radius = radius

    # # class square:
    # #     def __init__ (self, color, filled, width):
    # #         self.width = width
    # #         self.filled = filled
    # #         self.color = color

    # # class triangle:
    # #     def __init__ (self, color, filled, width, height):
    # #         self.base = width
    # #         self.height = height
    # #         self.filled = filled
    # #         self.color = color

    # # using super() (or calling it with the class name [shape]) to avoid repeating code and just call the parent class for the shared attributes
    # class shape():
    #     def __init__ (self, color, filled):
    #         self.color = color
    #         self.filled = filled

    #     def describe(self):
    #         print(f"this shape is {self.color} and filled: {self.filled}")

    # # both calls with super() and with the class name work, but super() is more common and easier to read
    # class circle(shape):
    #     def __init__ (self, color, filled, radius):
    #         super().__init__(color, filled)
    #         self.radius = radius

    #     # method overriding
    #     def describe(self):
    #         print(f"this circle has an area of {3.14*self.radius**2:.2f} and a circumference of {2*3.14*self.radius:.2f}")
    #         super().describe()

    # class square(shape):
    #     def __init__ (self, color, filled, width):
    #         self.width = width
    #         super().__init__(color, filled)

    # # calling with class name
    # class triangle(shape):
    #     def __init__ (self, color, filled, width, height):
    #         self.base = width
    #         self.height = height
    #         shape.__init__(self, color, filled)

    # circle = circle(color = "red", filled = True, radius = 5)
    # square = square(color = "blue", filled = False, width = 4)
    # triangle = triangle(color = "green", filled = True, width = 3, height = 4)

    # print(circle.color)
    # print(circle.filled)
    # print(circle.radius)   

    # print(square.color)
    # print(square.filled)
    # print(square.width)

    # print(triangle.color)
    # print(triangle.filled)
    # print(triangle.base)
    # print(triangle.height)

    # square.describe()
    # circle.describe()
    # triangle.describe()
# exit

# polymorphism

    # from abc import ABC, abstractmethod

    # class shape(ABC):
        
    #     @abstractmethod
    #     def area(self):
    #         pass

    # class circle(shape):
    #     def __init__ (self, radius):
    #         self.radius = radius

    #     def area(self):
    #         return 3.14 * self.radius ** 2


    # class square(shape):
    #     def __init__ (self, side):
    #         self.side = side

    #     def area(self):
    #         return self.side ** 2

    # class triangle(shape):
    #     def __init__(self, base, height):
    #         self.base = base
    #         self.height = height

    #     def area(self):
    #         return 0.5 * self.base * self.height

    # # pizza is a circle but with a topping, so we can use super() to call the area method of the circle class and add the topping as an attribute
    # class pizza(circle):
    #     def __init__ (self, topping, radius):
    #         self.topping = topping
    #         super().__init__(radius)


    # shapes = [circle(radius=5), square(side=4), triangle(base=3, height=4), pizza(topping="pepperoni", radius=6)]

    # for shape in shapes:
    #     print(shape.area())

# duck typing - if it looks like a duck and quacks like a duck, it's a duck (doesn't matter what class it is, as long as it has the same methods)

    # class animal:
    #     alive = True

    # class dog(animal):
    #     def speak(self):
    #         print("Woof")
                
    # class cat(animal):
    #     def speak(self):
    #         print("Meow")

    # class car:
    #     def speak(self):
    #         print("Beep")
        
    #     alive = False

    # animals = [dog(), cat(), car()]

    # for animal in animals:
    #     animal.speak()
    #     print(animal.alive)
# exit

# aggergation 

# the (whole) class contains other classes (parts) but the parts can exist without the whole    
    # class library:
    #     def __init__ (self, name):
    #         self.name = name
    #         self.books = []

    #     # method to add books to the library
    #     def add_book(self, book):
    #         self.books.append(book)

    #     def list_books(self):
    #         for book in self.books:
    #             print(f"{book.title} by {book.author}")

    # # the (parts) 
    # class book:
    #     def __init__(self, title, author):
    #         self.title = title
    #         self.author = author

    # library = library("NYC Public Library")

    # book1 = book("Hairy Potter", "JK Rowling")
    # book2 = book("The Hobbit", "JRR Tolkien")
    # book3 = book("The Hunger Games", "Suzanne Collins")

    # # adding in our parts (books) to the whole (library) but the books can exist without the library, they are not dependent on each other
    # library.add_book(book1)
    # library.add_book(book2)
    # library.add_book(book3)

    # print(library.name)
    # print(library.list_books())
# exit

# composition - the (whole) class contains other classes (parts) but the parts cannot exist without the whole

    # class engine:
    #     def __init__(self, horse_power):
    #         self.horse_power = horse_power

    # class wheel:
    #     def __init__(self, size):
    #         self.size = size

    # class car:
    #     def __init__(self, make, model, horse_power, wheel_size):
    #         self.make = make
    #         self.model = model
    #         self.engine = engine(horse_power)
    #         self.wheels = [wheel(wheel_size) for _ in range(4)]

    #     def display_car(self):
    #         return f"{self.make} {self.model} with {self.engine.horse_power} HP engine and {self.wheels[0].size}"

    # car1 = car(make="Ford", model="Mustang", horse_power=300, wheel_size=18)
    # car2 = car(make="Chevy", model="Camaro", horse_power=350, wheel_size=19)

    # print(car1.display_car())
    # print(car2.display_car())
# exit

# nested classes

    # # # same name (employee) but different classes (company and non_profit) so they can have different attributes and methods
    # # class company:
    # #     class employee:
    # #         print("this is the employee class")

    # # class non_profit:
    # #     class employee:
    # #         print("this is the second class)")

    # class company:
    #     class employee:
    #         def __init__(self, name, position):
    #             self.name = name
    #             self.position = position

    #         def get_details(self):
    #             return f"{self.name} is a {self.position}"

    #     def __init__(self, name):
    #         self.name = name
    #         self.employees = []

    #     def add_employee(self, name, position):
    #         new_employee = self.employee(name, position)
    #         self.employees.append(new_employee)

    #     def list_employees(self):
    #         return [employee.get_details() for employee in self.employees]


    # company1 = company("walamrt")
    # company1.add_employee("John", "Manager")
    # company1.add_employee("Jane", "Cashier")
    # company1.add_employee("Bob", "Stocker")

    # company2 = company("Red Cross")
    # company2.add_employee("Alice", "Director")
    # company2.add_employee("Eve", "Volunteer")

    # for employee in company1.list_employees():
    #     print(employee)

    # print()

    # for employee in company2.list_employees():
    #     print(employee)
# exit

# static methods - belongs to class rather than object from that class (instance)

    # class Employee:

    #     def __init__ (self, name, position):
    #         self.name = name
    #         self.position = position

    #     def get_info(self):
    #         return f"{self.name} = {self.position}"
        
    #     # belongs to class not to objedts
    #     @staticmethod
    #     def is_valid_position(position):
    #         valid_positions = ["Manager", "Cashier", "Stocker", "Director", "Volunteer"]
    #         return position in valid_positions
        

    # employee1 = Employee("John", "Manager")
    # employee2 = Employee("Jane", "Cashier")
    # employee3 = Employee("Bob", "Stocker")

    # Employee.is_valid_position("Manager")
    # print(employee1.get_info())
    # print(employee2.get_info())
    # print(employee3.get_info())
# exit

# class methods - operations related to class itself(cls)

    # class Student:

    #     count = 0
    #     total_gpa = 0

    #     def __init__(self, name, gpa):
    #         self.name = name
    #         self.gpa = gpa
    #         Student.count += 1
    #         Student.total_gpa += gpa

    #     # instance method 
    #     def get_info(self):
    #         return f"{self.name} {self.gpa}"
        
    #     @classmethod
    #     def get_count(cls):
    #         return f"total num of students: {cls.count}"
        
    #     @classmethod 
    #     def get_avg_gpa(cls):
    #         if cls.count ==0:
    #             return 0
    #         else:
    #             return f"{cls.total_gpa / cls.count}"






    # student1 = Student("Spongebob", 3.2)
    # student2 = Student("kid", 4.0)
    # studnet3 = Student("gary", 2.7)


    # print(Student.get_count())
    # print(Student.get_avg_gpa())
# exit

# magic methods - dunder methods 

    # class Book:
    #     def __init__(self, title, author, num_pages):
    #         self.title = title
    #         self.author = author
    #         self.num_pages = num_pages

    #     # return string representation of object when printing directly to console
    #     def __str__(self):
    #         return f"{self.title} by {self.author}"
        
    #     # equal method
    #     def __eq__(self, other):
    #         return self.title == other.title and self.author == other.author
        
    #     # less than
    #     def __lt__(self, other):
    #         return self.num_pages < other.num_pages
        
    #     # add
    #     def __add__(self, other):
    #         return self.num_pages + other.num_pages
        
    #     # if something contains (is word in title/author)
    #     def __contains__(self, keyword):
    #         return keyword in self.title or keyword in self.author
        
    #     def __getitem__(self, key):
    #         if key == "title":
    #             return self.title
    #         if key == "author":
    #             return self.author
    #         elif key == "num_pages":
    #             return self.num_pages
    #         else:
    #             return f"{key} was not found"


    # book1 = Book("hobbit", "dick balls", 310)
    # book2 = Book("harry potter", "dick and balls", 500)
    # book3 = Book("whippers", "slave owner", 67)

    # print(book1)
    # print(book1 == book2)
    # print(book1 < book2)
    # print(book1 + book2)
    # print("slave" in book3)
    # print(book1["title"])
    # print(book1["author"])
    # print(book1["num_pages"])
    # print(book1["anal"])
# exit

# decorator - func that extends behavior of another func without modifying the base func

    # # formula for basic decorator
    # def add_sprinkles(func):
    #     def wrapper(*args, **kwargs):
    #         print("*u add sprinkles*")
    #         func(*args, **kwargs)
    #     return wrapper

    # def add_fudge(func):
    #     def wrapper(*args, **kwargs):
    #         print("adding fudge")
    #         func(*args, **kwargs)
    #     return wrapper

    # @add_sprinkles
    # @add_fudge
    # def get_ice_cream(flavor):
    #     print(f"here is your {flavor} ice cream")

    # get_ice_cream("choc")
# exit

# @property

    # class Rectangle:
    #     def __init__(self, width, h):
    #         self._width = width
    #         self._h = h

    #     @property
    #     def width(self):
    #         return f"{self._width:.1f} cm"
    #     @property
    #     def h(self):
    #         return f"{self._h:.1f} cm"

    #     @width.setter
    #     def width(self, new_width):
    #         if new_width > 0:
    #             self._width = new_width
    #         else:
    #             print("width must be greater than 0")

    #     @h.setter
    #     def h(self, new_h):
    #         if new_h > 0:
    #             self._h = new_h
    #         else:
    #             print("h must be greater than 0")

    #     @width.deleter
    #     def width(self):
    #         del self._width
    #         print("deleted")

    #     @h.deleter
    #     def h(self):
    #         del self._h
    #         print("deleted")



    # rectangle = Rectangle(3, 4)

    # # setter
    # rectangle.h = 6
    # rectangle.width = 10

    # # del rectangle.h
    # # del rectangle.width

    # print(rectangle.width, ",", rectangle.h)
# exit

# LAMBDA - small, one time use, then throw them away

    # double = lambda x: x*2
    # add = lambda x, y: x+y
    # max_value = lambda x, y: x if x > y else y
    # min_value = lambda x, y: x if x< y else y
    # full_name = lambda first, last: first + " " + last
    # is_even = lambda x: x % 2 == 0
    # age_check = lambda age: True if age >= 18 else False

    # print(double(2))
    # print(add(6, 7))
    # print(max_value(10, 9))
    # print(min_value(15, 8))
    # print(full_name("smith", "john"))
    # print(is_even(18))
    # print(age_check(21))
# exit

# sorting - .sort() or sorted()

    # # lists, alphabet, ascending, descedning (fruits.sort(reverse=True))
    # fruits = ["apple", "orange", "banana" ]
    # fruits.sort()
    # print(fruits)

    # # tuples
    # fruits = ("apple", "orange", "banana")
    # fruits = sorted(fruits)
    # print(fruits)

    # # dict
    # fruits = {"apple":72,
    #          "orange":73, 
    #          "banana":90}
    # fruits = sorted(fruits.items())
    # print(fruits)

    # sort by value in reverse
    # fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
    # print(fruits)

    # sort by key
    # fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
    # print(fruits)

    # sort by key in reverse
    # fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse = True))
    # print(fruits)

    # # obj
    # class Fruit:
    #     def __init__(self, name, calories):
    #         self.name = name
    #         self.calories = calories

    #     def __repr__(self):
    #         return f"{self.name}, {self.calories}"

    # fruit1 = Fruit("banama", 105)
    # fruit2 = Fruit("apple", 90)
    # fruit3 = Fruit("orange", 55)

    # fruits = [fruit1, fruit2, fruit3]

    # fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse = True)
    # print(fruits)

    # fruits = sorted(fruits, key = lambda fruit: fruit.calories, reverse = True)
    # print(fruits)
# exit

# zip() - combines iterables into single iterator

    # names = ["Spongebob", "patrick", "squid"]
    # ages = [30, 35, 50]
    # jobs = ["Cook", "UE", "cashier"]

    # data = list(zip(names, ages, jobs))

    # for name, age, job in data:
    #     print(f"{name} is {age} years old and is a {job}")

# exit

# recursion - func that calls itself from within (chop something complex into basic steps)

    # # iterative
    # def walk(steps):
    #     for step in range(1, steps+1):
    #         print(f"you take step {step}")
    # walk(100)

    # # recursion 
    # def walk(steps):
    #     if steps == 0:
    #         return
    #     walk(steps - 1)
    #     print(f"you take step {steps}")
    # walk(100)

    # # iterative
    # def factorial(x):
    #     result = 1
    #     if x > 0:
    #         for y in range(1, x+1):
    #             result *=y
    #         return result
    # factorial(10)

    # # recursion
    # def factorial(x):
    #     if x ==1:
    #         return 1
    #     else:
    #         return x * factorial(x - 1)

    # print(factorial(10))

# exception handling (try, except, finally)

    # # # ZeroDivisionError
    # # 1/0

    # # # TypeError
    # # 1+"1"

    # # # ValueError
    # # int("pizza")

    # try:
    #     number =int(input("enter number: "))
    #     print(1/number)
    # except ZeroDivisionError:
    #     print("cannot divide by 0")
    # except ValueError:
    #     print("enter only numbers")
    # # catches all exceptions, but very vauge
    # except Exception:
    #     print("something went wrong")
    # finally:
    #     print("do some cleanup")

# exit

# file detection

    # import os 

    # # acces file in folder
    # file_path = "learnpy/test.txt"

    # if os.path.exists(file_path):
    #     print(f"the location '{file_path}' exits")
    # else:
    #     print("location does not exist")

    # # folder directly on desktop
    # file_path = "C:/Users/austi/OneDrive/Desktop/test.txt"
    # if os.path.exists(file_path):
    #     print(f"the location '{file_path}' exits")
        
    #     if os.path.isfile(file_path):
    #         print("that is a file")
    #     elif os.path.isdir(file_path):
    #         print("that is a directory")
    # else:
    #     print("location does not exist")
# exit

# writing files

    # txt_data = "I like pizza"

    # file_path = "output.txt"

    # # w is for write, and will override a file
    # with open(file = file_path, mode = "w") as file:
    #     file.write(txt_data)
    #     print(f"text file '{file_path} was created")

    # try:
    # # will write if does not exist already using "x" (but also catching the error)
    #     with open(file = file_path, mode = "x") as file:
    #         file.write(txt_data)
    #         print(f"text file '{file_path} was created")
    # except FileExistsError:
    #     print("that file already exists")

    # # append with a, new data will be appended to the file
    # with open(file = file_path, mode = "a") as file:
    #     file.write("\n" + txt_data)
    #     print(f"text file '{file_path} was created")

    # # lopping thru lists converting to string then putting each on a new line
    # employees = ["mr. krabs", "squid", "spongebob"]

    # file_path = "output.txt"

    # with open(file = file_path, mode = "w") as file:
    #     for employee in employees:
    #         file.write(employee + "\n")
    #     print(f"text file '{file_path} was created")

    # # json file
    # import json

    # employees = {"name" : "Spongebob", "age" : 30,
    #              "job" : "cook"}
    # file_path = "output.json"

    # with open(file = file_path, mode = "w") as file:
    #     json.dump(employees, file, indent=4)
    #     print(f"text file '{file_path} was created")

    # # csv 
    # import csv

    # employees = [["name", "age", "job"],
    #              ["Sponge", 30, "cook"], 
    #              ["patty", 35, "janitor"], 
    #              ["krabs", 55, "manager"]]
    # file_path = "output.csv"

    # with open(file = file_path, mode = "w") as file:
    #     writer = csv.writer(file)
    #     for row in employees:
    #         writer.writerow(row)
    #     print(f"text file '{file_path} was created")
# exit

# reading files
    # file_path = "example.txt"

    # # r for read
    # try:
    #     with open(file_path, "r") as file:
    #         content = file.read()
    #         print(content)
    # except FileNotFoundError:
    #     print("file not found")
    # except PermissionError:
    #     print("you do not have premission to view this file")

    # # json
    # import json

    # try:
    #     with open(file_path, "r") as file:
    #         content = json.load(file)
    #         print(content["name"])
    # except FileNotFoundError:
    #     print("file not found")
    # except PermissionError:
    #     print("you do not have premission to view this file")

    # # csv
    # import csv
    # try:
    #     with open(file_path, "r") as file:
    #         content = csv.reader(file)
    #         for line in content:
    #             print(line)
    # except FileNotFoundError:
    #     print("file not found")
    # except PermissionError:
    #     print("you do not have premission to view this file")
# exit

# measure execution time

    # import time

    # start_time = time.perf_counter()

    # for i in range(10000000):
    #     pass

    # end_time = time.perf_counter()

    # elapsed_time = end_time - start_time

    # print(f"the elapsed time is {elapsed_time:.1f}s")
# exit

# dates and times

    # import datetime as dt

    # # date/date of today
    # date = dt.date(2026, 4, 19)
    # today = dt.date.today()
    # # print(today)

    # # time
    # time = dt.time(12, 30, 0)
    # # print(time)

    # # current time
    # current_time = dt.datetime.now()
    # # print(current_time)

    # # formatted current time
    # current_time = current_time.strftime("%H:%M:%S, %m-%d-%Y")
    # print(current_time)

    # target_datetime = dt.datetime(2030, 1, 2, 12, 30, 1)
    # current_datetime = dt.datetime.now()

    # if target_datetime < current_datetime:
    #     print("target date has passed")
    # else: 
    #     print("target date has NOT pass")
# exit

# iterators

    # import random

    # class Dice:
    #     def __init__(self, rolls):
    #         self.rolls = rolls
    #         self.count = 0

    #     def __iter__(self):
    #         return self
        
    #     def __next__(self):
    #         if self.count < self.rolls:
    #             self.count += 1
    #             return random.randint(1, 6)
    #         else:
    #             raise StopIteration
            
    # dice = Dice(3)

    # for die in dice:
    #     print(die)

    # dice = [die for die in Dice(3)]

    # print(dice)

    # # how the python interpeter iterates this (unimportant to actual language, but good to understand)
    # dice = Dice(3)

    # iterator = dice.__iter__()

    # while True:
    #     try:
    #         roll = iterator.__next__()
    #         print(roll)
    #     except StopIteration
    #         break
# exit

# generators - behaves like iterator (pause button)

    # # non generator way, no drip faucet possible memory issues, but makes most logical, east to read, sense
    # def count_to(n):
    #     nums = []
    #     count = 1
    #     while count <= n:
    #         nums.append(count)
    #         count += 1
    #     return nums

    # number = int(input("Enter a num to count to: "))

    # for n in count_to(number):
    #     print(n)


    # # generator way 
    # def count_to(n):
    #     count = 1
    #     while count <= n:
    #         yield count
    #         count += 1

    # number = int(input("Enter a num to count to: "))

    # for n in count_to(number):
    #     print(n)

    # # generator with file access from computer
    
    # def read_file(file_path):
    #     with open(file_path) as file:
    #         for line in file:
    #             yield line.strip()

    # file_path = "C:example.txt"
    # for line in read_file(file_path):
    #     print(line)
# exit

# generator expression
    # # (expression for value in iterable)

    # # basic generator expression
    # number = int(input("enter a number to count to: "))

    # counter = (count for count in range(1, number + 1))

    # for num in counter:
    #     print(num)

    # # gen express for file on pc

    # file_path = "C:example.txt"

    # with open(file_path) as file:
    #     lines = (line.strip() for line in file)
    #     for line in lines:
    #         print(line)

    # # adding if condition

    # number = int(input("enter num to square up to: "))

    # even_squares = (x**2 for x in range(1, number +1) if x %2 == 0)
    # for square in even_squares:
    #     print(square)
# exit

# multi threading - run multiple threads of code at the same time (concurrent execution)

    # import threading 
    # import time

    # def walk_dog(first, last):
    #     time.sleep(8)
    #     print(f"you are walking {first} {last}")


    # def trash():
    #     time.sleep(5)
    #     print("you are taking out the trash")

    # def mail():
    #     time.sleep(3)
    #     print("you are checking the mail")

    # # creating threads for each chore, so they can run at the same time instead of waiting for one to finish before starting the next one (concurrent execution)
    # chore1 = threading.Thread(target = walk_dog, args = ("Rover", "Smith"))
    # chore1.start()

    # chore2 = threading.Thread(target = trash)
    # chore2.start()

    # chore3 = threading.Thread(target = mail)
    # chore3.start()

    # chore1.join()
    # chore2.join()
    # chore3.join()

    # print("chores are done")
# end

# Request data from API
    # import requests

    # base_url = "https://pokeapi.co/api/v2/"

    # def get_pokemon_info(name):
    #     url = f"{base_url}pokemon/{name.lower()}"
    #     response = requests.get(url)

    #     if response.status_code == 200:
    #         pokemon_data = response.json()
    #         return pokemon_data
    #     else:
    #         print(f"failed to retrieve data {response.status_code}")

    # pokemon_name = "ditto"
    # pokemon_info = get_pokemon_info(pokemon_name)

    # if pokemon_info:
    #     print(f"Name: {pokemon_info['name'].capitalize()}")
    #     print(f"ID: {pokemon_info['id']}")
    #     print(f"Height: {pokemon_info['height']}")
    #     print(f"Weight: {pokemon_info['weight']}")
# end





# scroll




















# scroll


















# PyQt is unable to work right now, so this is basically the end of course