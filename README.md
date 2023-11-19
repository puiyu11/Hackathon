# OBJ Bounding Box Dimensions

This code calculates the dimensions of a bounding box for a 3D model stored in an OBJ file. It uses NumPy for mathematical operations and JSON for data serialization.

## Prerequisites

Make sure you have the following dependencies installed:

- NumPy
- JSON

## Usage

1. Place your OBJ file in the same directory as the script.
2. Update the `obj_file_path` variable in the script with the path to your OBJ file.
3. Run the script.

The script will compute the bounding box dimensions of the 3D model and display the width, height, and depth. Additionally, it will save the dimensions as a JSON file named `output.json` in the same directory.

## Example

Assuming you have a file named `textured_output.obj` in the same directory as the script, the script will load the OBJ file, calculate the bounding box dimensions, and display the results.

```
Width: [width_value]
Height: [height_value]
Depth: [depth_value]
```

The dimensions will also be saved in the `output.json` file in the following format:

```json
{
  "width": [width_value_in_cm],
  "height": [height_value_in_cm],
  "depth": [depth_value_in_cm],
  "cbm": [volume_value_in_cubic_meters]
}
```
