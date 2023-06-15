class Rozwiazanie:
    def __init__(self,nums,k):
        self.nums = nums
        self.k = k
    def removeDuplicates(self):
        lista = []
        for i in range(len(self.nums)):
            if i == 0:
                lista.append(self.nums[i])
            elif self.nums[i - 1] != self.nums[i]:
                lista.append(self.nums[i + 1])

        self.k = len(lista)
        lista += [None]*(len(self.nums)-len(lista))
        self.nums = lista


lista = [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4,5,5,5,5,5,5,5]
k = 0
Duplicates = Rozwiazanie(lista,k)
k = Duplicates.removeDuplicates()
print("lista: ",Duplicates.nums)
print("k: ",Duplicates.k)