print(1 == 1)
print(1 != 1)
print(1 > 1)

a  = input('Podaj liczbe parzysta:' )

if (int(a) % 2) == 0:
    print('Prawda')
elif (int(a) % 2) == 1:
    print('Fałsz')
else:
    print('To ja już nie wiem')
print('Koniec')