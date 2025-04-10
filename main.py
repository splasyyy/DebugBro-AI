import openai
import random
import os

# Set your OpenAI API key here
openai.api_key = "your_openai_api_key"

# Predefined motivational messages
motivational_messages = [
    "Believe in yourself, engineer! You've got this!",
    "Every bug you squash brings you closer to greatness.",
    "Failure is a step toward success. Keep going!",
    "Debugging is just problem-solving in disguise.",
    "Stay curious, stay building."
]

def generate_response(prompt):
    try:
        # Make a request to OpenAI API for text generation using the new ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use gpt-4 as well if you have access
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def translate(text, to_language):
    return f"(Translation to {to_language} not available offline – feature placeholder)"

def compare_results(old, new):
    try:
        old_val = float(old.strip('%'))
        new_val = float(new.strip('%'))
        diff = new_val - old_val
        trend = "increased" if diff > 0 else "decreased"
        return f"Your performance has {trend} by {abs(diff)}%."
    except:
        return "Invalid input. Please use percentage format (e.g., 85%, 90%)."

def get_user_info():
    name = input("What's your name? ")
    return name

def show_commands():
    print("\nHere are the things I can help you with:")
    print("1. Ask for a motivational message: Type 'motivate'")
    print("2. Translate text: Type 'translate'")
    print("3. Compare results: Type 'compare'")
    print("4. Ask about a hardware or software problem: Type 'hardware' or 'software'")
    print("5. Get help with a specific engineering query: Type any other command")
    print("Type 'exit' to quit the program.")

def main():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Change terminal color to green (Windows command prompt specific)
    if os.name == 'nt':
        os.system('color 0a')

    print("👋 Welcome to DebugBro – your friendly AI Engineering Assistant!")
    name = get_user_info()

    # Show the available commands
    show_commands()

    while True:
        command = input("\nType a command (or type 'exit' to quit): ").lower().strip()

        if command == "exit":
            print("Goodbye! Come back anytime if you need assistance!")
            break

        elif "motivate" in command:
            print(random.choice(motivational_messages))

        elif "translate" in command:
            text = input("Enter text to translate: ")
            lang = input("Translate to which language? ")
            print(translate(text, lang))

        elif "compare" in command:
            old = input("Previous result (e.g., 85%): ")
            new = input("New result (e.g., 90%): ")
            print(compare_results(old, new))

        elif "hardware" in command or "software" in command:
            issue_type = input(f"Is the problem hardware-related or software-related? ").lower()
            print(f"Understood, {name}. Let's address your {issue_type}-related problem.")
            print(generate_response(f"Please help with a {issue_type}-related problem"))

        else:
            print(f"{name}, here's what I found:")
            print(generate_response(command))

        # Show commands again after each interaction
        show_commands()

if __name__ == "__main__":
    main()
