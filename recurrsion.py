def show(n):
    print(n)
    if n > 0:
        show(n-1)

#!/usr/bin/env python3
show(5) #5, 4, 3, 2, 1, 0