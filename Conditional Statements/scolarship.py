import math
from math import floor

income= float(input())
gpa= float(input())
minimumWage=float(input())

if income<minimumWage and gpa>=4.5:
    if gpa>=5.5:
        if (gpa*25)>((35/100)*minimumWage):
            print(f"You get a scholarship for excellent results {floor(gpa*25)} BGN")
        else:
            print(f"You get a Social scholarship {floor((35/100)*minimumWage)} BGN")
    else:
        print(f"You get a Social scholarship {floor((35/100) * minimumWage)} BGN")
else:
    if gpa >=5.5:
        print(f"You get a scholarship for excellent results {floor(gpa * 25)} BGN")
    else:
        print("You cannot get a scholarship!")