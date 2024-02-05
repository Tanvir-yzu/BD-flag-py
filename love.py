import turtle
import math
import pygame

obj = turtle.Turtle()

def love_curve(t):
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, y

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('Amar_Sonar_Bangla.mp3')  # Replace 'your_song.mp3' with the path to your music file
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)

def draw_heart():
    obj.pensize(2)
    obj.pencolor("red")
    obj.speed(10)

    factor = 10
    obj.penup()

    for i in range(400):
        x, y = love_curve(i)
        obj.goto(x * factor, y * factor)
        obj.pendown()

    obj.penup()
    obj.forward(-180)
    obj.pendown()

    obj.setheading(42)

    obj.pensize(10)

    obj.forward(500)

    obj.setheading(-90)

    obj.forward(30)

    obj.setheading(90)

    obj.forward(30)

    obj.setheading(180)

    obj.forward(30)

    obj.hideturtle()

if __name__ == "__main__":
    turtle.title("Valentine's Day Special Love Art")
    turtle.bgcolor("black")
    turtle.delay(0)

    play_music()  # Start playing the music
    draw_heart()  # Draw the heart shape

    pygame.mixer.music.stop()  # Stop the music when the animation is done
    turtle.done()
