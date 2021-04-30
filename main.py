import cvxpy as cp
import numpy as np
import pandas as pd
import argparse

def armor_saiteki(atama_list,dou_list,ude_list,kosi_list,asi_list,select_skill_list,weight_list,maxlv_list):
    # Problem data.
    m = 30
    n = 20
    atama_size = atama_list.shape
    dou_size = dou_list.shape
    ude_size = ude_list.shape
    kosi_size = kosi_list.shape
    asi_size = asi_list.shape
    
    np.random.seed(1)
    # Construct the problem.
    atama_variable = cp.Variable(atama_size[1],boolean = True)
    dou_variable = cp.Variable(dou_size[1],boolean = True)
    ude_variable = cp.Variable(ude_size[1],boolean = True)
    kosi_variable = cp.Variable(kosi_size[1],boolean = True)
    asi_variable = cp.Variable(asi_size[1],boolean = True)
    
    atama_ste = atama_list@atama_variable
    dou_ste = dou_list@dou_variable
    ude_ste = ude_list@ude_variable
    kosi_ste = kosi_list@kosi_variable
    asi_ste = asi_list@asi_variable
                
    #
    tmp_1 = (atama_ste + dou_ste + ude_ste + kosi_ste + asi_ste)
    weight_tmp1 =  tmp_1 @ weight_list
    tmp_2 = None
    
    #選択したスキルを最大化する
    for i in select_skill_list:
        if tmp_2 is None:
            
            tmp_2 = tmp_1[i] * weight_list[i]

        else:
            tmp_2 += tmp_1[i] * weight_list[i]
            
    if not(tmp_2 is None):
        objective = cp.Maximize(cp.sum(tmp_2))
    else:
        objective = cp.Maximize(cp.sum(weight_tmp1))
    #防具は複数装備できない。
    constraints = [
        cp.sum(atama_variable) <= 1,
        cp.sum(dou_variable) <= 1,
        cp.sum(ude_variable) <= 1,
        cp.sum(kosi_variable) <= 1,
        cp.sum(asi_variable) <= 1,
        cp.sum(atama_variable) >= 1,
        cp.sum(dou_variable) >= 1,
        cp.sum(ude_variable) >= 1,
        cp.sum(kosi_variable) >= 1,
        cp.sum(asi_variable) >= 1,
        tmp_1 <= maxlv_list,
        ]
        
    prob = cp.Problem(objective, constraints)

    # The optimal objective value is returned by `prob.solve()`.
    result = prob.solve()
    return atama_variable.value,dou_variable.value,ude_variable.value,kosi_variable.value,asi_variable.value
#初期設定

parser = argparse.ArgumentParser(description="config")
parser.add_argument(
        "--select",
        type=str,
        default="",
        help="Enter the skill you want to maximize. Example:""lv2,攻撃,集中,強化持続""",
)

args = parser.parse_args()


#装備データを読み込む
armor_data = pd.read_csv("./data/armor.csv",index_col = [0],encoding="SHIFT-JIS")
weight_data = pd.read_csv("./data/weight.csv",encoding="SHIFT-JIS")
maxlv_data = pd.read_csv("./data/maxlv.csv",encoding="SHIFT-JIS")

atama_list = armor_data[armor_data["装備場所"] == "頭防具"].T["lv1":].to_numpy()
dou_list = armor_data[armor_data["装備場所"] == "胴体防具"].T["lv1":].to_numpy()
ude_list = armor_data[armor_data["装備場所"] == "腕防具"].T["lv1":].to_numpy()
kosi_list = armor_data[armor_data["装備場所"] == "腰防具"].T["lv1":].to_numpy()
asi_list = armor_data[armor_data["装備場所"] == "足防具"].T["lv1":].to_numpy()

weight_list = weight_data.to_numpy()[0]
maxlv_list = maxlv_data.to_numpy()[0]

select_skill_list = []
if len(args.select) > 0:
    skill_name_list = args.select.split(",")
else:
    skill_name_list = []
for i in skill_name_list:
    select_skill_list.append(list(armor_data.columns).index(i)-1)
    

a1,d,u,k,a2 = armor_saiteki(atama_list,dou_list,ude_list,kosi_list,asi_list,select_skill_list,weight_list,maxlv_list)

print("----------------------------------------------")
if len(skill_name_list) > 0:
    print(skill_name_list)
else:
    print("すべてのスキル")
print("を最大にする装備は以下のようになります。")
print("装備名")
print(armor_data[armor_data["装備場所"] == "頭防具"].index[a1== 1])
print(armor_data[armor_data["装備場所"] == "胴体防具"].index[d== 1])
print(armor_data[armor_data["装備場所"] == "腕防具"].index[u== 1])
print(armor_data[armor_data["装備場所"] == "腰防具"].index[k== 1])
print(armor_data[armor_data["装備場所"] == "足防具"].index[a2== 1])

tmp = atama_list[:,a1== 1] + dou_list[:,d== 1] + ude_list[:,u== 1] + kosi_list[:,k== 1] + asi_list[:,a2== 1]

#
print("スキル一覧")
for i,lv in enumerate(tmp):
    if lv > 0:
       print(str(armor_data.columns[i+1]) + ":lv"  + str(lv))
print("----------------------------------------------")