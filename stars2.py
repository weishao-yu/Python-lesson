def stars(n):
    for i in range(1,n+1):
        print('*'*i)
    for i in range(n-1, 0, -1):
        print('*'*i)


stars(1)
# *
stars(2)
# *
# **
# *
stars(3)
# *
# **
# ***
# **
# *
stars(4)
# *
# **
# ***
# ****
# ***
# **
# *