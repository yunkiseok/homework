def gugudan_upto(n):
    for i in range(1, n+1):
        for p in range(1, 10):
            print("%d x %d = %d" % (i, p, i*p))

gugudan_upto(5)