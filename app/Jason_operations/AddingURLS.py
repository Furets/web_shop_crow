import json

# Load the fig_to_url.json file
with open("fig_to_url.json", "r") as file:
    fig_to_url = json.load(file)

# Load the questionnaire_with_choice_URLs.json file
with open("questionnaire_with_choice_URLs.json", "r") as file:
    questionnaire_data = json.load(file)

# Helper function to find URLs for the given Fig. values
def find_urls(fig_values):
    urls = []
    for fig in fig_values:
        if fig in fig_to_url:
            urls.append(fig_to_url[fig])
    return urls

# Recursive function to update the questionnaire data
def update_questionnaire(data):
    if "result" in data:
        result = data["result"]
        fig_values = [fig.strip() for fig in result.split(",")]
        urls = find_urls(fig_values)
        data["URLs"] = urls
    if "answers" in data:
        for answer in data["answers"].values():
            update_questionnaire(answer)

# Update the questionnaire data
update_questionnaire(questionnaire_data)

# Save the updated questionnaire_with_choice_URLs.json file
with open("questionnaire_with_choice_URLs.json", "w") as file:
    json.dump(questionnaire_data, file, indent=4)
