# Cache Size
csize = int(input())

# Sequence of pages
pages = list(map(int,input().split()))

# Take a cache list
cache=[]

# Keep track of number of lement in cache
n=0
fault=0

# Hash to store current element in keys
dict={}

for page in pages:
    # If page exists in cache
    if page in dict:
        cache.remove(page)
        del dict[page]
        cache.append(page)
        dict[page]=True
    else:
        # Cache is full
        if(n==csize):
            out = cache.pop(0)
            del dict[out]
        else:
            n=n+1
        # Page not in cache => Page Fault
        fault += 1
        cache.append(page)
        dict[page]=True

print("Page Fault:",fault)
