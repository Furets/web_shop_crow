import json

# Load the JSON file
with open("fig_to_url.json", "r") as file:
    fig_to_url = json.load(file)

# Iterate over the keys and prompt for input URLs
for key in sorted(fig_to_url.keys()):
    url = input(f"Enter URL for {key}: ")
    fig_to_url[key] = url

# Save the updated dictionary as JSON
with open("fig_to_url.json", "w") as file:
    json.dump(fig_to_url, file)
