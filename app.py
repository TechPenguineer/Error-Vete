from lib.getInput import *
from lib.errorParser import * 
from lib.ERROR_MESSAGES import *

try:
    data = getInput()
    EVParser.parseErrorMessage(data, EVParser)
except ImportError:
    print(ERROR_MSG.IMPORT_ERROR)