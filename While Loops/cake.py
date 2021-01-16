cake_width = int(input())
cake_height = int(input())

cake_volume = cake_width * cake_height
total_pieces = 0

failed = True

command = input()

while command != "STOP":
    pieces = int(command)
    total_pieces += pieces
    if total_pieces > cake_volume:
        print(f"No more cake left! You need {total_pieces - cake_volume} pieces more.")
        failed = False
        break
    command = input()

if failed:
    print(f"{cake_volume - total_pieces} pieces are left." )