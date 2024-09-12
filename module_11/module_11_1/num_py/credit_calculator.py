"""
Данный модуль представляет кредитный калькулятор с использованием
библиотек numpy и numpy_financial
"""
import numpy_financial as npf
import numpy as np

credit_rate = float(input('Введите кредитную ставку (%): '))
credit_amount = float(input('Введите сумму кредита: '))
credit_time = int(input('Введите срок (лет): '))

monthly_rate = (credit_rate / 100) / 12
total_payments = credit_time * 12

annuity_payment = npf.pmt(monthly_rate, total_payments, -credit_amount)

principal_payment = credit_amount / total_payments

remaining_loan_amounts = credit_amount - \
    np.arange(total_payments) * principal_payment

interest_payments = remaining_loan_amounts * monthly_rate

differentiated_payments = principal_payment + interest_payments


print(f"{'Платеж':<10}{'Аннуитетный':<15}{'Дифференцированный':<15}")

for i, payment in enumerate(differentiated_payments, 1):
    print(f"{i:<11}{round(annuity_payment, 2):<16}{round(payment, 2):<16}")

total_cost_annuity = annuity_payment * total_payments
total_cost_differentiated = sum(differentiated_payments)

print(f'\nПереплата при аннуитетном погашении: {
      round(total_cost_annuity - credit_amount, 2)}')
print(f"Переплата при дифференцированном погашении: {
      round(total_cost_differentiated - credit_amount, 2)}")
