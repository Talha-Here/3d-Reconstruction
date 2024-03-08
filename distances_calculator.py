import json
import numpy as np
from scipy.spatial import distance

def dist_calc(position_vector):
    # Load JSON data from the file
    with open("reconstruction.json", "r") as file:
        data = json.load(file)

    # Extract shots data from the first item in the data list
    shots = data[0]["shots"]

    # Calculate Euclidean distances for shots
    shot_distances = {}
    for i in range(1, len(shots)):
        key1 = "{:02d}.jpg".format(i)
        key2 = "{:02d}.jpg".format(i + 1)

        translation1 = np.array(shots[key1]["translation"])
        translation2 = np.array(shots[key2]["translation"])

        dist = distance.euclidean(translation2, translation1)
        shot_distances[f"{key1}-{key2}"] = dist

    # Calculate Euclidean distances for position vectors
    vector_distances = {}
    for i in range(1, len(position_vector)):
        key1 = f"{i-1}-{i}"
        key2 = f"{i}-{i+1}"

        vector1 = position_vector[i-1]
        vector2 = position_vector[i]

        dist = np.linalg.norm(vector2 - vector1)
        vector_distances[key1] = dist

    # Create a dictionary with the desired structure
    merged_data = [
        {"shot_distances": shot_distances},
        {"vector_distances": vector_distances}
    ]

    output_file = "euclidean_distances.json"
    with open(output_file, "w") as file:
        json.dump(merged_data, file, indent=2)

    print(f"Distances saved to {output_file}")