import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'  # начальный цвет
    points = []  # точки для рисования линий
    shapes = []  # список фигур
    drawing = False
    start_pos = None
    drawing_rect = False
    drawing_circle = False
    drawing_shape = False  # для треугольников и ромба

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # Выход из программы
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Выбор режима рисования
                if event.key == pygame.K_r:
                    mode = 'red'  # красный
                elif event.key == pygame.K_g:
                    mode = 'green'  # зелёный
                elif event.key == pygame.K_b:
                    mode = 'blue'  # синий
                elif event.key == pygame.K_e:
                    mode = 'eraser'  # ластик
                elif event.key == pygame.K_s:
                    mode = 'square'  # квадрат
                elif event.key == pygame.K_c:
                    mode = 'circle'  # круг
                elif event.key == pygame.K_t:
                    mode = 'right_triangle'  # прямоугольный треугольник
                elif event.key == pygame.K_q:
                    mode = 'equilateral_triangle'  # равносторонний треугольник
                elif event.key == pygame.K_h:
                    mode = 'rhombus'  # ромб

            # Нажатие мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'square':
                    start_pos = event.pos
                    drawing_rect = True
                elif mode == 'circle':
                    start_pos = event.pos
                    drawing_circle = True
                elif mode in ['right_triangle', 'equilateral_triangle', 'rhombus']:
                    start_pos = event.pos
                    drawing_shape = True
                else:
                    drawing = True
                    points.append(((None, None), mode))
                    points.append((event.pos, mode))

            # Отпускание кнопки мыши
            elif event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos
                if drawing_rect and start_pos:
                    shapes.append((start_pos, end_pos, 'square'))
                    drawing_rect = False
                elif drawing_circle and start_pos:
                    shapes.append((start_pos, end_pos, 'circle'))
                    drawing_circle = False
                elif drawing_shape and start_pos:
                    shapes.append((start_pos, end_pos, mode))
                    drawing_shape = False
                drawing = False

            # Движение мыши при рисовании
            if event.type == pygame.MOUSEMOTION and drawing:
                position = event.pos
                points.append((position, mode))

        screen.fill((0, 0, 0))  # очистка экрана

        # Отображение всех сохранённых фигур
        for shape in shapes:
            start, end, shape_mode = shape
            if shape_mode == 'square':
                drawRectangle(screen, start, end, mode)
            elif shape_mode == 'circle':
                drawCircle(screen, start, end, mode)
            elif shape_mode == 'right_triangle':
                drawRightTriangle(screen, start, end, mode)
            elif shape_mode == 'equilateral_triangle':
                drawEquilateralTriangle(screen, start, end, mode)
            elif shape_mode == 'rhombus':
                drawRhombus(screen, start, end, mode)

        # Отображение линий при рисовании от руки
        i = 0
        while i < len(points) - 1:
            if points[i][0] != (None, None) and points[i + 1][0] != (None, None):
                drawLineBetween(screen, i, points[i], points[i + 1], radius, points[i][1])
            i += 1

        pygame.display.flip()
        clock.tick(60)

# Рисование линии между двумя точками
def drawLineBetween(screen, index, point1, point2, width, color_mode):
    start, color_mode = point1
    end, _ = point2

    color = getColor(color_mode)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Цвет по режиму
def getColor(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    elif mode == 'eraser':
        return (0, 0, 0)
    return (255, 255, 255)

# Прямоугольник (в т.ч. квадрат)
def drawRectangle(screen, start, end, mode):
    color = getColor(mode)
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])
    pygame.draw.rect(screen, color, (x, y, width, height), 3)

# Круг
def drawCircle(screen, start, end, mode):
    color = getColor(mode)
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
    radius = max(abs(start[0] - end[0]) // 2, abs(start[1] - end[1]) // 2)
    pygame.draw.circle(screen, color, center, radius, 3)

# Прямоугольный треугольник
def drawRightTriangle(screen, start, end, mode):
    color = getColor(mode)
    p1 = start
    p2 = (start[0], end[1])
    p3 = end
    pygame.draw.polygon(screen, color, [p1, p2, p3], 3)

# Равносторонний треугольник
def drawEquilateralTriangle(screen, start, end, mode):
    color = getColor(mode)
    mid_base = ((start[0] + end[0]) / 2, end[1])
    side = abs(end[0] - start[0])
    height = (math.sqrt(3) / 2) * side
    top = (mid_base[0], mid_base[1] - height)
    pygame.draw.polygon(screen, color, [start, end, top], 3)

# Ромб
def drawRhombus(screen, start, end, mode):
    color = getColor(mode)
    mid_x = (start[0] + end[0]) // 2
    mid_y = (start[1] + end[1]) // 2
    dx = abs(end[0] - start[0]) // 2
    dy = abs(end[1] - start[1]) // 2
    points = [
        (mid_x, start[1]),
        (end[0], mid_y),
        (mid_x, end[1]),
        (start[0], mid_y)
    ]
    pygame.draw.polygon(screen, color, points, 3)

main()