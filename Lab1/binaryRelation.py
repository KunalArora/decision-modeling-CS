import itertools
import pandas as pd
import numpy as np
from collections import defaultdict


class TopologicalSort:
    def __init__(self):
        self.graph = defaultdict(set)  # dictionary containing adjacency List

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def dfs(self, graph, start, end):
        st = [(start, [])]
        while st:
            state, path = st.pop()
            if path and state == end:
                return path
            for next_state in graph[state]:
                if next_state in path:
                    continue
                st.append((next_state, path + [next_state]))
        return []

    def get_cycle(self, graph):
        for node in graph:
            cycle = self.dfs(graph, node, node)
            if cycle:
                return [node] + cycle
        return []

    def remove_cycle(self, graph, cycle):
        new_graph = defaultdict(set)
        new_node = set()

        for entry in cycle:
            if type(entry) is tuple:
                for entry1 in entry:
                    new_node.add(entry1)
            else:
                new_node.add(entry)
        new_node = tuple(new_node)

        for node, neighbours in graph.items():
            if node in cycle:
                new_graph[new_node] = new_graph[new_node].union(graph[node])
            else:
                if cycle.intersection(graph[node]) == set():
                    new_graph[node] = graph[node]
                else:
                    new_graph[node] = graph[node].difference(cycle).union({new_node})
        new_graph[new_node] = new_graph[new_node].difference(cycle)
        return new_graph

    def remove_cycles(self, graph):
        # removing self-loops
        for node, value in graph.items():
            if node in value:
                graph[node].remove(node)

        while True:
            cycle = self.get_cycle(graph)
            if cycle:
                graph = self.remove_cycle(graph, set(cycle))
            else:
                break
        return graph

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(len(stack), v)

    def topologicalSort(self):
        visited = {}
        for k in self.graph.keys():
            visited[k] = False
        stack = []

        for i in self.graph.keys():
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        print(list(itertools.chain(*(i if isinstance(i, tuple) else (i,) for i in stack))))

    def print_graph(self, graph):
        for k, v in graph.items():
            print(k, v)
        print("\n")


class BinaryRelation:
    def __init__(self):
        pass

    def DfToSet(self, df):
        XY = set()
        for rowIndex in range(len(df)):
            XY.add(rowIndex)
        return XY

    def DfToRelation(self, df):
        RY = set()
        for row in range(0, 6):
            for col in range(0, 6):
                if (df[row][col]):
                    RY.add((col, row))
        return RY

    def CompleteCheck(self, X, R):
        for x in X:
            for y in X:
                if (x, y) not in R and (y, x) not in R:
                    return False
        return True

    def ReflexiveCheck(self, X, R):
        for x in X:
            if (x, x) not in R:
                return False
        return True

    def AsymmetricCheck(self, X, R):
        for x, y in R:
            if (y, x) in R:
                return False
        return True

    def AntisymmetricCheck(self, X, R):
        for x, y in R:
            if (y, x) in R:
                if not x == y:
                    return False
        return True

    def TransitiveCheck(self, X, R):
        for x, y1 in R:
            for y2, z in R:
                if y1 == y2:
                    if (x, z) not in R:
                        return False
        return True

    def NegativeTransitiveCheck(self, X, R):
        for x in X:
            for y in X:
                for z in X:
                    if (x, y) not in R and (y, z) not in R:
                        if (x, z) in R:
                            return False
        return True

    def SymmetricCheck(self, X, R):
        for x, y in R:
            if (y, x) not in R:
                return False
        return True

    def CompleteOrderCheck(self, X, R):
        return self.CompleteCheck(X, R) and self.AntisymmetricCheck(X, R) and self.TransitiveCheck(X, R)

    def CompletePreOrderCheck(self, X, R):
        return self.CompleteCheck(X, R) and self.TransitiveCheck(X, R)

    def StrictRelation(self, X, R):
        df_strict = pd.DataFrame(0, index=np.arange(0, 6), columns=np.arange(6))
        for (x, y) in R:
            if (y, x) not in R:
                df_strict[x][y] = 1
        return df_strict

    def StrictRelationCheck(self, X, R):
        df_strict = self.StrictRelation(X, R)
        XStrict = self.DfToSet(df_strict)
        RStrict = self.DfToRelation(df_strict)
        return self.AsymmetricCheck(XStrict, RStrict)

    def IndifferenceRelation(self, X, R):
        df_indi = pd.DataFrame(0, index=np.arange(0, 6), columns=np.arange(6))
        for (x, y) in R:
            if (y, x) in R:
                df_indi[x][y] = 1
        return df_indi

    def IndifferenceRelationCheck(self, X, R):
        df_indi = self.IndifferenceRelation(X, R)
        XIndi = self.DfToSet(df_indi)
        RIndi = self.DfToRelation(df_indi)
        return self.SymmetricCheck(XIndi, RIndi)

    def TopologicalSortCheck(self, X, R):
        g = TopologicalSort()
        for (x, y) in R:
            g.addEdge(x, y)

        # Remove cycles from graph
        # Convert the Directed Cyclic Graph to Directed Acyclic Graph
        g.graph = g.remove_cycles(g.graph)

        # Topological sort of Directed Acyclic Graph
        g.topologicalSort()


if __name__ == '__main__':
    df = pd.read_csv('datas.csv', error_bad_lines=False, header=None)
    binaryR = BinaryRelation()
    X = binaryR.DfToSet(df)
    R = binaryR.DfToRelation(df)

    print("ReflexiveCheck Result: " + str(binaryR.ReflexiveCheck(X, R)) + "\n")
    print("CompleteCheck Result: " + str(binaryR.CompleteCheck(X, R)) + "\n")
    print("AsymmetricCheck Result: " + str(binaryR.AsymmetricCheck(X, R)) + "\n")
    print("AntisymmetricCheck Result: " + str(binaryR.AntisymmetricCheck(X, R)) + "\n")
    print("TransitiveCheck Result: " + str(binaryR.TransitiveCheck(X, R)) + "\n")
    print("NegativeTransitiveCheck Result: " + str(binaryR.NegativeTransitiveCheck(X, R)) + "\n")
    print("SymmetricCheck Result: " + str(binaryR.SymmetricCheck(X, R)) + "\n")
    print("CompleteOrderCheck Result: " + str(binaryR.CompleteOrderCheck(X, R)) + "\n")
    print("CompletePreOrderCheck Result: " + str(binaryR.CompletePreOrderCheck(X, R)) + "\n")
    print("StrictRelation Result: " + str(binaryR.StrictRelationCheck(X, R)))
    print(binaryR.StrictRelation(X, R))
    print("\nIndifferenceRelationCheck Result: " + str(binaryR.IndifferenceRelationCheck(X, R)))
    print(binaryR.IndifferenceRelation(X, R))
    print("\nTopologicalSortCheck Result: ")
    binaryR.TopologicalSortCheck(X, R)



