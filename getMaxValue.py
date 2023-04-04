import numpy as np

# read the file into a numpy array
data = np.loadtxt('numfile.txt')

# find the maximum value in column 4
max_value = np.amax(data[:,3])

index = 0
for num in np.nditer(data[:,3]):
    if num == max_value:
        index += 1
        break
    index += 1

print(data[index-1:index:4])