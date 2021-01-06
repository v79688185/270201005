def sleep(n):
    import time
    if n == 0:
        print("ALEEEEERT")
    else:
        print(n)
        time.sleep(1)
        return sleep(n-1)

sleep(5)