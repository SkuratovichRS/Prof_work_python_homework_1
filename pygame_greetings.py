import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.width = 300
        self.height = 300
        self.color = (150, 100, 255)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Hello netology!")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(self.color)
            self.print_greetings()
            pygame.display.flip()

    def print_greetings(self):
        f = pygame.font.Font(None, 40)
        text = f.render('HELLO NETOLOGY!', True, (255, 192, 203))
        self.screen.blit(text, (20, 130))


game = Game()
game.run()
