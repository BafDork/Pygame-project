import pygame, os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


x, y = 100, 325 # - координаты перс
x1, y1 = 700, 290 # - координаты врага
attack_power_her = 15
attack_power_ene = 35
speed_her = 10
speed_ene = 10
hp_her = 100
hp_ene = 100


class Menu_hero(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(menu_hero_sprites)
        self.frames = []
        self.loading_frames()
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(35, 244)

    def loading_frames(self):
        for i in range(16):
            frame = load_image(f"меню\геральт заставка\{i} кадр.png")
            self.rect = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames.append(frame.subsurface(pygame.Rect((0, 0), (190, 225))))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

class Campfire(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(campfire_sprites)
        self.frames = []
        self.loading_frames()
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(250, 340)

    def loading_frames(self):
        for i in range(9):
            frame = load_image(f"меню\костер\{i} кадр.png")
            self.rect = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames.append(frame.subsurface(pygame.Rect((0, 0), (100, 137))))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Effects_menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(effects_menu_sprites)
        self.frames = []
        self.loading_frames()
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(0, 0)

    def loading_frames(self):
        for i in range(136):
            frame = load_image(f"меню\эффекты\{i} кадр.png")
            self.rect = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames.append(frame.subsurface(pygame.Rect((0, 0), (1024, 576))))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Background_los_surface(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(background_los_surface_sprites)
        self.frames = []
        self.loading_frames()
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(0, -170)

    def loading_frames(self):
        for i in range(39):
            frame = load_image(f"окно поражения\фон\{i} кадр.png")
            self.rect = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames.append(frame.subsurface(pygame.Rect((0, 0), (1024, 1024))))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Hp:

    def __init__(self):
        for i in range(hp_her):
            pygame.draw.line(screen, (255, 0, 0), (114 + (i * 3.4), 50), (114 + (i * 3.4), 70), 4)
        for i in range(hp_ene):
            pygame.draw.line(screen, (255, 0, 0), (574 + (i * 3.4), 50), (574 + (i * 3.4), 70), 4)
        

class Background_gameplay(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(background_gameplay_sprites)
        self.frames = []
        self.loading_frames()
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(0, 0)

    def loading_frames(self):
        for i in range(49):
            frame = load_image(f"gameplay\фон\{i} кадр.png")
            self.rect = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames.append(frame.subsurface(pygame.Rect((0, 0), (1024, 576))))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Static_hero(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(static_hero_sprites)
        self.frames_p = []
        self.frames_l = []
        self.loading_frames_p()
        self.loading_frames_l()
        self.cur_frame_p = 0
        self.cur_frame_l = 0
        self.image = self.frames_p[self.cur_frame_p]
        self.rect = self.rect_p.move(x, y)
        self.image = self.frames_l[self.cur_frame_l]
        self.rect = self.rect_l.move(x, y)
        self.x, self.y = x, y

    def loading_frames_p(self):
        for i in range(16):
            frame = load_image(f"gameplay\геральт статичный\{i} кадр_п.png")
            self.rect_p = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_p.append(frame.subsurface(pygame.Rect((0, 0), (121, 217))))

    def loading_frames_l(self):
        for i in range(16):
            frame = load_image(f"gameplay\геральт статичный\{i} кадр_л.png")
            self.rect_l = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_l.append(frame.subsurface(pygame.Rect((0, 0), (121, 217))))

    def update(self, flag):
        if x == 100 and self.x != x:
            self.rect = self.rect.move(100 - self.x, 0)
            self.x = x
        self.rect = self.rect.move(x - self.x, y - self.y)
        self.x, self.y = x, y
        if flag:
            self.cur_frame_p = (self.cur_frame_p + 1) % len(self.frames_p)
            self.image = self.frames_p[self.cur_frame_p]
        else:
            self.cur_frame_l = (self.cur_frame_l + 1) % len(self.frames_l)
            self.image = self.frames_l[self.cur_frame_l]
        self.mask = pygame.mask.from_surface(self.image)
    


class Movement_hero(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(mov_hero_sprites)
        self.frames_p = []
        self.frames_l = []
        self.loading_frames_p()
        self.loading_frames_l()
        self.cur_frame_p = 0
        self.cur_frame_l = 0
        self.image = self.frames_p[self.cur_frame_p]
        self.rect = self.rect_p.move(x, y)
        self.image = self.frames_l[self.cur_frame_l]
        self.rect = self.rect_l.move(x, y)
        self.x = x

    def loading_frames_p(self):
        for i in range(6):
            frame = load_image(f"gameplay\геральт ходит\{i} кадр_п.png")
            self.rect_p = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_p.append(frame.subsurface(pygame.Rect((0, 0), (121, 217))))

    def loading_frames_l(self):
        for i in range(6):
            frame = load_image(f"gameplay\геральт ходит\{i} кадр_л.png")
            self.rect_l = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_l.append(frame.subsurface(pygame.Rect((0, 0), (121, 217))))
 
    def update(self, flag):
        global x
        if x == 100 and self.x != x:
            self.rect = self.rect.move(100 - self.x, 0)
        self.x = x
        if flag and x + 100 < 1024:
            if shift:
                x += speed_her + 15
                self.rect = self.rect.move(speed_her + 15, 0)
            else:
                x += speed_her
                self.rect = self.rect.move(speed_her, 0)
            self.cur_frame_p = (self.cur_frame_p + 1) % len(self.frames_p)
            self.image = self.frames_p[self.cur_frame_p]
        if not flag and x + 10 > 0:
            if shift:
                x -= speed_her + 15
                self.rect = self.rect.move(-(speed_her + 15), 0)
            else:
                x -= speed_her
                self.rect = self.rect.move(-speed_her, 0)
            self.cur_frame_l = (self.cur_frame_l + 1) % len(self.frames_l)
            self.image = self.frames_l[self.cur_frame_l]


class Hit_hero(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__(hit_hero_sprites)
        self.frames_p = []
        self.frames_l = []
        self.loading_frames_p()
        self.loading_frames_l()
        self.cur_frame_p = 0
        self.cur_frame_l = 0
        self.image = self.frames_p[self.cur_frame_p]
        self.rect = self.rect_p.move(x, y)
        self.image = self.frames_l[self.cur_frame_l]
        self.rect = self.rect_l.move(x, y)
        self.x, self.y = x, y

    def loading_frames_p(self):
        for i in range(4):
            frame = load_image(f"gameplay\геральт бьет\{i} кадр_п.png")
            self.rect_p = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_p.append(frame.subsurface(pygame.Rect((0, 0), (162, 212))))

    def loading_frames_l(self):
        for i in range(4):
            frame = load_image(f"gameplay\геральт бьет\{i} кадр_л.png")
            self.rect_l = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_l.append(frame.subsurface(pygame.Rect((0, 0), (162, 212))))

    def update(self, flag):
        global hp_ene, win_surface, gameplay_surface
        if x == 100 and self.x != x:
            self.rect = self.rect.move(100 - self.x, 0)
            self.x = x
        self.rect = self.rect.move(x - self.x, y - self.y)
        self.x, self.y = x, y
        one_hit_flag = True
        if flag:
            for i in self.frames_p:
                if pygame.sprite.collide_mask(self, mov_enemy) and one_hit_flag and x1 > x:
                    hp_ene -= attack_power_her
                    one_hit_flag = False
                    if hp_ene <= 0:
                        pygame.mixer.music.fadeout(2000)
                        gameplay_surface = False
                        win_surface = True
                        flag_win = True
                    hp = Hp()
                self.image = i
                self.mask = pygame.mask.from_surface(self.image)
                background_gameplay_sprites.draw(screen)
                background_gameplay_sprites.update()
                hp = Hp()
                gameplay_sprites.draw(screen)
                hit_hero_sprites.draw(screen)
                mov_enemy_sprites.draw(screen)                         ############# ни хатю писать статичного
                pygame.display.flip()
                clock.tick(7)
        else:
            for i in self.frames_l:
                if pygame.sprite.collide_mask(self, mov_enemy) and one_hit_flag and x1 < x:
                    hp_ene -= attack_power_her
                    one_hit_flag = False
                    if hp_ene <= 0:
                        pygame.mixer.music.fadeout(2000)
                        gameplay_surface = False
                        win_surface = True
                        flag_win = True
                    hp = Hp()
                self.image = i
                self.mask = pygame.mask.from_surface(self.image)
                background_gameplay_sprites.draw(screen)
                background_gameplay_sprites.update()
                hp = Hp()
                gameplay_sprites.draw(screen)
                hit_hero_sprites.draw(screen)
                mov_enemy_sprites.draw(screen)
                pygame.display.flip()
                clock.tick(7)


class Movement_enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(mov_enemy_sprites)
        self.frames_p = []
        self.frames_l = []
        self.loading_frames_p()
        self.loading_frames_l()
        self.cur_frame_p = 0
        self.cur_frame_l = 0
        self.image = self.frames_p[self.cur_frame_p]
        self.rect = self.rect_p.move(x1, y1)
        self.image = self.frames_l[self.cur_frame_l]
        self.rect = self.rect_l.move(x1, y1)
        self.x1 = x1

    def loading_frames_p(self):
        for i in range(7):
            frame = load_image(f"gameplay\враг ходит\{i} кадр_п.png")
            self.rect_p = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_p.append(frame.subsurface(pygame.Rect((0, 0), (240, 253))))

    def loading_frames_l(self):
        for i in range(7):
            frame = load_image(f"gameplay\враг ходит\{i} кадр_л.png")
            self.rect_l = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_l.append(frame.subsurface(pygame.Rect((0, 0), (240, 253))))
 
    def update(self):
        global x1
        if x1 == 700 and self.x1 != x1:
            self.rect = self.rect.move(700 - self.x1, 0)
        self.x1 = x1
        if x - 230 > x1:
            x1 += speed_ene
            self.rect = self.rect.move(speed_ene, 0)
            self.cur_frame_p = (self.cur_frame_p + 1) % len(self.frames_p)
            self.image = self.frames_p[self.cur_frame_p]
        elif x + 80 < x1:
            x1 -= speed_ene
            self.rect = self.rect.move(-speed_ene, 0)
            self.cur_frame_l = (self.cur_frame_l + 1) % len(self.frames_l)
            self.image = self.frames_l[self.cur_frame_l]
        else:
            self.mask = pygame.mask.from_surface(self.image)
            hit_enemy_sprites.update()


class Hit_enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__(hit_enemy_sprites)
        self.frames_p = []
        self.frames_l = []
        self.loading_frames_p()
        self.loading_frames_l()
        self.cur_frame_p = 0
        self.cur_frame_l = 0
        self.image = self.frames_p[self.cur_frame_p]
        self.rect = self.rect_p.move(x1, y1 + 30)
        self.image = self.frames_l[self.cur_frame_l]
        self.rect = self.rect_l.move(x1, y1 + 30)
        self.x1, self.y1 = x1, y1

    def loading_frames_p(self):
        for i in range(4):
            frame = load_image(f"gameplay\враг бьет\{i} кадр_п.png")
            self.rect_p = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_p.append(frame.subsurface(pygame.Rect((0, 0), (299, 219))))

    def loading_frames_l(self):
        for i in range(4):
            frame = load_image(f"gameplay\враг бьет\{i} кадр_л.png")
            self.rect_l = pygame.Rect(0, 0, frame.get_width(), 
                                frame.get_height())
            self.frames_l.append(frame.subsurface(pygame.Rect((0, 0), (299, 219))))

    def update(self):
        global hp_her, los_surface, gameplay_surface, chet1
        if x1 == 700 and self.x1 != x1:
            self.rect = self.rect.move(700 - self.x1, 0)
            self.x1 = x1
        one_hit_flag = True
        if chet1 == 7: # - задержка после удара
            if x >= x1:
                self.rect = self.rect.move(x1 - self.x1 + 50, y1 - self.y1)
                self.x1, self.y1 = x1, y1
                for i in self.frames_p:
                    if pygame.sprite.collide_mask(self, static_her) and one_hit_flag:
                        hp_her -= attack_power_ene
                        one_hit_flag = False
                        if hp_her <= 0:
                            pygame.mixer.music.fadeout(2000)
                            gameplay_surface = False
                            los_surface = True
                            flag_los = True
                        hp = Hp()
                    self.image = i
                    self.mask = pygame.mask.from_surface(self.image)
                    background_gameplay_sprites.draw(screen)
                    background_gameplay_sprites.update()
                    hp = Hp()
                    gameplay_sprites.draw(screen)
                    static_hero_sprites.update(direction_mov)
                    static_hero_sprites.draw(screen)               
                    hit_enemy_sprites.draw(screen)
                    pygame.display.flip()
                    clock.tick(7)
                self.rect = self.rect.move(-50, 0)
            if x < x1:
                self.rect = self.rect.move(x1 - self.x1 - 50, y1 - self.y1) 
                self.x1, self.y1 = x1, y1
                for i in self.frames_l:
                    if pygame.sprite.collide_mask(self, static_her) and one_hit_flag:
                        hp_her -= attack_power_ene
                        one_hit_flag = False
                        if hp_her <= 0:
                            pygame.mixer.music.fadeout(2000)
                            gameplay_surface = False
                            los_surface = True
                            flag_los = True
                        hp = Hp()
                    self.image = i
                    self.mask = pygame.mask.from_surface(self.image)
                    background_gameplay_sprites.draw(screen)
                    background_gameplay_sprites.update()
                    hp = Hp()
                    gameplay_sprites.draw(screen)
                    static_hero_sprites.update(direction_mov)
                    static_hero_sprites.draw(screen)
                    hit_enemy_sprites.draw(screen)
                    pygame.display.flip()
                    clock.tick(7)
                self.rect = self.rect.move(50, 0)
            chet1 = 0
        else:
            chet1 += 1

 
pygame.init()
clock = pygame.time.Clock()
size = width, height = 1024, 576
screen = pygame.display.set_mode(size)

menu_hero_sprites = pygame.sprite.Group()
campfire_sprites = pygame.sprite.Group()
effects_menu_sprites = pygame.sprite.Group()
background_los_surface_sprites = pygame.sprite.Group()
background_gameplay_sprites = pygame.sprite.Group()
static_hero_sprites = pygame.sprite.Group()
mov_hero_sprites = pygame.sprite.Group()
hit_hero_sprites = pygame.sprite.Group()
mov_enemy_sprites = pygame.sprite.Group()
hit_enemy_sprites = pygame.sprite.Group()

menu_hero = Menu_hero()
campfire = Campfire()
effects_menu = Effects_menu()
background_los = Background_los_surface()
background_gameplay = Background_gameplay()
static_her = Static_hero()
mov_hero = Movement_hero()
hit_hero = Hit_hero()
mov_enemy = Movement_enemy()
hit_ene = Hit_enemy()

menu_sprites = pygame.sprite.Group()
background_menu = pygame.sprite.Sprite()
background_menu.image = load_image("меню\фон.png")
background_menu.rect = background_menu.image.get_rect()
title_begin = pygame.sprite.Sprite()
title_begin.image = load_image("меню\надпись.png")
title_begin.rect = title_begin.image.get_rect()
title_begin.rect = title_begin.rect.move(590, 380)
game_name = pygame.sprite.Sprite()
game_name.image = load_image("меню\название игры.png")
game_name.rect = game_name.image.get_rect()
game_name.rect = game_name.rect.move(360, 30)
complexity_eas = pygame.sprite.Sprite()
complexity_eas.image = load_image("меню\легкая сложность.png")
complexity_eas.rect = complexity_eas.image.get_rect()
complexity_eas.rect = complexity_eas.rect.move(730, 443)
complexity_med = pygame.sprite.Sprite()
complexity_med.image = load_image("меню\средняя сложность.png")
complexity_med.rect = complexity_med.image.get_rect()
complexity_med.rect = complexity_med.rect.move(690, 485)
complexity_har = pygame.sprite.Sprite()
complexity_har.image = load_image("меню\тяжелая сложность.png")
complexity_har.rect = complexity_har.image.get_rect()
complexity_har.rect = complexity_har.rect.move(620, 530)
tick = pygame.sprite.Sprite()
tick.image = load_image("меню\галочка.png")
tick.rect = tick.image.get_rect()
tick.rect = tick.rect.move(640, 495)

menu_sprites.add(background_menu)
menu_sprites.add(title_begin)
menu_sprites.add(complexity_eas)
menu_sprites.add(complexity_med)
menu_sprites.add(complexity_har)
menu_sprites.add(tick)
menu_sprites.add(game_name)

win_surface_sprites = pygame.sprite.Group()
background_win_surface = pygame.sprite.Sprite()
background_win_surface.image = load_image("окно победы\фон.png")
background_win_surface.rect = background_win_surface.image.get_rect()
background_win_surface.rect = background_win_surface.rect.move(0, -640)
title_win = pygame.sprite.Sprite()
title_win.image = load_image("окно победы\надпись.png")
title_win.rect = title_win.image.get_rect()
title_win.rect = title_win.rect.move(300, 410)
title_menu_win = pygame.sprite.Sprite()
title_menu_win.image = load_image("окно победы\надпись в меню.png")
title_menu_win.rect = title_menu_win.image.get_rect()
title_menu_win.rect = title_menu_win.rect.move(450, 490)
win_surface_sprites.add(background_win_surface)
win_surface_sprites.add(title_menu_win)
win_surface_sprites.add(title_win)

los_surface_sprites = pygame.sprite.Group()
title_los = pygame.sprite.Sprite()
title_los.image = load_image("окно поражения\надпись.png")
title_los.rect = title_los.image.get_rect()
title_los.rect = title_los.rect.move(540, 120)
title_menu_los = pygame.sprite.Sprite()
title_menu_los.image = load_image("окно победы\надпись в меню.png")
title_menu_los.rect = title_menu_los.image.get_rect()
title_menu_los.rect = title_menu_los.rect.move(615, 220)
los_surface_sprites.add(title_menu_los)
los_surface_sprites.add(title_los)

gameplay_sprites = pygame.sprite.Group()
logotype = pygame.sprite.Sprite()
logotype.image = load_image("gameplay\логотип.png")
logotype.rect = logotype.image.get_rect()
logotype.rect = logotype.rect.move(15, 20)       
strip_health_her = pygame.sprite.Sprite()
strip_health_her.image = load_image("gameplay\полоска здоровья героя.png")
strip_health_her.rect = strip_health_her.image.get_rect()
strip_health_her.rect = strip_health_her.rect.move(20, 10)
strip_health_ene = pygame.sprite.Sprite()
strip_health_ene.image = load_image("gameplay\полоска здоровья врага.png")
strip_health_ene.rect = strip_health_ene.image.get_rect()
strip_health_ene.rect = strip_health_ene.rect.move(555, -23) 
gameplay_sprites.add(strip_health_her)
gameplay_sprites.add(strip_health_ene)
gameplay_sprites.add(logotype)

eazy_compl_flag = False
medium_compl_flag = True
hard_compl_flag = False
flag_los = True
flag_win = True
flag_menu = True
flag_gameplay = True
direction_mov = True
mov_hero_flag = False
menu_surface = True
gameplay_surface = False
los_surface = False
win_surface = False
shift = False
running = True
chet = 0
chet1 = 7
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gameplay_surface:
                hit_hero_sprites.update(direction_mov)
            if menu_surface:
                if 590 <= event.pos[0] <= 967 and 380 <= event.pos[1] <= 447:
                    menu_surface = False
                    gameplay_surface = True
                    flag_gameplay = True
                    pygame.mixer.music.fadeout(2000)
                if 730 <= event.pos[0] <= 839 and 443 <= event.pos[1] <= 483:
                    if medium_compl_flag:
                        tick.rect = tick.rect.move(40, -42)
                        medium_compl_flag = False
                    if hard_compl_flag:
                        tick.rect = tick.rect.move(110, -87)
                        hard_compl_flag = False
                    attack_power_her = 25
                    attack_power_ene = 25
                    speed_her = 15
                    speed_ene = 5
                    eazy_compl_flag = True
                if 690 <= event.pos[0] <= 869 and 485 <= event.pos[1] <= 526:
                    if eazy_compl_flag:
                        tick.rect = tick.rect.move(-40, 42)
                        eazy_compl_flag = False
                    if hard_compl_flag:
                        tick.rect = tick.rect.move(70, -45)
                        hard_compl_flag = False
                    attack_power_her = 15
                    attack_power_ene = 35
                    speed_her = 10
                    speed_ene = 10
                    medium_compl_flag = True
                if 620 <= event.pos[0] <= 968 and 530 <= event.pos[1] <= 571:
                    if eazy_compl_flag:
                        tick.rect = tick.rect.move(-110, 87)
                        eazy_compl_flag = False
                    if medium_compl_flag:
                        tick.rect = tick.rect.move(-70, 45)
                        medium_compl_flag = False
                    attack_power_her = 10
                    attack_power_ene = 50
                    speed_her = 6
                    speed_ene = 15
                    hard_compl_flag = True
            if win_surface:
                if 450 <= event.pos[0] <= 597 and 490 <= event.pos[1] <= 546:
                    win_surface = False
                    menu_surface = True
                    flag_menu = True
                    pygame.mixer.music.fadeout(2000)
                    x, y = 100, 325
                    x1, y1 = 700, 290
                    hp_her, hp_ene = 100, 100
                    mov_hero_sprites.update(True)
            if los_surface:
                if 615 <= event.pos[0] <= 762 and 220 <= event.pos[1] <= 276:
                    los_surface = False
                    menu_surface = True
                    flag_menu = True
                    pygame.mixer.music.fadeout(2000)
                    x, y = 100, 325
                    x1, y1 = 700, 290
                    hp_her, hp_ene = 100, 100
                    mov_hero_sprites.update(True)
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                direction_mov = True
                mov_hero_flag = not mov_hero_flag
                shift = False
            if event.key == pygame.K_a:
                direction_mov = False
                mov_hero_flag = not mov_hero_flag
                shift = False
            if event.key == pygame.K_d and event.mod == pygame.KMOD_LSHIFT:
                shift = not shift
            if event.key == pygame.K_a and event.mod == pygame.KMOD_LSHIFT:
                shift = not shift
    if menu_surface:
        if flag_menu:
            pygame.mixer.music.load('data\меню\музыка.mp3')
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            flag_menu = False                    
        menu_sprites.draw(screen)
        campfire_sprites.draw(screen)
        campfire_sprites.update()
        effects_menu_sprites.draw(screen)
        effects_menu_sprites.update()
        if chet == 3:
            menu_hero_sprites.update()
            chet = 0
        else:
            chet += 1
        menu_hero_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(15)                   
    if gameplay_surface:
        if flag_gameplay:
            pygame.mixer.music.load('data\gameplay\On the Champs-Désolés.mp3')
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play()
            flag_gameplay = False
        background_gameplay_sprites.draw(screen)
        background_gameplay_sprites.update()
        hp = Hp()
        gameplay_sprites.draw(screen)
        mov_enemy_sprites.draw(screen)
        mov_enemy_sprites.update()
        if mov_hero_flag:
            mov_hero_sprites.draw(screen)
            if direction_mov:
                mov_hero_sprites.update(True)
            else:
                mov_hero_sprites.update(False)
        else:
            static_hero_sprites.update(direction_mov)
            static_hero_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(5)
    if win_surface:
        if flag_win:
            pygame.mixer.music.fadeout(2000)
            pygame.mixer.music.load('data\окно победы\Лютик - Ведьмаку заплатите чеканной монетой.mp3')
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            flag_win = False
        win_surface_sprites.draw(screen)
        pygame.display.flip()
    if los_surface:
        if flag_los:
            pygame.mixer.music.fadeout(2000)
            pygame.mixer.music.load('data\окно поражения\музыка.mp3')
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            flag_los = False
        background_los_surface_sprites.draw(screen)
        background_los_surface_sprites.update()
        los_surface_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(5)
pygame.quit()
