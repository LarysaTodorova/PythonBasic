def calculate_gross_salary(salary_rate, hours, bonus):
    gross = salary_rate * hours + bonus
    return gross

def calculate_net_salary(salary_gross, tax):
    tax_sum = salary_gross * tax / 100
    net = salary_gross - tax_sum
    return net


salary_per_hour = float(input("Enter salary per hour: "))
working_hours = int(input("Enter working hours: "))
fixed_bonus = float(input("Enter the employee's bonus amount: "))
tax_rate = int(input("Enter the income tax rate: "))


gross_salary = calculate_gross_salary(salary_per_hour, working_hours, fixed_bonus)
net_salary = calculate_net_salary(gross_salary, tax_rate)
print("The employee will receive", net_salary, "euros.")