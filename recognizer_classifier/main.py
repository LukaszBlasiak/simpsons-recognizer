from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QGridLayout, QPushButton
from os import listdir, remove
from os.path import isfile, join
import random
import subprocess
import cv2
import numpy as np

class BIAI(QWidget):

    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.IMAGES_DIR = "images/"
        CASCADES_DIR = "resources/"
        self.fileNamesArray = listdir(self.IMAGES_DIR)
        self.cascadeNamesArray = listdir(CASCADES_DIR)
        self.interfejs()
    
    def interfejs(self):
        self.status = QLabel('Analyzing',self)
        self.status.setWordWrap(True)
        self.status.move(10,50)
        self.pic = QLabel(self)
        self.pic.setPixmap(QPixmap("image.bmp"))
        self.nextImageButton = QPushButton("&Next image >>", self)
        self.nextImageButton.resize(100,40)
        self.nextImageButton.clicked.connect(self.nextImage)
        self.foundAbrahamLabel = QLabel("Abraham Simpson:",self);
        self.foundBartLabel = QLabel("Bart Simpson:",self);
        self.foundMontgomeryLabel = QLabel("Montgomery Burns:",self);
        self.foundWiggumLabel = QLabel("Chief Wiggum:",self);
        self.foundHomerLabel = QLabel("Homer Simpson:",self);
        self.foundLisaLabel = QLabel("Lisa Simpson:",self);
        self.foundMargeLabel = QLabel("Marge Simpson:",self);
        self.foundMilhouseLabel = QLabel("Milhouse Houten:",self);
        self.foundMoeLabel = QLabel("Moe Szyslak:",self);
        self.foundNedLabel = QLabel("Ned Flanders:",self);
        self.foundSkinnerLabel = QLabel("Principal Skinner:",self);
        self.foundBobLabel = QLabel("Sideshow Bob:",self);
        self.foundAbrahamStatusLabel = QLabel("    ",self);
        self.foundBartStatusLabel = QLabel("    ",self);
        self.foundMontgomeryStatusLabel = QLabel("    ",self);
        self.foundWiggumStatusLabel = QLabel("    ",self);
        self.foundHomerStatusLabel = QLabel("    ",self);
        self.foundLisaStatusLabel = QLabel("    ",self);
        self.foundMargeStatusLabel = QLabel("    ",self);
        self.foundMilhouseStatusLabel = QLabel("    ",self);
        self.foundMoeStatusLabel = QLabel("    ",self);
        self.foundNedStatusLabel = QLabel("    ",self);
        self.foundSkinnerStatusLabel = QLabel("    ",self);
        self.foundBobStatusLabel = QLabel("    ",self);
        self.foundAbrahamLabel.move(50,550);
        self.foundBartLabel.move(50,570);
        self.foundMontgomeryLabel.move(50,590);
        self.foundWiggumLabel.move(50,610);
        self.foundHomerLabel.move(50,630);
        self.foundLisaLabel.move(50,650);
        self.foundMargeLabel.move(50,670);
        self.foundMilhouseLabel.move(50,690);
        self.foundMoeLabel.move(50,710);
        self.foundNedLabel.move(50,730);
        self.foundSkinnerLabel.move(50,750);
        self.foundBobLabel.move(50,770);
        self.foundAbrahamStatusLabel.move(160,550);
        self.foundBartStatusLabel.move(160,570);
        self.foundMontgomeryStatusLabel.move(160,590);
        self.foundWiggumStatusLabel.move(160,610);
        self.foundHomerStatusLabel.move(160,630);
        self.foundLisaStatusLabel.move(160,650);
        self.foundMargeStatusLabel.move(160,670);
        self.foundMilhouseStatusLabel.move(160,690);
        self.foundMoeStatusLabel.move(160,710);
        self.foundNedStatusLabel.move(160,730);
        self.foundSkinnerStatusLabel.move(160,750);
        self.foundBobStatusLabel.move(160,770);
        
        self.setGeometry(120, 60, 800, 800)
        self.resetStatusLabels()
        self.setWindowTitle("The simpsons characters detector")
        self.show()
        self.nextImage()

    def resetStatusLabels(self):
        self.foundAbrahamStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundBartStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundMontgomeryStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundWiggumStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundHomerStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundLisaStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundMargeStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundMilhouseStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundMoeStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundNedStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundSkinnerStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        self.foundBobStatusLabel.setStyleSheet("QLabel { background-color : red;}")
        QApplication.processEvents()
    def updateStatusLabels(self, foundCharacter):
        if foundCharacter == "abraham":
            self.foundAbrahamStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "bart":
            self.foundBartStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "bob":
            self.foundBobStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "flanders":
            self.foundNedStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "homer":
            self.foundHomerStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "lisa":
            self.foundLisaStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "marge":
            self.foundMargeStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "milhouse":
            self.foundMilhouseStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "moe":
            self.foundMoeStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "montgomery":
            self.foundMontgomeryStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "skinner":
            self.foundSkinnerStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        elif foundCharacter == "wiggum":
            self.foundWiggumStatusLabel.setStyleSheet("QLabel { background-color : green;}")
        
    def updateStatus(self, status):
        if status is 'Ready':
            self.status.setText('Ready')
            self.status.setStyleSheet("QLabel { background-color : green; color : white; }")
        elif status is 'Analyzing':
            self.status.setText('Analyzing')
            self.status.setStyleSheet("QLabel { background-color : yellow; color : black; }")
        elif status is 'Error':
            self.status.setText('Error')
            self.status.setStyleSheet("QLabel { background-color : red; color : white; }")
        QApplication.processEvents()
        
    def updateImage(self, path):  
        self.image = QPixmap(path)
        self.pic.setPixmap(self.image)
        self.pic.move(400-self.image.width()/2, 0)
        QApplication.processEvents()
        
    def nextImage(self):
        self.resetStatusLabels()
        self.path = self.IMAGES_DIR + random.choice (self.fileNamesArray)
        cv2.imwrite('current_face.jpg',cv2.imread (self.path, 1))
        self.updateImage(self.path)
        self.charactersArray = ["abraham", "bart", "bob", "flanders", "homer", "lisa", "marge", "milhouse", "moe", "montgomery", "skinner", "wiggum"]
        charactersCount = len(self.charactersArray)
        for cascade in self.cascadeNamesArray:
            self.findFace('resources/' + cascade)
        if len(self.charactersArray) == charactersCount:
            print("I didn't find anyone")
        
    def findFace(self, cascadePath):
        self.updateStatus('Analyzing')
        face_cascade = cv2.CascadeClassifier(cascadePath)
        image2 = cv2.imread ('current_face.jpg', 1)
        gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.imwrite('entry_face.jpg',image2[y:y+h, x:x+w])
            proc = str(subprocess.Popen(['python', 'classify.py',  'entry_face.jpg'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0])
            found = self.validateResults(proc)
            if found:
                cv2.rectangle(image2, (x,y), (x+w, y+h), (0,255,0),3)
                cv2.imwrite('current_face.jpg',image2)
                self.updateImage('current_face.jpg')
        self.updateStatus('Ready')
        
    def validateResults(self, results):
        tmp=str(results).replace("b'","")
        resultsArray = tmp.split(';')
        if resultsArray[0] in self.charactersArray and float(resultsArray[1]) > 0.6:
            self.charactersArray.remove(resultsArray[0])
            self.updateStatusLabels(resultsArray[0])
            print('I found: ' + resultsArray[0] + ' with: ' + resultsArray[1])
            return True
        return False
        
    def closeEvent(self, event):
        try:
            remove('entry_face.jpg')
            remove('current_face.jpg')
        except OSError:
            pass
            
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = BIAI()
    sys.exit(app.exec_())
