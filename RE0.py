class Character:
    Attack = {
        "基础攻击": 0,
        "伤害加成": 0
    }
    Probability = [0, 0]
    Auxiliary = [150, 1.5]
    Skill = {
        "A": {
            "LV1": [(0, 0, 0, 0)],
            "LV2": [(0, 0, 0, 0)],
            "LV3": [(0, 0, 0, 0)],
            "LV4": [(0, 0, 0, 0)],
            "LV5": [(0, 0, 0, 0)]
        },
        "AP": {
            "LV1": [(0, 0, 0, 0)],
            "LV2": [(0, 0, 0, 0)],
            "LV3": [(0, 0, 0, 0)],
            "LV4": [(0, 0, 0, 0)],
            "LV5": [(0, 0, 0, 0)]
        },
        "SP": {
            "LV1": [(0, 0, 0, 0)],
            "LV2": [(0, 0, 0, 0)],
            "LV3": [(0, 0, 0, 0)],
            "LV4": [(0, 0, 0, 0)],
            "LV5": [(0, 0, 0, 0)]
        }
    }

class Emilia(Character):
    CharName = "爱蜜莉雅·朦胧的睡意"
    Skill = {
        # 引动冰雪攻击敌方全体，对目标造成攻击力36%的伤害
        "A": {
            "LV1": [(3, 1, 36, 10)],
            "LV2": [(3, 1, 37, 11)],
            "LV3": [(3, 1, 39, 12)],
            "LV4": [(3, 1, 41, 13)],
            "LV5": [(3, 1, 45, 15)]
        },
        # 对敌方所有目标进行攻击，造成攻击力80%的伤害
        "AP": {
            "LV1": [(8, 1, 80, 10)],
            "LV2": [(8, 1, 84, 10)],
            "LV3": [(8, 1, 88, 10)],
            "LV4": [(8, 1, 92, 10)],
            "LV5": [(8, 1, 100, 10)]
        },
        # 与帕克一起对敌方全体造成136%伤害，由所有敌人分摊
        "SP": {
            "LV1": [(4, 1, 45.33, 10)],
            "LV2": [(4, 1, 47.33, 10)],
            "LV3": [(4, 1, 49.67, 10)],
            "LV4": [(4, 1, 52, 10)],
            "LV5": [(4, 1, 56.67, 10)]
        }
    }
    def __init__(self, AttackPower = 1299, AmplifyDamage = 0, Probability = [17, 3], Auxiliary = [150, 1.5]):
        self.Attack["基础攻击"] = AttackPower
        self.Attack["伤害加成"] = AmplifyDamage
        self.Probability = Probability
        self.Auxiliary = Auxiliary

fact = lambda n: [1, 0][n > 1] or fact(n - 1) * n
power = lambda num, n: [1, 0][n > 0] or power(num, n - 1) * num
round_up = lambda num: round(num * 100) / 100.0

'''
    AttackList - 技能总数据
        AttackInfo - 技能分段信息
        AttackInfo[0] - 技能攻击次数
        AttackInfo[1] - 是否群体技能
        AttackInfo[2] - 技能伤害比例
    AttackV - 角色攻击属性
        AttackV[0] - 基础攻击
        AttackV[1] - 伤害加成
    Probability - 概率
        Probability[0] - 连击概率
        Probability[1] - 暴击概率
    Auxiliary - 攻击辅正（连击115%或暴击150%的超出部分）
    Deviation - 范围偏差（0.2大范围至0.8普遍）
    # CalcMode - 连击(0)或暴击(1)计算
''' 
def SkillDamage(AttackList, AttackV, Probability, Auxiliary, Combo = 100, Deviation = 0.5, CalcMode = 0):
    Skill = []
    CurrentCombo = 0
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

    for AttackInfo in AttackList:
        LList = []
        HeppenProbabilityList_EXT = []
        HeppenProbabilityList_CRT = []
        Attacks = AttackInfo[0] * 3 if AttackInfo[1] else AttackInfo[0]
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
            
            # HeppenProbabilityMax_EXT = HeppenProbability_EXT if HeppenProbability_EXT > HeppenProbabilityMax_EXT else HeppenProbabilityMax_EXT
            # HeppenProbabilityMax_CRT = HeppenProbability_CRT if HeppenProbability_CRT > HeppenProbabilityMax_CRT else HeppenProbabilityMax_CRT
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
        # 输出最大概率次数，过滤低于阈值事件
        HeppenProbabilityList_EXT.sort()
        HeppenProbabilityList_CRT.sort()
        HeppenProbabilityThreshold_EXT = round_up(max(HeppenProbabilityList_EXT) * Deviation)
        HeppenProbabilityThreshold_CRT = round_up(max(HeppenProbabilityList_CRT) * Deviation)
        n = 3 if 3 < len(HeppenProbabilityList_EXT) - 1 else len(HeppenProbabilityList_EXT) - 1
        if (HeppenProbabilityThreshold_EXT > HeppenProbabilityList_EXT[-n] and HeppenProbabilityList_EXT[-n] > 0):
            HeppenProbabilityThreshold_EXT = HeppenProbabilityList_EXT[-n]
        n = 3 if 3 < len(HeppenProbabilityList_CRT) - 1 else len(HeppenProbabilityList_CRT) - 1
        if (HeppenProbabilityThreshold_CRT > HeppenProbabilityList_CRT[-n] and HeppenProbabilityList_CRT[-n] > 0):
            HeppenProbabilityThreshold_CRT = HeppenProbabilityList_CRT[-n]
        
    AttackValue = 0
    for AttackInfo in Skill:
        for SingleSkill in AttackInfo:
            HeppenProbability_EXT = SingleSkill["连击概率"]
            HeppenProbability_CRT = SingleSkill["暴击概率"]
            if HeppenProbability_EXT < HeppenProbabilityThreshold_EXT and HeppenProbability_CRT < HeppenProbabilityThreshold_CRT:
                continue
            else:
                HeppenProbability_EXT = 0 if HeppenProbability_EXT < HeppenProbabilityThreshold_EXT else HeppenProbability_EXT
                HeppenProbability_CRT = 0 if HeppenProbability_CRT < HeppenProbabilityThreshold_CRT else HeppenProbability_CRT
            # 发生次数、连击概率、暴击概率等
            print("发生", SingleSkill["发生次数"], "次：连击概率", SingleSkill["连击概率"], "%，暴击概率", SingleSkill["暴击概率"], "%。")
            AttackPower = AttackV["基础攻击"]
            AmplifyDamage = AttackV["伤害加成"]
            # 附加连击伤害等于
            # 连击段数 * 面板攻击力 *（15% + 辅正）* 伤害加成 * 默认连携 100%
            Attack_EXT = 0
            if (HeppenProbability_EXT > 0):
                Attack_EXT = SingleSkill["发生次数"] * (AttackPower / 100) * Auxiliary_EXT * ((AmplifyDamage + 100) / 100) * ((Combo + SingleSkill["连携加成"] / 2) / 100)
            # print("连击附加", int(Attack_EXT), "点伤害。")
            # 暴击附加伤害等于
            # 暴击段数 * 技能每段伤害 * 面板攻击力 *（50% + 辅正）* 伤害加成 * 默认连携 100% * 敌人伤减 50%
            Attack_CRT = 0
            if (HeppenProbability_CRT > 0):
                Attack_CRT = SingleSkill["发生次数"] * SingleSkill["单段倍率"] * (AttackPower / 100)  * (Auxiliary_CRT / 100) * ((AmplifyDamage + 100) / 100) * ((Combo + SingleSkill["连携加成"] / 2) / 100) * (50 / 100)
            # print("暴击附加", int(Attack_CRT), "点伤害。")
            # 常规攻击伤害等于
            # 攻击段数 * 技能每段伤害 * 面板攻击力 * 伤害加成 * 默认连携 100% * 敌人伤减 50%
            Attack_P = 0
            Attack_P = SingleSkill["技能段数"] * SingleSkill["单段倍率"] * (AttackPower / 100)  * ((AmplifyDamage + 100) / 100) * ((Combo + SingleSkill["连携加成"] / 2) / 100) * (50 / 100)
            # print("常规攻击", int(Attack_P), "点伤害。")
            Attack_Total = Attack_EXT + Attack_CRT + Attack_P
            print("技能伤害输出", int(Attack_Total), "点伤害。")
        print("该段攻击结束")
    print("概率运算结束")
    return CurrentCombo

if __name__ == '__main__':
    Team = [
        Emilia(1429, 4.5, [95, 20], [15, 150]),
        # Emilia(1429, [80, 10], [188, 17.5]),
        # Emilia(1429, [80, 10], [188, 17.5])
    ]

    Combo = 100
    for Member in Team:
        Combo = Combo + SkillDamage(Member.Skill["AP"]["LV5"], Member.Attack, Member.Probability, Member.Auxiliary, Combo)
    # SkillDamage([(3, 0, 375)], [3.2, 0], [40, 5])
    