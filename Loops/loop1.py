import time

attempts = 0
retries = 5
wait_time = 1

while (attempts < retries):
    print("attempt", attempts + 1 ,"wait time", wait_time ,"secs")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
