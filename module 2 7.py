def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(5)
print_params(3, 'слово', False)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [5, 4.5, 'string']
values_dict = {'a': 6, 'b': 7.45, 'c': 'строка'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7.62, 'Калибр']
print_params(*values_list_2, 47)