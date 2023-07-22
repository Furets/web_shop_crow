import json

def find_figure_by_name(data, figure_name):
    for key, value in data.items():
        if isinstance(value, dict):
            if "figures" in value:
                for figure in value["figures"]:
                    if figure["name"] == figure_name:
                        return figure
            else:
                result = find_figure_by_name(value, figure_name)
                if result is not None:
                    return result
    return None

def update_figure_prices(data):
    # Step 2: Get user input for the figure name
    figure_name = input("Enter the figure name (e.g., Fig. 1301a): ")

    # Step 3: Find the figure based on the figure name
    figure = find_figure_by_name(data, figure_name)
    if figure is None:
        print(f"Figure '{figure_name}' not found in the JSON data.")
        return

    # Step 4: Get user input for the new prices
    new_price = input("Enter the new price (leave empty to skip): ")
    new_price_per_meter = input("Enter the new price per meter (leave empty to skip): ")
    new_price_for_workers = input("Enter the new price for workers (leave empty to skip): ")

    # Step 5: Update the figure prices
    figure["result"] = "Result"  # You can modify this if necessary

    if new_price.strip():
        figure["price"] = [int(new_price)] + [0] * (len(figure["price"]) - 1)

    if new_price_per_meter.strip():
        figure["price_per_meter"] = [int(new_price_per_meter)] + [0] * (len(figure["price_per_meter"]) - 1)

    if new_price_for_workers.strip():
        figure["price_for_workers"] = [int(new_price_for_workers)] + [0] * (len(figure["price_for_workers"]) - 1)

# Step 1: Load the JSON data from the file
file_path = 'questionnaire_with_price_fig.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Step 6: Execute the update_figure_prices function
update_figure_prices(data)

# Step 7: Write the updated data back to the file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

# Step 8: Print a message indicating successful update
print("Figure prices have been updated and saved to the file.")
