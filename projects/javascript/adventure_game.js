/**
 * 🗺️ Adventure Quest
 * ==================
 * Programming Merit Badge — Requirement 5b (JavaScript)
 *
 * This is a text-based adventure game that runs in the browser.
 * The player makes choices, and the story changes based on those decisions.
 *
 * HOW THIS PROGRAM WORKS:
 * - INPUT:       Player clicks choice buttons
 * - COMPUTATION: Score tracking, room counting
 * - DECISIONS:   if/else logic determines what happens next
 * - OUTPUT:      Story text and final score displayed on screen
 */

// ============================================================
// GAME STATE — These variables track what's happening
// ============================================================

let score = 0;          // Player's current score
let roomNumber = 0;     // Which room/scene the player is in
let history = [];       // Log of choices the player made

// ============================================================
// STORY DATA — Each scene has text and choices
// ============================================================
// Each scene is an object with:
//   - text: what the player reads (the OUTPUT)
//   - choices: array of options (the INPUT), each with:
//       - text: what the button says
//       - nextScene: which scene to go to
//       - points: how many points this choice is worth
//       - message: feedback shown before the next scene

const scenes = {
    start: {
        text: "You wake up in a mysterious forest. 🌲 The sun is barely peeking through the thick canopy of trees above you. You hear a stream nearby and see a faint path leading deeper into the woods.\n\nWhat do you do?",
        choices: [
            {
                text: "🚶 Follow the path deeper into the forest",
                nextScene: "forest_path",
                points: 10,
                message: "You bravely head down the path..."
            },
            {
                text: "💧 Go toward the sound of the stream",
                nextScene: "stream",
                points: 10,
                message: "You follow the sound of running water..."
            },
            {
                text: "🌳 Climb a tall tree to look around",
                nextScene: "treetop",
                points: 15,
                message: "You find a climbable tree and start going up..."
            }
        ]
    },

    forest_path: {
        text: "The path leads to a fork in the road. On the left, you see an old wooden bridge over a ravine. On the right, there's a cave entrance with strange glowing symbols carved around it. 🔮\n\nWhich way do you go?",
        choices: [
            {
                text: "🌉 Cross the old wooden bridge",
                nextScene: "bridge",
                points: 10,
                message: "You carefully step onto the bridge..."
            },
            {
                text: "🕳️ Enter the mysterious cave",
                nextScene: "cave",
                points: 15,
                message: "You take a deep breath and enter the cave..."
            }
        ]
    },

    stream: {
        text: "You find a beautiful clear stream. 💧 The water looks refreshing. You notice something shiny at the bottom of the stream, and there's also a small wooden boat tied to a tree nearby.\n\nWhat do you do?",
        choices: [
            {
                text: "✨ Reach in and grab the shiny object",
                nextScene: "shiny_object",
                points: 20,
                message: "You roll up your sleeves and reach into the cold water..."
            },
            {
                text: "🚣 Untie the boat and float downstream",
                nextScene: "boat_ride",
                points: 10,
                message: "You hop into the boat and push off..."
            }
        ]
    },

    treetop: {
        text: "From the top of the tree, you can see the entire forest! 🌄 To the north, there's a village with smoke rising from chimneys. To the east, you spot ancient ruins covered in vines. A friendly eagle lands on a branch near you. 🦅\n\nWhat do you do?",
        choices: [
            {
                text: "🏘️ Climb down and head toward the village",
                nextScene: "village",
                points: 10,
                message: "You climb down and head north..."
            },
            {
                text: "🏛️ Head toward the ancient ruins",
                nextScene: "ruins",
                points: 15,
                message: "The ruins look fascinating — you head east..."
            },
            {
                text: "🦅 Try to befriend the eagle",
                nextScene: "eagle",
                points: 25,
                message: "You slowly extend your hand toward the eagle..."
            }
        ]
    },

    bridge: {
        text: "The bridge creaks as you cross, but you make it! On the other side, you find a friendly old wizard sitting by a campfire. 🧙‍♂️\n\n'Ah, a traveler! I can teach you a magic spell, or I can give you a map to a hidden treasure. Which would you prefer?'",
        choices: [
            {
                text: "✨ 'Teach me the spell, please!'",
                nextScene: "ending_magic",
                points: 20,
                message: "The wizard smiles and raises his staff..."
            },
            {
                text: "🗺️ 'I'll take the treasure map!'",
                nextScene: "ending_treasure",
                points: 20,
                message: "The wizard hands you an ancient parchment..."
            }
        ]
    },

    cave: {
        text: "Inside the cave, the glowing symbols light your way. 🔮 You find a room with three treasure chests! But a sign warns: 'Only one chest is safe to open. Choose wisely.'\n\nThe chests are labeled: Gold 🥇, Silver 🥈, Bronze 🥉",
        choices: [
            {
                text: "🥇 Open the Gold chest",
                nextScene: "ending_gold",
                points: 10,
                message: "You open the gold chest..."
            },
            {
                text: "🥈 Open the Silver chest",
                nextScene: "ending_silver",
                points: 25,
                message: "You open the silver chest..."
            },
            {
                text: "🥉 Open the Bronze chest",
                nextScene: "ending_bronze",
                points: 15,
                message: "You open the bronze chest..."
            }
        ]
    },

    shiny_object: {
        text: "You pull out a beautiful crystal that glows with an inner light! 💎 As you hold it up, it projects a map on the cave wall nearby showing a path to a hidden village.\n\nThe crystal seems to hum with energy...",
        choices: [
            {
                text: "🗺️ Follow the projected map",
                nextScene: "village",
                points: 15,
                message: "The crystal guides your way!"
            },
            {
                text: "💎 Keep the crystal and continue exploring",
                nextScene: "ending_crystal",
                points: 20,
                message: "You pocket the crystal — it might be useful..."
            }
        ]
    },

    boat_ride: {
        text: "The boat carries you downstream through beautiful scenery! 🚣 You pass by fireflies and glowing mushrooms. Eventually, the stream leads to a peaceful lake near a small village.\n\nVillagers wave at you from the shore!",
        choices: [
            {
                text: "🏘️ Land the boat and visit the village",
                nextScene: "village",
                points: 10,
                message: "You paddle to shore..."
            }
        ]
    },

    village: {
        text: "The village is warm and welcoming! 🏘️ The villagers are amazed by your journey through the forest. The village elder approaches you.\n\n'Welcome, adventurer! You've shown great courage. We'd like to offer you a place in our village, or we can point you toward one final challenge — the Dragon's Peak! 🐉'",
        choices: [
            {
                text: "🏠 'I'll stay in the village!' (Safe ending)",
                nextScene: "ending_village",
                points: 15,
                message: "The villagers cheer!"
            },
            {
                text: "🐉 'Dragon's Peak? I'm in!' (Risky ending)",
                nextScene: "ending_dragon",
                points: 30,
                message: "You grab a sword and head for the peak..."
            }
        ]
    },

    ruins: {
        text: "The ancient ruins are covered in vines and moss. 🏛️ You find an old library with books that still have readable pages! You discover the ruins were once a school for young wizards.\n\nOn a pedestal, there's a glowing book titled 'Beginner Spells.'",
        choices: [
            {
                text: "📖 Read the spell book",
                nextScene: "ending_magic",
                points: 20,
                message: "You open the book and start reading..."
            },
            {
                text: "🔍 Explore deeper into the ruins",
                nextScene: "ending_treasure",
                points: 15,
                message: "You venture further into the darkness..."
            }
        ]
    },

    eagle: {
        text: "The eagle is friendly! 🦅 It lets you climb on its back and takes you soaring above the forest. From up high, you see everything — the village, the ruins, and even a dragon sleeping on a distant peak!\n\nThe eagle circles, waiting for you to choose a destination.",
        choices: [
            {
                text: "🏘️ 'Take me to the village!'",
                nextScene: "village",
                points: 15,
                message: "The eagle swoops down toward the village..."
            },
            {
                text: "🐉 'Take me to the dragon!'",
                nextScene: "ending_dragon",
                points: 30,
                message: "The eagle shrieks and flies toward Dragon's Peak..."
            }
        ]
    },

    // TODO Challenge #1: Add your own scene here!
    // Follow this pattern:
    //
    // my_new_scene: {
    //     text: "Describe what the player sees...",
    //     choices: [
    //         {
    //             text: "First choice",
    //             nextScene: "some_ending",
    //             points: 10,
    //             message: "What happens..."
    //         },
    //         {
    //             text: "Second choice",
    //             nextScene: "another_ending",
    //             points: 20,
    //             message: "What happens..."
    //         }
    //     ]
    // },

    // ============================================================
    // ENDINGS — These are the final scenes
    // ============================================================

    ending_magic: {
        text: "✨ ENDING: The Apprentice Wizard ✨\n\nYou learn the basics of magic! Sparks fly from your fingertips as you cast your first spell. The forest animals gather around, amazed. You've discovered a talent you never knew you had.\n\nYou decide to stay and study more magic, eventually becoming a great wizard who protects the forest! 🧙‍♂️",
        choices: []  // Empty = game over (ending)
    },

    ending_treasure: {
        text: "💰 ENDING: The Treasure Hunter 💰\n\nYou follow the map through twisting tunnels and find a room filled with gold coins, gems, and ancient artifacts! But the real treasure is a journal from a famous explorer with wisdom about courage and kindness.\n\nYou share the wealth with the nearby village, and they name a street after you! 🏆",
        choices: []
    },

    ending_gold: {
        text: "🥇 ENDING: Gold Wasn't the Answer 🥇\n\nThe gold chest was... empty! Just a note that says 'Not everything that glitters is gold!' 😅\n\nBut you learned an important lesson about making assumptions. You find your way back out of the cave and continue your journey wiser than before.",
        choices: []
    },

    ending_silver: {
        text: "🥈 ENDING: The Wise Choice 🥈\n\nThe silver chest contains a beautiful silver compass that always points toward home! 🧭 It was the right choice all along — sometimes the flashiest option isn't the best.\n\nWith the compass, you navigate out of the cave and find your way to an amazing village. You're hailed as a wise adventurer!",
        choices: []
    },

    ending_bronze: {
        text: "🥉 ENDING: The Humble Path 🥉\n\nThe bronze chest contains a warm blanket and some food. Simple, but exactly what an adventurer needs! A note inside reads: 'Practical wisdom is the greatest treasure.'\n\nYou're well-prepared for the rest of your journey. Sometimes the practical choice is the smart choice! 🎒",
        choices: []
    },

    ending_crystal: {
        text: "💎 ENDING: The Crystal Bearer 💎\n\nThe crystal turns out to be a legendary artifact! It glows brighter as you help people — it's powered by kindness. Word spreads of the young adventurer with the magical crystal.\n\nYou travel the land, using the crystal's light to help those in need. You become known as the Crystal Bearer! ✨",
        choices: []
    },

    ending_village: {
        text: "🏠 ENDING: A New Home 🏠\n\nYou settle into village life and discover your adventure skills are incredibly useful. You teach the village children about the forest, help build new bridges, and become a beloved member of the community.\n\nSometimes the greatest adventure is finding where you belong. 🤝",
        choices: []
    },

    ending_dragon: {
        text: "🐉 ENDING: The Dragon Rider 🐉\n\nYou reach Dragon's Peak and face the mighty dragon! But instead of fighting, you notice the dragon looks sad and lonely. You sit down and talk to it.\n\nThe dragon hasn't had a friend in 500 years! You become the first Dragon Rider in centuries, soaring through the skies together! 🐉✨\n\nBravery isn't about fighting — it's about understanding.",
        choices: []
    }
};


// ============================================================
// GAME FUNCTIONS — These make the game work
// ============================================================

/**
 * Display a scene on the screen.
 * This function handles the OUTPUT part of our program.
 */
function showScene(sceneId) {
    // Look up the scene data
    let scene = scenes[sceneId];

    // DECISION: Check if the scene exists
    if (!scene) {
        document.getElementById("story-text").textContent =
            "Error: Scene '" + sceneId + "' not found! Check your code. 🐛";
        return;
    }

    // Increment room counter (COMPUTATION)
    roomNumber = roomNumber + 1;

    // Update the display (OUTPUT)
    document.getElementById("story-text").textContent = scene.text;
    document.getElementById("score-display").textContent = score;
    document.getElementById("room-display").textContent = roomNumber;

    // Clear old choices
    let choicesContainer = document.getElementById("choices-container");
    choicesContainer.innerHTML = "";

    // DECISION: Is this an ending? (no choices = game over)
    if (scene.choices.length === 0) {
        showGameOver(choicesContainer);
        return;
    }

    // Create a button for each choice (INPUT setup)
    for (let i = 0; i < scene.choices.length; i++) {
        let choice = scene.choices[i];
        let button = document.createElement("button");
        button.className = "choice-btn";
        button.textContent = choice.text;

        // When the button is clicked, handle the choice
        button.addEventListener("click", function () {
            handleChoice(choice);
        });

        choicesContainer.appendChild(button);
    }
}

/**
 * Handle when the player makes a choice.
 * This is where INPUT, COMPUTATION, and DECISIONS come together!
 */
function handleChoice(choice) {
    // COMPUTATION: Add points to the score
    score = score + choice.points;

    // Log the choice in history
    history.push(choice.text + " (+" + choice.points + " pts)");
    updateHistoryLog();

    // Briefly show the transition message, then show next scene
    document.getElementById("story-text").textContent = choice.message;

    // Wait 1 second, then show the next scene (creates suspense!)
    setTimeout(function () {
        showScene(choice.nextScene);
    }, 1000);
}

/**
 * Show the game over screen with final score.
 * Makes DECISIONS about the rating based on score.
 */
function showGameOver(choicesContainer) {
    // COMPUTATION: Calculate the rating
    let rating;
    let ratingEmoji;

    // DECISIONS: Different messages based on score ranges
    if (score >= 80) {
        rating = "Legendary Explorer";
        ratingEmoji = "🏆";
    } else if (score >= 60) {
        rating = "Brave Adventurer";
        ratingEmoji = "⭐";
    } else if (score >= 40) {
        rating = "Curious Wanderer";
        ratingEmoji = "🗺️";
    } else {
        rating = "Cautious Traveler";
        ratingEmoji = "🚶";
    }

    // TODO Challenge #2: Add more score ranges and ratings!

    // OUTPUT: Show the final results
    let storyText = document.getElementById("story-text");
    storyText.textContent += "\n\n" +
        "━━━━━━━━━━━━━━━━━━━━\n" +
        ratingEmoji + " QUEST COMPLETE! " + ratingEmoji + "\n" +
        "Score: " + score + " points\n" +
        "Rooms visited: " + roomNumber + "\n" +
        "Rating: " + rating + "\n" +
        "━━━━━━━━━━━━━━━━━━━━";

    // Add a restart button
    let restartBtn = document.createElement("button");
    restartBtn.className = "choice-btn restart-btn";
    restartBtn.textContent = "🔄 Play Again? Try a different path!";
    restartBtn.addEventListener("click", function () {
        restartGame();
    });
    choicesContainer.appendChild(restartBtn);
}

/**
 * Record choices in the visible history log.
 */
function updateHistoryLog() {
    let logElement = document.getElementById("history-log");
    logElement.innerHTML = "";

    for (let i = 0; i < history.length; i++) {
        let li = document.createElement("li");
        li.textContent = history[i];
        logElement.appendChild(li);
    }
}

/**
 * Restart the game — reset all state and start over.
 */
function restartGame() {
    // Reset state
    score = 0;
    roomNumber = 0;
    history = [];
    document.getElementById("history-log").innerHTML = "";

    // Show the first scene
    showScene("start");
}


// ============================================================
// START THE GAME!
// ============================================================

// When the page finishes loading, start the adventure
showScene("start");
