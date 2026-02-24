# 🏅 Programming Merit Badge — Teaching Kit

A complete teaching kit for the **BSA Programming Merit Badge**, targeting Scouts aged 12–17.

## What's Inside

| Folder | Contents |
|--------|----------|
| `slides/` | Marp Markdown slide decks for Requirements 1–4 |
| `projects/python/` | 🐍 Temperature Converter — Python starter code (Req 5a) |
| `projects/javascript/` | 🌐 Adventure Quiz Game — JavaScript starter code (Req 5b) |
| `projects/scratch/` | 🧩 Grade Calculator — Step-by-step Scratch build guide (Req 5c) |

## Quick Start

### Viewing Slides

**Option A — VS Code (easiest):**
1. Install the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension.
2. Open any `.md` file in the `slides/` folder.
3. Press `Cmd+Shift+V` (Mac) or `Ctrl+Shift+V` (Windows) to see the slide preview.

**Option B — Marp CLI:**
```bash
npm install          # install dependencies
npm run slides:preview   # opens slides in browser with live reload
```

### Building Slides to PDF/HTML
```bash
npm run slides:build:html   # builds all slides to HTML in slides/output/
npm run slides:build:pdf    # builds all slides to PDF in slides/output/
```

### Running the Projects

**Python (Req 5a):**
```bash
cd projects/python
python temperature_converter.py
```

**JavaScript (Req 5b):**
```bash
cd projects/javascript
# Just open index.html in any web browser!
open index.html   # Mac
```

**Scratch (Req 5c):**
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

- **Node.js** (for Marp CLI slide building) — [nodejs.org](https://nodejs.org)
- **Python 3** (for Req 5a project) — [python.org](https://python.org)
- **A web browser** (for Req 5b project and Scratch)
- **Scratch account** (free) at [scratch.mit.edu](https://scratch.mit.edu)
