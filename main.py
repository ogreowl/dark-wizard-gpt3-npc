##Imports **********************************************************************
import pygame;
import random;
import time;
import os;
import openai;
pygame.init();
###openai.api_key = ## Get your key to insert here from OpenAI.com. Running this program will cost a few cents.
##Imports **********************************************************************
#
#
#
##OpenAI Language Inputs **********************************************************************
context1 = "You are a demon wizard who uses dark magic. A foolish young lad comes up to you. He says: ";
context2 = "Say something manipulative in response: ";
context3 = "You responded: ";
context4 = "He then said: ";
##OpenAI Language Inputs **********************************************************************
#
#
#
##PyGame Set-up **********************************************************************
screen_width = 600;
screen_height = 650;
screen = pygame.display.set_mode((screen_width, screen_height));
font = pygame.font.SysFont('Times New Roman', 26);
white = (255, 255, 255);
##PyGame Set-up **********************************************************************
#
#
#
##Load Images **********************************************************************
bg_img = pygame.image.load("Dark_Wizard_Image.png").convert_alpha();
panel_img = pygame.image.load("Panel_Image.png").convert_alpha();
##Load Images **********************************************************************
#
#
#
##Functions **********************************************************************************
def draw_bg(): #Draws the background
    scaled_bg = pygame.transform.scale(bg_img, (screen_width, 450));
    screen.blit(scaled_bg, (0,0));

def draw_panel(): #Draws the space where the text appears
    scaled_panel = pygame.transform.scale(panel_img, (screen_width, 200));
    screen.blit(scaled_panel, (0,450));

def text1(word,x,y): #Renders the player text
    font = pygame.font.SysFont('Times New Roman', 15);
    text = font.render("{}".format(word), True, white);
    return screen.blit(text,(x,y));

def text2(word,x,y): #Renders the NPC text
    font = pygame.font.SysFont('Times New Roman', 15);
    text = font.render("{}".format(word), True, white);
    return screen.blit(text,(x,y));

def inpt(): #Takes in player inputs
    word="";
    pygame.display.flip();
    done = True;
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_RETURN:
                    word+=str(chr(event.key));
                if event.key == pygame.K_RETURN:
                    done=False;
                    # BUGs NEED FIXING here:
                    # 1: Game crashes when you press shift
                    # 2: You can't see your text until you press enter
                    # 3: No delete button
    return word;
##Functions **********************************************************************************************
#
#
#
##pygame Program *******************************************************************************************
run = True;
while run:
    draw_bg();
    draw_panel();
    playerInput = inpt();
    text1(playerInput,10,455);
    inpt(); #Don't know if this is needed here... will test

    ## Can probably be made into a simpler function where you just input the prompt
    wizardResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt= context1 + playerInput + context2,
        temperature=0.6,
        max_tokens = 50,
    );
    response = wizardResponse['choices'][0]['text'].strip();

    ## This stuff here is needed to display the text line-by-line
    ## Will experiment with turning this into a function to improve readability / organization
    n = 90;
    stringList = [response[idx:idx + n] for idx in range(0, len(response), n)]
    if len(stringList) == 1:
        text2(stringList[0], 10, 470);
    if len(stringList) == 2:
        text2(stringList[0], 10, 470);
        text2(stringList[1], 10, 485);
    if len(stringList) == 3:
        text2(stringList[0], 10, 470);
        text2(stringList[1], 10, 485);
        text2(stringList[2], 10, 500);

    playerInput2 = inpt();
    text1(playerInput2,10,515);
    inpt(); # Don't know if this is needed
    wizardResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt= context1 + playerInput + context3 + response + context4 + playerInput2 + context2,
        temperature=0.6,
        max_tokens = 40,
    );
    ## I know, I know... not the most organized here. Mean't to save the past conversation to preserve the chatbot's memory.
    prompt2 = context1 + playerInput + context3 + response + context4 + playerInput2 + context3;
    response = wizardResponse['choices'][0]['text'].strip();
    prompt2 = prompt2 + response + context4;

    n = 90;
    newList = [response[idx:idx + n] for idx in range(0, len(response), n)]
    if len(newList) == 1:
        text2(newList[0], 10, 530);
    if len(newList) == 2:
        text2(newList[0], 10, 530);
        text2(newList[1], 10, 545);
    if len(newList) == 3:
        text2(newList[0], 10, 530);
        text2(newList[1], 10, 545);
        text2(newList[2], 10, 560);

    playerInput2 = inpt();
    text1(playerInput2,10,575);
    inpt();

    prompt2 = prompt2 + playerInput2 + context2;
    wizardResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt2,
        temperature=0.6,
        max_tokens = 40,
    );
    response = wizardResponse['choices'][0]['text'].strip();

    n = 90;
    newList = [response[idx:idx + n] for idx in range(0, len(response), n)];
    if len(newList) == 1:
        text2(newList[0], 10, 590);
    if len(newList) == 2:
        text2(newList[0], 10, 590);
        text2(newList[1], 10, 605);
    if len(newList) == 3:
        text2(newList[0], 10, 590);
        text2(newList[1], 10, 605);
        text2(newList[2], 10, 620);

    inpt();

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False;

    pygame.display.update()
##pygame Program  *******************************************************************************************
pygame.quit()
