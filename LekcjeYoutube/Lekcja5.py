i = 0

while i < 5:
    print(i)
    i += 1
print('koniec')

i = 0
while True:
    i += 1
    if i % 2 == 1:
        continue #powrót do począdku pętli
    print(i)
    if i > 10:
        break
print('koniec')