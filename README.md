# Week 1 — 2D Lattice Polymer Representation (SAW/HP Project)

## What this code does
- Represents a polymer chain on a **2D square lattice** as a list of coordinates `(x, y)`.
- Defines bonds implicitly between monomers `i` and `i+1`.
- Validates a conformation by checking:
  1) **Self-avoidance**: no overlapping lattice sites  
  2) **Connectivity**: each bond has Manhattan distance = 1

## File
- `week1_only_2d_polymer.py`

## Run
```bash
python week1_only_2d_polymer.py --N 20
# CHM_6461_Final_Project
