def select_items(weights, prices, limit):
    unit_prices = {}
    for i, (w, p) in enumerate(zip(weights, prices)):
        unit_prices[i] = p / w

    sorted_unit_prices = sorted(unit_prices.items(), key=lambda x: x[1], reverse=True)
    print(sorted_unit_prices)

    rest = limit
    results = {}
    for idx_to_select, _ in sorted_unit_prices:
        weight_to_load = weights[idx_to_select] if weights[idx_to_select] < rest else rest
        results[idx_to_select] = weight_to_load
        
        rest -= weight_to_load
        if rest == 0:
            break
        
    return results


if __name__ == '__main__':
    weights = [20, 30, 10]
    prices = [100, 120, 60]
    
    print("  i |", end='')
    for i in range(len(weights)):
        print(f"{i:>3}|", end='')
    print('')
    print("w[i]|", end='')
    for _w in weights:
        print(f"{_w:>3}|", end='')
    print('')
    print("p[i]|", end='')
    for _p in prices:
        print(f"{_p:>3}|", end='')
    print('')

    results = select_items(weights, prices, limit=50)
    total = 0
    for idx, weight_to_load in results.items():
        price = prices[idx] / weights[idx] * weight_to_load
        total += price

        print(f"no: {idx}, weight to load: {weight_to_load}, price: {price}")
    print(f"total price = {total}")
