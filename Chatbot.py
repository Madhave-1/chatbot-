from datetime import datetime
import os

# Helper function to get the desktop path
def get_desktop_path():
    # For Windows
    if os.name == 'nt':
        return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    # For macOS and Linux
    else:
        return os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

# Helper functions
def get_current_date_time():
    return datetime.now().strftime("%d %B %Y, %I:%M %p")

def process_list_operations(user_input):
    try:
        numbers = list(map(int, user_input.split(',')))
    except ValueError:
        return "Error: The list must contain integers only, separated by commas."

    sum_numbers = sum(numbers)
    max_number = max(numbers)
    reversed_list = numbers[::-1]

    response = f"Sum: {sum_numbers}\nMaximum: {max_number}\nReversed List: {reversed_list}"
    return response

def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

def save_summary(summary):
    desktop_path = get_desktop_path()
    filename = os.path.join(desktop_path, f"summary_{datetime.now().strftime('%d%m%Y')}.txt")
    with open(filename, 'w') as file:
        file.write(summary)
    return filename

# Main chatbot function
def chatbot():
    chat_history = []
    commands_used = {}

    print("Chatbot: Hello! I’m your assistant! How can I help you today?")
    chat_history.append("Chatbot: Hello! I’m your assistant! How can I help you today?")

    while True:
        user_input = input("User: ").strip().lower()
        chat_history.append(f"User: {user_input}")

        if user_input in ["hello", "hi"]:
            print("Chatbot: Hi there! How can I help you today?")
            chat_history.append("Chatbot: Hi there! How can I help you today?")
        elif "date" in user_input or "time" in user_input:
            print(f"Chatbot: {get_current_date_time()}")
            chat_history.append(f"Chatbot: {get_current_date_time()}")
            print("Chatbot: How else can I assist you?")
            chat_history.append("Chatbot: How else can I assist you?")
        elif "list operations" in user_input:
            print("Chatbot: Please enter a list of integers (comma-separated):")
            chat_history.append("Chatbot: Please enter a list of integers (comma-separated):")
            list_input = input("User: ").strip()
            chat_history.append(f"User: {list_input}")
            list_response = process_list_operations(list_input)
            print(f"Chatbot: {list_response}")
            chat_history.append(f"Chatbot: {list_response}")
            if "Sum:" in list_response:
                print("Chatbot: Would you like to remove duplicates? (yes/no)")
                chat_history.append("Chatbot: Would you like to remove duplicates? (yes/no)")
                remove_dup = input("User: ").strip().lower()
                chat_history.append(f"User: {remove_dup}")
                if remove_dup == "yes":
                    numbers = list(map(int, list_input.split(',')))
                    unique_numbers = remove_duplicates(numbers)
                    print(f"Chatbot: Updated List: {unique_numbers}")
                    chat_history.append(f"Chatbot: Updated List: {unique_numbers}")
            print("Chatbot: How else can I assist you?")
            chat_history.append("Chatbot: How else can I assist you?")
        elif "generate prime" in user_input:
            print("Chatbot: Enter the range (start and end, comma-separated):")
            chat_history.append("Chatbot: Enter the range (start and end, comma-separated):")
            range_input = input("User: ").strip()
            chat_history.append(f"User: {range_input}")
            try:
                start, end = map(int, range_input.split(','))
                primes = generate_primes(start, end)
                print(f"Chatbot: Prime Numbers: {primes}")
                chat_history.append(f"Chatbot: Prime Numbers: {primes}")
            except ValueError:
                print("Chatbot: Error: The range must contain two integers, separated by commas.")
                chat_history.append("Chatbot: Error: The range must contain two integers, separated by commas.")
            print("Chatbot: How else can I assist you?")
            chat_history.append("Chatbot: How else can I assist you?")
        elif "search history" in user_input:
            print("Chatbot: Enter the keyword to search in chat history:")
            chat_history.append("Chatbot: Enter the keyword to search in chat history:")
            keyword = input("User: ").strip().lower()
            chat_history.append(f"User: {keyword}")
            found_lines = [line for line in chat_history if keyword in line.lower()]
            if found_lines:
                print("Chatbot: Found the following lines:")
                for line in found_lines:
                    print(f"    - {line}")
                chat_history.append("Chatbot: Found the following lines:")
                chat_history.extend(found_lines)
            else:
                print("Chatbot: No matching lines found.")
                chat_history.append("Chatbot: No matching lines found.")
            print("Chatbot: How else can I assist you?")
            chat_history.append("Chatbot: How else can I assist you?")
        elif "bye" in user_input:
            summary = f"Commands Used: {len(commands_used)}\nMost Frequent Command: {max(commands_used, key=commands_used.get, default='None')}"
            print(f"Chatbot: Here’s a summary of your session:\n{summary}")
            chat_history.append(f"Chatbot: Here’s a summary of your session:\n{summary}")
            print("Chatbot: Do you want to save this summary? (yes/no)")
            chat_history.append("Chatbot: Do you want to save this summary? (yes/no)")
            save_input = input("User: ").strip().lower()
            chat_history.append(f"User: {save_input}")
            if save_input == "yes":
                filename = save_summary(summary)
                print(f"Chatbot: Summary saved to {filename}")
                chat_history.append(f"Chatbot: Summary saved to {filename}")
            print("Chatbot: Bye, have a good day!!")
            chat_history.append("Chatbot: Bye, have a good day!!")
            break
        else:
            print("Chatbot: Enter correct keyword")
            chat_history.append("Chatbot: Enter correct keyword")

        # Track commands used
        if user_input in commands_used:
            commands_used[user_input] += 1
        else:
            commands_used[user_input] = 1

# Run the chatbot
if __name__ == "__main__":
    chatbot()