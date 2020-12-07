import sys 
   
class Network: 
    def __init__(self, nodes,graph): 
        self.V = nodes 
        self.graph = graph
   
    def printTable(self, dist,src,path): 
        print("Shortest Path Table of {}".format(chr(ord('A')+src)))  
        for node in range(self.V): 
            print("{0}\t{1}\t{2}".format(chr(ord('A')+node), dist[node],path[node]))  
            
    def minDistance(self, dist, spathSet): 
        min = sys.maxsize 
        for v in range(self.V): 
            if dist[v] < min and spathSet[v] == False: 
                min = dist[v] 
                min_index = v 
   
        return min_index 

    def dijkstra(self, src): 
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        spathSet = [False] * self.V 
        path={}
        for _ in range(self.V):
            path[_]=[]
        for current in range(self.V): 
            u = self.minDistance(dist, spathSet) 
            spathSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and spathSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 
                    if u == src:
                        path[v].append(chr(ord('A')+v))
                    else:
                        path[v].append(chr(ord('A')+u))
                        if chr(ord('A')+v) not in path[v]:
                            path[v].append(chr(ord('A')+v))
   
        self.printTable(dist,src,path)

def main():
    matrix=[]
    print("Enter No. of Nodes : ")
    n=int(input())
    print("Enter the Link State Matrix :")
    for i in range(n):
        m=list(map(int,input().split(" ")))
        matrix.append(m)
    g = Network(5,matrix) 
    for _ in range(g.V):
        g.dijkstra(_)

main()