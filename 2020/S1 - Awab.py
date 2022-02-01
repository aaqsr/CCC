def userIn():
    N = int(input())
    
    observations = []
    
    for i in range(N):
        obs = input().split()
        obs = [int(obs[0]), int(obs[1])]
        
        observations.append(obs)
        
    return N, observations

def calcSpeed(posLater, posNow, timeLater, timeNow):
    timeTaken = timeLater - timeNow
    speed = abs(posLater - posNow) / timeTaken
    
    return speed


N, observations = userIn()

observations.sort(key=lambda x : x[0])

speeds = []

for i in range(1, N):
    posNow = observations[i][1]
    posBefore = observations[i-1][1]
    timeNow = observations[i][0]
    timeBefore = observations[i-1][0]
    
    speeds.append(calcSpeed(posNow, posBefore, timeNow, timeBefore))

print(round(max(speeds), 1))