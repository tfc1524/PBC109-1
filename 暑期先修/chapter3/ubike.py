import matplotlib.pyplot as py
import csv, datetime

# open the file
filename = 'C:\\Users\\jack\\business_program\\暑期先修\\chapter3\\ubike.csv'
with open(file=filename, mode='r') as f:
    station = {}
    count = {}
    lat = {}
    lon = {}
    capacity = {}
    for row in csv.DictReader(f):
        time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
        time = time.hour
        if time == 17 or time == 18:
            id = int(row["id"])
            if id not in station:
                lat[id] = float(row["latitude"])
                lon[id] = float(row["longitude"])
                capacity[id] = int(row["lot"])
                station[id] = int(row["bike"])
                count[id] = 1
            else:
                station[id] += int(row["bike"])
                capacity[id] += int(row["lot"])
                count[id] += 1

id_seq = station.keys()
id_seq = sorted(id_seq)
redlat = []
redlon = []
yellowlat = []
yellowlon = []
greenlat = []
greenlon = []
bluelat = []
bluelon = []

for k in id_seq:
    capacity[k] = float(capacity[k]) / count[k]
    station[k] = (float(station[k]) / count[k]) / capacity[k]
    if station[k] < 0.2:
        redlat.append(lat[k])
        redlon.append(lon[k])
    elif 0.2 <= station[k] < 0.3:
        yellowlat.append(lat[k])
        yellowlon.append(lon[k])
    elif 0.3 <= station[k] < 0.4:
        greenlat.append(lat[k])
        greenlon.append(lon[k])
    else:
        bluelat.append(lat[k])
        bluelon.append(lon[k])

py.xlabel("latitude")
py.ylabel("longitude")
py.title("Bike Distribution")
py.plot(redlat, redlon, 'ro', label='<20%')
py.plot(yellowlat, yellowlon, 'yo', label='20~30%')
py.plot(greenlat, greenlon, 'go', label='30~40%')
py.plot(bluelat, bluelon, 'bo', label='>=40%')
py.axis([25.01,25.05,121.52,121.56])
py.legend(loc='lower right')
py.show()
