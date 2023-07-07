"""
Avand urmatorul fisier JSON: file.
Creati un program care va afisa urmatoare informatie din fisier.
• Lista de toti lucratorii
• Lista la toate pozitiile din companie (Unicale)
• Calculeaza suma totala care compania are de achitat lucratorii
• Calculeaza suma totala de impozite care compania are de achitat intr-o luna
   • Valoarea de % impozit e introdusa la consola
• Afiseaza informatie despre 10 cei mai bine platiti lucratori ((name, position, salary, employment_start_date) de la
   mai mult la mai putin.
• Afiseaza informatie despre 10 lucratori cu cel mai mult timp in companie (name, position, salary,
   employment_start_date) de la mare la mic.
"""
# Solution
import json

# Read JSON data from file
with open('C:\\Users\\dabij\\OneDrive\\Desktop\\employee_list.json') as file:
    data = json.load(file)

# List all employee names
employee_names = [employee['name'] for employee in data]
print("Employee Names:")
print(*employee_names, sep="\n")

# List all position names
position_names = list(set(employee['position'] for employee in data))
print("\nPosition Names:")
print(*position_names, sep="\n")

# Calculate the total salary per month
total_salary = sum(employee['salary'] for employee in data)
print("\nTotal Salary per Month:", total_salary)

# Calculate the amount of money the company has to pay in taxes per month
tax_percentage = float(input("\nEnter the tax percentage: "))
tax_amount = (tax_percentage / 100) * total_salary
print("Tax Amount per Month:", tax_amount)

# Display information for the top 10 highest paid employees
top_10_highest_paid = sorted(data, key=lambda x: x['salary'], reverse=True)[:10]
print("\nTop 10 Highest Paid Employees:")
for employee in top_10_highest_paid:
    print("Name:", employee['name'])
    print("Position:", employee['position'])
    print("Salary:", employee['salary'])
    print("Employment Start Date:", employee['employee_from'])
    print()

# Display information for the top 10 employees with the longest time in the company
top_10_longest_employment = sorted(data, key=lambda x: x['employee_from'])[:10]
print("\nTop 10 Employees with Longest Time in the Company:")
for employee in top_10_longest_employment:
    print("Name:", employee['name'])
    print("Position:", employee['position'])
    print("Salary:", employee['salary'])
    print("Employment Start Date:", employee['employee_from'])
    print()