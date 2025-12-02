import turtle
def draw_koch(t, length, depth):
    if depth == 0:  
        t.forward(length)
    else:  

        draw_koch(t, length/3, depth-1)
        t.left(60)
        draw_koch(t, length/3, depth-1)
        t.right(120)
        draw_koch(t, length/3, depth-1)
        t.left(60)
        draw_koch(t, length/3, depth-1)

# Головна функція для малювання сніжинки
def draw_snowflake(depth):
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.title(f"Сніжинка Коха (рівень: {depth})")
    
    # Налаштовуємо черепашку
    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    
    # Малюємо 3 сторони сніжинки
    for _ in range(3):
        draw_koch(t, 300, depth)
        t.right(120)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (0-4): "))
        if 0 <= level <= 4:
            draw_snowflake(level)
        else:
            print("Рівень має бути від 0 до 4")
    except ValueError:
        print("Потрібно ввести число")