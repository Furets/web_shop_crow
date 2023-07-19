import json

def update_json_figure(json_data, figure_name, price_key, new_price):
    for key, value in json_data.items():
        if isinstance(value, dict):
            if "figures" in value and isinstance(value["figures"], list):
                for figure in value["figures"]:
                    if figure.get("name") == figure_name:
                        if price_key in value:
                            value[price_key] = [new_price]
                        break
            update_json_figure(value, figure_name, price_key, new_price)

# Load the JSON file
with open("questionnaire_with_price_fig.json", "r") as file:
    json_data = json.load(file)

# User input
figure_name = input("Please enter the figure that you want to update: ")
price_key = input("Which price key do you want to change? (e.g., price_per_meter, price_for_workers): ")
new_price = int(input("What is the new price?: "))

# Update the JSON data
update_json_figure(json_data, figure_name, price_key, new_price)

# Save the updated JSON data
with open("updated_questionnaire.json", "w") as file:
    json.dump(json_data, file, indent=4)
