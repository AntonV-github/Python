from geopy.geocoders import Nominatim

def decimale(str):
    dm = str.split(',')
    deg = float(dm[0])
    min = float(dm[1].split("'")[0])
    return (deg+min/60)


def get_from_file(file):
    with open(file, 'r') as f:
        coords = f.readline().split(";")
        lati = decimale(coords[0])
        long = decimale(coords[1])
    return f"{lati},{long}"

coordinates = get_from_file('coords.txt')
geo = Nominatim(user_agent="My16")

location = geo.reverse(coordinates)
print(location.address)
print('Google Maps URL: ' f'https://www.google.com/maps/search/?api=1&query={location.latitude},{location.longitude}')