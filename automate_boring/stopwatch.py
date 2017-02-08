#! python3
# stopwatch.py

import time

# Display the program's instructions
print('Press ENTER to begin. Aftewards, press ENTER to "click the stopwatch',
      'Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap is #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() #reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep error message from displaying.
    print('\nDone')
