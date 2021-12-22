#Import Modul
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Inisialisasi Posisi Box 1 dan Box 2
pos_x_box_1 = 0
pos_y_box_1 = 1
pos_x_box_2 = 0
pos_y_box_2 = 1

#Inisialisasi Posisi Bendera
pos_flag = [[2, 57], [-2, 57]]

#Inisialisasi Posisi Bom
pos_x_bom_1 = 0
pos_y_bom_1 = 1
pos_x_bom_2 = 0
pos_y_bom_2 = 1
pos_x_bom_3 = 0
pos_y_bom_3 = 1
pos_x_bom_4 = 0
pos_y_bom_4 = 1

#Inisialisasi Variabel Pendukung
motion = 2
game = False
win = False
loss = False
boleh_jalan = True

judul_game = "BRO AND MAX"
petunjuk_1 = "Tekan HOME untuk memulai permainan"
petunjuk_2 = "Tekan F1 untuk Pause, F2 untuk Resume"
petunjuk_3 = "Tekan END untuk Restart"
kalimat_win = "WIN. Selamat!"
kalimat_loss = "LOSS. Yahh:("

#Inisialisasi Posisi Gambar Box
#b1 = Box Kuning
#b2 = Box Biru
b1 = [-4, 0, -30, -26]
b2 = [0, 4, -27, -30]


#kt = List Koordinat Tembok
kt = [
    [-26, 26, -22, -26],
    [-30, -4, -14, -18],
    [4, 30, -14, -18],
    [-30, -18, -6, -10],
    [-14, 20, -6, -10],
    [24, 30, -6, -10],
    [-30, -14, 2, -2],
    [-10, 2, 2, -2],
    [6, 30, 2, -2],
    [-30, -6, 10, 6],
    [-2, 8, 10, 6],
    [12, 18, 10, 6],
    [22, 30, 10, 6],
    [-30, -24, 18, 14],
    [-20, -14, 18, 14],
    [-10, 14, 18, 14],
    [18, 30, 18, 14],
    [-30, -20, 26, 22],
    [-16, -10, 26, 22],
    [-6, 6, 26, 22],
    [10, 18, 26, 22],
    [22, 30, 26, 22]
]

#List untuk data perjalanan Box
log_path1 = [[0,1],[0,1]]
log_path = [[0,1],[0,1]]

#List untuk data perjalanan Bom
log_bom_1 = []
log_bom_2 = []
log_bom_3 = []
log_bom_4 = []

#List untuk jalan yang dapat diambil oleh Box 1
path_box_1 = [
    [0,1],[-2,1],[-4,1],[-6,1],[-8,1],[-10,1],[-12,1],[-14,1],[-16,1],[-18,1],[-20,1],[-22,1],[-24,1],[-26,1],
    [-26,3],[-26,5],[-26,7],[-26,9],[-24,9],[-22,9],[-20,9],[-18,9],[-16,9],[-14,9],[-12,9],[-10,9],[-8,9],[-6,9],
    [-4,9],[-2,9],[0,9],[0,11],[0,13],[0,15],[0,17],[-2,17],[-4,17],[-6,17],[-8,17],[-10,17],[-12,17],[-14,17],
    [-16,17],[-18,17],[-20,17],[-22,17],[-24,17],[-26,17],[-14,19],[-14,21],[-14,23],[-14,25],[-26,25],[-24,25],
    [-22,25],[-20,25],[-18,25],[-16,25],[-14,25],[-12,25],[-10,25],[-8,25],[-6,25],[-4,25],[-2,25],[0,25],[-10,27],
    [-10,29],[-10,31],[0,33],[-2,33],[-4,33],[-6,33],[-8,33],[-10,33],[-12,33],[-14,33],[-16,33],[-18,33],[-20,33],
    [-22,33],[-24,33],[-26,33],[-2,35],[-2,37],[-2,39],[-2,41],[0,41],[-4,41],[-6,41],[-8,41],[-10,41],[-12,41],
    [-14,41],[-16,41],[-18,41],[-20,41],[-22,41],[-24,41],[-26,41],[-20,43],[-20,45],[-20,47],[-20,49],[-10,43],
    [-10,45],[-10,47],[-10,49],[0,49],[-2,49],[-4,49],[-6,49],[-8,49],[-10,49],[-12,49],[-14,49],[-16,49],[-18,49],
    [-20,49],[-22,49],[-24,49],[-26,49],[-6,51],[-6,53],[-6,55],[-6,57],[-16,51],[-16,53],[-16,55],[-16,57],[0,57],
    [-2,57],[-4,57],[-6,57],[-8,57],[-10,57],[-12,57],[-14,57],[-16,57],[-18,57],[-20,57],[-22,57],[-24,57],[-26,57],[2,57]
]

#List untuk jalan yang dapat diambil Box 2
path_box_2 = [
    [0,1],[2,1],[4,1],[6,1],[8,1],[10,1],[12,1],[14,1],[16,1],[18,1],[20,1],[22,1],[24,1],[26,1],
    [26,3],[26,5],[26,7],[26,9],[24,9],[22,9],[20,9],[18,9],[16,9],[14,9],[12,9],[10,9],[8,9],[6,9],
    [4,9],[2,9],[0,9],[0,11],[0,13],[0,15],[0,17],[2,17],[4,17],[6,17],[8,17],[10,17],[12,17],[14,17],
    [16,17],[18,17],[20,17],[22,17],[24,17],[26,17],[20,19],[20,21],[20,23],[20,25],[26,25],[24,25],
    [22,25],[20,25],[18,25],[16,25],[14,25],[12,25],[10,25],[8,25],[6,25],[4,25],[2,25],[0,25],[2,27],[2,29],
    [2,31],[0,33],[2,33],[4,33],[6,33],[8,33],[10,33],[12,33],[14,33],[16,33],[18,33],[20,33],[22,33],
    [24,33],[26,33],[8,35],[8,37],[8,39],[8,41],[18,35],[18,37],[18,39],[18,41],[0,41],[2,41],[4,41],[6,41],
    [8,41],[10,41],[12,41],[14,41],[16,41],[18,41],[20,41],[22,41],[24,41],[26,41],[14,43],[14,45],[14,47],
    [14,49],[0,49],[2,49],[4,49],[6,49],[8,49],[10,49],[12,49],[14,49],[16,49],[18,49],[20,49],[22,49],[24,49],
    [26,49],[6,51],[6,53],[6,55],[6,57],[18,51],[18,53],[18,55],[18,57],[0,57],[2,57],[4,57],[6,57],[8,57],[10,57],
    [12,57],[14,57],[16,57],[18,57],[20,57],[22,57],[24,57],[26,57],[-2,57]
]

#Penggambaran Objek
def titikPusat():
    glPointSize(5)
    glColor3f(1, 1, 1)
    glBegin(GL_POINTS)
    glVertex(0, 0)
    glEnd()

def sumbuY():
    glLineWidth(3)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex(0, -30)
    glVertex(0, 26)
    glEnd()

def Box1():
    os.system('cls') #Agar duplikat output cukup tampil sekali
    global pos_x_box_1,pos_y_box_1, boleh_jalan, path_box_2, motion, log_path1, game, pos_pemain1, win, loss #Dibuat global variabel agar dapat dipanggil dimanapun
    #print('pos box1: ',pos_x_box_1,"",pos_y_box_1)
    pos_pemain1 = [pos_x_box_1, pos_y_box_1]

    try: #Untuk menguji statment dibawah erro atau tidak
        if len(log_path1) > 2:
            log_path1.pop()
        if pos_pemain1 == log_path1[1]:
            pass
        else:
            log_path1.pop(0)
            log_path1.append(pos_pemain1)

    except:
        log_path1.append(pos_pemain1)
  
    if log_path1[1] not in path_box_1: #Jika koordinat jalan yang diambil selanjutnya tidak ada di path maka akan direplace dengan koordinat sebelumnya
        log_path1[1] = log_path1[0]
        pos_x_box_1 = log_path1[1][0]
        pos_y_box_1 = log_path1[1][1]

    if pos_x_box_1 == pos_x_bom_2 and pos_y_box_1 == 25 or pos_y_box_1 == 49: #Pengecekan Collision Box dengan Bom
        loss = True #Jika iya, kalah dan game berhenti
        game = False

    glPushMatrix()
    glColor4f(1, 1, 0, 0)
    glTranslated(pos_x_box_1,pos_y_box_1,0)
    glTranslated(0,-1,0)
    glBegin(GL_QUADS)
    glVertex(b1[0], b1[3])
    glVertex(b1[1], b1[3])
    glVertex(b1[1], b1[2])
    glVertex(b1[0], b1[2])
    glEnd()

    glBegin(GL_QUADS)
    glColor4f(1, 0, 0, 0)
    glVertex(0, -26.8)
    glVertex(-4, -26.8)
    glVertex(-4, -26.4)
    glVertex(0, -26.4)
    glEnd()
    glPopMatrix()


    
def Box2():
    os.system('cls')
    global pos_x_box_2,pos_y_box_2, boleh_jalan, path_box_2, motion, log_path, game, pos_flag, win, loss
    print('pos box 2: ',pos_x_box_2,"",pos_y_box_2)
    pos_pemain = [pos_x_box_2, pos_y_box_2]

    try:
        if len(log_path) > 2:
            log_path.pop()
        if pos_pemain == log_path[1]:
            pass
        else:
            log_path.pop(0)
            log_path.append(pos_pemain)
    except:
        log_path.append(pos_pemain)

  
    if log_path[1] not in path_box_2:
        log_path[1] = log_path[0]
        pos_x_box_2 = log_path[1][0]
        pos_y_box_2 = log_path[1][1]

    if pos_pemain1[0] == 2 and pos_pemain1[1] == 57 and pos_pemain[0] == -2 and pos_pemain[1] == 57:
        #Pengecekan kemenangan yang akan terjadi jika posisi Box 1 dan Box 2 tumpang tindih
        win = True
        game = False

    if pos_x_box_2 == pos_x_bom_1 and pos_y_box_2 == 41 or pos_y_box_2 == 49: #Pengecekan Collison Box dengan Bom
        loss = True
        game = False
        
    glPushMatrix()
    glColor3f(0, 0, 255)
    glTranslated(pos_x_box_2,pos_y_box_2,0)
    glTranslated(0,-1,0)
    glBegin(GL_QUADS)
    glVertex(b2[0], b2[3])
    glVertex(b2[1], b2[3])
    glVertex(b2[1], b2[2])
    glVertex(b2[0], b2[2])
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(0, -27)
    glVertex(0, -26)
    glVertex(1, -27)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(4, -27)
    glVertex(4, -26)
    glVertex(3, -27)
    glEnd()

    glPointSize(3)
    glColor3f(1, 1, 1)
    glBegin(GL_POINTS)
    glVertex(2, -29)
    glEnd()
    glPopMatrix()

def Wall():
    glPushMatrix()
    glColor3f(0, 0, 255)
    glLineWidth(2.0)
    glBegin(GL_LINE_LOOP)
    glVertex(30, 30)
    glVertex(-30, 30)
    glVertex(-30, -30)
    glVertex(30, -30)
    glEnd()
    glPopMatrix()

def Tembok():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(kt[0][0], kt[0][3])
    glVertex(kt[0][0], kt[0][2])
    glVertex(kt[0][1], kt[0][2])
    glVertex(kt[0][1], kt[0][3])
    
    glVertex(kt[1][0], kt[1][2])
    glVertex(kt[1][1], kt[1][2])
    glVertex(kt[1][1], kt[1][3])
    glVertex(kt[1][0], kt[1][3])
    
    glVertex(kt[2][0], kt[2][2])
    glVertex(kt[2][1], kt[2][2])
    glVertex(kt[2][1], kt[2][3])
    glVertex(kt[2][0], kt[2][3])
    
    glVertex(kt[3][0], kt[3][2])
    glVertex(kt[3][1], kt[3][2])
    glVertex(kt[3][1], kt[3][3])
    glVertex(kt[3][0], kt[3][3])
    
    glVertex(kt[4][0], kt[4][2])
    glVertex(kt[4][1], kt[4][2])
    glVertex(kt[4][1], kt[4][3])
    glVertex(kt[4][0], kt[4][3])
    
    glVertex(kt[5][0], kt[5][2])
    glVertex(kt[5][1], kt[5][2])
    glVertex(kt[5][1], kt[5][3])
    glVertex(kt[5][0], kt[5][3])
    
    glVertex(kt[6][0], kt[6][2])
    glVertex(kt[6][1], kt[6][2])
    glVertex(kt[6][1], kt[6][3])
    glVertex(kt[6][0], kt[6][3])
    
    glVertex(kt[7][0], kt[7][2])
    glVertex(kt[7][1], kt[7][2])
    glVertex(kt[7][1], kt[7][3])
    glVertex(kt[7][0], kt[7][3])
    
    glVertex(kt[8][0], kt[8][2])
    glVertex(kt[8][1], kt[8][2])
    glVertex(kt[8][1], kt[8][3])
    glVertex(kt[8][0], kt[8][3])
    
    glVertex(kt[9][0], kt[9][2])
    glVertex(kt[9][1], kt[9][2])
    glVertex(kt[9][1], kt[9][3])
    glVertex(kt[9][0], kt[9][3])
    
    glVertex(kt[10][0], kt[10][2])
    glVertex(kt[10][1], kt[10][2])
    glVertex(kt[10][1], kt[10][3])
    glVertex(kt[10][0], kt[10][3])
    
    glVertex(kt[11][0], kt[11][2])
    glVertex(kt[11][1], kt[11][2])
    glVertex(kt[11][1], kt[11][3])
    glVertex(kt[11][0], kt[11][3])
    
    glVertex(kt[12][0], kt[12][2])
    glVertex(kt[12][1], kt[12][2])
    glVertex(kt[12][1], kt[12][3])
    glVertex(kt[12][0], kt[12][3])
    
    glVertex(kt[13][0], kt[13][2])
    glVertex(kt[13][1], kt[13][2])
    glVertex(kt[13][1], kt[13][3])
    glVertex(kt[13][0], kt[13][3])
    
    glVertex(kt[14][0], kt[14][2])
    glVertex(kt[14][1], kt[14][2])
    glVertex(kt[14][1], kt[14][3])
    glVertex(kt[14][0], kt[14][3])
    
    glVertex(kt[15][0], kt[15][2])
    glVertex(kt[15][1], kt[15][2])
    glVertex(kt[15][1], kt[15][3])
    glVertex(kt[15][0], kt[15][3])
    
    glVertex(kt[16][0], kt[16][2])
    glVertex(kt[16][1], kt[16][2])
    glVertex(kt[16][1], kt[16][3])
    glVertex(kt[16][0], kt[16][3])
    
    glVertex(kt[17][0], kt[17][2])
    glVertex(kt[17][1], kt[17][2])
    glVertex(kt[17][1], kt[17][3])
    glVertex(kt[17][0], kt[17][3])

    glVertex(kt[18][0], kt[18][2])
    glVertex(kt[18][1], kt[18][2])
    glVertex(kt[18][1], kt[18][3])
    glVertex(kt[18][0], kt[18][3])

    glVertex(kt[19][0], kt[19][2])
    glVertex(kt[19][1], kt[19][2])
    glVertex(kt[19][1], kt[19][3])
    glVertex(kt[19][0], kt[19][3])

    glVertex(kt[20][0], kt[20][2])
    glVertex(kt[20][1], kt[20][2])
    glVertex(kt[20][1], kt[20][3])
    glVertex(kt[20][0], kt[20][3])

    glVertex(kt[21][0], kt[21][2])
    glVertex(kt[21][1], kt[21][2])
    glVertex(kt[21][1], kt[21][3])
    glVertex(kt[21][0], kt[21][3])
    glEnd()
    glPopMatrix()


def Flag():
    glPushMatrix()
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-1, 30)
    glVertex(1, 29)
    glVertex(-1, 28)
    glEnd()

    glColor3f(0, 0, 1)
    glBegin(GL_LINES)
    glVertex(-1, 30)
    glVertex(-1, 26)
    glEnd()
    glPopMatrix()

def Bom1():
    os.system("cls")
    global pos_x_bom_1, pos_y_bom_1, game, motion, pos_bom_1
    pos_bom_1 = [pos_x_bom_1, pos_y_bom_1]

    if game == True and pos_x_bom_1 < 26: #Jika y kurang dari 26 maka bom akan bergeser
        pos_x_bom_1 += motion
        log_bom_1.append(pos_bom_1)

    if pos_bom_1 == [26, 1]: #Jika sudah mencapai 26 maka akan kembali kesemula
        pos_x_bom_1 = 0
        pos_y_bom_1 = 1
    #print(pos_bom_1)

    glPushMatrix()
    glTranslated(pos_x_bom_1, pos_y_bom_1,0)
    glTranslated(0,-1,0)
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(2, 14)
    glVertex(0, 10.5)
    glVertex(4, 10.5)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(2, 10)
    glVertex(0, 13.5)
    glVertex(4, 13.5)
    glEnd()
    glPopMatrix()

def Bom2():
    os.system("cls")
    global pos_x_bom_2, pos_y_bom_2, game, motion
    pos_bom_2 = [pos_x_bom_2, pos_y_bom_2]

    if game == True and pos_x_bom_2 > -26:
        pos_x_bom_2 -= motion
        log_bom_2.append(pos_bom_2)

    if pos_bom_2 == [-26, 1]:
        pos_x_bom_2 = 0
        pos_y_bom_2 = 1

    glPushMatrix()
    glTranslated(pos_x_bom_2, pos_y_bom_2,0)
    glTranslated(0,-1,0)
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 22)
    glVertex(0, 18.5)
    glVertex(-4, 18.5)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(-2, 18)
    glVertex(0, 21.5)
    glVertex(-4, 21.5)
    glEnd()
    glPopMatrix()

def Bom3():
    os.system("cls")
    global pos_x_bom_3, pos_y_bom_3, game, motion, pos_bom_3
    pos_bom_3 = [pos_x_bom_3, pos_y_bom_3]

    if game == True and pos_x_bom_3 < 26:
        pos_x_bom_3 += motion
        log_bom_3.append(pos_bom_1)

    if pos_bom_3 == [26, 1]:
        pos_x_bom_3 = 0
        pos_y_bom_3 = 1

    glPushMatrix()
    glTranslated(pos_x_bom_3, pos_y_bom_3,0)
    glTranslated(0,-1,0)
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(2, 22)
    glVertex(0, 18.5)
    glVertex(4, 18.5)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(2, 18)
    glVertex(0, 21.5)
    glVertex(4, 21.5)
    glEnd()
    glPopMatrix()

def Bom4():
    os.system("cls")
    global pos_x_bom_4, pos_y_bom_4, game, motion
    pos_bom_4 = [pos_x_bom_4, pos_y_bom_4]

    if game == True and pos_x_bom_4 > -26:
        pos_x_bom_4 -= motion
        log_bom_4.append(pos_bom_4)

    if pos_bom_4 == [-26, 1]:
        pos_x_bom_4 = 0
        pos_y_bom_4 = 1

    glPushMatrix()
    glTranslated(pos_x_bom_4, pos_y_bom_4,0)
    glTranslated(0,-1,0)
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, -2)
    glVertex(0, -5.5)
    glVertex(-4, -5.5)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(-2, -6)
    glVertex(0, -2.5)
    glVertex(-4, -2.5)
    glEnd()
    glPopMatrix()

def Background():
    glPushMatrix()
    glColor3f(0, 0, 0)
    glLineWidth(2.0)
    glBegin(GL_QUADS)
    glVertex(30, 30)
    glVertex(-30, 30)
    glVertex(-30, -30)
    glVertex(30, -30)
    glEnd()
    glPopMatrix()

def Menu():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-15, 5)
    glVertex(15, 5)
    glVertex(15, -5)
    glVertex(-15, -5)
    glEnd()
    glPopMatrix()

def Start():
    glPushMatrix()
    glColor3f(0, 0, 1)
    glRasterPos(-9, 2)
    for i in judul_game:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))
    glRasterPos(-9, 1)
    for i in petunjuk_1:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, ord(i))
    glRasterPos(-9, 0)
    for i in petunjuk_2:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, ord(i))
    glRasterPos(-9, -1)
    for i in petunjuk_3:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, ord(i))
    glPopMatrix()

def Winner():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-20, 5)
    glVertex(20, 5)
    glVertex(20, -5)
    glVertex(-20, -5)
    glEnd()
    
    glColor3f(1, 0, 0)
    glRasterPos(-7, 0)
    for i in kalimat_win:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))
    glPopMatrix()


def Loss():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-20, 5)
    glVertex(20, 5)
    glVertex(20, -5)
    glVertex(-20, -5)
    glEnd()
    
    glColor3f(1, 0, 0)
    glRasterPos(-7, 0)
    for i in kalimat_loss:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))
    glPopMatrix()

def input_keyboard(key, x, y):
    global pos_x_box_1, pos_y_box_1, pos_x_box_2,pos_y_box_2, boleh_jalan, motion, game, pos_x_bom_1, win
    
    if key == GLUT_KEY_UP and boleh_jalan == True and game == True:
        pos_y_box_1 += motion
        pos_y_box_2 += motion
    if key == GLUT_KEY_DOWN and boleh_jalan == True and game == True:
        pos_y_box_1 -= motion
        pos_y_box_2 -= motion
    if key == GLUT_KEY_RIGHT and boleh_jalan == True and game == True:
        pos_x_box_1 -= motion
        pos_x_box_2 += motion
    if key == GLUT_KEY_LEFT and boleh_jalan == True and game == True:
        pos_x_box_1 += motion
        pos_x_box_2 -= motion
    if key == GLUT_KEY_HOME:
        game = True
        win = False
        loss = False
    if key == GLUT_KEY_END:
        game = False
        win = False
        loss = False
        pos_x_box_1 = 0
        pos_y_box_1 = 1
        pos_x_box_2 = 0
        pos_y_box_2 = 1
    if key == GLUT_KEY_F1:
        boleh_jalan = False
    if key == GLUT_KEY_F2:
        boleh_jalan = True

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-30, 30, -30, 30)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #titikPusat()
    #Menu()
    Start()
    if win == True:
        Background()
        Winner() #Ini akan tampil jika win bernilai True
    if loss == True:
        Background()
        Loss() #Ini akan tampil jika loss bernilai True
    if game == True:
        Background() #Ini akan tampil selama game berjalan
        Box1()
        Box2()
        Tembok()
        Flag()
        Wall()
        sumbuY()
        Bom1()
        Bom2()
        Bom3()
        Bom4()
    glutSwapBuffers()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv) 
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("BRO AND MAX")
    glutDisplayFunc(draw)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    glutMainLoop()


main()
