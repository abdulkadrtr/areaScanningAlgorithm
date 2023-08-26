import matplotlib.pyplot as plt

def is_inside_polygon(x, y, vertices):
    n = len(vertices)
    inside = False
    p1x, p1y = vertices[0]
    for i in range(n+1):
        p2x, p2y = vertices[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def create_route(coordinates, radius):
    x = [x[0] for x in coordinates]
    y = [x[1] for x in coordinates]
    points = []
    xmin , xmax = min(x), max(x)
    ymin , ymax = min(y), max(y)
    x = xmin + radius
    flag = 0
    while x < xmax:
        y = ymin + radius
        if flag == 0:
            while y < ymax:
                if is_inside_polygon(x, y, coordinates):
                    points.append((x, y))
                y += 2 * radius
            flag = 1
        else:
            y = ymax + radius
            while y > ymin:
                if is_inside_polygon(x, y, coordinates):
                    points.append((x, y))
                y -= 2 * radius
            flag = 0
        x += 2 * radius
    return points

def main():
    coordinates = [(0,0),(10,0),(10,10),(0,20),(0,0)]
    x = [x[0] for x in coordinates]
    y = [x[1] for x in coordinates]
    plt.plot(x,y, color='red')
    radius = 1
    points = create_route(coordinates, radius)
    for p in points:
        circle = plt.Circle(p, radius, color='yellow', fill=True)
        plt.gca().add_artist(circle)
    for i in range(len(points) - 1):
        plt.plot([points[i][0], points[i + 1][0]], [points[i][1], points[i + 1][1]], color='green')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Tarama Algoritması')
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":
    main()

