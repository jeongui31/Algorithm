N, B = map(int, input().split())

def base_change(n,q):
    rev_base = ''
    
    while n>0:
        n, mod = divmod(n, q)
        if mod >= 10:
            rev_base += chr(mod - 10 + ord('A'))
        else:
            rev_base += str(mod)
        
    return rev_base[::-1]

print(base_change(N, B))