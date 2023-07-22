import json

def find_figure_by_name(data, figure_name):
    if isinstance(data, dict):
        if "name" in data and data["name"].lower() == figure_name:
            return data
        for key, value in data.items():
            result = find_figure_by_name(value, figure_name)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_figure_by_name(item, figure_name)
            if result is not None:
                return result
    return None

def find_keys(d, value, path=None):
    if path is None:
        path = []

    found_keys = []

    for k, v in d.items():
        new_path = path + [k]

        if isinstance(v, dict):
            found_keys.extend(find_keys(v, value, new_path))
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict) and item == value:
                    found_keys.append(new_path)

    return found_keys

def find_place_of_the_figure(data,keys):
    i = 0
    while i < len(keys):
        data = data[keys[i]]
        i = i +1
    return data


def update_figure_prices(data):
    # Step 2: Get user input for the figure name
    figure_name = input("Enter the figure name (e.g., Fig. 1301a): ").strip().lower()

    # Step 3: Find the figure based on the figure name
    figure = find_figure_by_name(data, figure_name)
    if figure is None:
        print(f"Figure '{figure_name}' not found in the JSON data.")
        return

    R = find_keys(data,figure)


    # Step 4: Get user input for the new prices
    new_price = input("Enter the new price (montage+demontage): ")
    new_price_per_meter = input("Enter the new price per meter: ")
    new_price_for_workers = input("Enter the new price for worker hour: ")

    for i in range(len(R)):
        index_of_target = None
        for j, S_figure in enumerate(find_place_of_the_figure(data,R[i])):
            if S_figure == figure:
                index_of_target = j
                break
        # Step 5: Update the figure prices
        find_place_of_the_figure(data,R[i][:-1])["price"][index_of_target] = int(new_price)
        find_place_of_the_figure(data,R[i][:-1])["price_per_meter"][index_of_target] = int(new_price_per_meter)
        find_place_of_the_figure(data,R[i][:-1])["price_for_workers"][index_of_target] = int(new_price_for_workers)

def main():
    # Step 1: Load the JSON data from the file
    file_path = './questionnaire_with_price_fig.json'
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Step 6: Execute the update_figure_prices function
    update_figure_prices(data)

    # Step 7: Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    # Step 8: Print a message indicating successful update
    print("Figure prices have been updated and saved to the file.")

if __name__ == "__main__":
    main()
