import itertools


def simulate_fight(list_of_spells):
    boss_hit_points = 51
    boss_damage = 9
    player_hit_points = 50
    player_mana = 500
    shield_counter = 0
    poison_counter = 0
    recharge_counter = 0

    round = 0
    while player_hit_points > 0 and boss_hit_points >0:
        # players turn
        # print("-- Player turn --")
        # print("- Player has {} hit points, {} mana".format(player_hit_points, player_mana))
        # print("- Boss has {} hit points".format(boss_hit_points))
        # part 2
        player_hit_points -= 1
        if player_hit_points <=0:
            return False
        if recharge_counter > 0:
            recharge_counter -= 1
            player_mana += 101
            # print("Recharge provides 101 mana; its timer is now {}.".format(recharge_counter))
        if poison_counter > 0:
            poison_counter -= 1
            boss_hit_points -= 3
        if boss_hit_points <= 0:
            break
        if shield_counter > 0:
            shield_counter -=1
        if round >= len(list_of_spells):
            return False
        spell = list_of_spells[round]
        # print("Spell: " + spell)
        if spell == "Magic Missile":
            if player_mana - 53 < 0:
                return False
            player_mana -= 53
            boss_hit_points -= 4
        elif spell == "Drain":
            if player_mana - 73 < 0:
                return False
            player_mana -= 73
            boss_hit_points -= 2
            player_hit_points += 2
        elif spell == "Shield":
            if player_mana - 113 < 0 or shield_counter > 0:
                return False
            player_mana -= 113
            shield_counter = 6
        elif spell == "Poison":
            if player_mana - 173 < 0 or poison_counter > 0:
                return False
            player_mana -= 173
            poison_counter = 6
        elif spell == "Recharge":
            if player_mana - 229 < 0 or recharge_counter > 0:
                return False
            player_mana -= 229
            recharge_counter = 5
        # print()

        # boss turn
        # print("-- Boss turn --")
        # print("- Player has {} hit points, {} mana".format(player_hit_points, player_mana))
        # print("- Boss has {} hit points".format(boss_hit_points))
        if recharge_counter > 0:
            recharge_counter -= 1
            player_mana += 101
            # print("Recharge provides 101 mana; its timer is now {}.".format(recharge_counter))
        if poison_counter > 0:
            poison_counter -= 1
            boss_hit_points -= 3
        if boss_hit_points <= 0:
            break
        if shield_counter > 0:
            shield_counter -=1
            player_hit_points -= max(1, boss_damage - 7)
            # print("Boss attacks for {} damage!".format(max(1, boss_damage - 7)))
        else:
            player_hit_points -= boss_damage
            # print("Boss attacks for 8 damage!")
        round += 1
        # print()
    return boss_hit_points <= 0


possible_spells= ["Recharge", "Shield", "Drain", "Poison", "Magic Missile"]

won_fights = 0
min_mana = -1
for i in range(11):
    # get all possible spell combinations of length i
    possible_combinations = list(itertools.product(possible_spells, repeat=i))

    for combination in possible_combinations:
        result = simulate_fight(list(combination))
        if result:
            won_fights += 1
            mana_cost = 0
            for spell in list(combination):
                if spell == "Magic Missile":
                    mana_cost += 53
                elif spell == "Drain":
                    mana_cost += 73
                elif spell == "Shield":
                    mana_cost += 113
                elif spell == "Poison":
                    mana_cost += 173
                elif spell == "Recharge":
                    mana_cost += 229
            if min_mana == -1:
                min_mana = mana_cost
            else:
                min_mana = min(min_mana, mana_cost)
    print("round: {}, possible combinations: {}, won: {}, min_mana: {}".format(i, len(possible_combinations), won_fights, min_mana))
print("TASK 1 - won fights: {}".format(won_fights))

print("TASK 2 - ")
