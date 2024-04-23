import random
# Created by Melissa Chessa (@nonverbalexpress) on 04/22/2024 for IT-140 class project
class Room:
    def __init__(self, name, items=None, directions=None, story=""):
        self.name = name
        self.items = items if items else []
        self.directions = directions if directions else {}
        self.story = story

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def reset_items(self, original_items):
        self.items = original_items

    def show_story(self):
        print(self.story)

    def investigate_crab(self, player):
        if "crab" in self.items:
            print("You see a curious crab holding something shiny.")
            choice = input("Do you want to investigate and try to grab the item? (Yes/No): ").lower()
            if choice == "yes":
                success = random.choice([True, False])  # Randomize success or failure
                if success:
                    item = "Seaglass"
                    self.remove_item("crab")
                    self.add_item(item)
                    player.add_to_inventory(item)
                    print(f"You successfully grabbed the {item} from the crab!")
                else:
                    print("Oops! The crab got startled and scurried away, dropping the item.")
        else:
            print("There's no crab here holding an item.")

    def play_high_low_game(self, player):
        print("\nYou encounter a mini-game to obtain the seaglass!")
        print("The crab is thinking of a number between 1 and 25.")
        number_to_guess = random.randint(1, 25)

        attempts = 0
        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                seaglass = "Seaglass"
                self.add_item(seaglass)
                player.add_to_inventory(seaglass)
                print(f"You obtained the {seaglass}!")
                break

    def play_word_game(self, player):
        print("\nYou encounter a word game to obtain the conch shell!")
        choice = input("Do you want to play the word game? (Yes/No): ").lower()
        if choice == "yes":
            ocean_names = ["pacific ocean", "indian ocean", "arctic ocean", "atlantic ocean"]
            word_to_guess = random.choice(ocean_names)
            scrambled_word = "".join(random.sample(word_to_guess, len(word_to_guess)))
            print("Scrambled Word:", scrambled_word)

            attempts = 0
            while True:
                guess = input("Enter your guess (e.g., Pacific Ocean): ").lower()
                attempts += 1

                if guess == word_to_guess:
                    print(f"Congratulations! You guessed it in {attempts} attempts.")
                    conch_shell = "Conch Shell"
                    self.add_item(conch_shell)
                    player.add_to_inventory(conch_shell)
                    print(f"You obtained the {conch_shell}!")
                    break
                else:
                    print("Incorrect guess. Try again!")
        else:
            print("You decided not to play the word game.")

    def play_mermaid_riddle(self, player):
        print("\nYou encounter a friendly mermaid amidst the wreckage.")

        # Check if the player already has the Pearl
        if "Pearl" in player.inventory:
            print("You already have the Pearl. No need to play the riddle again.")
            return

        choice = input("Do you want to hear her riddle? (Yes/No): ").lower()
        if choice == "yes":
            riddle = "I'm as blue as the sky,\nBut I'm not found up high.\nI dance with the tides,\nYet I never truly hide.\nWhat am I?"
            answer = "ocean"
            user_answer = input(f"\nRiddle: {riddle}\nYour answer: ").lower()
            if user_answer == answer:
                print("Correct! The mermaid smiles and gives you a treasure.")
                pearl = "Pearl"
                self.add_item(pearl)
                player.add_to_inventory(pearl)
                print(f"You obtained the {pearl}!")
            else:
                print("Incorrect answer.")
                hint_choice = input("Would you like a hint? (Yes/No): ").lower()
                if hint_choice == "yes":
                    print("Hint: One word. It's a vast body of water that covers most of the Earth's surface.")
                    user_answer = input("Your answer: ").lower()  # Prompt for answer again after hint
                    if user_answer == answer:
                        print("Correct! The mermaid smiles and gives you a treasure.")
                        pearl = "Pearl"
                        self.add_item(pearl)
                        player.add_to_inventory(pearl)
                        print(f"You obtained the {pearl}!")
                    else:
                        print("Incorrect answer.")
                        print("The mermaid giggles and wishes you luck on your journey.")
                else:
                    print("The mermaid giggles and wishes you luck on your journey.")
        else:
            print("You decide not to listen to the mermaid's riddle.")

    def find_coral_fragment(self, player):
        print("\nYou don a diving suit and explore the coral reef.")
        print("Charmer, your feline companion, is dressed in a funny-looking cat diving suit.")
        print("You discover a shimmering Coral Fragment!")
        choice = input("Do you want to take the Coral Fragment? (Yes/No): ").lower()
        if choice == "yes":
            coral_fragment = "Coral Fragment"
            self.add_item(coral_fragment)
            player.add_to_inventory(coral_fragment)
            print(f"You obtained the {coral_fragment}!")
        else:
            print("You decided to leave the Coral Fragment behind.")

    def find_seashell(self, player):
        print("\nYou step into the hidden cave, the sound of crashing waves echoing within.")
        print("Charmer playfully meows and it echoes, leading you to discover a gleaming Seashell!")
        seashell = "Seashell"
        self.add_item(seashell)
        player.add_to_inventory(seashell)
        print(f"You obtained the {seashell}!")

    def play_trivia_game(self, player):
        print("\nThe lighthouse keeper pets Charmer and asks you to play a trivia game about the ocean.")
        choice = input("Do you want to play the trivia game? (Yes/No): ").lower()
        if choice == "yes":
            print("Answer two out of the four questions correctly to obtain the Sand Dollar.")

            ocean_facts = {
                "What is the largest ocean on Earth?": "pacific ocean",
                "What percentage of the Earth’s surface is covered by oceans?": "71",
                "What’s the deepest point in the world’s oceans?": "mariana trench",
                "What phenomenon results in the rise and fall of sea levels daily?": "tide"
            }

            correct_answers = 0
            for question, answer in ocean_facts.items():
                user_answer = input(f"{question} ").lower()
                if user_answer == answer:
                    print("Correct!")
                    correct_answers += 1

            if correct_answers >= 2:
                sand_dollar = "Sand Dollar"
                self.add_item(sand_dollar)
                player.add_to_inventory(sand_dollar)
                print(f"You obtained the {sand_dollar}!")
            else:
                print("You didn't answer enough questions correctly. Try again later.")
        else:
            print("You decided not to play the trivia game.")

class Player:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def display_inventory(self):
        print("\nYour Beach Bag (Inventory):")
        if self.inventory:
            for item in self.inventory:
                print(item)
        else:
            print("Your Beach Bag is currently empty. Explore to add items!")

    def return_all_items(self, rooms):
        for item in self.inventory:
            for room in rooms.values():
                if item in room.items:
                    room.add_item(item)
                    break
        self.inventory.clear()

def main():
    # Define the rooms and their connections
    rooms = {
        "Sandy Shore": Room("Sandy Shore", directions={"east": "Tide Pools"},
                             story="\nAs you stand by the ocean's shore, a salty breeze tousles your hair."
                                   "\nBy your side is your orange and white feline companion and Charmer."
                                   "\nWith curious eyes, you watch as seagulls swoop low over the waves, their calls echoing against the vastness of the sea." 
                                   "\nJust as you bend down to gather a handful of seashells, a mischievous seagull swoops in and snatches your beach bag stealing your collection!" 
                                   "\nPrompting you and Charmer to embark on an unexpected adventure to retrieve your prized collection."),
        "Tide Pools": Room("Tide Pools", items=["crab"], directions={"west": "Sandy Shore", "north": "Rocky Cliffs",
                                                                       "south": "Hidden Cave", "east": "Lighthouse Point"},
                           story="You and Charmer approach the tide pool, drawn by the salty breeze." "\nWith curious eyes, you both discover a hidden world teeming with tiny crabs," 
                                 "\ncolorful sea stars, and shimmering seaweed, lost in the magic of nature's miniature kingdom."),
        "Rocky Cliffs": Room("Rocky Cliffs", items=["Conch Shell"],
                             directions={"south": "Tide Pools", "east": "Coral Reef"},
                             story="The salty breeze invigorating your senses."),
        "Coral Reef": Room("Coral Reef", items=["Coral Fragment"], directions={"west": "Rocky Cliffs"},
                           story="The colorful coral reef mesmerizes you with its vibrant hues."),
        "Hidden Cave": Room("Hidden Cave", items=["Seashell"], directions={"north": "Tide Pools",
                                                                            "east": "Shipwreck Cove"},
                            story="The sound of crashing waves echoes within."),
        "Shipwreck Cove": Room("Shipwreck Cove", items=["Pearl"], directions={"west": "Hidden Cave"},
                               story="The remnants of a forgotten pirate treasure."),
        "Lighthouse Point": Room("Lighthouse Point", items=["Sand Dollar"],
                                 directions={"north": "Seagull's Nest", "west": "Tide Pools"},
                                 story="You are in Lighthouse Point. The lighthouse casts its beacon over the vast ocean, guiding lost souls."),
        "Seagull's Nest": Room("Seagull's Nest",
                               story="You reach the seagull's nest, a perch overlooking the entire coastline. "
                                      "A seagull eyes your beach bag menacingly, ready to snatch it.")
    }

    # Initialize the player and starting room
    player = Player()
    current_room = rooms["Sandy Shore"]

    print("Welcome to Seashell Serenity! Your adventure begins.")
    print("Rules:")
    print("You must collect all 6 ocean treasures to bypass the seagull and win the game.")
    print("Failure to collect all items before entering the Seagull's Nest, you lose and the Seagull wins.")

    while True:
        print("\nYou are in", current_room.name)
        current_room.show_story()
        player.display_inventory()
        print("Available directions:", list(current_room.directions.keys()))

        if current_room.name == "Tide Pools" and "Seaglass" not in player.inventory:
            current_room.investigate_crab(player)
            if "Seaglass" in player.inventory:
                continue
            else:
                play_game = input("Do you want to play the mini-game to obtain the Seaglass? (Yes/No): ").lower()
                if play_game == "yes":
                    current_room.play_high_low_game(player)
                    if "Seaglass" in player.inventory:
                        continue
        elif current_room.name == "Rocky Cliffs" and "Conch Shell" not in player.inventory:
            play_game = input("Do you want to play the word game to obtain the Conch Shell? (Yes/No): ").lower()
            if play_game == "yes":
                current_room.play_word_game(player)
                if "Conch Shell" in player.inventory:
                    continue
            else:
                print("You decided not to play the word game.")

        elif current_room.name == "Lighthouse Point" and "Sand Dollar" not in player.inventory:
            play_game = input("Do you want to play a trivia game for the Sand Dollar? (Yes/No): ").lower()
            if play_game == "yes":
                current_room.play_trivia_game(player)
                if "Sand Dollar" in player.inventory:
                    continue
            else:
                print("You decided not to play the trivia game.")

        elif current_room.name == "Coral Reef":
            current_room.find_coral_fragment(player)

        elif current_room.name == "Hidden Cave":
            current_room.find_seashell(player)

        elif current_room.name == "Shipwreck Cove":
            play_game = input("Do you want to answer a riddle to obtain a pearl? (Yes/No): ")
            if play_game == "yes":
                current_room.play_mermaid_riddle(player)
                if "Pearl" in player.inventory:
                    continue
            else:
                print("You decided not to answer a riddle.")

        if current_room.name == "Seagull's Nest":
            if len(player.inventory) < 6:
                print("\nThe seagull cackles as you approach with a less than full beach bag.")
                print("The seagull succeeds in snatching your beach bag. You lose!")

                # Ask the player if they want to restart
                restart_choice = input("Do you want to restart the game? (Yes/No): ").lower()
                if restart_choice == "yes":
                    # Reset the game by emptying the inventory and returning all items to their original rooms
                    player.inventory.clear()
                    player.return_all_items(rooms)
                    current_room = rooms["Sandy Shore"]
                    continue
                else:
                    print("Thank you for playing! Fair winds and following seas, matey!")
                    break
            else:
                print(
                    "\nCharmer, your feline companion, scares away the seagull as you approach with your full beach bag.")
                print("Congratulations! You bypassed the seagull and won the game!")

                # Ask the player if they want to restart or quit
                restart_choice = input("Do you want to restart the game? (Yes/No): ").lower()
                if restart_choice == "yes":
                    # Reset the game by emptying the inventory and returning all items to their original rooms
                    player.inventory.clear()
                    player.return_all_items(rooms)
                    current_room = rooms["Sandy Shore"]
                    continue
                else:
                    print("Thank you for playing! Fair winds and following seas, matey!")
                    break

        command = input("Enter a direction (North, South, East, West) or 'Quit' to exit: ").lower()
        if command == "quit":
            print("Thank you for playing!")
            break

        if command in current_room.directions:
            current_room = rooms[current_room.directions[command]]  # Update current_room
        else:
            print("Invalid direction! Are you trying to sleep with the fishes! Please try again.")

if __name__ == "__main__":
    main()
