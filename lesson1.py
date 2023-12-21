def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
    return pay

# Prompt user for input
hours_input = input("Enter hours worked: ")
rate_input = input("Enter rate per hour: ")

# Convert input to numeric values
try:
    hours = float(hours_input)
    rate = float(rate_input)
except ValueError:
    print("Error: Please enter numeric values for hours and rate.")
    exit()

# Calculate and print gross pay using the computepay function
gross_pay = computepay(hours, rate)
print(f"Pay {gross_pay}")