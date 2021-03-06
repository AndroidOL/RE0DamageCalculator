class Character:
    SKILLTYPE = ["普通攻击", "AP 技能", "SP 技能", "必杀技能"]
    Attack = {
        "基础攻击": 0,
        "伤害加成": 0
    }
    Probability = [0, 0]
    Auxiliary = [150, 1.5]
    AttackValue = [0, 0, 0]
    Skill = {
        "A": {
            "TYPE": 0,
            "NAME": "",
            "LV1": [(0, 0, 0, 0)],
            "LV2": [(0, 0, 0, 0)],
            "LV3": [(0, 0, 0, 0)],
            "LV4": [(0, 0, 0, 0)],
            "LV5": [(0, 0, 0, 0)]
        },
        "AP": {
            "TYPE": 1,
            "NAME": "",
            "LV1": [(0, 0, 0, 0)],
            "LV2": [(0, 0, 0, 0)],
            "LV3": [(0, 0, 0, 0)],
            "LV4": [(0, 0, 0, 0)],
            "LV5": [(0, 0, 0, 0)]
        },
        "SP": {
            "TYPE": 2,
            "NAME": "",
            "LV1": [(0, 0, 0, 0)],
            "LV2": [(0, 0, 0, 0)],
            "LV3": [(0, 0, 0, 0)],
            "LV4": [(0, 0, 0, 0)],
            "LV5": [(0, 0, 0, 0)]
        },
        "B": {
            "TYPE": 3,
            "NAME": "",
            "LV1": [(0, 0, 0, 0)],
            "LV2": [(0, 0, 0, 0)],
            "LV3": [(0, 0, 0, 0)],
            "LV4": [(0, 0, 0, 0)],
            "LV5": [(0, 0, 0, 0)]
        }
    }
    def AttackValues(self, attminV, attmidV, attmaxV):
        self.AttackValue[0] = self.AttackValue[0] + attminV
        self.AttackValue[1] = self.AttackValue[1] + attmidV
        self.AttackValue[2] = self.AttackValue[2] + attmaxV

    def AttackValuesClean(self):
        self.AttackValue[0] = 0
        self.AttackValue[1] = 0
        self.AttackValue[2] = 0

class Emilia(Character):
    CharName = "爱蜜莉雅·朦胧的睡意"
    Skill = {
        # 引动冰雪攻击敌方全体，对目标造成攻击力36%的伤害
        "A": {
            "TYPE": 0,
            "NAME": "冰屑席卷",
            "LV1": [(3, 1, 36, 10)],
            "LV2": [(3, 1, 37, 11)],
            "LV3": [(3, 1, 39, 12)],
            "LV4": [(3, 1, 41, 13)],
            "LV5": [(3, 1, 45, 15)]
        },
        # 对敌方所有目标进行攻击，造成攻击力80%的伤害
        "AP": {
            "TYPE": 1,
            "NAME": "温柔冰花",
            "LV1": [(8, 1, 80, 10)],
            "LV2": [(8, 1, 84, 10)],
            "LV3": [(8, 1, 88, 10)],
            "LV4": [(8, 1, 92, 10)],
            "LV5": [(8, 1, 100, 10)]
        },
        # 与帕克一起对敌方全体造成136%伤害，由所有敌人分摊
        "SP": {
            "TYPE": 2,
            "NAME": "冰冻境地",
            "LV1": [(4, 1, 45.33, 10)],
            "LV2": [(4, 1, 47.33, 10)],
            "LV3": [(4, 1, 49.67, 10)],
            "LV4": [(4, 1, 52, 10)],
            "LV5": [(4, 1, 56.67, 10)]
        },
        # 对敌人全体造成240%伤害
        "B": {
            "TYPE": 3,
            "NAME": "冰冻术(群体)",
            "LV1": [(1, 1, 80, 10)],
            "LV2": [(1, 1, 84, 10)],
            "LV3": [(1, 1, 88, 10)],
            "LV4": [(1, 1, 92, 10)],
            "LV5": [(1, 1, 100, 10)]
        }
    }
    def __init__(self, AttackPower = 1299, AmplifyDamage = 0, Probability = [17, 3], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Ram(Character):
    CharName = "幼年拉姆·纸风车的约定"
    Skill = {
        # 对目标连续释放唤风术，造成攻击力100%的伤害
        "A": {
            "TYPE": 0,
            "NAME": "风的利刃",
            "LV1": [(4, 0, 100, 20)],
            "LV2": [(4, 0, 105, 22)],
            "LV3": [(4, 0, 110, 24)],
            "LV4": [(4, 0, 115, 26)],
            "LV5": [(4, 0, 125, 30)]
        },
        # 对目标呼出烈风，造成攻击力80%的伤害，再对敌人全体造成攻击力108%的伤害
        "AP": {
            "TYPE": 1,
            "NAME": "烈风术",
            "LV1": [(4, 0, 80, 10), (5, 1, 108, 10)],
            "LV2": [(4, 0, 84, 10), (5, 1, 114, 10)],
            "LV3": [(4, 0, 88, 10), (5, 1, 119, 10)],
            "LV4": [(4, 0, 92, 10), (5, 1, 125, 10)],
            "LV5": [(4, 0, 100, 10), (5, 1, 136, 10)]
        },
        # 对接触风障的目标造成伤害，造成攻击力120%的伤害，并使自己获得2层风盾
        "SP": {
            "TYPE": 2,
            "NAME": "暴怒的风障",
            "LV1": [(4, 0, 120, 20)],
            "LV2": [(4, 0, 126, 20)],
            "LV3": [(4, 0, 132, 20)],
            "LV4": [(4, 0, 138, 20)],
            "LV5": [(4, 0, 144, 20)]
        },
        # 召唤巨大的龙卷风将目标卷至空中，造成400%的伤害
        "B": {
            "TYPE": 3,
            "NAME": "独角的宠儿",
            "LV1": [(1, 0, 400, 20)],
            "LV2": [(1, 0, 420, 20)],
            "LV3": [(1, 0, 440, 20)],
            "LV4": [(1, 0, 460, 20)],
            "LV5": [(1, 0, 480, 20)]
        }
    }
    def __init__(self, AttackPower = 1472, AmplifyDamage = 0, Probability = [20, 0], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Crusch(Character):
    CharName = "库珥修·晚宴的女主人"
    Skill = {
        # 剑气犹如细丝般贯穿敌人，对目标单体造成100%攻击力的伤害
        "A": {
            "TYPE": 0,
            "NAME": "剑之絁",
            "LV1": [(1, 0, 100, 0), (4, 0, 100, 20)],
            "LV2": [(1, 0, 100, 0), (4, 0, 105, 22)],
            "LV3": [(1, 0, 100, 0), (4, 0, 110, 24)],
            "LV4": [(1, 0, 100, 0), (4, 0, 115, 26)],
            "LV5": [(1, 0, 100, 0), (4, 0, 125, 30)]
        },
        # 用7段具有自身50%攻击力的剑气攻击敌方
        "AP": {
            "TYPE": 1,
            "NAME": "剑岚之奔流",
            "LV1": [(6, 0, 50 * 6, 0), (2, 0, 100, 0), (1, 1, 50, 10)],
            "LV2": [(6, 0, 52.5 * 6, 0), (2, 0, 100, 0), (1, 1, 52.5, 10)],
            "LV3": [(6, 0, 55 * 6, 0), (2, 0, 100, 0), (1, 1, 55, 10)],
            "LV4": [(6, 0, 57.5 * 6, 0, (2, 0, 100, 0)), (1, 1, 57.5, 10)],
            "LV5": [(6, 0, 62.5 * 6, 0), (2, 0, 100, 0), (1, 1, 62.5, 10)]
        },
        # 剑气化作流星雨坠向敌方全体，对每个敌人皆造成总共120%攻击力的3段伤害。
        "SP": {
            "TYPE": 2,
            "NAME": "流星之剑阵",
            "LV1": [(3, 1, 120, 10), (3, 0, 100, 0)],
            "LV2": [(3, 1, 126, 10), (3, 0, 100, 0)],
            "LV3": [(3, 1, 132, 10), (3, 0, 100, 0)],
            "LV4": [(3, 1, 138, 10), (3, 0, 100, 0)],
            "LV5": [(3, 1, 150, 10), (3, 0, 100, 0)]
        },
        # 与威尔海姆合力施展华丽的超绝剑之絁，对目标单体造成300%攻击力的伤害
        "B": {
            "TYPE": 3,
            "NAME": "苍华·剑之絁",
            "LV1": [(1, 0, 300, 20)],
            "LV2": [(1, 0, 315, 20)],
            "LV3": [(1, 0, 330, 20)],
            "LV4": [(1, 0, 345, 20)],
            "LV5": [(1, 0, 360, 20)]
        }
    }
    def __init__(self, AttackPower = 1299, AmplifyDamage = 0, Probability = [17, 3], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Felt(Character):
    CharName = "菲鲁特·偷窃徽章"
    Skill = {
        # 闪身到目标背后进行一次攻击
        "A": {
            "TYPE": 0,
            "NAME": "突袭",
            "LV1": [(1, 0, 100, 20)],
            "LV2": [(1, 0, 105, 22)],
            "LV3": [(1, 0, 110, 24)],
            "LV4": [(1, 0, 115, 26)],
            "LV5": [(1, 0, 125, 30)]
        },
        # 攻击目标3次造成200%的伤害
        "AP": {
            "TYPE": 1,
            "NAME": "金色刀锋",
            "LV1": [(3, 0, 200, 20)],
            "LV2": [(3, 0, 210, 20)],
            "LV3": [(3, 0, 220, 20)],
            "LV4": [(3, 0, 230, 20)],
            "LV5": [(3, 0, 250, 20)]
        },
        # 瞬移到目标身边，对目标造成120%攻击的伤害
        "SP": {
            "TYPE": 2,
            "NAME": "快腿",
            "LV1": [(2, 0, 120, 20)],
            "LV2": [(2, 0, 126, 20)],
            "LV3": [(2, 0, 132, 20)],
            "LV4": [(2, 0, 138, 20)],
            "LV5": [(2, 0, 138, 20)]
        },
        # 对目标进行攻击造成360%的伤害
        "B": {
            "TYPE": 3,
            "NAME": "疾风",
            "LV1": [(1, 0, 360, 20)],
            "LV2": [(1, 0, 378, 20)],
            "LV3": [(1, 0, 396, 20)],
            "LV4": [(1, 0, 414, 20)],
            "LV5": [(1, 0, 450, 20)]
        }
    }
    def __init__(self, AttackPower = 1229, AmplifyDamage = 0, Probability = [14, 2], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Rem(Character):
    CharName = "雷姆·失控的鬼"
    Skill = {
        # 以自身15%当前生命值为代价，对目标进行一次重锤，造成120%的伤害
        "A": {
            "TYPE": 0,
            "NAME": "重锤",
            "LV1": [(1, 0, 120, 20)],
            "LV2": [(1, 0, 126, 22)],
            "LV3": [(1, 0, 132, 24)],
            "LV4": [(1, 0, 138, 26)],
            "LV5": [(1, 0, 150, 30)]
        },
        # 以自身25%当前生命为代价，对目标展开疯狂攻击，对目标造成攻击力300%的伤害
        "AP": {
            "TYPE": 1,
            "NAME": "疯狂",
            "LV1": [(4, 0, 300, 20)],
            "LV2": [(4, 0, 315, 20)],
            "LV3": [(4, 0, 330, 20)],
            "LV4": [(4, 0, 345, 20)],
            "LV5": [(4, 0, 375, 20)]
        },
        # 以自身20%当前生命为代价，使用冰锥对目标造成攻击力160%的伤害
        "SP": {
            "TYPE": 2,
            "NAME": "迷失的冰锥",
            "LV1": [(3, 0, 160, 20)],
            "LV2": [(3, 0, 168, 20)],
            "LV3": [(3, 0, 176, 20)],
            "LV4": [(3, 0, 184, 20)],
            "LV5": [(3, 0, 200, 20)]
        },
        # 拼尽自身全力的一击，以自身50%当前生命为代价，对目标造成520%的伤害，如果击杀了目标，则剩余敌人都会受到溢出伤害量100%的伤害
        "B": {
            "TYPE": 3,
            "NAME": "恶鬼",
            "LV1": [(1, 0, 520, 20)],
            "LV2": [(1, 0, 546, 20)],
            "LV3": [(1, 0, 572, 20)],
            "LV4": [(1, 0, 598, 20)],
            "LV5": [(1, 0, 650, 20)]
        }
    }
    def __init__(self, AttackPower = 1229, AmplifyDamage = 0, Probability = [14, 2], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Julius(Character):
    CharName = "由里乌斯·王国之剑"
    Skill = {
        # 冲向目标，对目标进行快速的剑击连斩，造成攻击力60%的伤害
        "A": {
            "TYPE": 0,
            "NAME": "正面疾袭",
            "LV1": [(6, 0, 60, 20)],
            "LV2": [(6, 0, 63, 22)],
            "LV3": [(6, 0, 66, 24)],
            "LV4": [(6, 0, 69, 26)],
            "LV5": [(6, 0, 75, 30)]
        },
        # 在空中施展多段剑击，对目标造成6段总计300%攻击力的伤害
        "AP": {
            "TYPE": 1,
            "NAME": "优雅的绝杀",
            "LV1": [(6, 0, 300, 10), (2, 0, 80, 10)],
            "LV2": [(6, 0, 315, 10), (2, 0, 84, 10)],
            "LV3": [(6, 0, 330, 10), (2, 0, 88, 10)],
            "LV4": [(6, 0, 345, 10), (2, 0, 92, 10)],
            "LV5": [(6, 0, 375, 10), (2, 0, 100, 10)]
        },
        # 蓄力对目标进行多道剑气攻击，对目标造成攻击力100%的伤害
        "SP": {
            "TYPE": 2,
            "NAME": "王国之剑",
            "LV1": [(4, 0, 100, 20)],
            "LV2": [(4, 0, 105, 20)],
            "LV3": [(4, 0, 110, 20)],
            "LV4": [(4, 0, 115, 20)],
            "LV5": [(4, 0, 115, 20)]
        },
        # 对目标造成400%的伤害，自身每存在一个微精灵，则无视目标8%的防御
        "B": {
            "TYPE": 3,
            "NAME": "大聚灵斩",
            "LV1": [(1, 0, 400, 20)],
            "LV2": [(1, 0, 420, 20)],
            "LV3": [(1, 0, 440, 20)],
            "LV4": [(1, 0, 460, 20)],
            "LV5": [(1, 0, 500, 20)]
        }
    }
    def __init__(self, AttackPower = 1417, AmplifyDamage = 0, Probability = [18, 2], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Elsa(Character):
    CharName = "艾尔莎·诱惑的回眸"
    Skill = {
        # 对目标造成80%的伤害
        "A": {
            "TYPE": 0,
            "NAME": "猎肠",
            "LV1": [(3, 0, 80, 20)],
            "LV2": [(3, 0, 84, 22)],
            "LV3": [(3, 0, 88, 24)],
            "LV4": [(3, 0, 92, 26)],
            "LV5": [(3, 0, 92, 30)]
        },
        # 在目标周身范围内进行4次连续攻击造成总计100%的伤害
        "AP": {
            "TYPE": 1,
            "NAME": "共舞",
            "LV1": [(4, 0, 100, 20)],
            "LV2": [(4, 0, 105, 20)],
            "LV3": [(4, 0, 110, 20)],
            "LV4": [(4, 0, 115, 20)],
            "LV5": [(4, 0, 125, 20)]
        },
        # 对全体目标进行8次快速攻击造成总计65%的伤害
        "SP": {
            "TYPE": 2,
            "NAME": "斩击盛宴",
            "LV1": [(8, 1, 21.67, 10)],
            "LV2": [(8, 1, 22.67, 10)],
            "LV3": [(8, 1, 22.67, 10)],
            "LV4": [(8, 1, 23.67, 10)],
            "LV5": [(8, 1, 24.67, 10)]
        },
        # 对目标造成400%的伤害，自身每存在一个微精灵，则无视目标8%的防御
        "B": {
            "TYPE": 3,
            "NAME": "猎肠者的做法",
            "LV1": [(1, 0, 360, 20)],
            "LV2": [(1, 0, 378, 20)],
            "LV3": [(1, 0, 396, 20)],
            "LV4": [(1, 0, 414, 20)],
            "LV5": [(1, 0, 450, 20)]
        }
    }
    def __init__(self, AttackPower = 1431, AmplifyDamage = 0, Probability = [17, 3], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Betelgeuse(Character):
    CharName = "怠惰·疯狂的信仰"
    Skill = {
        # 使用无形之手连续攻击选中目标，对目标造成攻击力100%的伤害
        "A": {
            "TYPE": 0,
            "NAME": "假意倾听",
            "LV1": [(6, 0, 100, 20)],
            "LV2": [(6, 0, 105, 22)],
            "LV3": [(6, 0, 110, 24)],
            "LV4": [(6, 0, 115, 26)],
            "LV5": [(6, 0, 125, 30)]
        },
        # 使用无形之手连续攻击选中目标，对目标造成攻击力120%的伤害
        "AP": {
            "TYPE": 1,
            "NAME": "癫狂怒吼",
            "LV1": [(3, 0, 120, 20)],
            "LV2": [(3, 0, 126, 20)],
            "LV3": [(3, 0, 132, 20)],
            "LV4": [(3, 0, 138, 20)],
            "LV5": [(3, 0, 144, 20)]
        },
        # 咬手指并损失20%当前生命，然后使用无形之手攻击全体目标造成攻击力100%的伤害
        "SP": {
            "TYPE": 2,
            "NAME": "狂人啃食",
            "LV1": [(3, 1, 33.33, 10)],
            "LV2": [(3, 1, 35, 10)],
            "LV3": [(3, 1, 35, 10)],
            "LV4": [(3, 1, 36.67, 10)],
            "LV5": [(3, 1, 38.33, 10)]
        },
        # 使用无形之手攻击全体目标，对目标造成攻击力160%的伤害
        "B": {
            "TYPE": 3,
            "NAME": "不可视之手",
            "LV1": [(1, 1, 160, 10)],
            "LV2": [(1, 1, 168, 10)],
            "LV3": [(1, 1, 176, 10)],
            "LV4": [(1, 1, 184, 10)],
            "LV5": [(1, 1, 192, 10)]
        }
    }
    def __init__(self, AttackPower = 1410, AmplifyDamage = 0, Probability = [15, 5], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Rozuwaru(Character):
    CharName = "罗兹瓦尔·夜阑已至"
    Skill = {
        # 使用2段风属性和1段火属性魔法攻击目标造成攻击力100%的伤害
        "A": {
            "TYPE": 0,
            "NAME": "刃风烈火",
            "LV1": [(3, 0, 100, 40)],
            "LV2": [(3, 0, 105, 42)],
            "LV3": [(3, 0, 110, 44)],
            "LV4": [(3, 0, 115, 46)],
            "LV5": [(3, 0, 125, 50)]
        },
        # 使用1段地属性和4段水属性魔法攻击目标造成共计150%攻击力的伤害，并使目标浮空
        "AP": {
            "TYPE": 1,
            "NAME": "魔导马戏",
            "LV1": [(5, 0, 150, 60)],
            "LV2": [(5, 0, 157, 60)],
            "LV3": [(5, 0, 165, 60)],
            "LV4": [(5, 0, 172, 60)],
            "LV5": [(5, 0, 180, 60)]
        },
        # 对敌方所有目标进行1段大火球攻击，造成攻击力120%的伤害
        "SP": {
            "TYPE": 2,
            "NAME": "赤焰滔天",
            "LV1": [(1, 1, 40, 10)],
            "LV2": [(1, 1, 42, 10)],
            "LV3": [(1, 1, 44, 10)],
            "LV4": [(1, 1, 46, 10)],
            "LV5": [(1, 1, 50, 10)]
        },
        # 罗兹瓦尔对全体敌方目标造成攻击力360%的伤害，由所有敌人分担
        "B": {
            "TYPE": 3,
            "NAME": "炎爆术",
            "LV1": [(1, 1, 120, 10)],
            "LV2": [(1, 1, 126, 10)],
            "LV3": [(1, 1, 132, 10)],
            "LV4": [(1, 1, 138, 10)],
            "LV5": [(1, 1, 150, 10)]
        }
    }
    def __init__(self, AttackPower = 1424, AmplifyDamage = 0, Probability = [5, 15], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Reinhard(Character):
    CharName = "莱因哈鲁特·工作闲暇"
    Skill = {
        # 在目标近前进行斩击体术的混合攻击造成攻击力100%的伤害
        "A": {
            "TYPE": 0,
            "NAME": "骑士讨伐",
            "LV1": [(1, 0, 100, 20)],
            "LV2": [(1, 0, 105, 22)],
            "LV3": [(1, 0, 110, 24)],
            "LV4": [(1, 0, 115, 26)],
            "LV5": [(1, 0, 125, 30)]
        },
        # 敌人全体造成攻击力120%的伤害，对选中的目标造成双倍伤害
        "AP": {
            "TYPE": 1,
            "NAME": "龙剑的裁决",
            "LV1": [(1, 1, 160, 10)],
            "LV2": [(1, 1, 168, 10)],
            "LV3": [(1, 1, 176, 10)],
            "LV4": [(1, 1, 184, 10)],
            "LV5": [(1, 1, 216, 10)]
        },
        # 使用佩剑对目标进行连续的3次斩击造成攻击力195%的伤害
        "SP": {
            "TYPE": 2,
            "NAME": "正义的审判",
            "LV1": [(1, 0, 40, 10)],
            "LV2": [(1, 0, 42, 10)],
            "LV3": [(1, 0, 44, 10)],
            "LV4": [(1, 0, 46, 10)],
            "LV5": [(1, 0, 50, 10)]
        },
        # 强力的挥击对目标造成攻击力575%的伤害，由所有敌人分摊
        "B": {
            "TYPE": 3,
            "NAME": "阿斯特雷亚家的剑击",
            "LV1": [(1, 1, 191.67, 10)],
            "LV2": [(1, 1, 201, 10)],
            "LV3": [(1, 1, 210.67, 10)],
            "LV4": [(1, 1, 220.33, 10)],
            "LV5": [(1, 1, 239.33, 10)]
        }
    }
    def __init__(self, AttackPower = 1438, AmplifyDamage = 0, Probability = [10, 10], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Wilhelm(Character):
    CharName = "青年威尔海姆·挥剑练习"
    Skill = {
        # 在目标身前进行多段斩击，造成100%攻击力的伤害
        "A": {
            "TYPE": 0,
            "NAME": "剑锋",
            "LV1": [(1, 0, 100, 20)],
            "LV2": [(1, 0, 105, 22)],
            "LV3": [(1, 0, 110, 24)],
            "LV4": [(1, 0, 115, 26)],
            "LV5": [(1, 0, 125, 30)]
        },
        # 冰冷的剑刃对敌方全体造成145%攻击力的伤害
        "AP": {
            "TYPE": 1,
            "NAME": "冰冷剑刃",
            "LV1": [(1, 0, 145, 10)],
            "LV2": [(1, 0, 152, 10)],
            "LV3": [(1, 0, 159, 10)],
            "LV4": [(1, 0, 166, 10)],
            "LV5": [(1, 0, 181, 10)]
        },
        # 用自己纯熟的剑技对敌方单体造成145%攻击力的伤害
        "SP": {
            "TYPE": 2,
            "NAME": "剑之巅峰者",
            "LV1": [(1, 0, 145, 20)],
            "LV2": [(1, 0, 152, 20)],
            "LV3": [(1, 0, 159, 20)],
            "LV4": [(1, 0, 166, 20)],
            "LV5": [(1, 0, 181, 20)]
        },
        # 为了守护而挥动的剑对敌人造成480%攻击力的伤害
        "B": {
            "TYPE": 3,
            "NAME": "挥剑的意义",
            "LV1": [(1, 0, 480, 20)],
            "LV2": [(1, 0, 504, 20)],
            "LV3": [(1, 0, 528, 20)],
            "LV4": [(1, 0, 552, 20)],
            "LV5": [(1, 0, 600, 20)]
        }
    }
    def __init__(self, AttackPower = 1465, AmplifyDamage = 0, Probability = [1, 19], Auxiliary = [15, 150]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

class Monster:
    Def = 0
    def __init__(self, Def = 375, Buff = 1):
        self.Def = Def * Buff

fact = lambda n: [1, 0][n > 1] or fact(n - 1) * n
power = lambda num, n: [1, 0][n > 0] or power(num, n - 1) * num
round_up = lambda num: round(num * 100) / 100.0

def MaxCount(problist, CalcMode):
    n = []
    tmp = sorted(problist, key = lambda i:i["暴击概率" if CalcMode else "连击概率"])
    i = 3 if len(tmp) - 1 > 3 else len(tmp) - 1
    for x in tmp[-i:]:
        if (x["暴击概率" if CalcMode else "连击概率"] > 0):
            n.append([x["发生次数"], x["暴击概率" if CalcMode else "连击概率"]])
    return n

def attmin(List, index = 0):
    tmp = sorted(List, key = lambda l:l[index])
    return tmp[0][index]

def attmid(List):
    Total = 0
    TotalProb = 0
    for l in List:
        Total = Total + l[0] * l[1]
        TotalProb = TotalProb + l[1]
    return Total * (100 / TotalProb) / 100

def attmax(List, index = 0):
    tmp = sorted(List, key = lambda l:l[index])
    return tmp[-1][index]

def Analyse(List):
    maxV = 0
    skillVL = []
    for l in List:
        maxV = maxV if maxV > attmax(l, 2) else attmax(l, 2)
    for l in List:
        skillV = []
        for skill in l:
            if (skill[2] > maxV - 10):
                skillV.append(skill)
        if (len(skillV)):
            skillVL.append(skillV)

    minatt, midatt, maxatt = 0, 0, 0
    for skill in skillVL:
        minatt = minatt + attmin(skill)
        midatt = midatt + attmid(skill)
        maxatt = maxatt + attmax(skill)
    # attmin(skillV), attmid(skillV), attmax(skillV)
    if (len(skillVL)):
        return int(minatt / len(skillVL)), int(midatt / len(skillVL)), int(maxatt / len(skillVL))
    return 0, 0, 0

'''
    AttackList - 技能总数据
        AttackInfo - 技能分段信息
        AttackInfo[0] - 技能攻击次数
        AttackInfo[1] - 是否群体技能
        AttackInfo[2] - 技能伤害比例
    eu - 角色攻击属性
        AttackV[0] - 基础攻击
        AttackV[1] - 伤害加成
    Probability - 概率
        Probability[0] - 连击概率
        Probability[1] - 暴击概率
    Auxiliary - 攻击辅正（连击115%或暴击150%的超出部分）
    Deviation - 范围偏差（0.2大范围至0.8普遍）
    # CalcMode - 连击(0)或暴击(1)计算
''' 
def SkillDamage(AttackList, CharCard, SkillUp = 0, Combo = 100, MonsterList = [Monster(375)] * 3, Deviation = 0.2):
    Skill = []
    CurrentCombo = 0
    DefDePercent = 0
    AttackV = CharCard.Attack
    Probability = CharCard.Probability
    Auxiliary = CharCard.Auxiliary
    if (len(MonsterList)):
        DefPercent = 0
        for Monster in MonsterList:
            DefPercent = DefPercent + 375 / (375 + Monster.Def)
        DefDePercent = DefPercent / len(MonsterList)
    else:
        DefDePercent = 0.5
    # 拆分伤害概率
    Probability_EXT = Probability[0]
    Probability_CRT = Probability[1]
    # 拆分伤害辅正
    Auxiliary_EXT = Auxiliary[0]
    Auxiliary_CRT = Auxiliary[1]
    # 概率溢出作废
    # Probability = 1 if Probability > 1 else Probability
    Probability_EXT = (Probability_EXT > 100 and 100 or Probability_EXT)
    Probability_CRT = (Probability_CRT > 100 and 100 or Probability_CRT)
    CalcMode = Probability_EXT > Probability_CRT
    HeppenProbabilityThreshold_EXT = []
    HeppenProbabilityThreshold_CRT = []
    HeppenProbabilityThresholdList_EXT = []
    HeppenProbabilityThresholdList_CRT = []

    for AttackInfo in AttackList:
        LList = []
        HeppenProbabilityList_EXT = []
        HeppenProbabilityList_CRT = []
        Attacks = AttackInfo[0] * len(MonsterList) if AttackInfo[1] else AttackInfo[0]
        HeppenProbabilityMax_EXT = 0
        HeppenProbabilityMax_CRT = 0
        # 该段技能结束后增加连携加成
        CurrentCombo = CurrentCombo + AttackInfo[3]
        for times in range(0, Attacks + 1):
            L = dict()
            # 计算组合次数
            # C time Attacks
            Combination = fact(Attacks) / (fact(Attacks - times) * fact(times))
            # 计算发生概率
            # (1-80%)^2*80%^0=4%*1
            # miss 概率 * happen 概率
            # Single = (((100 - Probability) / 100) ^ (Attacks - times)) * ((Probability / 100.0) ^ times)
            Single_EXT = power((100 - Probability_EXT), Attacks - times) * power(Probability_EXT, times)
            Single_CRT = power((100 - Probability_CRT), Attacks - times) * power(Probability_CRT, times)
            # 单次概率乘以出现次数
            Comprehensive_EXT = Combination * Single_EXT
            Comprehensive_CRT = Combination * Single_CRT
            # 对概率四舍五入
            HeppenProbability_EXT = round_up(Comprehensive_EXT / power(100, Attacks - 1))
            HeppenProbabilityList_EXT.append(HeppenProbability_EXT)
            HeppenProbability_CRT = round_up(Comprehensive_CRT / power(100, Attacks - 1))
            HeppenProbabilityList_CRT.append(HeppenProbability_CRT)
            # 保存伤害概率
            L["技能段数"] = Attacks
            L["伤害倍率"] = AttackInfo[2]
            L["单段倍率"] = round_up(AttackInfo[2] / AttackInfo[0] * 100) / 100
            L["连携加成"] = CurrentCombo
            L["发生次数"] = times
            L["连击概率"] = HeppenProbability_EXT
            L["暴击概率"] = HeppenProbability_CRT
            LList.append(L)
        Skill.append(LList)
        #print(Skill)
        # 输出最大概率次数，过滤低于阈值事件
        HeppenProbabilityList_EXT.sort()
        HeppenProbabilityList_CRT.sort()
        #print(HeppenProbabilityList_EXT)
        HeppenProbabilityThreshold_EXT_TMP = round_up(max(HeppenProbabilityList_EXT) * Deviation)
        HeppenProbabilityThreshold_CRT_TMP = round_up(max(HeppenProbabilityList_CRT) * Deviation)
        n = 3 if 3 < len(HeppenProbabilityList_EXT) - 1 else len(HeppenProbabilityList_EXT) - 1
        for i in range(1, n + 1):
            x = n + 1 - i
            if ((HeppenProbabilityThreshold_EXT_TMP < HeppenProbabilityList_EXT[-x]) and HeppenProbabilityList_EXT[-x] > 5):
                HeppenProbabilityThreshold_EXT.append(HeppenProbabilityList_EXT[-x])
        n = 3 if 3 < len(HeppenProbabilityList_CRT) - 1 else len(HeppenProbabilityList_CRT) - 1
        for i in range(1, n + 1):
            x = n + 1 - i
            if ((HeppenProbabilityThreshold_CRT_TMP < HeppenProbabilityList_CRT[-x]) and HeppenProbabilityList_CRT[-x] > 5):
                HeppenProbabilityThreshold_CRT.append(HeppenProbabilityList_CRT[-x])
        HeppenProbabilityThresholdList_EXT.append(HeppenProbabilityThreshold_EXT)
        HeppenProbabilityThresholdList_CRT.append(HeppenProbabilityThreshold_CRT)
    CountTimes = 0
    AttackValue = 0
    CharCard.AttackValue = [0, 0, 0]
    for AttackInfo in Skill:
        AttackProbListPercent = 0
        AttackProbListAnalyse = []
        for SingleSkill in AttackInfo:
            HeppenProbability_EXT = SingleSkill["连击概率"]
            HeppenProbability_CRT = SingleSkill["暴击概率"]
            CountTimes_EXT = len(HeppenProbabilityThreshold_EXT) - 1 if len(HeppenProbabilityThreshold_EXT) - 1 < CountTimes else CountTimes
            if (HeppenProbability_EXT < HeppenProbabilityThreshold_EXT[CountTimes_EXT] and not CalcMode):
                CountTimes = CountTimes + 1
                continue
            CountTimes_CRT = len(HeppenProbabilityThreshold_CRT) - 1 if len(HeppenProbabilityThreshold_CRT) - 1 < CountTimes else CountTimes
            if (HeppenProbability_CRT < HeppenProbabilityThreshold_CRT[CountTimes_CRT] and CalcMode):
                CountTimes = CountTimes + 1
                continue
            elif (abs(HeppenProbability_EXT - HeppenProbability_CRT) == 100 and SingleSkill["发生次数"] == 0):
                CountTimes = CountTimes + 1
                continue
            else:
                HeppenProbability_EXT = 0 if HeppenProbability_EXT < HeppenProbabilityThreshold_EXT[CountTimes_EXT] else HeppenProbability_EXT
                HeppenProbability_CRT = 0 if HeppenProbability_CRT < HeppenProbabilityThreshold_CRT[CountTimes_CRT] else HeppenProbability_CRT
            # 发生次数、连击概率、暴击概率等
            AttackProbListPercent = SingleSkill["连击概率"] if not CalcMode else SingleSkill["暴击概率"]
            print("发生", SingleSkill["发生次数"], "次：", "连击" if not CalcMode else "暴击", "概率", AttackProbListPercent, "%")
            AttackPower = AttackV["基础攻击"]
            AmplifyDamage = AttackV["伤害加成"]
            # 常规攻击伤害等于
            # 攻击段数 * 技能每段伤害 * 面板攻击力 * 伤害加成 * 默认连携 100% * 敌人伤减 50%
            Attack_P = 0
            TeamWork = 0 if SingleSkill["技能段数"] == 1 else SingleSkill["连携加成"] / 2
            Attack_P = SingleSkill["技能段数"] * SingleSkill["单段倍率"] * (AttackPower / 100)  * ((AmplifyDamage + 100) / 100) * ((Combo + TeamWork) / 100) * DefDePercent * ((100 + SkillUp) / 100)
            # print("常规攻击", int(Attack_P), "点伤害。")

            AttackProbList = []
            if (not CalcMode):
                # 以连击为主
                # 附加连击伤害等于
                # 连击段数 * 面板攻击力 *（15% + 辅正）* 伤害加成 * 默认连携 100%
                Attack_EXT = 0
                if (HeppenProbability_EXT > 0):
                    Attack_EXT = SingleSkill["发生次数"] * (AttackPower / 100) * Auxiliary_EXT * ((AmplifyDamage + 100) / 100) * ((Combo + TeamWork) / 100) * ((100 + SkillUp) / 100)
                # print("连击附加", int(Attack_EXT), "点伤害。")
                # 连击次数 SingleSkill["发生次数"]
                # 阈值 HeppenProbabilityThreshold_EXT * 3
                # 暴击超出概率的有 sorted(x, key = lambda x:x[2]) => n/len -3 x[:-n]
                # 概率表取前三计算范围
                CRTMaxCount = MaxCount(AttackInfo, not CalcMode)
                for Count in CRTMaxCount:
                    # 计算概率前三的暴击伤害
                    Attack_CRT = 0
                    if (Count[1] > 0):
                        Attack_CRT = Count[0] * SingleSkill["单段倍率"] * (AttackPower / 100)  * (Auxiliary_CRT / 100) * ((AmplifyDamage + 100) / 100) * ((Combo + TeamWork) / 100) * DefDePercent * ((100 + SkillUp) / 100)
                    else:
                        Attack_CRT = 0
                    AttackProbList.append([Attack_CRT + Attack_EXT + Attack_P, Count[1], AttackProbListPercent])
            else:
                # 以暴击为主
                # 暴击附加伤害等于
                # 暴击段数 * 技能每段伤害 * 面板攻击力 *（50% + 辅正）* 伤害加成 * 默认连携 100% * 敌人伤减 50%
                Attack_CRT = 0
                if (HeppenProbability_CRT > 0):
                    Attack_CRT = SingleSkill["发生次数"] * SingleSkill["单段倍率"] * (AttackPower / 100)  * (Auxiliary_CRT / 100) * ((AmplifyDamage + 100) / 100) * ((Combo + TeamWork) / 100) * DefDePercent * ((100 + SkillUp) / 100)
                # print("暴击附加", int(Attack_CRT), "点伤害。")
                # 概率表取前三计算范围
                EXTMaxCount = MaxCount(AttackInfo, not CalcMode)
                for Count in EXTMaxCount:
                    # 计算概率前三的连击伤害
                    Attack_EXT = 0
                    if (Count[1] > 0):
                        Attack_EXT = Count[0] * (AttackPower / 100) * Auxiliary_EXT * ((AmplifyDamage + 100) / 100) * ((Combo + SingleSkill["连携加成"] / 2) / 100)
                    else:
                        Attack_EXT = 0
                    AttackProbList.append([Attack_EXT + Attack_CRT + Attack_P, Count[1], AttackProbListPercent])

            # Attack_Total = Attack_EXT + Attack_CRT + Attack_P
            # AttackProbList = list(set(AttackProbList))
            print("技能伤害输出", int(AttackProbList[0][0]) if len(AttackProbList) == 1 else str(int(attmin(AttackProbList))) + " <- " + str(int(attmid(AttackProbList))) + " -> " + str(int(attmax(AttackProbList))), "点伤害。")
            AttackProbListAnalyse.append(AttackProbList)
        print("该段攻击结束")
        minVT, midVT, maxVT = Analyse(AttackProbListAnalyse)
        CharCard.AttackValues(minVT, midVT, maxVT)
        CountTimes = CountTimes + 1
    print("概率运算结束")
    return CurrentCombo


if __name__ == '__main__':
    Team = [
        # Emilia(3000, 12, [90, 30], [15.0, 200]),
        # Felt(3000, 12, [90, 30], [15.0, 200]),
        # Crusch(3000, 13, [26.5, 75+15], [15.0, 186])
        Julius(2130, 12.2, [90, 10.6], [17.7, 161.6])
        # 角色(基础攻击, 伤害加成, [连击率, 暴击率], [连击伤害, 暴击伤害]),
        # Felt / Crusch / Emilia(2097, 6, [50, 100], [17.5, 150])
    ]

    MonsterList =[
        Monster(375, 1),
        # Monster(初始防御率, 增防减伤 Buff)
    ]

    index = 1
    Combo = 100
    for Member in Team:
        index = index + 1
        print("当前出手：", Member.CharName, "【连携加成：", Combo, "%】")
        Combo = Combo + SkillDamage(Member.Skill["SP"]["LV1"], Member, 0, Combo, MonsterList)
        print("结束技能：", Member.AttackValue)
        if index > 3: Combo = 100
'''

import json
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/.*": {"origins": ["http://106.13.206.213", "http://106.13.206.213:5001", "http://127.0.0.1"]}})

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/RE0Skill', methods=['POST'])
def RE0Skill():
    SkillInfo = []
    CharInfo = json.loads(request.get_data())
    for x in ["A", "AP", "SP", "B"]:
        init = "{name}.Skill['{skill}']['NAME']".format(name=CharInfo['name'], skill=x)
        SkillInfo.append([x, eval(init)])
    return json.dumps(SkillInfo, ensure_ascii=True)

@app.route('/RE0', methods=['POST'])
def RE0():
    CharInfo = json.loads(request.get_data())
    init = "{name}({att}, {add}, [{ext}, {crt}], [{extadd}, {crtadd}])".format(name=CharInfo['name'], att=CharInfo['attack'], add=CharInfo['da'], ext=CharInfo['ext'], crt=CharInfo['crt'], extadd=CharInfo['extadd'], crtadd=CharInfo['crtadd'])
    print(init)
    Char = eval(init)

    MonsterList =[
        Monster(int(CharInfo['monsterdefinfo'][0]), 1)
        # Monster(初始防御率, 增防减伤 Buff)
    ]

    MLCount = len(MonsterList)
    for ML in CharInfo['monsterinfo']:
        print(ML)
        if (ML):
            print(ML)
            MonsterList.append(Monster(int(CharInfo['monsterdefinfo'][MLCount]), 1))
        MLCount = MLCount + 1
    print(json.dumps(Char.__dict__, ensure_ascii=True))

    Combo = int(CharInfo['teamwork'])
    ret = []
    SLCount = 0
    for SkillType in ["A", "AP", "SP", "B"]:
        SkillDamage(Char.Skill[SkillType]["LV" + str(int(CharInfo['skilllevel'][SLCount])) if int(CharInfo['skilllevel'][SLCount]) in (1, 2, 3, 4, 5) else "1" ], Char,
                    float(CharInfo['skilllevelup'][SLCount]), Combo, MonsterList)
        ret.append(', '.join([str(x) for x in Char.AttackValue]))
        Char.AttackValuesClean()
        SLCount = SLCount + 1
    return ', '.join(ret)

if __name__ == '__main__':
    app.run()

'''
