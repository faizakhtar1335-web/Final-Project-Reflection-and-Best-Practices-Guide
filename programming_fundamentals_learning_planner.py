"""
Programming Fundamentals: Learning Progress and Study Planner
-------------------------------------------------------------
A beginner-friendly command-line project demonstrating:
- variables and data types
- lists and dictionaries
- functions
- loops and conditional statements
- input validation
- simple summaries and progress tracking

Run:
    python programming_fundamentals_learning_planner.py
"""

weekly_tasks = [
    {
        "week": "Week 1",
        "topic": "Programming fundamentals and project planning",
        "lesson": "Break a problem into smaller steps and define requirements.",
        "status": "Completed",
    },
    {
        "week": "Week 2",
        "topic": "Basic Python concepts and implementation planning",
        "lesson": "Use variables, data types, conditions, loops, and functions.",
        "status": "Completed",
    },
    {
        "week": "Week 3",
        "topic": "Code review, quality assurance, and development roadmap",
        "lesson": "Test small pieces, review logic, and plan work in stages.",
        "status": "Completed",
    },
    {
        "week": "Week 4",
        "topic": "Debugging and code improvement",
        "lesson": "Read error messages, reproduce bugs, and improve carefully.",
        "status": "Completed",
    },
    {
        "week": "Week 5",
        "topic": "Final reflection and programming best practices",
        "lesson": "Reflect on progress and create a repeatable learning routine.",
        "status": "Completed",
    },
]

personal_goals = []


def show_menu():
    """Display the available actions."""
    print("\\n" + "=" * 55)
    print(" PROGRAMMING FUNDAMENTALS - LEARNING PLANNER")
    print("=" * 55)
    print("1. View internship learning journey")
    print("2. View programming best practices")
    print("3. Add a personal learning goal")
    print("4. View personal learning goals")
    print("5. Show study recommendations")
    print("6. Exit")


def show_learning_journey():
    """Print the topics and lessons from each internship week."""
    print("\\nYOUR FIVE-WEEK LEARNING JOURNEY")
    print("-" * 55)
    for task in weekly_tasks:
        print(f"{task['week']}: {task['topic']}")
        print(f"  Status: {task['status']}")
        print(f"  Key lesson: {task['lesson']}")
        print()


def show_best_practices():
    """Present practical advice for beginner programmers."""
    practices = [
        ("Start with the problem",
         "Write down the expected input, process, and output before coding."),
        ("Break work into small steps",
         "Build one feature at a time and test it before adding another."),
        ("Use meaningful names",
         "Choose names such as total_price instead of unclear names such as x."),
        ("Keep code readable",
         "Use consistent indentation, spacing, and short explanatory comments."),
        ("Test normal and unusual inputs",
         "Try valid values, empty input, incorrect types, and boundary values."),
        ("Learn from error messages",
         "Read the traceback from the bottom, locate the relevant line, and test a fix."),
        ("Use version control",
         "Save meaningful checkpoints so changes can be reviewed or reversed."),
        ("Practise consistently",
         "Short daily practice is more effective than irregular long sessions."),
        ("Ask focused questions",
         "Share the error, expected result, actual result, and a small code example."),
        ("Review and reflect",
         "Record what worked, what failed, and what you will try next."),
    ]

    print("\\nBEST PRACTICES FOR BEGINNERS")
    print("-" * 55)
    for number, (title, explanation) in enumerate(practices, start=1):
        print(f"{number}. {title}")
        print(f"   {explanation}")


def add_goal():
    """Collect and store one learning goal."""
    goal = input("\\nEnter a learning goal: ").strip()
    if not goal:
        print("Goal cannot be empty. Please try again.")
        return

    personal_goals.append({"goal": goal, "completed": False})
    print("Your goal has been saved for this session.")


def view_goals():
    """Show goals added during the current program session."""
    print("\\nYOUR PERSONAL LEARNING GOALS")
    print("-" * 55)
    if not personal_goals:
        print("No goals added yet. Choose option 3 to add one.")
        return

    for index, item in enumerate(personal_goals, start=1):
        status = "Completed" if item["completed"] else "In progress"
        print(f"{index}. {item['goal']} - {status}")


def show_recommendations():
    """Give the learner a practical weekly routine."""
    recommendations = [
        "Choose one small topic, such as loops or functions.",
        "Read or watch one short explanation from a reliable source.",
        "Write a tiny example without copying it line by line.",
        "Change the example and predict what the program will do.",
        "Test at least three inputs, including an unusual one.",
        "Write down one mistake and how you corrected it.",
        "Save your work and review it at the end of the week.",
    ]

    print("\\nA SIMPLE WEEKLY PRACTICE ROUTINE")
    print("-" * 55)
    for step, recommendation in enumerate(recommendations, start=1):
        print(f"{step}. {recommendation}")


def main():
    """Run the menu until the learner chooses to exit."""
    print("Welcome! Use this program to review your learning journey.")
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_learning_journey()
        elif choice == "2":
            show_best_practices()
        elif choice == "3":
            add_goal()
        elif choice == "4":
            view_goals()
        elif choice == "5":
            show_recommendations()
        elif choice == "6":
            print("\\nThank you for using the Learning Planner. Keep practising!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
