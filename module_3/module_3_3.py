def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(False)
print_params(1, b='string')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [23, 'value', (1, 2, 3)]
values_dict = {'a': False, 'b': 2.0, 'c': 'first'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['string', 55]
print_params(*values_list_2, 42)
