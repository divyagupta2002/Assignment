for _ in range(int(input())):
    n, h, m = map(int, input().split())
    t = h*60 + m
    mt = 1440
    for i in range(n):
        th, tm = map(int, input().split())
        tt = (th*60 + tm - t) % 1440
        if tt <= mt:
            mh = tt//60
            mm = tt % 60
            mt = tt
    print(mh, mm)
