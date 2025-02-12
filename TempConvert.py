#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  userInput = input("enter the temp in Fahrenheit: ")
  fTemp = float(userInput)

  #Convert that temperature to celsius, rounding to 1 decimal percision
  cTemp = (fTemp - 32) * 5 / 9
  #Output converted temperature.
  print(fTemp)

  print(cTemp)
  tempF = 80

  tempC = tempF / 2

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
