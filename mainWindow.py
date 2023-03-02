from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox, QFileDialog
import mainWindow_ui
import backlash

class form(QtWidgets.QMainWindow, mainWindow_ui.Ui_MainWindow):
    def __init__(self):
        super(form, self).__init__()
        self.setupUi(self)  #setup user interface

        self.btnInput.clicked.connect(self.btnInput_callback) #set connect button callback
        self.btnOutput.clicked.connect(self.btnOutput_callback) #set connect button callback
        self.btnRun.clicked.connect(self.btnRun_callback) #set connect button callback

        self.backlash = backlash.backlash()

        self.inputFile = ""
        self.outputFile = ""

    def btnInput_callback(self):
        self.inputFile =  QFileDialog.getOpenFileName(self, 'Select File')[0]  #select file
        self.lblInput.setText(self.inputFile)    #display input file

    def btnOutput_callback(self):
        self.outputFile =  QFileDialog.getSaveFileName(self, 'Select File')[0] #select file
        self.lblOutput.setText(self.outputFile)  #display output file

    def btnRun_callback(self):
        self.btnRun.setEnabled(False)   #disable button while running

        if (self.inputFile == ""):  #make sure an input file has been selected
            QMessageBox.about(self, "Error", "You must select an input file before running!")
            self.btnRun.setEnabled(True)   #enable button
            return

        if (self.outputFile == ""):  #make sure an output file has been selected
            QMessageBox.about(self, "Error", "You must select an output file before running!")
            self.btnRun.setEnabled(True)   #enable button
            return

        try:
            xbl = float(self.txtXBacklash.text())  #convert text to float
        except:
            QMessageBox.about(self, "Error", "X backlash must be a number!")
            self.btnRun.setEnabled(True)   #enable button
            return

        try:
            ybl = float(self.txtYBacklash.text())  #convert text to float
        except:
            QMessageBox.about(self, "Error", "Y backlash must be a number!")
            self.btnRun.setEnabled(True)   #enable button
            return

        try:
            zbl = float(self.txtZBacklash.text())  #convert text to float
        except:
            QMessageBox.about(self, "Error", "Z backlash must be a number!")
            self.btnRun.setEnabled(True)   #enable button
            return

        try:
            tol = float(self.txtTolerance.text())  #convert text to float
        except:
            QMessageBox.about(self, "Error", "Tolerance must be a number!")
            self.btnRun.setEnabled(True)   #enable button
            return

        #see if need to convert compensation from metric
        if (self.rbMetric.isChecked() == True):
            xbl = xbl * 25.4
            ybl = ybl * 25.4
            zbl = zbl * 25.4
            tol = tol * 25.4

        try:
            self.backlash.setBacklash(xbl, ybl, zbl, tol)
            self.backlash.applyBacklash(self.inputFile)
        except:
            QMessageBox.about(self, "Error!", "Error reading GCode file!")
            self.btnRun.setEnabled(True)   #enable button
            return 

        try:
            self.backlash.saveOutput(self.outputFile)
        except:
            QMessageBox.about(self, "Error!", "Error saving GCode file!")
            self.btnRun.setEnabled(True)   #enable button
            return

        self.btnRun.setEnabled(True)   #enable button
        QMessageBox.about(self, "Finished!", "Backlash compensation complete!")