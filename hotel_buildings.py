# Imagine a hotel. It's a huge hotel consisting of three buildings,
# 15 floors each. There are 20 rooms on each floor. For this,
# you need an array which can collect and
# process information on the occupied/free rooms.

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# print(rooms)
# rooms[0][4][15] = True
# print(rooms[0][4][15])

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
        
print(vacancy)
