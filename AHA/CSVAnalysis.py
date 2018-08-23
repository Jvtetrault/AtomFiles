import csv
import easygui
import numpy as np
import matplotlib.pyplot as plt

url = easygui.enterbox(
    msg="Paste CVS file path here",
    title="CVS testing inquiry",
    strip=True,
    default="C:\Users\Joe_T\OneDrive\Desktop\Test\Plots\PT0.5-01.cvs")

k = 0
dataArray = []
xValue = []

with open(url) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[0].strip() == "Value":
            print("Found it")
        else:
            for string in row:
                row = [k, string.split(None, 1)[-1]]
                k = k+1
                dataArray.append(float(row[1]))
                xValue.append(int(row[0]))

newArray = dataArray
newValue = xValue

def smoothen(data):
    data2 = data[:]
    for i in range(1, len(data)-1):
        data2[i] = round(sum(data[i-1:i+2])/3, 2)
    data = data2
    return data

def reject_outliers(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def turnpoint(data):
    dx = np.diff(data)
    return np.sum(dx[1:]*dx[:-1]<0)


def plot(series, xaxis=3000, yaxis=6, userLabel='Label'):
    axes = plt.gca()
    plt.plot(xValue, dataArray, 'r+', label=str(userLabel))
    axes.set_xlim([0,xaxis])
    axes.set_ylim([0,yaxis])
    plt.grid(True)
    plt.show()

corrected = smoothen(reject_outliers(np.array(newArray)))
print(turnpoint(corrected))
print(corrected)

plot(corrected, 3000, 6, "Test")
# axes = plt.gca()
# plt.plot(xValue, corrected, 'g+', label='corrected')
# axes.set_xlim([0,3000])
# axes.set_ylim([0,15])
# plt.grid(True)
# plt.show()

# axes2 = plt.gca()
# plt.plot(xValue, dataArray, 'r+', label='stock')
# axes2.set_xlim([0,3000])
# axes2.set_ylim([0,15])
# plt.grid(True)
# plt.show()
