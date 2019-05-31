import turtle
import math

koch_size = 300
koch_step = int(turtle.numinput('Koch Snowflake', '몇단계 까지 그리겠습니까?')) # // 그릴 코흐의 눈송이 단계를 입력받음.

turtle.bgcolor('black')             # // 거북이 색깔 및 배경색깔 조절
turtle.color('sky blue', 'white')

def koch_line(length, step):                  # // 코흐 곡선을 그리는 재귀함수.
    if step > 0:
        length = length/3
        for angle in [60,-120,60,0]:
            koch_line(length,step-1)
            turtle.left(angle)
    else:
        turtle.forward(length)


turtle.tracer(3)
turtle.penup()
turtle.backward(koch_size/math.sqrt(3))
turtle.left(0)
turtle.pendown()
turtle.begin_fill()
for i in range(3):
    koch_line(koch_size,koch_step)
    turtle.left(-120)

turtle.end_fill()
turtle.update()
turtle.done()
