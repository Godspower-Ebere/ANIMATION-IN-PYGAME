import pygame
pygame.init()
size=width,height=1000,600
screen=pygame.display.set_mode((size))
pygame.display.set_caption("ANIMATION BY GP")
icon=pygame.transform.scale(pygame.image.load("Idle__000.png"),(50,100))
pygame.display.set_icon(icon)

count=0
bgcount=0
x=width/2
y=height/2-50
vel=5
stop=0
tr=False
tl=False
sl=False
sr=False
left=False
right=False
jump=False
jumpl=False
attack=False
idle=[pygame.transform.scale(pygame.image.load("Idle__000.png"),(90,140)),
      pygame.transform.scale(pygame.image.load("Idle__001.png"),(90,140)),
      pygame.transform.scale(pygame.image.load("Idle__002.png"),(90,140)),
      pygame.transform.scale(pygame.image.load("Idle__003.png"),(90,140)),
      pygame.transform.scale(pygame.image.load("Idle__004.png"),(90,140)),
      pygame.transform.scale(pygame.image.load("Idle__005.png"),(90,140)),
      pygame.transform.scale(pygame.image.load("Idle__006.png"),(90,140)),
      pygame.transform.scale(pygame.image.load("Idle__007.png"),(90,140)),
      pygame.transform.scale(pygame.image.load("Idle__008.png"),(90,140)),
      pygame.transform.scale(pygame.image.load("Idle__009.png"),(90,140))
      ]
idleleft=[pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__000.png"),(90,140)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__001.png"),(90,140)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__002.png"),(90,140)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__003.png"),(90,140)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__004.png"),(90,140)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__005.png"),(90,140)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__006.png"),(90,140)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__007.png"),(90,140)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__008.png"),(90,140)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Idle__009.png"),(90,140)),True,False)
         ]


run1=[pygame.transform.scale(pygame.image.load("Run__000.png"),(100,150)),
     pygame.transform.scale(pygame.image.load("Run__001.png"),(100,150)),
     pygame.transform.scale(pygame.image.load("Run__002.png"),(100,150)),
     pygame.transform.scale(pygame.image.load("Run__003.png"),(100,150)),
     pygame.transform.scale(pygame.image.load("Run__004.png"),(100,150)),
     pygame.transform.scale(pygame.image.load("Run__005.png"),(100,150)),
     pygame.transform.scale(pygame.image.load("Run__006.png"),(100,150)),
     pygame.transform.scale(pygame.image.load("Run__007.png"),(100,150)),
     pygame.transform.scale(pygame.image.load("Run__008.png"),(100,150)),
     pygame.transform.scale(pygame.image.load("Run__009.png"),(100,150))
     ]

leftrun=[pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__000.png"),(100,150)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__001.png"),(100,150)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__002.png"),(100,150)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__003.png"),(100,150)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__004.png"),(100,150)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__005.png"),(100,150)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__006.png"),(100,150)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__007.png"),(100,150)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__008.png"),(100,150)),True,False),
         pygame.transform.flip(pygame.transform.scale(pygame.image.load("Run__009.png"),(100,150)),True,False)
         ]
attack1=[
        pygame.transform.scale(pygame.image.load("Attack__000.png"),(150,150)),
        pygame.transform.scale(pygame.image.load("Attack__001.png"),(150,150)),
        pygame.transform.scale(pygame.image.load("Attack__002.png"),(150,150)),
        pygame.transform.scale(pygame.image.load("Attack__003.png"),(150,150)),
        pygame.transform.scale(pygame.image.load("Attack__004.png"),(150,150)),
        pygame.transform.scale(pygame.image.load("Attack__005.png"),(150,150)),
        pygame.transform.scale(pygame.image.load("Attack__006.png"),(150,150)),
        pygame.transform.scale(pygame.image.load("Attack__007.png"),(150,150)),
        pygame.transform.scale(pygame.image.load("Attack__008.png"),(150,150)),
        pygame.transform.scale(pygame.image.load("Attack__009.png"),(150,150))
        ]
dead1=[pygame.transform.scale(pygame.image.load("Dead__000.png"),(100,150)),
      pygame.transform.scale(pygame.image.load("Dead__001.png"),(100,150)),
      pygame.transform.scale(pygame.image.load("Dead__002.png"),(100,150)),
      pygame.transform.scale(pygame.image.load("Dead__003.png"),(100,150)),
      pygame.transform.scale(pygame.image.load("Dead__004.png"),(100,150)),
      pygame.transform.scale(pygame.image.load("Dead__005.png"),(100,150)),
      pygame.transform.scale(pygame.image.load("Dead__006.png"),(100,150)),
      pygame.transform.scale(pygame.image.load("Dead__007.png"),(100,150)),
      pygame.transform.scale(pygame.image.load("Dead__008.png"),(100,150)),
      pygame.transform.scale(pygame.image.load("Dead__009.png"),(100,150))
      ]
jump1=[
      pygame.transform.scale(pygame.image.load("Jump__000.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Jump__001.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Jump__002.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Jump__003.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Jump__004.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Jump__005.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Jump__006.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Jump__007.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Jump__008.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Jump__009.png"),(120,150))
      ]
jump2=[
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__000.png"),(120,150)),True,False),
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__001.png"),(120,150)),True,False),
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__002.png"),(120,150)),True,False),
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__003.png"),(120,150)),True,False),
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__004.png"),(120,150)),True,False),
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__005.png"),(120,150)),True,False),
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__006.png"),(120,150)),True,False),
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__007.png"),(120,150)),True,False),
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__008.png"),(120,150)),True,False),
      pygame.transform.flip(pygame.transform.scale(pygame.image.load("Jump__009.png"),(120,150)),True,False)
      ]
Throw1=[
      pygame.transform.scale(pygame.image.load("Throw__000.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Throw__001.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Throw__002.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Throw__003.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Throw__004.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Throw__005.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Throw__006.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Throw__007.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Throw__008.png"),(120,150)),
      pygame.transform.scale(pygame.image.load("Throw__009.png"),(120,150))
      ]

bg1=pygame.image.load("bg.png")
bg1trans=pygame.transform.scale(bg1,(width,height))
bgrect=bg1trans.get_rect()

bg2=pygame.image.load("bg.png")
bg2trans=pygame.transform.flip(pygame.transform.scale(bg2,(width,height)),True,False)

bgx1=0
bgx2=bgrect.width

clock=pygame.time.Clock()

run=True
while run:

    clock.tick(60)
    screen.blit(bg1trans,(bgx1,0))
    screen.blit(bg2trans,(bgx2,0))
    
    count+=0.25
    if count>=9:
        count=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                run=False
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                left=False
                sl=True
                sr=False
            if event.key==pygame.K_RIGHT:
                right=False
                sl=False
                sr=True
                
    
            
    key=pygame.key.get_pressed()
    
    if key[pygame.K_LEFT]:
        left=True
        right=False
        
    if key[pygame.K_RIGHT]:
        right=True
        left=False
    if key[pygame.K_d]:
        tr=True
   
      
    if key[pygame.K_SPACE]:
        if sr==True:
            jump=True
        if sl==True:
            jumpl=True
    if key[pygame.K_SPACE] and key[pygame.K_LEFT]:
        if left==True:
            jumpl=True
            jump=False
    if key[pygame.K_SPACE] and key[pygame.K_RIGHT]:
        if right==True:
            jump=True
            jumpl=False
        
    if key[pygame.K_f] and key[pygame.K_m]:
        print("both")
        attack=True
        
    if jump:
        
        jumping=jump1[int(count)]
        screen.blit(jumping,(x,y))
        y-=vel
        vel-=0.1
        if vel <= -5:
            vel=5
            jump=False
    elif jumpl:
        
        jumping2=jump2[int(count)]
        screen.blit(jumping2,(x,y))
        y-=vel
        vel-=0.1
        if vel <= -5:
            vel=5
            jumpl=False
    elif left:
        bgx1+=10
        bgx2+=10
        if bgx1 >= width:
            bgx1=-width
        if bgx2 >=width:
            bgx2=-width
        left=leftrun[int(count)]
        screen.blit(left,(x,y))
        attack=False
    elif right:
        bgx1-=10
        bgx2-=10
        if bgx1 <= -width:
            bgx1=width
        if bgx2 <= -width:
            bgx2=width
        run=run1[int(count)]
        screen.blit(run,(x,y))
        attack=False
    elif attack:
        att=attack1[int(count)]
        screen.blit(att,(x,y))
        stop+=1
        if stop>=60:
            attack=False
            stop=0
    elif sl==True:
        standleft=idleleft[int(count)]
        screen.blit(standleft,(x,y))
    elif sr==True:
        stand=idle[int(count)]
        screen.blit(stand,(x,y))
    else:
        stand=idle[int(count)]
        screen.blit(stand,(x,y))
        
    pygame.display.update()
pygame.quit()



