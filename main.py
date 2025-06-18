# Python Clash Royale Deck Advisor
# Note: Boss Bandit is in between tank and normal troop, same w/ Ice Golem, Knight, Rascals
# Note: add tower category, dps, responsive to stimuli, support

pip install requests

dps_mapping = {
    "Archers": "medium",
    "Cannon Cart": "medium",
    "Dart Goblin": "medium",
    "Electro Dragon": "low",
    "Electro Giant": "high",
    "Electro Wizard": "medium",
    "Firecracker": "low",
    "Flying Machine": "medium",
    "Hunter": "medium",
    "Ice Wizard": "low",
    "Inferno Dragon": "high",
    "Little Prince": "medium",
    "Lumberjack": "high",
    "Magic Archer": "medium",
    "Mini P.E.K.K.A.": "high",
    "Mighty Miner": "high",
    "Musketeer": "medium",
    "P.E.K.K.A.": "high",
    "Phoenix": "medium",
    "Prince": "high",
    "Princess": "low",
    "Skeleton Dragons": "low",
    "Witch": "low",
    "Zappies": "low"
}


card_data = {
    "Archers": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Archer Queen": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Arrows": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Baby Dragon": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Balloon": {"air": True, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Bandit": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Barbarians": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Barbarian Barrel": {"air": False, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Barbarian Hut": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Bats": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Battle Healer": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Battle Ram": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Beserker": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Bomber": {"air": False, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Bomb Tower": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": True},
    "Boss Bandit": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": True, "is_spell": False, "support": True, "responsive": True},
    "Bowler": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Bush Goblins": {"air": False, "splash": False, "cycle": True, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Cannon": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": True},
    "Cannon Cart": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Clone": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": True},
    "Dark Prince": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Dart Goblin": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Earthquake": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Electro Dragon": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Electro Giant": {"air": False, "splash": True, "cycle": False, "win_condition": True, "swarm": True, "tank": True, "is_spell": False, "support": False, "responsive": False},
    "Electro Spirit": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "is_spell": False},
    "Electro Wizard": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Elite Barbarians": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Elixir Golem": {"air": False, "splash": False, "cycle": True, "win_condition": True, "swarm": True, "tank": True, "is_spell": False, "support": False, "responsive": False},
    "Executioner": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Fireball": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Firecracker": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Fire Spirit": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Fisherman": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Flying Machine": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Freeze": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Furnace": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": False},
    "Giant": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": True, "is_spell": False, "support": True, "responsive": False},
    "Giant Skeleton": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": True, "is_spell": False, "support": True, "responsive": True},
    "Goblin Barrel": {"air": False, "splash": False, "cycle": True, "win_condition": True, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Goblin Cage": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": True},
    "Goblin Gang": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Goblin Demolisher": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Goblin Giant": {"air": True, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": True, "is_spell": False, "support": False, "responsive": False},
    "Goblin Hut": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Goblin Machine": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Goblins": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Goblinstein": {"air": True, "splash": True, "cycle": False, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Golden Knight": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Golem": {"air": False, "splash": True, "cycle": False, "win_condition": True, "swarm": False, "tank": True, "is_spell": False, "support": False, "responsive": False},
    "Graveyard": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": True, "tank": False, "is_spell": True},
    "Guards": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Hog Rider": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Hunter": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Heal Spirit": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Ice Golem": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": False},
    "Ice Spirit": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Ice Wizard": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Inferno Dragon": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Inferno Tower": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Knight": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": True, "is_spell": False, "support": True, "responsive": True},
    "Lava Hound": {"air": True, "splash": False, "cycle": False, "win_condition": True, "swarm": True, "tank": True, "is_spell": False, "support": False, "responsive": False},
    "Little Prince": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Lightning": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Log": {"air": False, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Lumberjack": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Magic Archer": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Mega Knight": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Mega Minion": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Mighty Miner": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": True, "is_spell": False, "support": True, "responsive": True},
    "Miner": {"air": False, "splash": False, "cycle": True, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Mini P.E.K.K.A.": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Minion Horde": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Minions": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Mirror": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Monk": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Mortar": {"air": False, "splash": True, "cycle": False, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": True},
    "Mother Witch": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Musketeer": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Night Witch": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "P.E.K.K.A.": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": True, "is_spell": False, "support": True, "responsive": True},
    "Phoenix": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Poison": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Prince": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Princess": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Rage": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Ram Rider": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Rascals": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Rocket": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Royal Ghost": {"air": False, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Royal Giant": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": True, "is_spell": False, "support": False, "responsive": False},
    "Royal Hogs": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": True, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Royal Recruits": {"air": False, "splash": False, "cycle": False, "win_condition": True, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Rune Giant": {"air": False, "splash": False, "cycle": False, "win_condition": False, "swarm": False, "tank": True, "is_spell": False, "support": True, "responsive": False},
    "Skeleton Army": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Skeleton Barrel": {"air": True, "splash": True, "cycle": True, "win_condition": True, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Skeleton Dragons": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Skeleton King": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Skeletons": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Snowball": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": True},
    "Sparky": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Spear Goblins": {"air": True, "splash": False, "cycle": True, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Suspicious Bush": {"air": False, "splash": False, "cycle": True, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Three Musketeers": {"air": True, "splash": False, "cycle": False, "win_condition": True, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Tombstone": {"air": False, "splash": False, "cycle": True, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Tornado": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": True, "support": True, "responsive": True},
    "Valkyrie": {"air": False, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Wall Breakers": {"air": False, "splash": True, "cycle": True, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Witch": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "Wizard": {"air": True, "splash": True, "cycle": False, "win_condition": False, "swarm": False, "tank": False, "is_spell": False, "support": True, "responsive": True},
    "X-Bow": {"air": True, "splash": False, "cycle": False, "win_condition": True, "swarm": False, "tank": False, "is_spell": False, "support": False, "responsive": False},
    "Zap": {"air": True, "splash": True, "cycle": True, "win_condition": False, "swarm": False, "tank": False, "is_spell": True, "support": True, "responsive": True},
    "Zappies": {"air": True, "splash": False, "cycle": False, "win_condition": False, "swarm": True, "tank": False, "is_spell": False, "support": True, "responsive": True}
}

for card, dps_value in dps_mapping.items():
    if card in card_data:
        card_data[card]["DPS"] = dps_value
for card in card_data:
    if "DPS" == False in card_data[card]:
        card_data[card]["DPS"] = "none"
for card, data in card_data.items():
    if data.get("is_spell", False):
        data["support"] = False
        data["responsive"] = False
        data["DPS"] = "none"

all_cards = list(card_data.keys())
for card in all_cards:
    print(card)
    
deck = ["Mega Knight", "Prince", "Musketeer", "Wall Breakers", "Arrows", "Zap", "Miner", "Bats"]
    
def deck_to_vector(deck, all_cards):
    vector = {}
    for card in all_cards:
        if card in deck:
            vector[card] = 1
        else:
            vector[card] = 0
    return vector
    
print(deck_to_vector(deck, all_cards))

def analyze_deck(deck):
    analysis = {"air_defense": 0, "splash": 0, "cycle_cards": 0, "win_condition": 0, "swarm": 0, "tank": 0, "is_spell": 0, "support": 0, "responsive": 0}
    for card in deck:
        if card_data[card]["air"]: analysis["air_defense"] += 1
        if card_data[card]["splash"]: analysis["splash"] += 1
        if card_data[card]["cycle"]: analysis["cycle_cards"] += 1
        if card_data[card]["win_condition"]: analysis["win_condition"] += 1
        if card_data[card]["swarm"]: analysis["swarm"] += 1
        if card_data[card]["tank"]: analysis["tank"] += 1
        if card_data[card]["is_spell"]: analysis["is_spell"] += 1
        if card_data[card]["support"]: analysis["is_spell"] += 1
        if card_data[card]["responsive"]: analysis["responsive"] += 1

    
    recommendations = []
    if analysis["air_defense"] < 2:
        recommendations.append("Consider adding more air defense (e.g., Archers, Musketeer, Electro Wizard)")
    if analysis["splash"] < 2:
        recommendations.append("You might struggle against swarm. Add splash (e.g., Valkyrie, Bomber, Baby Dragon)")
    if analysis["cycle_cards"] < 2:
        recommendations.append("Your deck might be slow. Add cycle cards like Skeletons or Ice Spirit.")
    if analysis["win_condition"] < 1:
        recommendations.append("Your deck does not have enough consistent tower damage dealers. Add win conditions such as Hog Rider or Wall Breakers.")

    return analysis, recommendations