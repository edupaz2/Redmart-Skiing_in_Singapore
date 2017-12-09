

class Skiing(object):
    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

        self.depths = [[0 for _ in range(self.w)] for __ in range(self.h)]
        self.max_depth = 0
        self.max_nodes = []
        self.max_drop = 0

    def expand_adyacents(self, r, c):
        """
        Expand and increase the depth of the allowed adyacents
        """
        adyacents = []
        current_node = self.g[r][c]
        current_depth = self.depths[r][c]

        # Top
        if r-1 >= 0 and current_node > self.g[r-1][c] and current_depth+1 >= self.depths[r-1][c]:
            #print("Adyacent:", self.g[r-1][c], ", d:", self.depths[r-1][c])
            adyacents.append((r-1,c))
            self.depths[r-1][c] = current_depth + 1
        # Left
        if c-1 >= 0 and current_node > self.g[r][c-1] and current_depth+1 >= self.depths[r][c-1]:
            adyacents.append((r, c-1))
            self.depths[r][c-1] = current_depth + 1
        # Right
        if c+1 < self.w and current_node > self.g[r][c+1] and current_depth+1 >= self.depths[r][c+1]:
            adyacents.append((r, c+1))
            self.depths[r][c+1] = current_depth + 1
        # Down
        if r+1 < self.h and current_node > self.g[r+1][c] and current_depth+1 >= self.depths[r+1][c]:
            adyacents.append((r+1, c))
            self.depths[r+1][c] = current_depth + 1

        return adyacents

    def ski(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.depths[i][j] == 0:
                    visited = []
                    to_visit = [(i,j)]
                    starting_drop = self.g[i][j]
                    while to_visit:
                        node = to_visit.pop(0)
                        visited.append(node)
                        node_depth = self.depths[node[0]][node[1]]
                        if node_depth == self.max_depth:
                            self.max_nodes.append((node[0], node[1]))
                            self.max_drop = max(self.max_drop, starting_drop-self.g[node[0]][node[1]])
                        elif node_depth > self.max_depth:
                            self.max_depth = node_depth
                            self.max_nodes = [(node[0], node[1])]
                            self.max_drop = starting_drop-self.g[node[0]][node[1]]

                        to_visit = to_visit + self.expand_adyacents(node[0], node[1])

        print("Max Depth:", self.max_depth+1)
        # print("Max Nodes:", self.max_nodes)
        print("Max Drop:", self.max_drop)


lines = [list(map(int, line.strip("\n").split())) for line in open('map.txt')]
dimensions=lines[0]
grid=lines[1:]
assert(len(dimensions)==2)
assert(dimensions[0]==len(grid))
assert(dimensions[1]==len(grid[0]))

ski = Skiing(grid)
ski.ski()