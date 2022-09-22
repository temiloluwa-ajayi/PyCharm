fahrenheit = int(input("Enter a temperature in degrees F: "))

celsiusMethod = (fahrenheit - 32) * (5 / 9)

print(f"{fahrenheit} degrees F = {celsiusMethod} degrees C")

celsius = int(input("Enter a temperature in degrees C: "))

fahrenheitMethod = celsius * (9 / 5) + 32

print(fahrenheit)
print(f"{celsius} degrees C =  {fahrenheitMethod} degrees F")
