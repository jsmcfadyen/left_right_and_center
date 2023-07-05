import random;

class lrc_game:
    players = []
    isWinner = False
    curr_player_idx = -1
    winner_idx = -1
    def __init__(self, chip_number, player_count):
        self.players = [chip_number] * player_count
        self.chip_number = chip_number

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
            self.check_winner()
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
    
    def check_winner(self):
        if 1 == len(list(filter(lambda y: y > 0, self.players))):
            self.isWinner = True

def main():
    chip_number = 3
    player_count = 2
    print("hello")

    results = [0]*player_count
    num_iterations = 100000
    for i in range(num_iterations):
        game = lrc_game(chip_number, player_count)
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