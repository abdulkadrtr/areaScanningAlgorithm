# areaScanningAlgorithm
This algorithm generates a GPS route, enabling drones to autonomously scan entire areas by following this route. The parameter 'R' represents the drone's domain radius, ensuring efficient coverage.


![1](https://github.com/abdulkadrtr/areaScanningAlgorithm/assets/87595266/4143502f-d771-401b-8d6a-c5492f763c73)
![2](https://github.com/abdulkadrtr/areaScanningAlgorithm/assets/87595266/2972deeb-0548-439c-9731-39ff0dc743c7)


## How does it work ?

The Area Scanning Algorithm has been meticulously crafted for autonomous agricultural drones, with a specific focus on facilitating precise area irrigation and pesticide application. Initially, the algorithm identifies the designated area using GPS coordinates of its corner points, effectively converting them into Cartesian coordinates. Subsequently, it strategically positions a maximum number of circles with a radius of 'r' within this area.

Employing a custom-designed algorithm, the centers of these circles are organized into a sequence that forms the optimal route. This route, constructed in the Cartesian coordinate system, is then transformed back into the GPS coordinate system. Utilizing the Folium library, the resulting route is visually represented in the `route.html` file. Simultaneously, the `area.html` file showcases the boundary edges of the scanning area.

The algorithm's core purpose is to enable autonomous agricultural drones to execute precise irrigation and pesticide application tasks within a designated field.

## Algorithm
![MultiRobot Kopyası](https://github.com/abdulkadrtr/areaScanningAlgorithm/assets/87595266/0d1e59d3-6824-467c-9bab-bc9e2c09792d)

## Requirements
```
- folium
- pyproj
- matplotlib
```
