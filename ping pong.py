from tkinter import *
import turtle

def winner(player):

    display = Tk()

    Label(display, text = player + ' WINS!!!', bg='white', fg='red', font='Broadway 40 bold').pack()

    display.mainloop()

def data_entry():

    main_window.destroy()

    def play_game():

        player1 = e1.get()
        player2 = e2.get()

        entry_window.destroy()

        WIDTH = 800
        HEIGHT = 600

        BAR_WIDTH = 5
        BAR_HEIGHT = 1

        SCREEN = turtle.Screen()
        SCREEN.title('PING PONG')
        SCREEN.bgcolor('black')
        SCREEN.setup(WIDTH, HEIGHT)
        SCREEN.tracer(0)
        
        P1 = turtle.Turtle()
        P1.shape('square')
        P1.shapesize(BAR_WIDTH, BAR_HEIGHT)
        P1.color('white')
        P1.up()
        P1.goto(-350,0)

        P2 = turtle.Turtle()
        P2.shape('square')
        P2.shapesize(BAR_WIDTH, BAR_HEIGHT)
        P2.color('white')
        P2.up()
        P2.goto(350,0)

        BALL = turtle.Turtle()
        BALL.speed(0)
        BALL.shape('circle')
        BALL.color('white')
        BALL.up()
        BALL.goto(0,0)
        BALL.dx = 0.2
        BALL.dy = 0.2

        def P1_up():
            y = P1.ycor()
            if y < 250:
                y += 10
            else:
                y = 250
            P1.sety(y)

        def P1_down():
            y = P1.ycor()
            if y > -240:
                y -= 10
            else:
                y = -240
            P1.sety(y)

        def P2_up():
            y = P2.ycor()
            if y < 250:
                y += 10
            else:
                y = 250
            P2.sety(y)

        def P2_down():
            y = P2.ycor()
            if y > -240:
                y -= 10
            else:
                y = -240
            P2.sety(y)

        game_over = False

        while not game_over:
            SCREEN.listen()
            SCREEN.onkeypress(P1_up,'w')
            SCREEN.onkeypress(P2_up,'Up')
            SCREEN.onkeypress(P1_down,'s')
            SCREEN.onkeypress(P2_down,'Down')
            SCREEN.update()
            BALL.setx(BALL.xcor() + BALL.dx)
            BALL.sety(BALL.ycor() + BALL.dy)
            if(BALL.ycor() > 290):
                BALL.sety(290)
                BALL.dy *= -1
            elif(BALL.ycor() < -290):
                BALL.sety(-290)
                BALL.dy *= -1
            if(BALL.xcor() > 390):
                SCREEN.bye()
                winner(player1)
                game_over = True
            elif(BALL.xcor() < -390):
                SCREEN.bye()
                winner(player2)
                game_over = True
            if((BALL.xcor() > 340 and BALL.xcor() < 341) and (BALL.ycor() < P2.ycor()+50 and BALL.ycor() > P2.ycor()-50)):
                BALL.setx(340)
                BALL.dx *= -1
            if((BALL.xcor() < -340 and BALL.xcor() > -341) and (BALL.ycor() < P1.ycor()+50 and BALL.ycor() > P1.ycor()-50)):
                BALL.setx(-340)
                BALL.dx *= -1
    
    entry_window = Tk()

    Label(entry_window, text = 'PLEASE ENTER YOUR NAMES TO START THE GAME!!!').grid(columnspan=2)
    Label(entry_window, text = "PLAYER 1").grid(row=2)
    Label(entry_window, text = "PLAYER 2").grid(row=3)

    e1 = Entry(entry_window)
    e2 = Entry(entry_window)

    e1.grid(row=2, column=1)
    e2.grid(row=3, column=1)

    Button(entry_window, text = 'PLAY', command = play_game).grid(row=5, column=0)
    Button(entry_window, text = 'QUIT', command = leave_window).grid(row=5, column=1)

    entry_window.mainloop()

def leave_window():
    entry_window.destroy()

def leave_game():
    main_window.destroy()

main_window = Tk()

frame = Frame(main_window)
frame.pack()

Button(frame, text = 'PLAY GAME', fg = 'black', command = data_entry).pack()
Button(frame, text = 'QUIT', fg = 'black', command = leave_game).pack()

main_window.mainloop()

