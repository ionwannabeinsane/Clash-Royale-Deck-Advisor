import requests
import json

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjI0MDczZDczLWMxNjYtNGJkNC1hZGM5LTI4Y2E1OGJlNDNjYiIsImlhdCI6MTc1MDI3MDE1OSwic3ViIjoiZGV2ZWxvcGVyL2RkNDdiYTU5LTlhODktOWE0Yi0xM2VkLTFiOWJiN2Y4MWVlNiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMzYuNjAuOS4xMzkiXSwidHlwZSI6ImNsaWVudCJ9XX0.G6BcuihiHRNvdN7Biebq3uL9_5jjAB6aTlZ19hp81ATtFaaGv3Sl6dNJUmXPPQR_m9QgMKaW1LOQCSznOaQ_xQ" 

headers = {
    "Accept": "application/json",
    "authorization": f"Bearer {API_KEY}"
}

def fetch_top_decks():
    url = "https://api.royaleapi.com/v1/decks/popular"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        formatted_decks = []

        for deck in data:
            cards = [card['name'] for card in deck['cards']]
            formatted_decks.append({
                "deck": cards,
                "label": "good"
            })

        with open("decks.json", "w") as f:
            json.dump(formatted_decks, f, indent=2)

        print("Decks saved to decks.json ✅")
        return formatted_decks
    else:
        print("Error:", response.status_code, response.text)
        return []

if __name__ == "__main__":
    fetch_top_decks()
