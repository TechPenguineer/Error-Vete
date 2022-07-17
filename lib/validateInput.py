import ERROR_MESSAGES
def validateInput(data):
    if len(data) < 0:
        print(ERROR_MESSAGES.ERROR_MSG.LENGTH_TO_SMALL)