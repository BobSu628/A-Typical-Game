from collections import deque


class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.actions = deque([])
        self.process()

    def process(self):
        hero_turn = True
        while self.hero.hp > 0 and self.enemy.hp > 0:
            if hero_turn:
                dmg = self.hero.ap - self.enemy.dp
                self.actions.append([self.hero, self.enemy, "damage", dmg])
                hero_turn = False

            else:
                dmg = self.enemy.ap - self.hero.dp
                self.actions.append([self.enemy, self.hero, "damage", dmg])
                hero_turn = True

        if self.hero.hp <= 0:
            self.actions.append([self.hero, "die"])

        else:
            self.actions.append([self.enemy, "die"])

