# 2D Lattice Polymer Representation (SAW/HP Project)

## What this code does
- Represents a polymer chain on a **2D square lattice** as a list of coordinates `(x, y)`.
- Defines bonds implicitly between monomers `i` and `i+1`.
- Validates a conformation by checking:
  1) **Self-avoidance**: no overlapping lattice sites  
  2) **Connectivity**: each bond has Manhattan distance = 1

## File
- `Model_basis.py`

## Run
```bash
python Model_basis.py --N 20
# CHM_6461_Final_Project
