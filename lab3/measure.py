# Lab 3: Measure, as a Function
# Lab 1's scenario block, written once as a function and called once per password.

guesses_per_second = 10_000_000_000   # the course's fixed attack speed: 10 billion guesses a second


def possible_passwords(characters, length):
    """Determine the number of possible passwords for a given rule
    characters: the number of characters for each position
    length: the number of positions
    """
    return characters ** length


def measure(label, characters, length):
    """Print how many passwords a rule allows and how long trying them all would take.

    label: a short name for the scenario, printed first
    characters: the choices for each position (26 letters, 94 keys, or 7,776 words)
    length: the number of positions
    """
    possible = possible_passwords(characters, length)
    seconds = possible / guesses_per_second
    days = seconds / 86400                # 86,400 seconds in a day
    years = days / 365
    hours = seconds / 3600
    over_a_year = years >= 1              # True or False

    print(label)
    print("Possible passwords:", f"{possible:,}")
    print("Seconds to try them all:", round(seconds))
    print("Days to try them all:", round(days, 1))
    print("Years to try them all:", round(years, 1))
    print("More than a year?", over_a_year)
    print("Hours to try them all: ", round(hours,1))
    print(type(hours))
    print()


measure("A: 8 lowercase letters", 26, 8)
measure("B: 6-digit student login", 10, 6)
measure("C: District Rule", 94, 12)
measure("D: 12 lowercase letters", 16, 12)
measure("E: 5 random words", 7776, 5)
