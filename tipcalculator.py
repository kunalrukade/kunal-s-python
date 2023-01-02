#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Kunals tip Calculator")

bill = input("What was the total bill ?\n")
bill_flt = float(bill)
tip = input("What percentage of the bill would you like to tip ? eg 10%, 12% or 15%\n")
tip_flt = float(tip)

no_of_people = input("How many people would split the bill ?\n")
no_of_people_flt = float(no_of_people)

total_tip = (tip_flt/100) * bill_flt
total_bill = bill_flt + total_tip
money_per_head = total_bill / no_of_people_flt
rounded_per_head = round(money_per_head, 2)

print(f"Each person should pay : {rounded_per_head}")