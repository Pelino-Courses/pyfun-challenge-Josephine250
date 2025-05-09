def process_inputs(*args):
    """
    Validates and processes the input arguments.

    Parameters:
    - *args: Arbitrary number of numerical inputs.

    Returns:
    - list: A list of validated float numbers.

    Raises:
    - ValueError: If any input is not a number.
    """
    processed = []
    for arg in args:
        if isinstance(arg, (int, float)):
            processed.append(float(arg))
        else:
            raise ValueError(f"Invalid input: {arg} is not a number.")
    return processed

def calculate(*args, **kwargs):
    """
    Perform arithmetic operations on input numbers.

    Parameters:
    - *args: Numerical inputs.
    - **kwargs: Keyword arguments indicating operations to apply. 
        Supported operations: add, subtract, multiply, divide (all booleans).

    Returns:
    - float: Result of the calculation based on specified operations.

    Raises:
    - ValueError: If no numbers or no valid operations are provided.
    - ZeroDivisionError: If division by zero is attempted.
    """
    numbers = process_inputs(*args)

    if not numbers:
        raise ValueError("At least one numeric input is required.")

    operations = {k: v for k, v in kwargs.items() if v is True and k in {'add', 'subtract', 'multiply', 'divide'}}

    if not operations:
        raise ValueError("At least one valid operation (add, subtract, multiply, divide) must be specified.")

    result = numbers[0]

    for operation in operations:
        if operation == 'add':
            result = sum(numbers)
        elif operation == 'subtract':
            result = numbers[0]
            for n in numbers[1:]:
                result -= n
        elif operation == 'multiply':
            result = numbers[0]
            for n in numbers[1:]:
                result *= n
        elif operation == 'divide':
            result = numbers[0]
            for n in numbers[1:]:
                if n == 0:
                    raise ZeroDivisionError("Division by zero encountered.")
                result /= n

    return result

# Interactive mode
if __name__ == "__main__":
    try:
        nums_input = input("Enter numbers separated by spaces: ")
        nums = [float(n) for n in nums_input.strip().split()]
        
        op_input = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()
        valid_ops = {"add", "subtract", "multiply", "divide"}

        if op_input not in valid_ops:
            raise ValueError(f"Invalid operation. Choose from {', '.join(valid_ops)}")

        # Construct keyword argument dynamically
        operation_kwargs = {op_input: True}

        result = calculate(*nums, **operation_kwargs)
        print("Result:", result)
    
    except ValueError as ve:
        print("Error:", ve)
    except ZeroDivisionError as ze:
        print("Math Error:", ze)
