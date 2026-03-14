from flask import Flask, render_template, request

app = Flask(__name__)

# Our massive dictionary of epic Bopl Battle combos
combo_recommender = {
    "The Wrecking Ball": ["Push", "Rock", "Grappling Hook"],
    "The Balloon": ["Mine", "Gust", "Grappling Hook"],
    "Instant Destruction": ["Dash", "Dash", "Meteor"],
    "Map Eater": ["Growth Ray", "Black Hole", "Platform"],
    "Stealth Sniper": ["Smoke", "Time Stop", "Bow"],
    "The Rumbling": ["Growth Ray", "Revival", "Revival"],
    "Demon Core": ["Growth Ray", "Mine", "Duplicator"],
    "Quantum": ["Beam", "Invisibility", "Teleport"],
    "Apocalypse Survivor": ["Push", "Revival", "Teleport"],
    "Assassin": ["Bow", "Time Stop", "Grappling Hook"],
    "Black Hole Cannon": ["Black Hole", "Beam", "Smoke"],
    "Reverse the Polarity": ["Shrink Ray", "Black Hole", "Shrink Ray"],
    "Tele-Mines": ["Teleport", "Mine", "Dash"],
    "Where is the map???": ["Blink Gun", "Blink Gun", "Blink Gun"]
}

def power_match(power1, power2, power3):
    chosen_powers = [power1, power2, power3]
    for combo_name, combo_powers in combo_recommender.items():
        if sorted(chosen_powers) == sorted(combo_powers):
            return f"Awesome! You created the '{combo_name}' combo!"
    return "No known combo found for these powers. You might have invented a new one!"

# --- THE FLASK BRIDGE ---

# 1. The Homepage Route
@app.route("/")
def home():
    # This serves your HTML file to the user
    return render_template("index.html")

# 2. The Combine Route (Catches the form data)
@app.route("/combine", methods=["POST"])
def combine():
    # request.form.getlist("powers") grabs all the checkboxes the user clicked!
    chosen_powers = request.form.getlist("powers")
    
    # A quick safety check: Did they actually pick exactly 3?
    if len(chosen_powers) != 3:
        return "Hold up! You need to pick exactly 3 powers. Go back and try again!"
        
    # Send the 3 powers to your matching function
    result = power_match(chosen_powers[0], chosen_powers[1], chosen_powers[2])
    
    # Show the result on the screen
    return result

if __name__ == "__main__":
    # debug=True means the server will automatically update if you change the code!
    app.run(debug=True)