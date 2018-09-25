import cfg
from rooms import room_parent
from util import text, button


class Menu(room_parent.RoomPar):

    def __init__(self):
        super().__init__()
        but_w = 100
        but_h = 50
        but_center_y = 665
        self.but_help = button.Button("help", self.w/10, but_center_y-but_h/2, but_w, but_h, cfg.yellow,
                                      cfg.light_yellow, action="help")
        self.but_quit = button.Button("quit", self.w-self.w/10*2, but_center_y-but_h/2, but_w, but_h, cfg.red,
                                      cfg.light_red, action="quit")
        self.but_play = button.Button("play", self.w/10*4, but_center_y-but_h, but_w*2, but_h*2, cfg.green,
                                      cfg.light_green, action="play")
        self.title = text.Text("A Typical Game",
                               cfg.green, 80, "arial")
        self.msg = text.Text("The type of RPG game that brings back memories of your nerdy childhood.\n"
                             "Experience a legendary adventure in a world of wonders and fantasy\n"
                             "and complete epic quests leading to the ultimate knowledge!",
                             cfg.white, 25, "comicsansms")

        self.buttons.append(self.but_help)
        self.buttons.append(self.but_quit)
        self.buttons.append(self.but_play)

    def blit(self, display):
        super().blit(display)

        self.title.display_to_screen(display, 300)
        self.msg.display_to_screen(display, 400)

        self.but_help.draw(display)
        self.but_quit.draw(display)
        self.but_play.draw(display)
