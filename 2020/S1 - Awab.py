def userIn():
    N = int(input())

    observations = []

    for i in range(N):
        obs = input().split()
        obs = [int(obs[0]), int(obs[1])]

        observations.append(obs)

    return N, observations


def calcSpeed(pos, time):
    posLater, posNow = pos
    timeLater, timeNow = time

    timeTaken = timeLater - timeNow
    speed = abs(posLater - posNow) / timeTaken

    return speed


N, observations = userIn()

sortedObs = observations.sort(key=lambda x: x[0])

speeds = []

for i in range(N):
    pos = (sortedObs[i+1, 1], sortedObs[i, 1])
    time = (sortedObs[i+1, 0], sortedObs[i, 0])

    speeds.append(calcSpeed(pos, time))

print("{.1f}".format(max(speeds)))
