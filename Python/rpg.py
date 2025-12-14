full_dot = '●'
empty_dot = '○'
limit_name = 10

def create_character(name, power, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if len(name) > limit_name:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'
    stats = [power, intelligence, charisma]

    if not all(isinstance(s, int) for s in stats):
        return 'All stats should be integers'
    if any(s < 1 for s  in stats):
        return 'All stats should be no less than 1'
    if any(s > 4 for s in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'

    def bar(value):
        return full_dot * value + empty_dot * (10 - value)
    
    return (
        f"{name}\n"
        f"STR {bar(power)}\n"
        f"INT {bar(intelligence)}\n"
        f"CHA {bar(charisma)}"
    )
    
print(create_character("ren", 4, 2, 1))
