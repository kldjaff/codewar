# coding=utf-8
import math


class PaginationHelper(object):
    """
    https://www.codewars.com/kata/515bb423de843ea99400000a
    The constructor takes in an array of items and a integer indicating
    how many items fit within a single page
    """

    def __init__(self, collection, items_per_page):
        """
        :param collection:
        :param items_per_page:
        """
        self.collection = collection
        self.page_size = items_per_page
        self.page_total = math.ceil(len(self.collection) / self.page_size)
        self.item_total = len(self.collection)

    def item_count(self):
        """
        :return: returns the number of items within the entire collection
        """
        return self.item_total

    def page_count(self):
        """
        :return: returns the number of pages
        """
        return self.page_total

    def page_item_count(self, page_index):
        """
        :param page_index:
        :return:
            returns the number of items on the current page. page_index is zero based
            this method should return -1 for page_index values that are out of range
        """
        if page_index >= 0 and page_index < self.page_total - 1:
            return self.page_size
        else:
            if page_index == self.page_total - 1:
                return self.item_total - page_index * self.page_size
            else:
                return -1

    def page_index(self,item_index):
        """
        :param item_index:
        :return:
            determines what page an item is on. Zero based indexes.
            this method should return -1 for item_index values that are out of range
        """
        page_index = math.floor(item_index / self.page_size)
        if page_index < 0 or item_index >= self.item_total:
            page_index = -1
        return page_index


if __name__ == '__main__':
    _collection = range(0, 25)
    helper = PaginationHelper(_collection, 10)

    print(helper.page_count())      #, 3, 'page_count is returning incorrect value.')
    print(helper.page_index(11))    #, 2, 'page_index returned incorrect value')
    print(helper.item_count())      #, 24, 'item_count returned incorrect value')
    print(helper.page_item_count(2))
