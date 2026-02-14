# RPG Character System - Day 18 Practice Project
# Demonstrates inheritance, polymorphism, abstract classes, and advanced OOP

from abc import ABC, abstractmethod
import random

# ===== ABSTRACT BASE CLASS =====

class Character(ABC):
    """Abstract base class for all characters."""
    
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = 1
        self.experience = 0
    
    @abstractmethod
    def special_ability(self, target):
        """Each character must implement their special ability."""
        pass
    
    def basic_attack(self, target):
        """Basic attack available to all characters."""
        damage = max(0, self.attack - target.defense + random.randint(-5, 5))
        target.take_damage(damage)
        return f"{self.name} attacks {target.name} for {damage} damage!"
    
    def take_damage(self, amount):
        """Take damage and check if defeated."""
        self.health = max(0, self.health - amount)
        if self.health == 0:
            return f"{self.name} has been defeated!"
        return f"{self.name} has {self.health}/{self.max_health} HP remaining"
    
    def heal(self, amount):
        """Heal character."""
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        healed = self.health - old_health
        return f"{self.name} healed for {healed} HP!"
    
    def is_alive(self):
        """Check if character is still alive."""
        return self.health > 0
    
    def gain_experience(self, amount):
        """Gain experience and level up if threshold reached."""
        self.experience += amount
        if self.experience >= 100 * self.level:
            self.level_up()
    
    def level_up(self):
        """Increase level and stats."""
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack += 5
        self.defense += 3
        print(f" {self.name} leveled up to Level {self.level}!")
    
    def get_stats(self):
        """Display character stats."""
        return (f"{self.name} (Lv.{self.level})\n"
                f"  HP: {self.health}/{self.max_health}\n"
                f"  Attack: {self.attack}\n"
                f"  Defense: {self.defense}\n"
                f"  XP: {self.experience}")
    
    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}, Lv.{self.level})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.health})"


# ===== WARRIOR CLASS =====

class Warrior(Character):
    """Strong melee fighter with high health and defense."""
    
    def __init__(self, name):
        super().__init__(name, health=150, attack=25, defense=15)
        self.rage = 0
    
    def special_ability(self, target):
        """Berserker Rage - powerful attack that costs health."""
        self_damage = 10
        self.health = max(1, self.health - self_damage)
        
        damage = int(self.attack * 2 - target.defense)
        target.take_damage(damage)
        
        self.rage = min(100, self.rage + 20)
        
        return (f" {self.name} uses BERSERKER RAGE!\n"
                f"   Deals {damage} damage to {target.name}!\n"
                f"   Takes {self_damage} self-damage. Rage: {self.rage}")
    
    def shield_bash(self, target):
        """Stun attack with reduced damage."""
        damage = int(self.attack * 0.8 - target.defense)
        target.take_damage(damage)
        return f"🛡️  {self.name} shield bashes {target.name} for {damage} damage!"


# ===== MAGE CLASS =====

class Mage(Character):
    """Magic user with powerful spells but low defense."""
    
    def __init__(self, name):
        super().__init__(name, health=80, attack=35, defense=5)
        self.mana = 100
        self.max_mana = 100
    
    def special_ability(self, target):
        """Fireball - powerful magic attack costing mana."""
        mana_cost = 30
        
        if self.mana < mana_cost:
            return f" {self.name} doesn't have enough mana! ({self.mana}/{mana_cost})"
        
        self.mana -= mana_cost
        damage = int(self.attack * 1.5)
        target.take_damage(damage)
        
        return (f"🔥 {self.name} casts FIREBALL!\n"
                f"   Deals {damage} damage to {target.name}!\n"
                f"   Mana: {self.mana}/{self.max_mana}")
    
    def restore_mana(self, amount=20):
        """Restore mana."""
        self.mana = min(self.max_mana, self.mana + amount)
        return f"✨ {self.name} restored {amount} mana! ({self.mana}/{self.max_mana})"
    
    def get_stats(self):
        """Override to include mana."""
        base = super().get_stats()
        return f"{base}\n  Mana: {self.mana}/{self.max_mana}"


# ===== ARCHER CLASS =====

class Archer(Character):
    """Ranged attacker with critical hit chance."""
    
    def __init__(self, name):
        super().__init__(name, health=100, attack=30, defense=10)
        self.arrows = 20
        self.crit_chance = 0.25  # 25% crit chance
    
    def special_ability(self, target):
        """Multi-shot - attack multiple times."""
        if self.arrows < 3:
            return f" {self.name} doesn't have enough arrows! ({self.arrows}/3)"
        
        self.arrows -= 3
        total_damage = 0
        
        result = f"🏹 {self.name} uses MULTI-SHOT!\n"
        
        for i in range(3):
            damage = int(self.attack * 0.6 - target.defense)
            total_damage += damage
            result += f"   Arrow {i+1}: {damage} damage\n"
        
        target.take_damage(total_damage)
        result += f"   Total: {total_damage} damage! Arrows: {self.arrows}"
        
        return result
    
    def critical_strike(self, target):
        """Attack with chance for critical hit."""
        is_crit = random.random() < self.crit_chance
        
        if self.arrows < 1:
            return f" {self.name} is out of arrows!"
        
        self.arrows -= 1
        
        if is_crit:
            damage = int((self.attack * 2 - target.defense))
            target.take_damage(damage)
            return f" CRITICAL HIT! {self.name} deals {damage} damage to {target.name}!"
        else:
            damage = max(0, self.attack - target.defense)
            target.take_damage(damage)
            return f" {self.name} shoots {target.name} for {damage} damage"
    
    def get_stats(self):
        """Override to include arrows."""
        base = super().get_stats()
        return f"{base}\n  Arrows: {self.arrows}"


# ===== HEALER CLASS =====

class Healer(Character):
    """Support class that can heal allies."""
    
    def __init__(self, name):
        super().__init__(name, health=90, attack=15, defense=8)
        self.healing_power = 40
    
    def special_ability(self, target):
        """Heal target (including self)."""
        heal_amount = self.healing_power + random.randint(-5, 10)
        old_health = target.health
        target.heal(heal_amount)
        actual_heal = target.health - old_health
        
        return f" {self.name} heals {target.name} for {actual_heal} HP!"
    
    def group_heal(self, targets):
        """Heal multiple targets."""
        heal_amount = int(self.healing_power * 0.6)
        result = f" {self.name} casts GROUP HEAL!\n"
        
        for target in targets:
            if target.is_alive():
                target.heal(heal_amount)
                result += f"   {target.name} +{heal_amount} HP\n"
        
        return result


# ===== ENEMY CLASSES =====

class Goblin(Character):
    """Weak enemy - good for beginners."""
    
    def __init__(self, name="Goblin"):
        super().__init__(name, health=50, attack=15, defense=5)
    
    def special_ability(self, target):
        """Sneaky stab."""
        damage = int(self.attack * 1.2)
        target.take_damage(damage)
        return f"  {self.name} sneakily stabs {target.name} for {damage} damage!"


class Dragon(Character):
    """Powerful boss enemy."""
    
    def __init__(self, name="Dragon"):
        super().__init__(name, health=300, attack=40, defense=20)
        self.fire_breath_cooldown = 0
    
    def special_ability(self, target):
        """Fire breath attack."""
        damage = int(self.attack * 2)
        target.take_damage(damage)
        return f" {self.name} breathes fire! {target.name} takes {damage} damage!"


# ===== GAME FUNCTIONS =====

def battle(character1, character2):
    """Simple 1v1 battle."""
    print(f"\n  BATTLE START: {character1.name} vs {character2.name}!")
    print(f"{character1.get_stats()}")
    print(f"\n{character2.get_stats()}\n")
    
    turn = 1
    while character1.is_alive() and character2.is_alive():
        print(f"--- Turn {turn} ---")
        
        # Character 1 attacks
        if random.random() < 0.7:  # 70% normal attack
            print(character1.basic_attack(character2))
        else:  # 30% special
            print(character1.special_ability(character2))
        
        if not character2.is_alive():
            print(f"\n🏆 {character1.name} wins!")
            character1.gain_experience(50)
            break
        
        # Character 2 attacks
        if random.random() < 0.7:
            print(character2.basic_attack(character1))
        else:
            print(character2.special_ability(character1))
        
        if not character1.is_alive():
            print(f"\n🏆 {character2.name} wins!")
            character2.gain_experience(50)
            break
        
        print()
        turn += 1


def demonstrate_polymorphism():
    """Show polymorphism in action."""
    print("\n=== POLYMORPHISM DEMONSTRATION ===")
    
    characters = [
        Warrior("Conan"),
        Mage("Gandalf"),
        Archer("Legolas"),
        Healer("Mercy")
    ]
    
    dummy = Goblin("Training Dummy")
    dummy.health = 1000  # Make it survive
    
    print(f"All characters attacking {dummy.name}:\n")
    
    for char in characters:
        # Same method call, different implementation!
        print(char.special_ability(dummy))
        print()


def create_party():
    """Create a party of heroes."""
    return [
        Warrior("Warrior"),
        Mage("Mage"),
        Archer("Archer"),
        Healer("Healer")
    ]


# ===== MAIN MENU =====

def display_menu():
    """Display main menu."""
    print("\n" + "="*60)
    print("          RPG CHARACTER SYSTEM ⚔️")
    print("="*60)
    print("1. View Character Classes")
    print("2. Create Custom Character")
    print("3. Demonstrate Polymorphism")
    print("4. Quick Battle (Warrior vs Goblin)")
    print("5. Boss Battle (Party vs Dragon)")
    print("6. Compare Characters")
    print("7. Exit")
    print("="*60)


def main():
    """Main program."""
    print("="*60)
    print("   Welcome to RPG Character System!")
    print("="*60)
    print("\nDemonstrates:")
    print("✓ Inheritance (Character → Warrior, Mage, etc.)")
    print("✓ Abstract Base Classes (Character.special_ability)")
    print("✓ Polymorphism (Same method, different behaviors)")
    print("✓ Method Overriding (get_stats in Mage, Archer)")
    print("✓ super() for parent class methods")
    
    while True:
        display_menu()
        choice = input("\nEnter choice (1-7): ")
        
        try:
            if choice == '1':
                print("\n=== CHARACTER CLASSES ===")
                classes = {
                    "Warrior": "High HP/Defense, Berserker Rage",
                    "Mage": "High Attack, Fireball spell",
                    "Archer": "Critical hits, Multi-shot",
                    "Healer": "Support, Group heal"
                }
                for cls, desc in classes.items():
                    print(f"{cls}: {desc}")
            
            elif choice == '2':
                print("\n=== CREATE CHARACTER ===")
                print("1. Warrior")
                print("2. Mage")
                print("3. Archer")
                print("4. Healer")
                
                cls_choice = input("Choose class (1-4): ")
                name = input("Enter name: ")
                
                if cls_choice == '1':
                    char = Warrior(name)
                elif cls_choice == '2':
                    char = Mage(name)
                elif cls_choice == '3':
                    char = Archer(name)
                elif cls_choice == '4':
                    char = Healer(name)
                else:
                    print("Invalid choice!")
                    continue
                
                print(f"\n✓ Created: {char}")
                print(char.get_stats())
            
            elif choice == '3':
                demonstrate_polymorphism()
            
            elif choice == '4':
                warrior = Warrior("Hero")
                goblin = Goblin()
                battle(warrior, goblin)
            
            elif choice == '5':
                print("\n=== BOSS BATTLE ===")
                party = create_party()
                dragon = Dragon("Ancient Dragon")
                
                print(f"Party vs {dragon.name}!")
                for hero in party:
                    print(f"  - {hero.name} ({hero.__class__.__name__})")
                
                input("\nPress Enter to start battle...")
                
                # Simplified party battle
                turn = 1
                while dragon.is_alive() and any(h.is_alive() for h in party):
                    print(f"\n--- Turn {turn} ---")
                    
                    # Party attacks
                    for hero in party:
                        if hero.is_alive():
                            print(hero.special_ability(dragon))
                            if not dragon.is_alive():
                                break
                    
                    if not dragon.is_alive():
                        print(f"\n🏆 The party defeated {dragon.name}!")
                        break
                    
                    # Dragon attacks random hero
                    alive_heroes = [h for h in party if h.is_alive()]
                    if alive_heroes:
                        target = random.choice(alive_heroes)
                        print(dragon.special_ability(target))
                    
                    turn += 1
                    
                    if turn > 10:  # Prevent infinite battle
                        print("\nBattle timeout!")
                        break
            
            elif choice == '6':
                print("\n=== CHARACTER COMPARISON ===")
                characters = [
                    Warrior("Warrior"),
                    Mage("Mage"),
                    Archer("Archer"),
                    Healer("Healer")
                ]
                
                for char in characters:
                    print(f"\n{char.get_stats()}")
            
            elif choice == '7':
                print("\n" + "="*60)
                print("Thanks for exploring RPG Character System!")
                print("\nOOP Concepts Demonstrated:")
                print("✓ Inheritance hierarchy")
                print("✓ Abstract base classes")
                print("✓ Polymorphism in action")
                print("✓ Method overriding")
                print("✓ super() usage")
                print("\nGoodbye! ")
                print("="*60)
                break
            
            else:
                print("\n✗ Invalid choice!")
        
        except Exception as e:
            print(f"\n✗ Error: {e}")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
