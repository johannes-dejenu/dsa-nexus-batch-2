if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split( ))
lst = set()
for i in arr:
    lst.add(i)
lst.remove(max(lst))
print(max(lst))
    
    
