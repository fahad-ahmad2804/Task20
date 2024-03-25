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

swim_time = int(input("Enter the Swim time in minutes: "))
cyc_time = int(input("Enter the Cycling time in minutes: "))
run_time = int(input("Enter the Run time in minutes: "))
total_time = str(swim_time + cyc_time + run_time)
if (swim_time + cyc_time + run_time >=0 and swim_time + cyc_time + run_time <=100):
  print('''Congratulations! Your total time is: " + total_time + " minutes,\n
  You have been awarded Provincial Colours!''')
elif (swim_time + cyc_time + run_time >=101 and swim_time + cyc_time + run_time <=105):
    print('''Congratulations! Your total time is: " + total_time + " minutes,\n
You have been awarded Provincial Half Colours!''')
elif (swim_time + cyc_time + run_time >=106 and swim_time + cyc_time + run_time <=110):
  print('''Congratulations! Your total time is: " + total_time + " minutes,\n
You have been awarded Provincial Scroll!''')
elif (swim_time + cyc_time + run_time >=111):
    print('''Your total time is: " + total_time + " minutes,\nThanks for taking part, better luck next time!''')