from turtle import Screen, shape, Turtle
import pandas as pd

screen = Screen()
tim = Turtle()
screen.title("U.S States Game")
tim.hideturtle()
tim.penup()

image = "blank_states_img.gif"
screen.addshape(image)
shape(image)

# Read csv file
df = pd.read_csv("50_states.csv")

# Q&A
all_good = True
my_score = 0

while all_good:
    if my_score == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?")
    if my_score != 0:
        answer_state = screen.textinput(title=f"{my_score}/50 States Correct", prompt="What's another State's name?")

    if answer_state in df["state"].values:
        position = df[df.state == answer_state].reset_index()
        indic = df[df.state == answer_state].index
        df = df.drop(df.index[indic])
        tim.setposition(position["x"][0], position["y"][0])
        tim.write(answer_state, True, font=('terminal', 12))
        my_score += 1
    elif answer_state == "exit":
        all_good = False
        print(df)
        not_guessed_states = df.to_csv("not_guessed_states.csv")
    else:
        all_good = False







screen.exitonclick()
