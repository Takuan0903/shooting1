import random
import time


def slow_print(text, delay=0.02):
    """文字を少しずつ表示する演出"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def create_player(name):
    return {
        "name": name,
        "level": 1,
        "hp": 40,
        "max_hp": 40,
        "attack": 10,
        "exp": 0,
        "potions": 3,
    }


def show_status(player):
    print("\n===== ステータス =====")
    print(f"名前: {player['name']}")
    print(f"Lv: {player['level']}")
    print(f"HP: {player['hp']} / {player['max_hp']}")
    print(f"攻撃力: {player['attack']}")
    print(f"経験値: {player['exp']}")
    print(f"回復薬: {player['potions']}個")
    print("====================\n")


def level_up(player):
    needed_exp = player["level"] * 20

    if player["exp"] >= needed_exp:
        player["exp"] -= needed_exp
        player["level"] += 1
        player["max_hp"] += 15
        player["attack"] += 5
        player["hp"] = player["max_hp"]

        slow_print(f"\n{player['name']}はレベルアップした！")
        slow_print(f"レベル {player['level']} になった！")
        slow_print("HPと攻撃力が上がり、HPが全回復した！\n")


def create_enemy(stage):
    enemies = [
        {"name": "スライム", "hp": 25, "attack": 6, "exp": 10},
        {"name": "ゴブリン", "hp": 35, "attack": 8, "exp": 15},
        {"name": "影の狼", "hp": 45, "attack": 10, "exp": 20},
    ]

    if stage >= 4:
        return {"name": "黒き竜", "hp": 90, "attack": 15, "exp": 50}

    return random.choice(enemies)


def use_potion(player):
    if player["potions"] <= 0:
        slow_print("回復薬はもう残っていない！")
        return

    heal = 25
    player["hp"] = min(player["hp"] + heal, player["max_hp"])
    player["potions"] -= 1
    slow_print(f"{player['name']}は回復薬を使った！ HPが{heal}回復した。")


def battle(player, enemy):
    slow_print(f"\n{enemy['name']}が現れた！")

    while player["hp"] > 0 and enemy["hp"] > 0:
        print("\n行動を選んでください")
        print("1: 攻撃")
        print("2: 回復薬を使う")
        print("3: ステータスを見る")

        choice = input("> ")

        if choice == "1":
            damage = random.randint(player["attack"] - 3, player["attack"] + 5)
            damage = max(1, damage)
            enemy["hp"] -= damage
            slow_print(f"{player['name']}の攻撃！ {enemy['name']}に{damage}ダメージ！")

            if enemy["hp"] <= 0:
                slow_print(f"{enemy['name']}を倒した！")
                player["exp"] += enemy["exp"]
                slow_print(f"{enemy['exp']}経験値を手に入れた！")
                level_up(player)
                return True

            enemy_damage = random.randint(enemy["attack"] - 2, enemy["attack"] + 4)
            enemy_damage = max(1, enemy_damage)
            player["hp"] -= enemy_damage
            slow_print(f"{enemy['name']}の攻撃！ {player['name']}は{enemy_damage}ダメージを受けた！")

        elif choice == "2":
            use_potion(player)

            enemy_damage = random.randint(enemy["attack"] - 2, enemy["attack"] + 4)
            enemy_damage = max(1, enemy_damage)
            player["hp"] -= enemy_damage
            slow_print(f"{enemy['name']}の攻撃！ {player['name']}は{enemy_damage}ダメージを受けた！")

        elif choice == "3":
            show_status(player)

        else:
            slow_print("1、2、3のどれかを入力してください。")

    return False


def main():
    slow_print("=== 小さな冒険者の旅 ===\n")
    name = input("あなたの名前を入力してください: ").strip()

    if not name:
        name = "勇者"

    player = create_player(name)

    slow_print(f"\n{name}は、小さな村から旅立った。")
    slow_print("森の奥には、村を苦しめる黒き竜がいるという……。")

    for stage in range(1, 5):
        if stage < 4:
            slow_print(f"\n--- 第{stage}エリア ---")
            enemy = create_enemy(stage)
        else:
            slow_print("\n--- 最終エリア ---")
            slow_print("空気が重い。巨大な影がこちらを見下ろしている。")
            enemy = create_enemy(stage)

        won = battle(player, enemy)

        if not won:
            slow_print("\nあなたは倒れてしまった……。")
            slow_print("GAME OVER")
            return

        if stage < 4:
            slow_print("少し先へ進んだ。")
            if random.random() < 0.5:
                player["potions"] += 1
                slow_print("道端で回復薬を1個見つけた！")

    slow_print("\n黒き竜は地に倒れた。")
    slow_print("村に朝日が差し込み、人々は歓声を上げる。")
    slow_print(f"{player['name']}の冒険は、ここに一つの終わりを迎えた。")
    slow_print("\nCLEAR!")


if __name__ == "__main__":
    main()
