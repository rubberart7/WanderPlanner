class ParseData:

    def __init__(self):
        self.__dataList = []

    def addItinerary(self, itinerary):
        self.__dataList.append(eval(itinerary))
        print(self.__dataList)

    def getDataList(self):
        return self.__dataList

    def clear(self):
        self.__dataList = []
