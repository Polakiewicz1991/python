from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[list]]) -> bool:
        n = len(graph)
        colors = [0] * n  # Tablica przechowująca przypisane kolory wierzchołków (-1, 0, 1)

        for i in range(n):
            print("colors[i]",colors[i])
            if colors[i] == 0:  # Jeśli wierzchołek nie został jeszcze pokolorowany
                queue = deque([i])
                print("queue", list(queue))
                colors[i] = 1  # Przypisanie koloru 1 dla wierzchołka
                print("colors:", colors)
                while queue:
                    node = queue.popleft()
                    print("node",node)
                    print("graph[node]",graph[node])

                    for neighbor in graph[node]:
                        print("neighbor",neighbor)
                        if colors[neighbor] == colors[node]:
                            return False  # Konflikt kolorów - graf nie jest dwudzielny
                        elif colors[neighbor] == 0:
                            queue.append(neighbor)
                            colors[neighbor] = -colors[node]  # Przypisanie przeciwnego koloru

        return True  # Wszystkie wierzchołki zostały pokolorowane bez konfliktów, graf jest dwudzielny


Wynik = Solution()

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Wynik1 = Wynik.isBipartite(graph)
print("Wynik1: ",Wynik1)
print("\n")

graph = [[1,3],[0,2],[1,3],[0,2]]
Wynik2 = Wynik.isBipartite(graph)
print("Wynik2: ",Wynik2)

#nie rozumiem tego zadania
#wygenerowane przez AI