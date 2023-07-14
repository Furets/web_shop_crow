import json

# Read the JSON data from file
with open('fig_to_url.json', 'r') as file:
    data = json.load(file)

# Extract the "Fig." values from the JSON data
fig_values = [key for key in data.keys() if key.startswith('Fig.')]

# Prompt the user to input prices for each "Fig." value
prices = {}
for fig in fig_values:
    branch = {}
    print(f"Enter prices for {fig}:")
    branch["huur_dag"] = float(input("huur_dag: ").replace("€ ", "").replace(",", "."))
    branch["huur_week"] = float(input("huur_week: ").replace("€ ", "").replace(",", "."))
    branch["Montage"] = float(input("Montage: ").replace("€ ", "").replace(",", "."))
    branch["Demontage"] = float(input("Demontage: ").replace("€ ", "").replace(",", "."))
    prices[fig] = branch

# Update the JSON data with the prices
for fig, branch in prices.items():
    data[fig] = branch

# Write the updated JSON data back to file
with open('fig_to_prices.json', 'w') as file:
    json.dump(data, file, indent=4)
