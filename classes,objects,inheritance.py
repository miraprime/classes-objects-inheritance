class GameCharacter:
    def __init__(self, name, x_pos, health):
        self.name = name
        self.x_pos = x_pos
        self.health = health

    def move(self, by_amount):
        self.x_pos += by_amount

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def check_is_dead(self):
        return self.health <= 0


class PlayerCharacter(GameCharacter):

  def __init__(self, name, x_pos, health, num_lives):
    super().__init__(name, x_pos, health)
    self.max_health = health
    self.num_lives = num_lives

  def take_damage(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.num_lives -= 1
      self.health = self.max_health

  def check_is_dead(self):
    return self.health <= 0 and self.num_lives <= 0

pc = PlayerCharacter('Mira', 0, 100, 3)
gc = GameCharacter('Wolf', 0, 100)

pc.take_damage(150)
gc.take_damage(150)

print(pc.health)
print(gc.health)
print(pc.check_is_dead())
print(gc.check_is_dead())
print(pc.num_lives)