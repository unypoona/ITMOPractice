import json
from practice5_0 import play_round, determine_round_winner,create_player



def main():
    name1 = input('Введите имя 1-го играющего: ')
    name2 = input('Введите имя 2-го играющего: ')
    player1 = create_player(name1)
    player2 = create_player(name2)
    rounds = 5

    for i in range(rounds):
        print(f"Раунд {i + 1}")
        n1 = play_round(player1)
        n2 = play_round(player2)
        determine_round_winner(player1, player2, n1, n2)

    # Определение итогового победителя
    if player1['wins'] > player2['wins']:
        print('Итоговый победитель:', player1['name'])
    elif player1['wins'] < player2['wins']:
        print('Итоговый победитель:', player2['name'])
    else:
        print('Итоговая ничья')

    # Сохранение результатов игры в файл
    results = {"players": [player1, player2]}
    with open('game_results.json', 'w') as file:
        json.dump(results, file)


if __name__ == "__main__":
    main()