class Network:
    def __init__(self,n):
        self.matrix=[]
        self.n=n
        
    def addlink(self, u, v, w):  
        self.matrix.append((u, v, w))
        
    def printtable(self, dist,src,fromn):
        print("Each Destination router and distance from router {}:".format(chr(ord('A')+src)))  
        for i in range(self.n):  
            print("{0}\t{1}".format(chr(ord('A')+i), dist[i]))
            print("Next hop address is:{}".format(chr(ord('A')+fromn[i][i])))
            
    def algor(self, src,fromn):  
   
      
        dist = [99] * self.n 
        dist[src] = 0
        
        for _ in range(self.n - 1):   
            for u, v, w in self.matrix:  
                if dist[u] != 99 and dist[u] + w < dist[v]:  
                        dist[v] = dist[u] + w
                        fromn[u][v] = v
  
        self.printtable(dist,src,fromn)

def main():
    matrix=[]
    print("Enter No. of Nodes : ")
    n=int(input())
    fromn = [[0 for i in range(10)] for j in range(10)]
    print("Enter the Distance Matrix :")
    for i in range(n):
        m=list(map(int,input().split(" ")))
        matrix.append(m)
    g=Network(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]!=99:
                g.addlink(i,j,matrix[i][j])
                fromn[i][j] = j
    for _ in range(n):
        g.algor(_,fromn)
main()