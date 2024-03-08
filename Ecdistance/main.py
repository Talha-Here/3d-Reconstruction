import json
import math

# Load JSON data
with open('reconstruction.json', 'r') as file:
    data = json.load(file)

# Extract translation vectors from the shots
translations = [shot['translation'] for shot in data[0]['shots'].values()]

# translations = [shot['translation'] for shot in data[0]['shots']]


# for shot in data[0]["shots"]:
print(translations)

# Calculate Euclidean distance between consecutive translations
total_distance = 0
for i in range(1, len(translations)):
    prev_translation = translations[i - 1]
    curr_translation = translations[i]
    
    # Calculate Euclidean distance between two points in 3D space
    distance = math.sqrt(sum((curr - prev) ** 2 for curr, prev in zip(curr_translation, prev_translation)))
    
    total_distance += distance

print("Total Euclidean distance:", total_distance)