#input will accept user entered string and hold it to use
#print("Hello " + input("What is your name? ")+"!")
#calculate the length of the user input
#print(len(input("What is your name? ")))


a = input("a: ")
b = input("b: ")

c=a
a=b
b=c

print("a: "+a)
print("b: "+b)

#Band name program
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator!")
#2. Ask the user for the city that they grew up in.
User_City = input("What city did you grow up in?\n")
#3. Ask the user for the name of a pet.
User_Pet = input("What is the name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("I would name your band "+User_City+" "+User_Pet+"!\n")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

#variables and converting str to int
num_var = input("Enter a two digit number:")
num_var1 = int(num_var[0])
num_var2 = int(num_var[1])
print(num_var1+num_var2)

print(2**2)

#tip calculator
#Tip Calculator
#Bill of $150 add 12% tip
#tip = 150 times .12
#add tip back to original bill amount
#variables
print("Welcome to the tip calculator!")
bill_amount = input("What is the bill amount? $")
tip_amt = input("What percent would you like to tip? e.g. 10, 12, 15: \n")
parties = input("How many people are paying the bill?\n")
split_bill_amt = float(bill_amount)/int(parties)
individual_tip = split_bill_amt*float(int(tip_amt)*.01)
individual_amt = round(split_bill_amt+individual_tip,2)
message = print(f"Each member of the party will pay ${individual_amt:.2f}.")