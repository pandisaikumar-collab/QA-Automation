# Problem statement:

import time
from datetime import datetime

while True:
    current_time = datetime.now()
    current_our = current_time.hour
    print(current_time)

    if current_our > 12: # == for exact match
        print("now time is 12..")
        break
    else:
        print("time not yet 12..")
        time.sleep(300)