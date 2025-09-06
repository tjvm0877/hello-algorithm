x, y, w, h = map(int, input().split())

go_h = h - y
go_w = w - x
x_min = min(x, go_w)
y_min = min(y, go_h)

print(min(x_min, y_min))
