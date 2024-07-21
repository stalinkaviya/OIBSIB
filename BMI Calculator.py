# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

class BMI_Calculator:
    def __init__(self):
        self.users = {}

    def calculate_bmi(self, weight, height):
        return weight / (height ** 2)

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def add_user_data(self, name, weight, height):
        bmi = self.calculate_bmi(weight, height)
        category = self.classify_bmi(bmi)
        if name not in self.users:
            self.users[name] = {"weights": [weight], "heights": [height], "bmis": [bmi], "categories": [category]}
        else:
            self.users[name]["weights"].append(weight)
            self.users[name]["heights"].append(height)
            self.users[name]["bmis"].append(bmi)
            self.users[name]["categories"].append(category)

    def visualize_history(self, name):
        if name not in self.users:
            print("User not found.")
            return

        weights = self.users[name]["weights"]
        heights = self.users[name]["heights"]
        bmis = self.users[name]["bmis"]
        categories = self.users[name]["categories"]

        # Plot BMI history
        plt.figure(figsize=(10, 6))
        plt.plot(bmis, marker='o', linestyle='-')
        plt.xlabel('Measurement Index')
        plt.ylabel('BMI')
        plt.title('BMI History')
        plt.xticks(np.arange(len(bmis)), [f"Measurement {i}" for i in range(1, len(bmis) + 1)])
        plt.grid(True)
        plt.show()

        # Plot weight and height history
        plt.figure(figsize=(10, 6))
        plt.plot(weights, marker='o', linestyle='-', color='b', label='Weight (kg)')
        plt.plot(heights, marker='o', linestyle='-', color='r', label='Height (m)')
        plt.xlabel('Measurement Index')
        plt.ylabel('Value')
        plt.title('Weight and Height History')
        plt.xticks(np.arange(len(weights)), [f"Measurement {i}" for i in range(1, len(weights) + 1)])
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plot BMI categories
        categories_count = {"Underweight": 0, "Normal weight": 0, "Overweight": 0, "Obese": 0}
        for category in categories:
            categories_count[category] += 1
        labels = list(categories_count.keys())
        values = list(categories_count.values())
        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('BMI Categories Distribution')
        plt.show()

def main():
    bmi_calculator = BMI_Calculator()

    while True:
        print("\nBMI Calculator Menu:")
        print("1. Calculate BMI")
        print("2. Add user data")
        print("3. Visualize history")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            bmi = bmi_calculator.calculate_bmi(weight, height)
            category = bmi_calculator.classify_bmi(bmi)
            print(f"Your BMI is: {bmi:.2f}")
            print(f"Category: {category}")
        elif choice == "2":
            name = input("Enter your name: ")
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            bmi_calculator.add_user_data(name, weight, height)
            print("User data added successfully.")
        elif choice == "3":
            name = input("Enter your name: ")
            bmi_calculator.visualize_history(name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()