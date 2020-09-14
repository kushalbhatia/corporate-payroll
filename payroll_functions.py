# Corporate Payroll Project

# def is defining function, get_salary is calling function and employee_id is the parameter that the function is calling upon:
def get_salary(employee_id):  # get employees salary
    if employee_id < 100:
        salary = 50000
    elif employee_id > 100 and employee_id < 500:
        salary = 100000
    else:
        salary = 150000
    return salary  # return employees salary


print(get_salary(400))  # 400 is the employee_id and prints 100000


def get_grade(employee_id):  # get employees grade
    if employee_id < 100:
        grade = 5
    elif employee_id > 100 and employee_id < 500:
        grade = 10
    else:
        grade = 15
    return grade  # return employees grade


print(get_grade(400))  # 400 is the employee_id and prints 10


def compute_bonus(employee_id):  # get employees bonus
    base_bonus = 500
    large_bonus_percent = 1.05
    small_bonus_percent = 1.02
    salary = get_salary(employee_id)
    grade = get_grade(employee_id)
    if grade < 15:
        bonus = large_bonus_percent*salary
    elif grade < 10:
        bonus = small_bonus_percent*salary
    else:
        bonus = base_bonus
    print(employee_id, salary, grade, bonus)
    return bonus  # return employees salary with bonus


print(compute_bonus(400))  # 400 is the employee_id and prints 105000
