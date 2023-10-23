import pygame
import os

BASE_IMG_PATH = "data/images/"


def load_image(path: str) -> pygame.Surface:
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_images(path: str) -> list[pygame.Surface]:
    return [
        load_image(path + "/" + img_name)
        for img_name in sorted(os.listdir(BASE_IMG_PATH + path))
    ]


class Animation:
    def __init__(self, images, img_dur=5, loop=True) -> None:
        self.images = images
        self.img_duration = img_dur
        self.loop = loop
        self.done = False
        self.frame = 0

    def copy(self) -> "Animation":
        return Animation(self.images, self.img_duration, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (len(self.images) * self.img_duration)
        else:
            self.frame = min(self.frame + 1, len(self.images) * self.img_duration - 1)

            if self.frame >= len(self.images) * self.img_duration - 1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.img_duration)]
