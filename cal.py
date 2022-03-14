def cal():
    try:
        while True:
            print("your operators +,-,*,/")
            num = input("put your first number: ")
            operator = input("put your operator: ")
            num2 = input("put your second number: ")

            def operation():
                if operator == "+":
                    return float(num)+float(num2)
                elif operator == "-":
                    return float(num)-float(num2)
                elif operator == "*":
                    return float(num)*float(num2)
                else:
                  operator == "/"
                  return float(num)/float(num2)
            print(operation())
    except (ValueError, TypeError):
        print("Invalid input")
    except:
        print("An Error")
    cal()



cal()
