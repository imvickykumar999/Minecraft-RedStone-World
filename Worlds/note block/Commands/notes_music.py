
hbd = [8,3,8,1,10,4,8,4,13,4,12,8,8,3,8,1,10,4,8,4,15,4,13,8,8,3,8,1,20,4,17,4,13,4,12,4,10,4,18,3,18,1,17,4,13,4,15,4,13]

print(hbd[::2])
print(hbd[1::2])

tetris = [22,4,17,2,18,2,20,4,18,2,17,2,15,4,15,2,18,2,22,4,20,2,18,2,17,4,17,2,18,2,20,4,22,4,18,4,15,4,15]

print(tetris[::2])
print(tetris[1::2])

import winsound

# frequency is set to 500Hz
freq = 500

# duration is set to 100 milliseconds			
dur = 100
			
winsound.Beep(freq, dur)

