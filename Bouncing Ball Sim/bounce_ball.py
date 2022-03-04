import turtle
import random

window = turtle.Screen()
window.bgcolor("black")
window.title("Bouncing Ball Simulator")
window.tracer(5)

balls = []
for _ in range(25):
    balls.append(turtle.Turtle())


colors = ["red", "blue", "green", "orange", "yellow", "white" "purple", "pink"]
shapes = ["circle", "triangle", "square"]


for ball in balls:

    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.uniform(-x, x)
    ball.da = random.randint(-5, 5)

gravity = 0.1

while True:
    window.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)


        #check for a wall collision
        if ball.xcor() > 330:
            ball.dx *= -1
            ball.da *= -1

        if ball.xcor() < -330:
            
            ball.dx *= -1
            ball.da *= -1
            
            
        #check for bounce

        if ball.ycor() < -310:
            ball.sety(-330)
            ball.dy *= -1
            ball.da *= -1

    #check for collisions
    for i in range(0, len(balls)):
        for j in range(i + 1, len(balls)):

            #check for collisions
            if balls[i].distance(balls[j]) < 20:
                temp_dx = balls[i].dx
                temp_dy = balls[i].dy

                balls[i].dx = balls[j].dx
                balls[i].dy = balls[j].dy

                balls[j].dx = temp_dx
                balls[j].dy = temp_dy












window.mainloop()
