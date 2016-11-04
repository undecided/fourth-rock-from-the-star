def get_description(t):
    if t == 1: return "Tundra"
    if t == 2: return "Mountain"
    if t == 3: return "Crater"
    if t == 4: return "Lake"
    if t == 5: return "Quicksand"
    if t == 6: return "Planetary boosters"
    if t == 8: return "Nowhere"
    if t == 7: return "Russia"
    if t == 9: return "Tarmac"
    if t == 10: return "Wonderland"
    return "nothing interesting"

def is_passable(t):
    if t == 1: return True
    if t == 2: return False
    if t == 3: return False
    if t == 4: return False
    if t == 5: return False
    if t == 6: return True
    if t == 7: return True
    if t == 9: return True
    if t == 10: return True
    return True

