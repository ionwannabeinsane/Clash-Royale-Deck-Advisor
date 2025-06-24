import os
import unicodedata
import re
import requests
from collections import Counter
from dotenv import load_dotenv

# Import your modules
from card_data import card_data
from synergy_map import synergy_map

# 1) Normalization helper
def normalize(name: str) -> str:
    """
    Normalize card names: lowercase, strip non-alphanumerics.
    """
    name = name.strip()
    name = re.sub(r'^the\s+', '', name, flags=re.I)
    name = unicodedata.normalize('NFKD', name)
    name = name.encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[^a-z0-9]', '', name.lower())

# 2) Build normalized lookup for card_data
normalized_card_data = { normalize(k): v for k, v in card_data.items() }

# 3) Deck analysis function
def analyze_deck(deck):
    analysis = {
        "air_defense": 0, "splash": 0, "cycle_cards": 0,
        "win_condition": 0, "swarm": 0, "tank": 0,
        "is_spell": 0, "support": 0, "responsive": 0
    }
    missing = []

    for card in deck:
        key = normalize(card)
        data = normalized_card_data.get(key)
        if not data:
            missing.append(card)
            continue

        if data.get("air"):           analysis["air_defense"]  += 1
        if data.get("splash"):        analysis["splash"]       += 1
        if data.get("cycle"):         analysis["cycle_cards"]  += 1
        if data.get("win_condition"): analysis["win_condition"] += 1
        if data.get("swarm"):         analysis["swarm"]        += 1
        if data.get("tank"):          analysis["tank"]         += 1
        if data.get("is_spell"):      analysis["is_spell"]     += 1
        if data.get("support"):       analysis["support"]      += 1
        if data.get("responsive"):    analysis["responsive"]   += 1

    if missing:
        print(f"⚠️ Skipped unknown cards: {missing}")

    recommendations = []
    if analysis["air_defense"] < 2:
        recommendations.append("Consider adding more air defense (e.g., Archers, Musketeer)")
    if analysis["splash"] < 2:
        recommendations.append("Add splash damage troops (e.g., Baby Dragon, Valkyrie)")
    if analysis["cycle_cards"] < 2:
        recommendations.append("Include faster cycle cards (e.g., Skeletons, Ice Spirit)")
    if analysis["win_condition"] < 1:
        recommendations.append("You need at least one win condition (e.g., Hog Rider, X-Bow)")

    return analysis, recommendations, missing

# 4) Synergy recommendation function
def recommend_synergies(deck):
    suggestions = []
    for card in deck:
        partners = synergy_map.get(card, [])
        for p in partners:
            if p not in deck:
                suggestions.append(f"Add **{p}** to synergize with **{card}**")
    return suggestions

# 5) Main execution block
if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv("CR_API_KEY")
    if not API_KEY:
        print("❌ CR_API_KEY not set in .env")
        exit(1)

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    # Use URL-encoded tag
    player_tag = "%23U9PRPY8Q0"
    url = f"https://api.clashroyale.com/v1/players/{player_tag}/battlelog"

    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print("❌ Failed to fetch battle log:", resp.status_code, resp.text)
        exit(1)

    battles = resp.json()
    my_decks = []
    for b in battles:
        for p in b['team']:
            if p['tag'] == player_tag.replace('%23', '#'):
                my_decks.append([c['name'] for c in p['cards']])

    print(f"🔍 Found {len(my_decks)} recent decks")

    # Most used cards
    all_cards = [card for deck in my_decks for card in deck]
    counts = Counter(all_cards)
    print("\n📊 Top cards:")
    for card, cnt in counts.most_common(10):
        print(f"  - {card}: {cnt}")

    # Analyze each deck
    print("\n🧠 Deck Analysis & Recommendations:")
    for i, deck in enumerate(my_decks, start=1):
        analysis, recs, missing = analyze_deck(deck)
        if missing:
            print("⚠️ Skipped cards:", missing)
            # …then
        synergy_recs = recommend_synergies(deck)
        recs.extend(synergy_recs)


        print(f"\nDeck {i}: {deck}")
        print(" Breakdown:", analysis)
        print(" Recommendations:")
        for r in recs:
            print("  -", r)
        print("-" * 40)
