import numpy as np
import json


def compute_bounding_box_dimensions(vertices):
    min_coords = np.min(vertices, axis=0)
    max_coords = np.max(vertices, axis=0)
    dimensions = max_coords - min_coords
    return dimensions

def load_obj(file_path):
    vertices = []

    with open(file_path, 'r') as obj_file:
        for line in obj_file:
            tokens = line.strip().split()

            if tokens and tokens[0] == 'v':
                # Extract vertex coordinates
                x, y, z = map(float, tokens[1:])
                vertices.append((x, y, z))

    return np.array(vertices)

if __name__ == "__main__":
    # Replace 'path/to/your/model.obj' with the actual path to your OBJ file
    obj_file_path = 'textured_output.obj'

    # Load OBJ file
    model_vertices = load_obj(obj_file_path)

    # Compute bounding box dimensions
    dimensions = compute_bounding_box_dimensions(model_vertices)
    
    # Print the dimensions
    print(f"Width: {dimensions[0]}, Height: {dimensions[1]}, Depth: {dimensions[2]}")

    dimensions_dict = {"width": round(dimensions[0]*100, 2), "height": round(dimensions[1]*100, 2), "depth": round(dimensions[2]*100, 2), "cbm": round(dimensions[0]*dimensions[1]*dimensions[2], 3)}

     # Convert the dictionary to a JSON string
    dimensions_json = json.dumps(dimensions_dict)

    # Print the dimensions
    print(dimensions_json)

    # Write the dimensions to a JSON file
    with open('output.json', 'w') as json_file:
        json.dump(dimensions_dict, json_file, indent=2)
