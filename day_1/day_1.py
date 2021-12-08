import numpy as np

with open("/home/stijn/Documents/input.txt", "r") as file:
    data = [int(x) for x in file.readlines()]

# [1,2,3,4,5 ,6 ,7 ,8 ,9 ,10     ]
# [  1,2,3,4 ,5 ,6 ,7 ,8 ,9, 10  ]
# [    1,2,3 ,4 ,5 ,6 ,7 ,8, 9,10]
# [    6,9,12,15,18,21,24,27     ]


w1 = data + [0, 0]
w2 = [0] + data + [0]
w3 = [0, 0] + data
f_moving_window = np.array(w1) + np.array(w2) + np.array(w3)
moving_window = f_moving_window[2:-2]
print(len(data))
print(len(moving_window))
before = np.append(moving_window, 0)
after = np.append(0, moving_window)
res = (before-after)[1:-1]
print(before)
print(after)
print(res)
print(len(np.where(res > 0)[0]))
