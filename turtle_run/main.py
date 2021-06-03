from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)

turtles = []
for i in colors:
    tim = Turtle(shape="turtle")
    tim.color(i)
    turtles.append(tim)
j = 0
for i in range(6):
    turtles[i].penup()
    turtles[i].goto(x=-250, y=-130 + j)
    j += 50


user_bet = screen.textinput(title="Make a bet",prompt="which turtle will win the race? Enter a color: ")


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

screen.exitonclick()
