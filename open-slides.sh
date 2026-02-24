#!/bin/bash
# Programming Merit Badge - Mac/Linux Launch Script
# This opens the slides in your default browser

echo ""
echo "========================================"
echo "  Programming Merit Badge Slides"
echo "========================================"
echo ""
echo "Opening slides in your browser..."
echo ""

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open slides/html/index.html
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    xdg-open slides/html/index.html 2>/dev/null || \
    x-www-browser slides/html/index.html 2>/dev/null || \
    firefox slides/html/index.html 2>/dev/null || \
    chromium slides/html/index.html 2>/dev/null || \
    echo "Could not detect browser. Please open slides/html/index.html manually."
else
    echo "Unknown OS. Please open slides/html/index.html manually."
fi

echo ""
echo "Done! Use arrow keys to navigate slides."
echo ""
