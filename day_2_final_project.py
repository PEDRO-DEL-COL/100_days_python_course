bill = float(input('What is the total bill? '))
tip = float(input('How much tip would you like to give? 10, 12 or 15? '))
total_pay = round(bill + bill * (tip / 100), 2)
amout_of_people = int(input('How many people will split the bill? '))
final_pay_per_person = round(total_pay / amout_of_people, 2)
print(f'The ${bill} bill with {tip}% tip is a total pay of ${total_pay}.\nEach person should pay ${final_pay_per_person}.')