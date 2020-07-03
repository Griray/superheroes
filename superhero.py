import requests
import json

hulk_response = requests.get("https://www.superheroapi.com/api.php/2619421814940190/search/Hulk")
hulk_intelligence = json.loads(hulk_response.text)["results"][0]["powerstats"]["intelligence"]

captain_america_response = requests.get("https://www.superheroapi.com/api.php/2619421814940190/search/Captain America")
captain_america_intelligence = json.loads(captain_america_response.text)["results"][0]["powerstats"]["intelligence"]

thanos_response = requests.get("https://www.superheroapi.com/api.php/2619421814940190/search/Thanos")
thanos_intelligence = json.loads(thanos_response.text)["results"][0]["powerstats"]["intelligence"]

print(hulk_intelligence, captain_america_intelligence, thanos_intelligence)


if int(hulk_intelligence) > int(captain_america_intelligence):
    if int(hulk_intelligence) > int(thanos_intelligence):
        print("Самый умный герой Халк, его уровень интелекта составляет:", hulk_intelligence)
    else:
        print("Самый умный герой Танос, его уровень интелекта составляет:", thanos_intelligence)
else:
    if int(captain_america_intelligence) > int(thanos_intelligence):
        print("Самый умный герой Капитан Америка, его уровень интелекта составляет:", captain_america_intelligence)
    else:
        print("Самый умный герой Танос, его уровень интелекта составляет:", thanos_intelligence)







