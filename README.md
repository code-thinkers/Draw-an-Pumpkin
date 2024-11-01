# Vẽ Hình Nghệ Thuật với Turtle 🐢 - Bí Ngô Halloween 🔵🔺

Chào mừng bạn đến với dự án **Vẽ Hình Nghệ Thuật với Turtle**! 🌈 Dự án này sẽ hướng dẫn bạn cách vẽ các hình đơn giản nhưng đầy thú vị bằng cách sử dụng thư viện **Turtle** trong Python. Chúng ta sẽ vẽ các hình tròn và tam giác, tạo nên một bức tranh nhỏ sáng tạo ngay trên màn hình. Thật tuyệt vời phải không? 🌟

## Mô Tả Dự Án 📝

Dự án này sử dụng thư viện **Turtle** để vẽ hai hình tròn màu cam 🍊 và ba hình tam giác màu vàng 🌟. Bạn sẽ học cách điều khiển bút vẽ của Turtle để tạo ra các hình khác nhau, thiết lập màu sắc và sử dụng các lệnh cơ bản như di chuyển và tô màu. 

## Cách Chạy Dự Án 🚀

1. **Cài đặt Python**: Đảm bảo bạn đã cài đặt Python trên máy tính của mình. Tải Python tại [python.org](https://www.python.org/downloads/).
   
2. **Chạy mã nguồn**: Sao chép mã nguồn, mở tệp Python (.py) trong trình soạn thảo mã và chạy:
   ```bash
   python DrawAnPumpkin.py
   ```

## Mã Nguồn 📄

Dưới đây là mã nguồn chính của dự án:

```python
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
```

## Tính Năng Chính 🎨

- **Tùy chỉnh màu sắc**: Bạn có thể dễ dàng thay đổi màu sắc của các hình để tạo nên tác phẩm của riêng mình!
- **Vẽ hình cơ bản**: Tập trung vào việc vẽ hình tròn và tam giác, giúp bạn hiểu rõ hơn về các lệnh vẽ trong Turtle.
- **Khám phá Turtle**: Dự án này là cơ hội để bạn làm quen và thực hành với các lệnh điều khiển trong Turtle.

## Liên Hệ 🤝

Nếu bạn có bất kỳ câu hỏi nào hoặc muốn chia sẻ tác phẩm của mình, hãy liên hệ với chúng tôi qua [Fanpage CodeThinkers](https://www.facebook.com/CodeThinkers).

---

**Hãy thử tự tạo các hình vẽ và biến ý tưởng của bạn thành hiện thực qua từng nét bút Turtle!** 🖌️✨
