class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   ERROR_MSG_COLOR = '\033[1m\033[91m'

class ERROR_MSG:
    ERROR_ICO = color.BOLD + color.YELLOW + "( ! ) "
    
    LENGTH_TO_SMALL = ERROR_ICO + color.ERROR_MSG_COLOR + "The provided length is to small."
    LENGTH_TO_LARGE = ERROR_ICO + color.ERROR_MSG_COLOR + "The provided length is to large."
    IMPORT_ERROR = ERROR_ICO + color.ERROR_MSG_COLOR + "Import Error. Unable to successfuly import libraries."
    INVALID_FORMAT = ERROR_ICO + color.ERROR_MSG_COLOR + "Format Error. The format provided is an invalid type."
    PARSE_ERROR = ERROR_ICO + color.ERROR_MSG_COLOR + "Unable to parse."