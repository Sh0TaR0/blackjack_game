# ぐーれ
# ? ブラックジャックは、ディーラーとプレイヤーにカードが配られ、
# ? その合計値が「２１」に近いほうが勝ちというカードゲームです。

# * ディーラーとプレイヤー全員に２枚ずつカードが配られます。
# * ディーラーのカードは１枚伏せた状態となります。
# * 自分のカードの合計値が２１に近づくよう、
# * ヒットしてカードを追加したり、追加しないスタンドを選択します。
# * カードの合計値が２１を超えてしまった時点で、その場で負けが決定します。
# * プレイヤーは２１を超えない限り好きなだけカードを追加することができます。
# * ディーラーはカードの合計値が１７を超えるまでカードを追加しなければなりません。

# ! 2〜9のカード = そのまま2〜9として数えます。
# ! 10と絵札(J,Q,K)のカード = 10として数えます。
# ! Aのカード = 1か11として有利な方で数えます。

# ? プログラミング的思考
#  (deck) トランプを作る: 得点を数えられうように数字
#  (deal) トランプを２枚配る: 絵札(J,Q,K)で表示させる
#  (hand) プレイヤーに配られたカードを記録する
#  (hit) ヒットの場合 hand を追加する
#  (game) 実際にプレーする
#  (total) プレイヤーの合計を求める
# TODO (result) 勝ち負けを表記する
#  (play_again) もう１度プレイするか確認する

import random


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4


def deal():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 1:
            card = "A"
        hand.append(card)
    return hand


def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 1:
        card = "A"
    hand.append(card)
    return hand


def total(hand):
    score = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score = score + 10
        elif card == "A":
            if score >= 11:
                score = score + 1
            else:
                score += 11
        else:
            score += card
    return score


def play_again():
    again = input("もう１度プレイしますか？ (Y/N): ")
    if again == "y" or again == "Y":
        # game()
        return
    else:
        print("お疲れ様でした！")
        exit()


def game():
    dealer_hand = deal()
    player_hand = deal()
    print(f"ディーラーのカードは {dealer_hand[0]} です。")
    print(f"プレイヤーのカードは　{player_hand}　合計が　{total(player_hand)}　です。")

    choice = 0

    while choice != quit:
        choice = input("ヒットしますか？　スタンドしますか？　(HIT/STAND): ").lower()
        if choice == "hit":
            hit(player_hand)
            print(
                f"\nあなたに {player_hand[-1]}　が配られ、カードは {player_hand}　合計は {total(player_hand)} です。")
            if total(player_hand) > 21:
                print("あなたは　21 を超えてしまいました。 YOU LOSE...")
                choice = quit

        elif choice == "stand":
            print(
                f"\nディーラーの２枚めのカードは {dealer_hand[1]}　合計は {total(dealer_hand)} です。")
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(
                    f"ディーラー {dealer_hand[-1]}　が配られ、カードは {dealer_hand}　合計は {total(dealer_hand)} です。")
                if total(dealer_hand) > 21:
                    print("ディーラーは　21 を超えてしまいました。 YOU WIN!")
                    choice = quit

            # result()
            choice = quit


game()
