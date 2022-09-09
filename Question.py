# #Question One
# # a= "positive" if int(input('Enter the number:'))>0 else "non positivepositive"
# # print(a)

# # print("positive" if int(input('Enter the number:'))>0 else "non-postive") 

# # TODO: QuestionTwo

# # number = int(input('Enter the number:'))
# # if number % 5 ==0:
# #   print('Divisible by Five')
# # else:
# #   print('Not Divisible By Five')

# # TODO: SingleLine If Else

# # print('Divisible by Five' if int(input('Enter the number:')) % 5 ==0 else "not divisible by 5")

# # TODO: QUESTION Three/ Single Line If Else

# # print("Even Number" if int(input('Enter the number')) % 2 ==0 else "Odd number")

# # TODO: Question Four

# # firstNumber= int(input('Enter the 1st number:'))
# # secondNumber = int(input('Enter the number:'))

# # if(firstNumber>secondNumber):
# #   print('First Number is Greater')
# # elif (firstNumber<secondNumber):
# #   print('Second Number is Greater')
# # else:
# #   print(firstNumber)
  
# # Ineuron Solution 

# # print('Enter two Numbers:')
# # a,b = int(input()), int(input())

# # print(a if a>b else b)




# # TODO: Question 5 I neuron Solution
# # print('Enter two words:')
# # a,b = input(), input()
# # print(b,a if a>b else a,b )

# # TODO: Question 6

# # i = int(input('Enter the number:'))
# # if(i>99):
# #   print('Its a Three Digit Number')
# # else:
# #   print('Its not a three digit Number')

# # Ineuron Solution
# x = int(input('Enter the number:'))
# print('Three Digit Number' if 99<x<1000 else "Not a Three Digit Number")


# # print('Its a Three Digit Number' if int(input('Enter the number:'))>99 else 'its not a three digit number') 

# # TODO: Question 7
# # number = int(input('Enter the number:'))
# # if(number>0):
# #   print('Its a positive number')
# # elif number <0:
# #   print('Its a negative number')
# # else:
# #   print('It a Zero')

# # print('positive number'if int(input('Enter the number:')) >0 else "negative" if int(input('Enter the number:'))<0 else '0')


# # TODO:Question 10
# # a,b,c = 98,90,120
# # if (a>b) and (a>c):
# #   print(a,' a is greater')
# # elif b>a and b>c:
# #   print(b,' b is greater')
# # elif c>a and c>b:
# #   print(c,'c is greater')
# # else:
# #   if(a ==b) or (a==c):
# #     print(a)

# # TODO: Implement this for single line if else

# # Question 10 2nd way

# # a,b,c = 100,90,100
# # print(a if a>b and a>c else b if b>a and b>c else c)


# # TODO:Question 11 
# # a = int(input('Enter Month Number:'))
# # if a in (1,3,5,7,8,10,20):
# #   print('31 Days')
# # elif a in (4,6,9,11):
# #   print('30 Days')
# # elif a == 2:
# #   print('28Days')
# # else:
# #   print('Invalid Month Number')

# # TODO: Question 12
# a = 10+50j

# # print(int(a.real) if a.real>a.imag else int(a.imag))
# # if int((a.real)) > int((a.imag)):
# #   print(int(a.real),'real part is greater')
# # else:
# #   print(int(a.imag),'imaginary part is greater')


# # TODO: QUESTION 9

# # year = int(input('Enter the Year:'))

# # if(year % 4 == 0):
# #   if (year % 100 == 0):
# #     if(year % 400 ==0):
# #       print('The Year',year,'Is a leap Year')
# #     else:
# #       print('The Year',year, 'is not a leap Year')
# #   else:
# #     print('The Year',year,'is a leap Year')
# # else:
# #   print('The Year',year,'is not a leap Year')


# # if(year % 4 ==0) and (year % 100 !=0) or (year % 400 ==0):
# #   print('The Year',year,'Is a Leap Year')
# # else:
# #   print('The Year', year, 'is not a Leap Year')

# # year = int(input('Enter the year:'))
# # result = 'Leap Year' if year % 400 ==0 else "Leap Year" if year % 4 ==0 and year % 100 !=0 else 'Nt a Leap Year'
# # print(result)


