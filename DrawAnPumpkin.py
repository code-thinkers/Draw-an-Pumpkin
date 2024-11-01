import turtle

def drawcircle(x):
    t.color("orange")  # Đặt màu cho hình tròn là cam 🍊
    t.penup()  # Nhấc bút để di chuyển mà không vẽ ✋
    t.goto(x, -50)  # Di chuyển đến vị trí (x, -50) 📍
    t.pendown()  # Hạ bút để bắt đầu vẽ ✏️
    t.begin_fill()  # Bắt đầu tô màu hình tròn 🎨
    t.circle(70)  # Vẽ hình tròn bán kính 70 🔵
    t.end_fill()  # Kết thúc tô màu hình tròn 🖌️

def drawtriangle(x, y):
    t.color("yellow")  # Đặt màu cho hình tam giác là vàng 🌟
    t.penup()  # Nhấc bút để di chuyển mà không vẽ ✋
    t.goto(x, y)  # Di chuyển đến vị trí (x, y) 📍
    t.pendown()  # Hạ bút để bắt đầu vẽ ✏️
    t.begin_fill()  # Bắt đầu tô màu hình tam giác 🎨
    for i in range(3):  # Vẽ hình tam giác bằng cách lặp 3 lần 🔺
        t.forward(36)  # Vẽ cạnh dài 36 đơn vị 📏
        t.left(360 / 3)  # Quay trái 120 độ để tạo góc tam giác 🔄
    t.end_fill()  # Kết thúc tô màu hình tam giác 🖌️

if __name__ == '__main__':
    t = turtle.Turtle()  # Tạo đối tượng Turtle để vẽ 🐢
    t.speed(5)  # Đặt tốc độ vẽ trung bình 🚶‍♂️
    turtle.bgcolor("black")  # Đặt màu nền là đen 🖤

    drawcircle(20)  # Vẽ hình tròn đầu tiên 🎨
    drawcircle(-20)  # Vẽ hình tròn thứ hai 🎨

    drawtriangle(20, 25)  # Vẽ tam giác đầu tiên 🎨
    drawtriangle(-55, 25)  # Vẽ tam giác thứ hai 🎨
    drawtriangle(-18, 0)  # Vẽ tam giác thứ ba 🎨

    turtle.done()  # Hoàn tất vẽ và giữ cửa sổ mở 🎉
