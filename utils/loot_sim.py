import random
from sb_item_price import fetch_item_price

class f7:
    def __init__(self):

# ========= Loot Table Data definition ============

        # Wood chest
        self.wood_weight = {
            "BASE": 118,
            "ENCHANTMENT_ULTIMATE_BANK_1": 20,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 1,
            "ENCHANTMENT_INFINITE_QUIVER_6": 30,
            "ENCHANTMENT_FEATHER_FALLING_6": 35,
            "ENCHANTMENT_REJUVENATE_1": 30,
            "ESSENCE_WITHER": 1,
            "ESSENCE_UNDEAD": 1
        }
        self.wood_cost = {
            "ENCHANTMENT_ULTIMATE_BANK_1": 0,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 0,
            "ENCHANTMENT_INFINITE_QUIVER_6": 0,
            "ENCHANTMENT_FEATHER_FALLING_6": 0,
            "ENCHANTMENT_REJUVENATE_1": 0,
            "ESSENCE_WITHER": 0
        }
        self.wood_quality = {
            "BASE": 125,
            "ENCHANTMENT_ULTIMATE_BANK_1": 100,
            "ENCHANTMENT_ULTIMATE_JERRY_1": 100,
            "ENCHANTMENT_INFINITE_QUIVER_6": 80,
            "ENCHANTMENT_FEATHER_FALLING_6": 80,
            "ENCHANTMENT_REJUVENATE_1": 80,
            "ESSENCE_WITHER": 10,
            "ESSENCE_UNDEAD": 1
            
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

        self.chest_tables = {
            "wood": {
                "weight": self.wood_weight,
                "quality": self.wood_quality,
                "cost": self.wood_cost,
            },
            "gold": {
                "weight": self.gold_weight,
                "quality": self.gold_quality,
                "cost": self.gold_cost,
            },
            "diamond": {
                "weight": self.diamond_weight,
                "quality": self.diamond_quality,
                "cost": self.diamond_cost,
            },
            "emerald": {
                "weight": self.emerald_weight,
                "quality": self.emerald_quality,
                "cost": self.emerald_cost,
            },
            "obsidian": {
                "weight": self.obsidian_weight,
                "quality": self.obsidian_quality,
                "cost": self.obsidian_cost,
            },
            "bedrock": {
                "weight": self.bedrock_weight,
                "quality": self.bedrock_quality,
                "cost": self.bedrock_cost,
            }
        }

# ========= end of Loot Table Data definition ============

    def chest_converter(self, chest_type: str):
        tables = self.chest_tables.get(chest_type)

        if tables is None:
            print("An Error occurred:Unknown chest type")
            return None
        
        return tables["weight"],tables["quality"],tables["cost"]
# ========= loot roll logic ==========
    def roll_loot(self,weight,quality):
        chest_weight = weight
        chest_quality = quality

        # ぱっと見まどろっこしいけど、後でこのweightとqualityをいじるのでchestのweightとqualityを入れておかないといけない
        remaining_weight = chest_weight["BASE"]
        remaining_quality = chest_quality["BASE"]

        loot_list = list(chest_weight.keys())
        loot_quality = list(chest_quality.values())
        loot_weight = list(chest_weight.values())

        # print(f"base_quality : {loot_quality[0]}")
        # print(f"base_weight  : {loot_weight[0]}")
        # print (sum(loot_weight[1:]))

        rolled_loots = []
        obtained_items = []
        while remaining_quality > 0:

            roll_flag = False
            # loot_listを見るとわかるが、listの(0)にはchestのbase_weightが記載されているため、0ではなく1から始めなければならない
            attempts = 1
            remaining_weight = loot_weight[0]
            # print(remaining_weight)

            # このコードベースでは、抽選の方法として規定値(weight)よりランダムで選ばれた数字が小さければ当選として扱う
            # lootが当選するとroll_flagがTrueになって残りのweight分に入るようなアイテムを探しに行く
            while roll_flag is False:
                
                rolled_number = random.randint(0,remaining_weight)
                # その試行で抽選されたアイテム、番号の可視化　デバッグ用なので完成したら消して問題ない
                # print(f"rolled_number : {rolled_number}")
                # print(f"loot_weight   : {loot_weight[attempts]} \n")

                # remaining_weight は「まだ候補として残っているアイテムの重みの合計」を表す。
                # 1回の抽選ごとに 0〜remaining_weight の範囲で乱数を振り、
                # 各アイテムの重みを順番に引いていくことで、
                # 「重みが大きいアイテムほど当たりやすい」ようにしている。
                #
                # 具体的には：  
                #   1. 最初に total_weight（ここでは BASE）を remaining_weight に入れておく。
                #   2. 乱数 rolled_number を 0〜remaining_weight で1回だけ生成する。
                #   3. アイテムを先頭から見ていき、外れたアイテムの重みを remaining_weight から引く。
                #      → これは「このアイテムの分の範囲はもう使い切った」という意味。
                #   4. こうして「残りの重み」だけを対象にしながら次のアイテムを判定することで、
                #      結果として重みに比例した確率でどれか1つが当たる。
                #
                # もし remaining_weight を減らさないと、
                # 「もう通り過ぎたアイテムの重み」を何度も混ぜて計算してしまい、
                # 実際の重みと違う確率になってしまう。

                # attempts は「現在の候補アイテムの位置」。
                # このアイテムを見終わったら、次の候補を調べるために attempts を 1 増やす。
                # これをしないと、同じアイテムだけを延々と判定することになってしまう。
                # (i hope it's not just an AI slop)
                if loot_list[attempts] not in self.duplicatable and loot_list[attempts] in obtained_items:
                    remaining_weight =  remaining_weight - loot_weight[attempts]
                    attempts += 1
                    continue 

                # rollされた番号がattmpts番目のloot_weightより小さいかつremaining_qualityよりloot_qualityが小さいなら当選
                if rolled_number <= loot_weight[attempts] and loot_quality[attempts] <= remaining_quality:
        
                    item_name = loot_list[attempts]

                    if item_name not in self.duplicatable:
                        obtained_items.append(loot_list[attempts])

                    # print(f"rolled_number : {rolled_number}!")
                    # print(f"loot_weight   : {loot_weight[attempts]}!")
              

                    # print(f"\n===========================================\n"
                    #       +f"{loot_list[attempts]} got rolled! GG!\n"
                    #       +f"{loot_list[attempts]}'s quality : {loot_quality[attempts]}\n"
                    #       +"===========================================\n"
                    #   )

                    remaining_quality = remaining_quality - loot_quality[attempts]
                    # print(f"Current remaining_quality:{remaining_quality} \n")
              

                    roll_flag = True
                    rolled_loots.append(loot_list[attempts])
              
                # 抽選されたitemがrollされなかったら、残りのweightから今回抽選されたアイテムのweightを引く
                # こうすれば同じアイテムをrollし続けることがなくなる
                else:
                    # print(attempts)
                    # print(f"==============================================\n'{loot_list[attempts]}' didn't get rolled!")
                    remaining_weight = remaining_weight - loot_weight[attempts]
                    # print (f"remaining_weight:{remaining_weight}\n==============================================\n")
                    attempts = attempts + 1


        total_quality = 0
        print(f"{rolled_loots}\n")
        print("==============================================")

        for rolled_loot in rolled_loots:
            print(f"{rolled_loot}(Quality:{chest_quality[rolled_loot]})")
            total_quality = total_quality + chest_quality[rolled_loot]

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

    def calculate_chest_profit(self,item_price,loot_cost,loots):
        # 参照するitemの値段のdict
        all_item_price = item_price
        # 参照するchestの開封コストのdict
        item_open_cost = loot_cost
        # roll_loot関数で抽選されたlootのリスト
        rolled_loots = loots

        print(f"item_price:{all_item_price}")
        print(f"open_cost:{item_open_cost}")
        print(f"rolled_loots:{rolled_loots}")
        
        total_value = 0
        chest_value = 0
        max_cost = 0

        for loot in rolled_loots:
            price = all_item_price.get(loot,0)
            cost = item_open_cost.get(loot,0)

            chest_value += price
            if cost>=max_cost:
                max_cost = cost
        
        profit = chest_value - max_cost

        print(rolled_loots)
        print(chest_value)
        print(f"OpenCost:{max_cost}")
        print(f"Profit:{profit:2f} coins")

        return profit
# ========== Calculate chest value logic ==========


if __name__ == "__main__":
    f = f7()
    chest_type = "emerald"
    weight, quality, cost = f.chest_converter(chest_type)
    f.roll_loot(weight, quality)