# OMSI Map Duplicate Folder Remover

This tool helps clean up repeated folder paths in your OMSI map files.

## Problem Example

A path like:
```
Splines\Splines\hktaxidriver\hktaxidriver\2lanes_oneway_noped.sli
```
will be fixed to:
```
Splines\hktaxidriver\2lanes_oneway_noped.sli
```

## Requirements

- Python 3.12 or newer

## Usage Instructions

1. Place the Python script in the root directory of your map (e.g., `maps\Kwun Tsuen City 1.0`).
2. Run the script from inside the root directory.

The script will automatically find and fix duplicate folder names in your map paths.
