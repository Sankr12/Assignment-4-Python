# Write a python script to calculate simple interest 

initial = int(input("Enter initial Amount: "))

Rate = int(input("Enter the rate of interest: "))

Time = int(input("Enter the time: "))

final = (initial*Rate*Time)/100 + initial

SI = final - initial

print("The Simple interest of Your Amount:",SI)