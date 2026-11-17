import matplotlib.pyplot as plt
hours = [2, 3, 4, 5, 6]
python_marks = [ 30, 50, 70, 80, 90]
java_marks = [ 25, 45, 65, 75, 85]
plt.figure(figsize=(9,5))
plt.plot(hours, python_marks, color='red', linewidth=2, linestyle='-', marker='o', label='Python Marks')
plt.plot(hours, java_marks, color='blue', linewidth=2, linestyle='--', marker='s', label='Java Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Student Performance')
plt.legend()
plt.show()