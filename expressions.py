def calc_math_expression(num1, num2, operator):

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == ":":
        print(num1 / num2)
    else:
        print("None")

def calc_math_expression_from_str(str_input):
    str_input = 'num1,operator,num2'
    print(str_input.split(","))

def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    if num1 >= num2 and num1 >= num3:
        max = num1
    elif num2 >= num1 and num2 >= num3:
        max = num2
    else:
        max = num3

    if num1 <= num2 and num1 <= num3:
        min = num1
    elif num2 <= num1 and num2 <= num3:
        min = num2
    else:
        min = num3
    return min, max

    print("max, min")

def quadratic_equation_solver(a, b, c):
    d = b**2-4*a*c
    if d < 0:
        print("none")
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        return (x)
        print("none")
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
        x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
        return (x1, x2)


def quadratic_equation_solver_from_user_input():
    () = float(int_a, int_b, int_c)

    print(user_input().split(","))
    return (quadratic_equation_solver(a,b,c))

def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if min_temp < temp_1 and min_temp < temp_2:
        return True
    elif min_temp < temp_2 and min_temp < temp_3:
        return True
    elif min_temp < temp_3 and min_temp < temp_1:
        return True
    elif min_temp < temp_2 and min_temp < temp_3:
        return True
    else:
        return False
