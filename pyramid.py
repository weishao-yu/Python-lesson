def pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

    print()
pyramid(1)
# *
pyramid(2)
#  *
# ***
pyramid(4)
#    *
#   ***
#  *****
# *******

def inverted_pyramid(n):
    for i in range(n):
        print(' ' * i + '*' * ((n - i ) * 2 - 1))
inverted_pyramid(4)
# *******
#  *****
#   ***
#    *