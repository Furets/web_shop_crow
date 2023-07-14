import json

def find_unique_results(data, unique_results):
    if "result" in data:
        result = data["result"]
        results = result.split(", ")
        for res in results:
            if res.startswith("Fig."):
                unique_results[res] = True
    if "answers" in data:
        for answer in data["answers"].values():
            find_unique_results(answer, unique_results)

# Read the JSON file
with open("questionnaire_with_choice_URLs.json", "r") as file:
    questionnaire_data = json.load(file)

# Find unique "Fig." values
unique_results = {}
find_unique_results(questionnaire_data, unique_results)

# Print the unique "Fig." values
unique_fig_keys = sorted(unique_results.keys())
unique_fig_dict = {fig: index for index, fig in enumerate(unique_fig_keys, start=1)}

for fig, index in unique_fig_dict.items():
    print(f"Key {index}: {fig}")

with open("fig_to_url.json", "w") as file:
    json.dump(unique_fig_dict, file)