#reversed Cat
def Cat(a):
    b = str(a)
    print("".join(reversed(b)))
    assert len(b) < 10,f"Obj len max 10"
#dicl Cat       
d = Cat(123456789)
print(dir(d))
