import json
import os

FIGURE_DIRECTORY = "/Users/yehorfurtsev/PycharmProjects/questionnaire-main/public/fig"

def find_matching_figures(figure):
    figure_prefix = figure.rstrip('0123456789')
    matching_figures = []

    for file_name in os.listdir(FIGURE_DIRECTORY):
        if file_name.startswith(figure_prefix):
            matching_figures.append(file_name.rstrip('.jpeg'))

    return matching_figures

def add_additional_keys(node):
    if "answers" in node:
        for key, value in node["answers"].items():
            add_additional_keys(value)

            if "result" in value:
                result = value["result"]
                figures = [figure.strip() for figure in result.split(",")]
                price = [0] * len(figures)
                price_per_meter = [0] * len(figures)
                price_for_workers = [0] * len(figures)
                figure_paths = []

                for figure in figures:
                    figure_path = os.path.join(FIGURE_DIRECTORY, f"{figure}.jpeg")
                    if os.path.isfile(figure_path):
                        figure_paths.append(figure_path)
                        index = figures.index(figure)
                        price[index] = 0
                        price_per_meter[index] = 0
                        price_for_workers[index] = 0
                    else:
                        matching_figures = find_matching_figures(figure)
                        if matching_figures:
                            for matching_figure in matching_figures:
                                matching_figure_path = os.path.join(FIGURE_DIRECTORY, f"{matching_figure}.jpeg")
                                if os.path.isfile(matching_figure_path):
                                    figure_paths.append(matching_figure_path)
                                    price.append(0)
                                    price_per_meter.append(0)
                                    price_for_workers.append(0)

                node["answers"][key]["result"] = ", ".join(figures + matching_figures)
                node["answers"][key]["price"] = price
                node["answers"][key]["price_per_meter"] = price_per_meter
                node["answers"][key]["price_for_workers"] = price_for_workers
                node["answers"][key]["figures"] = figure_paths

    return node

# Load the initial JSON data
with open("questionnaire_with_choice.json") as file:
    data = json.load(file)

# Modify the JSON structure and add additional keys
updated_data = add_additional_keys(data)

# Save the updated JSON data
with open("questionnaire_with_price_fig.json", "w") as file:
    json.dump(updated_data, file, indent=4)
