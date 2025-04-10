from transformers import pipeline
import random

# Load the model
assistant = pipeline("text-generation", model="distilgpt2")

# Predefined motivational messages
motivational_messages = [
    "Believe in yourself, engineer! You've got this!",
    "Every bug you squash brings you closer to greatness.",
    "Failure is a step toward success. Keep going!",
    "Debugging is just problem-solving in disguise.",
    "Stay curious, stay building."
]

def generate_response(prompt):
    response = assistant(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    return response.strip()

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
    focus = input("What engineering field are you in? (e.g., software, electrical) ")
    return name, focus

def main():
    print("👋 Welcome to DebugBro – your friendly AI Engineering Assistant!")
    name, field = get_user_info()

    while True:
        command = input("\nType a command (or type 'exit' to quit): ").lower()

        if command == "exit":
            print("Goodbye!")
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

        else:
            print(f"{name}, here's what I found:")
            print(generate_response(command))

if __name__ == "__main__":
    main()
