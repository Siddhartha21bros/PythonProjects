import pygame
import random
pygame.init()

# Colours definitions:
white= (255,255,255)
Red = (255,0,0)
Black= (0,0,0)


screen_width=700
screen_height=600
gamewindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("SnakesWithSiddhartha")
pygame.display.update()



clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)

def text_Screen(text,colour,x,y):
    screen_text=font.render(text, True, colour)
    gamewindow.blit(screen_text, [x,y])


def plot_snake(gamewindow,colour,Snake_list,snake_size):
    for x,y in Snake_list:
            pygame.draw.rect(gamewindow,colour, [x,y,snake_size,snake_size] )

def gameLoop(): 
    #game specific variables
    exit_game=False
    Snake_x=45
    Snake_y=50
    Velocity_x=0
    Velocity_y=0
    snake_size=10
    init_velocity=4
    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    fps=60
    Score=0
    Game_Over=False
    Snake_list=[]
    Snake_length=1
    
    while not exit_game:
        if Game_Over:
            gamewindow.fill(white)
            text_Screen("Game Over! Press Enter to continue", Black, 2, 100)
            text_Screen("Score:"+str(Score*10),Black,2,200)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameLoop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        Velocity_x=init_velocity
                        Velocity_y=0
                        # This will make the snake move towards the right without us having to keep presing the button

                    elif event.key == pygame.K_LEFT:
                        Velocity_x=-init_velocity
                        Velocity_y=0

                    elif event.key == pygame.K_UP:
                        Velocity_y=-init_velocity
                        Velocity_x=0

                    elif event.key == pygame.K_DOWN:
                        Velocity_y=init_velocity
                        Velocity_x=0



            Snake_x= Snake_x+Velocity_x
            Snake_y=Snake_y+Velocity_y

            if abs(Snake_x-food_x)<6 and abs(Snake_y-food_y)<6:
                Score=Score+1
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                Snake_length=Snake_length+5


            gamewindow.fill(white)
            text_Screen("Score:"+ str(Score*10),Red,5,5)
            pygame.draw.rect(gamewindow,Black, [Snake_x,Snake_y,snake_size,snake_size] )
            pygame.draw.rect(gamewindow,Red, [food_x,food_y,snake_size,snake_size] )
            pygame.display.update()
            clock.tick(fps)
            head=[]
            head.append(Snake_x)
            head.append(Snake_y)
            Snake_list.append(head)

            if len(Snake_list)>Snake_length:
                del Snake_list[0]
            if Snake_x<0 or Snake_x>screen_width or Snake_y<0 or Snake_y>screen_height:
                Game_Over=True

            for i in range(1,len(Snake_list)):
                if Snake_list[0]==Snake_list[i]:
                    Game_Over=True
            
            plot_snake(gamewindow,Black,Snake_list,snake_size)
        pygame.display.update()




    pygame.quit()
    quit()

print(gameLoop())

