import random
import json
import os 

# Designed for 7 players.

def simulateTurn(player):
    # One win and 7 - player losses.
    options = [1] + [0] * (7-player)
    return random.choice(options)

def testSimulateTurn():
    # Test the simulate turn function
    # Expected: 14.2%, 16.6%, 20.0%, 25.0%, 33.3%, 50.0%, 100.0%
    expected = [14.2, 16.6, 20.0, 25.0, 33.3, 50.0, 100.0]
    # Initialise.
    wins = 0
    testIterations = 75000

    # Iterate through all players.
    for player in range(1,8):
        # Test Function.
        for _ in range(0,testIterations):
            win = simulateTurn(player)
            if win:
                wins += 1
        
        # Calculate percentages
        simulatedChance = round((wins/testIterations)*100,1)
        expectedChance = expected[player-1]
        deviation = round(expectedChance - simulatedChance, 2)

        # Print Output.
        print(f'Player {player} Win Chance: {simulatedChance} | Expected: {expectedChance} | Deviation {deviation}') 

        # Given it is random, allow a percent leeway.
        if deviation >= 1:
            return 0
        wins = 0

    return 1

def simulateGame():
    # Initialise.
    winner = False
    player = 1

    # Run game until winner is picked.
    while not winner:
        win = simulateTurn(player)
        if win:
            winner = player
        else:
            player += 1

    return winner

def runSimulation(iterations=100000):
    # Get current file dir.
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Get data from JSON file.
    with open(dir_path + "/rawData.json", "r") as f:
        data = json.load(f)

    # Play the game for given iterations.
    for _ in range(0,iterations):
        winner = simulateGame()
        data['wins'][f'{winner}'] += 1
        data['totalGames'] += 1

    # Save data to JSON file.
    with open(dir_path + "/rawData.json", "w") as f:
        json.dump(data,f, indent=2)
    

def presentData():
    # Get current file dir.
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Get data from JSON file.
    with open(dir_path + "/rawData.json", "r") as f:
        rawData = json.load(f)

    readableData = rawData

    for player in rawData['wins']:
        readableData['wins'][player] = round((rawData['wins'][player]/rawData['totalGames'])*100,1)

    # Get data from JSON file.
    with open(dir_path + "/readableData.json", "w") as f:
        json.dump(readableData,f, indent=2)


if __name__ == '__main__':
    runSimulation()
    presentData()