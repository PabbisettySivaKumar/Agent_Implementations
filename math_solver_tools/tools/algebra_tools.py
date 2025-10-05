import re
import math
from ollama_utils import query_ollama

def solve_algebra(equation: str):
    try:
        equation= equation.replace(' ', '')
        if '=' not in equation:
            return "Error: Equaiton Must Contain '='"
        lhs, rhs= equation.split('=')
        rhs_val= eval(rhs)

        #quadratic equation
        pattern= r"([+-]?\d*\.?\d*)x\^2([+-]\d*\.?\d*)x([+-]\d+\.?\d*)"
        match = re.match(pattern, lhs)

        if match:
            a, b, c= match.groups()
            a= float(a) if a not in ["", "+", "-"] else float(a+"1")
            b= float(b)
            c= float(c)-rhs_val
            d= b**2-4*a*c

            if d<0:
                return {"output":"No Real Roots"}
            r1= (-b+math.sqrt(d))/(2*a)
            r2= (-b-math.sqrt(d))/(2*a)
            return {"output":f"Quadratic Roots: {r1}, {r2}"}

        prompt= f"solve this algebraic equation step-by-step: {equation}. Give Extract roots if possible."
        response= query_ollama(prompt)
        return {"output": response}
    except Exception as e:
        return {"output":f"Error solving equation: {e}"}