import math
from geopy.distance import geodesic
from time import sleep


def get_gps_data():
    
    sample_coords = [
        (12.971598, 77.594566), 
        (12.972598, 77.594566),  
        (12.972598, 77.595566),  
    ]
    return sample_coords.pop(0)  

def get_camera_direction():
   
    return 45

def calculate_square_meters(distance1, distance2):
    """Calculate area in square meters given two distances."""
    return distance1 * distance2

def square_meters_2_square_feet(square_meters):
    """Convert square meters to square feet."""
    conversion_factor = 10.7639
    return square_meters * conversion_factor

if __name__ == "__main__":
    points = []

    print("Please point the camera at three different points.")
    for i in range(3):
        input(f"Press Enter to capture point {i + 1}")
        
        gps_coords = get_gps_data()
        print(f"Captured point {i + 1}: {gps_coords}")
        points.append(gps_coords)
        sleep(1)  

    if len(points) == 3:
    
        distance1 = geodesic(points[0], points[1]).meters
        distance2 = geodesic(points[1], points[2]).meters

        print(f"Distance1: {distance1:.2f} meters")
        print(f"Distance2: {distance2:.2f} meters")

    
        area_square_meters = calculate_square_meters(distance1, distance2)
        area_square_feet = square_meters_2_square_feet(area_square_meters)

        print(f"Area: {area_square_meters:.2f} square meters")
        print(f"Area: {area_square_feet:.2f} square feet")
    else:
        print("Failed to capture three points.")

