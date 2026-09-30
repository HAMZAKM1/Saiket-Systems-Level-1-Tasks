import requests
import sys

def fetch_random_joke(category: str = "Programming", safe_mode: bool = True) -> dict:
    """
    Fetches a random joke from the public JokeAPI.
    """
    url = f"https://v2.jokeapi.dev/joke/{category}"
    params = {}
    
    if safe_mode:
        params["safe-mode"] = ""

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("error"):
            raise Exception(data.get("message", "Unknown API Error occurred."))
            
        return data

    except requests.exceptions.Timeout:
        print("\n[Error] The request timed out. Please check your internet connection.")
        sys.exit(1)
    except requests.exceptions.HTTPError as err:
        print(f"\n[Error] HTTP Error occurred: {err}")
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(f"\n[Error] Network error occurred: {err}")
        sys.exit(1)


def display_joke(joke_data: dict) -> None:
    """
    Parses and displays the fetched joke data.
    """
    print("\n" + "=" * 50)
    print("                JOKE OF THE DAY                 ")
    print("=" * 50)
    print(f" Category : {joke_data.get('category')}")
    print(f" Type     : {joke_data.get('type').capitalize()}")
    print("-" * 50 + "\n")

    if joke_data.get("type") == "single":
        print(f"💬 {joke_data.get('joke')}\n")
    elif joke_data.get("type") == "twopart":
        print(f"❓ Setup: {joke_data.get('setup')}")
        print(f"💡 Punchline: {joke_data.get('delivery')}\n")

    print("=" * 50)


def main():
    print("Fetching data from Public JokeAPI...")
    category = "Programming"
    joke_data = fetch_random_joke(category=category, safe_mode=True)
    display_joke(joke_data)


if __name__ == "__main__":
    main()