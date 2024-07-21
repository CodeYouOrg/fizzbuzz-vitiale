# add your code here


def fizzbuzzFunction(a, b):
    if a < b :
        for i in range(a,b):
            if i % 3 == 0 and i % 5 == 0 :
                print('FizzBuzz')
            elif i % 3 == 0 :
                print('Fizz')
            elif i % 5 == 0 :
                print('Buzz')
            else:
                print(i)
    else:
        print("Make sure the first number entered is less than the second number")

try:

    num1 = int(input("Enter the first number in the range: "))

    num2 = int(input("Enter the second number in the range: "))

    fizzbuzzFunction(num1, num2)

except ValueError:

    print("Invalid input. Please enter valid integers")    

        

