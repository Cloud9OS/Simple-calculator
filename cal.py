print("your operators +,-,*,/")
num = input("put your first number: ")
operator = input("put your operator: ")
num2 = input("put your second number: ")

def cal():
    try:
        if operator == "+":
            return float(num)+float(num2)
        if operator == "-":
            return float(num)-float(num2)
        if operator == "*":
            return float(num)*float(num2)
        if operator == "/":
            return float(num)/float(num2)
    except ValueError as err:
        print(err)

print(cal())
