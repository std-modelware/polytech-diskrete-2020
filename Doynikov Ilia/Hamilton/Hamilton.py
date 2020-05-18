n = 8                    # sample of graph, (oriented) to test algorhymm
Visited = [False] * n
Path = []
A =  [[0,1,1,1,1,1,1,1], # 1
	  [0,0,1,0,1,0,1,1], # 2
	  [0,0,0,1,1,0,0,0], # 3
	  [0,0,1,0,1,1,0,0], # 4
	  [1,0,0,0,0,1,0,1], # 5
	  [1,1,1,0,1,0,1,1], # 6
	  [1,1,0,0,1,1,0,0], # 7
	  [1,0,0,0,1,1,1,0]] # 8
def hamilton(curr): #checking hamilton cycle from curr 
    Path.append(curr)
    if len(Path) == n:
        if A[Path[0]][Path[-1]] == 1:
            print(Path) # Print path
            return True 
        else: 
            Path.pop() #not correct
            return False 
    Visited[curr] = True
    for next in range(n): 
        if A[curr][next] == 1 and not Visited[next]: 
            if hamilton(next): #recursive call
                return True 
    Visited[curr] = False #no one call was success
    Path.pop()
    return False
    
# Main
for i in range(n): 
    if hamilton(i):
        print(i+1, 'Yes')
    else:
        print(i+1, 'No')