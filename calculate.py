import functools


def stability_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Error occurred during code execution: {e}")
            return None

    return wrapper


@stability_decorator
def calculate(expression):
    return eval(expression)


while True:
    expression = input("Enter a mathematical expression (or 'exit' to quit): ")

    if expression.lower() == 'exit':
        print("Exiting the program.")
        break

    result = calculate(expression)

    print(f"The result of the expression '{expression}' is: {result}")
