def ambil_tengah(r, t=None):
    if t == None:
        e1 = len(r)
        e2 = (round(e1 / 2))
        return (r[e2])
    else:
        e1 = len(r)
        e2 = (round(e1 / 2))
        return (r[e2 + t - 1])


print(ambil_tengah("abcdefg", 1))
print(ambil_tengah("abcdefg", 2))
print(ambil_tengah("abcd"))