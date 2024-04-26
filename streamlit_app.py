
import json

def read_file(file_path):
    """Read data from a file and return a set of values."""
    with open(file_path, 'r') as file:
        data = {line.strip() for line in file}
    return data

def write_difference(file_path, data_difference):
    """Write the sorted difference data to a new file."""
    with open(file_path, 'w') as file:
        for value in sorted(data_difference):
            file.write(f"{value}\n")

def extract_values_from_json(json_file_path, output_file_path):
    """Extract values from a JSON file and write them to a text file."""
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    with open(output_file_path, 'w') as output_file:
        for entry in data:
            value = entry["string_list_data"][0]["value"]
            output_file.write(f"{value}\n")

    print(f"Values have been written to '{output_file_path}'")

def compare_and_print(old_list_path, new_list_path, output_path):
    """Compare two lists and print values only present in the new list."""
    old_list = read_file(old_list_path)
    new_list = read_file(new_list_path)

    # Find values only present in the new list
    unique_values = new_list - old_list

    # Write the unique values to the output file
    with open(output_path, 'w') as output_file:
        for value in sorted(unique_values):
            output_file.write(f"{value}\n")

    print(f"Unique values present in 'new list' and not in 'old list' have been written to '{output_path}'")

# Specify paths
following_json_path = 'C:\Kanak\Unfollowers+\Insta Data\following.json'
followers_json_path = 'C:\Kanak\Unfollowers+\Insta Data\followers_1.json'
following_text_path = 'C:\Kanak\Unfollowers+\Insta Data\Following.txt'
followers_text_path = 'C:\Kanak\Unfollowers+\Insta Data\Followers.txt'
following_not_in_followers_path = r'C:\Kanak\Unfollowers+\Insta Data\following_not_in_followers.txt'
old_list_path = 'C:\Kanak\Unfollowers+\Insta Data\New 12\following_not_in_followers.txt'
new_list_path = 'C:\Kanak\Unfollowers+\Insta Data\following_not_in_followers.txt'
output_difference_path = 'C:\Kanak\Unfollowers+\Insta Data\Difference.txt'

# Extract values from JSON files and write to text files
extract_values_from_json(following_json_path, following_text_path)
extract_values_from_json(followers_json_path, followers_text_path)

# Compare the "new list" with the "old list"
compare_and_print(old_list_path, new_list_path, output_difference_path)

# Read data from followers and following files
followers_data = read_file(followers_text_path)
following_data = read_file(following_text_path)

# Find data present in following but not in followers
following_not_in_followers = following_data - followers_data

# Write the difference to a new file
write_difference(following_not_in_followers_path, following_not_in_followers)

print(f"Data in 'following' but not in 'followers' has been written to '{following_not_in_followers_path}'")
