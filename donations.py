def donation_analysis(don):
    total = sum(don.values())
    avg = total // len(don.items())
    max_value = max(don.values())

    for key, value in don.items():
        if value == max_value:
            max_person = key

    return total, avg, max_person


donations = {
    'ali': 200,
    'armaghan': 1000,
    'sara': 800,
    'hasan': 300
}


total, avg, max_person = donation_analysis(donations)
print(f"Total donation is {total}")
print(f"Average donation is {avg}")
print(f"Special thanks to {max_person}")
