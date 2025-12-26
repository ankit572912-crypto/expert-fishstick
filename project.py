
import pandas as pd
import matplotlib.pyplot as plt 


# Create Student GPA Dataset

data = {
    "Student_ID": [1,2,3,4,5,6,7,8,9,10],
    "Name": ["Amit","Akash","Golu","Neha","Raushan",
             "Ankit","Sneha","Karan","Pooja","Arjun"],
    "Semester": [1,1,2,2,3,3,4,4,2,1],
    "GPA": [7.8,6.2,8.9,5.4,9.1,4.9,8.2,6.8,9.5,5.8]
}

df = pd.DataFrame(data)

print("Student GPA Data:")
print(df)
print("-" * 40)


# Summary Statistics

print("GPA Summary Statistics:")
print(df["GPA"].describe())
print("-" * 40)


# Average GPA per Semester (Trend)

avg_gpa = df.groupby("Semester")["GPA"].mean()
print("Average GPA per Semester:")
print(avg_gpa)
print("-" * 40)


# Top & Bottom Performers

top_students = df.sort_values(by="GPA", ascending=False).head(3)
bottom_students = df.sort_values(by="GPA").head(3)

print("Top Performers:")
print(top_students)
print("-" * 40)

print("Bottom Performers:")
print(bottom_students)

print("-" * 40)

# GPA Histogram

plt.hist(df["GPA"], bins=15)
plt.xlabel("GPA")
plt.ylabel("Number of Students")
plt.title("GPA Distribution")
plt.show()
