import requests
import json

hero_dict = {}
def intelligence_level():
    quant = int(input("Сколько героев вы будете сравнивать, введите число "))
    for repeat in range (quant):
        hero_name = input("Введите имя супергероя ")
        hero_response = requests.get(f"https://www.superheroapi.com/api.php/2619421814940190/search/{hero_name}")
        if json.loads(hero_response.text)["response"] == "error":
            print("Такого героя не существуе")
        else:
            hero_intelligence = json.loads(hero_response.text)["results"][0]["powerstats"]["intelligence"]
            hero_dict[hero_name] = int(hero_intelligence)

    result_list = [(name, intelligence) for name, intelligence in hero_dict.items()]
    best_result = max(result_list)
    print("Самый умный герой", best_result)

intelligence_level()
