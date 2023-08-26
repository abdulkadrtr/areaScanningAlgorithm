# areaScanningAlgorithm
Area scanning algorithm for autonomous robots. This algorithm provides you with a GPS route.


<img src="https://github.com/abdulkadrtr/areaScanningAlgorithm/assets/87595266/9a0aea9b-ac98-42dc-8ba9-febab344732e" alt="1" width="960" height="540">
<img src="https://github.com/abdulkadrtr/areaScanningAlgorithm/assets/87595266/14713706-d648-4267-8300-99207140ae08" alt="2" width="960" height="540">

## How does it work ?
The Area Scanning Algorithm has been meticulously crafted for autonomous agricultural drones, with a specific focus on facilitating precise area irrigation and pesticide application. Initially, the algorithm identifies the designated area using GPS coordinates of its corner points, effectively converting them into Cartesian coordinates. Subsequently, it strategically positions a maximum number of circles with a radius of 'r' within this area.

Employing a custom-designed algorithm, the centers of these circles are organized into a sequence that forms the optimal route. This route, constructed in the Cartesian coordinate system, is then transformed back into the GPS coordinate system. Utilizing the Folium library, the resulting route is visually represented in the `route.html` file. Simultaneously, the `area.html` file showcases the boundary edges of the scanning area.

The algorithm's core purpose is to enable autonomous agricultural drones to execute precise irrigation and pesticide application tasks within a designated field.

## Algorithm
<img src="https://github.com/abdulkadrtr/areaScanningAlgorithm/assets/87595266/8c39af51-9fe8-4308-bfa5-4907536b9b4c" alt="3" width="960" height="540">
