class Player:
    def play(self):
        print("The player is playing cricket.")
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
if __name__ == "__main__":
    batsman = Batsman()
    bowler = Bowler()
    batsman.play()
    bowler.play()