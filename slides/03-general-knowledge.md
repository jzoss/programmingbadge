---
marp: true
theme: default
paginate: true
footer: "🏅 Programming Merit Badge — Requirement 3: General Knowledge"
style: |
  section {
    font-size: 28px;
    overflow: auto !important;
  }
  h1 {
    color: #003f87;
  }
  h2 {
    color: #c6093b;
  }
  section.lead h1 {
    font-size: 48px;
    text-align: center;
  }
  section.lead h2 {
    text-align: center;
  }
  code {
    font-size: 22px;
  }
  section.compact {
    font-size: 23px;
  }
  section.compact table {
    font-size: 20px;
  }
  section.compact pre, section.compact code {
    font-size: 18px;
  }
---

<!-- _class: lead -->

# 🌍 Requirement 3: General Knowledge

## Programming Languages & Devices Around You

---

# 📋 What This Requirement Asks

**(a)** Create a list of **five popular programming languages** in use today. Describe which **industry** each is used in and **why**.

**(b)** Describe **three different programmed devices** you rely on every day.

---

<!-- _class: compact -->

# 🐍 Language #1: Python

### "The Swiss Army Knife of Programming"

**Industries:** Data Science, AI/Machine Learning, Web Development, Science, Education

**Why it's popular:**
- Reads almost like English — easiest language to start with
- Massive library of pre-built tools
- #1 language for AI and data science

**Example — What does this do?**
```python
name = input("What's your name? ")
print(f"Hello, {name}! Welcome to programming!")
```

**Who uses it:** Google, Netflix, Instagram, NASA, SpaceX

---

<!-- _class: compact -->

# 🌐 Language #2: JavaScript

### "The Language of the Web"

**Industries:** Web Development (front-end AND back-end), Mobile Apps, Games

**Why it's popular:**
- The ONLY language that runs directly in web browsers
- Every website you visit uses JavaScript
- Can build websites, servers, apps, and games

**Example — What does this do?**
```javascript
let name = prompt("What's your name?");
document.write("Hello, " + name + "! Welcome!");
```

**Who uses it:** Every website ever! Plus: Facebook, Uber, Airbnb, Discord

---

<!-- _class: compact -->

# ☕ Language #3: Java

### "Write Once, Run Anywhere"

**Industries:** Enterprise Software, Android Apps, Banking, Big Corporations

**Why it's popular:**
- Works on any device that has the Java Virtual Machine
- Extremely reliable — banks and hospitals trust it
- Used to build Android apps (now alongside Kotlin)

**Example — What does this do?**
```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**Who uses it:** Amazon, Google (Android), most big banks, Minecraft! ⛏️

---

<!-- _class: compact -->

# ⚡ Language #4: C++

### "The Speed Demon"

**Industries:** Video Games, Operating Systems, Embedded Systems, Robotics

**Why it's popular:**
- Extremely FAST — gives direct control over hardware
- Used when performance is critical
- Powers most AAA video games and game engines

**Example — What does this do?**
```cpp
#include <iostream>
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

**Who uses it:** Epic Games (Fortnite/Unreal Engine), Adobe, Microsoft Windows, Tesla

---

<!-- _class: compact -->

# 🍎 Language #5: Swift

### "The Apple Language"

**Industries:** iOS/macOS App Development, Apple Ecosystem

**Why it's popular:**
- Designed by Apple specifically for iPhones and iPads
- Modern, safe, and fast
- If you want to make an iPhone app, this is the language!

**Example — What does this do?**
```swift
let name = "Scout"
print("Hello, \(name)! Welcome to Swift!")
```

**Who uses it:** Apple, Lyft, LinkedIn, Airbnb (iOS apps)

---

<!-- _class: compact -->

# 🎮 Language #6: C# (.NET)

### "The Microsoft All-Rounder"

**Industries:** Game Development, Enterprise Software, Web Applications

**Why it's popular:**
- Created by Microsoft in 2000 as part of the **.NET** platform
- The go-to language for **Unity** (world's most popular game engine)
- Also powers **MonoGame** — used to build *Stardew Valley*, *Celeste*, and *Bastion*
- Great for Windows apps, web APIs (ASP.NET), and enterprise systems

**Example — What does this do?**
```csharp
Console.WriteLine("Hello, World!");
```

**Who uses it:** Microsoft, Unity Technologies, Stack Overflow, Stardew Valley (ConcernedApe)

---

# 📊 Language Comparison

| Language | Main Industry | Best For | Difficulty |
|----------|--------------|----------|------------|
| 🐍 Python | AI, Data Science, Web | Beginners, data analysis, automation | ⭐ Easy |
| 🌐 JavaScript | Web Development | Websites, web apps, servers | ⭐⭐ Medium |
| ☕ Java | Enterprise, Android | Big business apps, Android | ⭐⭐⭐ Medium-Hard |
| ⚡ C++ | Games, Systems | Game engines, performance-critical | ⭐⭐⭐⭐ Hard |
| 🍎 Swift | iOS Apps | iPhone/iPad apps | ⭐⭐ Medium |
| 🎮 C# | Games, Enterprise, Web | Unity/MonoGame games, web APIs | ⭐⭐ Medium |

### Notice:
All six print "Hello, World!" — but the **syntax** (how you write it) is different in each!

---

# 📱 Part B: Programmed Devices You Use Every Day

> **Think about it:** How many programmed devices did you use TODAY before you even got here?

Let's look at three devices you probably rely on...

---

<!-- _class: compact -->

# 📱 Device #1: Smartphone

### What's programmed inside your phone?

| Component | Software Involved |
|-----------|------------------|
| Operating System | iOS (Swift/Obj-C) or Android (Java/Kotlin) |
| Apps | Each written in various languages |
| Camera | AI algorithms for face detection, filters |
| GPS/Maps | Routing algorithms find shortest path |
| Voice Assistant | Siri/Google — AI & speech recognition |
| Touchscreen | Code translates finger position to actions |

**Your phone runs MILLIONS of lines of code!**
- Android: ~12 million lines of code
- iOS: estimated 10+ million lines

---

<!-- _class: compact -->

# 🎮 Device #2: Gaming Console / PC

### What's programmed in your Xbox, PlayStation, Switch, or gaming PC?

| Component | Software Involved |
|-----------|------------------|
| Game Engine | Renders 3D graphics 60+ times per second |
| Physics Engine | Simulates gravity, collisions, ragdoll |
| AI | Controls non-player characters (NPCs) |
| Matchmaking | Connects you with other players online |
| Audio Engine | 3D spatial sound, dynamic music |
| Anti-cheat | Detects and prevents cheating |

**A modern game like Fortnite or Minecraft has millions of lines of code!**

---

<!-- _class: compact -->

# 🚗 Device #3: Modern Car

### Yes, your car is a computer on wheels! 🖥️🚗

| System | What's Programmed |
|--------|------------------|
| Engine Control | Fuel injection timing, emissions |
| Anti-lock Brakes (ABS) | Prevents wheels from locking up |
| GPS Navigation | Route calculation, traffic avoidance |
| Infotainment | Touchscreen, music, phone connection |
| Safety Systems | Lane assist, collision warnings, airbags |
| Electric Vehicles | Battery management, regenerative braking |

**A modern car has over 100 million lines of code** — more than a fighter jet! ✈️

---

# 🤯 Bonus: Programmed Things You Might Not Think Of

- 🚦 **Traffic lights** — timed by software, some use sensors
- 🌡️ **Thermostat** — programmed to maintain temperature
- 🏧 **ATM machines** — still running COBOL from the 1960s!
- 🛒 **Self-checkout machines** — barcode scanning + payment
- 🎵 **Spotify/YouTube** — algorithms decide what to recommend
- 🚀 **Spacecraft** — Mars rovers are programmed in C!
- 🧺 **Washing machine** — yes, your washer has a microcontroller!

> **Everything with a "smart" in front of it is programmed!**

---

<!-- _class: compact -->

# ✏️ Activity Time!

### Your Turn — Fill This Out:

**Part (a):** List five programming languages and their industries.
(Use the ones we just learned, or research others!)

| Language | Industry | Why? |
|----------|----------|------|
| 1. | | |
| 2. | | |
| 3. | | |
| 4. | | |
| 5. | | |

**Part (b):** Name 3 programmed devices YOU use daily.
For each one, describe what the software does.

---

# 💬 Discussion Time!

Discuss with your counselor:

1. **Name five popular programming languages.** For each, describe what industry uses it and why.

2. **What are three programmed devices** you rely on every day? What does the software in each one do?

3. **Which language** would you most want to learn? Why?

4. **Were you surprised** by any of the devices? Which ones?

> ✅ **Req 3 Complete!** When you've discussed these with your counselor.

---

# ⏭️ Up Next: Requirement 4

## ⚖️ Intellectual Property

Who owns software? What's the difference between a license and owning something? Let's find out! 🔍

### [➡️ Continue to Requirement 4: Intellectual Property →](04-intellectual-property.html)
