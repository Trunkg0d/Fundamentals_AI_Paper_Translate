import pygame
from maze import SearchSpace, Node
from const import GREEN, BLUE, RED, WHITE, YELLOW
import random

def DFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.id]
    closed_set = []
    father = [-1] * g.get_length()

    while len(open_set) != 0:
        cur_id = open_set[-1]
        open_set = open_set[:-1]
        cur_node = g.grid_cells[cur_id]
        if cur_node.id != g.start.id and g.is_goal(cur_node) == 0:
            cur_node.set_color(YELLOW, sc)

        if cur_id not in closed_set:
            closed_set.append(cur_id)
            if cur_node.id != g.start.id and g.is_goal(cur_node) == 0:
                cur_node.set_color(BLUE, sc)

        if g.is_goal(cur_node):
            path = []
            while cur_node.id != g.start.id:
                path.append(cur_node)
                cur_node = g.grid_cells[father[cur_node.id]]
            path.append(g.start)

            for n in range(1, len(path)):
                pygame.draw.line(sc, WHITE, path[n].rect.center, path[n - 1].rect.center, 2)
                pygame.time.delay(10)
                pygame.display.update()
            break

        neighbors = g.get_neighbors(cur_node)
        for neighbor in neighbors:
            if neighbor.id not in closed_set and neighbor.id not in open_set:
                father[neighbor.id] = cur_id
                open_set.append(neighbor.id)
                if neighbor.id != g.start.id and g.is_goal(neighbor) == 0:
                    neighbor.set_color(RED, sc)
        pygame.display.update()


def BFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.id]
    closed_set = []
    father = [-1]*g.get_length()

    while len(open_set) != 0:
        cur_id = open_set[0]
        cur_node = g.grid_cells[cur_id]
        open_set = open_set[1:]
        if cur_node.id != g.start.id and g.is_goal(cur_node) == 0:
            cur_node.set_color(YELLOW, sc)

        if g.is_goal(cur_node):
            path = []
            while cur_node.id != g.start.id:
                path.append(cur_node)
                cur_node = g.grid_cells[father[cur_node.id]]
            path.append(g.start)

            for n in range(1, len(path)):
                pygame.draw.line(sc, WHITE, path[n].rect.center, path[n-1].rect.center, 2)
                pygame.time.delay(10)
                pygame.display.update()
            break

        closed_set.append(cur_id)

        if cur_node.id != g.start.id and g.is_goal(cur_node) == 0 and cur_node.id in closed_set:
            cur_node.set_color(BLUE, sc)

        neighbors = g.get_neighbors(cur_node)

        for neighbor in neighbors:
            neighbor_id = neighbor.id
            if neighbor_id not in closed_set and neighbor_id not in open_set:
                closed_set.append(neighbor_id)
                father[neighbor_id] = cur_id
                if neighbor.id != g.start.id and g.is_goal(neighbor) == 0:
                    neighbor.set_color(RED, sc)
                open_set.append(neighbor_id)
        pygame.display.update()
def UCS(g: SearchSpace, sc: pygame.Surface):
    print('Implement UCS algorithm')

    open_set = [(0, g.start.id)]
    closed_set = []
    father = [-1] * g.get_length()
    node_costs = [100_000] * g.get_length()
    node_costs[g.start.id] = 0

    while len(open_set) != 0:
        min_cost = float("inf")
        min_node_id = None

        for cost, node_id in open_set:
            if cost < min_cost:
                min_node_id = node_id
                min_cost = cost
        cur_node_id = min_node_id
        open_set.remove((min_cost, cur_node_id))
        cur_node = g.grid_cells[cur_node_id]
        if cur_node.id != g.start.id and g.is_goal(cur_node) == 0:
            cur_node.set_color(YELLOW, sc)

        if g.is_goal(cur_node):
            path = []
            while cur_node.id != g.start.id:
                path.append(cur_node)
                cur_node = g.grid_cells[father[cur_node.id]]
            path.append(g.start)

            for n in range(1, len(path)):
                pygame.draw.line(sc, WHITE, path[n].rect.center, path[n - 1].rect.center, 2)
                pygame.time.delay(10)
                pygame.display.update()
            break

        closed_set.append(cur_node_id)

        if cur_node.id != g.start.id and g.is_goal(cur_node) == 0:
            cur_node.set_color(BLUE, sc)

        neighbors = g.get_neighbors(cur_node)

        for neighbor in neighbors:
            if neighbor.id not in closed_set:
                # I set the default cost from current node to their neighbors is 1
                cost_from_cur_node = 1

                # or we can random for more fun xD, if you want random, remove the comment below
                # cost_from_cur_node = random.randint(1, 100)

                neighbor_cost = node_costs[cur_node_id] + cost_from_cur_node
                if neighbor_cost < node_costs[neighbor.id]:
                    node_costs[neighbor.id] = neighbor_cost
                    father[neighbor.id] = cur_node_id
                    open_set.append((neighbor_cost, neighbor.id))
                if neighbor.id != g.start.id and g.is_goal(neighbor) == 0:
                    neighbor.set_color(RED, sc)
        pygame.display.update()

def AStar(g: SearchSpace, sc: pygame.Surface):
    print('Implement AStar algorithm')

    open_set = [(0, g.start.id)]
    closed_set = []
    father = [-1] * g.get_length()
    g_costs = [100_000] * g.get_length()
    h_costs = [100_000] * g.get_length()
    g_costs[g.start.id] = 0

    while open_set:
        min_f_cost = float("inf")
        min_node_id = None

        for f_cost, node_id in open_set:
            if f_cost < min_f_cost:
                min_node_id = node_id
                min_f_cost = f_cost

        cur_node_id = min_node_id
        open_set = [item for item in open_set if item[1] != cur_node_id]
        cur_node = g.grid_cells[cur_node_id]
        if cur_node.id != g.start.id and g.is_goal(cur_node) == 0:
            cur_node.set_color(YELLOW, sc)

        if g.is_goal(cur_node):
            path = []
            while cur_node.id != g.start.id:
                path.append(cur_node)
                cur_node = g.grid_cells[father[cur_node.id]]
            path.append(g.start)

            for n in range(1, len(path)):
                pygame.draw.line(sc, WHITE, path[n].rect.center, path[n - 1].rect.center, 2)
                pygame.time.delay(10)
                pygame.display.update()
            break

        closed_set.append(cur_node_id)

        if cur_node.id != g.start.id and g.is_goal(cur_node) == 0:
            cur_node.set_color(BLUE, sc)

        neighbors = g.get_neighbors(cur_node)

        for neighbor in neighbors:
            if neighbor.id in closed_set:
                continue

            # I set the default cost from current node to their neighbors is 1
            cost_from_cur_node = 1

            # or we can random for more fun xD, if you want random, remove the comment below
            # cost_from_cur_node = random.randint(1, 100)

            g_cost = g_costs[cur_node_id] + cost_from_cur_node
            h_cost = ((neighbor.rect.x - g.goal.rect.x)**2 + (neighbor.rect.y - g.goal.rect.y)**2)**(1/2)
            f_cost = g_cost + h_cost

            if (neighbor_cost := g_costs[neighbor.id]) is None or g_cost < neighbor_cost:
                father[neighbor.id] = cur_node_id
                g_costs[neighbor.id] = g_cost
                h_costs[neighbor.id] = h_cost
                open_set.append((f_cost, neighbor.id))

            if neighbor.id != g.start.id and g.is_goal(neighbor) == 0:
                neighbor.set_color(RED, sc)

        pygame.display.update()

