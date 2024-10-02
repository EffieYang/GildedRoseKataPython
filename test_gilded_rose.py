# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
    
        
    def test_conjured_item_degrades_twice_as_fast(self):
        conjured_item = "Conjured Mana Cake"
        items = [Item(conjured_item, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 8)

        
    def test_quality_never_negative_after_sell_by_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(gilded_rose.items[0].sell_in, 0) 
    
    
    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)
        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]


    def test_aged_brie(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(gilded_rose.items[0].quality, 51) 

     
        


if __name__ == '__main__':
    unittest.main()
