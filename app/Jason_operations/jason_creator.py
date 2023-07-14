import json

def create_question():
    question = input("Enter the question: ")
    question_type = input("What type of question is it? Yes/No (Y/N) or multiple choice (M)? ").upper()

    if question_type == "Y":
        return create_yes_no_question(question)
    elif question_type == "M":
        num_choices = int(input("How many choices are there? "))
        return create_multiple_choice_question(question, num_choices)
    else:
        print("Invalid input. Please try again.")
        return create_question()

def create_yes_no_question(question):
    yes_result_type = input(f"Does the 'Yes' branch lead to a result (R) or another question (Q) for '{question}'? ").upper()

    if yes_result_type == "R":
        yes_result = input(f"For '{question}' enter the result for 'Yes': ")
        yes_branch = {"result": yes_result}
    elif yes_result_type == "Q":
        yes_branch = create_question()
    else:
        print("Invalid input. Please try again.")
        return create_yes_no_question(question)

    no_result_type = input(f"Does the 'No' branch lead to a result (R) or another question (Q) for '{question}'? ").upper()

    if no_result_type == "R":
        no_result = input(f"For '{question}' enter the result for 'No': ")
        no_branch = {"result": no_result}
    elif no_result_type == "Q":
        no_branch = create_question()
    else:
        print("Invalid input. Please try again.")
        return create_yes_no_question(question)

    return {
        "question": question,
        "answers": {
            "Yes": yes_branch,
            "No": no_branch
        }
    }

def create_multiple_choice_question(question, num_choices):
    choices = {}
    for i in range(num_choices):
        choice = input(f"Enter choice {i+1}: ")
        choice_result_type = input(f"Does choice '{choice}' lead to a result (R) or another question (Q) for '{question}'? ").upper()

        if choice_result_type == "R":
            choice_result = input(f"Enter the result for choice '{choice}' for '{question}': ")
            choices[choice] = {"result": choice_result}
        elif choice_result_type == "Q":
            choices[choice] = create_question()
        else:
            print("Invalid input. Please try again.")
            return create_multiple_choice_question(question, num_choices)

    return {
        "question": question,
        "answers": choices
    }

questionnaire = create_question()

with open("updated_questionnaire.json", "w") as file:
    json.dump(questionnaire, file, indent=4)

print("Questionnaire created and saved as 'questionnaire_with_choice_URLs.json'.")
