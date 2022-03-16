# Asmaa Gamal
#Assignment 2
# Electronics & Communications department
#Using Minimax Algorithm to Make Connect 4 AI Agent

#-------------------------------------------------- preparing for the GUI stage -----------------------------------------------------------------

#--------------------------------------------------------------using QT--------------------------------------------------------------------------

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
#------------------------------------------ My Methods to link the Welcoming-Gui with my pygame-Gui ----------------------
    '''
    def MinmaxGui(self):
       return True

    def Pruning_Gui(self):
        return True
     '''
#-------------------------------------------------------------------------------------------------------------------------
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(785, 390)
        Form.setStyleSheet("background-color: rgb(255, 255, 255)\n""")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 220, 450, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n""Background:rgb(55, 255, 225)\n""\n""}")
        self.pushButton.setObjectName("pushButton")
        ''''
        # ------------------------------MyMinmax Button Event -------------------------------
        self.pushButton.clicked.connect(self.MinmaxGui)
        # ---------------------------------------------------------------------------------
        '''
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 300, 450, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n""Background:rgb(55, 255, 225)\n""\n""}")
        self.pushButton_2.setObjectName("pushButton_2")

        '''
        # ------------------------------My MinMax-Pruning Button Event -------------------------------
        self.pushButton_2.clicked.connect(self.Pruning_Gui)
        # ---------------------------------------------------------------------------------
        '''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 10, 800, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 300, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 200, 300, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 90, 800, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n""Background:rgb(169, 255, 248)rgb(144, 255, 233)\n""\n""}")
        self.label_4.setObjectName("label_4")



        ##-------pushButtons of depths
        #pushButton_dep1
        self.pushButton_dep1 = QtWidgets.QPushButton(Form)
        self.pushButton_dep1.setGeometry(QtCore.QRect(320, 170, 50, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.pushButton_dep1.setFont(font)
        self.pushButton_dep1.setStyleSheet("QPushButton{\n""Background:rgb(55, 255, 225)\n""\n""}")
        self.pushButton_dep1.setObjectName("pushButton_dep1")


        # pushButton_dep2
        self.pushButton_dep2 = QtWidgets.QPushButton(Form)
        self.pushButton_dep2.setGeometry(QtCore.QRect(400, 170, 50, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.pushButton_dep2.setFont(font)
        self.pushButton_dep2.setStyleSheet("QPushButton{\n""Background:rgb(55, 255, 225)\n""\n""}")
        self.pushButton_dep2.setObjectName("pushButton_dep2")


        ##pushButton_dep3
        self.pushButton_dep3 = QtWidgets.QPushButton(Form)
        self.pushButton_dep3.setGeometry(QtCore.QRect(480, 170, 50, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.pushButton_dep3.setFont(font)
        self.pushButton_dep3.setStyleSheet("QPushButton{\n""Background:rgb(55, 255, 225)\n""\n""}")
        self.pushButton_dep3.setObjectName("pushButton_dep3")


        ##pushButton_dep4
        self.pushButton_dep4 = QtWidgets.QPushButton(Form)
        self.pushButton_dep4.setGeometry(QtCore.QRect(560, 170, 50, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.pushButton_dep4.setFont(font)
        self.pushButton_dep4.setStyleSheet("QPushButton{\n""Background:rgb(55, 255, 225)\n""\n""}")
        self.pushButton_dep4.setObjectName("pushButton_dep4")



        ##pushButton_dep5
        self.pushButton_dep5 = QtWidgets.QPushButton(Form)
        self.pushButton_dep5.setGeometry(QtCore.QRect(640, 170, 50, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.pushButton_dep5.setFont(font)
        self.pushButton_dep5.setStyleSheet("QPushButton{\n""Background:rgb(55, 255, 225)\n""\n""}")
        self.pushButton_dep5.setObjectName("pushButton_dep5")



        ##pushButton_dep6
        self.pushButton_dep6 = QtWidgets.QPushButton(Form)
        self.pushButton_dep6.setGeometry(QtCore.QRect(720, 170, 50, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.pushButton_dep6.setFont(font)
        self.pushButton_dep6.setStyleSheet("QPushButton{\n""Background:rgb(55, 255, 225)\n""\n""}")
        self.pushButton_dep6.setObjectName("pushButton_dep6")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Connect-4 Game Welcoming GUI"))
        self.pushButton.setText(_translate("Form", "MinMax"))
        self.pushButton_2.setText(_translate("Form", "α-β Pruning Minmax"))
        self.label.setText(_translate("Form", "        Welcome To Connect-4 Game!"))
        self.label_2.setText(_translate("Form", "Pick AI Searching Depth Level For Me:"))
        self.label_3.setText(_translate("Form", "Pick an AI Searching Algorithm For Me:"))
        self.label_4.setText(_translate("Form", "         Hi Dude.. How are things?  I am your Computer and I will Be Your opponent Player"))

        ##-------pushButtons of depths
        self.pushButton_dep1.setText(_translate("Form", "1"))
        self.pushButton_dep2.setText(_translate("Form", "2"))
        self.pushButton_dep3.setText(_translate("Form", "3"))
        self.pushButton_dep4.setText(_translate("Form", "4"))
        self.pushButton_dep5.setText(_translate("Form", "5"))
        self.pushButton_dep6.setText(_translate("Form", "6"))


#----------------------------------------------------------- using colors in printing on the console screen code----------------------------------------------------


ANSI_RESET = "\u001B[0m"
ANSI_CYAN = "\u001B[36m"

def print_cyan(msg):
    print(f"{ANSI_CYAN}{msg}{ANSI_RESET}")

def print_cyan_without_NewLine(msg):
    print(f"{ANSI_CYAN}{msg}{ANSI_RESET}",end='')