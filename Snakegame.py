import pygame as py
import sys,random
from pygame.math import Vector2
class MAIN():
    def __init__(self):
        self.snake=SNAKE()
        self.fruit=Fruit()

    def update(self):
        self.snake.movesnake()
        self.check_coll()
        self.check_fail()
    def draw_elem(self):
        self.draw_grass()
        self.fruit.drawfruit()
        self.snake.draw_snake()
        self.show_score()
        
    def check_coll(self):
        if self.fruit.pos==self.snake.body[0]:
            self.fruit.randomize()
            self.snake.addblock()
            self.snake.play_sound()
        for block in self.snake.body[1:]:
            if block==self.fruit.pos:
                self.fruit.randomize()
    def check_fail(self):
        if not 0<= self.snake.body[0].x < cell_n or not 0<= self.snake.body[0].y < cell_n:
            self.game_over()
          
            
            

        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                self.game_over()
                
                
                
    def game_over(self):
            self.snake.reset()
            self.snake.play_gosound()
      
    def draw_grass(self):
        grass_color=(0,236,118)
        for row in range(cell_n):
            if row%2==0:
                for col in range(cell_n):
                    if col%2==0:
                        grass_rect=py.Rect(col*cell_s,row*cell_s,cell_s,cell_s)
                        py.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_n):
                    if col%2==1:
                        grass_rect=py.Rect(col*cell_s,row*cell_s,cell_s,cell_s)
                        py.draw.rect(screen,grass_color,grass_rect)
    
    def show_score(self):
        score=str(len(self.snake.body)-3)
        score_surface=font.render(score,True,(255,0,0))
        score_x=int((cell_s*cell_n)-60)
        score_y=int((cell_s*cell_n)-40)
        score_rect=score_surface.get_rect(center=(score_x,score_y))
        apple_rect=apple.get_rect(midright=(score_rect.left,score_rect.centery))
        bg_rect=py.Rect(apple_rect.left,apple_rect.top,apple_rect.width+5+score_rect.width+6,apple_rect.height)
        py.draw.rect(screen,(0,255,128),bg_rect)

        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        py.draw.rect(screen,(58,74,12),bg_rect,2)

                        
class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(0,1)
        self.newblock=False
        self.head_up=py.image.load("G:/Arun joseph/s_headup.png").convert_alpha()
        self.head_down=py.image.load("G:/Arun joseph/s_headdown.jpg").convert_alpha()
        self.head_left=py.image.load('G:/Arun joseph/s_headleft.png').convert_alpha()
        self.head_right=py.image.load('G:/Arun joseph/s_headright.png').convert_alpha()

        self.tail_down=py.image.load('G:/Arun joseph/s_tailup.png').convert_alpha()
        self.tail_up=py.image.load('G:/Arun joseph/s_taildown.png').convert_alpha()
        self.tail_right=py.image.load('G:/Arun joseph/s_tailleft.png').convert_alpha()
        self.tail_left=py.image.load('G:/Arun joseph/s_tailright.png').convert_alpha()

        self.body_tr=py.image.load('G:/Arun joseph/s_tr.png').convert_alpha()
        self.body_tl=py.image.load('G:/Arun joseph/s_tl.png').convert_alpha()
        self.body_bl=py.image.load('G:/Arun joseph/b_bl.png').convert_alpha()
        self.body_br=py.image.load('G:/Arun joseph/b_br.png').convert_alpha()

        self.body_horizontal=py.image.load('G:/Arun joseph/s_horizontal.png').convert_alpha()
        self.body_vertical=py.image.load('G:/Arun joseph/s_vertical.png').convert_alpha()
        self.sound=py.mixer.Sound('G:/Arun joseph/ra.wav')
        self.gosound=py.mixer.Sound('G:/Arun joseph/gover.wav')
    def addblock(self):
        self.newblock=True
        
    def draw_snake(self):

        
        self.update_head()
        self.update_tail()

        
        for index,block in enumerate(self.body):
            x_pos=int(block.x*cell_s)
            y_pos=int(block.y*cell_s)
            block_rect=py.Rect(x_pos,y_pos,cell_s,cell_s)

            if index==0:
                screen.blit(self.head,block_rect)
            elif index==len(self.body)-1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block=self.body[index+1]-block
                next_block=self.body[index-1]-block
                if previous_block.x==next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y==next_block.y:
                    screen.blit(self.body_horizontal,block_rect)   
                else:
                    if previous_block.x==-1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==-1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x==-1 and next_block.y==1 or previous_block.y==1 and next_block.x==-1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x==1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x==1 and next_block.y==1 or previous_block.y==1 and next_block.x==1:
                        screen.blit(self.body_br,block_rect)
            
    def update_head(self):
        head_relate=self.body[1]-self.body[0]
        if head_relate==Vector2(1,0):
            self.head=self.head_left
        elif head_relate==Vector2(-1,0):
            self.head=self.head_right
        elif head_relate==Vector2(0,1):
            self.head=self.head_up
        elif head_relate==Vector2(0,-1):
            self.head=self.head_down

    def update_tail(self):
        tail_relate=self.body[-2]-self.body[-1]

        if tail_relate==Vector2(1,0):
                self.tail=self.tail_left
        elif tail_relate==Vector2(-1,0):
            self.tail=self.tail_right
        elif tail_relate==Vector2(0,1):
            self.tail=self.tail_up
        elif tail_relate==Vector2(0,-1):
            self.tail=self.tail_down
    def movesnake(self):
        if self.newblock==True:
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
            self.newblock=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
    def play_sound(self):
        self.sound.play()
    def play_gosound(self):
        self.gosound.play()
    def reset(self):
        self.body=[Vector2(6,10),Vector2(5,10),Vector2(4,10)]

class Fruit:
    def __init__(self):
      self.randomize()
    def drawfruit(self):
        fruit_rect=py.Rect(int(self.pos.x*cell_s),int(self.pos.y*cell_s),cell_s,cell_s)
        #py.draw.rect(screen,(11,32,116),fruit_rect)
        screen.blit(apple,fruit_rect)
    def randomize(self):
        self.x=random.randint(0,cell_n-1)
        self.y=random.randint(0,cell_n-1)
        self.pos=py.math.Vector2(self.x,self.y)
py.init()
cell_s=20
cell_n=32
screen=py.display.set_mode((cell_s*cell_n,cell_s*cell_n))
clock=py.time.Clock()
apple=py.image.load("G:/Arun joseph/apple.jpg").convert_alpha()

font=py.font.Font('G:/Arun joseph/game_font.ttf',20)
SCREEN_UPDATE=py.USEREVENT
py.time.set_timer(SCREEN_UPDATE,150)
main_g=MAIN()
while True:
    for event in py.event.get():
        if event.type==py.QUIT:
            py.quit()
            sys.exit()
        if event.type==SCREEN_UPDATE:
             main_g.update() 
        if event.type==py.KEYDOWN:
            if event.key==py.K_UP:
                if main_g.snake.direction.y !=1:
                    main_g.snake.direction=Vector2(0,-1)
            if event.key==py.K_DOWN:
                if main_g.snake.direction.y !=-1:
                    main_g.snake.direction=Vector2(0,1)
            if event.key==py.K_RIGHT:
                if main_g.snake.direction.x !=-1:
                    main_g.snake.direction=Vector2(1,0)   
            if event.key==py.K_LEFT:
                if main_g.snake.direction.x !=1:
                    main_g.snake.direction=Vector2(-1,0)   
    screen.fill(py.Color(0,255,128))
    main_g.draw_elem()
 
    py.display.update()
    clock.tick(150)
