from collections import Counter
import csv

def findmean(totalweight, total):
    mean = totalweight / total
    print(f"Mean = {mean:2f}")

def findmedian(total, sorteddata):
    if total % 2 == 0:
        median1 = float(sorteddata[total//2])
        median2 = float(sorteddata[total//2 - 1])
        median = (median1 + median2) / 2
    else:
        median = float(sorteddata[total//2])
    print(f"Median = {median:2f}")

def findmode(sorteddata):
    data = Counter(sorteddata)
    modedata = {
                            "75-85": 0,
                            "85-95": 0,
                            "95-105": 0,
                            "105-115": 0,
                            "115-125": 0,
                            "125-135": 0,
                            "135-145": 0,
                            "145-155": 0,
                            "155-165": 0,
                            "165-175": 0
                        }
    for weight, occurence in data.items():
        if 75 < weight < 85:
            modedata["75-85"] += occurence
        elif 85 < weight < 95:
            modedata["85-95"] += occurence
        elif 95 < weight < 105:
            modedata["95-105"] += occurence
        elif 105 < weight < 115:
            modedata["105-115"] += occurence
        elif 115 < weight < 125:
            modedata["115-125"] += occurence
        elif 125 < weight < 135:
            modedata["125-135"] += occurence
        elif 135 < weight < 145:
            modedata["135-145"] += occurence
        elif 145 < weight < 155:
            modedata["145-155"] += occurence
        elif 155 < weight < 165:
            modedata["155-165"] += occurence
        elif 165 < weight < 175:
            modedata["165-175"] += occurence
    mode_range, mode_occurence = 0, 0
    for range, occurence in modedata.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode = {mode:2f}")

with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)

totalweight = 0
total = len(file_data)
sorteddata = []

for datap in file_data:
    totalweight += float(datap[2])
    sorteddata.append(float(datap[2]))

sorteddata.sort()

findmean(totalweight, total)
findmedian(total, sorteddata)
findmode(sorteddata)
