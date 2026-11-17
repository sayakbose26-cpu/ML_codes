import matplotlib.pyplot as plt
students = ["A", "B", "C", "D", "E"]
marks = [45, 60 , 75, 85, 95]
hours = [2, 3, 4, 5, 6]
study_marks= [ 30, 50, 70, 80, 90]
plt.subplot(2,2,1)
plt.scatter(hours, study_marks, color='red', label='Study Hours vs Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Student Performance')
plt.legend()
plt.subplot(2,2,2)
plt.bar(students, marks, color='blue', label='Marks of Students')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Student Performance')
plt.legend()
plt.subplot(2,2,3)
plt.hist(marks, bins=5, color='yellow', label='Marks Distribution')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Marks Distribution')
plt.legend()
plt.show()