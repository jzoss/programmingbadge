"""
🎱 Magic 8-Ball Demo
====================
Programming Merit Badge — Teaching Demonstration

This is a TEACHING EXAMPLE to walk through with Scouts.
Use this to show how programs work BEFORE they write their own.

HOW THIS WORKS:
  INPUT:       User types a question
  COMPUTATION: Generate a random number
  DECISIONS:   Pick an answer based on the number
  OUTPUT:      Show the Magic 8-Ball's response
"""

# ============================================================
# STEP 1: IMPORT TOOLS
# ============================================================
# Python has built-in "modules" with extra functionality.
# We need the "random" module to pick random numbers.

import random


# ============================================================
# STEP 2: SHOW WELCOME MESSAGE (OUTPUT)
# ============================================================

def show_welcome():
    """
    Display the welcome banner.
    This is an example of OUTPUT — showing information to the user.
    """
    print("=" * 50)
    print("       🎱  MAGIC 8-BALL  🎱")
    print("   Programming Merit Badge Demo")
    print("=" * 50)
    print()
    print("Ask me any yes/no question, and I'll give you an answer!")
    print()


# ============================================================
# STEP 3: GET INPUT FROM THE USER
# ============================================================

def get_question():
    """
    Ask the user for a question.
    This is an example of INPUT — getting data from the user.
    
    Returns:
        The question the user typed (a string)
    """
    question = input("🤔 Your question: ")
    return question


# ============================================================
# STEP 4: COMPUTATION — Generate Random Number
# ============================================================

def shake_the_ball():
    """
    "Shake" the Magic 8-Ball by picking a random number.
    This is an example of COMPUTATION — the computer does math/calculations.
    
    Returns:
        A random number between 1 and 20
    """
    print()
    print("*shaking the Magic 8-Ball...*")
    print()
    
    # Pick a random integer (whole number) from 1 to 20
    random_number = random.randint(1, 20)
    
    return random_number


# ============================================================
# STEP 5: DECISIONS — Pick Answer Based on Number
# ============================================================

def get_answer(random_number):
    """
    Use DECISIONS (if/elif/else) to pick an answer based on the random number.
    
    This is the most important part to show Scouts!
    The program makes DECISIONS based on the data.
    
    Args:
        random_number: A number from 1-20
        
    Returns:
        The Magic 8-Ball's answer (a string)
    """
    
    # DECISION LADDER:
    # Check the number and decide what answer to give.
    
    # Positive answers (1-10)
    if random_number == 1:
        answer = "✅ Yes, definitely!"
    elif random_number == 2:
        answer = "✅ It is certain."
    elif random_number == 3:
        answer = "✅ Without a doubt."
    elif random_number == 4:
        answer = "✅ You may rely on it."
    elif random_number == 5:
        answer = "✅ As I see it, yes."
    elif random_number == 6:
        answer = "✅ Most likely."
    elif random_number == 7:
        answer = "✅ Outlook good."
    elif random_number == 8:
        answer = "✅ Yes."
    elif random_number == 9:
        answer = "✅ Signs point to yes."
    elif random_number == 10:
        answer = "✅ Absolutely!"
    
    # Non-committal answers (11-15)
    elif random_number == 11:
        answer = "🤷 Reply hazy, try again."
    elif random_number == 12:
        answer = "🤷 Ask again later."
    elif random_number == 13:
        answer = "🤷 Better not tell you now."
    elif random_number == 14:
        answer = "🤷 Cannot predict now."
    elif random_number == 15:
        answer = "🤷 Concentrate and ask again."
    
    # Negative answers (16-20)
    elif random_number == 16:
        answer = "❌ Don't count on it."
    elif random_number == 17:
        answer = "❌ My reply is no."
    elif random_number == 18:
        answer = "❌ My sources say no."
    elif random_number == 19:
        answer = "❌ Outlook not so good."
    elif random_number == 20:
        answer = "❌ Very doubtful."
    
    # This should never happen (safety check)
    else:
        answer = "❓ Error: Unknown number!"
    
    return answer


# ============================================================
# STEP 6: DISPLAY OUTPUT
# ============================================================

def show_answer(answer):
    """
    Display the Magic 8-Ball's answer.
    This is more OUTPUT — showing the result to the user.
    """
    print("🎱 Magic 8-Ball says:")
    print()
    print("     " + answer)
    print()


# ============================================================
# STEP 7: ASK IF THEY WANT TO PLAY AGAIN
# ============================================================

def play_again():
    """
    Ask if the user wants to ask another question.
    This shows INPUT again, and we use a DECISION to check their answer.
    
    Returns:
        True if they want to play again, False if not
    """
    response = input("Ask another question? (yes/no): ").lower().strip()
    
    # DECISION: Check what they typed
    if response == "yes" or response == "y":
        return True
    else:
        return False


# ============================================================
# MAIN PROGRAM — This is where everything runs!
# ============================================================

def main():
    """
    Main function — runs the Magic 8-Ball program.
    
    THIS IS WHAT THE FLOW LOOKS LIKE:
    1. Show welcome (OUTPUT)
    2. Loop:
       a. Get question (INPUT)
       b. Shake ball / pick random number (COMPUTATION)
       c. Decide answer based on number (DECISIONS)
       d. Show answer (OUTPUT)
       e. Ask if they want to continue (INPUT + DECISION)
    3. Say goodbye (OUTPUT)
    """
    
    # Step 1: Show the welcome screen
    show_welcome()
    
    # Step 2: Keep looping until they want to stop
    keep_playing = True
    
    while keep_playing:
        # Get their question (INPUT)
        question = get_question()
        
        # Shake the ball and get a random number (COMPUTATION)
        random_number = shake_the_ball()
        
        # Make a DECISION about which answer to give
        answer = get_answer(random_number)
        
        # Show the answer (OUTPUT)
        show_answer(answer)
        
        print("-" * 50)
        print()
        
        # Ask if they want to continue (INPUT + DECISION)
        keep_playing = play_again()
        
        print()
    
    # Step 3: Say goodbye (OUTPUT)
    print("=" * 50)
    print("Thanks for consulting the Magic 8-Ball! 🎱")
    print("=" * 50)


# ============================================================
# START THE PROGRAM
# ============================================================

# This line means "if someone runs this file directly, start the main() function"
if __name__ == "__main__":
    main()


# ============================================================
# TEACHING TIPS FOR COUNSELORS
# ============================================================
"""
WHEN WALKING THROUGH THIS CODE WITH SCOUTS:

1. START AT THE BOTTOM
   - Show them where the program starts (if __name__ == "__main__")
   - Explain it calls main(), which controls everything

2. FOLLOW main() STEP BY STEP
   - Point out: it's just a recipe!
   - Show how it calls other functions in order
   - Emphasize: INPUT → COMPUTATION → DECISION → OUTPUT

3. DIVE INTO get_answer()
   - This is the most important function!
   - Show how if/elif/else is like a flowchart
   - Ask: "What would happen if random_number was 5?" (trace it!)

4. TALK ABOUT RANDOMNESS
   - Explain: random.randint(1, 20) picks a number we can't predict
   - That's why you get different answers each time!
   - Where else do programs use randomness? (games, shuffling, etc.)

5. RUN IT TOGETHER
   - Have each Scout ask a question out loud
   - Run the program for each one
   - Point out when you see positive/neutral/negative answers

6. DISCUSSION QUESTIONS:
   - "What if we used random.randint(1, 3) instead?"
     Answer: Only 3 possible answers — less variety
   
   - "How would you add a new answer?"
     Answer: Add another elif branch
   
   - "Why do we use functions?"
     Answer: Makes code organized and reusable
   
   - "What does .lower().strip() do in play_again()?"
     Answer: Makes input case-insensitive and removes spaces

7. CONNECT TO THEIR PROJECTS
   - "Your projects will follow the same pattern!"
   - Temperature Converter: INPUT temp → COMPUTE conversion → DECIDE message
   - Adventure Game: INPUT choice → COMPUTE score → DECIDE next scene
   - Grade Calculator: INPUT scores → COMPUTE average → DECIDE letter grade

8. CHALLENGE THEM
   - "Can you add a 21st answer before we finish?"
   - "Can you make it count how many times it's been used?"
   
GOOD LUCK! This demo sets them up for success on their own projects.
"""
