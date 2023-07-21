import json

def update_figure_prices(data, figure_name, price, price_per_meter, price_for_workers):
    def update_figure(figure_list, figure_name, price, price_per_meter, price_for_workers):
        for figure in figure_list:
            if figure['name'] == figure_name:
                figure['price'] = [price]
                figure['price_per_meter'] = [price_per_meter]
                figure['price_for_workers'] = [price_for_workers]
                return True
        return False

    updated = False

    for _, answers in data['answers']['Yes']['answers']['Yes']['answers']['Yes']['answers']['Werken naast de rijbaan']['answers'].items():
        for figures_data in answers.values():
            updated = update_figure(figures_data['figures'], figure_name, price, price_per_meter, price_for_workers)
            if updated:
                break

    return updated, data

def main():
    # Load JSON data from file
    with open('questionnaire_with_price_fig.json', 'r') as file:
        data = json.load(file)

    while True:
        figure_name = input("Which Figure should be impacted (e.g., 1321d): ")
        price = int(input("What is the price on installation and deinstallation: "))
        price_per_meter = int(input("What is the price per meter: "))
        price_for_workers = int(input("What is the price for workers: "))

        updated, data = update_figure_prices(data, figure_name, price, price_per_meter, price_for_workers)

        if updated:
            print(f"\nUpdated prices for Figure {figure_name}:")
            print(f"Price: {price}")
            print(f"Price per meter: {price_per_meter}")
            print(f"Price for workers: {price_for_workers}")
        else:
            print(f"\nFigure {figure_name} not found. Please try again.")

        another_update = input("\nDo you want to update another Figure? (yes/no): ").lower()
        if another_update != 'yes':
            break

    # Save the updated JSON data to a file
    with open('questionnaire_with_price_fig_u.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()
