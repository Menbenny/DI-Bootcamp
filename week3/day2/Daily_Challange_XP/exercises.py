class Pagination:
   
    def __init__(self, items: list = None, pageSize=10) -> None:
        if items is not None:
            self.items = items
        else:
            self.items = []
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = int(len(self.items) / self.pageSize) + (1 if len(self.items) % self.pageSize > 0 else 0)
        self.currentPage = 0

    def getVisibleItems(self):
        startIndex = (self.currentPage - 1) * self.pageSize
        endIndex = startIndex + self.pageSize
        return self.items[startIndex:endIndex]

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        if pageNum < 1:
            pageNum = 1
        elif pageNum > self.totalPages:
            pageNum = self.totalPages
        self.currentPage = pageNum
        return self
