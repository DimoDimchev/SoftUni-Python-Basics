lenght=int(input())
width=int(input())
height=int(input())
volume_taken=(float(input()))/100
volume_liter=((lenght*width*height)*(1/1000))

volume_water=float(volume_liter-((volume_liter)*volume_taken))
print(volume_water)