def position(s):
    for index, ch in enumerate(s):
        if ch.isupper():
            print((ch, index))
            return (ch, index)
    print(-1)
    return -1

position("Abcdef")