#Solution taken from
#https://stackoverflow.com/questions/34638040/plot-arbitrary-2-d-function-in-python-pyplot-like-matlabs-ezplot
from sympy.plotting import plot_implicit
from sympy.parsing.sympy_parser import parse_expr

def ezplot(s):
    #Parse doesn't parse = sign so split
    lhs, rhs = s.replace("^","**").split("=")
    eqn_lhs = parse_expr(lhs)
    eqn_rhs = parse_expr(rhs)
    plot_implicit(eqn_lhs)

# take user input
choice = int(input('Enter choice(1-4):'))

if choice == 1:
    ezplot('Abs(x)^1 + Abs(y)^2 - 1 = 0')
elif choice == 2:
    ezplot('Abs(x)^0.5 + Abs(y)^5 - 1 = 0')
elif choice == 3:
    ezplot('Abs(x)^1.5 + Abs(y)^1.5 - 1 = 0')
elif choice == 4:
    ezplot('Abs(x)^0.5 + Abs(y)^2 - 1 = 0')

