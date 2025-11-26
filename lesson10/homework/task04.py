# Напишите программу, которая запрашивает у пользователя оценки студента по трем предметам
# и выводит, прошел ли студент на следующий курс на основе средней оценки.
# Программа должна использовать логические выражения для принятия решения о результате.
# Запросите у пользователя оценки по трем предметам (например, математика, физика и информатика).
# Напишите функцию, которая в качестве параметров принимает три оценки и выполняет следующие действия:
# Рассчитывает среднюю оценку. Использует логические выражения для определения,
# прошел ли студент на следующий курс:
# Если средняя оценка равна или больше 4.0, студент проходит.
# Если средняя оценка ниже 4.0, студент не проходит.
# Возвращает True, если студент проходит, False - если нет.
# Вызвав функцию, получите результат и выведите на экран информацию по следующему шаблону:
# Оценки студента: 5, 3, 4 Студент проходит (или не проходит) на следующий курс.

def get_student_grades(grade1, grade2, grade3):
    average_grade = (grade1 + grade2 + grade3) / 3
    return average_grade >= 4.0


def print_function():
    math = float(input("What is your math score? "))
    physics = float(input("What is your physics score? "))
    informatics = float(input("What is your informatics score? "))
    result = get_student_grades(math, physics, informatics)
    if result:
        print("Student's grade:", math, ",", physics, ",", informatics, "The student passes to the next course.")
    else:
        print("Student's grade:", math, ",", physics, ",", informatics,
              "The student doesn't pass to the next course.")


print_function()