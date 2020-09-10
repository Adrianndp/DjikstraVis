import pygame
import math


class Settings:
    def __init__(self):
        # SETTINGS
        self.start = ()
        self.target = ()
        self.size = 15  # Size of pixel (if you want to change it make sure to change it in input file too)
        self.visited = []
        (self.width, self.height) = (600, 600)
        self.BLACK = (0, 0, 0)
        self.GREY = (220, 220, 220)
        self.WHITE = (255, 255, 255)
        self.limit = int(self.width / self.size)
        self.thickness = 2
        self.positions = {}  # The whole positions and weights of the map
        self.positions_list = []  # the positions trimmed without the border and walls
        self.weight = []  # i used the function of distance to append the weight of each node
        self.paths_list = []
        self.draw = True
        # settings from pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('shortest path finder   DRAW WALLS WITH THE MOUSE THEN PRESS SPACE KEY')
        self.running = True
        points = [i * self.size for i in range(self.limit)]
        for x in points:
            for y in points:
                self.positions[(x, y)] = (self.WHITE, self.thickness)

    def show(self):
        for key, val in self.positions.items():
            pygame.draw.rect(self.screen, val[0], [key[0], key[1], self.size, self.size], val[1])

    def set_pixel(self, x, y, r, b, g):
        pixel = (x, y)
        if pixel in self.positions:
            self.positions[pixel] = ((r, b, g), 0)

    def border(self):
        pygame.draw.rect(self.screen, self.WHITE, [0, 0, self.size, self.size], 0)
        for key in self.positions.keys():
            if key[0] == 0 or key[1] == 0 or key[0] == 600 - self.size or key[1] == 600 - self.size:
                self.positions[key] = (self.GREY, 0)

    def run(self, x1, y1, x2, y2):
        self.start = ((x1 + 1)*self.size, (y1 + 1)*self.size)
        self.target = ((x2 + 1)*self.size, (y2 + 1)*self.size)
        print()
        self.set_pixel(self.start[0], self.start[1], 255, 80, 80)
        self.set_pixel(self.target[0], self.target[1], 220, 170, 100 )
        while self.running:
            x_pos = pygame.mouse.get_pos()[0]
            y_pos = pygame.mouse.get_pos()[1]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.draw = False
                        self.search_shortest_path()
                        # print(self.positions)
            if pygame.mouse.get_pressed()[0]:
                if self.draw:
                    x_pos = math.floor(x_pos / self.size)
                    y_pos = math.floor(y_pos / self.size)
                    x_pos = x_pos * self.size
                    y_pos = y_pos * self.size
                    if (x_pos, y_pos) != self.start and (x_pos, y_pos) != self.target:
                        self.set_pixel(x_pos, y_pos, 255, 255, 255)
            self.screen.fill(self.BLACK)
            self.border()
            self.show()
            pygame.display.flip()

    def add_neighbor(self, x, y):
        neighbor = []
        width = self.width - self.size
        if (x + self.size) < width:
            neighbor.append((x + self.size, y))
        if (y + self.size) < width:
            neighbor.append((x, y + self.size))
        if (y + self.size) < width and (x + self.size) < width:
            neighbor.append((x + self.size, y + self.size))
        if (x - self.size) > 0:
            neighbor.append((x - self.size, y))
        if (y - self.size) > 0:
            neighbor.append((x, y - self.size))
        if (x - self.size) > 0 and (y - self.size) > 0:
            neighbor.append((x - self.size, y - self.size))
        if (x + self.size) < width and (y - self.size) > 0:
            neighbor.append((x + self.size, y - self.size))
        if (x - self.size) > 0 and (y + self.size) < width:
            neighbor.append((x - self.size, y + self.size))
        return neighbor

    def distance(self, x1, y1, x2, y2):
        result = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
        return result

    def path_list(self):
        # REMOVING EVERYTHING WHICH IS NOT A POTENTIAL PATH OR NODES
        for key, value in self.positions.items():
            if key[0] != 0 and key[1] != 0 and key[0] != 600 - self.size and key[1] != 600 - self.size:
                self.positions_list.append(key)
                if value[1] != 0:
                    self.weight.append(self.distance(key[0], key[1], self.target[0], self.target[1]))
                else:
                    self.visited.append(key)  # walls also in visited so he wont consider to take it
                    self.positions_list.pop()
        dictionary = dict(zip(self.positions_list, self.weight))
        curr_neighbor = self.add_neighbor(self.start[0], self.start[1])
        for x in range(len(curr_neighbor)):
            path = []
            if self.positions_list.__contains__(curr_neighbor[x]):
                path.append(curr_neighbor[x])
                path.append(dictionary[curr_neighbor[x]])
                self.paths_list.append(path)
        for path in self.paths_list:
            self.visited.append(path[-2])
            self.set_pixel(int(path[-2][0]), int(path[-2][1]), 0, 0, 255)
            self.show()
            pygame.display.flip()
        self.visited.append(self.start)

    def shortest_path(self):
        while True:
            min_weight_list = []
            for path in self.paths_list:
                min_weight_list.append(path[-1])
            if len(min_weight_list) == 0:
                print("ITS NOT POSSIBLE")
                return
            min_weight = min(min_weight_list)
            next_curr = self.paths_list[min_weight_list.index(min_weight)]
            neighbors = self.add_neighbor(next_curr[-2][0], next_curr[-2][1])

            for neighbor in neighbors:
                if neighbor == self.target:
                    next_curr = next_curr[:-1]
                    for point in next_curr:
                        self.set_pixel(point[0], point[1], 50, 255, 80)
                        self.show()
                        pygame.display.flip()
                    # PATH HAS BEEN FOUNDED
                    return
                new_list = self.paths_list[min_weight_list.index(min_weight)]
                if neighbor not in self.visited:
                    new_list.insert(-1, neighbor)
                    self.visited.append(neighbor)
                    self.set_pixel(int(neighbor[0]), int(neighbor[1]), 0, 0, 255)
                    self.show()
                    pygame.display.flip()
                    new_list[-1] = min_weight + 1
                    self.paths_list.append(new_list.copy())
                    new_list.pop(-2)

            self.paths_list.remove(next_curr)

    def search_shortest_path(self):
        self.path_list()
        if len(self.paths_list) == 0:
            print("ITS NOT POSSIBLE")
            return
        self.shortest_path()
