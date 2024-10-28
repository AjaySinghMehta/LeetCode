class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0]*(2*n-1)
        i = 0
        visited = [False]*(n+1)
        print(arr)
        print(visited)
        def solve(i,arr,visited):
            if i>=2*n-1:
                return True
            for x in range(n,0,-1):
                if(x>1 and (arr[i]!=0 or i+x>=2*n-1 or arr[i+x]!=0)):
                    continue
                if(x==1 and arr[i]!=0):
                    continue
                if(visited[x]):
                    continue
                if x>1:
                    arr[i]=x
                    arr[i+x]=x
                else:
                    arr[i]=x
                                            
                visited[x]=True
                nexti = i+1
                while(nexti<2*n-1 and arr[nexti]!=0):
                    nexti += 1
                if(solve(nexti,arr, visited)):
                    return True
                solve(i,arr,visited)
                if(x>1):
                    arr[i]=0
                    arr[i+x]=0
                else:
                    arr[i]=0
                visited[x]=False
            return False
        solve(0,arr,visited)                  
        return arr
