import time

print("Welcome to the Random Number Generator! Please state your number")
x = input()
print("Thank you for your number.")
for i in range (3):
    time.sleep(3)
    print("Generating random number")
print(x + " is your random number!")
