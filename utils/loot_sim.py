import random
from sb_item_price import fetch_item_price

class f7:
    def __init__(self):

# ========= Loot Table Data definition ============#

        # Wood chest
        self.wood_weight = {
            "BASE": 118,
            "ENCHANTMENT_ULTIMATE_BANK_1": 20,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 1,
            "ENCHANTMENT_INFINITE_QUIVER_6": 30,
            "ENCHANTMENT_FEATHER_FALLING_6": 35,
            "ENCHANTMENT_REJUVENATE_1": 30,
            "ESSENCE_WITHER": 1,
        }
        self.wood_cost = {
            "ENCHANTMENT_ULTIMATE_BANK_1": 0,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 0,
            "ENCHANTMENT_INFINITE_QUIVER_6": 0,
            "ENCHANTMENT_FEATHER_FALLING_6": 0,
            "ENCHANTMENT_REJUVENATE_1": 0,
            "ESSENCE_WITHER": 0,
        }
        self.wood_quality = {
            "BASE": 125,
            "ENCHANTMENT_ULTIMATE_BANK_1": 100,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 100,
            "ENCHANTMENT_INFINITE_QUIVER_6": 80,
            "ENCHANTMENT_FEATHER_FALLING_6": 80,
            "ENCHANTMENT_REJUVENATE_1": 80,
            "ESSENCE_WITHER": 10,
        }

        # Gold chest
        self.gold_weight = {
            "BASE": 189,
            "Wither Boots": 2,
            "WITHER_CATALYST": 5,
            "HOT_POTATO_BOOK": 5,
            "PRECURSOR_GEAR": 7,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 16,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 16,
            "ENCHANTMENT_ULTIMATE_BANK_1": 15,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 15,
            "ENCHANTMENT_ULTIMATE_WISE_1": 20,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 1,
            "ENCHANTMENT_INFINITE_QUIVER_6": 20,
            "ENCHANTMENT_FEATHER_FALLING_6": 25,
            "ENCHANTMENT_REJUVENATE_1": 40,
            "ESSENCE_WITHER": 1,
            "ESSENCE_UNDEAD": 1,
        }
        self.gold_cost = {
            "Wither Boots": 2500000,
            "WITHER_CATALYST": 1000000,
            "HOT_POTATO_BOOK": 100000,
            "PRECURSOR_GEAR": 500000,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 100000,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 100000,
            "ENCHANTMENT_ULTIMATE_BANK_1": 100000,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 100000,
            "ENCHANTMENT_ULTIMATE_WISE_1": 100000,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 100000,
            "ENCHANTMENT_INFINITE_QUIVER_6": 100000,
            "ENCHANTMENT_FEATHER_FALLING_6": 100000,
            "ENCHANTMENT_REJUVENATE_1": 100000,
            "ESSENCE_WITHER": 100000,
            "ESSENCE_UNDEAD": 100000,
        }
        self.gold_quality = {
            "BASE": 180,
            "Wither Boots": 170,
            "WITHER_CATALYST": 160,
            "HOT_POTATO_BOOK": 160,
            "PRECURSOR_GEAR": 140,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 120,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 120,
            "ENCHANTMENT_ULTIMATE_BANK_1": 100,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 100,
            "ENCHANTMENT_ULTIMATE_WISE_1": 100,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 100,
            "ENCHANTMENT_INFINITE_QUIVER_6": 80,
            "ENCHANTMENT_FEATHER_FALLING_6": 80,
            "ENCHANTMENT_REJUVENATE_1": 80,
            "ESSENCE_WITHER": 10,
            "ESSENCE_UNDEAD": 1,
        }

        # Diamond chest
        self.diamond_weight = {
            "BASE": 193,
            "Wither Helmet": 1,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 2,
            "Wither Boots": 2,
            "WITHER_CATALYST": 5,
            "HOT_POTATO_BOOK": 5,
            "PRECURSOR_GEAR": 8,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 16,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 16,
            "ENCHANTMENT_ULTIMATE_BANK_1": 15,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 15,
            "ENCHANTMENT_ULTIMATE_WISE_1": 20,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 1,
            "ENCHANTMENT_INFINITE_QUIVER_6": 20,
            "ENCHANTMENT_FEATHER_FALLING_6": 25,
            "ENCHANTMENT_REJUVENATE_1": 40,
            "ESSENCE_WITHER": 1,
            "ESSENCE_UNDEAD": 1,
        }
        self.diamond_cost = {
            "Wither Helmet": 4000000,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 1000000,
            "Wither Boots": 2500000,
            "WITHER_CATALYST": 1000000,
            "HOT_POTATO_BOOK": 250000,
            "PRECURSOR_GEAR": 500000,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 250000,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 250000,
            "ENCHANTMENT_ULTIMATE_BANK_1": 250000,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 250000,
            "ENCHANTMENT_ULTIMATE_WISE_1": 250000,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 250000,
            "ENCHANTMENT_INFINITE_QUIVER_6": 250000,
            "ENCHANTMENT_FEATHER_FALLING_6": 250000,
            "ENCHANTMENT_REJUVENATE_1": 250000,
            "ESSENCE_WITHER": 250000,
            "ESSENCE_UNDEAD": 250000,
        }
        self.diamond_quality = {
            "BASE": 220,
            "Wither Helmet": 210,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 180,
            "Wither Boots": 170,
            "WITHER_CATALYST": 160,
            "HOT_POTATO_BOOK": 160,
            "PRECURSOR_GEAR": 140,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 120,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 120,
            "ENCHANTMENT_ULTIMATE_BANK_1": 100,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 100,
            "ENCHANTMENT_ULTIMATE_WISE_1": 100,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 100,
            "ENCHANTMENT_INFINITE_QUIVER_6": 80,
            "ENCHANTMENT_FEATHER_FALLING_6": 80,
            "ENCHANTMENT_REJUVENATE_1": 80,
            "ESSENCE_WITHER": 10,
            "ESSENCE_UNDEAD": 1,
        }

        # Emerald chest
        self.emerald_weight = {
            "BASE": 176,
            "Wither Leggings": 1,
            "Wither Cloak Sword": 1,
            "Wither Helmet": 2,
            "WITHER_BLOOD": 2,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 6,
            "Wither Boots": 4,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 5,
            "WITHER_CATALYST": 5,
            "HOT_POTATO_BOOK": 5,
            "PRECURSOR_GEAR": 7,
            "ENCHANTMENT_INFINITE_QUIVER_6": 16,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 16,
            "ENCHANTMENT_ULTIMATE_BANK_1": 10,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 10,
            "ENCHANTMENT_ULTIMATE_LAST_STAND_1": 10,
            "ENCHANTMENT_ULTIMATE_WISE_1": 20,
            "ENCHANTMENT_FEATHER_FALLING_6": 20,
            "ENCHANTMENT_REJUVENATE_2": 25,
            "ENCHANTMENT_ULTIMATE_JERRY_2": 10,
            "ESSENCE_WITHER": 1,
            "ESSENCE_UNDEAD": 1,
        }
        self.emerald_cost = {
            "Wither Leggings": 6000000,
            "Wither Cloak Sword": 4500000,
            "Wither Helmet": 4000000,
            "WITHER_BLOOD": 2500000,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 1000000,
            "Wither Boots": 2500000,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 500000,
            "WITHER_CATALYST": 1000000,
            "HOT_POTATO_BOOK": 500000,
            "PRECURSOR_GEAR": 500000,
            "ENCHANTMENT_INFINITE_QUIVER_6": 500000,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 500000,
            "ENCHANTMENT_ULTIMATE_BANK_1": 500000,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 500000,
            "ENCHANTMENT_ULTIMATE_LAST_STAND_1": 500000,
            "ENCHANTMENT_ULTIMATE_WISE_1": 500000,
            "ENCHANTMENT_FEATHER_FALLING_6": 500000,
            "ENCHANTMENT_REJUVENATE_2": 500000,
            "ENCHANTMENT_ULTIMATE_JERRY_2": 500000,
            "ESSENCE_WITHER": 500000,
            "ESSENCE_UNDEAD": 500000,
        }
        self.emerald_quality = {
            "BASE": 260,
            "Wither Leggings": 250,
            "Wither Cloak Sword": 230,
            "Wither Helmet": 210,
            "WITHER_BLOOD": 210,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 180,
            "Wither Boots": 170,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 160,
            "WITHER_CATALYST": 160,
            "HOT_POTATO_BOOK": 160,
            "PRECURSOR_GEAR": 140,
            "ENCHANTMENT_INFINITE_QUIVER_6": 120,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 120,
            "ENCHANTMENT_ULTIMATE_BANK_1": 100,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 100,
            "ENCHANTMENT_ULTIMATE_LAST_STAND_1": 100,
            "ENCHANTMENT_ULTIMATE_WISE_1": 100,
            "ENCHANTMENT_FEATHER_FALLING_6": 80,
            "ENCHANTMENT_REJUVENATE_2": 80,
            "ENCHANTMENT_ULTIMATE_JERRY_2": 80,
            "ESSENCE_WITHER": 10,
            "ESSENCE_UNDEAD": 1,
        }

        # Obsidian chest
        self.obsidian_weight = {
            "BASE": 309,
            "Wither Chestplate": 1,
            "ENCHANTMENT_ULTIMATE_ONE_FOR_ALL_1": 1,
            "RECOMBOBULATOR_3000": 2,
            "Wither Leggings": 4,
            "Wither Cloak Sword": 6,
            "Wither Helmet": 6,
            "WITHER_BLOOD": 6,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 14,
            "FUMING_POTATO_BOOK": 14,
            "Wither Boots": 14,
            "WITHER_CATALYST": 14,
            "HOT_POTATO_BOOK": 10,
            "PRECURSOR_GEAR": 16,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 10,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 32,
            "ENCHANTMENT_ULTIMATE_BANK_2": 15,
            "ENCHANTMENT_REJUVENATE_2": 50,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 15,
            "ENCHANTMENT_ULTIMATE_LAST_STAND_1": 30,
            "ENCHANTMENT_ULTIMATE_WISE_1": 40,
            "ENCHANTMENT_ULTIMATE_JERRY_2": 8,
            "ESSENCE_WITHER": 1,
            "ESSENCE_UNDEAD": 1,
        }
        self.obsidian_cost = {
            "Wither Chestplate": 10000000,
            "ENCHANTMENT_ULTIMATE_ONE_FOR_ALL_1": 2000000,
            "RECOMBOBULATOR_3000": 6000000,
            "Wither Leggings": 6000000,
            "Wither Cloak Sword": 4500000,
            "Wither Helmet": 4000000,
            "WITHER_BLOOD": 2500000,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 1000000,
            "FUMING_POTATO_BOOK": 1000000,
            "Wither Boots": 2500000,
            "WITHER_CATALYST": 1000000,
            "HOT_POTATO_BOOK": 1000000,
            "PRECURSOR_GEAR": 1000000,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 1000000,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 1000000,
            "ENCHANTMENT_ULTIMATE_BANK_2": 1000000,
            "ENCHANTMENT_REJUVENATE_2": 1000000,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 1000000,
            "ENCHANTMENT_ULTIMATE_LAST_STAND_1": 1000000,
            "ENCHANTMENT_ULTIMATE_WISE_1": 1000000,
            "ENCHANTMENT_ULTIMATE_JERRY_2": 1000000,
            "ESSENCE_WITHER": 1000000,
            "ESSENCE_UNDEAD": 1000000,
        }
        self.obsidian_quality = {
            "BASE": 330,
            "Wither Chestplate": 310,
            "ENCHANTMENT_ULTIMATE_ONE_FOR_ALL_1": 290,
            "RECOMBOBULATOR_3000": 250,
            "Wither Leggings": 250,
            "Wither Cloak Sword": 230,
            "Wither Helmet": 210,
            "WITHER_BLOOD": 210,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 180,
            "FUMING_POTATO_BOOK": 175,
            "Wither Boots": 170,
            "WITHER_CATALYST": 160,
            "HOT_POTATO_BOOK": 160,
            "PRECURSOR_GEAR": 140,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_1": 120,
            "ENCHANTMENT_ULTIMATE_COMBO_1": 120,
            "ENCHANTMENT_ULTIMATE_BANK_2": 100,
            "ENCHANTMENT_REJUVENATE_2": 100,
            "ENCHANTMENT_ULTIMATE_WISDOM_1": 100,
            "ENCHANTMENT_ULTIMATE_LAST_STAND_1": 100,
            "ENCHANTMENT_ULTIMATE_WISE_1": 100,
            "ENCHANTMENT_ULTIMATE_JERRY_2": 100,
            "ESSENCE_WITHER": 10,
            "ESSENCE_UNDEAD": 1,
        }

        # Bedrock chest
        self.bedrock_weight = {
            "BASE": 13706,
            "Necron's Handle": 15,
            "SHADOW_WARP": 20,
            "WITHER_SHIELD": 20,
            "IMPLOSION": 20,
            "Auto Recombobulator": 80,
            "Wither Chestplate": 80,
            "ENCHANTMENT_ULTIMATE_ONE_FOR_ALL_1": 80,
            "RECOMBOBULATOR_3000": 400,
            "Wither Leggings": 320,
            "Wither Cloak Sword": 480,
            "Wither Helmet": 480,
            "WITHER_BLOOD": 480,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 800,
            "FUMING_POTATO_BOOK": 400,
            "Wither Boots": 480,
            "WITHER_CATALYST": 400,
            "HOT_POTATO_BOOK": 800,
            "PRECURSOR_GEAR": 1200,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_2": 400,
            "ENCHANTMENT_ULTIMATE_COMBO_2": 1000,
            "ENCHANTMENT_REJUVENATE_3": 1000,
            "ENCHANTMENT_ULTIMATE_BANK_3": 500,
            "ENCHANTMENT_ULTIMATE_WISDOM_2": 500,
            "ENCHANTMENT_ULTIMATE_WISE_2": 800,
            "ENCHANTMENT_ULTIMATE_JERRY_3": 600,
            "ENCHANTMENT_ULTIMATE_LAST_STAND_2": 1000,
            "ENCHANTMENT_INFINITE_QUIVER_7": 1000,
            "ENCHANTMENT_FEATHER_FALLING_7": 320,
            "Storm The Fish": 10,
            "Maxor The Fish": 10,
            "Goldor The Fish": 10,
            "ESSENCE_WITHER": 1,
            "ESSENCE_UNDEAD": 0,
        }
        self.bedrock_cost = {
            "Necron's Handle": 100000000,
            "SHADOW_WARP": 50000000,
            "WITHER_SHIELD": 50000000,
            "IMPLOSION": 50000000,
            "Auto Recombobulator": 10000000,
            "Wither Chestplate": 10000000,
            "ENCHANTMENT_ULTIMATE_ONE_FOR_ALL_1": 2000000,
            "RECOMBOBULATOR_3000": 6000000,
            "Wither Leggings": 6000000,
            "Wither Cloak Sword": 4500000,
            "Wither Helmet": 4000000,
            "WITHER_BLOOD": 3000000,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 2000000,
            "FUMING_POTATO_BOOK": 2000000,
            "Wither Boots": 2500000,
            "WITHER_CATALYST": 2000000,
            "HOT_POTATO_BOOK": 2000000,
            "PRECURSOR_GEAR": 2000000,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_2": 2000000,
            "ENCHANTMENT_ULTIMATE_COMBO_2": 2000000,
            "ENCHANTMENT_REJUVENATE_3": 2000000,
            "ENCHANTMENT_ULTIMATE_BANK_3": 2000000,
            "ENCHANTMENT_ULTIMATE_WISDOM_2": 2000000,
            "ENCHANTMENT_ULTIMATE_WISE_2": 2000000,
            "ENCHANTMENT_ULTIMATE_JERRY_3": 2000000,
            "ENCHANTMENT_ULTIMATE_LAST_STAND_2": 2000000,
            "ENCHANTMENT_INFINITE_QUIVER_7": 2000000,
            "ENCHANTMENT_FEATHER_FALLING_7": 2000000,
            "Storm The Fish": 2000000,
            "Maxor The Fish": 2000000,
            "Goldor The Fish": 2000000,
            "ESSENCE_WITHER": 2000000,
            "ESSENCE_UNDEAD": 2000000,
        }
        self.bedrock_quality = {
            "BASE": 389,
            "Necron's Handle": 360,
            "SHADOW_WARP": 350,
            "WITHER_SHIELD": 350,
            "IMPLOSION": 350,
            "Auto Recombobulator": 330,
            "Wither Chestplate": 310,
            "ENCHANTMENT_ULTIMATE_ONE_FOR_ALL_1": 290,
            "RECOMBOBULATOR_3000": 250,
            "Wither Leggings": 250,
            "Wither Cloak Sword": 230,
            "Wither Helmet": 210,
            "WITHER_BLOOD": 210,
            "ENCHANTMENT_ULTIMATE_SOUL_EATER_1": 180,
            "FUMING_POTATO_BOOK": 175,
            "Wither Boots": 170,
            "WITHER_CATALYST": 160,
            "HOT_POTATO_BOOK": 160,
            "PRECURSOR_GEAR": 140,
            "ENCHANTMENT_ULTIMATE_NO_PAIN_NO_GAIN_2": 120,
            "ENCHANTMENT_ULTIMATE_COMBO_2": 120,
            "ENCHANTMENT_REJUVENATE_3": 100,
            "ENCHANTMENT_ULTIMATE_BANK_3": 100,
            "ENCHANTMENT_ULTIMATE_WISDOM_2": 100,
            "ENCHANTMENT_ULTIMATE_WISE_2": 100,
            "ENCHANTMENT_ULTIMATE_JERRY_3": 100,
            "ENCHANTMENT_ULTIMATE_LAST_STAND_2": 100,
            "ENCHANTMENT_INFINITE_QUIVER_7": 80,
            "ENCHANTMENT_FEATHER_FALLING_7": 80,
            "Storm The Fish": 61,
            "Maxor The Fish": 61,
            "Goldor The Fish": 61,
            "ESSENCE_WITHER": 10,
            "ESSENCE_UNDEAD": 1,
        }
        self.duplicatable = {
            "ESSENCE_WITHER",
            "ESSENCE_UNDEAD"
        }
# ========= end of Loot Table Data definition ============#

# ========= loot roll logic ==========
    def roll_loot(self):
        
        remaining_weight = self.bedrock_weight["BASE"]
        remaining_quality = self.bedrock_quality["BASE"] #(f7 bedrockなら389になるはず)
        loot_list = list(self.bedrock_weight.keys())
        loot_quality = list(self.bedrock_quality.values())
        loot_weight = list(self.bedrock_weight.values())
        
        print(f"base_quality : {loot_quality[0]}")
        print(f"base_weight  : {loot_weight[0]}")
        
        # print (sum(loot_weight[1:]))
        rolled_loots = []
        obtained_items = []

        while remaining_quality > 0:
            roll_flag = False
            
            attempts = 1
            remaining_weight = self.bedrock_weight["BASE"]
            
            
            while roll_flag is False:
                rolled_number = random.randint(0,remaining_weight)
            
                print(f"rolled_number : {rolled_number}")
                print(f"loot_weight   : {loot_weight[attempts]} \n")

                if loot_list[attempts] not in self.duplicatable and loot_list[attempts] in obtained_items:
                    remaining_weight -= loot_weight[attempts]
                    attempts += 1
                    continue

                # rollされた番号がattmpts番目のloot_weightより小さいかつremaining_qualityよりloot_qualityが小さいなら当選
                if rolled_number <= loot_weight[attempts] and loot_quality[attempts] <= remaining_quality:
                    
                    item_name = loot_list[attempts]

                    if item_name not in self.duplicatable:
                        obtained_items.append(loot_list[attempts])

                    print(f"rolled_number : {rolled_number}!")
                    print(f"loot_weight   : {loot_weight[attempts]}!")
                    
                    print(f"\n===========================================\n"
                            +f"{loot_list[attempts]} got rolled! GG!\n"
                            +f"{loot_list[attempts]}'s quality : {loot_quality[attempts]}\n"
                            +"===========================================\n"
                        )
                    
                    remaining_quality = remaining_quality - loot_quality[attempts]
                    print(f"Current remaining_quality:{remaining_quality} \n")
    
                    roll_flag = True
                    rolled_loots.append(loot_list[attempts])
    
                else:
                    print(attempts)
                    # print(f"==============================================\n'{loot_list[attempts]}' didn't get rolled!")
                    remaining_weight = remaining_weight - loot_weight[attempts]
                    # print (f"remaining_weight {remaining_weight}\n==============================================\n")
                    attempts = attempts + 1
    
        total_quality = 0
        print(f"{rolled_loots}\n")
        print("==============================================")
        for rolled_loot in rolled_loots:
            print(f"{rolled_loot}(Quality:{self.bedrock_quality[rolled_loot]})")
            total_quality = total_quality + self.bedrock_quality[rolled_loot]
    
        quality_diff = total_quality - loot_quality[0]
        print (f"\ntotal_quality:{total_quality}\nBase_quality :{loot_quality[0]}\nquality_diff:{quality_diff}")
        print("==============================================")
        
        return rolled_loots
# ========== End of loot roll logic ==========    

# ========== pricing logic ==========
    def get_item_price(self):
        
        item_price = fetch_item_price()
        return item_price
# ========== end of pricing logic ==========


# ========== Calculate chest value logic ==========
    def calculate_chest_profit(self):
        rolled_loots = self.roll_loot()
        item_price = self.get_item_price()
        open_cost = self.bedrock_cost


        total_value = 0
        max_cost = 0


        for loot in rolled_loots:
            price = item_price.get(loot,0)
            cost = open_cost.get(loot,0)


            total_value += price
            if cost >= max_cost:
                max_cost = cost
       
        profit = total_value - max_cost
        print(rolled_loots)
        print(total_value)
        print(f"Profit:{profit} coins")


f = f7()
f.calculate_chest_profit()