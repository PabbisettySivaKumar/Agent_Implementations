def add_numbers(input_text: str):
    try:
        nums = [float(x) for x in input_text.replace(",", " ").split() if x.replace('.', '', 1).isdigit()]
        if len(nums) < 2:
            return {"output": "Need at least two numbers."}
        return {"output": f"Sum = {sum(nums)}"}
    except Exception as e:
        return {"output": f"Error: {e}"}


def subtract_numbers(input_text: str):
    try:
        nums = [float(x) for x in input_text.replace(",", " ").split() if x.replace('.', '', 1).isdigit()]
        if len(nums) < 2:
            return {"output": "Need at least two numbers."}
        result = nums[0] - sum(nums[1:])
        return {"output": f"Difference = {result}"}
    except Exception as e:
        return {"output": f"Error: {e}"}


def multiply_numbers(input_text: str):
    try:
        nums = [float(x) for x in input_text.replace(",", " ").split() if x.replace('.', '', 1).isdigit()]
        if not nums:
            return {"output": "No numbers provided."}
        result = 1
        for n in nums:
            result *= n
        return {"output": f"Product = {result}"}
    except Exception as e:
        return {"output": f"Error: {e}"}


def divide_numbers(input_text: str):
    try:
        nums = [float(x) for x in input_text.replace(",", " ").split() if x.replace('.', '', 1).isdigit()]
        if len(nums) != 2:
            return {"output": "Provide two numbers (a b)."}
        if nums[1] == 0:
            return {"output": "Error: Division by zero"}
        return {"output": f"Quotient = {nums[0] / nums[1]}"}
    except Exception as e:
        return {"output": f"Error: {e}"}
