
def openStyleSheet(path):
    with open(path, "r") as styleSheet:
        return styleSheet.read()


class Dimension(object):

    def __init__(self,width,height):
        self.width = width
        self.height= height

class RectDimension(Dimension):
    def __init__(self, x, y, width, height):
        super()