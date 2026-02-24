# 🎓 Teaching Guide for Counselors

## Recommended Session Flow

### Morning Session (2-3 hours)

#### Part 1: Introduction (15 min)
- Show `slides/html/00-intro.html`
- Set expectations and ground rules
- Get Scouts excited about programming!

#### Part 2: Safety (20 min)
- Show `slides/html/01-safety.html`
- Do the stretching exercise together (slide 8)
- **Discussion:** Digital safety, RSI prevention, ergonomics

#### Part 3: History (25 min)
- Show `slides/html/02-history.html`
- Interactive: Have Scouts pick their favorite milestone
- **Discussion:** How has programming changed over time?

#### Break (10 min)
Stretch, grab water, rest eyes!

#### Part 4: General Knowledge (25 min)
- Show `slides/html/03-general-knowledge.html`
- Activity: Scouts fill out the language/device worksheet (slide 11)
- **Discussion:** What devices surprised them?

#### Part 5: Intellectual Property (30 min)
- Show `slides/html/04-intellectual-property.html`
- Use real-world examples (Netflix, apps they use)
- **Discussion:** Why respect software licenses?

---

### Afternoon Session (2-3 hours)

#### Part 6: **DEMO — Magic 8-Ball Walkthrough** (30-45 min) ⭐

**This is the MOST IMPORTANT teaching moment!**

Run `projects/demo/magic_8_ball.py` and walk through it together:

1. **Open the code** in a text editor side-by-side with the terminal
2. **Run it first** — let Scouts ask questions and see it work
3. **Explain the flow:**
   ```
   INPUT → COMPUTATION → DECISION → OUTPUT
   ```
4. **Walk through the code:**
   - Start at `main()` — show how it's a recipe/flowchart
   - Explain `get_question()` — this is INPUT
   - Explain `shake_the_ball()` — this is COMPUTATION (random number)
   - **FOCUS HERE:** `get_answer()` — this is DECISIONS (if/elif/else)
   - Explain `show_answer()` — this is OUTPUT
5. **Trace an example:**
   - "Let's say the random number is 7. Follow it through the code!"
   - Point at line 76: `elif random_number == 7:`
   - Show: "It would return 'Outlook good.'"
6. **Discussion questions:**
   - "What would happen if we only used `random.randint(1, 3)`?"
   - "How would you add your own custom answer?"
   - "Why do we use functions to organize code?"

**Key Teaching Point:** "All three of your projects follow this same pattern!"

#### Break (10 min)

#### Part 7: Project Setup (15 min)

Assign Scouts to their three projects:
1. **Python** — Temperature Converter (`projects/python/`)
2. **JavaScript** — Adventure Quiz (`projects/javascript/`)
3. **Scratch** — Grade Calculator (`projects/scratch/`)

**Walk through each project README together** — show them:
- How to run it
- Where the TODO comments are
- What they need to modify/explain

#### Part 8: Project Work Time (60-90 min)

Scouts work on their three projects. Circulate to help!

**Encourage pair programming** — work together, help each other debug.

**Common issues to watch for:**
- Python: `NameError` (forgot to define variable), `IndentationError` (wrong spacing)
- JavaScript: Forgetting to open `index.html` in a browser, typos in scene names
- Scratch: Forgetting to set initial variable values, nesting if/else incorrectly

#### Part 9: Demonstrations (30 min)

Each Scout (or pair) demonstrates ONE of their projects:
1. **Run it** — show the input/output
2. **Explain it** — "Here's where it gets input, here's where it makes decisions..."
3. **Show a modification** — "I added Kelvin conversion!" or "I added a new room!"

---

## Teaching Tips

### For the Demo (Magic 8-Ball)

✅ **DO:**
- Run it multiple times to show randomness
- Ask Scouts to predict what will happen
- Trace through the code line-by-line for one execution
- Point out the if/elif/else ladder clearly
- Connect it to real programs they use (game AI, Siri, etc.)

❌ **DON'T:**
- Rush through it — this sets them up for success!
- Get bogged down in syntax details (semicolons, parentheses, etc.)
- Skip the "trace an example" — that's where learning happens

### For Code Review

When a Scout shows you their project, ask:
1. **"Where does your program get INPUT?"**
2. **"Show me where it does COMPUTATION."**
3. **"What DECISIONS does your program make?"**
4. **"How does it produce OUTPUT?"**

These questions ensure they understand the concepts, not just copied code.

### Debugging Help

When Scouts get stuck:
1. **Read the error message together** — what does it say?
2. **Trace the code** — use `print()` statements to see variable values
3. **Check the basics:**
   - Did you spell variable names correctly?
   - Did you indent properly? (Python)
   - Did you close all parentheses/brackets? (JavaScript)
4. **Pair them up** — two heads are better than one!

### Encouraging Struggling Scouts

- "Programming is SUPPOSED to be hard at first. You're learning a new language!"
- "Every programmer Googles things and gets errors. That's normal!"
- "The fact that you found the bug means you're thinking like a programmer!"
- "Let's break this down into smaller steps."

### Challenging Advanced Scouts

If someone finishes early:
1. **Add features** — More answers, color, sound, new game mechanics
2. **Help others** — Can you explain your solution to someone stuck?
3. **Refactor** — Can you make your code cleaner or more efficient?
4. **Combine projects** — Can you make a Python web app? A JavaScript calculator?

---

## Key Concepts to Emphasize

Throughout the day, keep returning to these themes:

### 1. The Four-Part Pattern
Every program has:
- **INPUT** — Get data from the user/world
- **COMPUTATION** — Process/calculate something
- **DECISIONS** — Make choices with if/else
- **OUTPUT** — Show results

### 2. Bugs Are Learning Opportunities
- "There's a bug!" → "Great! Now we get to be detectives!"
- Every error message teaches you something

### 3. Code Is Communication
- You're writing instructions for a computer
- You're also writing for other humans who will read your code
- Clear variable names, comments, and organization matter!

### 4. Programming Is Everywhere
- Your phone, car, thermostat — all programmed
- Every app, game, and website
- Learning to code helps you understand the world

### 5. Growth Mindset
- "I don't know how to do this... **yet**"
- Mistakes help you learn faster
- Asking for help is a sign of strength, not weakness

---

## Time-Saving Tips

### If You're Short on Time

**3-hour session?**
- Do intro + safety + ONE concept (history OR general knowledge)
- Demo the Magic 8-Ball
- Work on projects
- Skip intellectual property or assign as "homework discussion"

**2-hour session?**
- Skip intro slides, jump straight to demo
- Work on projects (they can read slides at home)
- Do discussions while projects are running

**Multiple shorter sessions?**
- Session 1: Slides 1-4 (requirements 1-4)
- Session 2: Demo + start projects
- Session 3: Finish projects + demonstrate

### If You Have Extra Time

- Build a 4th project together as a group
- Have Scouts present to each other
- Invite a professional programmer to talk about their job
- Tour a computer museum (virtually or in person)
- Play coding games (CodeCombat, Scratch community projects)

---

## Required Materials Checklist

**For Counselor:**
- [ ] Laptop/computer with projector for slides
- [ ] Python 3 installed (for demo)
- [ ] Text editor (VS Code, Sublime, Notepad++)
- [ ] Slides open in browser (`slides/html/index.html`)
- [ ] Demo code ready to run (`projects/demo/`)

**For Each Scout:**
- [ ] Laptop/computer (one per scout or pair)
- [ ] Python 3 installed
- [ ] Web browser (for JavaScript project)
- [ ] Text editor
- [ ] Scratch account (created in advance or during session)
- [ ] Copy of this project folder

**Optional but Helpful:**
- [ ] Backup USB drives with project folder
- [ ] Printed copies of project READMEs
- [ ] Whiteboard/markers for drawing flowcharts
- [ ] Extension cord / power strips

---

## Success Metrics

By the end, each Scout should be able to:

✅ Explain the difference between INPUT, COMPUTATION, DECISION, and OUTPUT  
✅ Identify these four parts in a simple program  
✅ Write/modify a program that uses if/else logic  
✅ Debug a simple error by reading error messages  
✅ Run their programs and demonstrate them to the counselor  
✅ Discuss the merit badge requirements (1-4) intelligently  

---

## Follow-Up & Next Steps

**After completing the merit badge:**
- Encourage Scouts to keep coding! Share resources:
  - [freeCodeCamp.org](https://freecodecamp.org) — Free web dev courses
  - [Codecademy](https://codecademy.com) — Interactive lessons
  - [Python.org Tutorial](https://docs.python.org/3/tutorial/) — Official Python guide
  - [Scratch Community](https://scratch.mit.edu/explore/projects/all) — Millions of projects to remix

**Project ideas to try next:**
- Discord bot (Python)
- Chrome extension (JavaScript)
- Game in Pygame/Scratch
- Personal website (HTML/CSS/JS)

**Join communities:**
- Local coding clubs
- Hour of Code events
- GitHub (share projects!)
- Stack Overflow (get help)

---

## Questions or Issues?

If you encounter problems or have suggestions for improving this teaching kit, please share feedback with your fellow merit badge counselors!

**Good luck, and have fun! Programming is an amazing skill that will serve these Scouts for life.** 🎉
