def select_items(weights, prices, limit):
    unit_prices = {}
    for i, (weight, price) in enumerate(zip(weights, prices)):
        unit_prices[i] = price / weight

    sorted_unit_prices = sorted(
        unit_prices.items(), key=lambda x: x[1], reverse=True)

    results = {}
    rest = limit
    i = 0
    while rest > 0:
        item_to_load = sorted_unit_prices[i][0]
        weight_to_load = weights[item_to_load] if rest >= weights[item_to_load] else rest
        results[item_to_load] = weight_to_load

        rest -= weight_to_load

        i += 1

    return results


if __name__ == '__main__':
    weights = [20, 30, 10]
    prices = [100, 120, 60]

    print("  i |", end='')
    for i in range(len(weights)):
        print(f"{i:>3}|", end='')
    print('')
    print("w[i]|", end='')
    for weight in weights:
        print(f"{weight:>3}|", end='')
    print('')
    print("p[i]|", end='')
    for price in prices:
        print(f"{price:>3}|", end='')
    print('')

    selected_items = select_items(weights, prices, 50)
    total = 0.0
    for idx, weight in selected_items.items():
        print(f"no = {idx}, weight = {weight}")

        total += prices[idx] / weights[idx] * weight
    print(f"total = {total}")
