# Number Guessing Game - Week 1 Mini Project
# Combines all concepts from Days 1-6

import random

def display_welcome():
    """Display welcome message and game rules"""
    print("=" * 60)
    print("           NUMBER GUESSING GAME  ")
    print("=" * 60)
    print("\nWelcome! Try to guess the secret number.")
    print("You'll get hints after each guess (higher/lower).")
    print("The fewer attempts you use, the higher your score!")
    print("=" * 60)

def display_menu():
    """Display main menu"""
    print("\n" + "-" * 60)
    print("MAIN MENU")
    print("-" * 60)
    print("1. Play Game")
    print("2. View Statistics")
    print("3. How to Play")
    print("4. Change Difficulty")
    print("5. Exit")
    print("-" * 60)

def select_difficulty():
    """Let user select game difficulty"""
    print("\n" + "=" * 60)
    print("SELECT DIFFICULTY")
    print("=" * 60)
    print("1. Easy   - Numbers 1-50,  10 attempts")
    print("2. Medium - Numbers 1-100, 7 attempts")
    print("3. Hard   - Numbers 1-200, 5 attempts")
    print("=" * 60)
    
    while True:
        choice = input("\nSelect difficulty (1-3): ")
        
        if choice == '1':
            return {"name": "Easy", "range": 50, "attempts": 10}
        elif choice == '2':
            return {"name": "Medium", "range": 100, "attempts": 7}
        elif choice == '3':
            return {"name": "Hard", "range": 200, "attempts": 5}
        else:
            print("✗ Invalid choice! Please select 1, 2, or 3.")

def calculate_score(attempts_used, max_attempts):
    """
    Calculate score based on attempts used
    Perfect score = 1000 points
    """
    if attempts_used == 1:
        return 1000  # Lucky first guess!
    else:
        # Score decreases with more attempts
        percentage = (max_attempts - attempts_used + 1) / max_attempts
        return int(1000 * percentage)

def play_game(difficulty, stats):
    """Main game logic"""
    # Generate random secret number
    secret_number = random.randint(1, difficulty["range"])
    attempts_left = difficulty["attempts"]
    attempts_used = 0
    guess_history = []
    
    print("\n" + "=" * 60)
    print(f" GAME START - {difficulty['name']} Mode")
    print("=" * 60)
    print(f"Guess a number between 1 and {difficulty['range']}")
    print(f"You have {attempts_left} attempts")
    print("=" * 60)
    
    # Game loop
    while attempts_left > 0:
        print(f"\n Attempts remaining: {attempts_left}")
        
        # Show guess history if any
        if guess_history:
            print(f"Previous guesses: {', '.join(map(str, guess_history))}")
        
        # Get user guess
        guess_input = input("Enter your guess: ")
        
        # Validate input
        if not guess_input.isdigit():
            print("✗ Please enter a valid number!")
            continue
        
        guess = int(guess_input)
        
        # Check if guess is in valid range
        if guess < 1 or guess > difficulty["range"]:
            print(f"✗ Please guess between 1 and {difficulty['range']}!")
            continue
        
        # Check if already guessed
        if guess in guess_history:
            print("You already guessed that number!")
            continue
        
        # Add to history
        guess_history.append(guess)
        attempts_left -= 1
        attempts_used += 1
        
        # Check if correct
        if guess == secret_number:
            # WON!
            score = calculate_score(attempts_used, difficulty["attempts"])
            
            print("\n" + "🎉" * 20)
            print("🎊 CONGRATULATIONS! YOU WON! 🎊")
            print("🎉" * 20)
            print(f"\n✓ Correct! The number was {secret_number}")
            print(f"✓ You guessed it in {attempts_used} attempts")
            print(f"✓ Your score: {score} points")
            print("=" * 60)
            
            # Update statistics
            stats["games_played"] += 1
            stats["games_won"] += 1
            stats["total_attempts"] += attempts_used
            
            # Update best score for this difficulty
            diff_key = f"best_score_{difficulty['name'].lower()}"
            if diff_key not in stats or score > stats[diff_key]:
                stats[diff_key] = score
                print(f"🏆 NEW HIGH SCORE for {difficulty['name']} mode!")
            
            return True
        
        elif guess < secret_number:
            print("📈 Too low! Try a higher number.")
        else:
            print("📉 Too high! Try a lower number.")
        
        # Give additional hints based on how close
        difference = abs(guess - secret_number)
        if difference <= 5:
            print("🔥 You're very close!")
        elif difference <= 10:
            print("🌡️  Getting warm...")
        elif difference <= 20:
            print("❄️  Getting cold...")
    
    # Out of attempts - LOST
    print("\n" + "💔" * 20)
    print("😢 GAME OVER! YOU LOST!")
    print("💔" * 20)
    print(f"\n✗ The secret number was: {secret_number}")
    print(f"✗ You used all {difficulty['attempts']} attempts")
    print(f"Your guesses: {', '.join(map(str, guess_history))}")
    print("=" * 60)
    
    # Update statistics
    stats["games_played"] += 1
    stats["games_lost"] += 1
    stats["total_attempts"] += attempts_used
    
    return False

def view_statistics(stats):
    """Display game statistics"""
    print("\n" + "=" * 60)
    print("📊 GAME STATISTICS")
    print("=" * 60)
    
    if stats["games_played"] == 0:
        print("No games played yet! Start playing to see statistics.")
        print("=" * 60)
        return
    
    # Calculate win rate
    win_rate = (stats["games_won"] / stats["games_played"]) * 100
    avg_attempts = stats["total_attempts"] / stats["games_played"]
    
    print(f"Total Games Played:    {stats['games_played']}")
    print(f"Games Won:             {stats['games_won']}")
    print(f"Games Lost:            {stats['games_lost']}")
    print(f"Win Rate:              {win_rate:.1f}%")
    print(f"Average Attempts:      {avg_attempts:.1f}")
    
    # Best scores per difficulty
    print("\n🏆 HIGH SCORES:")
    print("-" * 60)
    
    for difficulty in ["easy", "medium", "hard"]:
        key = f"best_score_{difficulty}"
        if key in stats and stats[key] > 0:
            print(f"{difficulty.title():<10} {stats[key]} points")
        else:
            print(f"{difficulty.title():<10} Not played yet")
    
    print("=" * 60)

def show_instructions():
    """Display game instructions"""
    print("\n" + "=" * 60)
    print("📖 HOW TO PLAY")
    print("=" * 60)
    print("\n1. Select your difficulty level:")
    print("   - Easy: Numbers 1-50, 10 attempts")
    print("   - Medium: Numbers 1-100, 7 attempts")
    print("   - Hard: Numbers 1-200, 5 attempts")
    print("\n2. The computer will think of a secret number")
    print("\n3. Try to guess the number!")
    print("   - You'll get hints: 'Too high' or 'Too low'")
    print("   - Distance hints: Very close, Warm, Cold")
    print("\n4. Win by guessing correctly within attempts")
    print("\n5. Score System:")
    print("   - Fewer attempts = Higher score")
    print("   - Maximum score: 1000 points")
    print("   - First guess bonus: 1000 points")
    print("\n6. Track your statistics and high scores!")
    print("=" * 60)

def main():
    """Main program"""
    # Initialize game statistics
    stats = {
        "games_played": 0,
        "games_won": 0,
        "games_lost": 0,
        "total_attempts": 0,
        "best_score_easy": 0,
        "best_score_medium": 0,
        "best_score_hard": 0
    }
    
    # Default difficulty
    current_difficulty = {"name": "Medium", "range": 100, "attempts": 7}
    
    # Display welcome message
    display_welcome()
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            # Play game
            won = play_game(current_difficulty, stats)
            
            # Ask to play again
            play_again = input("\n🎮 Play again? (yes/no): ").lower()
            if play_again != 'yes' and play_again != 'y':
                continue
            else:
                # Option to change difficulty
                change = input("Change difficulty? (yes/no): ").lower()
                if change == 'yes' or change == 'y':
                    current_difficulty = select_difficulty()
        
        elif choice == '2':
            # View statistics
            view_statistics(stats)
        
        elif choice == '3':
            # How to play
            show_instructions()
        
        elif choice == '4':
            # Change difficulty
            current_difficulty = select_difficulty()
            print(f"\n✓ Difficulty set to: {current_difficulty['name']}")
        
        elif choice == '5':
            # Exit
            print("\n" + "=" * 60)
            print("👋 Thanks for playing!")
            
            if stats["games_played"] > 0:
                print("\n📊 FINAL STATISTICS:")
                print("-" * 60)
                print(f"Games Played: {stats['games_played']}")
                print(f"Games Won: {stats['games_won']}")
                win_rate = (stats['games_won'] / stats['games_played']) * 100
                print(f"Win Rate: {win_rate:.1f}%")
            
            print("\nCome back soon! 🎮")
            print("=" * 60)
            break
        
        else:
            print("\n✗ Invalid choice! Please select 1-5.")

# Run the game
if __name__ == "__main__":
    main()