# Keep asking for scores until the player types "stop".
while True:
    score_input = input("Enter your game score (or type stop): ").strip().lower()

    # End the game session when the player types stop.
    if score_input == "stop":
        print("Game session ended!")
        break

    # Change the score into a number.
    score = int(score_input)

    # Check if the score is a high score.
    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")
