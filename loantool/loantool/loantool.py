import os 
import numpy_financial as npf
import random
import numpy as np
  

# loantool()
def loan_data(prin = 5000.0, rate = 5.0, term = 4) :
    # if (prin != 5000.0):
    #     prin = float(input("What is the principal for your loan?"))
    # if (rate != 5.0):
    #     rate = float(input("What is the rate of Intrest?"))/100
    # if (term != 4):
    #     term = int(input("How long is the loan for?"))


    return((prin, rate/1200, term))


   
payment = 0
def one_time_payment (): 
    if input("do u wann make 1 time payment? [y/n]") == "n":
        return

    return float(input("how much do u wan pay? "))


data = []

for _ in range(4):
    data.append(loan_data(random.uniform(1000.0, 10000.0), random.uniform(3.0, 12.0), random.randint(1, 6)))


def monthly_payment(rate, number_of_payments, present_value, future_value) :
    return -npf.pmt(rate, number_of_payments, present_value, future_value, "end")


    
def interest_saved(prin, one_time_payment, rate, monthly_payment, term):
    per = np.arange(term*12)
    temp = npf.ipmt(rate, per, term*12, prin,) 
    interest_paid = np.sum(temp)

    new_prin = prin - one_time_payment
    new_number_of_payments = -npf.nper(rate, monthly_payment, new_prin,)
    new_per = np.arange(int(new_number_of_payments))
    temp2 = npf.ipmt(rate, new_per, new_number_of_payments, new_prin)
    # print(new_number_of_payments)

    interest_saved = -interest_paid + np.sum(temp2)

    return interest_saved

# print(interest_saved(10000, 5000, .0072, 246.96, 4))


for d in data:
    prin = d[0]
    rate = d[1]
    term = d[2]
    payment = monthly_payment(rate, 12*term, prin, 0)
    print(f'principal: {prin:.2f}\trate: {rate:.4f}\tterm: {term}\tmonthly_payment: {payment:.2f}')


# print(one_time_payment())

def generate_rate_dictionary(data):
    dictionary = {}
    for loan in data:
        prin, rate, term = loan
        dictionary[rate] = (prin, rate, term, monthly_payment(rate, term*12, prin, 0))
    dictionary.keys
    
    return dictionary

def apply_one_time_payment(payment, data_dictionary):
    sorted_keys = sorted(data_dictionary.keys(), reverse=True)
    decision_list = []
    remaining_loans = []

    for rate in sorted_keys:
        prin, rate, term, monthly_payment = data_dictionary[rate]
        if prin > payment:
            #add payment amount and remaining loan balance to decision list 
            decision_list.append((payment, prin))
            remaining_loans.append((prin - payment, rate, term, monthly_payment))
            payment = 0
        elif payment > prin:
            payment -= prin
            decision_list.append((prin, prin))
        else:
            remaining_loans.append((prin, rate, term, monthly_payment))
    return decision_list, remaining_loans, payment


     


data_dictionary = generate_rate_dictionary(data) 

result = apply_one_time_payment(15000, data_dictionary)
print()
print("Payments To make Towards loans: (payment amount, loan principal)")
for r in result[0]:
    print(r)
print()
print("loans left to do: (prin, rate, term, monthly payment)")
for r in result[1]:
    print(r)
print()
print("left over one time payment:")
print(result[2])


