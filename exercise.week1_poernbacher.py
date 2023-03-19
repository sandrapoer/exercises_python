#QUESTION NR1
def name_age():
    name = input("Please enter you name: ")
    age = int(input("Please enter your age: "))
    name = str.upper(name)
    print(f"Hello {name}. Your age is: {age}")
    name = str.capitalize(name)
    return f"{name}{age}"

#QUESTION NR2
def swap_integers(num1,num2):
    print(f"Before:\r\nX={num1} \r\nY={num2}\r\n")
    num1, num2 = num2, num1
    print(f"After swap:\r\nX={num1} \r\nY={num2}\r\n")
    return f"{num1}{num2}"

#QUESTION NR3
def check_numbers(num1, num2):
    if num1 % 6 == 0 or num2 % 6 == 0:
        if num1 % 10 == 0 and num2 % 10 == 0:
            return True
        else:
            return False
    else:
        return False

#QUESTION NR4
def sum_up(num1,num2):
    result = 0
    if num1 > num2:
        return 0
    else:
        if num1 <= 0 and num2 <= 0:
            return 0
        else:
            for number in range(num1, num2+1, 1):
                result += number
    return result

#QUESTION NR5
def circle_area(r1, r2, r3):
    pi = 3.142
    return pi*(r1**2) + pi*(r2**2) + pi*(r3**2)

#QUESTION NR6
def check_string(text):
    if text.startswith("a") or text.endswith("a") or text.startswith("A") or text.endswith("A"):
        return True
    else:
        return False

#QUESTION NR7
def triangle(rows):
    for number in range(1, rows+1, 1):
        print("*" * number)