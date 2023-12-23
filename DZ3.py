result = []

def divider(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("a and b should be numbers")
        if a < b:
            raise ValueError("a should be greater than or equal to b")
        if b == 0:
            raise ZeroDivisionError("division by zero")
        if b > 100:
            raise IndexError("b should be less than or equal to 100")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
        return None
    except IndexError as ie:
        print(f"IndexError: {ie}")
        return None
    except TypeError as te:
        print(f"TypeError: {te}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, (1, 2, 3): 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
