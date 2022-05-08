import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('salary.csv')

years = df.Year.to_list()
teacher_salary = df.Teacher.to_list()
adviser_salary = df.Adviser.to_list()
programmer_salary = df.Programmer.to_list()


plt.plot(years, teacher_salary, 'k--o', label='Teacher salary')
plt.plot(years, adviser_salary, 'b.-.', label='Advisor salary')
plt.plot(years, programmer_salary, 'y-s', label='Programmer salary')

plt.tight_layout()
plt.grid(True)
plt.legend()
plt.title("Mean salaries charts")
plt.xlabel('Year')
plt.ylabel('Salary')

plt.show()