# Task 04: Logical Programming - Operators
# Declare 3 variables to store the times for swimming, cycling and running
# Name these variables based on the activity they represent
# Convert each variable to integer
# Declare a variable to store the total time based on the three inputs
# Use a nested if/elif structure
# Add each input using the "+" arithmetic operator to calculate a total time
# Use a combination of comparison operators, coupled with the "and" logical operator
# To judge which range the total input falls within
# Structure the if/elif statements in ascending order
# print the total time
# Print the correct award message based on the total time

s_time = int(input("Enter the Swim time in minutes: "))
c_time = int(input("Enter the Cycling time in minutes: "))
r_time = int(input("Enter the Run time in minutes: "))
total = int(s_time + c_time + r_time)
if (s_time + c_time + r_time >=0 and s_time + c_time + r_time <=100):
  print('''Congratulations! Your total time is: " + total_time + " minutes,\n
  You have been awarded Provincial Colours!''')
elif (s_time + c_time + r_time >=101 and s_time + c_time + r_time <=105):
    print('''Congratulations! Your total time is: " + total_time + " minutes,\n
You have been awarded Provincial Half Colours!''')
elif (s_time + c_time + r_time >=106 and s_time + c_time + r_time <=110):
  print('''Congratulations! Your total time is: " + total_time + " minutes,\n
You have been awarded Provincial Scroll!''')
elif (s_time + c_time + r_time >=111):
    print('''Your total time is: "''' + str(total) + '''" minutes,\nThanks for taking part, better luck next time!''')