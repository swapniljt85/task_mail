import random


class ShootingGame:
    def __init__(self):
        self.guns = ["Pistol", "Shotgun", "Sniper"]
        self.animals = ["Deer", "Bear", "Rabbit"]
        self.points = 0

    def show_guns(self):
        print("Select a gun:")
        for i, gun in enumerate(self.guns, start=1):
            print(f"{i}. {gun}")

    def select_gun(self):
        choice = int(input("Enter the number of your chosen gun: "))
        if choice in [1, 2, 3]:
            return self.guns[choice - 1]
        else:
            print("Invalid choice. Try again.")
            return self.select_gun()

    def shoot_animal(self, selected_gun):
        target_animal = random.choice(self.animals)
        print(f"Target animal: {target_animal}")
        shot = input(f"Shoot {target_animal} with {selected_gun}? (yes/no): ").lower()
        if shot in ["yes", "y"]:
            points_earned = random.randint(1, 10)
            print(f"You earned {points_earned} points!")
            self.points += points_earned
        else:
            print("You missed!")

    def play_game(self):
        print("Welcome to the Shooting Game!")
        self.show_guns()
        selected_gun = self.select_gun()

        rounds = int(input('Enter number of shots for shoot:'))
        for _ in range(rounds):
            self.shoot_animal(selected_gun)

        print(f"\nGame over! Total points earned: {self.points}")


if __name__ == "__main__":
    game = ShootingGame()
    game.play_game()
