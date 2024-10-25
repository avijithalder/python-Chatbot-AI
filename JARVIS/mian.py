from JARVIS.browser import browseropen
from jarvis import listen, say
import datetime
import os
import wikipedia
from google import search
from responses import responses


# Function to handle chatbot responses
def chatbot_response(task):

    # Ensure the task is a valid command
    task = task.replace("chatbot", "").strip()
    response = responses.get(task, "Sorry, I didn't understand that.")
    return response


def mfx(fx):
    def ifx():
        try:
            fx()
        except ValueError as e:
            say(f"Invalid argument error: {str(e)}")
        except Exception as e:
            say(f"Sorry, an error occurred: {str(e)}")

    return ifx


@mfx
def main():
    print(
        # "Search on Internet\n"
        #   "Open on Browser\n"
        #   "Wikipedia\n"
        #   "Application\n"
        #   "Music\n"
        #   "Time\n"
        #   "Weather\n"
        "Chatbot")

    task = listen().lower().strip()  # Convert input to lowercase and remove extra spaces
    print(f"Received command: {task}")  # Debug print to see the exact command received

    if "browser"in task:
        result = browseropen(task)
        say(result)
    elif "time" in task:
        dt = datetime.datetime.now().strftime("%H O'Clock and %M Minutes")
        say(f"Time is {dt}")
    elif "code" in task:
        try:
            os.startfile("C:/Users/Mohit Prajapat/AppData/Local/Programs/Microsoft VS Code/Code.exe")
        except FileNotFoundError:
            say("The application could not be found.")
    elif "music" in task:
        try:
            os.startfile("link.mp3")
        except FileNotFoundError:
            say("The music file could not be found.")
    elif "wikipedia" in task:
        task = task.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(task, sentences=2)
            print(result)
            say(result)
        except wikipedia.exceptions.DisambiguationError as e:
            say(f"Disambiguation error: {str(e)}")
        except wikipedia.exceptions.PageError:
            say("Page not found on Wikipedia.")
    elif "search" in task:
        query = task.replace("search", "").strip()
        try:
            result = search(query)
            say(result)
        except Exception as e:
            say(f"Search error: {str(e)}")
    elif "weather" in task:
        try:
            # Open the Windows Weather app
            os.startfile("msnweather:")
            say("Weather app opened successfully.")
        except Exception as e:
            say(f"Error opening Weather app: {e}")
    elif "chatbot" in task:
        # Handle chatbot interaction
        response = chatbot_response(task)
        say(response)
    else:
        say("Sorry, I didn't understand that command. Please try again.")


while True:
    main()
    say("Is there anything else, Sir?")
    # Wait for a short time before repeating the loop to avoid rapid requests
    import time

    time.sleep(2)
