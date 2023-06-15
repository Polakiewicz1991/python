print(", ".join(["a","b","c"]))
#a, b, c

print("Witaj świecie".replace("Witaj","Cześć"))
#Cześć świecie

print("To jest zdanie".startswith("To"))
#True

print("To jest zdanie".startswith("to"))
#False - rozpoczny na od "to"

print("To jest zdanie".endswith("nie"))
#True - kończy się na "nie"

print("j" in "To jest zdanie")
#True - czy "j" jest w zdaniu

print("To jest zdanie".upper())
#TO JEST ZDANIE

print("To jest zdanie".lower())
#to jest zdanie

print("-------------")


lista = [10, 20 ,32 ,24 ,92]

print("All")
if all([i % 2 == 0 for i in lista]):
    print("parzyste")
else:
    print("nieparzyte")

lista = [10, 20 ,35 ,25 ,99]
print("any")
if any([i % 2 == 0 for i in lista]):
    print("co najmniej 1 parzysta")
else:
    print("żadne nieparzyte")

for i in enumerate(lista):
    print(i)
    print(i[0] + 1, "-", i[1])