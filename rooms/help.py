from rooms import room_parent
from util import text, button
import cfg


class Help(room_parent.RoomPar):
    def __init__(self):
        but_w = 100
        but_h = 50
        but_center_y = 665
        super().__init__()
        self.heading = text.Text("Help", cfg.light_yellow, 80, "arial")
        self.content = text.Text("W: move up\n"
                                 "A: move down\n"
                                 "S: move down\n"
                                 "D: move right\n",
                                 cfg.white, 25, "microsoftsansserif")

        self.but_back = button.Button("back", self.w - self.w / 10 * 2, but_center_y - but_h / 2, but_w, but_h, cfg.red,
                                      cfg.light_red, action="back")

        self.buttons.append(self.but_back)

    def blit(self, display):
        super().blit(display)

        self.heading.display_to_screen(display, 100, align="left")
        self.content.display_to_screen(display, 200, align="left")

        self.but_back.draw(display)
