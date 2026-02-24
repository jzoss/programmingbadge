# 🏅 Programming Merit Badge — Teaching Kit

A complete teaching kit for the **BSA Programming Merit Badge**, targeting Scouts aged 12–17.

📖 **NEW TO TEACHING THIS?** See [TEACHING_GUIDE.md](TEACHING_GUIDE.md) for a complete walkthrough!

## What's Inside

| Folder | Contents |
|--------|----------|
| `slides/` | Marp Markdown slide decks for Requirements 1–4 |
| `projects/demo/` | 🎱 Magic 8-Ball — Teaching demo to walk through with Scouts |
| `projects/python/` | 🐍 Temperature Converter — Python starter code (Req 5a) |
| `projects/javascript/` | 🌐 Adventure Quiz Game — JavaScript starter code (Req 5b) |
| `projects/scratch/` | 🧩 Grade Calculator — Step-by-step Scratch build guide (Req 5c) |

## Quick Start

### 🚀 Super Quick Launch (Easiest!)

Just double-click one of these files:
- **Windows:** `open-slides.bat`
- **Mac/Linux:** `open-slides.sh`

This opens an index page with links to all 5 slide decks.

### Viewing Slides

**Option A — Pre-built HTML (easiest!):**
Just open any HTML file in `slides/html/` with your browser:
- **Mac/Linux:** `open slides/html/index.html`
- **Windows:** `start slides/html/index.html` or double-click the file

The index page links to all 5 slide decks. Use arrow keys to navigate slides.

**Option B — VS Code:**
1. Install the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension.
2. Open any `.md` file in the `slides/` folder.
3. Press `Cmd+Shift+V` (Mac) or `Ctrl+Shift+V` (Windows) to see the slide preview.

**Option C — Marp CLI:**
```bash
npm install          # install dependencies
npm run slides:preview   # opens slides in browser with live reload
```

### Building Slides to PDF/HTML (Optional)
```bash
npm run slides:build:html   # rebuilds all slides to HTML in slides/html/
npm run slides:build:pdf    # builds all slides to PDF in slides/html/
```

### Running the Projects
Teaching Demo (Walk through this FIRST!):**
```bash
# Mac/Linux:
cd projects/demo
python3 magic_8_ball.py

# Windows:
cd projects\demo
python magic_8_ball.py
```
This is a simple Magic 8-Ball program to demonstrate INPUT → COMPUTATION → DECISION → OUTPUT before Scouts start their own projects.

**
**Python (Req 5a):**
```bash
# Mac/Linux:
cd projects/python
python3 temperature_converter.py

# Windows:
cd projects\python
python temperature_converter.py
```

**JavaScript (Req 5b):**
```bash
# Mac/Linux:
cd projects/javascript
open index.html

# Windows:
cd projects\javascript
start index.html

# Or double-click index.html in File Explorer
```

****Demo** | **Teaching Example (do this first!)** | `projects/demo/` |
| Scratch (Req 5c):**
1. Go to [scratch.mit.edu](https://scratch.mit.edu)
2. Follow the step-by-step guide in `projects/scratch/README.md`

## Merit Badge Requirements Covered

| Req | Topic | Resource |
|-----|-------|----------|
| 1 | Safety | `slides/01-safety.md` |
| 2 | History of Programming | `slides/02-history.md` |
| 3 | General Knowledge | `slides/03-general-knowledge.md` |
| 4 | Intellectual Property | `slides/04-intellectual-property.md` |
| 5a | Project — Python | `projects/python/` |
| 5b | Project — JavaScript | `projects/javascript/` |
| 5c | Project — Scratch | `projects/scratch/` |

## Prerequisites

**To view slides (required):**
- Any web browser (Chrome, Firefox, Safari, Edge)

**To run projects (required for Requirement 5):**
- **Python 3** — [python.org](https://python.org) 
  - Windows: Download installer, check "Add Python to PATH" during installation
  - Mac: Pre-installed or use `brew install python3`
  - Linux: `sudo apt install python3` or equivalent
- **Web browser** — For JavaScript project (already installed)

**To build/edit slides (optional):**
- **Node.js & npm** — [nodejs.org](https://nodejs.org)
  - Windows: Download installer (includes npm automatically)
  - Mac: Use installer or `brew install node`
  - Linux: Use package manager or NodeSource

**For Scratch (Requirement 5c):**
- Free account at [scratch.mit.edu](https://scratch.mit.edu) — works on any OS
