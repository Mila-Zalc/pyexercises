# Name: Mila Zalc
# Group: A

# 1. Input: The program reads scenarios from scenarios_A.csv. The columns contain a scenario, three options, their budget and reputation changes,and feedback. The changes are written as whole numbers, sometimes negative.
# 2. What happens: The program shows the day, the budget, the reputation, and the scenario. It shows options A, B, and C, then asks the player to choose one.It repeats the question if the choice is invalid.It applies the changes, shows the feedback, and checks if the game ends.
# 3. Output: It applies the changes, shows the feedback, and checks if the game ends. the title, and the best and worst moves. It adds the player's name, budget, reputation, title, and date to results.csv.
# 4. Possible problems and what the program does: Possible problems and what the program does:If the player types something other than A, B, or C, the game asks again. If the budget or reputation reaches zero or less, the game ends immediately. If reputation goes above 100, the program sets it back to 100.
# Feature chosen: Difficulty. The player chooses easy or hard at the start. Easy starts with 15,000 EUR; hard starts with 6,000 EUR. I chose it because the player can choose the game's difficulty.

# These tools will read the scenarios, shuffle them, and get today's date.
import csv
import os
import random
from datetime import date

# This function reads the scenarios from the CSV file.
def load_scenarios(filename):
    scenarios = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            option_a = (row["OptionA"], int(row["BudgetA"]),
                        int(row["ReputationA"]), row["FeedbackA"])
            option_b = (row["OptionB"], int(row["BudgetB"]),
                        int(row["ReputationB"]), row["FeedbackB"])
            option_c = (row["OptionC"], int(row["BudgetC"]),
                        int(row["ReputationC"]), row["FeedbackC"])

            scenarios.append(
                (row["Scenario"], option_a, option_b, option_c)
            )

    return scenarios

# This function asks the player to choose A, B, or C.
def get_player_choice(scenario):
    print("Situation:", scenario[0])
    print("A:", scenario[1][0])
    print("B:", scenario[2][0])
    print("C:", scenario[3][0])

    choice = input("Your choice (A, B or C): ").strip().upper()

    while choice not in ["A", "B", "C"]:
        choice = input("Please type A, B or C: ").strip().upper()

    if choice == "A":
        return scenario[1]
    elif choice == "B":
        return scenario[2]
    else:
        return scenario[3]

# This function applies the chosen option to the two gauges.
def apply_choice(budget, reputation, option):
    budget_change = option[1]
    reputation_change = option[2]

    budget = budget + budget_change
    reputation = min(100, reputation + reputation_change)

    print(option[3])
    print(f"Budget {budget_change:+} EUR, Reputation {reputation_change:+}")

    return budget, reputation

# This function chooses a title based on the final score.
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"

# This function starts the game and sets the starting values.
def main():
    player_name = input("Player name: ")

    difficulty = input("Choose easy or hard: ").strip().lower()
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Please type easy or hard: ").strip().lower()

    if difficulty == "easy":
        budget = 15000
    else:
        budget = 6000

    reputation = 50
    scenarios = load_scenarios("scenarios_A.csv")
    random.shuffle(scenarios)
    history = []

# This loop plays up to ten days and stops if the player is fired.
    fired_reason = None

    for day in range(1, 11):
        scenario = scenarios[day - 1]

        print(f"\n--- Day {day} ---")
        print(f"Budget: {budget} EUR | Reputation: {reputation}/100")

        option = get_player_choice(scenario)
        budget, reputation = apply_choice(budget, reputation, option)

        # Save the reputation change, day, and chosen action.
        history.append((option[2], day, option[0]))

        if budget <= 0:
            fired_reason = "budget"
            break

        if reputation <= 0:
            fired_reason = "reputation"
            break

# This block shows the final result and saves it.
    if fired_reason is not None:
        title = "Fired"
        print(f"Game over: your {fired_reason} reached zero or less.")
    else:
        final_score = reputation + budget // 200
        title = get_title(final_score)
        print("Quarter survived!")
        print(f"Final score: {final_score}")
        print(f"{player_name}, your title: {title}")

    print(f"Budget left: {budget} EUR | Reputation: {reputation}/100")

    best_move = max(history)
    worst_move = min(history)

    print(f"Best move: Day {best_move[1]}, {best_move[2]} ({best_move[0]:+})")
    print(f"Worst move: Day {worst_move[1]}, {worst_move[2]} ({worst_move[0]:+})")

    file_exists = os.path.exists("results.csv")

    with open("results.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Budget", "Reputation", "Title", "Date"])

        writer.writerow([player_name, budget, reputation, title, date.today()])

    print("Game saved in results.csv")

if __name__ == "__main__":
    main()
