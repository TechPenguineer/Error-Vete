ERROR_MSG_TEST = """  File "d:\Desktop\ErrorVete\Error-Vete\__test.py", line 2, in <module>
    print("Total number of days: " + days)
 TypeError: can only concatenate str (not "int") to str"""

import sys
from .ERROR_MESSAGES import ERROR_MSG

class EVParser:
    def __init__(self):
        self.fileLocation
        self.errorLine
        self.typeError

    def removeCharType(char, data):
        try:
            import re
        except ImportError:
            print(ERROR_MSG.IMPORT_ERROR)
            sys.exit(0)
        return re.sub(char,"", data)


    def parseErrorMessage(msg, self):
     try:
        data = msg.split()
        self.errorLine = EVParser.removeCharType(",", data[3] )
        fl1 = EVParser.removeCharType('"', data[1] )
        self.fileLocation = EVParser.removeCharType(',', fl1 )
        #print("Error @:\n\nLine: " + self.errorLine + "\nOf File: " + self.fileLocation)
     except:
        print(ERROR_MSG.PARSE_ERROR)
