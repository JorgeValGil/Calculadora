import events
import sys
import var
from calculadora import *


class Main(QtWidgets.QMainWindow):
    """Clase principal del programa"""

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        var.ui.b0.clicked.connect(events.Eventos.bzero)
        var.ui.b1.clicked.connect(events.Eventos.bone)
        var.ui.b2.clicked.connect(events.Eventos.btwo)
        var.ui.b3.clicked.connect(events.Eventos.bthree)
        var.ui.b4.clicked.connect(events.Eventos.bfour)
        var.ui.b5.clicked.connect(events.Eventos.bfive)
        var.ui.b6.clicked.connect(events.Eventos.bsix)
        var.ui.b7.clicked.connect(events.Eventos.bseven)
        var.ui.b8.clicked.connect(events.Eventos.beight)
        var.ui.b9.clicked.connect(events.Eventos.bnine)

        var.ui.bsum.clicked.connect(events.Eventos.bsum)
        var.ui.bsubtract.clicked.connect(events.Eventos.bsubtract)
        var.ui.bmultiplication.clicked.connect(events.Eventos.bmultiplication)
        var.ui.bdivision.clicked.connect(events.Eventos.bdivision)

        var.ui.bdot.clicked.connect(events.Eventos.bdot)
        var.ui.bparenthesiso.clicked.connect(events.Eventos.bparenthesisopen)
        var.ui.bparenthesisc.clicked.connect(events.Eventos.bparenthesisclose)

        var.ui.bclear.clicked.connect(events.Eventos.bclear)
        var.ui.bcalculate.clicked.connect(events.Eventos.bcalculate)


if __name__ == '__main__':
    '''Ejecución del programa'''
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
