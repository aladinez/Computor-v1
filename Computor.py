import sys
import re

# get the polynomial second or lower degree equation
equation = sys.argv[1]
print(equation)

# parse the equation string "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
left_part, right_part = equation.split('=') # split the equation into left and right parts

print(left_part)
print(right_part)

def parse_part(part):
    terms = re.findall(r'([+-]?\s*\d*\.?\d*)\s*\*\s*X\^(\d+)', part)
    parsed_terms = [(float(coef.replace(' ', '')), int(power)) for coef, power in terms]
    return parsed_terms

left_terms = parse_part(left_part)
right_terms = parse_part(right_part)

print(left_terms)
print(right_terms)

# Combine the terms
def combine_terms(terms):
    combined_terms = {}
    for coef, power in terms:
        if power in combined_terms:
            combined_terms[power] += coef
        else:
            combined_terms[power] = coef
    return combined_terms

left_combined_terms = combine_terms(left_terms)
right_combined_terms = combine_terms(right_terms)

print(left_combined_terms)
print(right_combined_terms)

# move all the terms to the left side
for power, coef in right_combined_terms.items():
    if power in left_combined_terms:
        left_combined_terms[power] -= coef
    else:
        left_combined_terms[power] = -coef

print("===>" , left_combined_terms)

# print reduced form of the equation
reduced_form = ' '.join([f'{coef:+} * X^{power}' for power, coef in left_combined_terms.items() if coef != 0]).replace(' +', ' + ').replace(' -', ' - ').lstrip('+ ')
print("Reduced form: " + reduced_form + " = 0")

# get the degree of the equation
degree = max(left_combined_terms.keys())
print("Polynomial degree: " , degree)



