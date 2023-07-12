from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dictEquation: dict = {}
        resultList = []

        i = 0
        print("len(equations) :",len(equations) )
        while i < len(equations):
            # print(f"equations[{i}][0]",equations[i][0], f"equations[[{i}][1]]", equations[i][1])
            dictEquation[equations[i][0]] = {}#{equations[i][1] : values[i]}
            dictEquation[equations[i][1]] = {}#{equations[i][0]: 1/values[i]}
            i += 1
        i = 0
        while i < len(equations):
            # print(f"equations[{i}][0]", equations[i][0], f"equations[[{i}][1]]", equations[i][1])
            #dictEquation["a"]["a"]
            dictEquation[equations[i][0]][equations[i][0]] = 1
            # dictEquation["a"]["c"]
            dictEquation[equations[i][0]][equations[i][1]] = values[i]
            # dictEquation["b"]["a"]
            dictEquation[equations[i][1]][equations[i][0]] = 1/values[i]
            # dictEquation["b"]["b"]
            dictEquation[equations[i][1]][equations[i][1]] = 1
            i += 1

        print("dictEquation: ",dictEquation)
        dictEquationKeys = dictEquation.keys()

        print("dictEquationKeys:",dictEquationKeys)

        #dictEquation: {'a': {'a': 1, 'b': 2.0}, 'b': {'a': 0.5, 'b': 1, 'c': 3.0},'c': {'b': 0.3333333333333333, 'c': 1}}
        #dictEquation["a"]["c"] = dictEquation["a"]["b"] * dictEquation["b"]["c"]

        for key in dictEquationKeys:
            dictKeyKeys = dictEquation[key].keys()
            missingKeys: list = dictEquationKeys - dictKeyKeys
            print("\nmissingKeys", missingKeys)

            for subKey in dictEquationKeys:
                dictKeyKeys = dictEquation[subKey].keys()
                dictKeyKeys2 = dictEquation[key].keys()
                for misKey in missingKeys:
                    if misKey in dictKeyKeys and subKey in dictKeyKeys2 and misKey != subKey:
                        print("misKey: ", misKey,type(misKey))
                        print("key: ", key, type(key))
                        print("subKey: ", key, type(subKey))
                        # print(dictEquation[key][subKey])
                        # print(dictEquation[subKey][misKey])
                        # print(f"dictKeyKeys[{key}][{misKey}]")

                        dictEquation[key][misKey] = dictEquation[key][subKey] * dictEquation[subKey][misKey]
                        break
            print("dictEquation: ", dictEquation)


        for querie in queries:
            finded = False
            for key in dictEquationKeys:
                dictKeyKeys = dictEquation[key].keys()
                print("key:", key, " querie[0]:", querie[0], " querie[1]:", querie[1])
                if querie[0] in dictKeyKeys and querie[1] in dictKeyKeys and not(finded):
                    print("dictEquation[key][querie[0]]:", dictEquation[key][querie[0]], " dictEquation[key][querie[1]]:", dictEquation[key][querie[1]])
                    resultList.append(dictEquation[key][querie[1]]/dictEquation[key][querie[0]])
                    finded = True
            if finded == False:
                resultList.append(-1.0)


        print("dictEquation:",dictEquation)
        return  resultList
Wynik = Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print("equations: ", equations, " values: ", values, " queries: ", queries)
Wynik1 = Wynik.calcEquation(equations= equations, values= values, queries= queries)
print("wynik1: ",Wynik1, "\n***************\n") #[6.0, 0.5, -1.0, 1.0, -1.0 ]

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
print("equations: ", equations, " values: ", values, " queries: ", queries)
Wynik2 = Wynik.calcEquation(equations= equations, values= values, queries= queries)
print("wynik2: ",Wynik2, "\n***************\n")

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
print("equations: ", equations, " values: ", values, " queries: ", queries)
Wynik3 = Wynik.calcEquation(equations= equations, values= values, queries= queries)
print("Wynik3: ",Wynik3, "\n***************\n")

equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
print("equations: ", equations, " values: ", values, " queries: ", queries)
Wynik3 = Wynik.calcEquation(equations= equations, values= values, queries= queries)
print("Wynik3: ",Wynik3, "\n***************\n")