ERROR_MSG = """  File "d:\Desktop\ErrorVete\Error-Vete\__test.py", line 2, in <module>
    print("Total number of days: " + days)
 TypeError: can only concatenate str (not "int") to str"""

from ERROR_MESSAGES import *

class EVParser:
    def __init__(self):
        self.fileLocation
        self.errorLine
        self.statement
        self.typeError

    def removeCharType(char, data):
        try:
            import refsa
        except ImportError:
            print(ERROR_MSG.IMPORT_ERROR)
        return re.sub(char,"", data)


    def parseErrorMessage(msg, self):
        data = msg.split()
        self.errorLine = EVParser.removeCharType(",", data[3] )
        fl1 = EVParser.removeCharType('"', data[1] )
        self.fileLocation = EVParser.removeCharType(',', fl1 )
        print("Error @:\n\nLine: " + self.errorLine + "\nOf File: " + self.fileLocation)


EVParser.parseErrorMessage(ERROR_MSG, EVParser)