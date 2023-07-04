from collections import defaultdict

class Graph:

    def __init__(self):
        self.Graph = defaultdict(list)

    def addEdge(self,u,v):
        self.Graph[u].append(v)

    def DFS(self,root):
        #created visited
        visited = [False] * (max(self.Graph)+1)
        #created stack
        stack = []
        #add root to stack , mark it as visited
        stack.append(root)
        visited[root] = True

        #print root and pop it from the stack and append it's adjacents
        print(root,end=" ")
        stack.pop()
        for i in self.Graph[root]:
            stack.append(i)
            visited[i] = True
            
        while len(stack):
            # make the top element as root and add it adjacents to the stack only if they are not visted before, mark them as visited
            # print the root and remove the top element
            root = stack[-1]
            for i in self.Graph[root]:
                if visited[i] == False:
                    stack.append(i)
                    visited[root] = True
            print(root,end=" ")
            stack.pop()

if __name__ == "__main__":
    # g = Graph()
    # vertices,edges = input().split()
    # for i in range(int(edges)):
    #     u,v = input().split()
    #     g.addEdge(int(u),int(v))
    # g.BFS(int(input("Enter the starting vertex : ")))
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.DFS(2)







        

    