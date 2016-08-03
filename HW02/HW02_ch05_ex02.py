#!/usr/bin/env python
# HW02_ch05_ex02

# Fermat's Last Theorem says that there are no positive integers a, b, and c
# such that
#        a^n + b^n = c^n
# for any values of n greater than 2.

# (1) Write a function named check_fermat that takes four parameters-a, b, c and
# n-and that checks to see if Fermat's theorem holds. If n is greater than 2
# and it turns out to be true that
#        a^n + b^n = c^n
# the program should print, "Holy smokes, Fermat was wrong!""
# Otherwise the program should print, "No, that doesn't work."

# (2) Write a function named check_fermat_ints that prompts the user to input
# values for a, b, c and n, converts them to integers, and uses check_fermat
# to check whether they violate Fermat's theorem.

################################################################################
# Write your functions below:
# Body


def check_fermat(a,b,c,n):
    x = a ** n + b ** n    # Equation to calculate a^2 + b^2
    y = c ** n             # Equation to calculate c^2
    #print(x)
    #print(y)
    if ( (x == y) and n > 2):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def check_fermat_ints():
     a = int(input("Please enter the value for a = "))
     b = int(input("Please enter the value for b = "))
     c = int(input("Please enter the value for c = "))
     n = int(input("Please enter the value for n = "))
     check_fermat(a,b,c,n)


# Write your functions above:
################################################################################
def main():
    """Call your function within this function.
    When complete have one function call in this function:
    check_fermat_ints()
    and two functions defined in the body:
    check_fermat_ints()
    check_fermat()
    """
    check_fermat_ints()
    #check_fermat(12,5,13,2)
    #print("Hello World!")



if __name__ == "__main__":
    main()
