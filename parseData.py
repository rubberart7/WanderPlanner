class ParseData:

    def __init__(self):
        self.dataList = []

    def addItinerary(self, itinerary):
        self.dataList.append(eval(itinerary))
        print(self.dataList)
