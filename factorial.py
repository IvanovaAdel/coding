def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n
my_file = open("fact", "w+")
my_file.write(str(fac(11)))
my_file.close()
my_file = open("fact", 'r')
my_file.close
print(my_file.read())
    
