import random
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# 博弈模块，计算i个体的收益payoff_i
def interaction(i, b, S, direct_nei_i):
    payoff_i = 0
    for j in direct_nei_i:
        if ws.nodes[j]['game'] == 1:
            payoff_i += b
        else:
            payoff_i += S
    return payoff_i



# 策略更新，个体i学习近邻中收益最高的策略
def strategy_update(i, direct_nei_i):
    max_payoff = -float('inf')
    best_strategy = ws.nodes[i]['game']
    for strategy in [0, 1]:
        ws.nodes[i]['game'] = strategy
        payoff_i = interaction(i, b, S, direct_nei_i)
        if payoff_i > max_payoff:
            max_payoff = payoff_i
            best_strategy = strategy
    ws.nodes[i]['game'] = best_strategy



# 移动模块 背叛者驱动移动
def mobility_i(i, direct_nei_i):
    if ws.nodes[i]['game'] == 1:
        a = random.random()
        if a < p and len(direct_nei_i) > 0:
            new_pos = random.choice(direct_nei_i)
            ws.nodes[new_pos]['flag'] = 1
            ws.nodes[new_pos]['game'] = 1
            ws.nodes[i]['flag'] = 0
            ws.nodes[i]['game'] = 2


# main function
b = 1.3
S = -0.3
p = 0.1
circle_N = 1000
cycle_N = 50
key_final = 5

file_fc_t = open("p02_fct.txt", "wt+")
fc_final = 0.0
ws = nx.Graph()

fp = open("CA-GrQc.txt", "r")

while True:
    content = fp.readline()
    if len(content) == 0:
        break
    else:
        str_list = content.split()
        node = int(str_list[0])
        edge_node = int(str_list[1])
        ws.add_node(node)
        ws.add_node(edge_node)
        ws.add_edge(node, edge_node)
network_size = len(ws.nodes)

print("读取网络结束")
print(len(ws.nodes))
print(len(ws.edges))

for cycle in range(cycle_N):
    for i in ws.nodes:
        a = random.random()
        if a <= 0.7:
            ws.nodes[i]['flag'] = 1
        else:
            ws.nodes[i]['flag'] = 0

        if ws.nodes[i]['flag'] == 1:
            a = random.random()
            if a <= 0.5:
                ws.nodes[i]['game'] = 1
            else:
                ws.nodes[i]['game'] = 0
        else:
            ws.nodes[i]['game'] = 2

    node_list = list(ws.nodes)
    for circle in range(circle_N):
        for Monte_step in range(network_size):
            i_ran = random.randint(0, network_size - 1)
            i = node_list[i_ran]
            mobility_flag = 0
            empty_flag = 0
            emp_count = 0

            if ws.nodes[i]['flag'] == 1:
                direct_nei_i = list(ws.neighbors(i))
                length_nei_i = len(direct_nei_i)
                # 进行博弈
                payoff_i = interaction(i, b, S, direct_nei_i)
                # 策略更新
                strategy_update(i, direct_nei_i)
                # 移动模块
                mobility_i(i, direct_nei_i)

        D_sum = 0
        C_sum = 0
        E_sum = 0
        empty_node_list = []
        for s in ws.nodes:
            if ws.nodes[s]['game'] == 0:
                C_sum += 1
            elif ws.nodes[s]['game'] == 1:
                D_sum += 1
            elif ws.nodes[s]['flag'] == 0:
                E_sum += 1
                empty_node_list.append(s)
        fc = C_sum / (C_sum + D_sum)

        # 更新最终fc值
        if cycle >= cycle_N - key_final + 1:
            fc_final += fc / key_final

file_fc_t.write("%6.4f,%6.4f,%6.4f,%6.4f,%6.4f,%6.4f,%6.4f,%6.4f,%6.4f\n" % (b, S, p, fc_final))
file_fc_t.close()