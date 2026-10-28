def is_even(n):
    return n % 2 == 0


def get_odds(nums):
    odds = []
    count = 0

    for num in nums:
        if not is_even(num):
            odds.append(num)
            count += 1

    return count, odds


mylist = [4, 7, 23, 8, 9, 3, 5, 7, 3, 6, 15]
odds_count, my_odds = get_odds(mylist)
print(odds_count)
print(my_odds)