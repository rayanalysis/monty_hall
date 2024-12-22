import random


stay_wins = 0
switch_wins = 0
positions = [(0,-1,0),(0,0,0),(0,1,0)]

for x in range(200000):
    car_pos = random.choice(positions)
    player_choice = random.choice(positions)
    goat_positions = []
    
    for p in positions:
        if p != car_pos:
            goat_positions.append(p)
            
    goat_pos_1 = goat_positions[0]
    goat_pos_2 = goat_positions[1]
    eliminated_goat_pos = []
    
    for g in goat_positions:
        if g != car_pos:
            if g != player_choice:
                eliminated_goat_pos = g
    
    remaining_goat_pos = []
    
    if goat_pos_1 != eliminated_goat_pos:
        remaining_goat_pos = goat_pos_1
        
    elif goat_pos_1 == eliminated_goat_pos:
        remaining_goat_pos = goat_pos_2

    # this defines the "stay" choice, return the win condition
    if player_choice == car_pos:
        stay_wins += 1
        
    remaining_positions = [car_pos, remaining_goat_pos]
    switch_pos = []
    
    for p in remaining_positions:
        if player_choice != p:
            switch_pos = p
            
    # this defines the "switch" choice, return the win condition
    if switch_pos == car_pos:
        switch_wins += 1
    
print(stay_wins, ' = stay wins')
print(switch_wins, ' = switch wins')
