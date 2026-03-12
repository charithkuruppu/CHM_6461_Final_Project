#  represent a 2D lattice polymer as (x, y) coordinates + basic validation

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def make_straight_chain(N):
    # starts at (0,0) and goes to the right: (1,0), (2,0), ...
    coords = []
    for i in range(N):
        coords.append((i, 0))
    return coords

def validate_polymer(coords):
    # 1) self-avoidance (no overlaps)
    if len(set(coords)) != len(coords):
        raise ValueError("Overlap detected: not self-avoiding")

    # 2) connectivity (each bond must be to a nearest neighbor)
    for i in range(len(coords) - 1):
        if manhattan(coords[i], coords[i + 1]) != 1:
            raise ValueError(f"Broken bond at {i}->{i+1}: {coords[i]} to {coords[i+1]}")

def main():
    N = 8  
    coords = make_straight_chain(N)
    validate_polymer(coords)

    print("N =", N)
    print("Coordinates (i, x, y):")
    for i, (x, y) in enumerate(coords):
        print(i, x, y)

if __name__ == "__main__":
    main()
