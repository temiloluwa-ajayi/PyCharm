for i in range(1, 11):
    sym = '*' * i
    print('{:>10} {:<10} {:^10}'.format(sym, sym, sym))


for i in range(1, 11):
    sym = '*' * i
    print(f'{sym:>10}', f'{sym:<10}', f'{sym:^10}')