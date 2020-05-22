V=5
parent =[0]*V

def Find(i):
    while(parent[i]!=i):
        i=parent[i]
    return i

def Union(i,j):
    a=Find(i)
    b=Find(j)
    parent[a]=b

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]),' ', end="")
        print()

def Kruskal_Alg(matr):
     mincost=0
     for i in range(V):
        parent[i]=i

     edge_count=0
     while(edge_count<V-1):
         min=1000
         a = -1
         b = -1
         for i in range(V):
             for j in range(V):
                 if (Find(i) !=Find(j)) and (matr[i][j]<min):
                     min=matr[i][j]
                     a=i
                     b=j

         Union(a,b)
         edge_count=edge_count+1
         print("Ребро %d:(%d,%d) вес:%d"%(edge_count,a,b,min))
         mincost+=min
     print("Минимальный вес= %d"%(mincost))

matrix=[
     [1000,2,1000,6,1000], [ 2,1000,3,8,5],	[ 1000,3 ,1000, 1000,7],[ 6,8,1000,1000,9],[ 1000,5,7,9,1000 ],
  ]
print('Вводимая матрица весов')
printMatrix(matrix)
print(" ")
Kruskal_Alg(matrix)
