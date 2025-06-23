# main.py

import re
from card_data import card_data
from synergy_map import synergy_map

def normalize(name: str) -> str:
    """Normalize a card name to lowercase alphanumeric only."""
    return re.sub(r'[^a-z0-9]', '', name.lower())

# Build a normalized lookup for faster matching
normalized_card_data = {
    normalize(k): v
    for k, v in card_data.items()
}

def analyze_deck(deck):
    """
    Analyze a deck list of card-names.
    Returns:
      - analysis: counts of categories (air_defense, splash, etc.)
      - recommendations: generic deck-balance tips
      - missing: list of any cards we couldn't recognize
    """
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

        if data.get("air", False):        analysis["air_defense"] += 1
        if data.get("splash", False):     analysis["splash"]      += 1
        if data.get("cycle", False):      analysis["cycle_cards"] += 1
        if data.get("win_condition", False): analysis["win_condition"] += 1
        if data.get("swarm", False):      analysis["swarm"]       += 1
        if data.get("tank", False):       analysis["tank"]        += 1
        if data.get("is_spell", False):   analysis["is_spell"]    += 1
        if data.get("support", False):    analysis["support"]     += 1
        if data.get("responsive", False): analysis["responsive"]  += 1

    recommendations = []
    if analysis["air_defense"] < 2:
        recommendations.append(
            "Consider adding more air defense (e.g., Archers, Musketeer)"
        )
    if analysis["splash"] < 2:
        recommendations.append(
            "You might struggle against swarm. Add splash (e.g., Baby Dragon, Valkyrie)"
        )
    if analysis["cycle_cards"] < 2:
        recommendations.append(
            "Your deck might be slow. Add cycle cards like Skeletons or Ice Spirit."
        )
    if analysis["win_condition"] < 1:
        recommendations.append(
            "You need at least one reliable win-condition (e.g., Hog Rider, X-Bow)."
        )

    return analysis, recommendations, missing


def recommend_synergies(deck):
    """
    For each card in deck, suggest one partner card from synergy_map
    that isn’t already in deck.
    """
    suggestions = []
    for card in deck:
        for partner in synergy_map.get(card, []):
            if partner not in deck:
                suggestions.append(f"Add **{partner}** to synergize with **{card}**")
    return suggestions
