import heapq

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the blank space

# Function to find the location of the blank tile (0)
def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

# Heuristic function: number of misplaced tiles and Manhattan distance
def heuristic(state):
    misplaced = 0
    manhattan_distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                misplaced += 1
                # Find the goal position of the current tile
                for x in range(len(goal_state)):
                    for y in range(len(goal_state[x])):
                        if goal_state[x][y] == state[i][j]:
                            manhattan_distance += abs(x - i) + abs(y - j)
    return misplaced + manhattan_distance

# Generate possible moves
def generate_moves(state):
    moves = []
    x, y = find_blank(state)
    # Up
    if x > 0:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
        moves.append(new_state)
    # Down
    if x < 2:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
        moves.append(new_state)
    # Left
    if y > 0:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
        moves.append(new_state)
    # Right
    if y < 2:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]
        moves.append(new_state)
    return moves

# Best-fit search algorithm
def best_fit_search(start_state):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (heuristic(start_state), start_state))
    
    while open_list:
        _, current_state = heapq.heappop(open_list)
        print(f"Current State: {current_state}")  # Display each state's output
        
        if current_state == goal_state:
            print("Goal reached!")
            return current_state
        
        closed_list.add(tuple(map(tuple, current_state)))
        
        for move in generate_moves(current_state):
            if tuple(map(tuple, move)) not in closed_list:
                heapq.heappush(open_list, (heuristic(move), move))

    return None

# Define the start state
start_state = [[1, 2, 3],
               [5, 7, 6],
               [4, 0, 8]]  # Blank is represented by 0

# Run the search algorithm
best_fit_search(start_state)
