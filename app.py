import threading
from functions.speech2text import _interact
from rich.console import Console


console = Console()

# initial message
_interact("""
start a conversation with the user now.
""")

# main app entry point
while True:
    # get user input
    user_input = input("You: ")
    console.print("Loading...", style="bold blue")
    
    # call the _interact function in a new thread
    threading.Thread(target=_interact, args=(user_input,)).start()