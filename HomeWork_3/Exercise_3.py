MAX_WEIGHT = 10

things = {"Tent": 6, "Toolbox": 7, "Food/water": 5, "navigation": 1, "boat": 6,
          "Illumination": 2, "Ignition kit": 2, "Warm clothes": 3}


def get_all_set(things_set: dict[str, float], max_backpack_weight: float):
    things_list = list(enumerate(things_set.keys()))
    number_combinations = 2 ** len(things_list)
    valid_combinations = {}

    for comb in range(1, number_combinations):
        combination_bin = f"{bin(comb).replace('0b', ''):0>{len(things_list)}}"[::-1]
        current_set = frozenset({thing[1] for thing in things_list if combination_bin[thing[0]] == '1'})
        current_set_weight = sum([things_set[thing] for thing in current_set])
        if current_set_weight <= max_backpack_weight:
            valid_combinations[current_set] = current_set_weight

    return valid_combinations


def get_optimal_set_dynamic(things_set: dict[str, float], max_backpack_weight: float, weight_step: float) -> set[str]:
    things_list = list(enumerate(things_set.keys(), start=1))
    weights_list = list(enumerate([i * weight_step for i in range(int(max_backpack_weight / weight_step) + 1)]))

    d = [[0] * len(weights_list)]
    for i, current_thing in things_list:
        d.append([])
        w_i = int(things_set[current_thing] / weight_step)
        for c, current_weight in weights_list:
            if c < w_i or d[i - 1][c] > d[i - 1][c - w_i] + w_i:
                d[i].append(d[i - 1][c])
            else:
                d[i].append(d[i - 1][c - w_i] + w_i)

    result_set = set()

    def restore_result_set(k, s):
        nonlocal result_set, d, things_list, things_set, weight_step
        if d[k][s] == 0:
            return
        if d[k - 1][s] == d[k][s]:
            restore_result_set(k - 1, s)
        else:
            w_k = int(things_set[things_list[k - 1][1]] / weight_step)
            restore_result_set(k - 1, s - w_k)
            result_set.add(things_list[k - 1][1])

    restore_result_set(len(things_list), len(weights_list) - 1)

    return result_set


combinations = get_all_set(things, MAX_WEIGHT)
print("It's possible:")
for combination, weight in combinations.items():
    print(f"{combination}: mass {weight}")

optimal_combinations = {combination: weight for combination, weight in combinations.items() if
                        weight == max(combinations.values())}

print("\n------------------\noptimally:")
for combination, weight in optimal_combinations.items():
    print(f"{combination}: mass {weight}")


print("\n------------------\nProgrammatic:")
print(get_optimal_set_dynamic(things, MAX_WEIGHT, 0.5))