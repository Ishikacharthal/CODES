import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

print(df)

print(df[["Name", "Department", "Salary"]])

avg_salary = df.groupby("Department")["Salary"].mean()
print("Average Salary by Department:")
print(avg_salary)

plt.bar(df["Name"], df["Salary"])
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Salary Analysis")
plt.show()

avg_salary.plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.show()