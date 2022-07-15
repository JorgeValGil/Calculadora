import var


class Eventos:

    def number(self, s):
        var.ui.textoperation.setStyleSheet("background-color: white")
        var.ui.textoperation.insertPlainText(s)

    def bzero(self):
        return Eventos.number(self, "0")

    def bone(self):
        return Eventos.number(self, "1")

    def btwo(self):
        return Eventos.number(self, "2")

    def bthree(self):
        return Eventos.number(self, "3")

    def bfour(self):
        return Eventos.number(self, "4")

    def bfive(self):
        return Eventos.number(self, "5")

    def bsix(self):
        return Eventos.number(self, "6")

    def bseven(self):
        return Eventos.number(self, "7")

    def beight(self):
        return Eventos.number(self, "8")

    def bnine(self):
        return Eventos.number(self, "9")

    def bparenthesisopen(self):
        return Eventos.number(self, "(")

    def bparenthesisclose(self):
        return Eventos.number(self, ")")

    def validateoperator(self, text):
        if len(text) == 0:
            var.ui.textoperation.setStyleSheet("background-color: red")
            return False
        else:
            lastchar = text[-1]
            symbols = "+-*/."
            valid = True
            for i in range(len(symbols)):
                if symbols[i] == lastchar:
                    valid = False
                    break
            if valid:
                var.ui.textoperation.setStyleSheet("background-color: white")
            else:
                var.ui.textoperation.setStyleSheet("background-color: red")
            return valid

    def operator(self, op):
        textoperation = var.ui.textoperation.toPlainText()
        if Eventos.validateoperator(self, textoperation):
            newtextoperation = textoperation + op
            Eventos.setresult(self, newtextoperation)

    def bsum(self):
        return Eventos.operator(self, '+')

    def bsubtract(self):
        return Eventos.operator(self, '-')

    def bmultiplication(self):
        return Eventos.operator(self, '*')

    def bdivision(self):
        return Eventos.operator(self, '/')

    def bdot(self):
        return Eventos.operator(self, '.')

    def setresult(self, a):
        var.ui.textoperation.clear()
        var.ui.textoperation.insertPlainText(a)

    def validateoperation(self, text):
        numbers = "0123456789"
        count = 0
        for i in range(len(numbers)):
            for j in range(len(text)):
                if numbers[i] == text[j]:
                    count += 1
        if count >= 2:
            var.ui.textoperation.setStyleSheet("background-color: white")
            return True
        else:
            var.ui.textoperation.setStyleSheet("background-color: red")
            return False

    def calcular(self, text):
        try:
            result = eval(str(text))
        except (ZeroDivisionError, NameError, TypeError, SyntaxError, Exception):
            result = 'error'
            var.ui.textoperation.setStyleSheet("background-color: red")
        if result != 'error':
            Eventos.setresult(self, str(result))

    def bclear(self):
        var.ui.textoperation.setStyleSheet("background-color: white")
        var.ui.textoperation.clear()

    def bcalculate(self):
        text = var.ui.textoperation.toPlainText()
        if Eventos.validateoperation(self, text):
            Eventos.calcular(self, text)
