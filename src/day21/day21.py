


class Item:

    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

def simulate_fight(list_of_items):
    boss_hit_points = 100
    boss_armor = 2
    boss_damage = 8
    player_hit_points = 100
    player_armor = 0
    player_damage = 0
    for item in list_of_items:
        player_armor += item.armor
        player_damage += item.damage
    print("player armor: {}, player damage: {}".format(player_armor, player_damage))
    boss_effective_damage = max(1, boss_damage - player_armor)
    player_effective_damage = max(1, player_damage - boss_armor)
    round = 1
    while player_hit_points > 0 and boss_hit_points >0:
        # players turn
        boss_hit_points -= player_effective_damage
        if boss_hit_points <= 0:
            break
        player_hit_points -= boss_effective_damage
        print("after round {}: boss_hit_points: {}, player_hit_points: {}".format(round, boss_hit_points, player_hit_points))
    return boss_hit_points <= 0

weapons = []
armors = []
rings = []
# parse the shop
parse_weapons = False
parse_armor = False
parse_rings = False
file1 = open('test.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    if "Weapons:" in input_line:
        parse_weapons = True
        continue
    if "Armor:" in input_line:
        parse_armor = True
        continue
    if "Rings:" in input_line:
        parse_rings = True
        continue
    split_string = input_line.split(" ")
    print(split_string)
    current_item = Item(split_string[0], int(split_string[1]), int(split_string[2]), int(split_string[3]))
    if parse_rings:
        rings.append(current_item)
    elif parse_armor:
        armors.append(current_item)
    elif parse_weapons:
        weapons.append(current_item)

print("Number of weapons: {}".format(len(weapons)))
print("Number of armor: {}".format(len(armors)))
print("Number of rings: {}".format(len(rings)))



# get all valid combinations:
count = 0
min_cost = 999
max_cost = 0
for weapon in weapons:
    for armor in armors:
        # 0 rings
        current_items = [weapon, armor]
        result = simulate_fight(current_items)
        if result:
            count += 1
            costs = 0
            for item in current_items:
                costs += item.cost
            min_cost = min(min_cost, costs)
        else:
            costs = 0
            for item in current_items:
                costs += item.cost
            max_cost = max(max_cost, costs)
for weapon in weapons:
    for armor in armors:
        # 1 rings
        for ring in rings:
            current_items = [weapon, armor, ring]
            result = simulate_fight(current_items)
            if result:
                count += 1
                costs = 0
                for item in current_items:
                    costs += item.cost
                min_cost = min(min_cost, costs)
            else:
                costs = 0
                for item in current_items:
                    costs += item.cost
                max_cost = max(max_cost, costs)
for weapon in weapons:
    for armor in armors:
        # 2 rings
        for ring in rings:
            for ring2 in rings:
                if ring2 != ring:
                    current_items = [weapon, armor, ring, ring2]
                    result = simulate_fight(current_items)
                    if result:
                        count += 1
                        costs = 0
                        for item in current_items:
                            costs += item.cost
                        min_cost = min(min_cost, costs)
                    else:
                        costs = 0
                        for item in current_items:
                            costs += item.cost
                        max_cost = max(max_cost, costs)


print("won fights: {}".format(count))

print("TASK 1 - Min coasts: {}".format(min_cost))

print("TASK 2 - Max cost and lose: {}".format(max_cost))
