ERROR_MSG = """  File "d:\Desktop\ErrorVete\Error-Vete\__test.py", line 2, in <module>
    print("Total number of days: " + days)
 TypeError: can only concatenate str (not "int") to str"""


class EVParser:
    def __init__(self):
        self.fileLocation
        self.errorLine
        self.statement
        self.typeError

    def removeCommaSep(data):
        
    def parseErrorMessage(msg, self):
        data = msg.split()
        self.errorLine = data[3]
        self.fileLocation = data[1]
        print("Error @:\n\nLine: " + self.errorLine + "\nOf File: " + self.fileLocation)


EVParser.parseErrorMessage(ERROR_MSG, EVParser)