import random;

class lrc_game:
    players = []
    isWinner = False
    curr_player_idx = -1
    winner_idx = -1
    oneToken = False
    def __init__(self, chip_number, player_count, oneToken):
        self.players = [chip_number] * player_count
        self.chip_number = chip_number
        self.oneToken = oneToken

    def __str__(self):
        return str(self.players)
    
    def start(self):
        def getWinnerIdx(players):
            for i,val in enumerate(players):
                if val > 0:
                    return i
            return -1
        while( not self.isWinner):
            self.curr_player_idx = (self.curr_player_idx + 1) % len(self.players)
            self.take_turn()
        self.winner_idx = getWinnerIdx(self.players)
    
    def take_turn(self):
        count = self.players[self.curr_player_idx]
        if count == 0:
            return
        elif count == 1 or count == 2:
            for i in range(count):
                self.roll()
        elif count >= 3:
            for i in range(self.chip_number):
                self.roll()
    
    def roll(self):
        result = random.randint(1,6)
        if result == 4:
            # Left
            self.players[(self.curr_player_idx - 1) % len(self.players)] += 1
            self.players[self.curr_player_idx] -= 1
        elif result == 5:
            # Center
            self.players[self.curr_player_idx] -= 1
        elif result == 6:
            # Right 
            self.players[(self.curr_player_idx + 1) % len(self.players)] += 1
            self.players[self.curr_player_idx] -= 1
        self.check_winner()
    
    def check_winner(self):
        numPlayers = len(self.players)
        if self.oneToken:
            if self.players.count(0) == numPlayers - 1 and self.players.count(1) == 1:
                self.isWinner = True
        else:
            if 1 == len(list(filter(lambda y: y > 0, self.players))):
                self.isWinner = True

def main():
    chip_number = 3 
    player_count = 10
    oneToken = True
    num_iterations = 100000 
    print("hello")

    results = [0]*player_count
    for i in range(num_iterations):
        game = lrc_game(chip_number, player_count, oneToken)
        game.start()
        results[game.winner_idx] += 1
    percentage = [0]* player_count
    for i, val in enumerate(results):
        percentage[i] = val / num_iterations
    print(results)
    print(percentage)

    return



if __name__ == '__main__':
    main()