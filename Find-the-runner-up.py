if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(" ")))
    maxi=max(arr)
    ans = -100
    for i in arr:
        if ans < i and i != maxi:
            ans = i
    print(ans)
        
