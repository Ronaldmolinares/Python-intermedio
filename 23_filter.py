numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_pair = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)
print(numbers_pair)


# Filter con dict
matches = [
    {
        "home_team": "Bolivia",
        "away_team": "Uruguay",
        "home_team_score": 3,
        "away_team_score": 1,
        "home_team_result": "Win",
    },
    {
        "home_team": "Brazil",
        "away_team": "Mexico",
        "home_team_score": 1,
        "away_team_score": 1,
        "home_team_result": "Draw",
    },
    {
        "home_team": "Ecuador",
        "away_team": "Venezuela",
        "home_team_score": 5,
        "away_team_score": 0,
        "home_team_result": "Win",
    },
]

winners = list(filter(lambda matches: matches["home_team_result"] == "Win", matches))
print(winners)
