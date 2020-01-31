import math

class bowl():

    def __init__(self, triangles):
        self.slices = triangles

        self.baseAngle = ((180 * (self.slices - 2)) / self.slices) / 2
        self.baseHeight = None

        self.triBase = 10
        self.triHeight = 18.66025

        self.sliceHeight = None


    def calc_base_height(self):
        self.baseHeight = (self.triBase / 2) / math.cos(math.radians(self.baseAngle))


    def calc_slice_height(self):
        self.sliceHeight = self.triHeight * math.cos(math.asin(self.baseHeight / self.triHeight))


    def calc_volume(self):
        sliceBase = (self.triBase * self.baseHeight) / 2
        bowlVolume = ((sliceBase * self.sliceHeight) / 3) * self.slices

        return bowlVolume


    def print_bowl(self):
        print "Slices: {0}".format(self.slices)
        print "Base Angle: {0}".format(self.baseAngle)
        print "Base Height: {0}".format(self.baseHeight)
        print "Tri Base: {0}".format(self.triBase)
        print "Tri Height: {0}".format(self.triHeight)
        print "Slice Height: {0}".format(self.sliceHeight)


def get_dimensions():

    for i in range(3,12):

        b = bowl(i)
        b.calc_base_height()
        #b.print_bowl()
        b.calc_slice_height()
        #b.print_bowl()
        vol = b.calc_volume()

        print "Bowl of {0} slices has volume of {1}".format(i, vol)

get_dimensions()
