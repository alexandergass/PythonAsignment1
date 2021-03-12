
try:
    number1 = float(input("Enter first number: "));
    number2 = float(input("Enter second number: "));
except:
    print("Non-number entered");
    exit();

def addThem(number1, number2):
    sum = number1+number2;
    return sum;

def subtractThem(number1, number2):
    difference = number1-number2;
    return difference;

def multiplyThem(number1, number2):
    product = number1*number2;
    return product;

def divideThem(number1, number2):
    quotient = number1/number2;
    return quotient;

print(number1," plus ",number2," is ",addThem(number1, number2));
print(number1," minus ",number2," is ",subtractThem(number1, number2));
print(number1," times ",number2," is ",multiplyThem(number1, number2));
print(number1," over ",number2," is ",divideThem(number1, number2));
