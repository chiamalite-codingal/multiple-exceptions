try:
  num1 , num2 = eval(input("Enter numbers separated by comma:"))
  result = num1/num2
  print(result)
except SyntaxError:
  print("use comma between 1st and 2nd number!")
except ZeroDivisionError:
  print("Don't use zero in denominator")
except NameError:
  print("Don't use alphabets use numbers")
else:
  print("Invalid!")
finally:
  print("The code is running fine")