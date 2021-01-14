import math
from math import floor

record= float(input())
distance= float(input())
time_per_meter= float(input())

attempt= distance*time_per_meter+(floor((distance/15))*12.5)

if attempt<record:
    print(f"Yes, he succeeded! The new world record is "+'{0:.2f}'.format(attempt)+" seconds.")
else:
    print(f"No, he failed! He was "+'{0:.2f}'.format(attempt-record)+" seconds slower.")