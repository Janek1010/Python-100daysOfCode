#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What is your bill value $$$?"))
people = int(input("For how many people split it?"))
tip = (float(input("Tell me tip percentage value")) / 100) + 1.0

print(f"bill is ${bill} people: {people} people and tip percentage is ${tip}")

to_pay = round(bill / people * tip, 2)
print(f"Your payment: ${to_pay:.2f}")
