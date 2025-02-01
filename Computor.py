import sys
import re

if len(sys.argv) < 2:
    print("Error: No equation provided. Please provide a polynomial equation as a command-line argument.")
    sys.exit(1)
# get the polynomial second or lower degree equation
equation = sys.argv[1]
# print(equation)

# Parse the equation string
try:
    left_part, right_part = equation.split('=')
except ValueError:
    print("Error: Invalid equation format.")
    sys.exit(1)

# print(left_part)
# print(right_part)

def parse_part(part):
    try:
        terms = re.findall(r'([+-]?\s*\d*\.?\d*)\s*\*\s*X\^(\d+)', part)
        parsed_terms = [(float(coef.replace(' ', '')), int(power)) for coef, power in terms]
        return parsed_terms
    except Exception as e:
        print(f"Error parsing part '{part}': {e}")
        sys.exit(1)

left_terms = parse_part(left_part)
right_terms = parse_part(right_part)

# print(left_terms)
# print(right_terms)

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

# print(left_combined_terms)
# print(right_combined_terms)

# move all the terms to the left side
for power, coef in right_combined_terms.items():
    #substraction of the right terms from the left terms if pow is the same.
    if power in left_combined_terms:
        left_combined_terms[power] -= coef
    #addition of the right terms to the left terms
    else:
        left_combined_terms[power] = -coef

# print("===>" , left_combined_terms)

# print reduced form of the equation
reduced_form = ' '.join([f'{coef:+} * X^{power}' for power, coef in left_combined_terms.items() if coef != 0]).replace(' +', ' + ').replace(' -', ' - ').lstrip('+ ')
print("Reduced form: " + reduced_form + " = 0")

# get the degree of the equation
degree = max(left_combined_terms.keys())
print("Polynomial degree: " , degree)


# calculate the discriminant

def calculate_discriminant(a, b, c):
    return b ** 2 - 4 * a * c

if degree == 2:
    a = left_combined_terms[2]
    b = left_combined_terms.get(1, 0)
    c = left_combined_terms.get(0, 0)
    discriminant = calculate_discriminant(a, b, c)
    # print("Discriminant: " , discriminant)

    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print("Discriminant is strictly positive, the two solutions are:")
        print(x1)
        print(x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        print("Discriminant is zero, the solution is:")
        print(x)
    else:
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * a)
        print("Discriminant is strictly negative, the two solutions are:")
        print(f'{real_part} + i * {imaginary_part}')
        print(f'{real_part} - i * {imaginary_part}')

elif degree == 1:
    a = left_combined_terms[1]
    b = left_combined_terms.get(0, 0)
    x = -b / a
    print("The solution is:")
    print(x)

elif degree == 0:
    if left_combined_terms[0] == 0:
        print("The solution is:")
        print("All real numbers")
    else:
        print("No solution")
else:
    print("The polynomial degree is stricly greater than 2, I can't solve.")

