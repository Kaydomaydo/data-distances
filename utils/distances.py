def manhattan(a, b):
    # a ve b birer tuple: (x, y)
    d_x = abs(b[0] - a[0])
    d_y = abs(b[1] - a[1])
    
    return d_x + d_y
