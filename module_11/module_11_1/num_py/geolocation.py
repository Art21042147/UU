"""
Данный модуль выводит расстояние между двумя точками на земной поверхности,
введёнными пользователем, используя формулу Хаверсина и библиотеку numpy.
"""
import numpy as np

earth_radius = 6371.0


def haversine(lat1, lon1, lat2, lon2):
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * \
        np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return earth_radius * c


def get_coordinates():
    lat = float(input("Введите широту точки (в градусах): "))
    lon = float(input("Введите долготу точки (в градусах): "))
    return lat, lon


print("Введите координаты первой точки")
lat1, lon1 = get_coordinates()

print("Введите координаты второй точки")
lat2, lon2 = get_coordinates()

lat1_rad = np.radians(lat1)
lon1_rad = np.radians(lon1)
lat2_rad = np.radians(lat2)
lon2_rad = np.radians(lon2)

distance = haversine(lat1_rad, lon1_rad, lat2_rad, lon2_rad)

print(f"Расстояние между двумя точками: {distance:.2f} км")
