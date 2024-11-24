import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()

states = pandas.read_csv('50_states.csv')
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title="Guess the State" if len(guessed_states) == 0 else f"{len(guessed_states)}/{50} States Correct",
        prompt="What's another state's name?").title()
    # If answer_state is one of the states in all the states of the 50_states.csv
    state_data = states[states.state == answer_state]
    if answer_state == 'Exit':
        # Add the states in a csv file called states_to_learn.csv which couldn't be answered
        all_states = states.state.to_list()
        states_to_learn = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv('states_to_learn.csv')
        break
    # If they got it right
    if not state_data.empty:
        guessed_states.append(answer_state)
        # Create a turtle to write the name of the state at the state's x and y coordinates.
        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        state.write(answer_state)
        # or state.write(state_data.state.item())
