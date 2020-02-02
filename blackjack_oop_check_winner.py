def check_winner(self, player_hand, dealer_hand, game_over=False):
    if not game_over:
        if player_hand.calc_value() > 21:
            print('あなたは21を超えました. Dealer wins!')
            return True
        elif dealer_hand.calc_value() > 21:
            print('ディーラーは21を超えました. You win!')
            return True
        elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
            print('ふたりともブラックジャックです. Draw!')
            return True
        elif player_hand.is_blackjack():
            print('あなたはブラックジャックです! You win!')
            return True
        elif dealer_hand.is_blackjack():
            print('ディーラーはブラックジャックです! Dealer wins!')
            return True
    else:
        if player_hand.calc_value() > dealer_hand.calc_value():
            print('You win!')
        elif player_hand.calc_value() == dealer_hand.calc_value():
            print('Draw!')
        else:
            print('Dealer wins!')
        return True
    return False
