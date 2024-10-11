import time

my_time = int(input("Enter the time in seconds: "))

# To count backwards, rather than reversed() we can use
# the input variable to be the start, end, and the step 
# would be -1
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x / 3600)
    
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    # sleep() stops our time for a second 
    time.sleep(1)

print("TIME'S UP")