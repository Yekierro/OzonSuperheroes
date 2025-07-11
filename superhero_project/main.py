import requests

def get_tallest_hero(gender, has_job):
    data = requests.get("https://akabab.github.io/superhero-api/api/all.json").json()
    return max(
        (h for h in data
         if h.get("appearance", {}).get("gender", "").lower() == gender.lower()
         and bool(h.get("work", {}).get("occupation", "").strip()) == has_job
         and "cm" in h.get("appearance", {}).get("height", ["", ""])[1]),
        key=lambda h: int(h["appearance"]["height"][1].replace("cm", "").strip()),
        default=None
    )

if __name__ == "__main__":
    hero = get_tallest_hero("Male", True)
    if hero:
        print(f"Самый высокий герой: {hero['name']}")
        print(f"Рост: {hero['appearance']['height'][1]}")
        print(f"Пол: {hero['appearance']['gender']}")
        print(f"Профессия: {hero['work']['occupation']}")
    else:
        print("Герой не найден")
