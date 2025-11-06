# Project Overview

This project generates world maps using the Matplotlib and Cartopy Python libraries. The main script, `world_map_dots.py`, creates a world map with a Plate Carrée projection, highlighting major cities with scatter points and using hatch patterns to represent landmasses. The output is saved as a PNG image in the `maps/` directory.

# Building and Running

## Dependencies

* Python 3.x
* Matplotlib
* Cartopy

## Running the project

To generate a world map, run the following command:

```bash
python world_map_dots.py
```

This will create a new file named `world_map_<random_number>.png` in the `maps/` directory.

# Development Conventions

The code is written in Python and follows standard PEP 8 conventions. The project is structured with a clear separation of concerns, with different scripts for generating different types of maps.
