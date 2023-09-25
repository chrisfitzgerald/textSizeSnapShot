import csv
import random

# Function to generate a random text size
def generate_text_size():
    # Define the size ranges and their associated probabilities
    size_ranges = [
        (0.01, 1000),       # Small size range (most common)
        (1001, 30000),     # Medium size range (less common)
        (30001, 5000000),  # Large size range (least common)
    ]

    # Define probabilities for each size range (adjust as needed)
    probabilities = [0.6, 0.3, 0.1]

    # Choose a size range based on probabilities
    selected_range = random.choices(size_ranges, probabilities)[0]

    # Generate a random size within the selected range
    size_kb = random.uniform(selected_range[0], selected_range[1])

    # Determine the size classification based on text size range
    if selected_range == size_ranges[0]:
        size_class_range = "Small"
    elif selected_range == size_ranges[1]:
        size_class_range = "Medium"
    else:
        size_class_range = "Large"

    # Determine the size classification based on thirds within each range
    lower, mid, upper = selected_range[0], (selected_range[0] + selected_range[1]) / 2, selected_range[1]
    if lower <= size_kb <= mid:
        size_class_thirds = "Lower"
    elif mid < size_kb <= upper:
        size_class_thirds = "Mid"
    else:
        size_class_thirds = "Upper"

    return f"{size_kb:.2f}", size_class_range, size_class_thirds

# Function to generate a random file type based on text size
def generate_file_type(text_size):
    # Determine file type based on text size
    if text_size < 100:  # Smaller text sizes
        file_types = ["msg", "doc"]
    else:  # Larger text sizes
        file_types = ["excel", "pdf"]
    return random.choice(file_types)

# Initialize an empty list to store the data
data = []

# Get the number of records from the user
num_records = int(input("Enter the number of documents to generate: "))

# Generate data for each document
for i in range(1, num_records + 1):
    document_id = i
    text_size, size_class_range, size_class_thirds = generate_text_size()
    file_type = generate_file_type(float(text_size.split()[0]))  # Extract size in KB for file type decision
    data.append([document_id, text_size, size_class_range, size_class_thirds, file_type])

# Specify the CSV file path
csv_file = "documents_dataset.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Document ID", "Text Size", "Size Classification (Range)", "Size Classification (Thirds)", "File Type"])  # Write header row
    writer.writerows(data)

print(f"Dataset with {num_records} documents saved as {csv_file}")