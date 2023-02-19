Average = 0, 
Total = 0
HowManyEntered = 0
HowMany = int(input('how many test scores would you like to input?'))

while HowManyEntered < HowMany:
 testScore = (int(input('enter test score')))
 Total = (Total + testScore)
 HowManyEntered = HowManyEntered + 1;


else:
    Average = Total / HowMany

    print('The average for the test score you entered is: ')
print(Average)
