import numpy as np

class player:
    def __init__(self, identity, pay_off_matrix, utility):
        self.rep = 0
        self.j = identity
        self.pay_off_matrix = pay_off_matrix
        self.utility = utility
        pass

    def generate_long_term_utility(self, a, b):
        # a=0 is honest, a=1 is dishonest
        # b是另一个miner的策略
        omega = self.utility
        delta = 1 if a == 0 else -1
        t = abs(delta) / delta; dja = a
        if a == 0:
            rep = self.rep + 1
        else:
            rep = self.rep - 1
        fi = abs(rep*1.4)
        dish_numb = a + b
        long_term_utility = omega * (t * fi + dja + dja / (dish_numb + 1))
        return long_term_utility

    def generate_short_term_utility(self, a, b):
        # a=0 is honest, a=1 is dishonest
        # b是另一个miner的策略
        omega = self.utility
        dja = a
        dish_numb = a + b
        short_term_utility = omega * (dja + dja / (dish_numb + 1))
        return short_term_utility

    def choose_strategy(self):
        long_term_h2 = self.generate_long_term_utility(a=0,b=0)
        short_term_h2 = self.generate_short_term_utility(a=0, b=0)

        long_term_d1 = self.generate_long_term_utility(a=1,b=1)
        short_term_d1 = self.generate_short_term_utility(a=1, b=1)

        honest = long_term_h2 + short_term_h2
        dishonest = long_term_d1 + short_term_d1
        if honest > dishonest:
            self.rep += 1
            print("honest value: ", honest)
            print("dishonest value: ", dishonest)
            print("rep value: ", self.rep)
            return "honest"
        else:
            self.rep -= 1
            print("honest value: ", honest)
            print("dishonest value: ", dishonest)
            print("rep value: ", self.rep)
            return "dishonest"

class repeated_game:
    def __init__(self, unit_utility):
        self.utility = unit_utility
        self.pay_off_matrix = np.array([[(0, 0), (0, self.utility)],
                                       [(self.utility, 0), (self.utility/2, self.utility/2)]])
        self.player1 = player(1, pay_off_matrix=self.pay_off_matrix, utility=self.utility)
        self.player2 = player(2, pay_off_matrix=self.pay_off_matrix, utility=self.utility)
        pass

    def main(self):
        for i in range(40):
            player1_strategy = self.player1.choose_strategy()
            player2_strategy = self.player2.choose_strategy()
            print("Player1's strategy is: ", player1_strategy)
            print("Player2's strategy is: ", player2_strategy)
            print("")

if __name__ == "__main__":
    game = repeated_game(50)
    game.main()
    pass