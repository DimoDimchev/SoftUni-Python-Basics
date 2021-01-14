hours= int(input())
minutes= int(input())

added= minutes+15

if added>59:
    hours+=1
    if hours>23:
        hours=hours-24

    minutes= added-60
    if minutes<10:
        print(f"{hours}:0{minutes}")
    else:
        print(f"{hours}:{minutes}")
else:
    minutes=added
    if minutes<10:
        print(f"{hours}:0{minutes}")
    else:
        print(f"{hours}:{minutes}")