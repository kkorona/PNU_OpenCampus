import turtle as t




def tri(tri_len):
    if tri_len <= 40:  # 삼각형 크기 조절
        for i in range(0, 3):
            t.forward(tri_len)
            t.left(120)
        return

    new_len = tri_len / 2
    tri(new_len)
    t.forward(new_len)
    tri(new_len)
    t.backward(new_len)
    t.left(60)
    t.forward(new_len)
    t.right(60)
    tri(new_len)
    t.left(60)
    t.backward(new_len)
    t.right(60)

i = 3   # 삼각현 단계의 수
t.speed(0)
tri(40*2**i)
t.hideturtle()
t.done()