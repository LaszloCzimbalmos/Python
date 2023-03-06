import turtle
import pandas

# import data
data = pandas.read_csv("50_states.csv")

# basic settings
sc = turtle.Screen()
sc.title("US States Game")
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

# game basics
count = 0
all_states = data.state.to_list()
accepted = []

#scoreboard
score = turtle.Turtle()
score.ht()
score.up()
score.setposition(0, 250)
score.down()
score.write(arg=f"Score: {count}", align='center', font=('Times New Roman', 30, 'normal'))

loop = True
while loop:
    guess = sc.textinput("Guess a state!", "New state:").title()
    if guess == "exit".title():
        break

    if guess in all_states:
        count += 1
        accepted.append(guess)
        score.clear()
        score.write(arg=f"Score: {count}", align='center', font=('Times New Roman', 30, 'normal'))
        t = turtle.Turtle()
        t.ht()
        x = int(data[data["state"] == guess].x)
        y = int(data[data["state"] == guess].y)
        t.up()
        t.setposition(x, y)
        t.write(guess)

    if count == 50:
        loop = False

if count == 50:
    print("Congratulations, you guessed all the states!")

need_to_learn = [item for item in all_states if item not in accepted]


pandas.DataFrame(need_to_learn).to_csv(f"Need_to_learn({len(all_states)-count}).csv")


