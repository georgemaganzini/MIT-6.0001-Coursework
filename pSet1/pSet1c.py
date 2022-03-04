# -*- coding: utf-8 -*-

annual_salary = float(input("Enter your annual salary: "))

starting_annual_salary = annual_salary
total_cost = 1000000
portion_down_payment = total_cost * .25

epsilon = 100
semi_annual_raise = .07
monthly_salary = annual_salary / 12
r = .04

current_savings = 0

low = 0
high = 10000
rate_guess = (high + low) /2.0
num_guesses = 0


times = 0
# while abs(current_savings - portion_down_payment) >= epsilon:
while True:
    if annual_salary * 3 < portion_down_payment:
        print("It is not possible to pay the down payment in three years")
        break
    months = 0
    while months < 36:
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = (annual_salary/12)
        current_savings += current_savings*r/12
        current_savings += (monthly_salary*rate_guess) / 10000
        months += 1

    num_guesses += 1
    times += 1


    print(num_guesses, rate_guess/100, current_savings, high, low)

    if abs(current_savings - portion_down_payment) <= epsilon:
        break

    if current_savings > portion_down_payment:
        high = rate_guess
    else:
        low = rate_guess
    rate_guess = int((high + low)/2)
    current_savings = 0
    annual_salary = starting_annual_salary

print("Steps in bisection search:", num_guesses)
print("Best savings rate:", rate_guess)