def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
    except TypeError as e:
        print(f"Invalid input: {e}")
        return None
    finally:
        print("Execution completed.")
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: None