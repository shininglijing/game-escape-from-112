# Reference: 
# run function refers to http://www.cs.cmu.edu/~112/notes/events-example0.py
# mode dispacher functions refer to 
# http://www.cs.cmu.edu/~112/notes/notes-animations-examples.html#modeDemo

from tkinter import *
import random

####################################
# init
####################################

def init(data):
    data.mode = "welcomeScreen"
    data.loading = True
    data.score = 0
    data.fill = "green"
    data.item0 = PhotoImage(file = "item0.gif")
    data.count = 0
    data.clickInCircle = False

def initTitle(data):
    data.mode = "title"
    data.item1 = PhotoImage(file = "item1.gif")
    data.item1R = 40
    data.clickInCircle = False

def initIntroduction(data):
    data.mode = "introduction"
    data.item2 = PhotoImage(file = "item1.gif")
    data.item2R = 40
    data.countIntro = 0
    data.textX = 340 
    data.clickInCircle = False

def initBackground(data):
    data.mode = "background"
    data.item3 = PhotoImage(file = "item1.gif")
    data.item3R = 40
    data.countStep = 0
    data.x3 = data.width/2
    data.y3 = data.height/2
    data.x31 = data.width-100
    data.y31 = 100
    data.click = False

def initGameModeSelect(data):
    data.cx = data.width/2
    data.cy = data.height/2

def initTutorial(data):
    data.mode = "tutorial"
    data.item4 = PhotoImage(file = "item1.gif")
    data.item4R = 40
    data.countFlash = 0
    data.x4 = data.width/2
    data.y4 = data.height/2
    data.x41 = data.x4 - 100
    data.y41 = data.y4 + 230
    data.x42 = data.x4 + 100
    data.y42 = data.y4 + 230
    data.xLeft = data.x4 - 100
    data.xRight = data.x4 + 100
    data.yUp = data.height - 280
    data.yDown = data.height - 270
    data.clickInCircle = False

def initPlay(data):
    data.bgX = 0
    data.bgY = 0
    data.inTheSky = False
    data.currStuckBarrier = None
    data.topY = 350 # keep the player at the middle of the canvas
    data.barrierSpace = 100
    data.caught = False
    data.flyWithBalloon = False
    data.flyCount = 0
    data.gameOver = False
    data.doingHW = False
    data.doingQuiz = False
    data.doingTP = False
    data.isPaused = False
    data.barriers = ["Project", "HW", "HW", "Quiz", "Quiz", "Quiz", 
                     None, None, None]
    data.coins = 0
    data.score = 0
    data.steps = 0
    data.coinPoint = 1
    data.silverStarPoint = 5
    data.goldStarPoint = 10
    data.highestScore = 0 
    data.left = True
    data.leftX = data.cx - 80
    data.rightX = data.cx + 85
    data.initY = -50
    data.barriersOnCanvas = []
    data.coinInitY = 450
    data.barrierSpace = 100
    for i in range(5):
        y = data.coinInitY - data.barrierSpace * i
        x = random.choice([data.leftX, data.rightX])
        data.barriersOnCanvas.append(Coin(x, y))
    #init the movements of the player, Kosbie and CA
    data.leftXP = data.leftX+45
    data.rightXP = data.rightX-45
    data.player = Player(data.leftXP, 550)
    data.kosbie = Kosbie(data.leftXP, 800)
    data.ca = CA(data.rightXP, 800)
    data.kozPlay = False

def initKozPlay(data):
    initPlay(data)
    data.kozPlay = True
    data.kosbie = Kosbie(data.leftXP, 50)
    data.score = 1000
    data.doingTP = False

def initGameOver(data):
    data.Iconx1, data.Icony1 = data.width-80, 100
    data.Iconx2, data.Icony2 = data.width-80, 200
    data.Iconx3, data.Icony3 = data.width-80, 300
    data.Iconx4, data.Icony4 = data.width-80, 400

def initKozFail(data):
    data.x1, data.y1 = 120, data.height - 200
    data.x2, data.y2 = 240, data.height - 200
    data.x3, data.y3 = 360, data.height - 200
    data.x4, data.y4 = 480, data.height - 200

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "welcomeScreen"):  welcomeScreenMousePressed(event, data)
    elif (data.mode == "title"):        titleMousePressed(event, data)
    elif (data.mode == "introduction"): introductionMousePressed(event, data)
    elif (data.mode == "background"):   backgroundMousePressed(event, data)
    elif (data.mode == "playGame"):     playGameMousePressed(event, data)
    elif (data.mode == "gameModeSelect"): gameModeSelectMousePressed(event,data)
    elif (data.mode == "tutorial"):     tutorialMousePressed(event, data)
    elif (data.mode == "gameOver"):     gameOverMousePressed(event, data)
    elif (data.mode == "kozFail"):      kozFailMousePressed(event, data)    

def keyPressed(event, data):
    if (data.mode == "welcomeScreen"):  welcomeScreenKeyPressed(event, data)
    elif (data.mode == "title"):        titleKeyPressed(event, data)
    elif (data.mode == "introduction"): introductionKeyPressed(event, data)
    elif (data.mode == "background"):   backgroundKeyPressed(event, data)
    elif (data.mode == "playGame"):     playGameKeyPressed(event, data)
    elif (data.mode == "gameModeSelect"): gameModeSelectKeyPressed(event, data)
    elif (data.mode == "tutorial"):     tutorialKeyPressed(event, data)
    elif (data.mode == "gameOver"):     gameOverKeyPressed(event, data)
    elif (data.mode == "kozFail"):      kozFailKeyPressed(event, data)

def mouseMoved(event, data):
    if (data.mode == "welcomeScreen"): welcomeScreenMouseMoved(event, data)
    elif (data.mode == "title"):       titleMouseMoved(event, data)
    elif (data.mode == "introduction"): introductionMouseMoved(event, data)
    elif (data.mode == "background"): backgroundMouseMoved(event, data)
    elif (data.mode == "playGame"):   playGameMouseMoved(event, data)
    elif (data.mode == "gameModeSelect"): gameModeSelectMouseMoved(event, data)
    elif (data.mode == "tutorial"):   tutorialMouseMoved(event, data)
    elif (data.mode == "gameOver"):   gameOverMouseMoved(event, data)
    elif (data.mode == "kozFail"):    kozFailMouseMoved(event, data)

def timerFired(data):
    if (data.mode == "welcomeScreen"): welcomeScreenTimerFired(data)
    elif (data.mode == "title"):      titleTimerFired(data)
    elif (data.mode == "introduction"): introductionTimerFired(data)
    elif (data.mode == "background"): backgroundTimerFired(data)
    elif (data.mode == "playGame"):   playGameTimerFired(data)
    elif (data.mode == "gameModeSelect"): gameModeSelectTimerFired(data)
    elif (data.mode == "tutorial"):       tutorialTimerFired(data)
    elif (data.mode == "gameOver"):   gameOverTimerFired(data)
    elif (data.mode == "kozFail"):    kozFailTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "welcomeScreen"): welcomeScreenRedrawAll(canvas, data)
    elif (data.mode == "title"):       titleRedrawAll(canvas, data)
    elif (data.mode == "introduction"): introductionRedrawAll(canvas, data)
    elif (data.mode == "background"):  backgroundRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)
    elif (data.mode == "gameModeSelect"): gameModeSelectRedrawAll(canvas, data)
    elif (data.mode == "tutorial"):       tutorialRedrawAll(canvas, data)
    elif (data.mode == "gameOver"):   gameOverRedrawAll(canvas, data)
    elif (data.mode == "kozFail"):    kozFailRedrawAll(canvas, data)

####################################
# welcomeScreen mode
####################################

def welcomeScreenMousePressed(event, data):
    x0, y0 = data.x0 - 30, data.y0 + 70
    x1, y1 = data.x0 + 30, data.y0 + 130
    if data.loading:
        return
    elif (x0 < event.x < x1 and y0 < event.y < y1):
        data.mode = "title"
        initTitle(data)

def welcomeScreenMouseMoved(event, data):
    x0, y0 = data.x0 - 30, data.y0 + 70
    x1, y1 = data.x0 + 30, data.y0 + 130
    if (x0 < event.x < x1 and y0 < event.y < y1):
        data.clickInCircle = True
    else:
        data.clickInCircle = False

def welcomeScreenKeyPressed(event, data):
    pass

def welcomeScreenTimerFired(data):
    data.count += 1
    if data.count > 10:
        data.loading = False

def welcomeScreenRedrawAll(canvas, data):
    data.bg0 = PhotoImage(file = "bg0.gif")
    data.x0 = data.width/2
    data.y0 = data.height/2
    logoY = 200
    textY = data.y0 + 50
    iconY = data.y0 + 100
    canvas.create_image(data.x0, data.y0, image = data.bg0)
    data.logo = PhotoImage(file = "logo.gif")
    canvas.create_image(data.x0, logoY, image = data.logo)
    canvas.create_image
    if data.count <= 10:
        canvas.create_text(data.x0, textY, text = "Loading...", 
                           font = "herculanum 30", fill = "orange")
    else:
        canvas.create_text(data.x0, textY, text = "Click here to start!", 
                           font = "herculanum 30", fill = "orange")
        if data.clickInCircle:
            data.item0 = PhotoImage(file = "item00.gif")
        else:
            data.item0 = PhotoImage(file = "item0.gif")
        canvas.create_image(data.x0, iconY, image = data.item0)

####################################
# title mode
####################################

def titleMousePressed(event, data):
    if ((data.x1 - event.x)**2 + (data.y11 - event.y)**2)**0.5 <= data.item1R:
        data.mode = "introduction"
        initIntroduction(data)

def titleMouseMoved(event, data):
    if ((data.x1 - event.x)**2 + (data.y11 - event.y)**2)**0.5 <= data.item1R:
        data.clickInCircle = True
    else:
        data.clickInCircle = False

def titleKeyPressed(event, data):
    pass

def titleTimerFired(data):
    pass

def titleRedrawAll(canvas, data):
    data.bg1 = PhotoImage(file = "bg1.gif")
    data.x1 = data.width/2
    data.y1 = data.height/2
    data.y11 = data.y1 + 200
    canvas.create_image(data.x1,data.y1, image = data.bg1)
    if data.clickInCircle == True:
        data.item1 = PhotoImage(file = "item11.gif")
    else:
        data.item1 = PhotoImage(file = "item1.gif")
    canvas.create_image(data.x1,data.y11, image = data.item1)

####################################
# introduction mode
####################################

def introductionMousePressed(event, data):
    if ((data.x2 - event.x)**2 + (data.y21 - event.y)**2)**0.5 <= data.item2R:
        data.mode = "background"
        initBackground(data)

def introductionMouseMoved(event, data):
    if ((data.x2 - event.x)**2 + (data.y21 - event.y)**2)**0.5 <= data.item2R:
        data.clickInCircle = True
    else:
        data.clickInCircle = False

def introductionKeyPressed(event, data):
    pass

def introductionTimerFired(data):
    data.countIntro += 1

def introductionRedrawAll(canvas, data):
    data.bg2 = PhotoImage(file = "bg2.gif")
    data.x2 = data.width/2
    data.y2 = data.height/2
    data.y21 = data.y2 + 200
    canvas.create_image(data.x2,data.y2,image = data.bg2)
    if data.clickInCircle == True:
        data.item2 = PhotoImage(file = "item11.gif")
    else:
        data.item2 = PhotoImage(file = "item1.gif")
    canvas.create_image(data.x1,data.y21,image = data.item2)
    introDrawText(canvas, data)

def introDrawText(canvas,data):
    textX, textY1, textY2, textY3 = 340, 150, 200, 250
    time1, time2, time3 = 5, 15, 25
    if data.countIntro <= time1:
        canvas.create_text(textX, textY1, text = "John had planned to",
                            fill = "red", font= "herculanum 25")
        canvas.create_text(textX, textY2, text = "travel out", 
                            fill = "red", font= "herculanum 25")
        canvas.create_text(textX, textY3, text = "during Thanksgiving.", 
                            fill = "red", font= "herculanum 25")
    elif data.countIntro <= time2:
        canvas.create_text(textX, textY1, text = "Alas!",
                            fill = "red", font= "herculanum 25")
        canvas.create_text(textX, textY2, text = "He receives a call", 
                            fill = "red", font= "herculanum 25")
        canvas.create_text(textX, textY3, text = "from his CA.", 
                            fill = "red", font= "herculanum 25")
    elif data.countIntro <= time3:
        canvas.create_text(textX, textY1, text = "He is required",
                            fill = "red", font= "herculanum 25")
        canvas.create_text(textX, textY2, text = "to stay to finish", 
                            fill = "red", font= "herculanum 25")
        canvas.create_text(textX, textY3, text = "the term project.", 
                            fill = "red", font= "herculanum 25")
    else:
        canvas.create_text(textX, textY1, text = "John puts the",
                            fill = "red", font= "herculanum 25")
        canvas.create_text(textX, textY2, text = "phone down and", 
                            fill = "red", font= "herculanum 25")
        canvas.create_text(textX, textY3, text = "starts escaping!", 
                            fill = "red", font= "herculanum 25")

####################################
# background mode
####################################

def backgroundMousePressed(event, data):
    if ((data.x31-event.x)**2 + (data.y31-event.y)**2)**0.5 <= data.item3R:
        data.mode = "gameModeSelect"
        initGameModeSelect(data)

def backgroundMouseMoved(event, data):
    if ((data.x31-event.x)**2 + (data.y31-event.y)**2)**0.5 <= data.item3R:
        data.click = True
    else:
        data.click = False

def backgroundKeyPressed(event, data):
    pass

def backgroundTimerFired(data):
    data.countStep += 1
    # rolling play of the background picture
    data.x3 -= 100
    if data.x3 == - data.width/2:
        data.x3 = data.width/2

def backgroundRedrawAll(canvas, data):
    data.bg3 = PhotoImage(file = "bg3.gif")
    canvas.create_image(data.x3,data.y3,image = data.bg3)
    canvas.create_image(data.x3+data.width,data.y3, image = data.bg3)
    if data.click == True:
        data.item3 = PhotoImage(file = "item11.gif")
    else:
        data.item3 = PhotoImage(file = "item1.gif")
    canvas.create_image(data.x31,data.y31,image = data.item3)
    backgroundDrawPlayer(canvas, data)
    backgroundDrawCA(canvas, data)
    data.talk1 = PhotoImage(file = "talk1.gif")
    data.talk2 = PhotoImage(file = "talk2.gif")
    talk1X, talk1Y = data.width/2-150, data.y3-150
    talk2X, talk2Y = data.width/2+100, data.y3-150
    canvas.create_image(talk1X, talk1Y, image = data.talk1)
    canvas.create_image(talk2X, talk2Y, image = data.talk2)

def backgroundDrawPlayer(canvas, data):
    xP = data.width - 150
    yP = data.height - 300
    steps = 3
    data.runPlayer1 = PhotoImage(file = "runPlayer1.gif")
    data.runPlayer2 = PhotoImage(file = "runPlayer2.gif")
    data.runPlayer3 = PhotoImage(file = "runPlayer3.gif")
    if data.countStep % steps == 0:
        canvas.create_image(xP, yP, image = data.runPlayer1)
    elif data.countStep % steps == 1:
        canvas.create_image(xP, yP, image = data.runPlayer2)
    elif data.countStep % steps == 2:
        canvas.create_image(xP, yP, image = data.runPlayer3)

def backgroundDrawCA(canvas, data):
    xCA = 200
    yCA = data.height - 300
    steps = 3
    data.runCA1 = PhotoImage(file = "runCA1.gif")
    data.runCA2 = PhotoImage(file = "runCA2.gif")
    data.runCA3 = PhotoImage(file = "runCA3.gif")
    if data.countStep % steps == 0:
        canvas.create_image(xCA, yCA, image = data.runCA1)
    elif data.countStep % steps == 1:
        canvas.create_image(xCA, yCA, image = data.runCA2)
    elif data.countStep % steps == 2:
        canvas.create_image(xCA, yCA, image = data.runCA3)

####################################
# gameModeSelect mode
####################################

def gameModeSelectMousePressed(event, data):
    itemSize = 160
    x0, y0 = 300, 250
    x1, y1 = 300, 500
    if (x0<event.x < (x0+itemSize)) and (y0<event.y<(y0+itemSize)):
        data.mode = "tutorial"
        initTutorial(data)
        data.kozPlay = False
    elif (x1<event.x < (x1+itemSize)) and (y1<event.y<(y1+itemSize)):
        data.mode = "tutorial"
        initTutorial(data)
        data.kozPlay = True

def gameModeSelectKeyPressed(event, data):
    pass

def gameModeSelectMouseMoved(event, data):
    pass

def gameModeSelectTimerFired(data):
    pass

def gameModeSelectRedrawAll(canvas, data):
    textX = 150
    texY1, textY2 = 350, 580
    data.background = PhotoImage(file = "modeSelect.gif")
    canvas.create_image(data.cx, data.cy, image = data.background)
    studentModeScore = readFile("highestScore.txt")
    kosbieModeScore = readFile("highestScore1.txt")
    canvas.create_text(textX, texY1, text = "HighScore: " + studentModeScore,
                        fill = "coral", font = "chalkboard 30")
    canvas.create_text(textX, textY2, text = "HighScore: " + kosbieModeScore,
                        fill = "coral", font = "chalkboard 30")

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

####################################
# tutorial mode
####################################

def tutorialMousePressed(event, data):
    if ((data.x41-event.x)**2 + (data.y41-event.y)**2)**0.5 <= data.item4R:
        data.mode = "playGame"
        if data.kozPlay == True:
            initKozPlay(data)
        else:
            initPlay(data)
    elif ((data.x42-event.x)**2 + (data.y42-event.y)**2)**0.5 <= data.item4R:
        data.mode = "gameModeSelect"
        initGameModeSelect(data)

def tutorialKeyPressed(event, data):
    pass

def tutorialMouseMoved(event, data):
    if ((data.x41-event.x)**2 + (data.y41-event.y)**2)**0.5 <= data.item4R:
        data.clickInCircle = True
    else:
        data.clickInCircle = False

def tutorialTimerFired(data):
    data.countFlash += 1

def tutorialRedrawAll(canvas, data):
    if data.kozPlay == True:
        data.bg4 = PhotoImage(file = "bg41.gif")
    else:
        data.bg4 = PhotoImage(file = "bg4.gif")
    data.leftArrow = PhotoImage(file = "leftArrow.gif")
    data.rightArrow = PhotoImage(file = "rightArrow.gif")
    canvas.create_image(data.x4,data.y4,image = data.bg4)
    if data.clickInCircle == True:
        data.item4 = PhotoImage(file = "item11.gif")
    else:
        data.item4 = PhotoImage(file = "item1.gif")
    canvas.create_image(data.x41,data.y41,image = data.item4)
    data.returnItem = PhotoImage(file = "return.gif")
    canvas.create_image(data.x42, data.y42, image = data.returnItem)
    # draw flashing arrow keys
    if data.countFlash % 2 == 0:
        canvas.create_image(data.xLeft, data.yDown, image = data.leftArrow)
        canvas.create_image(data.xRight, data.yUp, image = data.rightArrow)
    else:
        canvas.create_image(data.xLeft, data.yUp, image = data.leftArrow)
        canvas.create_image(data.xRight, data.yDown, image = data.rightArrow)

####################################
# playGame mode
####################################

class Project(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.R = 20
        self.name = "Project"

    def collideWithPlayer(self, x, y, r, data):
        if data.caught == False:
            d = ((self.x - x)**2 + (self.y - y)**2)**0.5
            return (d <= (self.R + r))

    def draw(self, canvas):
        self.picture = PhotoImage(file = "tp.gif")
        canvas.create_image(self.x, self.y, image = self.picture)

    def move(self, data):
        # when palyer climbs up, barriers actually move down
        self.y += data.barrierSpace
        # move down the background picture
        data.bgY += 10
        if data.bgY >= data.height:
            data.bgY = 0
            data.inTheSky = True

    def onTimerFired(self, data):
        pass

class Homework(Project):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "HW"
        self.count = 0

    def draw(self, canvas):
        self.picture = PhotoImage(file = "computer1.gif")
        canvas.create_image(self.x, self.y, image = self.picture)

class Quiz(Project):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Quiz"

    def draw(self, canvas):
        self.picture = PhotoImage(file = "quiz2.gif")
        canvas.create_image(self.x, self.y, image = self.picture)

class Coin(Project):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Coin"
        self.count = 0
        self.isCollide = False

    def onTimerFired(self, data):
        self.count += 1
        if self.isCollide == True:
            self.x = data.width/2
            self.y -= 120
            # remove the coin when the player collects it
            if self.y < 10 or data.flyWithBalloon:
                data.barriersOnCanvas.remove(self)

    def draw(self, canvas):
        # make coins turn around
        frames = 5
        frame0, frame1, frame2, frame3, frame4 = 0, 1, 2, 3, 4
        if self.isCollide == True:
            self.picture = PhotoImage(file = "coin.gif")
            canvas.create_image(self.x, self.y, image = self.picture)
        else:    
            if self.count % frames == frame0:
                self.picture = PhotoImage(file = "coin.gif")
                canvas.create_image(self.x, self.y, image = self.picture)
            elif self.count % frames == frame1:
                self.picture1 = PhotoImage(file = "coin1.gif")
                canvas.create_image(self.x, self.y, image = self.picture1)
            elif self.count % frames == frame2:
                self.picture2 = PhotoImage(file = "coin2.gif")
                canvas.create_image(self.x, self.y, image = self.picture2)
            elif self.count % frames == frame3:
                self.picture3 = PhotoImage(file = "coin3.gif")
                canvas.create_image(self.x, self.y, image = self.picture3)
            elif self.count % frames == frame4:
                self.picture4 = PhotoImage(file = "coin4.gif")
                canvas.create_image(self.x, self.y, image = self.picture4)

class SilverStar(Project):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "silverStar"
        self.isCollide = False

    def onTimerFired(self, data):
        if self.isCollide == True:
            self.x = data.width/2
            self.y -= 120
            # remove the star when the player collects it
            if self.y < 10 or data.flyWithBalloon:
                data.barriersOnCanvas.remove(self)

    def draw(self, canvas):
        self.picture = PhotoImage(file = "silverStar.gif")
        canvas.create_image(self.x, self.y, image = self.picture)

class GoldStar(Project):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "goldStar"
        self.isCollide = False

    def onTimerFired(self, data):
        if self.isCollide == True:
            self.x = data.width/2
            self.y -= 120
            # remove the star when the player collects it
            if self.y < 10 or data.flyWithBalloon:
                data.barriersOnCanvas.remove(self)

    def draw(self, canvas):
        self.picture = PhotoImage(file = "goldStar.gif")
        canvas.create_image(self.x, self.y, image = self.picture)

class Balloon(Project):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Balloon"

    def draw(self, canvas):
        self.picture = PhotoImage(file = "balloon.gif")
        canvas.create_image(self.x, self.y, image = self.picture)

class Player(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.R = 30
        self.name = "Player"
        self.count = 0            

    def draw(self, data, canvas):
        self.drawPlayer(data, canvas)
        steps = 5
        textX, textY = 100, data.topY-20
        countDownX, countDownY = 100, data.topY+20
        # draw the effects that player collides with homework
        if data.doingHW == True:
            canvas.create_text(textX, textY, text = "Count down:", 
                               font = "chalkboard 30", fill = "red")
            HWCountDown = 3
            data.text = str(HWCountDown - self.count // steps)
            canvas.create_text(countDownX, countDownY, font = "chalkboard 40",
                               text = data.text, fill = "red")
        # draw the effects that player collides with quiz
        elif data.doingQuiz == True:
            canvas.create_text(textX, textY, text = "Count down:", 
                               font = "chalkboard 30", fill = "red")
            QuizCountDown = 1
            data.text = str(QuizCountDown - self.count // steps)
            canvas.create_text(countDownX, countDownY, font = "chalkboard 40",
                               text = data.text, fill = "red")
        # draw the effects that player collides with TP
        elif data.doingTP == True:
            canvas.create_text(textX, textY, text = "Count down:", 
                               font = "chalkboard 30", fill = "red")
            TPCountDown = 5
            data.text = str(TPCountDown - self.count // steps)
            canvas.create_text(countDownX, countDownY, font = "chalkboard 40",
                               text = data.text, fill = "red")
        # draw the effects that player grabs a balloon
        elif data.flyWithBalloon == True:
            # draw plying palyer with balloon
            self.drawPlayerWithBalloon(data, canvas)

    def drawPlayer(self, data, canvas):
        if data.gameOver == True:
            self.picture = PhotoImage(file = "fallingPlayer.gif")
            canvas.create_image(self.x, self.y, image = self.picture)
            return 
        if data.left == True:
            if data.kozPlay == True:
                self.picture = PhotoImage(file = "climbKoz.gif")
            else:
                #change player's color when he collides with HW or Quiz
                if data.doingHW or data.doingQuiz:
                    self.picture = PhotoImage(file = "climbPlayerLeft1.gif")
                else:
                    self.picture = PhotoImage(file = "climbPlayerLeft.gif")
            canvas.create_image(self.x, self.y, image = self.picture)
        else:
            if data.kozPlay == True:
                self.picture = PhotoImage(file = "climbKozRight.gif")
            else:
                #change player's color when he collides with HW or Quiz
                if data.doingHW or data.doingQuiz:
                    self.picture = PhotoImage(file = "climbPlayerRight1.gif")
                else:
                    self.picture = PhotoImage(file = "climbPlayerRight.gif")
            canvas.create_image(self.x, self.y, image = self.picture)

    def drawPlayerWithBalloon(self, data, canvas):
        # draw the flying image of the player
        if data.kozPlay == True:
            self.picture = PhotoImage(file = "flyKoz.gif")
            kozX, kozY = self.x - 45, self.y - 70
            canvas.create_image(kozX, kozY, image = self.picture)    
        else:
            self.picture = PhotoImage(file = "flyPlayer.gif")
            playerX, playerY = self.x + 20 , self.y
            canvas.create_image(playerX, playerY, image = self.picture)    
        self.balloon = PhotoImage(file = "balloon.gif")
        balloonX, balloonY = self.x, self.y - 200
        canvas.create_image(balloonX, balloonY, image = self.balloon)
        lineX0, lineY0 = self.x , self.y-90
        lineX1, lineY1 = self.x, self.y-160
        canvas.create_line(lineX0, lineY0, lineX1, lineY1, width=2,
                             fill = "white")

    def onTimerFired(self, data):
        fallSpeed = 30
        if data.caught == True:
            self.y += fallSpeed
        elif data.gameOver == True:
            self.y += fallSpeed
            if data.left: 
                self.x = data.leftX
            else:
                self.x = data.rightX
        elif data.doingHW == True:
            self.HWTimerFired(data)
        elif data.doingQuiz == True:
            self.QuizTimerFired(data)
        elif data.doingTP == True:
            self.TPTimerFired(data)

    def HWTimerFired(self, data):
        self.count += 1
        detentionTime = 20
        if self.count == detentionTime:
            self.count = 0
            data.doingHW = False
            data.barriersOnCanvas.remove(data.currStuckBarrier)
            data.currStuckBarrier = None

    def QuizTimerFired(self, data):
        self.count += 1
        detentionTime = 10
        if self.count == detentionTime:
            self.count = 0
            data.doingQuiz = False
            data.barriersOnCanvas.remove(data.currStuckBarrier)
            data.currStuckBarrier = None

    def TPTimerFired(self, data):
        self.count += 1
        detentionTime = 30
        if self.count == detentionTime:
            self.count = 0
            data.doingTP = False
            data.barriersOnCanvas.remove(data.currStuckBarrier)
            data.currStuckBarrier = None

    def climbUp(self, data):
        speed = 100
        self.y -= speed
        chasingSpeed = 20
        if data.kozPlay == True:
            data.kosbie.y += speed
        else:
            data.kosbie.y += chasingSpeed
            data.ca.y += chasingSpeed
            # scroll to make player in the middle of the canvas
        if (self.y < data.topY):
            self.y = data.topY
            for barrier in data.barriersOnCanvas:
                barrier.move(data)
        if data.left == True:
            self.x = data.leftXP
        else:
            self.x = data.rightXP

class Kosbie(Player):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Kos"
        self.speed1 = 10
        self.speed2 = 15
        self.count = 0

    def draw(self, data, canvas):
        if data.kozPlay == True:
            if self.x < data.width/2:
                self.picture = PhotoImage(file = "climbPlayerLeft.gif")
            else:
                self.picture = PhotoImage(file = "climbPlayerRight.gif")
        else:
            self.picture = PhotoImage(file = "climbKoz.gif")
        canvas.create_image(self.x, self.y, image = self.picture)

    def moveUp(self, data):
        # for kozPlay mode: the student climbs up 
        # and could avoid barriers automatically
        losePoint = 20
        speed = 100
        if self.count % 2 == 0:
            self.y -= speed
            data.score -= losePoint
            for barrier in data.barriersOnCanvas:
                if (barrier.y == self.y):
                    if (barrier.name == "Balloon" or barrier.name == "goldStar"
                        or barrier.name == "silverStar" or
                        barrier.name == "Coin" or  barrier == None):
                        if barrier.x < data.width/2:
                            self.x = data.leftXP
                        else:
                            self.x = data.rightXP
                        break

    def onTimerFired(self, data):
        fallSpeed = 30
        climbSpeed = 100
        self.count += 1
        if data.caught == True:
                self.y += fallSpeed      
        elif data.kozPlay == True:
            if data.flyWithBalloon == True:
                self.y += climbSpeed
            else:
                self.moveUp(data)
        
        else:
            if data.flyWithBalloon == True:
                self.y += fallSpeed
                # to ensure kosbie and CA not falls behind too far away
                if self.y >= data.height:
                    self.y = data.height
            else:
                speedChangeSteps = 5
                if self.count // speedChangeSteps % 2 == 0:
                    self.y -= self.speed1
                else:
                    self.y -= self.speed2

    def catchPlayer(self, x, y, r):
        # to check collision
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return (d <= (self.R + r))

class CA(Player):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "CA"
        self.speed1 = 10
        self.speed2 = 15
        self.count = 0

    def draw(self, data, canvas):
        if data.kozPlay == True:
            pass
        else:
            self.picture = PhotoImage(file = "climbCA.gif")
            canvas.create_image(self.x, self.y, image = self.picture)

    def onTimerFired(self, data):
        fallSpeed = 30
        speedChangeSteps = 5
        if data.kozPlay == True:
            pass
        else:
            self.count += 1
            if data.caught == True:
                self.y += fallSpeed
            elif data.flyWithBalloon == True:
                self.y += fallSpeed
                if self.y >= data.height:
                    self.y = data.height
            else:
                if self.count // speedChangeSteps % 2 == 1:
                    self.y -= self.speed1
                else:
                    self.y -= self.speed2

    def catchPlayer(self, x, y, r):
        # to check collision
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return (d <= (self.R + r))   

def playGameMousePressed(event, data):
    buttonY = 50
    IconSpace = 100
    iconR = 30
    if data.isPaused == False:
        if ((data.cx - event.x)**2 + (buttonY - event.y)**2)**0.5 < iconR:
            data.isPaused = True
    else:
        if ((data.cx-IconSpace-event.x)**2 + (data.cy-event.y)**2)**0.5<iconR:
            data.isPaused = False
        elif ((data.cx - event.x)**2 + (data.cy - event.y)**2)**0.5 < iconR:
            data.mode == "tutorial"
            initTutorial(data)
            if data.kozPlay == True:
                data.kozPlay = True
        elif ((data.cx+IconSpace-event.x)**2+(data.cy-event.y)**2)**0.5<iconR:
            data.mode == "welcomeScreen"
            init(data)
        elif ((data.cx-event.x)**2 + (data.cy+100-event.y)**2)**0.5<iconR:
            data.mode = "gameModeSelect"
            initGameModeSelect(data)

def playGameKeyPressed(event, data):
    if data.isPaused:
        return
    if data.flyWithBalloon:
        return
    if data.gameOver:
        return
    if data.caught:
        return
    if data.doingHW:
        return
    if data.doingQuiz:
        return
    if data.doingTP:
        return
    if (event.keysym == "Left"):
        data.left = True
        data.steps += 1
        data.score += 1
        data.player.climbUp(data)
        if data.player.y == data.topY:
            randomAddBarrier(data)    
    elif (event.keysym == "Right"):
        data.left = False
        data.steps += 1
        data.score += 1
        data.player.climbUp(data)
        if data.player.y == data.topY:
            randomAddBarrier(data)

def randomAddBarrier(data):
    # randomly add new barrier on the top of the canvas
    barrierToBeAdd = random.choice(data.barriers)
    initX1 = random.choice([data.leftX, data.rightX])
    balloonRepeatDist, goldStarRepeatDist, silverStarRepeatDist = 40, 30, 15
    if data.steps % balloonRepeatDist == 0:
        data.barriersOnCanvas.append(Balloon(initX1, data.initY))
    elif data.steps % goldStarRepeatDist == 0:
        data.barriersOnCanvas.append(GoldStar(initX1, data.initY))
    elif data.steps % silverStarRepeatDist == 0:
        data.barriersOnCanvas.append(SilverStar(initX1, data.initY))
    elif barrierToBeAdd == "Project":
        data.barriersOnCanvas.append(Project(initX1, data.initY))
    elif barrierToBeAdd == "HW":
        data.barriersOnCanvas.append(Homework(initX1, data.initY))
    elif barrierToBeAdd == "Quiz":
        data.barriersOnCanvas.append(Quiz(initX1, data.initY))
    if initX1 == data.leftX:
        initX2 = data.rightX
    else:
        initX2 = data.leftX
    if (data.barriersOnCanvas[-1].name != "silverStar" and 
        data.barriersOnCanvas[-1].name != "goldStar"):
        data.barriersOnCanvas.append(Coin(initX2, data.initY))

def playGameMouseMoved(event, data):
    pass

def playGameTimerFired(data):
    if data.kozPlay == True:
        if data.score <= 0:
            data.score = 0
            data.mode = "kozFail"
            initKozFail(data)
        if data.flyWithBalloon == True:
            if data.kosbie.y == data.player.y and data.score > 0:
                data.flyWithBalloon = False
                data.caught = True
    if data.isPaused == False:
        for barrier in data.barriersOnCanvas:
            barrier.onTimerFired(data)
            if barrier.y > data.height:
                data.barriersOnCanvas.remove(barrier)
            if data.flyWithBalloon:
                flyPointSystem(data, barrier)
        # move barriers on board
        if data.flyWithBalloon == True:
            # add barrier at flying and also add extra point during flying
            addAndMoveBarriersDuringFlying(data)
        else:
            climbPointSystem(data)

        playerCaughtByKosOrCA(data) 
        data.kosbie.onTimerFired(data)      
        data.player.onTimerFired(data)
        if data.kozPlay != True:
            data.ca.onTimerFired(data)
    # To decide if the game is over
    # write the results into IO
    if data.player.y >= data.height:
        recordScore(data)
        data.mode = "gameOver"
        initGameOver(data)

def addAndMoveBarriersDuringFlying(data):
    # add barrier at flying and also add extra point during flying
    landPosition = 16
    flyDistance = 20
    for barrier in data.barriersOnCanvas:
        barrier.move(data)   
    data.flyCount += 1
    if data.flyCount != landPosition: 
        randomAddBarrier(data)
    if data.flyCount == flyDistance:
        data.score += flyDistance
        data.flyCount = 0
        data.flyWithBalloon = False

def recordScore(data):
    # write current score into txt documents and also compare the score with
    # the highest
    currScore = data.score
    writeFile("currScore.txt", str(currScore))
    currCoins = data.coins
    writeFile("currCoins.txt", str(currCoins))
    if data.kozPlay == True:
        data.highestScore1 = int(readFile("highestScore1.txt"))
        if currScore > data.highestScore1:
            writeFile("highestScore1.txt", str(currScore))
    else:
        data.highestScore = int(readFile("highestScore.txt"))
        if currScore > data.highestScore:
            writeFile("highestScore.txt", str(currScore))

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def flyPointSystem(data, barrier):
    # this function is to calculate points during the player is flying with 
    # balloon and also collect all the bonus along the way
    if (barrier.name == "Coin" and barrier.y == data.topY):
        data.barriersOnCanvas.remove(barrier)
        data.coins += data.coinPoint
        data.score += data.coinPoint
    if (barrier.name == "goldStar" and barrier.y == data.topY):
        data.barriersOnCanvas.remove(barrier)
        data.coins += data.goldStarPoint
        data.score += data.goldStarPoint
    if (barrier.name == "silverStar"  and barrier.y == data.topY):
        data.barriersOnCanvas.remove(barrier)
        data.coins += data.silverStarPoint
        data.score += data.silverStarPoint

def climbPointSystem(data):
    # this function is used to record score under different conditions
    if data.gameOver: return
    for barrier in data.barriersOnCanvas:
        if barrier.collideWithPlayer(data.player.x,data.player.y,
                                     data.player.R,data):
            barrier.isCollide = True
            if barrier.name == "Coin":
                data.coins += data.coinPoint
                data.score += data.coinPoint
            elif barrier.name == "Balloon":
                data.flyWithBalloon = True
                data.barriersOnCanvas.remove(barrier)
            elif barrier.name == "silverStar":
                data.coins += data.silverStarPoint
                data.score += data.silverStarPoint
            elif barrier.name == "goldStar":
                data.coins += data.goldStarPoint
                data.score += data.goldStarPoint
            elif barrier.name == "Project":
                if data.kozPlay == True:
                    data.doingTP = True
                    data.currStuckBarrier = barrier
                else:
                    data.gameOver = True
            elif barrier.name == "HW":
                data.doingHW = True
                data.currStuckBarrier = barrier
            elif barrier.name == "Quiz":
                data.doingQuiz = True
                data.currStuckBarrier = barrier

def playerCaughtByKosOrCA(data):
    # to check if the player is caught by hunters
    x = data.player.x
    y = data.player.y
    r = data.player.R
    if data.kosbie.catchPlayer(x, y, r) or data.ca.catchPlayer(x, y, r):
        data.caught = True
        data.flyWithBalloon = False

def playGameRedrawAll(canvas, data):
    WarningX, WarningY = data.width-100, 100
    WarningScore = 100
    if data.isPaused:
        drawPause(canvas, data)
    else:
        drawPlayBackground(canvas, data)
        drawPlayIcons(canvas, data)
        if data.kozPlay == True:
            if data.score <= WarningScore:
                canvas.create_text(WarningX, WarningY, text = "Warning!", 
                           fill = "red", font= "Phosphate 30")
        for barrier in data.barriersOnCanvas:
            barrier.draw(canvas)     
        data.player.draw(data, canvas)
        data.kosbie.draw(data, canvas)
        data.ca.draw(data, canvas)

def drawPlayBackground(canvas, data):
    # draw the background canvas of the games, move down the canvas when the
    # player climbs up
    if data.kozPlay == True:
        if data.inTheSky == True:
            data.background = PhotoImage(file = "bgsky1.gif")
        else:
            data.background = PhotoImage(file = "bg7.gif")
        data.bgsky = PhotoImage(file = "bgsky1.gif")
    else:
        if data.inTheSky == True:
            data.background = PhotoImage(file = "bgsky.gif")
        else:
            data.background = PhotoImage(file = "bg.gif")
        data.bgsky = PhotoImage(file = "bgsky.gif")
    canvas.create_image(data.bgX, data.bgY, anchor=NW, 
                        image = data.background)
    canvas.create_image(data.bgX, data.bgY-data.height, anchor=NW,
                        image = data.bgsky)

def drawPlayIcons(canvas, data):
    # draw the ladder in the middle
    lineWidth = 6
    canvas.create_rectangle(data.cx, 0, data.cx+lineWidth,
                            data.height, fill = "black")
    # draw icons on this canvas
    data.coinScoreIm = PhotoImage(file = "coinScore.gif")
    data.pauseIm = PhotoImage(file = "pause.gif")
    data.scoreIm = PhotoImage(file = "score.gif")
    margin = 50
    canvas.create_image(margin,margin,image = data.coinScoreIm)
    canvas.create_image(data.cx, margin, image = data.pauseIm)
    canvas.create_image(data.width-margin, margin, image = data.scoreIm)
    textMargin = 120
    canvas.create_text(textMargin, margin, text = "%d" %data.coins, 
                       fill = "red", font= "Phosphate 30")
    canvas.create_text(data.width-textMargin, margin,text = "%d" %data.score, 
                       fill = "red", font= "Phosphate 30")

def drawPause(canvas, data):
    # draw pause interface 
    data.itemR = 30
    data.isPausedPic = PhotoImage(file = "bg5.gif")
    data.restart = PhotoImage(file = "restart.gif")
    data.help = PhotoImage(file = "help.gif")
    data.home = PhotoImage(file = "home.gif")
    data.returnItem = PhotoImage(file = "return.gif")
    restartX = data.cx-100
    homeX = data.cx+100
    returnY = data.cy+100
    canvas.create_image(data.cx, data.cy, image = data.isPausedPic)
    canvas.create_image(restartX, data.cy, image = data.restart)
    canvas.create_image(data.cx, data.cy, image = data.help)
    canvas.create_image(homeX, data.cy, image = data.home)
    canvas.create_image(data.cx, returnY, image = data.returnItem)

####################################
# gameOver mode
####################################

def gameOverMousePressed(event, data):
    iconR = 30
    if ((data.Iconx2 - event.x)**2 + (data.Icony2 - event.y)**2)**0.5 < iconR:
        data.mode = "playGame"
        if data.kozPlay == True:
            initKozPlay(data)
        else:
            initPlay(data)
    elif ((data.Iconx3 - event.x)**2 + (data.Icony3 - event.y)**2)**0.5 < iconR:
        data.mode == "tutorial"
        initTutorial(data)
    elif ((data.Iconx4 - event.x)**2 + (data.Icony4 - event.y)**2)**0.5 < iconR:
        data.mode == "welcomeScreen"
        init(data)
    elif ((data.Iconx1 - event.x)**2 + (data.Icony1 - event.y)**2)**0.5 < iconR:
        data.mode = "gameModeSelect"
        initGameModeSelect(data)

def gameOverMouseMoved(event, data):
    pass

def gameOverKeyPressed(event, data):
    pass

def gameOverTimerFired(data):
    pass

def gameOverRedrawAll(canvas, data):
    x1, y1 = data.cx+10, 208
    x2, y2 = data.cx+10, 317
    x3, y3 = data.cx+10, 420
    if data.kozPlay == True:
        data.bg6 = PhotoImage(file = "bg61.gif")
        highestScore = readFile("highestScore1.txt")
    else:
        data.bg6 = PhotoImage(file = "bg6.gif")
        highestScore = readFile("highestScore.txt")
    currScore = readFile("currScore.txt")
    currCoins = readFile("currCoins.txt")   
    canvas.create_image(data.cx, data.cy, image = data.bg6)
    canvas.create_text(x1, y1, text = currScore, 
                       font = "Phosphate 45", fill = "navy") 
    canvas.create_text(x2, y2, text = currCoins, 
                       font = "Phosphate 45", fill = "navy")
    canvas.create_text(x3, y3, text = highestScore, 
                       font = "Phosphate 45", fill = "red")
    data.restart = PhotoImage(file = "restart.gif")
    data.help = PhotoImage(file = "help.gif")
    data.home = PhotoImage(file = "home.gif")
    data.returnItem = PhotoImage(file = "return.gif")
    canvas.create_image(data.Iconx1, data.Icony1, image = data.returnItem)
    canvas.create_image(data.Iconx2, data.Icony2, image = data.restart)
    canvas.create_image(data.Iconx3, data.Icony3, image = data.help)
    canvas.create_image(data.Iconx4, data.Icony4, image = data.home)

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

####################################
# kozFail mode
####################################

def kozFailMousePressed(event, data):
    # click icons to switch interfaces
    iconR = 30
    if ((data.x1 - event.x)**2 + (data.y1 - event.y)**2)**0.5 < iconR:
        data.mode = "playGame"
        initKozPlay(data)
    elif ((data.x2 - event.x)**2 + (data.y2 - event.y)**2)**0.5 < iconR:
        data.mode = "gameModeSelect"
        initGameModeSelect(data)
    elif ((data.x3 - event.x)**2 + (data.y3 - event.y)**2)**0.5 < iconR:
        data.mode == "tutorial"
        initTutorial(data)
    elif ((data.x4 - event.x)**2 + (data.y4 - event.y)**2)**0.5 < iconR:
        data.mode == "welcomeScreen"
        init(data)

def kozFailMouseMoved(event, data):
    pass

def kozFailKeyPressed(event, data):
    pass

def kozFailTimerFired(data):
    pass

def kozFailRedrawAll(canvas, data):
    data.failbg = PhotoImage(file = "losebg.gif")
    canvas.create_image(data.cx, data.cy, image = data.failbg)
    data.restart = PhotoImage(file = "restart.gif")
    data.returnItem = PhotoImage(file = "return.gif")
    data.help = PhotoImage(file = "help.gif")
    data.home = PhotoImage(file = "home.gif")
    canvas.create_image(data.x1, data.y1, image = data.restart)
    canvas.create_image(data.x2, data.y2, image = data.returnItem)
    canvas.create_image(data.x3, data.y3, image = data.help)
    canvas.create_image(data.x4, data.y4, image = data.home)

####################################
# use the run function as-is
####################################

def run(width=600, height=800):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def mouseMovedWrapper(event, canvas, data):
        mouseMoved(event, data)
        #redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # create the root
    root = Tk()
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 80 # milliseconds
    init(data)
    # create the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Motion>", lambda event:
                            mouseMovedWrapper(event,canvas, data))
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data)) 
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 800)