# 🧩 Project 5c: Grade Calculator (Scratch)

## What This Program Does

A grade calculator built in Scratch! It asks for test scores, computes the average, decides the letter grade, and displays the result with a fun message.

**Requirements met:**
- ✅ Takes **input** from the user (test scores via "ask" blocks)
- ✅ Performs **computations** (sum, average)
- ✅ Makes **decisions** (if/else for letter grades)
- ✅ Produces **output** (average, letter grade, message via "say" blocks)

---

## Getting Started

1. Go to [scratch.mit.edu](https://scratch.mit.edu)
2. Click **"Create"** to start a new project
3. Follow the step-by-step instructions below!

---

## Pseudocode (The Plan)

Before we build in Scratch, here's the plan in plain English:

```
START

1. Ask "How many test scores do you have?"
2. Store the answer in a variable called "numberOfTests"

3. Set "totalScore" to 0
4. Set "counter" to 0

5. REPEAT (numberOfTests) times:
   a. Ask "Enter score #(counter + 1):"
   b. Add the answer to "totalScore"
   c. Add 1 to "counter"

6. COMPUTE the average:
   average = totalScore / numberOfTests

7. DECIDE the letter grade:
   IF average >= 90 THEN
       grade = "A"
       message = "Amazing work! 🌟"
   ELSE IF average >= 80 THEN
       grade = "B"
       message = "Great job! Keep it up! 💪"
   ELSE IF average >= 70 THEN
       grade = "C"
       message = "Not bad! A little more studying will help! 📚"
   ELSE IF average >= 60 THEN
       grade = "D"
       message = "You passed, but let's work on improving! 💡"
   ELSE
       grade = "F"
       message = "Don't give up! Ask for help and try again! 🤝"

8. OUTPUT the results:
   Say "Your average is (average)"
   Say "Your grade is: (grade)"
   Say message

END
```

---

## Step-by-Step Scratch Build Instructions

### Step 1: Create Variables

Click on **"Variables"** category (orange blocks) and create these variables:

| Variable Name | What It Stores |
|--------------|---------------|
| `numberOfTests` | How many test scores the user will enter |
| `totalScore` | Running total of all scores added together |
| `counter` | Keeps track of which score we're on |
| `average` | The calculated average score |
| `grade` | The letter grade (A, B, C, D, or F) |
| `message` | The fun feedback message |

> **How:** Click "Make a Variable" for each one. Make sure "For all sprites" is selected.

---

### Step 2: Start the Program

Drag these blocks from the **Events** category:

```
🟡 When green flag clicked
```

Then from **Looks**:
```
🟣 say "Welcome to the Grade Calculator! 📊" for 2 seconds
```

---

### Step 3: Ask How Many Tests

From **Sensing** (light blue):
```
🔵 ask "How many test scores do you have?" and wait
```

From **Variables** (orange):
```
🟠 set [numberOfTests] to (answer)
```

---

### Step 4: Initialize Variables

From **Variables**:
```
🟠 set [totalScore] to 0
🟠 set [counter] to 0
```

---

### Step 5: Collect Scores (The Loop!)

From **Control** (gold):
```
🟤 repeat (numberOfTests)
```

Inside the repeat loop, add:

From **Sensing**:
```
    🔵 ask (join "Enter score #" (counter + 1)) and wait
```

> **Tip:** Use `join` from Operators (green) to combine the text "Enter score #" with the counter + 1

From **Variables**:
```
    🟠 change [totalScore] by (answer)
    🟠 change [counter] by 1
```

---

### Step 6: Calculate the Average (Computation!)

After the repeat loop ends:

From **Variables** + **Operators**:
```
🟠 set [average] to ( (totalScore) / (numberOfTests) )
```

> **Tip:** The division block `( ) / ( )` is in the green **Operators** category. Drag `totalScore` and `numberOfTests` into it.

---

### Step 7: Decide the Letter Grade (Decisions!)

This is where `if/else` blocks come in! From **Control**:

```
🟤 if < (average) >= 90 > then
    🟠 set [grade] to "A"
    🟠 set [message] to "Amazing work! 🌟"
🟤 else
    🟤 if < (average) >= 80 > then
        🟠 set [grade] to "B"
        🟠 set [message] to "Great job! Keep it up! 💪"
    🟤 else
        🟤 if < (average) >= 70 > then
            🟠 set [grade] to "C"
            🟠 set [message] to "Not bad! Study a bit more! 📚"
        🟤 else
            🟤 if < (average) >= 60 > then
                🟠 set [grade] to "D"
                🟠 set [message] to "You passed! Let's improve! 💡"
            🟤 else
                🟠 set [grade] to "F"
                🟠 set [message] to "Don't give up! Ask for help! 🤝"
```

> **Tip:** The `>=` block is in green **Operators**. You'll need to **nest** if/else blocks inside each other — drag one `if/else` into the `else` part of the previous one!

> **Alternative:** Scratch doesn't have `else if`, so you nest `if/else` blocks. It looks like a staircase!

---

### Step 8: Show the Results (Output!)

From **Looks**:
```
🟣 say (join "Your average is: " (round (average))) for 3 seconds
🟣 say (join "Your letter grade: " (grade)) for 3 seconds
🟣 say (message) for 3 seconds
🟣 say "Thanks for using the Grade Calculator! 🎓" for 2 seconds
```

> **Tip:** Use `join` from Operators to combine text with variables. Use `round` from Operators to round the average to a whole number.

---

### Complete Block Layout

Here's the full program flow at a glance:

```
🟡 When green flag clicked
🟣 say "Welcome to the Grade Calculator! 📊" for 2 seconds
🔵 ask "How many test scores do you have?" and wait
🟠 set [numberOfTests] to (answer)
🟠 set [totalScore] to 0
🟠 set [counter] to 0
🟤 repeat (numberOfTests)
    🔵 ask (join "Enter score #" ((counter) + 1)) and wait
    🟠 change [totalScore] by (answer)
    🟠 change [counter] by 1
🟠 set [average] to ((totalScore) / (numberOfTests))
🟤 if <(average) >= 90> then
    🟠 set [grade] to "A"
    🟠 set [message] to "Amazing work! 🌟"
🟤 else
    🟤 if <(average) >= 80> then
        🟠 set [grade] to "B"
        🟠 set [message] to "Great job! 💪"
    🟤 else
        [... continue nesting for C, D, F ...]
🟣 say (join "Your average is: " (round (average))) for 3 seconds
🟣 say (join "Your letter grade: " (grade)) for 3 seconds
🟣 say (message) for 3 seconds
🟣 say "Thanks! 🎓" for 2 seconds
```

---

## TODO Challenges

After you get the basic version working, try these:

- [ ] **Add more subjects:** Ask the user for a subject name before each score and display "Math: 92, Science: 85" etc.
- [ ] **Add a pass/fail message:** If the grade is D or F, say "You need to retake this class."
- [ ] **Add sound effects:** Play a "win" sound for A/B grades and a different sound for lower grades.
- [ ] **Make the sprite react:** Change the sprite's costume based on the grade (happy face for A, sad for F).
- [ ] **Add a "highest and lowest" feature:** Track and display the highest and lowest scores entered.

---

## Explaining to Your Counselor

When you demonstrate this project, be ready to explain:

1. **Input:** "The program uses `ask` blocks to get test scores from the user."
2. **Computation:** "It adds all scores together and divides by the number of tests to get the average."
3. **Decisions:** "It uses nested `if/else` blocks to decide what letter grade to assign based on the average."
4. **Output:** "It uses `say` blocks to display the average, letter grade, and a motivational message."

---

## Helpful Scratch Resources

- 🎓 [Scratch Tutorials](https://scratch.mit.edu/projects/editor/?tutorial=getStarted) — Built-in tutorials
- 📖 [Scratch Wiki](https://en.scratch-wiki.info/) — Community knowledge base
- 🎥 [Scratch YouTube Channel](https://www.youtube.com/@ScratchTeam) — Video tutorials
