import cfg
from rooms import room_parent
from characters import hero
from util import text, button, fight_stage
import pygame


class LvlPar(room_parent.RoomPar):
    grid = []
    len = 7
    hero_pos = (0, 0)
    dim = cfg.scr_len / len
    show_enemy_stats = False
    enemy = None

    def __init__(self):
        super().__init__()
        w = cfg.display_width
        sl = cfg.scr_len
        self.but_menu = button.Button("MENU", (w - sl) / 3, sl / 7 * 6.25, (w - sl) / 3, (w - sl) / 6, cfg.blue,
                                      cfg.light_blue, action="menu")

        for i in range(self.len):
            self.grid.append([])
            for j in range(self.len):
                self.grid[i].append(None)

        self.hero = hero.Hero(self.pos(self.hero_pos[0], self.hero_pos[1]))

        self.fight = None
        self.ani = 0

        self.init_map()
        self.init_level()

    def init_map(self):
        pass

    def init_level(self):
        pass

    def pos(self, y, x):
        w = cfg.display_width
        return y*self.dim, w-700 + x*self.dim

    def draw_stats(self, display):
        x = 50
        y = 100
        w = 200
        h = 400
        stats = text.Text("Hitpoint: " + str(self.hero.hp) + "\n" +
                          "Attack: " + str(self.hero.ap) + "\n" +
                          "Defense: " + str(self.hero.dp) + "\n",
                          cfg.white, 20, "microsoftsansserif")
        stats.display_to_screen(display, 150, align="left", padding=75)
        pygame.draw.rect(display, cfg.orange, [x, y, w, h], 5)

    def draw_enemy_stats(self, display):
        stats = text.Text("HP: " + str(self.enemy.hp) + ", Attack: " + str(self.enemy.ap) + ", Defense: " + str(self.enemy.dp),
                          cfg.white, 25, "microsoftsansserif")
        y = cfg.scr_len + (cfg.display_height - cfg.scr_len) / 2
        stats.display_to_screen(display, y)

    '''
    def displayFight(self):
        if self.fight is not None and len(self.fight.actions) > 0:
            timer = 30
            if timer == 0:
                action = self.fight.actions.popleft()
                self.process_actions(action)
                timer = 30

            timer -= 1
    
    def process_actions(self, action):
        if action[0] == "damage":
            defender = action[2]
            damage = action[3]
            defender.hp -= damage
    '''

    def blit(self, display):
        super().blit(display)

        for i in range(0, self.len):
            for j in range(0, self.len):

                self.grid[i][j].draw(display)

                if self.grid[i][j].obj is not None:
                    self.grid[i][j].obj.draw(display)

        self.but_menu.draw(display)
        self.buttons.append(self.but_menu)
        self.draw_stats(display)

        if self.show_enemy_stats:
            self.draw_enemy_stats(display)

        # self.displayFight()

    def handle_event(self, event):
        speed = 10
        if event.type == pygame.KEYDOWN:
            x = self.hero_pos[0]
            y = self.hero_pos[1]
            dx = 0
            dy = 0
            if self.ani == 0:
                if event.key == pygame.K_w:
                    dx = -1
                elif event.key == pygame.K_s:
                    dx = 1
                elif event.key == pygame.K_a:
                    dy = -1
                elif event.key == pygame.K_d:
                    dy = 1
            nx = x + dx
            ny = y + dy

            if 0 <= nx < self.len and 0 <= ny < self.len:
                tile = self.grid[nx][ny]
                if tile.obj is None and tile.canWalkOn:
                    self.hero.move((dx, dy))
                    self.ani += speed
                    self.hero_pos = (nx, ny)
                    tile.setObj(self.hero)
                    self.grid[x][y].setObj(None)
                elif tile.obj is not None and tile.obj != self.hero:
                    self.show_enemy_stats = True
                    self.enemy = tile.obj
                    # if tile.obj.hostile:
                    #     self.fight = fight_stage.Fight(self.hero, self.enemy)
        if self.ani != 0:
            self.ani += speed
        if self.ani >= 100:
            self.ani = 0

        return super().handle_event(event)
