import random
from dataclasses import dataclass

@dataclass
class Team:
    name: str
    seed: int

first_round = [
    # SOUTH
    (Team("Auburn", seed = 1), Team("Alabama St", seed = 16)), 
    (Team("Louisville", seed = 8), Team("Creighton", seed = 9)),
    (Team("Michigan", seed = 5), Team("UC San Diego", seed = 12)),
    (Team("Texas A&M", seed = 4), Team("Yale", seed = 13)),
    (Team("Ole Miss", seed = 6), Team("North Carolina", seed = 11)),
    (Team("Iowa State", seed = 3), Team("Lipscomb", seed = 14)),
    (Team("Marquette", seed = 7), Team("New Mexico", seed = 10)),
    (Team("Michigan State", seed = 2), Team("Bryant", seed = 15)),
    # WEST
    (Team("Florida", seed = 1), Team("Norfolk State", seed = 16)), 
    (Team("UConn", seed = 8), Team("Oklahoma", seed = 9)),
    (Team("Memphis", seed = 5), Team("Colorado State", seed = 12)),
    (Team("Maryland", seed = 4), Team("Grand Canyon", seed = 13)),
    (Team("Grand Canyon", seed = 6), Team("Drake", seed = 11)),
    (Team("Texas Tech", seed = 3), Team("UNC Wilmington", seed = 14)),
    (Team("Kansas", seed = 7), Team("Arkansas", seed = 10)),
    (Team("St. John's", seed = 2), Team("Omaha", seed = 15)),
    # EAST
    (Team("Duke", seed = 1), Team("Mount St. Mary's", seed = 16)), 
    (Team("Mississippi State", seed = 8), Team("Baylor", seed = 9)),
    (Team("Oregon", seed = 5), Team("Liberty", seed = 12)),
    (Team("Arizona", seed = 4), Team("Akron", seed = 13)),
    (Team("BYU", seed = 6), Team("VCU", seed = 11)),
    (Team("Wisconsin", seed = 3), Team("Montana", seed = 14)),
    (Team("Saint Mary's", seed = 7), Team("Vanderbilt", seed = 10)),
    (Team("Alabama", seed = 2), Team("Robert Morris", seed = 15)),
    # MIDWEST
    (Team("Houston", seed = 1), Team("SIU Edwardsville", seed = 16)), 
    (Team("Gonzaga", seed = 8), Team("Georgia", seed = 9)),
    (Team("Clemson", seed = 5), Team("McNeese", seed = 12)),
    (Team("Purdue", seed = 4), Team("High Point", seed = 13)),
    (Team("Illinois", seed = 6), Team("Xavier", seed = 11)),
    (Team("Kentucky", seed = 3), Team("Troy", seed = 14)),
    (Team("UCLA", seed = 7), Team("Utah State", seed = 10)),
    (Team("Tennessee", seed = 2), Team("Wofford", seed = 15))
]

# # This method will always return the higher seed
# def simulate_game(team1, team2):
#     if team1.seed == team2.seed:
#         return random.choice([team1, team2])
#     if team1.seed > team2.seed:
#         return team2
#     return team1

def simulate_game(team1, team2):
    team1_seed_weight = 1 / (team1.seed)
    team2_seed_weight = 1 / (team2.seed)

    # # User power for seed weight
    # power = 1.1618
    # team1_seed_weight = 1 / (team1.seed**power)
    # team2_seed_weight = 1 / (team2.seed**power)

    # Convert to probabilities
    total = team1_seed_weight + team2_seed_weight
    team1_prob = 100 * (team1_seed_weight / total)
    team2_prob = 100 * (team2_seed_weight / total)

    # Get winner based on probabilities
    winner = random.choices([team1, team2], weights=[team1_prob, team2_prob], k=1)[0]

    print(f"{team1.name}-{team1.seed} ({team1_prob:.1f}%) vs {team2.name}-{team2.seed} ({team2_prob:.1f}%), Winner: {winner.name}")

    return winner

def simulate_tournment(first_round):
    current_games = first_round
    while len(current_games) > 0:
        print("\n===== NEW ROUND =====")
        winners = []

        for team1, team2 in current_games:
            winner = simulate_game(team1, team2)
            winners.append(winner)

        if len(winners) == 1:
            return winners[0]
        
        next_round = []
        for i in range(0, len(winners), 2):
            next_round.append((winners[i], winners[i + 1]))
            # [1, 2, 3, 4, 5, 6]
            # [(1,2), (3,4), (5,6)]

        current_games = next_round
    return None

winner = simulate_tournment(first_round)
print(f"\n{winner.name} wins the tournment!")