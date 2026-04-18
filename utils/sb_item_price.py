import requests 
import time

class getitemprice:
    def __init__ (self):
        self.auction_item_list = [
            "Necron's Handle","Dark Claymore",
            "Wither Helmet","Wither Chestplate","Wither Leggings","Wither Boots",                # Wither Armors
            "Wither Cloak Sword","Auto Recombobulator"
        ]
        self.bazaar_item_list = [
            "KISMET_FEATHER",
            "IMPLOSION_SCROLL","SHADOW_WARP_SCROLL","WITHER_SHIELD_SCROLL",                                 # F7 High profit Items
            "WITHER_BLOOD","PRECURSOR_GEAR","WITHER_CATALYST",                                              # F7 Low profit Items
            "ENCHANTMENT_ULTIMATE_ONE_FOR_ALL_1",                                         # F7 u-book
            "FIFTH_MASTER_STAR",                                                                            # M7 High profit Item
            "RECOMBOBULATOR_3000","FUMING_POTATO_BOOK","HOT_POTATO_BOOK",                                   # Dungeon Low profit Items
            "ENCHANTMENT_REJUVENATE_1","ENCHANTMENT_REJUVENATE_2","ENCHANTMENT_REJUVENATE_3",               # Dungeon Low profit e-Books
            "ENCHANTMENT_INFINITE_QUIVER_6","ENCHANTMENT_INFINITE_QUIVER_7",
            "ENCHANTMENT_FEATHER_FALLING_6","ENCHANTMENT_FEATHER_FALLING_7"
            "ENCHANTMENT_ULTIMATE_JERRY_1","ENCHANTMENT_ULTIMATE_JERRY_2","ENCHANTMENT_ULTIMATE_JERRY_3",
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1","ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_2",
            "ENCHANTMENT_ULTIMATE_WISDOM_1","ENCHANTMENT_ULTIMATE_WISDOM_2",
            "ENCHANTMENT_ULTIMATE_COMBO_1","ENCHANTMENT_ULTIMATE_COMBO_2",
            "ENCHANTMENT_ULTIMATE_BANK_1","ENCHANTMENT_ULTIMATE_BANK_2","ENCHANTMENT_ULTIMATE_BANK_3",
            "ENCHANTMENT_ULTIMATE_LAST_STAND_1","ENCHANTMENT_ULTIMATE_LAST_STAND_2",
            "ENCHANTMENT_ULTIMATE_WISE_1","ENCHANTMENT_ULTIMATE_WISE_2",
            "ESSENCE_UNDEAD","ESSENCE_WITHER",                                                  # Essences
            ]
        self.bazaar_price = {}
        self.auction_price = {}
        self.merged_result = {}

    def fetch_auction(self):
        auction_lists =[]
        url = "https://api.hypixel.net/v2/skyblock/auctions"
        result = requests.get(url)
        raw_data = result.json()
        
        page = raw_data["totalPages"]
        auction_results = raw_data["auctions"]
        auction_lists.extend(raw_data["auctions"])


        for i in range(0,page): 
            url = f"https://api.hypixel.net/v2/skyblock/auctions?page={i}"
            print(f"進捗:Auction{i + 1}/{page}ページ目が終了") # ほんとは0ページ目から始まるけど、コード書かない人でも進捗をわかりやすくするために+1している　ビジュアルしか変わらない
            result = requests.get(url)
            raw_data = result.json()
            auction_lists.extend(raw_data["auctions"])
        
        for item in self.auction_item_list:
            item_list = [x for x in auction_lists if x["bin"] == True and x["item_name"] == item]
            lowest_price = min(item_list,key = lambda x: x["starting_bid"])
            self.auction_price[item] = lowest_price["starting_bid"]

        return self.auction_price
    

    def fetch_bazaar(self):
        url = "https://api.hypixel.net/v2/skyblock/bazaar"
        result = requests.get(url)
        raw_data = result.json()

        for item in self.bazaar_item_list:
            products = raw_data["products"]
            if item in products and products[item]["buy_summary"]:
                lowest_price = min(products[item]["buy_summary"],key = lambda x: x["pricePerUnit"])
                self.bazaar_price[item] = lowest_price["pricePerUnit"]
            else:
                self.bazaar_price[item] = 0

        return self.bazaar_price
    

def fetch_item_price():
    items = getitemprice()
    bazaar_result = items.fetch_auction()
    auction_result = items.fetch_bazaar()

    item_price = bazaar_result | auction_result

    return (item_price)

