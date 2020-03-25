
def openStyleSheet(path):
    with open(path, "r") as styleSheet:
        return styleSheet.read()


class Dimension(object):

    def __init__(self,width,height):
        self.width = width
        self.height= height

    def asQRect(self):
        print("")

    def asQSize(self):
        print("")
