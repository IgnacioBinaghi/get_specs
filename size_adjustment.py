import math

suffix = ["B", "KB", "MB", "GB", "TB"]   # Suffix for later clarification
factor = 1024   # Factor for later calculations

def size_adjustment(x):
    if x == 0:
        return "0B" # if the size is zero, quickly return zero bytes
    y = int(math.floor(math.log(x, factor)))   # Calculating Space
    u = math.pow(factor, y)   # Calculating Space
    z = round(x / u, 2)  # rounding the end result
    w = (z , suffix[y])  # Creating list of the memory and its type
    return str(w[0]) + " " + w[1]   # properly formatting

