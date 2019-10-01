import logging

class CalculateApp(object):

    def __init__(self):
        print('Welcome! to the calculator app')
        print('You can use below mentioned operations')
        print('--------------------add')
        print('--------------------subtract')
        print('--------------------divide')
        print('--------------------multiply')
        print('--------------------modulus')

    try:
	
	    # Addition of Numbers
        def add(self, num):
            if len(num) > 0 and num.find(','):
                num_lst = num.split(',')
                sum_nums = 0
                for numb in num_lst:
                    sum_nums += int(numb)
                    # logging.info('Adding the number(s) '+str(i))
                print('Sum is : '+str(sum_nums))
                return sum_nums
            else:
                return 0
				
		# Substraction of numbers
        def subt(self, num):
            if len(num) > 0 and num.find(','):
                num_lst = num.split(',')
                diff_nums = 0
                for numb in num_lst:
                    diff_nums -= int(numb)
                print('Difference is : '+str(diff_nums))
                return diff_nums
            else:
                return 0
				
		# Division of two numbers
        def divi(self, num1, num2=1):
            if num2 == 0:
                logging.critical('division by zero')
            div = num1/num2
            print('Division is : '+str(div))
            return div
			
		# Multiplication of two numbers
        def mult(self,num):
            if len(num) > 0 and num.find(','):
                num_lst = num.split(',')
                mul_nums = 0
                for numb in num_lst:
                    mul_nums *= int(numb)
                print('Multiplication is : '+str(mul_nums))
                return mul_nums
				
		# modulus of two numbers
        def mod(self, num1, num2=1):
            if num2 == 0:
                logging.critical('Mod by zero')
            mod = num1 % num2
            print(' Modulus is : '+str(mod))
            return mod
    except:
        print("something went wrong!!")
        logging.critical('There is an exception')

# Execution starts from here
if __name__ == '__main__':
    try:
        calc = CalculateApp()
        operations = ['add', 'subtract', 'multiply', 'divide', 'modulus']
        opr = input ("Enter the operation to be performed from above list: ")
        if not opr in operations:
            logging.critical('Invalid operation type entered.')

        if opr.lower() == 'divide' or opr.lower() == 'modulus':
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
        else:
            num = input('Enter the numbers separated by ",": ')

        if str(opr.casefold()) == 'add':
            calc.add(num)
        elif str(opr.casefold()) == 'subtract':
            calc.subt(num)
        elif str(opr.casefold()) == 'divide':
            calc.divi(num1, num2)
        elif str(opr.casefold()) == 'multiply':
            calc.mult(num)
        elif str(opr.casefold()) == 'modulus':
            calc.mod(num1, num2)
        else:
            print('Please check the entered operation type')
            logging.error('Invalid operation type entered')
    except:
        logging.critical('Invalid operation')

