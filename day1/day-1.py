import pandas as pd
from samp_package import module1 as ext
employee_data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "IT", "IT", "Sales"],
    "Salary": [50000, 75000, 82000, 60000]
}
df = pd.DataFrame(employee_data)

for employee in zip(df["Name"],df["Department"]):
    print(employee)

multiplesOf4 = [4*i for i in range(1,11)]
print(multiplesOf4)

for ind,val in enumerate(multiplesOf4, start=1):
    print(f"{ind}*4 = {val}")

a,b=(1,3)
print(a,b)
#a,b=(1,3,5)
#print(a)
#a,b=(1)
#print(a,b)

with open("sample.txt") as file:
    data = file.read()
print(data)
#print(file.read())

ext.display_name('nisha')

