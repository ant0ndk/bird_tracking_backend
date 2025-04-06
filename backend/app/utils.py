from math import radians, cos, sin, asin, sqrt
from datetime import datetime

# Haversine formula для расстояния между двумя GPS координатами
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Радиус Земли в км
    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    a = sin(d_lat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon/2)**2
    return 2 * R * asin(sqrt(a))

# Расчет средней скорости
def calculate_avg_speed(data):
    if len(data) < 2:
        return 0
    total_distance = 0
    total_time = 0
    for i in range(1, len(data)):
        d = haversine(data[i-1].latitude, data[i-1].longitude, data[i].latitude, data[i].longitude)
        t = (data[i].timestamp - data[i-1].timestamp).total_seconds() / 3600  # часы
        total_distance += d
        total_time += t
    return total_distance / total_time if total_time else 0

# Расчет средней дистанции
def calculate_avg_distance(data):
    if len(data) < 2:
        return 0
    total_distance = sum(
        haversine(data[i-1].latitude, data[i-1].longitude, data[i].latitude, data[i].longitude)
        for i in range(1, len(data))
    )
    return total_distance / (len(data) - 1)
