import heapq
from collections import deque
import time
from typing import Tuple, List, Set

class PuzzleState:
    """Represents an 8-puzzle state"""
    
    def __init__(self, state: Tuple[int, ...], parent=None, move: str = ""):
        """
        state: tuple of 9 integers (0 represents empty space)
        parent: parent PuzzleState
        move: the move that led to this state
        """
        self.state = state
        self.parent = parent
        self.move = move
        self.g = 0 if parent is None else parent.g + 1
        self.h = 0
        self.f = 0
    
    def __lt__(self, other):
        """For heapq comparison"""
        return self.f < other.f
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(self.state)
    
    def get_neighbors(self) -> List['PuzzleState']:
        """Generate all possible next states"""
        neighbors = []
        blank_pos = self.state.index(0)
        row, col = blank_pos // 3, blank_pos % 3
        
        # Possible moves: up, down, left, right
        moves = []
        if row > 0:
            moves.append((blank_pos - 3, "UP"))
        if row < 2:
            moves.append((blank_pos + 3, "DOWN"))
        if col > 0:
            moves.append((blank_pos - 1, "LEFT"))
        if col < 2:
            moves.append((blank_pos + 1, "RIGHT"))
        
        for new_pos, move_name in moves:
            new_state = list(self.state)
            new_state[blank_pos], new_state[new_pos] = new_state[new_pos], new_state[blank_pos]
            neighbors.append(PuzzleState(tuple(new_state), self, move_name))
        
        return neighbors
    
    def __str__(self):
        """Display the puzzle state"""
        s = ""
        for i in range(0, 9, 3):
            s += f"{self.state[i]} {self.state[i+1]} {self.state[i+2]}\n"
        return s


def heuristic_misplaced_tiles(state: Tuple[int, ...], goal: Tuple[int, ...]) -> int:
    """
    H1: Count the number of misplaced tiles (excluding the blank)
    """
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


def heuristic_manhattan_distance(state: Tuple[int, ...], goal: Tuple[int, ...]) -> int:
    """
    H2: Sum of Manhattan distances of all tiles from their goal positions
    Manhattan distance = |current_row - goal_row| + |current_col - goal_col|
    """
    distance = 0
    goal_positions = {}
    
    for i in range(9):
        if goal[i] != 0:
            goal_positions[goal[i]] = (i // 3, i % 3)
    
    for i in range(9):
        if state[i] != 0:
            current_row, current_col = i // 3, i % 3
            goal_row, goal_col = goal_positions[state[i]]
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    
    return distance


class AStarPuzzleSolver:
    """A* solver for 8-puzzle"""
    
    def __init__(self, heuristic_func):
        """
        heuristic_func: function that takes (state, goal) and returns heuristic value
        """
        self.heuristic_func = heuristic_func
        self.nodes_explored = 0
        self.solution_path = []
        self.goal_found = False
    
    def solve(self, initial_state: Tuple[int, ...], goal_state: Tuple[int, ...]) -> Tuple[bool, int]:
        """
        Solve using A* algorithm
        Returns: (found, depth_of_solution)
        """
        self.nodes_explored = 0
        self.solution_path = []
        self.goal_found = False
        
        start_node = PuzzleState(initial_state)
        start_node.h = self.heuristic_func(start_node.state, goal_state)
        start_node.f = start_node.g + start_node.h
        
        open_list = [start_node]
        closed_set: Set[Tuple[int, ...]] = set()
        
        while open_list:
            current = heapq.heappop(open_list)
            self.nodes_explored += 1
            
            if current.state == goal_state:
                self.goal_found = True
                path = []
                node = current
                while node:
                    path.append(node)
                    node = node.parent
                self.solution_path = path[::-1]
                return True, current.g
            
            closed_set.add(current.state)
            
            for neighbor in current.get_neighbors():
                if neighbor.state not in closed_set:
                    neighbor.h = self.heuristic_func(neighbor.state, goal_state)
                    neighbor.f = neighbor.g + neighbor.h
                    heapq.heappush(open_list, neighbor)
        
        return False, -1
    
    def print_solution(self):
        """Print the solution path"""
        if not self.goal_found:
            print("No solution found!")
            return
        
        print(f"Solution found in {len(self.solution_path) - 1} moves:\n")
        for i, state in enumerate(self.solution_path):
            print(f"Step {i}:")
            if i > 0:
                print(f"Move: {state.move}")
            print(state)
        
        print(f"Total moves: {len(self.solution_path) - 1}")


def run_comparison():
    """Compare both heuristics"""
    
    initial = (1, 2, 3, 4, 0, 5, 7, 8, 6)
    goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    
    print("=" * 60)
    print("8-PUZZLE A* SOLVER WITH HEURISTIC COMPARISON")
    print("=" * 60)
    
    print("\nInitial State:")
    print(f"{initial[0]} {initial[1]} {initial[2]}")
    print(f"{initial[3]} {initial[4]} {initial[5]}")
    print(f"{initial[6]} {initial[7]} {initial[8]}\n")
    
    print("Goal State:")
    print(f"{goal[0]} {goal[1]} {goal[2]}")
    print(f"{goal[3]} {goal[4]} {goal[5]}")
    print(f"{goal[6]} {goal[7]} {goal[8]}\n")
    
    print("=" * 60)
    print("HEURISTIC 1: MISPLACED TILES")
    print("=" * 60)
    solver_h1 = AStarPuzzleSolver(heuristic_misplaced_tiles)
    start_time = time.time()
    found, depth = solver_h1.solve(initial, goal)
    elapsed_h1 = time.time() - start_time
    
    print(f"Solution Found: {found}")
    print(f"Depth of Solution: {depth}")
    print(f"Nodes Explored: {solver_h1.nodes_explored}")
    print(f"Time Taken: {elapsed_h1:.6f} seconds\n")
    
    print("=" * 60)
    print("HEURISTIC 2: MANHATTAN DISTANCE")
    print("=" * 60)
    solver_h2 = AStarPuzzleSolver(heuristic_manhattan_distance)
    start_time = time.time()
    found, depth = solver_h2.solve(initial, goal)
    elapsed_h2 = time.time() - start_time
    
    print(f"Solution Found: {found}")
    print(f"Depth of Solution: {depth}")
    print(f"Nodes Explored: {solver_h2.nodes_explored}")
    print(f"Time Taken: {elapsed_h2:.6f} seconds\n")
    
    print("=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    print(f"Nodes Explored:")
    print(f"  H1 (Misplaced): {solver_h1.nodes_explored}")
    print(f"  H2 (Manhattan): {solver_h2.nodes_explored}")
    print(f"  Efficiency Improvement: {(1 - solver_h2.nodes_explored/solver_h1.nodes_explored)*100:.2f}%\n")
    
    print(f"Time Taken:")
    print(f"  H1 (Misplaced): {elapsed_h1:.6f} seconds")
    print(f"  H2 (Manhattan): {elapsed_h2:.6f} seconds\n")
    
    print("=" * 60)
    print("SOLUTION PATH (Using H2 - More Efficient)")
    print("=" * 60)
    solver_h2.print_solution()


def run_harder_puzzle():
    """Solve a harder puzzle configuration"""
    print("\n\n" + "=" * 60)
    print("SOLVING A MORE CHALLENGING PUZZLE")
    print("=" * 60 + "\n")
    
    initial = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    
    print("Initial State:")
    print(f"{initial[0]} {initial[1]} {initial[2]}")
    print(f"{initial[3]} {initial[4]} {initial[5]}")
    print(f"{initial[6]} {initial[7]} {initial[8]}\n")
    
    print("Using H1 (Misplaced Tiles):")
    solver_h1 = AStarPuzzleSolver(heuristic_misplaced_tiles)
    start_time = time.time()
    found, depth = solver_h1.solve(initial, goal)
    elapsed_h1 = time.time() - start_time
    print(f"Nodes Explored: {solver_h1.nodes_explored}, Time: {elapsed_h1:.6f}s, Depth: {depth}\n")
    
    print("Using H2 (Manhattan Distance):")
    solver_h2 = AStarPuzzleSolver(heuristic_manhattan_distance)
    start_time = time.time()
    found, depth = solver_h2.solve(initial, goal)
    elapsed_h2 = time.time() - start_time
    print(f"Nodes Explored: {solver_h2.nodes_explored}, Time: {elapsed_h2:.6f}s, Depth: {depth}\n")
    
    print(f"Efficiency Improvement: {(1 - solver_h2.nodes_explored/solver_h1.nodes_explored)*100:.2f}%")


if __name__ == "__main__":
    run_comparison()
    run_harder_puzzle()