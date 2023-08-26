import folium
from pyproj import Transformer

EPSG_GPS = 4326
EPSG_XYZ = 6500

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

def saveMap(coordinates,name):
    center = [sum(x[0] for x in coordinates) / len(coordinates), sum(x[1] for x in coordinates) / len(coordinates)]
    m = folium.Map(location=center, zoom_start=15)
    folium.PolyLine(locations=coordinates, color='blue').add_to(m)
    m.save(name+'.html')

def main():
    #Coordinates of the area
    coordinates = [(41.09766861427918, 28.034385995432903), (41.09906670509148, 28.03518110686258), (41.09698620200388, 28.043507690445626), (41.095371686198035, 28.043596036160036)]
    radius = 5 # meter
    coordinates.append(coordinates[0])
    saveMap(coordinates,'area')
    transformer_f = Transformer.from_crs(EPSG_GPS, EPSG_XYZ)
    coordinates = [transformer_f.transform(lat, lon) for lat, lon in coordinates]
    points = create_route(coordinates, radius)
    transformer_r = Transformer.from_crs(EPSG_XYZ, EPSG_GPS)
    points = [transformer_r.transform(x, y) for x, y in points]
    saveMap(points,'route')

if __name__ == "__main__":
    main()

