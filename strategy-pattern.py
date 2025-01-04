from abc import ABC, abstractmethod
class Strategy(ABC): # Abstract Strategy
    @abstractmethod
    def game(self):
        pass
class Rock(Strategy): # Concrete Strategies
    def game(self):
        return "Rock"
class Paper(Strategy):
    def game(self):
        return "Paper"
class Scissors(Strategy):
    def game(self):
        return "Scissors"
def main():
    rock = Rock().game()
    paper = Paper().game()
    scissors = Scissors().game()
    print(f"The {rock} strategy")  
    print(f"The {paper} strategy")  
    print(f"The {scissors} strategy")
main()
