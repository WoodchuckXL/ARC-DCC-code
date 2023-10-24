from djitellopy import Tello
import random
import matplotlib.pyplot as plt

def genenerateRandomWaypoints(count : int):
    waypoints = []

    for i in range(count):
        waypoints.append([0, 0])
        for j in range(2):
            waypoints[i][j] = random.randrange(-100, 100, 5)
    return waypoints


def generatePermutations(arr):
    def backtrack(start):
        if start == len(arr):
            permutations.append(arr[:])  # Append a copy of the current permutation
            return
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]  # Swap elements
            backtrack(start + 1)  # Recurse on the rest of the list
            arr[start], arr[i] = arr[i], arr[start]  # Restore the original arrangement

    permutations = []
    backtrack(0)
    return permutations


def findDist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ( (x1 - x2)**2 + (y1 - y2)**2 )**0.5

def pathDist(order, waypoints):
    dist = findDist([0,0], waypoints[order[0]])
    for i in range(len(order) - 1):
        dist += findDist(waypoints[order[i]], waypoints[order[i + 1]])
    return dist

def findShortestPath(waypoints):
    nums = [num for num in range(len(waypoints))]

    perms = generatePermutations(nums)

    bestOrder = None
    minDist = 2**31

    for order in perms:
        #Try every order looking for minimum dist
        dist = pathDist(order, waypoints)

        if dist < minDist:
            minDist = dist
            bestOrder = order

    return [waypoints[i] for i in bestOrder]

def flyTo(curPoint, toPoint, tello):
    tello.go_xyz_speed(toPoint[0] - curPoint[0], toPoint[1] - curPoint[1], 0, 20)


# Generate Random Coordinates inside a 2m by 2m
waypoints = genenerateRandomWaypoints(5)
print(waypoints)

# Find the shortest path through all the waypoints
newWaypoints = findShortestPath(waypoints)
print(newWaypoints)


# Fly calculated path
tello = Tello()

tello.connect(True)

tello.takeoff()

flyTo([0,0], newWaypoints[0], tello)
for i in range(1 , len(newWaypoints)):
    flyTo(newWaypoints[i - 1], newWaypoints[i], tello)

tello.land()


# Graph the waypoints
x = [point[0] for point in newWaypoints]
y = [point[1] for point in newWaypoints]
labels = [num for num in range(len(newWaypoints))]

x.append(0)
y.append(0)
labels.append("Start")

plt.scatter(x, y, label='Coordinates', color='blue', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.title('Coordinate Graph')

for i, label in enumerate(labels):
    plt.text(x[i], y[i], label, fontsize=12, ha='right')

plt.show()