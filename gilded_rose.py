# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def __eq__(self, other):
        return (self.name == other.name and
                self.sell_in == other.sell_in and
                self.quality == other.quality)

# Strategy Interface
class ItemStrategy:
    def update_quality(self, item: Item):
        raise NotImplementedError

# Normal Item Strategy
class NormalItemStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

# Aged Brie Strategy
class AgedBrieStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

# Sulfuras Strategy
class SulfurasStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        # Sulfuras never changes
        pass

# Backstage Passes Strategy
class BackstagePassesStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

# Conjured Item Strategy
class ConjuredItemStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        if item.quality > 0:
            item.quality -= 2
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item)
            strategy.update_quality(item)
    
    def get_strategy(self, item: Item) -> ItemStrategy:
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassesStrategy()
        elif "Conjured" in item.name:
            return ConjuredItemStrategy()
        else:
            return NormalItemStrategy()
