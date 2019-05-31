
import turtle as t


def ngak(D,L):

    gak = float( (D -2) * 180 / D)

    print(gak)
    t.pendown()
    for i in range(D):
        t.forward(L)
        t.right(180 - gak)

ngak(7,100)
t.done()