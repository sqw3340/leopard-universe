# -*- coding: utf-8 -*-
"""
豹药宇宙 - 自走棋
  v1.4.2 审计缺陷修复版
    - 修复P0/P1/P2核心缺陷：模拟卡池隔离、三星五费扣池、原子存档、更新语法校验、训练源码写入保护、真伤/易伤、纹章羁绊同步、存档schema、联机协议、财宝9层三选一
    - 新增模拟器脏数据清洗与多份源码备份
  v1.4.1 噩梦入侵排位版
    - 新增: 排位到达王者段位后，7名对手全部切换为当前最强噩梦AI（噩梦入侵）
    - 新增: 入侵噩梦AI沿用三星五费博弈+学习玩家运营，随训练突破自动升级优化
    - 新增: 排位页提示王者入侵规则；结算文案标注（噩梦AI入侵）
  v1.4.0 恭喜发财·三星五费博弈·AI学习玩家运营版
    - 新增: 恭喜发财独立模式（五费开局/大妮蔻狂欢/全员噩梦最强AI）
    - 新增: 大妮蔻获取途径扩充：财宝高层收菜/野怪法球/血量跌破50/海克斯
    - 新增: 恭喜发财阶段6结束存活单位100%保底大妮蔻
    - 新增: 噩梦/极限AI主动追三星五费（条件齐备才启动，追无望及时止损）
    - 新增: 场上有人三星五费时，其余极限AI追别的五费对抗，已三星的牌不再抢
    - 新增: 噩梦AI学习玩家运营（模仿运营倾向+针对性克制），设置可开关/一键清空样本
    - 新增: 主菜单【恭喜发财】入口与专属页面，与排位/普通/噩梦完全隔离
  v1.3.3 噩梦模式·挑战最强AI·内置段位池版
    - 新增: 噩梦模式难度（7名对手全部为当前最强AI，收入+75%，挑战失败记录对局供AI升级）
    - 新增: 主菜单【挑战最强AI】专属页面（显示当前最强AI段位/分数，一键开始挑战）
    - 新增: 源码内置青铜→王者8段位AI池，分发无需外部json，排位对手不会降级
    - 新增: 排位虚高保护（对手低于玩家段位：赢少加输多扣；更高：赢多加输少扣）
    - 新增: 离线训练突破时自动把最优AI固化进豹药宇宙.py源码（带.bak备份）
    - 优化: 段位AI强度经大样本校准（相邻段位1000局对决+200局混战，吃鸡率单调0%→49%）
    - 修复: 训练日志显示突破复核未达标原因，不再误解"高分为何没被采纳"
  v1.3.2 排位赛专属页面与昊天锤获取扩充版
    - 新增: 排位赛专属页面（段位/战绩/进度条/加分机制），页面内点开始对战才进入排位
    - 修复: 排位结算存档路径，防止打完段位没变化/重启归零
    - 新增: 海克斯【重铸工坊】【匠人之匣】、财宝3层昊天锤×2，扩充昊天锤获取
    - 修复: AI 误把装备拆卸器等一次性消耗道具装配到棋子身上的 BUG
    - 优化: 极限AI训练停滞机制（大变异只动少量字段/精英不重评估/突破复核）
    - 优化: 训练弹窗显示本代最优分
  v1.3.1 装备装配修复版
    - 修复: AI 误把装备拆卸器等一次性消耗道具装配到棋子身上的 BUG
    - 新增: 装备数据表 item_type 标记(可穿戴装备/一次性消耗道具) + is_wearable_item 判定
    - 新增: AI 装配过滤消耗道具 + 装配函数兜底拦截 + 历史误装配道具回收清理
  v1.3.0 金铲铲之战对标·伐木羁绊与道具权限完整版
    - 新增: 伐木羁绊3/5/8三档 + 巨斧选择器（常驻不消耗、跨回合保留）
    - 新增: 昊天锤(卸装→重铸→装回) / 拆卸器 / 大妮蔻 权限矩阵
    - 新增: 纹章之书备战席伪棋子（出售触发4选1）
    - 新增: 战斗备战席面板 + 详情弹窗统一出售按钮
    - 优化: 羁绊弹窗两栏分栏+垂直滚动、HUD连胜/连败徽章+利息满提示
    - 修复: 纹章羁绊无残留、2-1野怪100%掉拆卸器、物品栏散件直接合成
- 新增: 检测更新与自动更新功能（GitHub 更新源）
    - 新增: 主菜单"检测更新"按钮
    - 新增: 更新弹窗（显示新版本号、更新日志、立即更新按钮）
    - 新增: 详情面板职业前显示"法术/物理"标签
    - 优化: 羁绊弹窗棋子列表按费用排序并显示费用
    - 优化: 羁绊弹窗已上场棋子绿色、未上场浅蓝色
    - 修复: 职业羁绊（坦克/射手/术士/战士）不显示棋子的问题
  v1.2.7 界面与显示优化版
    - 新增: 设置菜单"查看更新日志"入口
    - 新增: 18 个新英雄技能中文名
    - 优化: 商店卡面显示职业羁绊
    - 优化: 详情面板羁绊含职业标签
    - 修复: 新英雄技能名显示为英文
  v1.2.6 职业与坦克扩展版
    - 新增: 4 种职业羁绊（坦克/射手/术士/战士），按 role 自动统计
    - 新增: 13 个英雄（8 坦克 + 5 射手）
    - 新增: 坦克技能多样化（举盾/爆盾/回血 3 种新类型）
    - 新增: 护盾溅射伤害类型可切换（物理/魔法）
    - 提升: 药剂族/财宝猎人 羁绊阈值升到 4 档 [2,4,6,8]
    - 修复: apply_poison 空返回导致中毒失效
    - 修复: take_damage 护盾双倍吸收的 bug
  v1.2.5 全面优化版
    - 修复: 共享英雄池并发预留、库存上限与售罄购买检查
    - 修复: AI出售高星棋子时归还正确数量的英雄副本
    - 修复: 自动布阵在棋子超出人口/备战席容量时不再静默丢子
    - 修复: 选秀中AI备战席已满时返还英雄池副本
    - 新增: 点击装备查看详细属性，合成装备也可查看详情
    - 修复: 起始英雄选择遇到库存变化时不会凭空生成棋子
  v1.2.4 终极雷霆版
    - 修复: 购买/升级不再自动上场, 战斗开始前自动补位
    - 修复: 战斗单位被中线锁死无法追击
    - 修复: 网络半包/断线/平局重置等
    - 新增: 雷霆六人组 + 雷霆羁绊
    - 新增: 雷霆AI助手 (自动吐槽)
    - 修复: 雷霆技能与AI助手的缩进错误
Changelog:
  v1.2.9 完整版
    - [X] A 类：羁绊阈值与棋子羁绊调整
    - [X] B 类：财宝猎人收菜系统完整实现
    - [X] C 类：豹灵符/药灵符/三神符转职系统
    - [X] D 类：特殊装备系统
    - [X] E 类：豹药神器
    - [X] F 类：光明装备系统
    - [X] G 类：三星五费设计
    - [X] H 类：全局验收与修复
    - [X] 转职限制：同一棋子禁止重复同类转职；原生同羁绊棋子禁止装备对应转职
"""
import pygame
import random
import copy
import math
import array
import os
import sys
import traceback
import socket
import threading
import pickle
import time
import urllib.request
import json
import re
import ast
import tempfile
import contextlib
from collections import deque

# v1.4.2 safety locks / isolated simulation state
_SOURCE_WRITE_LOCK = threading.RLock()
_AI_PARAMS_LOCK = threading.RLock()
_SIM_POOL_LOCAL = threading.local()

pygame.display.init()
pygame.font.init()
AUDIO_OK = False

def _try_init_audio():
    """多配置重试初始化音频；手机上导入时音频设备可能未就绪。"""
    global AUDIO_OK
    configs = [
        dict(frequency=44100, size=-16, channels=2, buffer=512),
        dict(frequency=22050, size=-16, channels=1, buffer=1024),
        dict(frequency=44100, size=-16, channels=1, buffer=2048),
        dict(frequency=22050, size=-16, channels=2, buffer=4096),
    ]
    for cfg in configs:
        try:
            pygame.mixer.quit()
            pygame.mixer.init(**cfg)
            pygame.mixer.music.set_volume(1.0)
            AUDIO_OK = True
            return True
        except Exception:
            continue
    AUDIO_OK = False
    return False

_try_init_audio()

FPS = 60
FIXED_BATTLE_DT = 1.0 / 60.0
MAX_FIXED_STEPS = 12
MIN_W, MIN_H = 540, 960
BG_COLOR = (18, 20, 28)
PANEL_COLOR = (32, 35, 46)
PANEL_DARK = (22, 24, 33)
TEXT_WHITE = (240, 240, 245)
TEXT_DIM = (145, 150, 162)
GOLD_COLOR = (255, 205, 80)
GOLD_DEEP = (195, 145, 35)
ORANGE_TIMER = (255, 155, 55)
GREEN_HP = (80, 215, 100)
RED = (225, 65, 65)
BLUE = (65, 120, 210)
BLUE_DEEP = (35, 65, 130)
PURPLE = (130, 75, 190)
PURPLE_DEEP = (75, 42, 115)
BLUE_MANA = (50, 165, 255)
WHITE_FLASH = (255, 255, 255)
HIGHLIGHT = (255, 235, 100)
SELL_RED = (210, 60, 60)
CRIT_COLOR = (255, 225, 55)
DAMAGE_COLOR = (255, 75, 75)
HEAL_COLOR = (75, 255, 125)
SHIELD_COLOR = (135, 195, 255)
LOCK_COLOR = (255, 195, 55)
UNLOCK_COLOR = (130, 130, 130)
BORDER_LIGHT = (75, 82, 100)
BORDER_GOLD = (200, 160, 60)
BEAR_COLOR = (205, 135, 60)
RUNE_COLOR = (140, 200, 255)
TREASURE_COLOR = (255, 195, 55)
FRONT_ROW_COLOR = (85, 42, 42)
BACK_ROW_COLOR = (35, 50, 85)
MIRROR_COLOR = (185, 130, 255)
ROLE_COLORS = {"tank": (110, 160, 220), "warrior": (220, 120, 90),
               "archer": (130, 220, 120), "mage": (200, 140, 240)}
ROLE_SHORT = {"tank": "坦", "warrior": "战", "archer": "射", "mage": "术"}
ROLE_NAME_CN = {"tank": "坦克", "warrior": "战士",
                "archer": "射手", "mage": "术士"}
RARITY_COLOR = {"silver": (190, 190, 200), "gold": (255, 210, 90),
                "prismatic": (220, 130, 255)}
RARITY_NAME = {"silver": "白银", "gold": "黄金", "prismatic": "棱彩"}
STAR_BORDER = {1: (180, 180, 180), 2: (110, 200, 255),
               3: (255, 200, 60), 4: (200, 80, 255)}
COST_COLORS = {1: (180, 180, 180), 2: (100, 220, 100),
               3: (80, 140, 255), 4: (200, 100, 255),
               5: (255, 200, 60)}
COST_BG = {1: (55, 55, 60), 2: (40, 70, 40),
           3: (35, 55, 90), 4: (65, 40, 90), 5: (90, 70, 25)}
DBG_LAST = "boot"
BATTLE_DURATION = 30.0
POST_BATTLE_WAIT = 5.0
OVERTIME_DURATION = 15.0   # 加时赛：倒计时归零后双方均有存活单位时的追加战斗时长
PREP_DURATION = 30
RANGE_TANK = 90
RANGE_WARRIOR = 140
RANGE_ARCHER = 700
RANGE_MAGE = 550
RANGED_KEEP_DIST = 200
RANGED_BACKOFF_LIMIT = 120.0
RANGED_BACKOFF_SPEED = 0.5
MIN_MOVE_DIST = 0.001
SEP_MIN_DIST_RATIO = 0.9
SIDE_ALLY_TOP = 0.52
SIDE_ALLY_BOTTOM = 0.98
SIDE_ENEMY_TOP = 0.10
SIDE_ENEMY_BOTTOM = 0.48
STAGE1_ROUNDS = 4
STAGE_NORMAL_ROUNDS = 7

BASE_MANA_REGEN_FLAT = 0.7
BASE_MANA_REGEN_PERCENT = 0.012
MANA_PER_HIT_TAKEN_FLAT = 1
MANA_PER_HIT_TAKEN_PERCENT = 0.02

DIFFICULTY_MULT = {"easy": 0.7, "normal": 1.0, "hard": 1.25, "extreme": 1.6,
                   "nightmare": 1.75}
DIFFICULTY_NAME = {"easy": "简单", "normal": "普通",
                   "hard": "困难", "extreme": "极限", "nightmare": "噩梦模式"}
DIFFICULTY_ORDER = ["easy", "normal", "hard", "extreme", "nightmare"]
DIFFICULTY_COLOR = {"easy": (120, 220, 120), "normal": (110, 170, 240),
                    "hard": (255, 170, 60), "extreme": (230, 80, 80),
                    "nightmare": (200, 60, 230)}

CURRENT_VERSION = "1.4.2"
# 更新源：填你自己的远程 version.json 地址（GitHub raw 即可）
# 留空 "" 则关闭检测更新
UPDATE_CHECK_URL = "https://fastly.jsdelivr.net/gh/sqw3340/leopard-universe@main/version.json"

CHANGELOG_TEXT = [
    "v1.4.2  稳定性强化·全面缺陷修复版",
    "  · 【重大修复】修复离线训练污染真实公共卡池的问题，训练模拟与玩家对局彻底隔离",
    "  · 【重大修复】修复噩梦AI追三星五费不扣公共卡池的问题，恢复正常卡池博弈",
    "  · 【存档修复】存档改为原子写入，并增加结构校验、损坏隔离与旧版本字段兼容",
    "  · 【更新修复】自动更新下载后先进行AST/编译校验，避免错误源码直接覆盖本体",
    "  · 【源码安全】训练固化AI与自动更新统一源码写入锁，并增加多份备份保护",
    "  · 【战斗修复】真实伤害不再受到护甲/魔抗减免；负数减伤正确实现易伤",
    "  · 【装备修复】拆卸器/昊天锤处理纹章后自动同步羁绊，清理非法装备与残留羁绊",
    "  · 【棋子修复】safe_unit脏数据修复、法师技能伤害类型兜底、星级边界校验",
    "  · 【财宝修复】财宝猎人9层终极掠夺恢复三选一奖励机制",
    "  · 【联机修复】强化半包、断线、EOF、畸形数据、超大数据包防护",
    "  · 【AI修复】训练参数采用独立候选+线程锁，异常候选正确淘汰，避免污染前台AI",
    "  · 【模拟器】增加人口、棋盘、装备、None、负数及非法字段等脏数据清洗",
    "  · 【稳定性】通过24项自动化单元测试，并完成3000局随机脏数据Fuzz无崩溃验证",
    "  · 【版本】本版本为v1.4.2正式缺陷修复基准版本，建议所有玩家从本版本重新训练AI",
    "v1.4.1  噩梦入侵排位版",
    "  · 新增 排位到达王者段位后：7名对手全部切换为当前最强噩梦AI（噩梦入侵）",
    "  · 新增 入侵噩梦AI沿用三星五费博弈+学习玩家运营，随训练突破自动升级优化",
    "  · 新增 排位页提示王者入侵规则；排位结算文案标注（噩梦AI入侵）",
    "  · 修复 恭喜发财开局选秀候选改为5费（原为1费），对手开局1费同步换为随机5费",
    "  · 修复 设置页『噩梦AI学习玩家运营』开关点击闪退（局部变量未声明global）",
    "  · 优化 主菜单UI：双列布局+按钮图标+信息卡片+装饰光效",
    "  · 说明 王者之下排位梯度不变，入侵只作用于王者段位，强度随训练自动提升",
    "",
    "v1.4.0  恭喜发财·三星五费博弈·AI学习玩家运营版",
    "  · 新增 恭喜发财独立模式：开局全员（你+7对手）随机5费，节奏更快、资源更丰富",
    "  · 新增 大妮蔻获取途径扩充：财宝高层收菜/野怪法球/血量跌破50/海克斯强化",
    "  · 新增 恭喜发财阶段6结束：存活单位100%获得1张大妮蔻（淘汰不领、一次性）",
    "  · 新增 噩梦/极限AI主动追三星五费：核心5费囤够+锁血+存活少+金币足才启动",
    "  · 新增 三星五费对抗博弈：场上有人三星时其余极限AI去追别的五费对抗，追无望止损抢名次",
    "  · 新增 已有人三星的那张牌其余AI不再抢（卡池只剩9张，避免死磕浪费经济）",
    "  · 新增 噩梦AI学习玩家运营：多局积累画像→模仿你的思路+针对性克制（设置可开关/一键清空）",
    "  · 新增 主菜单【恭喜发财】专属入口页面；该模式与排位/普通/噩梦完全隔离",
    "  · 说明 三星五费博弈仅限噩梦/恭喜发财，排位段位AI保持校准梯度不变",
    "",
    "v1.3.3  噩梦模式·挑战最强AI·内置段位池版",
    "  · 新增 噩梦模式难度：7名对手全部为当前最强AI（收入+75%），对局记录供AI自我升级",
    "  · 新增 主菜单【挑战最强AI】专属页面：显示当前最强AI段位/分数，一键开始挑战",
    "  · 新增 源码内置青铜→王者8段位AI池：分发无需外部json，排位对手不会降级",
    "  · 新增 排位虚高保护：对手低于玩家段位赢少加输多扣，更高赢多加输少扣",
    "  · 新增 离线训练突破时自动把最优AI固化进豹药宇宙.py源码（自动生成.bak备份）",
    "  · 优化 段位AI强度经大样本校准：相邻段位1000局对决+200局混战，吃鸡率单调0%→49%",
    "  · 修复 训练日志显示突破复核未达标原因，不再误解高分为何没被采纳",
    "",
    "v1.3.2  排位赛专属页面与昊天锤获取扩充版",
    "  · 新增 排位赛专属页面：段位/战绩/进度条/加分机制说明，页面内点击开始对战才进入排位",
    "  · 修复 排位结算存档写入路径，避免打完段位没变化/重启归零",
    "  · 新增 海克斯强化【重铸工坊】（金色）：获得1把昊天锤",
    "  · 新增 海克斯强化【匠人之匣】（棱彩）：获得昊天锤+拆卸器",
    "  · 新增 财宝猎人3层奖励备选：昊天锤×2",
    "  · 修复 AI 不再把拆卸器等消耗型道具装配到棋子身上",
    "  · 优化 极限AI训练停滞机制：大变异只动少量字段、精英不重评估、突破复核过滤运气",
    "  · 优化 训练弹窗显示本代最优分，替代易误导的最后候选分",
    "",
    "v1.3.0  金铲铲之战对标·伐木羁绊与道具权限完整版",
    "  · 新增 伐木（Lumber）羁绊三档：3/5/8，8伐木为棱彩终极羁绊",
    "  · 新增 巨斧选择器：物品栏常驻、不消耗、跨回合保留首领标记",
    "  · 新增 3伐木首领吸收最近2名伐木弈子90%生命并获得临时属性",
    "  · 新增 5伐木全体伐木弈子法强/物攻加成，首领双倍",
    "  · 新增 8伐木召唤远古树灵：继承全队75%生命攻击与首领装备",
    "  · 新增 昊天锤：卸下全部装备→重铸→装回原棋子",
    "  · 新增 装备拆卸器：卸下装备入物品栏，满栏溢出仓库",
    "  · 新增 大妮蔻：复制目标1星棋子入备战席，满备战席不消耗",
    "  · 新增 纹章之书：备战席伪棋子，出售触发4选1纹章弹窗",
    "  · 新增 战斗界面备战席面板开关：战斗中可出售/合成/用道具",
    "  · 新增 棋子详情弹窗统一出售按钮，战斗棋盘棋子拦截出售",
    "  · 优化 羁绊弹窗：标题固定头部、内容两栏分栏、垂直滚动条",
    "  · 优化 HUD：金币栏连胜/连败徽章、利息满5提示",
    "  · 优化 物品栏两个散件拖拽重叠直接合成，特殊道具禁参合成",
    "  · 优化 战斗中普通散件可佩戴棋盘棋子，禁拆卸/禁合成",
    "  · 修复 纹章佩戴加羁绊、卸下去羁绊无残留、不重复叠加",
    "  · 修复 2-1野怪回合100%掉落装备拆卸器",
    "  · 修复 巨斧首领角标显示与战斗中模型放大1.2倍",
    "  · 测试 五套自动化回归（全机制/对局存档/事件注入/专项/长时压力）全部通过",
    "",
    "v1.2.9  财宝秘境与全新宝物系统完整版",
    "  · 新增 羁绊阈值全面调整：药剂族/豹族/蛙族/伐木/舞者/长老/雷霆/财宝猎人",
    "  · 新增 财宝猎人收菜系统：藏宝碎片、层数、收宝离场、深入寻宝",
    "  · 新增 财宝猎人第2-9层奖励池与高阶掠夺规则",
    "  · 新增 8财宝棱彩捕获机制：战斗中捕获敌方弈子并获得藏宝碎片",
    "  · 新增 豹灵符、药灵符及普通转职合成系统",
    "  · 新增 豹灵符/药灵符与散件的差异化转职配方",
    "  · 新增 豹药神符、肥豹神符、药烂神符三种神符",
    "  · 新增 三神符套装效果：装备齐全后持续获得金币",
    "  · 新增 财宝猎人转职特殊规则：不可普通合成，可通过收菜/昊天锤获得",
    "  · 新增 转职装备限制：同一棋子禁止重复同类转职，原生同羁绊棋子禁止装备对应转职",
    "  · 新增 昊天锤：可将装备/转职/灵符等特殊资源转换为其他资源",
    "  · 新增 装备拆卸器：可拆卸棋子装备",
    "  · 新增 大妮蔻：复制1星英雄",
    "  · 新增 纹章之书：提供4个随机转职选择",
    "  · 新增 光明宝箱：根据棋子推荐装备提供光明装备选择",
    "  · 新增 杰作升级器：将普通成装升级为光明装备",
    "  · 新增 12种豹药神器及对应战斗效果",
    "  · 新增 光明装备系统：普通成装的强化版本与独立属性",
    "  · 新增 三星五费强化与专属高光表现系统",
    "  · 新增 1-1本局强化宝物获取途径：转职、灵符、神符、神器、光明装备及特殊道具",
    "  · 新增 海克斯/强化符文宝物获取途径",
    "  · 优化 宝物与强化符文资源分层获取，增加对局随机性与构筑选择",
    "  · 新增 财宝猎人羁绊说明与收菜进度提示",
    "  · 修复 特殊道具、掠夺规则、纹章之书、光明宝箱等系统之间的连接问题",
    "  · 修复 转职特殊键名、装备类型与部分奖励生成问题",
    "  · 修复 启动自检变量名错误及缺少 re 模块问题",
    "  · 优化 全局自检与版本1.2.9功能验收",
    "",
    "v1.2.8  检测更新与界面优化版",
    "  · 新增 检测更新与自动更新功能",
    "  · 新增 主菜单'检测更新'按钮",
    "  · 新增 更新弹窗与版本比对",
    "  · 新增 详情面板显示法术/物理标签",
    "  · 优化 羁绊弹窗按费用排序+显示费用",
    "  · 优化 羁绊弹窗区分上场/未上场棋子",
    "  · 修复 职业羁绊不显示棋子的问题",
    "",
    "v1.2.7  界面与显示优化版",
    "  · 新增 设置菜单'查看更新日志'入口",
    "  · 新增 18 个新英雄技能中文名",
    "  · 优化 商店卡面显示职业羁绊",
    "  · 修复 技能名显示英文的问题",
    "",
    "v1.2.6  职业与坦克扩展版",
    "  · 新增 4 种职业羁绊（坦克/射手/术士/战士）",
    "  · 新增 13 个英雄（8 坦克 + 5 射手）",
    "  · 新增 坦克技能多样化（举盾/爆盾/回血）",
    "  · 新增 护盾溅射伤害类型可切换",
    "  · 提升 药剂族/财宝猎人 阈值 [2,4,6,8]",
    "  · 修复 apply_poison / take_damage 若干",
    "",
    "v1.2.5  全面优化版",
    "  · 修复 共享英雄池并发预留与售罄检查",
    "  · 新增 点击装备查看详细属性",
    "  · 修复 自动布阵不再静默丢子",
    "",
    "v1.2.4  终极雷霆版",
    "  · 新增 雷霆六人组 + 雷霆羁绊",
    "  · 新增 雷霆AI助手（自动吐槽）",
    "  · 修复 网络半包/断线/平局重置",
]

AI_BEHAVIOR = {
    "easy": {"skip_chance": 0.30, "prune_board": False, "counter_pick": False,
             "smart_equip": False, "refresh_budget": 60, "level_reserve": 25},
    "normal": {"skip_chance": 0.08, "prune_board": True, "counter_pick": True,
               "smart_equip": True, "refresh_budget": None, "level_reserve": 20},
    "hard": {"skip_chance": 0.0, "prune_board": True, "counter_pick": True,
             "smart_equip": True, "refresh_budget": 25, "level_reserve": 14},
    "extreme": {"skip_chance": 0.0, "prune_board": True, "counter_pick": True,
                "smart_equip": True, "refresh_budget": 20, "level_reserve": 8},
}

SKILL_DMG_STAR_SCALE = {1: 1.0, 2: 1.65, 3: 3.1, 4: 4.8}
_ERR_SEEN = {}


def log_once(tag, exc=None):
    n = _ERR_SEEN.get(tag, 0) + 1
    _ERR_SEEN[tag] = n
    if n <= 3:
        print(f"[{tag}] {exc if exc is not None else ''}")


# ============================================================
#  检测更新
# ============================================================
def _parse_version(v):
    parts = []
    for seg in str(v).strip().split("."):
        try:
            parts.append(int(seg))
        except Exception:
            parts.append(0)
    return tuple(parts)


def check_for_update(timeout=6):
    if not UPDATE_CHECK_URL:
        return None
    try:
        req = urllib.request.Request(
            UPDATE_CHECK_URL, headers={"User-Agent": "BaoYaoUniverse"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="ignore")
        data = json.loads(raw)
        remote_ver = str(data.get("version", "")).strip()
        if not remote_ver:
            return None
        if _parse_version(remote_ver) <= _parse_version(CURRENT_VERSION):
            return None
        return {
            "version": remote_ver,
            "changelog": data.get("changelog", []) or [],
            "download_url": (data.get("download_url") or data.get("url") or ""),
        }
    except Exception as e:
        log_once("check_for_update", e)
        return None


import urllib.parse

def _atomic_write_bytes(path, data):
    """原子写入二进制文件：先写临时文件并fsync，再os.replace。"""
    directory = os.path.dirname(os.path.abspath(path)) or "."
    fd, tmp = tempfile.mkstemp(prefix=".baoyao_", suffix=".tmp", dir=directory)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
        return True
    except Exception:
        try:
            os.remove(tmp)
        except Exception:
            pass
        raise


def _atomic_write_text(path, text):
    return _atomic_write_bytes(path, text.encode("utf-8"))


def _validate_python_source(content, filename="<update>"):
    """更新覆盖前同时做UTF-8、AST、compile校验。"""
    text = content.decode("utf-8")
    ast.parse(text, filename=filename)
    compile(text, filename, "exec")
    return text


def _rotate_source_backups(src_path, text, keep=3):
    """保留多份源码备份，避免训练/更新共用单一bak互相覆盖。"""
    for i in range(keep, 0, -1):
        old = src_path + (".bak" if i == 1 else f".bak.{i-1}")
        new = src_path + f".bak.{i}"
        if os.path.exists(old):
            try:
                os.replace(old, new)
            except Exception:
                pass
    _atomic_write_text(src_path + ".bak", text)


def download_update(url, save_path, timeout=30):
    if not url:
        return False, "下载链接为空"
    tmp_path = save_path + ".new"
    try:
        if "raw.githubusercontent.com" in url:
            url = url.replace("raw.githubusercontent.com", "fastly.jsdelivr.net/gh")
            url = url.replace("/main/", "@main/")
        url = urllib.parse.quote(url, safe=':/?=&%#@')
        req = urllib.request.Request(url, headers={"User-Agent": "BaoYaoUniverse"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read()
        if len(content) < 500:
            return False, "文件过小"
        head = content[:2048].lstrip().lower()
        if b"<html" in head or b"<!doctype" in head:
            return False, "下载内容不是 Python 文件"
        try:
            text = _validate_python_source(content, save_path)
        except (UnicodeDecodeError, SyntaxError, ValueError) as e:
            return False, f"Python语法校验失败: {e}"
        with _SOURCE_WRITE_LOCK:
            _atomic_write_bytes(tmp_path, content)
            if os.path.exists(save_path):
                with open(save_path, "r", encoding="utf-8") as f:
                    old_text = f.read()
                # 备份也必须是可恢复源码
                ast.parse(old_text, filename=save_path)
                _rotate_source_backups(save_path, old_text, keep=3)
            os.replace(tmp_path, save_path)
        return True, ""
    except Exception as e:
        try:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        except Exception:
            pass
        log_once("download_update", e)
        return False, str(e)


def get_script_path():
    try:
        return os.path.abspath(__file__)
    except Exception:
        return ""


# ============================================================
#  存档系统
# ============================================================
SAVE_FILE = "savegame.pkl"


def save_game(gs):
    if gs.is_multiplayer:
        return False
    try:
        with _pool_lock:
            pool_snapshot = dict(_pool_remaining)
        data = {
            "version": 2,
            "difficulty": gs.difficulty,
            "me": gs.me,
            "players": gs.players,
            "stage": gs.stage,
            "round_counter": gs.round_counter,
            "shop": gs.shop,
            "shop_locked": gs.shop_locked,
            "global_augment": gs.global_augment,
            "bounty_shards": gs.bounty_shards,
            "bounty_layer_current": gs.bounty_layer_current,
            "bounty_last_layer_seen": gs.bounty_last_layer_seen,
            "bounty_layer_options": gs.bounty_layer_options,
            "pending_plunder": gs._pending_plunder,
            "active_plunder": gs._active_plunder,
            "bounty_capture_bonus": gs._bounty_capture_bonus,
            "pool_remaining": pool_snapshot,
            "battle_log_history": gs.battle_log_history[-20:],
        }
        directory = os.path.dirname(os.path.abspath(SAVE_FILE)) or "."
        fd, tmp = tempfile.mkstemp(prefix=".savegame_", suffix=".tmp", dir=directory)
        try:
            with os.fdopen(fd, "wb") as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, SAVE_FILE)
        except Exception:
            try:
                os.remove(tmp)
            except Exception:
                pass
            raise
        return True
    except Exception as e:
        log_once("save_game", e)
        return False


def has_save():
    return os.path.exists(SAVE_FILE)


def get_save_info():
    if not has_save():
        return None
    try:
        with open(SAVE_FILE, "rb") as f:
            data = pickle.load(f)
        stage = tuple(data.get("stage", (1, 1)))
        me = data.get("me", {}) or {}
        return {
            "stage": stage,
            "level": me.get("level", 1),
            "hp": me.get("hp", 100),
            "gold": me.get("gold", 0),
            "difficulty": data.get("difficulty", "normal"),
        }
    except Exception:
        return None


def delete_save():
    try:
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)
    except Exception:
        pass


def _validate_unit_schema(u):
    if not isinstance(u, dict):
        return u is None
    if not isinstance(u.get("name", ""), str):
        return False
    star = u.get("star", 1)
    if not isinstance(star, int) or not 1 <= star <= MAX_STAR:
        return False
    items = u.get("items", [])
    traits = u.get("traits", [])
    return isinstance(items, list) and isinstance(traits, list)


def _validate_player_schema(p):
    if not isinstance(p, dict):
        return False
    if not isinstance(p.get("board"), list) or len(p["board"]) != 4:
        return False
    if any(not isinstance(row, list) or len(row) != 7 for row in p["board"]):
        return False
    if not isinstance(p.get("bench"), list) or len(p["bench"]) != 8:
        return False
    if not isinstance(p.get("items", []), list):
        return False
    for row in p["board"]:
        if any(not _validate_unit_schema(u) for u in row):
            return False
    if any(not _validate_unit_schema(u) for u in p["bench"]):
        return False
    return True


def _validate_save_data(data):
    if not isinstance(data, dict):
        return False
    if not isinstance(data.get("me"), dict) or not _validate_player_schema(data["me"]):
        return False
    players = data.get("players")
    if not isinstance(players, list) or not players:
        return False
    if any(not _validate_player_schema(p) for p in players):
        return False
    stage = data.get("stage", (1, 1))
    if not isinstance(stage, (tuple, list)) or len(stage) != 2:
        return False
    pool = data.get("pool_remaining", {})
    if not isinstance(pool, dict):
        return False
    return True


def _is_wearable_for_recovery(it):
    try:
        return is_wearable_item(it)
    except Exception:
        return False


def load_game(gs):
    if not has_save():
        return False
    try:
        with open(SAVE_FILE, "rb") as f:
            data = pickle.load(f)
        if not _validate_save_data(data):
            bad = SAVE_FILE + ".bad"
            try:
                os.replace(SAVE_FILE, bad)
            except Exception:
                pass
            return False
        # 先对临时数据做脏道具清理，再一次性提交到GameState。
        players = data["players"]
        me = data["me"]
        _reclaim_illegal_equipped_items(me)
        for pl in players:
            _reclaim_illegal_equipped_items(pl)
        gs.difficulty = data.get("difficulty", gs.difficulty)
        gs.me = me
        gs.players = players
        gs.stage = tuple(data.get("stage", (1, 1)))
        gs.round_counter = int(data.get("round_counter", 0))
        gs.shop = data.get("shop", []) if isinstance(data.get("shop", []), list) else []
        gs.shop_locked = bool(data.get("shop_locked", False))
        gs.global_augment = data.get("global_augment", gs.global_augment)
        gs.bounty_shards = max(0, int(data.get("bounty_shards", 0)))
        gs.bounty_layer_current = max(1, min(9, int(data.get("bounty_layer_current", 1))))
        gs.bounty_last_layer_seen = max(1, min(9, int(data.get("bounty_last_layer_seen", 1))))
        gs.bounty_layer_options = data.get("bounty_layer_options", []) or []
        gs._pending_plunder = data.get("pending_plunder")
        gs._active_plunder = data.get("active_plunder")
        gs._bounty_capture_bonus = max(0, int(data.get("bounty_capture_bonus", 0)))
        saved_pool = data.get("pool_remaining", {})
        with _pool_lock:
            _pool_remaining.clear()
            for name, value in saved_pool.items():
                if isinstance(name, str) and isinstance(value, int) and value >= 0:
                    base = get_base_template(name)
                    if base and not base.get("no_shop"):
                        cap = POOL_SIZES.get(base.get("cost", 1), 20)
                        _pool_remaining[name] = min(cap, value)
        gs.battle_log_history = data.get("battle_log_history", [])[-20:]
        gs.show_starter_popup = False
        gs.show_global_augment_popup = False
        gs.starter_chosen = True
        gs.show_bounty_popup = False
        gs.phase_timer = PREP_DURATION
        gs.is_battle_phase = False
        gs.game_over = False
        gs.battles = []
        return True
    except (pickle.UnpicklingError, EOFError, AttributeError, ValueError, TypeError, OSError) as e:
        log_once("load_game", e)
        return False
    except Exception as e:
        log_once("load_game", e)
        return False


# ============================================================
#  联机模块
# ============================================================
class NetworkManager:
    DEFAULT_PORT = 5555

    def __init__(self):
        self.sock = None
        self.conn = None
        self.is_host = False
        self.connected = False
        self.port = self.DEFAULT_PORT
        self.peer_ip = ""
        self.error = ""
        self._accept_thread = None
        self._accepted = False
        self._connect_done = False
        self._recv_buf = b""
        self._pending_len = None

    @staticmethod
    def get_local_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"

    def start_host(self, port=DEFAULT_PORT):
        try:
            self.port = port
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind(("0.0.0.0", port))
            self.sock.listen(1)
            self.sock.settimeout(0.5)
            self.is_host = True
            self._accepted = False
            self.error = ""

            def _worker():
                while not self._accepted:
                    try:
                        conn, addr = self.sock.accept()
                        self.conn = conn
                        self.conn.settimeout(30)
                        self.peer_ip = addr[0]
                        self.connected = True
                        self._accepted = True
                        return
                    except socket.timeout:
                        continue
                    except Exception as e:
                        self.error = str(e)
                        return
            self._accept_thread = threading.Thread(target=_worker, daemon=True)
            self._accept_thread.start()
            return True
        except Exception as e:
            self.error = str(e)
            return False

    def connect(self, ip, port=DEFAULT_PORT, timeout=8):
        self._connect_done = False
        self.error = ""

        def _worker():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(timeout)
                s.connect((ip, port))
                s.settimeout(30)
                self.sock = s
                self.conn = s
                self.peer_ip = ip
                self.port = port
                self.connected = True
            except Exception as e:
                self.error = str(e)
            finally:
                self._connect_done = True
        threading.Thread(target=_worker, daemon=True).start()
        return True

    def send(self, data):
        if not self.conn:
            return False
        try:
            payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            header = len(payload).to_bytes(8, "big")
            self.conn.sendall(header + payload)
            return True
        except Exception as e:
            self.error = str(e)
            self.connected = False
            return False

    def recv(self, timeout=30):
        if not self.conn:
            return None
        try:
            self.conn.settimeout(timeout)
            if self._pending_len is None:
                header = self._recv_exact(8)
                if not header:
                    self.connected = False
                    return None
                length = int.from_bytes(header, "big")
                if length <= 0 or length > 2_000_000:
                    self.error = "网络数据包非法或过大"
                    self.connected = False
                    self.close()
                    return None
                self._pending_len = length
            data = self._recv_exact(self._pending_len)
            if data is None:
                self.connected = False
                return None
            self._pending_len = None
            obj = json.loads(data.decode("utf-8"))
            if not isinstance(obj, dict):
                raise ValueError("网络消息必须是JSON对象")
            return obj
        except socket.timeout:
            return None
        except Exception as e:
            self.error = str(e)
            self.connected = False
            return None

    def _recv_exact(self, n):
        while len(self._recv_buf) < n:
            try:
                need = n - len(self._recv_buf)
                chunk = self.conn.recv(max(1, min(65536, need)))
            except socket.timeout:
                return None
            except Exception as e:
                self.error = str(e)
                return None
            if not chunk:
                self.connected = False
                return None
            self._recv_buf += chunk
        result = self._recv_buf[:n]
        self._recv_buf = self._recv_buf[n:]
        return result

    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception:
            pass
        try:
            if self.sock:
                self.sock.close()
        except Exception:
            pass
        self.conn = None
        self.sock = None
        self.connected = False
        self.is_host = False
        self._accepted = False
        self._connect_done = False
        self.peer_ip = ""
        self._recv_buf = b""
        self._pending_len = None


def get_round_type(stage, rnd):
    if stage == 1:
        if rnd == 1:
            return "augment"
        return "monster"
    if rnd == 4:
        return "carousel"
    if rnd == 7:
        return "monster"
    return "pvp"


def get_stage_base_damage(stage):
    if stage <= 1:
        return 0
    if stage == 2:
        return 2
    if stage == 3:
        return 5
    if stage == 4:
        return 8
    return 10


def compute_player_damage(stage, enemy_alive_count):
    return get_stage_base_damage(stage) + max(0, enemy_alive_count)


POOL_SIZES = {1: 29, 2: 22, 3: 18, 4: 12, 5: 10}
_pool_remaining = {}
_pool_lock = threading.RLock()


def _make_pool_snapshot():
    return {c["name"]: POOL_SIZES.get(c.get("cost", 1), 20)
            for c in CHAMPION_LIST if not c.get("no_shop")}


def _active_pool():
    pool = getattr(_SIM_POOL_LOCAL, "pool", None)
    return pool if pool is not None else _pool_remaining


def init_pool():
    global _pool_remaining
    # 正常游戏初始化真实公共池；模拟器通过isolated_sim_pool()使用线程本地池。
    with _pool_lock:
        _pool_remaining = _make_pool_snapshot()


def consume_pool(name, count=1):
    """Consume available shared copies safely; returns the number consumed."""
    count = max(0, int(count))
    pool = _active_pool()
    lock = _pool_lock if pool is _pool_remaining else contextlib.nullcontext()
    with lock:
        if name not in pool or count <= 0:
            return 0
        consumed = min(count, pool[name])
        pool[name] -= consumed
        return consumed


def try_consume_pool(name, count=1):
    """Atomically reserve copies, preventing a stale shop from overselling."""
    count = max(0, int(count))
    pool = _active_pool()
    lock = _pool_lock if pool is _pool_remaining else contextlib.nullcontext()
    with lock:
        if name not in pool or pool[name] < count:
            return False
        pool[name] -= count
        return True


def return_pool(name, count=1):
    count = max(0, int(count))
    pool = _active_pool()
    lock = _pool_lock if pool is _pool_remaining else contextlib.nullcontext()
    with lock:
        if name not in pool or count <= 0:
            return 0
        base = get_base_template(name)
        cap = POOL_SIZES.get(base.get("cost", 1), 20) if base else 20
        before = pool[name]
        pool[name] = min(cap, before + count)
        return pool[name] - before


def pool_remaining(name):
    pool = _active_pool()
    lock = _pool_lock if pool is _pool_remaining else contextlib.nullcontext()
    with lock:
        return pool.get(name, 0)


CHAMP_NAME_CN = {
    "BearBig": "熊大", "BearTwo": "熊二", "GuangTouQiang": "光头强",
    "JiJi": "吉吉", "MaoMao": "毛毛", "FeiBo": "肥波",
    "BengBeng": "蹦蹦", "TuTu": "涂涂", "LaoE": "老鳄", "FeiFei": "肥肥",
    "Tuanzi": "团子", "AncientTree": "远古树灵",
    "EmblemTome": "纹章之书",
    "PotionPouch": "药剂袋", "CubLeopard": "豹崽", "MilkFrog": "奶蛙",
    "LoggerStrong": "力伐木", "LeopardPotion": "豹药剂", "SweatyElder": "汗长老",
    "NiuLai": "牛来", "MJWalker": "迈克步", "BaoLan": "豹兰",
    "SuperLogger": "超伐木", "GodFrog": "神蛙", "PotionCreator": "药剂师",
    "RuneApprentice": "符文学徒", "CrystalOracle": "水晶先知",
    "RuneArcher": "符文射手", "StormKnight": "风暴骑士", "ArcaneLord": "秘法领主",
    "Wolf": "野狼", "Boar": "野猪", "Golem": "石魔",
    "Dragon": "远古巨龙", "Treant": "树人", "Crab": "甲蟹",
    "XiaoDie": "小蝶", "LaoGui": "老龟",
    "ThunderHelper": "雷霆助手", "ThunderLicker": "雷霆舔狗",
    "ThunderComment": "雷霆注释", "ThunderPotato": "雷霆土豆",
    "ThunderGoddess": "雷霆女神", "ThunderPatch": "雷霆补丁",
    "PotionLeopard": "药铠豹垣", "OxKui": "沉轭牛岿",
    "FrogBulwark": "厚蛙盾胚", "BearFortress": "墟熊重胄",
    "PotionKeep": "定瓶守匣", "ThornGuard": "斑棘宿卫",
    "OxBastion": "岩轭驮卫", "AncientVial": "淬药古坨",
    "LeopardBow": "纹豹淬弩", "FrogBomb": "泡蛙弹囊",
    "OxGunner": "轭牛铳手", "VialSniper": "瓶芯飞针",
    "SwiftStrike": "疾斑掠弹",
}
TRAIT_NAME_CN = {
    "PotionClan": "药剂族", "LeopardKind": "豹族", "FrogTribe": "蛙族",
    "Lumber": "伐木", "Dancer": "舞者", "Elder": "长老",
    "BearRidge": "狗熊岭", "RuneLand": "符文大陆", "Summon": "召唤物",
    "Treasure": "财宝猎人",
    "Thunder": "雷霆",
    "ClassTank": "坦克", "ClassArcher": "射手",
    "ClassMage": "术士", "ClassWarrior": "战士",
}

TRAIT_SHORT_CN = {
    "PotionClan": "药剂", "LeopardKind": "豹族", "FrogTribe": "蛙族",
    "Lumber": "伐木", "Dancer": "舞者", "Elder": "长老",
    "BearRidge": "狗熊", "RuneLand": "符文", "Summon": "召唤",
    "Treasure": "财宝",
    "Thunder": "雷霆",
    "ClassTank": "坦克", "ClassArcher": "射手",
    "ClassMage": "术士", "ClassWarrior": "战士",
}
SKILL_NAME_CN = {
    "Potion Spray": "药剂喷洒", "Pounce": "猛扑", "Frog Resonance": "蛙鸣共鸣",
    "Axe Sweep": "战斧横扫", "Poison Assault": "剧毒突袭", "Mist Aura": "迷雾光环",
    "Bull Rush": "蛮牛冲撞", "Moonwalk": "月球漫步", "Doom Leopard": "末日豹",
    "Super Power Pill": "超能药剂", "Global Heal": "群体治疗",
    "Potion Nuke": "药剂轰击", "Arcane Bolt": "秘法弹",
    "Crystal Veil": "水晶帷幕", "Mana Shot": "法力射击",
    "Thunder Strike": "雷霆一击", "Arcane Nova": "秘法新星",
    "Forest Guard": "森林守护", "Bear Paw": "熊掌拍击",
    "Logging Strike": "伐木打击", "Banana Barrage": "香蕉弹幕",
    "Monkey King": "猴王怒吼", "Fat Wave": "肥波气场",
    "Flying Jump": "蹦跳突袭", "Owl Wisdom": "夜枭智慧",
    "Croc Bite": "巨鳄撕咬", "Bear Charge": "巨熊冲锋",
    "Lumberjack Rage": "光头强暴怒", "Ice Seal": "冰封之力",
    "Tree Smash": "巨木碾压",
    "Bite": "撕咬", "Charge": "冲撞", "Rock Throw": "投石",
    "Fire Breath": "龙焰", "Vine Whip": "藤鞭", "Bubble": "气泡",
    "Butterfly Dance": "蝶舞", "Ancient Shell": "远古甲壳",
    "Potion Barrier": "药剂屏障", "Ox Charge": "蛮牛冲锋",
    "Gel Shield": "凝胶之盾", "Roar Guard": "咆哮守御",
    "Vial Fortress": "瓶壘要塞", "Thorn Burst": "棘刺爆裂",
    "Ox Aegis": "牯牛神盾", "Ancestral Boil": "祖药沸腾",
    "Venom Bolt": "毒液箭", "Toxic Bomb": "剧毒炸弹",
    "Heavy Shot": "重炮轰击", "Needle Storm": "飞针风暴",
    "Swift Barrage": "疾影连射",
    "Thunder Brain": "雷霆之脑", "Lick": "舔狗之舌",
    "Comment": "注释弹幕", "Potato": "土豆壁垒",
    "Goddess": "女神之光", "Patch": "更新补丁",
}

def champ_cn(n):
    return CHAMP_NAME_CN.get(n, n)


def trait_cn(k):
    return TRAIT_NAME_CN.get(k, k)


def trait_short_cn(k):
    return TRAIT_SHORT_CN.get(k, k[:2])


def skill_cn(s):
    return SKILL_NAME_CN.get(s, s)


def set_dbg(m):
    global DBG_LAST
    DBG_LAST = m


_SCRIPT_DIR = ""
try:
    _SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except Exception:
    _SCRIPT_DIR = os.getcwd()

_CJK_FONT_CANDIDATES = [
    os.path.join(_SCRIPT_DIR, "NotoSansCJK-Regular.otf"),
    os.path.join(_SCRIPT_DIR, "NotoSansCJK-Regular.ttf"),
    "C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf",
    "/System/Library/Fonts/PingFang.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
]
_CJK_FONT_PATH = None
_CJK_FONT_NAME = None


def _find_cjk_font():
    global _CJK_FONT_PATH, _CJK_FONT_NAME
    if _CJK_FONT_PATH is not None:
        return _CJK_FONT_PATH, _CJK_FONT_NAME
    for path in _CJK_FONT_CANDIDATES:
        try:
            if os.path.exists(path):
                pygame.font.Font(path, 16)
                _CJK_FONT_PATH = path
                return _CJK_FONT_PATH, _CJK_FONT_NAME
        except Exception:
            continue
    for name in ("microsoftyahei", "simhei", "pingfang",
                 "notosanscjksc", "wenquanyimicrohei"):
        try:
            pygame.font.SysFont(name, 16)
            _CJK_FONT_PATH = ""
            _CJK_FONT_NAME = name
            return _CJK_FONT_PATH, _CJK_FONT_NAME
        except Exception:
            continue
    _CJK_FONT_PATH = ""
    _CJK_FONT_NAME = None
    return _CJK_FONT_PATH, _CJK_FONT_NAME


_FONT_CACHE = {}


def get_font(size):
    if size not in _FONT_CACHE:
        path, name = _find_cjk_font()
        try:
            if path:
                _FONT_CACHE[size] = pygame.font.Font(path, size)
            elif name:
                _FONT_CACHE[size] = pygame.font.SysFont(name, size)
            else:
                _FONT_CACHE[size] = pygame.font.Font(None, size)
        except Exception:
            _FONT_CACHE[size] = pygame.font.Font(None, size)
    return _FONT_CACHE[size]


def _make_sound(samples):
    if not AUDIO_OK:
        return None
    try:
        buf = array.array("h")
        for s in samples:
            v = int(max(-1.0, min(1.0, s)) * 32767)
            buf.append(v)
        if sys.byteorder == "big":
            buf.byteswap()
        snd = pygame.mixer.Sound(buffer=buf.tobytes())
        try:
            snd.set_volume(0.9)
        except Exception:
            pass
        return snd
    except Exception:
        return None


def gen_simple(freqs, dur=0.15, vol=0.12):
    if not AUDIO_OK:
        return None
    try:
        n = int(22050 * dur)
        out = []
        for i in range(n):
            t = i / 22050
            f = freqs[min(len(freqs) - 1, int(t / dur * len(freqs)))]
            env = (1 - i / n) ** 1.2
            out.append(math.sin(2 * math.pi * f * t) * vol * env)
        return _make_sound(out)
    except Exception:
        return None


def gen_noise(dur=0.15, vol=0.12):
    if not AUDIO_OK:
        return None
    try:
        n = int(22050 * dur)
        out = []
        for i in range(n):
            t = i / 22050
            env = (1 - i / n) ** 1.5
            out.append(random.uniform(-1, 1) * vol * env)
        return _make_sound(out)
    except Exception:
        return None


SND_HIT = gen_noise(0.05, 0.10)
SND_SKILL = gen_simple([440, 587, 740], 0.2, 0.15)
SND_DEATH = gen_noise(0.15, 0.12)
SND_SELL = gen_simple([500, 400], 0.1, 0.12)
SND_HEX = gen_simple([523, 659, 784, 1047], 0.3, 0.14)
SND_CLICK = gen_simple([900], 0.035, 0.09)
SND_BUY = gen_simple([523, 784], 0.13, 0.13)
SND_ERROR = gen_simple([180], 0.12, 0.15)
SND_COIN = gen_simple([1318, 1975], 0.1, 0.12)
SND_VICTORY = gen_simple([523, 659, 784, 1047], 0.5, 0.12)
# 三星五费专属音效：每个棋子使用不同音程组合。
ULT_SFX_FREQS = {
    "Dragon": [220, 330, 440, 660], "GuangTouQiang": [196, 247, 294, 392],
    "BaoLan": [262, 330, 523, 784], "SuperLogger": [174, 220, 277, 349],
    "GodFrog": [330, 415, 523, 659], "PotionCreator": [247, 311, 392, 622],
    "ArcaneLord": [196, 294, 440, 587], "Tuanzi": [392, 494, 659, 988],
    "ThunderPatch": [233, 311, 466, 932], "AncientVial": [185, 277, 370, 555],
    "SwiftStrike": [294, 370, 554, 831],
}
SND_ULT = {k: gen_simple(v, 0.34, 0.16) for k, v in ULT_SFX_FREQS.items()}
_sfx_cooldown = {k: 0.0 for k in
                 ("hit", "skill", "death", "sell", "hex",
                  "click", "buy", "error", "coin", "victory")}


def play_sfx(name):
    if not AUDIO_OK:
        # 导入时音频可能未就绪：首次播音再重试一次
        _try_init_audio()
    if not AUDIO_OK:
        return
    if _sfx_cooldown.get(name, 0) > 0:
        return
    snd = {"hit": SND_HIT, "skill": SND_SKILL, "death": SND_DEATH,
           "sell": SND_SELL, "hex": SND_HEX, "click": SND_CLICK,
           "buy": SND_BUY, "error": SND_ERROR, "coin": SND_COIN,
           "victory": SND_VICTORY}.get(name)
    if snd is None and name.startswith("ult_"):
        snd = SND_ULT.get(name[4:])
    if snd:
        try:
            snd.play()
        except Exception:
            pass
    _sfx_cooldown[name] = 0.05


def tick_sfx_cooldown(dt):
    for k in _sfx_cooldown:
        if _sfx_cooldown[k] > 0:
            _sfx_cooldown[k] -= dt


ITEMS = {
    "sword": {"name": "暴风大剑", "stats": {"ad": 15}, "color": (220, 100, 100)},
    "bow": {"name": "反曲弓", "stats": {"atk_speed": 0.15}, "color": (140, 220, 140)},
    "rod": {"name": "无用大棒", "stats": {"sp": 15}, "color": (200, 140, 240)},
    "tear": {"name": "女神之泪", "stats": {"mana": -15}, "color": (100, 180, 255)},
    "belt": {"name": "巨人腰带", "stats": {"hp": 150}, "color": (255, 160, 100)},
    "vest": {"name": "锁子甲", "stats": {"armor": 20}, "color": (170, 170, 190)},
    "cloak": {"name": "负极斗篷", "stats": {"mr": 20}, "color": (140, 200, 220)},
    "glove": {"name": "拳套", "stats": {"crit": 0.20}, "color": (255, 220, 120)},
}
# 豹灵符/药灵符是新散件；合成神符由 COMBINE_TABLE 处理。
ITEMS.update({
    "leopard_talisman": {"name": "豹灵符", "stats": {}, "color": (180, 90, 255)},
    "potion_talisman": {"name": "药灵符", "stats": {}, "color": (180, 90, 255)},
})
ITEM_IDS = [iid for iid in ITEMS.keys() if iid not in ("leopard_talisman", "potion_talisman")]

COMBINE_TABLE = {
    frozenset(["sword", "sword"]): {"name": "无尽之刃", "stats": {"ad": 40, "crit": 0.30}, "color": (255, 180, 60)},
    frozenset(["bow", "bow"]): {"name": "疾射火炮", "stats": {"atk_speed": 0.60, "range": 200}, "color": (140, 255, 140)},
    frozenset(["rod", "rod"]): {"name": "卢登的回声", "stats": {"sp": 60}, "color": (200, 100, 240)},
    frozenset(["tear", "tear"]): {"name": "蓝霸符", "stats": {"mana": -40, "sp": 20}, "color": (100, 200, 255)},
    frozenset(["belt", "belt"]): {"name": "狂徒铠甲", "stats": {"hp": 500}, "color": (255, 120, 60)},
    frozenset(["vest", "vest"]): {"name": "荆棘之甲", "stats": {"armor": 60}, "color": (200, 200, 220)},
    frozenset(["cloak", "cloak"]): {"name": "龙牙", "stats": {"mr": 60}, "color": (140, 220, 255)},
    frozenset(["glove", "glove"]): {"name": "正义之手",
                                     "stats": {"crit": 0.40, "ad": 30, "population": 1},
                                     "color": (255, 240, 120)},
    frozenset(["sword", "bow"]): {"name": "挑战护手", "stats": {"ad": 20, "atk_speed": 0.30}, "color": (200, 180, 100)},
    frozenset(["sword", "rod"]): {"name": "海克斯枪刃", "stats": {"ad": 20, "sp": 20}, "color": (220, 120, 200)},
    frozenset(["sword", "tear"]): {"name": "朔极之矛", "stats": {"ad": 20, "mana": -20}, "color": (140, 180, 255)},
    frozenset(["sword", "belt"]): {"name": "巨兽杀手", "stats": {"ad": 25, "hp": 200}, "color": (255, 140, 100)},
    frozenset(["sword", "vest"]): {"name": "斯特拉克", "stats": {"ad": 25, "armor": 30}, "color": (200, 160, 140)},
    frozenset(["sword", "cloak"]): {"name": "夜之锋刃", "stats": {"ad": 25, "mr": 30}, "color": (180, 180, 220)},
    frozenset(["sword", "glove"]): {"name": "饮血剑", "stats": {"ad": 30, "crit": 0.20}, "color": (255, 100, 100)},
    frozenset(["bow", "rod"]): {"name": "电刃", "stats": {"atk_speed": 0.30, "sp": 20}, "color": (200, 200, 240)},
    frozenset(["bow", "tear"]): {"name": "古兹马", "stats": {"atk_speed": 0.30, "mana": -20}, "color": (140, 220, 255)},
    frozenset(["bow", "belt"]): {"name": "破败王者", "stats": {"atk_speed": 0.30, "hp": 200}, "color": (180, 220, 140)},
    frozenset(["bow", "vest"]): {"name": "泰坦的坚决", "stats": {"atk_speed": 0.30, "armor": 30}, "color": (160, 200, 160)},
    frozenset(["bow", "cloak"]): {"name": "卢安娜飓风", "stats": {"atk_speed": 0.35, "mr": 20}, "color": (200, 240, 200)},
    frozenset(["bow", "glove"]): {"name": "最后的轻语", "stats": {"atk_speed": 0.35, "crit": 0.30}, "color": (220, 240, 160)},
    frozenset(["rod", "tear"]): {"name": "大天使之杖", "stats": {"sp": 40, "mana": -20}, "color": (200, 160, 255)},
    frozenset(["rod", "belt"]): {"name": "莫雷洛秘典", "stats": {"sp": 40, "hp": 200}, "color": (230, 130, 200)},
    frozenset(["rod", "vest"]): {"name": "中娅沙漏", "stats": {"sp": 40, "armor": 30}, "color": (180, 180, 240)},
    frozenset(["rod", "cloak"]): {"name": "离子火花", "stats": {"sp": 40, "mr": 30}, "color": (200, 180, 255)},
    frozenset(["rod", "glove"]): {"name": "珠光护手", "stats": {"sp": 40, "crit": 0.30}, "color": (240, 160, 255)},
    frozenset(["tear", "belt"]): {"name": "救赎", "stats": {"mana": -20, "hp": 300}, "color": (140, 200, 220)},
    frozenset(["tear", "vest"]): {"name": "冰霜之心", "stats": {"mana": -20, "armor": 40}, "color": (150, 200, 240)},
    frozenset(["tear", "cloak"]): {"name": "女妖之爪", "stats": {"mana": -20, "mr": 40}, "color": (160, 220, 255)},
    frozenset(["tear", "glove"]): {"name": "希望之刃", "stats": {"mana": -20, "crit": 0.30}, "color": (200, 220, 255)},
    frozenset(["belt", "vest"]): {"name": "守护天使",
                                   "stats": {"hp": 250, "armor": 20, "population": 1},
                                   "color": (255, 200, 120)},
    frozenset(["belt", "cloak"]): {"name": "暗裔", "stats": {"hp": 250, "mr": 20}, "color": (255, 180, 160)},
    frozenset(["belt", "glove"]): {"name": "视界专注", "stats": {"hp": 300, "crit": 0.20}, "color": (255, 220, 160)},
    frozenset(["vest", "cloak"]): {"name": "石像鬼石板", "stats": {"armor": 30, "mr": 30}, "color": (200, 200, 230)},
    frozenset(["vest", "glove"]): {"name": "冰脉护手", "stats": {"armor": 30, "crit": 0.20}, "color": (200, 200, 200)},
    frozenset(["cloak", "glove"]): {"name": "水银", "stats": {"mr": 30, "crit": 0.20}, "color": (200, 220, 240)},
}

# 光明装备：普通成装的强化版本。无法由两件普通散件直接合成。
RADIANT_ITEM_DATA = {}
for _key, _data in COMBINE_TABLE.items():
    if _key & {"leopard_talisman", "potion_talisman"}:
        continue
    _base_name = _data["name"]
    _stats = dict(_data.get("stats", {}))
    for _k, _v in list(_stats.items()):
        if isinstance(_v, (int, float)) and _k != "population":
            _stats[_k] = int(_v * 1.35) if isinstance(_v, int) else round(_v * 1.35, 3)
    RADIANT_ITEM_DATA[_base_name] = {
        "name": "光明" + _base_name,
        "stats": _stats,
        "color": (255, 225, 120),
        "is_radiant": True,
        "desc": "光明成装：普通成装强化版",
    }

def make_radiant_item(base_name):
    d = RADIANT_ITEM_DATA.get(base_name)
    if not d:
        return None
    return {
        "id": "radiant_" + re.sub(r"\W+", "_", base_name),
        "name": d["name"],
        "stats": dict(d["stats"]),
        "color": d["color"],
        "is_combined": True,
        "is_radiant": True,
        "desc": d["desc"],
    }

def random_radiant_item():
    if not RADIANT_ITEM_DATA:
        return None
    return make_radiant_item(random.choice(list(RADIANT_ITEM_DATA)))



# 转职神符合成：豹灵符/药灵符通过两两合成获得三种神符。
COMBINE_TABLE.update({
    frozenset(["leopard_talisman", "potion_talisman"]): {
        "name": "豹药神符", "stats": {"population": 1},
        "color": (255, 180, 80), "rune_kind": "leopard_potion"},
    frozenset(["leopard_talisman", "leopard_talisman"]): {
        "name": "肥豹神符", "stats": {"population": 1},
        "color": (255, 120, 180), "rune_kind": "fat_leopard"},
    frozenset(["potion_talisman", "potion_talisman"]): {
        "name": "药烂神符", "stats": {"population": 1},
        "color": (120, 230, 140), "rune_kind": "rotten_potion"},
})



# 普通转职合成：灵符 + 散件。财宝猎人不进入此表，只能收菜或昊天锤转换。
# 同一散件下，豹灵符与药灵符故意对应不同羁绊。
EMBLEM_RECIPES = {
    ("leopard_talisman", "sword"): "LeopardKind",
    ("potion_talisman", "sword"): "PotionClan",
    ("leopard_talisman", "bow"): "Dancer",
    ("potion_talisman", "bow"): "LeopardKind",
    ("leopard_talisman", "rod"): "Thunder",
    ("potion_talisman", "rod"): "FrogTribe",
    ("leopard_talisman", "tear"): "Elder",
    ("potion_talisman", "tear"): "Lumber",
    ("leopard_talisman", "belt"): "FrogTribe",
    ("potion_talisman", "belt"): "Dancer",
    ("leopard_talisman", "vest"): "Lumber",
    ("potion_talisman", "vest"): "Elder",
    ("leopard_talisman", "cloak"): "PotionClan",
    ("potion_talisman", "cloak"): "Thunder",
    ("leopard_talisman", "glove"): "BearRidge",
    ("potion_talisman", "glove"): "RuneLand",
}
for (_a, _b), _trait in EMBLEM_RECIPES.items():
    _result_name = trait_cn(_trait) + "纹章"
    COMBINE_TABLE[frozenset([_a, _b])] = {
        "name": _result_name, "stats": {},
        "color": (220, 180, 80),
        "is_emblem": True, "emblem_trait": _trait,
    }


def new_item(iid):
    item = {"id": iid, "name": ITEMS[iid]["name"],
            "stats": dict(ITEMS[iid]["stats"]), "color": ITEMS[iid]["color"],
            "is_combined": False, "item_type": "wearable"}
    if iid == "leopard_talisman":
        item["is_rune"] = True
        item["rune_kind"] = "leopard"
        item["desc"] = RUNE_ITEM_DATA["leopard"]["desc"]
    elif iid == "potion_talisman":
        item["is_rune"] = True
        item["rune_kind"] = "potion"
        item["desc"] = RUNE_ITEM_DATA["potion"]["desc"]
    return item


def try_combine_items(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a = items[i]
            b = items[j]
            if a.get("is_combined") or b.get("is_combined"):
                continue
            key = frozenset([a.get("id", ""), b.get("id", "")])
            if key in COMBINE_TABLE:
                r = COMBINE_TABLE[key]
                new_it = {"id": "combined_" + "_".join(sorted(key)),
                          "name": r["name"], "stats": dict(r["stats"]),
                          "color": r["color"], "is_combined": True,
                          "item_type": "wearable"}
                if r.get("rune_kind"):
                    new_it["rune_kind"] = r["rune_kind"]
                    new_it["is_rune"] = True
                    new_it["desc"] = RUNE_ITEM_DATA[r["rune_kind"]]["desc"]
                if r.get("is_emblem"):
                    new_it["is_emblem"] = True
                    new_it["is_special"] = True
                    new_it["special_kind"] = "emblem_generic"
                    new_it["emblem_trait"] = r["emblem_trait"]
                    new_it["desc"] = "装备后激活" + trait_cn(r["emblem_trait"]) + "羁绊。"
                result = [it for k, it in enumerate(items) if k != i and k != j]
                result.append(new_it)
                return result, True
    return items, False


def try_combine_items_all(items):
    while True:
        items, combined = try_combine_items(items)
        if not combined:
            return items


_EMPTY_ITEM_STATS = {"ad": 0, "hp": 0, "sp": 0, "atk_speed": 0.0,
                     "crit": 0.0, "mana": 0, "armor": 0, "mr": 0, "range": 0,
                     "population": 0}


def get_unit_item_stats(unit):
    stats = dict(_EMPTY_ITEM_STATS)
    for item in unit.get("items", []):
        for k, v in item.get("stats", {}).items():
            stats[k] = stats.get(k, 0) + v
    return stats


def item_stat_text(item):
    stats = item.get("stats", {})
    parts = []
    if stats.get("ad"):
        parts.append(f"攻击+{stats['ad']}")
    if stats.get("hp"):
        parts.append(f"生命+{stats['hp']}")
    if stats.get("sp"):
        parts.append(f"法强+{stats['sp']}")
    if stats.get("atk_speed"):
        parts.append(f"攻速+{int(stats['atk_speed']*100)}%")
    if stats.get("crit"):
        parts.append(f"暴击+{int(stats['crit']*100)}%")
    if stats.get("mana"):
        parts.append(f"法力{stats['mana']}")
    if stats.get("armor"):
        parts.append(f"护甲+{stats['armor']}")
    if stats.get("mr"):
        parts.append(f"魔抗+{stats['mr']}")
    if stats.get("range"):
        parts.append(f"射程+{stats['range']}")
    if stats.get("population"):
        parts.append(f"人口+{stats['population']}")
    return " ".join(parts) if parts else "无属性"


MONSTER_DATA = {
    "Wolf": {"hp": 700, "ad": 40, "role": "warrior", "cost": 1,
             "traits": ["Summon"], "attack_range": 90, "attack_cooldown": 1.1,
             "max_mana": 30, "mana_per_attack": 10, "sp_base_dmg": 50,
             "sp_multiplier": 1.2, "skill_desc": "Bite"},
    "Boar": {"hp": 850, "ad": 55, "role": "warrior", "cost": 1,
             "traits": ["Summon"], "attack_range": 100, "attack_cooldown": 1.3,
             "max_mana": 40, "mana_per_attack": 10, "sp_base_dmg": 80,
             "sp_multiplier": 1.4, "skill_desc": "Charge"},
    "Golem": {"hp": 1400, "ad": 40, "role": "tank", "cost": 2,
              "traits": ["Summon"], "attack_range": 90, "attack_cooldown": 1.5,
              "max_mana": 60, "mana_per_attack": 8, "sp_base_dmg": 100,
              "sp_multiplier": 1.6, "skill_desc": "Rock Throw"},
    "Treant": {"hp": 1100, "ad": 60, "role": "warrior", "cost": 2,
               "traits": ["Summon"], "attack_range": 120, "attack_cooldown": 1.4,
               "max_mana": 50, "mana_per_attack": 10, "sp_base_dmg": 120,
               "sp_multiplier": 1.5, "skill_desc": "Vine Whip"},
    "Crab": {"hp": 1500, "ad": 55, "role": "tank", "cost": 3,
             "traits": ["Summon"], "attack_range": 90, "attack_cooldown": 1.5,
             "max_mana": 55, "mana_per_attack": 9, "sp_base_dmg": 130,
             "sp_multiplier": 1.7, "skill_desc": "Bubble"},
    "Dragon": {"hp": 3000, "ad": 100, "role": "warrior", "cost": 5,
               "traits": ["Summon"], "attack_range": 130, "attack_cooldown": 1.2,
               "max_mana": 60, "mana_per_attack": 10, "sp_base_dmg": 300,
               "sp_multiplier": 2.0, "skill_desc": "Fire Breath"},
}


def make_monster_team(stage, rnd=1):
    if stage == 1:
        if rnd == 2:
            n, hp_mult, ad_mult = 2, 0.30, 0.30
            pool = ["Wolf", "Wolf", "Boar"]
        elif rnd == 3:
            n, hp_mult, ad_mult = 3, 0.30, 0.35
            pool = ["Wolf", "Boar", "Boar", "Golem"]
        else:
            n, hp_mult, ad_mult = 4, 0.30, 0.35
            pool = ["Wolf", "Boar", "Golem", "Treant"]
    elif stage == 2:
        n, hp_mult, ad_mult = 4, 0.85, 0.90
        pool = ["Wolf", "Boar", "Golem", "Treant"]
    elif stage == 3:
        n, hp_mult, ad_mult = 5, 1.10, 1.10
        pool = ["Boar", "Golem", "Treant", "Crab"]
    elif stage == 4:
        n, hp_mult, ad_mult = 5, 1.40, 1.30
        pool = ["Golem", "Treant", "Crab", "Crab"]
    elif stage == 5:
        n, hp_mult, ad_mult = 6, 1.75, 1.50
        pool = ["Golem", "Crab", "Treant", "Crab"]
    elif stage == 6:
        n, hp_mult, ad_mult = 6, 2.10, 1.70
        pool = ["Crab", "Dragon", "Golem"]
    else:
        extra = (stage - 6) * 0.4
        n = 7
        hp_mult = 2.10 + extra
        ad_mult = 1.70 + extra * 0.7
        pool = ["Crab", "Dragon", "Golem", "Dragon"]
    board = [[None] * 7 for _ in range(4)]
    slots_front = [(0, 2), (0, 3), (0, 1), (1, 2), (1, 3), (0, 4), (1, 4)]
    slots_back = [(3, 2), (3, 3), (3, 1), (2, 2), (2, 3), (3, 4), (2, 4)]
    all_slots = slots_front + slots_back
    for i in range(n):
        if i >= len(all_slots):
            break
        name = random.choice(pool)
        base = MONSTER_DATA[name]
        u = safe_unit(copy.deepcopy(base))
        u["name"] = name
        u["star"] = 1
        u["hp"] = max(30, int(base["hp"] * hp_mult))
        u["ad"] = max(5, int(base["ad"] * ad_mult))
        u["sp_base_dmg"] = max(5, int(base.get("sp_base_dmg", 0) * ad_mult * 0.85))
        slot = all_slots[i]
        board[slot[0]][slot[1]] = u
    return {
        "gold": 0, "hp": 999, "level": 9, "xp": 0, "xp_next": 999,
        "win_streak": 0, "lose_streak": 0,
        "hex_bonuses": {"hp_mult": 0.0, "atk_mult": 0.0, "sp_mult": 0.0,
                        "crit": 0.0, "atk_speed": 0.0, "income": 0, "armor": 0},
        "hex_list": [], "items": [], "board": board, "bench": [None] * 8,
        "shop": [], "is_monster": True
    }


HEX_LIST = [
    {"name": "巨人之力", "rarity": "silver", "desc": "全体 +10% 最大生命",
     "effect": "hp_mult", "value": 0.10},
    {"name": "利刃精通", "rarity": "silver", "desc": "全体 +10% 攻击力",
     "effect": "atk_mult", "value": 0.10},
    {"name": "秘法光辉", "rarity": "silver", "desc": "全体 +15% 法术强度",
     "effect": "sp_mult", "value": 0.15},
    {"name": "致命律动", "rarity": "silver", "desc": "全体 +15% 暴击率",
     "effect": "crit", "value": 0.15},
    {"name": "迅捷之靴", "rarity": "silver", "desc": "全体 +15% 攻速",
     "effect": "atk_speed", "value": 0.15},
    {"name": "淘金热", "rarity": "silver", "desc": "每回合 +2 金币",
     "effect": "income", "value": 2},
    {"name": "巨龙之心", "rarity": "gold", "desc": "全体 +25% 最大生命",
     "effect": "hp_mult", "value": 0.25},
    {"name": "无尽之刃", "rarity": "gold", "desc": "全体 +25% 攻击力",
     "effect": "atk_mult", "value": 0.25},
    {"name": "大法师", "rarity": "gold", "desc": "全体 +35% 法术强度",
     "effect": "sp_mult", "value": 0.35},
    {"name": "刺客之心", "rarity": "gold", "desc": "全体 +30% 暴击率",
     "effect": "crit", "value": 0.30},
    {"name": "风之步", "rarity": "gold", "desc": "全体 +30% 攻速",
     "effect": "atk_speed", "value": 0.30},
    {"name": "财富", "rarity": "gold", "desc": "每回合 +5 金币",
     "effect": "income", "value": 5},
    {"name": "泰坦之怒", "rarity": "prismatic", "desc": "全体 +50% 最大生命",
     "effect": "hp_mult", "value": 0.50},
    {"name": "战神之力", "rarity": "prismatic", "desc": "全体 +50% 攻击力",
     "effect": "atk_mult", "value": 0.50},
    {"name": "法力洪流", "rarity": "prismatic", "desc": "全体 +70% 法术强度",
     "effect": "sp_mult", "value": 0.70},
    {"name": "毁灭者", "rarity": "prismatic", "desc": "全体 +60% 暴击率",
     "effect": "crit", "value": 0.60},
    {"name": "神速", "rarity": "prismatic", "desc": "全体 +60% 攻速",
     "effect": "atk_speed", "value": 0.60},
    {"name": "财富累积", "rarity": "prismatic", "desc": "每回合 +10 金币",
     "effect": "income", "value": 10},
]

CHAMP_AUGMENT_THEMES = {
    "BearBig": {"name": "熊大·守护", "desc": "全体 +200 生命 +20 护甲",
                "hp_mult": 0.15, "armor": 20},
    "BengBeng": {"name": "蹦蹦·迅捷", "desc": "全体射手 +20% 攻速",
                 "atk_speed": 0.20},
    "FeiBo": {"name": "肥波·气场", "desc": "全体 +20 法强 +10% 攻速",
              "sp_mult": 0.20, "atk_speed": 0.10},
    "BearTwo": {"name": "熊二·蛮力", "desc": "全体 +15% 攻击力 +10% 生命",
                "atk_mult": 0.15, "hp_mult": 0.10},
    "MaoMao": {"name": "毛毛·精准", "desc": "全体 +20% 暴击率",
               "crit": 0.20},
    "JiJi": {"name": "吉吉·灵气", "desc": "全体 +25% 法术强度",
             "sp_mult": 0.25},
    "TuTu": {"name": "涂涂·智慧", "desc": "全体 +15% 攻速 +10% 法强",
             "atk_speed": 0.15, "sp_mult": 0.10},
    "LaoE": {"name": "老鳄·狂暴", "desc": "全体 +20% 攻击力",
             "atk_mult": 0.20},
    "FeiFei": {"name": "肥肥·坚壁", "desc": "全体 +20% 生命 +15 护甲",
               "hp_mult": 0.20, "armor": 15},
    "GuangTouQiang": {"name": "光头强·伐木", "desc": "全体 +30% 攻击力",
                      "atk_mult": 0.30},
    "PotionPouch": {"name": "药剂袋·调合", "desc": "全体 +20% 法强",
                    "sp_mult": 0.20},
    "CubLeopard": {"name": "豹崽·敏捷", "desc": "全体 +15% 攻速 +10% 暴击",
                   "atk_speed": 0.15, "crit": 0.10},
    "MilkFrog": {"name": "奶蛙·治愈", "desc": "全体 +15% 生命 +15% 法强",
                 "hp_mult": 0.15, "sp_mult": 0.15},
    "LoggerStrong": {"name": "力伐木·蛮力", "desc": "全体 +15% 生命 +15% 攻击",
                     "hp_mult": 0.15, "atk_mult": 0.15},
    "LeopardPotion": {"name": "豹药剂·剧毒", "desc": "全体 +25% 暴击率 +15% 攻击",
                      "crit": 0.25, "atk_mult": 0.15},
    "SweatyElder": {"name": "汗长老·迷雾", "desc": "全体 +20% 法强 +10% 生命",
                    "sp_mult": 0.20, "hp_mult": 0.10},
    "NiuLai": {"name": "牛来·冲撞", "desc": "全体 +20% 攻击力 +10% 生命",
               "atk_mult": 0.20, "hp_mult": 0.10},
    "MJWalker": {"name": "迈克步·舞动", "desc": "全体 +25% 攻速",
                 "atk_speed": 0.25},
    "BaoLan": {"name": "豹兰·毁灭", "desc": "全体 +30% 攻击 +20% 暴击",
               "atk_mult": 0.30, "crit": 0.20},
    "SuperLogger": {"name": "超伐木·全力", "desc": "全体 +30% 生命 +30% 攻击",
                    "hp_mult": 0.30, "atk_mult": 0.30},
    "GodFrog": {"name": "神蛙·恩泽", "desc": "全体 +30% 生命",
                "hp_mult": 0.30},
    "PotionCreator": {"name": "药剂师·狂想", "desc": "全体 +40% 法强",
                      "sp_mult": 0.40},
    "RuneApprentice": {"name": "符文学徒·启程", "desc": "全体 +15% 法强",
                       "sp_mult": 0.15},
    "CrystalOracle": {"name": "水晶先知·预知", "desc": "全体 +20% 法强 +10% 攻速",
                      "sp_mult": 0.20, "atk_speed": 0.10},
    "RuneArcher": {"name": "符文射手·洞察", "desc": "全体 +20% 攻速 +10% 法强",
                   "atk_speed": 0.20, "sp_mult": 0.10},
    "StormKnight": {"name": "风暴骑士·雷鸣", "desc": "全体 +20% 攻击 +15% 攻速",
                    "atk_mult": 0.20, "atk_speed": 0.15},
    "ArcaneLord": {"name": "秘法领主·奥义", "desc": "全体 +50% 法强",
                   "sp_mult": 0.50},
    "XiaoDie": {"name": "小蝶·飞旋", "desc": "全体 +20% 攻速 +10% 暴击",
                "atk_speed": 0.20, "crit": 0.10},
    "LaoGui": {"name": "老龟·坚壁", "desc": "全体 +20% 生命 +20 护甲",
               "hp_mult": 0.20, "armor": 20},
}


# v1.2.9 宝物型强化：参考金铲铲的强化符文/战利品思路，允许在开局强化中获得
# 转职、灵符、神符、特殊道具、神器、光明装备等稀有资源。
TREASURE_AUGMENTS = [
    {"name": "纹章宝匣", "desc": "获得1个随机羁绊转职（不会获得财宝猎人转职）。", "reward": "emblem"},
    {"name": "灵符宝匣", "desc": "获得1个豹灵符或药灵符。", "reward": "talisman"},
    {"name": "神符宝匣", "desc": "获得1个随机神符。", "reward": "rune"},
    {"name": "神器宝匣", "desc": "获得1件随机豹药神器。", "reward": "artifact"},
    {"name": "光明锻造", "desc": "获得1件随机光明装备。", "reward": "radiant"},
    {"name": "宝物工坊", "desc": "获得1个随机特殊道具：昊天锤、拆卸器、大妮蔻、光明宝箱或杰作升级器。", "reward": "special"},
    {"name": "重铸工坊", "desc": "获得1把昊天锤，可重铸目标英雄全部装备。", "reward": "haotian_hammer"},
    {"name": "匠人之匣", "desc": "获得昊天锤与拆卸器，自由拆解、重铸你的装备。", "reward": "hammer_kit"},
    {"name": "远古宝库", "desc": "随机获得一件高阶宝物。", "reward": "rare_bundle"},
]

def _make_augment_reward_item(kind):
    if kind == "emblem":
        traits = ["PotionClan", "LeopardKind", "FrogTribe", "Lumber", "Dancer", "Elder", "Thunder"]
        return make_trait_emblem(random.choice(traits))
    if kind == "talisman":
        return make_rune_item(random.choice(["leopard", "potion"]))
    if kind == "rune":
        return make_rune_item(random.choice(["leopard_potion", "fat_leopard", "rotten_potion"]))
    if kind == "artifact":
        return make_artifact_item()
    if kind == "radiant":
        return random_radiant_item()
    if kind == "special":
        return make_special_item(random.choice(["haotian_hammer", "disassembler", "mega_neeko", "radiant_chest", "masterwork_upgrader"]))
    if kind == "haotian_hammer":
        return make_special_item("haotian_hammer")
    if kind == "rare_bundle":
        return random.choice([make_artifact_item(), random_radiant_item(),
                              make_special_item("masterwork_upgrader")])
    return None

def make_emblem_tome_pseudo():
    """纹章之书（备战席伪棋子）：is_pseudo_bench_only=True，不可上棋盘、不参战、不占用英雄池。"""
    return {
        "name": "EmblemTome", "cost": 0, "star": 1,
        "hp": 1, "ad": 0, "max_mana": 1, "mana_per_attack": 0,
        "attack_cooldown": 1.0, "sp_base_dmg": 0, "sp_multiplier": 0,
        "attack_range": 100, "skill_desc": "Tome", "skill_type": "damage",
        "traits": [], "role": "mage", "no_shop": True, "items": [],
        "is_pseudo_bench_only": True, "pseudo_kind": "emblem_tome",
    }

def grant_emblem_tome(player):
    """产出纹章之书：真人玩家→备战席伪棋子；AI→直接折现为随机纹章装备。"""
    if player.get("is_ai"):
        # AI 无法与伪棋子交互，直接获得随机纹章装备
        valid = [t for t in TRAIT_DATA if t not in ("BearRidge", "RuneLand")]
        item = make_trait_emblem(random.choice(valid))
        if len(player.get("items", [])) < MAX_ITEM_BENCH:
            player.setdefault("items", []).append(item)
        else:
            player.setdefault("free_item_store", []).append(item)
        return True
    empty = next((i for i, s in enumerate(player.get("bench", []))
                  if s is None), None)
    if empty is None:
        player["_tome_grant_log"] = "备战席已满，纹章之书获取失败"
        return False
    player["bench"][empty] = make_emblem_tome_pseudo()
    player["_tome_grant_log"] = f"纹章之书已放入备战席 {empty + 1}"
    return True

def _grant_augment_reward(player, reward_kind):
    if reward_kind == "tome":
        return grant_emblem_tome(player)
    if reward_kind == "hammer_kit":
        # 匠人之匣：一次发放昊天锤 + 拆卸器
        items = [make_special_item("haotian_hammer"),
                 make_special_item("disassembler")]
    else:
        item = _make_augment_reward_item(reward_kind)
        items = [item] if item is not None else []
    for it in items:
        if len(player.get("items", [])) < MAX_ITEM_BENCH:
            player.setdefault("items", []).append(it)
        else:
            player.setdefault("free_item_store", []).append(it)
    return bool(items)


def roll_global_augment():
    # 大多数对局仍保持原有英雄主题强化；少量概率进入宝物型强化。
    if random.random() < 0.28:
        reward = random.choice(TREASURE_AUGMENTS)
        return {"champ": None, "name": reward["name"], "desc": reward["desc"],
                "reward": reward["reward"], "is_treasure_augment": True,
                "hp_mult": 0.0, "atk_mult": 0.0, "sp_mult": 0.0,
                "crit": 0.0, "atk_speed": 0.0, "armor": 0}
    key = random.choice(list(CHAMP_AUGMENT_THEMES.keys()))
    theme = CHAMP_AUGMENT_THEMES[key]
    return {
        "champ": key, "name": theme["name"], "desc": theme["desc"],
        "hp_mult": theme.get("hp_mult", 0.0),
        "atk_mult": theme.get("atk_mult", 0.0),
        "sp_mult": theme.get("sp_mult", 0.0),
        "crit": theme.get("crit", 0.0),
        "atk_speed": theme.get("atk_speed", 0.0),
        "armor": theme.get("armor", 0),
    }


def apply_augment_to_player(player, aug):
    if "hex_bonuses" not in player:
        player["hex_bonuses"] = {"hp_mult": 0.0, "atk_mult": 0.0, "sp_mult": 0.0,
                                 "crit": 0.0, "atk_speed": 0.0, "income": 0,
                                 "armor": 0}
    hb = player["hex_bonuses"]
    hb["hp_mult"] = hb.get("hp_mult", 0.0) + aug.get("hp_mult", 0.0)
    hb["atk_mult"] = hb.get("atk_mult", 0.0) + aug.get("atk_mult", 0.0)
    hb["sp_mult"] = hb.get("sp_mult", 0.0) + aug.get("sp_mult", 0.0)
    hb["crit"] = hb.get("crit", 0.0) + aug.get("crit", 0.0)
    hb["atk_speed"] = hb.get("atk_speed", 0.0) + aug.get("atk_speed", 0.0)
    hb["armor"] = hb.get("armor", 0) + aug.get("armor", 0)
    if "hex_list" not in player:
        player["hex_list"] = []
    player["hex_list"].append({"name": aug["name"], "rarity": "prismatic",
                                "desc": aug["desc"]})
    if aug.get("is_treasure_augment"):
        _grant_augment_reward(player, aug.get("reward"))



LEOPARD_ARTIFACTS = {
    "龙神丹": {"desc": "友方HP低于50%时获得一次强力治疗并短暂免伤。", "color": (255, 190, 80)},
    "九天雷符": {"desc": "战斗开始眩晕全体敌人并施加易伤。", "color": (120, 180, 255)},
    "玄冰镜": {"desc": "受击时反弹部分伤害并获得短暂护盾。", "color": (140, 220, 255)},
    "火莲印": {"desc": "施放技能后在目标位置爆炸并持续灼烧。", "color": (255, 90, 60)},
    "疾风靴": {"desc": "战斗开始获得极高攻速与移速，首次攻击必定暴击。", "color": (120, 255, 160)},
    "辟邪玉": {"desc": "首次受到控制时免疫该控制并立即获得法力。", "color": (180, 220, 255)},
    "聚宝盆": {"desc": "击杀获得金币，胜利时有概率获得藏宝碎片。", "color": (255, 215, 80)},
    "噬魂幡": {"desc": "攻击低生命目标时造成额外真伤，击杀后回复生命。", "color": (190, 80, 120)},
    "玲珑塔": {"desc": "定期为最低生命友军提供护盾并清除负面效果。", "color": (210, 170, 255)},
    "豹骨甲": {"desc": "自身获得大量生命、护甲、魔抗，并为附近友军分摊伤害。", "color": (210, 170, 120)},
    "诛仙弓": {"desc": "增加攻击距离，对当前最高生命敌人造成额外伤害。", "color": (255, 140, 140)},
    "浑天仪": {"desc": "战斗开始使全体友军获得攻击、法强和攻速。", "color": (180, 130, 255)},
}
LEOPARD_ARTIFACT_NAMES = list(LEOPARD_ARTIFACTS)

SPECIAL_ITEM_DATA = {
    "emblem_treasure": ("财宝猎人纹章", "激活财宝猎人羁绊。"),
    "emblem_lumber": ("伐木纹章", "激活伐木羁绊。"),
    "disassembler": ("装备拆卸器", "无限次拆下目标英雄全部装备。"),
    "haotian_hammer": ("昊天锤", "一次性随机重铸目标英雄的全部装备。"),
    "masterwork_upgrader": ("杰作升级器", "将目标英雄的成装升级为光明版。"),
    "mega_neeko": ("大妮蔻", "复制目标英雄的1星版本。"),
    "radiant_chest": ("光明宝箱", "选择该英雄推荐成装的光明版，三选一。"),
    "emblem_tome": ("纹章之书", "随机生成4个纹章供选择。"),
    "orb": ("法球", "打开后随机获得一种野怪掉落奖励。"),
    "artifact_forge": ("豹药神器锻造器", "随机获得一件豹药神器。"),
    "giant_axe": ("巨斧选择器", "标记1名棋盘伐木弈子为伐木首领（仅备战阶段可用，可反复使用，不消耗）。"),
}

# 一次性消耗型特殊道具清单（不可穿戴到棋子身上，拖到棋子即执行或作为工具使用）。
# 与【可穿戴装备】相对：纹章(emblem_*)/神器(is_artifact)/普通装备/灵符属于可穿戴装备；
# 下列特殊道具只是消耗功能道具，AI 装配时会被过滤，装配函数也会拦截。
SPECIAL_ITEM_CONSUMABLE_KINDS = frozenset({
    "disassembler", "haotian_hammer", "masterwork_upgrader",
    "mega_neeko", "radiant_chest", "emblem_tome", "orb",
    "artifact_forge", "giant_axe",
})

def is_wearable_item(item):
    """判定道具是否为【可穿戴装备】（普通装备/成装/纹章/神器/灵符），
    而非【一次性消耗道具】（拆卸器/昊天锤/法球等）。

    优先读取创建时写入的 item_type 标记；对旧存档等未打标记的数据，
    回退到结构特征判断（is_special 且非纹章/神器 → 消耗道具）。
    """
    t = item.get("item_type")
    if t is not None:
        return t == "wearable"
    if item.get("is_special") and not item.get("is_emblem") and not item.get("is_artifact"):
        return False
    return True


RUNE_ITEM_DATA = {
    "leopard": {
        "id": "leopard_talisman", "name": "豹灵符",
        "desc": "合成材料；与药灵符或豹灵符合成转职神符",
    },
    "potion": {
        "id": "potion_talisman", "name": "药灵符",
        "desc": "合成材料；与豹灵符或药灵符合成转职神符",
    },
    "leopard_potion": {
        "id": "leopard_potion_rune", "name": "豹药神符",
        "desc": "豹灵符+药灵符；最大人口+1",
    },
    "fat_leopard": {
        "id": "fat_leopard_rune", "name": "肥豹神符",
        "desc": "豹灵符+豹灵符；最大人口+1",
    },
    "rotten_potion": {
        "id": "rotten_potion_rune", "name": "药烂神符",
        "desc": "药灵符+药灵符；最大人口+1",
    },
}


def make_rune_item(kind):
    data = RUNE_ITEM_DATA.get(kind, RUNE_ITEM_DATA["leopard"])
    # 只有合成出来的神符(leopard_potion/fat_leopard/rotten_potion)才加人口；
    # 基础灵符(leopard/potion)只是材料，不加人口。
    is_combined = kind not in ("leopard", "potion")
    return {
        "id": data["id"], "name": data["name"], "desc": data["desc"],
        "stats": {"population": 1} if is_combined else {},
        "color": (180, 90, 255),
        "is_combined": is_combined,
        "is_rune": True, "rune_kind": kind,
        "item_type": "wearable",
    }


def get_rune_items(unit):
    return [it for it in unit.get("items", [])
            if it.get("rune_kind") in RUNE_ITEM_DATA]


def has_three_rune_set(unit):
    kinds = {it.get("rune_kind") for it in get_rune_items(unit)}
    return {"leopard_potion", "fat_leopard", "rotten_potion"} <= kinds


def apply_rune_set_gold(player):
    total = 0
    for row in player.get("board", []):
        for unit in row:
            if unit is not None and has_three_rune_set(unit):
                total += 4
    return total


BOUNTY_SHARD_GAIN = {
    3: (2, 3), 4: (2, 4), 5: (3, 5),
    6: (4, 7), 7: (4, 7), 8: (4, 7),
}


def _bounty_gain(treasure_cnt, won):
    if treasure_cnt < 3:
        return 0
    use = max(k for k in BOUNTY_SHARD_GAIN if treasure_cnt >= k)
    w, l = BOUNTY_SHARD_GAIN[use]
    return w if won else l


def _bounty_item(item_id, name, desc="", stats=None):
    extra = dict(stats or {})
    special_kind = extra.pop("special_kind", None)
    return {
        "id": item_id, "name": name,
        "desc": desc, "stats": extra,
        "color": TREASURE_COLOR, "is_combined": False,
        "is_special": True,
        "special_kind": special_kind or (item_id if item_id in SPECIAL_ITEM_DATA else None),
    }


def _bounty_reward_options(layer):
    # Each layer is a pool of 3-5 complete reward bundles. One bundle is
    # randomly selected when the layer is reached.
    return {
        2: [
            {"name": "散件", "desc": "随机 1 件散件", "items": [("base", 1)]},
            {"name": "昊天锤", "desc": "一次性随机重铸装备", "items": [("special", "haotian_hammer", "昊天锤", "敲击装备后随机重铸")]},
            {"name": "金币", "desc": "+10 金币", "gold": 10},
        ],
        3: [
            {"name": "散件+5金+6金", "desc": "随机散件 +11 金币", "items": [("base", 1)], "gold": 11},
            {"name": "成装+7金+昊天锤", "desc": "随机成装 +7金币 +昊天锤",
             "items": [("combined", 1), ("special", "haotian_hammer", "昊天锤", "敲击装备后随机重铸")], "gold": 7},
            {"name": "2散件+4金", "desc": "2 件散件 +4金币", "items": [("base", 2)], "gold": 4},
            {"name": "随机豹药神器+昊天锤", "desc": "随机豹药神器 + 昊天锤",
             "items": [("artifact_random", 1), ("special", "haotian_hammer", "昊天锤", "敲击装备后随机重铸")]},
            {"name": "昊天锤×2", "desc": "2 把昊天锤，尽情重铸装备",
             "items": [("special", "haotian_hammer", "昊天锤", "敲击装备后随机重铸"),
                       ("special", "haotian_hammer", "昊天锤", "敲击装备后随机重铸")]},
        ],
        4: [
            {"name": "豹药神器+成装+6金", "desc": "随机豹药神器 + 成装 +6金币",
             "items": [("artifact_random", 1), ("combined", 1)], "gold": 6},
            {"name": "3成装", "desc": "3 件随机成装", "items": [("combined", 3)]},
            {"name": "纹章之书+4金+2散件", "desc": "纹章之书 +4金币 +2散件",
             "items": [("tome", 1), ("base", 2)], "gold": 4},
            {"name": "4×10金", "desc": "+40 金币", "gold": 40},
        ],
        5: [
            {"name": "8法球+豹药神符", "desc": "8 个法球 + 豹药神符",
             "items": [("orb", 8), ("rune", "leopard_potion") ]},
            {"name": "4金+装备+2纹章之书", "desc": "+4金币 +随机装备 +2纹章之书",
             "items": [("random_item", 1), ("tome", 2)], "gold": 4},
            {"name": "6散件+杰作升级器", "desc": "6散件 + 杰作升级器",
             "items": [("base", 6), ("special", "masterwork_upgrader", "杰作升级器", "将成装升级为光明版")]},
            {"name": "5金×4+54金", "desc": "+74金币", "gold": 74},
            {"name": "光明装备+豹药神器锻造器+3散件+昊天锤+拆卸器",
             "desc": "光明装备 + 豹药神器锻造器 +3散件 +昊天锤 +拆卸器",
             "items": [("radiant_random", 1), ("special", "artifact_forge", "豹药神器锻造器", "后续用于获得豹药神器"),
                       ("base", 3), ("special", "haotian_hammer", "昊天锤", "敲击装备后随机重铸"),
                       ("special", "disassembler", "装备拆卸器", "无限次拆卸装备")]},
        ],
        6: [
            {"name": "2散件+3成装+64金", "desc": "2散件 +3成装 +64金币",
             "items": [("base", 2), ("combined", 3)], "gold": 64},
            {"name": "财宝猎人纹章+豹药神符×2+8法球", "desc": "财宝猎人纹章 +2豹药神符 +8法球",
             "items": [("special", "emblem_treasure", "财宝猎人纹章", "激活财宝猎人羁绊"),
                       ("rune", "leopard_potion"), ("rune", "leopard_potion"), ("orb", 8)]},
            {"name": "7金+7金+100金+7金+7金", "desc": "+128金币", "gold": 128},
            {"name": "光明宝箱+大妮蔻+30金×2+20金", "desc": "光明宝箱 + 大妮蔻 +80金币",
             "items": [("special", "radiant_chest", "光明宝箱", "开出推荐成装的光明版，3选1"),
                       ("special", "mega_neeko", "大妮蔻", "复制1个1星英雄")], "gold": 80},
        ],
        7: [
            {"name": "光明宝箱+伐木纹章+2星伐木5费卡+3星其余伐木弈子",
             "desc": "光明宝箱 + 伐木纹章 + 2星伐木5费卡 + 3星其余伐木弈子",
             "items": [("special", "radiant_chest", "光明宝箱", "开出推荐成装的光明版，3选1"),
                       ("special", "emblem_lumber", "伐木纹章", "激活伐木羁绊"),
                       ("champion_bundle", 1)]},
            {"name": "财宝猎人纹章+50金×2+6散件", "desc": "财宝猎人纹章 +100金币 +6散件",
             "items": [("special", "emblem_treasure", "财宝猎人纹章", "激活财宝猎人羁绊"),
                       ("base", 6)], "gold": 100},
            {"name": "30金+40金+30金+30金+40金", "desc": "+170金币", "gold": 170},
            {"name": "光明宝箱×2+豹药神符×2+40金", "desc": "2光明宝箱 +2豹药神符 +40金币",
             "items": [("special", "radiant_chest", "光明宝箱", "开出推荐成装的光明版，3选1"),
                       ("special", "radiant_chest", "光明宝箱", "开出推荐成装的光明版，3选1"),
                       ("rune", "leopard_potion"), ("rune", "leopard_potion")], "gold": 40},
        ],
        8: [
            {"name": "大妮蔻×2+100金×2", "desc": "2大妮蔻 +200金币",
             "items": [("special", "mega_neeko", "大妮蔻", "复制1个1星英雄"),
                       ("special", "mega_neeko", "大妮蔻", "复制1个1星英雄")], "gold": 200},
            {"name": "豹药神符×3+66生命值", "desc": "3豹药神符 +66生命值",
             "items": [("rune", "leopard_potion"), ("rune", "leopard_potion"),
                       ("rune", "leopard_potion")], "hp": 66},
            {"name": "光明宝箱×2+大妮蔻×2+126金", "desc": "2光明宝箱 +2大妮蔻 +126金币",
             "items": [("special", "radiant_chest", "光明宝箱", "开出推荐成装的光明版，3选1"),
                       ("special", "radiant_chest", "光明宝箱", "开出推荐成装的光明版，3选1"),
                       ("special", "mega_neeko", "大妮蔻", "复制1个1星英雄"),
                       ("special", "mega_neeko", "大妮蔻", "复制1个1星英雄")], "gold": 126},
        ],
        9: [
            {"name": "掠夺·商店", "desc": "刷新与购买不再消耗金币；5费卡永久9张",
             "type": "plunder", "plunder": "shop"},
            {"name": "掠夺·羁绊", "desc": "所有上阵弈子直接激活所属羁绊最高等级",
             "type": "plunder", "plunder": "trait"},
            {"name": "掠夺·技能", "desc": "敌方单位无法释放技能",
             "type": "plunder", "plunder": "skill"},
        ],
    }.get(layer, [])


def roll_bounty_reward(layer):
    options = _bounty_reward_options(layer)
    if not options:
        options = _bounty_reward_options(2)
    return copy.deepcopy(random.choice(options))


def _add_bounty_item(gs, item):
    if len(gs.me["items"]) < MAX_ITEM_BENCH:
        gs.me["items"].append(item)
        return True
    gs.me.setdefault("free_item_store", []).append(item)
    return False


def _make_random_combined_item():
    r = random.choice(list(COMBINE_TABLE.values()))
    return {"id": "bounty_comb_" + re.sub(r"\\W+", "_", r["name"]),
            "name": r["name"], "stats": dict(r["stats"]),
            "color": r["color"], "is_combined": True}



def make_special_item(kind):
    name, desc = SPECIAL_ITEM_DATA.get(kind, (kind, "特殊装备"))
    item = {
        "id": kind,
        "name": name,
        "desc": desc,
        "stats": {},
        "color": (255, 210, 90),
        "is_special": True,
        "is_combined": True,
        "special_kind": kind,
        "item_type": "consumable" if kind in SPECIAL_ITEM_CONSUMABLE_KINDS else "wearable",
    }
    if kind in ("emblem_treasure", "emblem_lumber"):
        item["is_emblem"] = True
        item["emblem_trait"] = "Treasure" if kind == "emblem_treasure" else "Lumber"
    return item


def make_trait_emblem(trait):
    """通用纹章：装备后把对应羁绊加入棋子，允许同类纹章叠加。"""
    return {
        "id": "emblem_" + str(trait),
        "name": trait_cn(trait) + "纹章",
        "desc": "装备后激活该羁绊。",
        "stats": {},
        "color": TRAIT_COLOR.get(trait, (220, 180, 80)),
        "is_special": True,
        "is_combined": True,
        "special_kind": "emblem_generic",
        "is_emblem": True,
        "emblem_trait": trait,
        "item_type": "wearable",
    }

def make_artifact_item(name=None):
    name = name or random.choice(LEOPARD_ARTIFACT_NAMES)
    d = LEOPARD_ARTIFACTS[name]
    return {
        "id": "artifact_" + re.sub(r"\W+", "_", name),
        "name": name,
        "desc": d["desc"],
        "stats": {},
        "color": d["color"],
        "is_special": True,
        "is_artifact": True,
        "artifact_name": name,
        "is_combined": True,
        "item_type": "wearable",
    }

def _reroll_item(item):
    if item.get("is_emblem") or item.get("special_kind") in ("emblem_treasure", "emblem_lumber"):
        # 昊天锤敲纹章时，可将其他纹章敲成财宝猎人纹章。
        return make_special_item("emblem_treasure")
    if item.get("rune_kind") == "leopard":
        return make_rune_item("potion")
    if item.get("rune_kind") == "potion":
        return make_rune_item("leopard")
    if item.get("rune_kind") in ("leopard_potion", "fat_leopard", "rotten_potion"):
        return make_rune_item(random.choice(["leopard_potion", "fat_leopard", "rotten_potion"]))
    if item.get("is_radiant"):
        r = random_radiant_item()
        return r or item
    if item.get("is_combined"):
        candidates=[make_item for make_item in (
            (lambda: _make_random_combined_item()), (lambda: random_radiant_item())
        )]
        return random.choice(candidates)() or item
    return new_item(random.choice(ITEM_IDS))


def _plunder_active(player, kind):
    return player.get("_active_plunder") == kind


def _add_bounty_unit(gs, unit):
    empty = next((i for i, x in enumerate(gs.me.get("bench", [])) if x is None), None)
    if empty is not None:
        gs.me["bench"][empty] = unit
        return True
    # 备战席满时不丢失奖励：按该棋子星级折算金币。
    gs.me["gold"] += unit.get("cost", 1) * (3 ** max(0, unit.get("star", 1) - 1))
    return False


def apply_bounty_reward(gs, reward):
    player = gs.me
    if reward.get("type") == "plunder":
        plunder = reward.get("plunder")
        gs._pending_plunder = plunder
        gs._active_plunder = plunder
        player["_active_plunder"] = plunder
        if plunder == "trait":
            player["_plunder_trait"] = True
        gs.battle_log = "终极掠夺已激活：" + reward.get("name", "")
        return

    player["gold"] += int(reward.get("gold", 0))
    player["hp"] += int(reward.get("hp", 0))
    for kind in reward.get("items", []):
        if not kind:
            continue
        typ = kind[0]
        if typ == "base":
            for _ in range(int(kind[1])):
                _add_bounty_item(gs, new_item(random.choice(ITEM_IDS)))
        elif typ == "combined":
            for _ in range(int(kind[1])):
                _add_bounty_item(gs, _make_random_combined_item())
        elif typ == "random_item":
            _add_bounty_item(gs, new_item(random.choice(ITEM_IDS)))
        elif typ == "artifact_random":
            _add_bounty_item(gs, make_artifact_item())
        elif typ == "radiant_random":
            rad = random_radiant_item()
            if rad:
                _add_bounty_item(gs, rad)
        elif typ == "orb":
            for _ in range(int(kind[1])):
                _add_bounty_item(gs, _bounty_item(
                    "orb_" + str(random.randint(1, 999999)), "法球",
                    "野怪随机掉落物", {"special_kind": "orb"}))
        elif typ == "tome":
            if grant_emblem_tome(gs.me):
                gs.battle_log = gs.me.get("_tome_grant_log",
                                          "纹章之书已放入备战席")
            else:
                gs.battle_log = gs.me.get("_tome_grant_log",
                                          "备战席已满，纹章之书获取失败")
        elif typ == "rune":
            _add_bounty_item(gs, make_rune_item(kind[1]))
        elif typ == "special":
            sk = kind[1]
            if sk == "artifact_forge":
                _add_bounty_item(gs, make_artifact_item())
            else:
                _add_bounty_item(gs, make_special_item(sk))
        elif typ == "champion_bundle":
            five = [c for c in CHAMPION_LIST if c.get("cost") == 5 and "Lumber" in c.get("traits", []) and not c.get("no_shop")]
            other = [c for c in CHAMPION_LIST if "Lumber" in c.get("traits", []) and c.get("cost") != 5 and not c.get("no_shop")]
            if five:
                _add_bounty_unit(gs, make_unit_with_star(random.choice(five)["name"], 2))
            for c in other:
                u = make_unit_with_star(c["name"], 3)
                if u:
                    _add_bounty_unit(gs, u)
    if reward.get("name") == "财宝猎人纹章+伐木纹章":
        pass
    if len(player["items"]) > MAX_ITEM_BENCH:
        overflow = player["items"][MAX_ITEM_BENCH:]
        player["items"] = player["items"][:MAX_ITEM_BENCH]
        player.setdefault("free_item_store", []).extend(overflow)


HEX_TREASURE_REWARDS = [
    {"name": "宝物库：转职", "rarity": "gold", "desc": "获得1个随机羁绊转职。", "effect": "treasure_reward", "value": "emblem"},
    {"name": "宝物库：灵符", "rarity": "gold", "desc": "获得1个豹灵符或药灵符。", "effect": "treasure_reward", "value": "talisman"},
    {"name": "宝物库：神符", "rarity": "gold", "desc": "获得1个随机神符。", "effect": "treasure_reward", "value": "rune"},
    {"name": "宝物库：神器", "rarity": "prismatic", "desc": "获得1件随机豹药神器。", "effect": "treasure_reward", "value": "artifact"},
    {"name": "宝物库：光明装备", "rarity": "prismatic", "desc": "获得1件随机光明装备。", "effect": "treasure_reward", "value": "radiant"},
    {"name": "宝物库：特殊道具", "rarity": "gold", "desc": "获得1个特殊道具。", "effect": "treasure_reward", "value": "special"},
]
HEX_LIST.extend(HEX_TREASURE_REWARDS)

def roll_hex_choices():

    r = random.randint(1, 100)
    if r <= 60:
        rarity = "silver"
    elif r <= 90:
        rarity = "gold"
    else:
        rarity = "prismatic"
    pool = [h for h in HEX_LIST if h["rarity"] == rarity]
    if len(pool) < 3:
        pool = list(HEX_LIST)
    picked = random.sample(pool, 3)
    return [copy.deepcopy(h) for h in picked]


def apply_hex_to_player(player, hex_data):
    if "hex_bonuses" not in player:
        player["hex_bonuses"] = {"hp_mult": 0.0, "atk_mult": 0.0, "sp_mult": 0.0,
                                 "crit": 0.0, "atk_speed": 0.0, "income": 0,
                                 "armor": 0}
    hb = player["hex_bonuses"]
    eff = hex_data["effect"]
    val = hex_data["value"]
    if eff in ("hp_mult", "atk_mult", "sp_mult", "crit", "atk_speed"):
        hb[eff] = hb.get(eff, 0.0) + val
    elif eff == "income":
        hb["income"] = hb.get("income", 0) + int(val)
    elif eff == "treasure_reward":
        _grant_augment_reward(player, val)
    if "hex_list" not in player:
        player["hex_list"] = []
    player["hex_list"].append(copy.deepcopy(hex_data))


def get_hex_bonuses(player):
    hb = player.get("hex_bonuses", {})
    return {
        "hp_mult": 1.0 + hb.get("hp_mult", 0.0),
        "atk_mult": 1.0 + hb.get("atk_mult", 0.0),
        "sp_mult": 1.0 + hb.get("sp_mult", 0.0),
        "crit": hb.get("crit", 0.0),
        "atk_speed": 1.0 + hb.get("atk_speed", 0.0),
        "income": int(hb.get("income", 0)),
        "armor": int(hb.get("armor", 0)),
    }


RECOMMEND_ITEMS = {
    "BearBig": ["狂徒铠甲", "荆棘之甲", "龙牙"],
    "BearTwo": ["无尽之刃", "饮血剑", "泰坦的坚决"],
    "FeiBo": ["卢登的回声", "大天使之杖", "珠光护手"],
    "MaoMao": ["疾射火炮", "无尽之刃", "最后的轻语"],
    "JiJi": ["卢登的回声", "大天使之杖", "莫雷洛秘典"],
    "TuTu": ["疾射火炮", "无尽之刃", "最后的轻语"],
    "LaoE": ["无尽之刃", "饮血剑", "挑战护手"],
    "FeiFei": ["狂徒铠甲", "荆棘之甲", "石像鬼石板"],
    "GuangTouQiang": ["无尽之刃", "饮血剑", "泰坦的坚决"],
    "BengBeng": ["疾射火炮", "无尽之刃", "挑战护手"],
    "PotionPouch": ["卢登的回声", "大天使之杖", "珠光护手"],
    "CubLeopard": ["无尽之刃", "饮血剑", "正义之手"],
    "MilkFrog": ["大天使之杖", "珠光护手", "莫雷洛秘典"],
    "LoggerStrong": ["无尽之刃", "饮血剑", "泰坦的坚决"],
    "LeopardPotion": ["无尽之刃", "珠光护手", "正义之手"],
    "SweatyElder": ["卢登的回声", "大天使之杖", "莫雷洛秘典"],
    "NiuLai": ["无尽之刃", "泰坦的坚决", "饮血剑"],
    "MJWalker": ["疾射火炮", "无尽之刃", "最后的轻语"],
    "BaoLan": ["无尽之刃", "饮血剑", "泰坦的坚决"],
    "SuperLogger": ["无尽之刃", "饮血剑", "斯特拉克"],
    "GodFrog": ["大天使之杖", "珠光护手", "莫雷洛秘典"],
    "PotionCreator": ["卢登的回声", "大天使之杖", "珠光护手"],
    "RuneApprentice": ["大天使之杖", "珠光护手", "卢登的回声"],
    "CrystalOracle": ["大天使之杖", "珠光护手", "莫雷洛秘典"],
    "RuneArcher": ["疾射火炮", "无尽之刃", "最后的轻语"],
    "StormKnight": ["无尽之刃", "泰坦的坚决", "饮血剑"],
    "ArcaneLord": ["卢登的回声", "大天使之杖", "珠光护手"],
    "Tuanzi": ["狂徒铠甲", "荆棘之甲", "龙牙"],
    "XiaoDie": ["疾射火炮", "无尽之刃", "最后的轻语"],
    "LaoGui": ["狂徒铠甲", "荆棘之甲", "龙牙"],
}


def get_recommend_items(name):
    return RECOMMEND_ITEMS.get(name, ["无尽之刃", "狂徒铠甲", "大天使之杖"])


CHAMPION_LIST = [
    {"name": "BearBig", "cost": 1, "traits": ["BearRidge"], "role": "tank",
     "hp": 750, "ad": 45, "max_mana": 40, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 150, "sp_multiplier": 1.3,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Forest Guard",
     "skill_type": "shield"},
    {"name": "BengBeng", "cost": 1, "traits": ["BearRidge", "Treasure"],
     "role": "archer",
     "hp": 480, "ad": 55, "max_mana": 30, "mana_per_attack": 13,
     "attack_cooldown": 1.1, "sp_base_dmg": 110, "sp_multiplier": 1.4,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Flying Jump",
     "skill_type": "damage"},
    {"name": "FeiBo", "cost": 2, "traits": ["BearRidge"],
     "role": "mage",
     "hp": 550, "ad": 38, "max_mana": 36, "mana_per_attack": 10,
     "attack_cooldown": 1.35, "sp_base_dmg": 130, "sp_multiplier": 1.6,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Fat Wave",
     "skill_type": "damage"},
    {"name": "BearTwo", "cost": 2, "traits": ["BearRidge"], "role": "warrior",
     "hp": 820, "ad": 58, "max_mana": 42, "mana_per_attack": 11,
     "attack_cooldown": 1.3, "sp_base_dmg": 140, "sp_multiplier": 1.5,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Bear Paw",
     "skill_type": "damage"},
    {"name": "MaoMao", "cost": 2, "traits": ["BearRidge"],
     "role": "archer",
     "hp": 500, "ad": 62, "max_mana": 32, "mana_per_attack": 12,
     "attack_cooldown": 1.1, "sp_base_dmg": 120, "sp_multiplier": 1.5,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Banana Barrage",
     "skill_type": "damage"},
    {"name": "JiJi", "cost": 3, "traits": ["BearRidge"],
     "role": "mage",
     "hp": 660, "ad": 45, "max_mana": 44, "mana_per_attack": 10,
     "attack_cooldown": 1.3, "sp_base_dmg": 180, "sp_multiplier": 1.7,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Monkey King",
     "skill_type": "damage"},
    {"name": "TuTu", "cost": 3, "traits": ["BearRidge"], "role": "archer",
     "hp": 580, "ad": 72, "max_mana": 40, "mana_per_attack": 12,
     "attack_cooldown": 1.15, "sp_base_dmg": 170, "sp_multiplier": 1.7,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Owl Wisdom",
"skill_type": "damage", "skill_dmg_type": "magic"},
    {"name": "LaoE", "cost": 4, "traits": ["BearRidge", "Treasure"],
     "role": "warrior",
     "hp": 1080, "ad": 78, "max_mana": 48, "mana_per_attack": 11,
     "attack_cooldown": 1.25, "sp_base_dmg": 215, "sp_multiplier": 1.9,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Croc Bite",
     "skill_type": "damage"},
    {"name": "FeiFei", "cost": 4, "traits": ["BearRidge"], "role": "tank",
     "hp": 1250, "ad": 62, "max_mana": 52, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 300, "sp_multiplier": 1.8,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Bear Charge",
     "skill_type": "shield"},
    {"name": "GuangTouQiang", "cost": 5, "traits": ["BearRidge"],
     "role": "warrior",
     "hp": 1400, "ad": 95, "max_mana": 58, "mana_per_attack": 11,
     "attack_cooldown": 1.2, "sp_base_dmg": 300, "sp_multiplier": 2.2,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Lumberjack Rage",
     "skill_type": "damage"},
    {"name": "PotionPouch", "cost": 1, "traits": ["PotionClan"], "role": "mage",
     "hp": 520, "ad": 42, "max_mana": 30, "mana_per_attack": 12,
     "attack_cooldown": 1.2, "sp_base_dmg": 105, "sp_multiplier": 1.3,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Potion Spray",
     "skill_type": "damage", "skill_dmg_type": "magic"},

    {"name": "CubLeopard", "cost": 1, "traits": ["LeopardKind"], "role": "warrior",
     "hp": 480, "ad": 48, "max_mana": 28, "mana_per_attack": 13,
     "attack_cooldown": 1.1, "sp_base_dmg": 95, "sp_multiplier": 1.4,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Pounce",
     "skill_type": "damage"},
    {"name": "MilkFrog", "cost": 2, "traits": ["FrogTribe", "RuneLand"],
     "role": "mage",
     "hp": 550, "ad": 32, "max_mana": 36, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 115, "sp_multiplier": 1.2,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Frog Resonance",
     "skill_type": "damage"},
    {"name": "LoggerStrong", "cost": 2, "traits": ["Lumber", "Treasure"],
     "role": "warrior",
     "hp": 620, "ad": 50, "max_mana": 38, "mana_per_attack": 11,
     "attack_cooldown": 1.25, "sp_base_dmg": 135, "sp_multiplier": 1.5,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Axe Sweep",
     "skill_type": "damage"},
    {"name": "XiaoDie", "cost": 2, "traits": ["Dancer", "Treasure"],
     "role": "archer",
     "hp": 520, "ad": 58, "max_mana": 34, "mana_per_attack": 12,
     "attack_cooldown": 1.1, "sp_base_dmg": 130, "sp_multiplier": 1.5,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Butterfly Dance",
     "skill_type": "damage"},
    {"name": "LeopardPotion", "cost": 3,
     "traits": ["PotionClan", "LeopardKind"],
     "role": "warrior",
     "hp": 720, "ad": 60, "max_mana": 42, "mana_per_attack": 12,
     "attack_cooldown": 1.2, "sp_base_dmg": 165, "sp_multiplier": 1.7,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Poison Assault",
"skill_type": "damage", "skill_dmg_type": "magic"},
    {"name": "SweatyElder", "cost": 3, "traits": ["Elder"],
     "role": "mage",
     "hp": 850, "ad": 44, "max_mana": 45, "mana_per_attack": 9,
     "attack_cooldown": 1.5, "sp_base_dmg": 125, "sp_multiplier": 1.6,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Mist Aura",
     "skill_type": "damage"},
    {"name": "LaoGui", "cost": 3, "traits": ["Elder", "RuneLand"],
     "role": "tank",
     "hp": 950, "ad": 50, "max_mana": 45, "mana_per_attack": 10,
     "attack_cooldown": 1.5, "sp_base_dmg": 220, "sp_multiplier": 1.7,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Ancient Shell",
     "skill_type": "shield"},
    {"name": "NiuLai", "cost": 4, "traits": ["Lumber", "LeopardKind"],
     "role": "warrior",
     "hp": 1100, "ad": 72, "max_mana": 52, "mana_per_attack": 10,
     "attack_cooldown": 1.3, "sp_base_dmg": 215, "sp_multiplier": 1.9,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Bull Rush",
     "skill_type": "damage"},
    {"name": "MJWalker", "cost": 4, "traits": ["Dancer", "RuneLand"],
     "role": "archer",
     "hp": 680, "ad": 65, "max_mana": 48, "mana_per_attack": 13,
     "attack_cooldown": 1.05, "sp_base_dmg": 200, "sp_multiplier": 1.8,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Moonwalk",
     "skill_type": "damage"},
    {"name": "BaoLan", "cost": 5, "traits": ["PotionClan", "LeopardKind"],
     "role": "warrior",
     "hp": 1400, "ad": 90, "max_mana": 60, "mana_per_attack": 11,
     "attack_cooldown": 1.2, "sp_base_dmg": 290, "sp_multiplier": 2.2,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Doom Leopard",
     "skill_type": "damage", "skill_dmg_type": "magic"},
    {"name": "SuperLogger", "cost": 5, "traits": ["Lumber"],
     "role": "warrior",
     "hp": 1300, "ad": 95, "max_mana": 58, "mana_per_attack": 10,
     "attack_cooldown": 1.25, "sp_base_dmg": 270, "sp_multiplier": 2.1,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Super Power Pill",
     "skill_type": "damage"},
    {"name": "GodFrog", "cost": 5, "traits": ["FrogTribe", "RuneLand"],
     "role": "mage",
     "hp": 1250, "ad": 55, "max_mana": 55, "mana_per_attack": 8,
     "attack_cooldown": 1.4, "sp_base_dmg": 280, "sp_multiplier": 2.5,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Global Heal",
     "skill_type": "heal"},
    {"name": "PotionCreator", "cost": 5, "traits": ["PotionClan", "RuneLand"],
     "role": "mage",
     "hp": 1350, "ad": 82, "max_mana": 62, "mana_per_attack": 9,
     "attack_cooldown": 1.3, "sp_base_dmg": 310, "sp_multiplier": 2.3,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Potion Nuke",
     "skill_type": "damage", "skill_dmg_type": "magic"},

    {"name": "RuneApprentice", "cost": 1, "traits": ["RuneLand"], "role": "mage",
     "hp": 470, "ad": 38, "max_mana": 30, "mana_per_attack": 12,
     "attack_cooldown": 1.2, "sp_base_dmg": 105, "sp_multiplier": 1.4,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Arcane Bolt",
     "skill_type": "damage", "skill_dmg_type": "magic"},

    {"name": "CrystalOracle", "cost": 2, "traits": ["RuneLand"], "role": "mage",
     "hp": 540, "ad": 36, "max_mana": 36, "mana_per_attack": 11,
     "attack_cooldown": 1.35, "sp_base_dmg": 125, "sp_multiplier": 1.5,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Crystal Veil",
     "skill_type": "damage", "skill_dmg_type": "magic"},

    {"name": "RuneArcher", "cost": 3, "traits": ["RuneLand"],
     "role": "archer",
     "hp": 640, "ad": 62, "max_mana": 40, "mana_per_attack": 12,
     "attack_cooldown": 1.15, "sp_base_dmg": 165, "sp_multiplier": 1.7,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Mana Shot",
"skill_type": "damage", "skill_dmg_type": "magic"},
    {"name": "StormKnight", "cost": 4, "traits": ["RuneLand"], "role": "warrior",
     "hp": 1000, "ad": 78, "max_mana": 48, "mana_per_attack": 11,
     "attack_cooldown": 1.2, "sp_base_dmg": 210, "sp_multiplier": 1.9,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Thunder Strike",
"skill_type": "damage", "skill_dmg_type": "magic"},
    {"name": "ArcaneLord", "cost": 5, "traits": ["RuneLand"],
     "role": "mage",
     "hp": 1380, "ad": 85, "max_mana": 60, "mana_per_attack": 10,
     "attack_cooldown": 1.25, "sp_base_dmg": 320, "sp_multiplier": 2.3,
     "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Arcane Nova",
     "skill_type": "damage", "skill_dmg_type": "magic"},

    {"name": "Tuanzi", "cost": 5, "traits": ["Summon"], "role": "tank",
     "hp": 700, "ad": 65, "max_mana": 50, "mana_per_attack": 12,
     "attack_cooldown": 1.2, "sp_base_dmg": 200, "sp_multiplier": 2.0,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Ice Seal",
     "skill_type": "shield", "no_shop": True},
    {"name": "AncientTree", "cost": 0, "traits": ["Summon"], "role": "tank",
     "hp": 1800, "ad": 80, "max_mana": 60, "mana_per_attack": 8,
     "attack_cooldown": 1.5, "sp_base_dmg": 350, "sp_multiplier": 2.2,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Tree Smash",
     "skill_type": "damage", "no_shop": True},
    {"name": "ThunderHelper", "cost": 1, "traits": ["Thunder"], "role": "mage",
 "hp": 500, "ad": 35, "max_mana": 20, "mana_per_attack": 15,
 "attack_cooldown": 1.3, "sp_base_dmg": 95, "sp_multiplier": 1.3,
  "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Thunder Brain",
 "skill_type": "damage", "skill_dmg_type": "magic"},

{"name": "ThunderLicker", "cost": 2, "traits": ["Thunder"], "role": "warrior",
 "hp": 680, "ad": 55, "max_mana": 30, "mana_per_attack": 10,
 "attack_cooldown": 1.2, "sp_base_dmg": 130, "sp_multiplier": 1.5,
 "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Lick",
 "skill_type": "damage", "skill_dmg_type": "magic"},
{"name": "ThunderComment", "cost": 3, "traits": ["Thunder"], "role": "mage",
 "hp": 720, "ad": 42, "max_mana": 40, "mana_per_attack": 10,
 "attack_cooldown": 1.4, "sp_base_dmg": 150, "sp_multiplier": 1.65,
  "attack_range": RANGE_MAGE, "star": 1, "skill_desc": "Comment",
 "skill_type": "damage", "skill_dmg_type": "magic"},

{"name": "ThunderPotato", "cost": 3, "traits": ["Thunder"], "role": "tank",
 "hp": 950, "ad": 48, "max_mana": 30, "mana_per_attack": 10,
 "attack_cooldown": 1.5, "sp_base_dmg": 180, "sp_multiplier": 1.6,
 "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Potato",
 "skill_type": "shield"},
{"name": "ThunderGoddess", "cost": 4, "traits": ["Thunder"], "role": "archer",
 "hp": 720, "ad": 72, "max_mana": 30, "mana_per_attack": 12,
 "attack_cooldown": 1.1, "sp_base_dmg": 220, "sp_multiplier": 1.9,
 "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Goddess",
 "skill_type": "damage", "skill_dmg_type": "magic"},
{"name": "ThunderPatch", "cost": 5, "traits": ["Thunder"], "role": "warrior",
 "hp": 1350, "ad": 90, "max_mana": 25, "mana_per_attack": 12,
 "attack_cooldown": 1.2, "sp_base_dmg": 280, "sp_multiplier": 2.1,
 "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Patch",
 "skill_type": "damage", "skill_dmg_type": "magic"},

    {"name": "PotionLeopard", "cost": 1, "traits": ["PotionClan", "LeopardKind"], "role": "tank",
     "hp": 800, "ad": 42, "max_mana": 40, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 150, "sp_multiplier": 1.3,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Potion Barrier",
     "skill_type": "bulwark"},
    {"name": "OxKui", "cost": 1, "traits": ["Lumber"], "role": "tank",
     "hp": 850, "ad": 45, "max_mana": 42, "mana_per_attack": 10,
     "attack_cooldown": 1.5, "sp_base_dmg": 155, "sp_multiplier": 1.3,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Ox Charge",
     "skill_type": "bulwark"},
    {"name": "FrogBulwark", "cost": 2, "traits": ["FrogTribe"], "role": "tank",
     "hp": 900, "ad": 45, "max_mana": 44, "mana_per_attack": 10,
     "attack_cooldown": 1.45, "sp_base_dmg": 175, "sp_multiplier": 1.5,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Gel Shield",
     "skill_type": "drain"},
    {"name": "BearFortress", "cost": 3, "traits": ["BearRidge"], "role": "tank",
     "hp": 1080, "ad": 55, "max_mana": 48, "mana_per_attack": 10,
     "attack_cooldown": 1.45, "sp_base_dmg": 220, "sp_multiplier": 1.7,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Roar Guard",
     "skill_type": "shield"},
    {"name": "PotionKeep", "cost": 3, "traits": ["PotionClan"], "role": "tank",
     "hp": 1050, "ad": 48, "max_mana": 46, "mana_per_attack": 10,
     "attack_cooldown": 1.5, "sp_base_dmg": 230, "sp_multiplier": 1.7,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Vial Fortress",
     "skill_type": "shield", "skill_dmg_type": "magic"},
    {"name": "ThornGuard", "cost": 4, "traits": ["LeopardKind"], "role": "tank",
     "hp": 1220, "ad": 58, "max_mana": 50, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 280, "sp_multiplier": 1.8,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Thorn Burst",
     "skill_type": "burst_shield"},
    {"name": "OxBastion", "cost": 4, "traits": ["Lumber"], "role": "tank",
     "hp": 1280, "ad": 58, "max_mana": 52, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 285, "sp_multiplier": 1.85,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Ox Aegis",
     "skill_type": "drain", "skill_dmg_type": "magic"},
    {"name": "AncientVial", "cost": 5, "traits": ["PotionClan", "RuneLand"], "role": "tank",
     "hp": 1500, "ad": 70, "max_mana": 60, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 350, "sp_multiplier": 2.1,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Ancestral Boil",
     "skill_type": "burst_shield", "skill_dmg_type": "magic"},
    {"name": "LeopardBow", "cost": 1, "traits": ["LeopardKind"], "role": "archer",
     "hp": 490, "ad": 55, "max_mana": 30, "mana_per_attack": 13,
     "attack_cooldown": 1.1, "sp_base_dmg": 110, "sp_multiplier": 1.4,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Venom Bolt",
     "skill_type": "damage"},
    {"name": "FrogBomb", "cost": 2, "traits": ["FrogTribe"], "role": "archer",
     "hp": 540, "ad": 52, "max_mana": 34, "mana_per_attack": 12,
     "attack_cooldown": 1.15, "sp_base_dmg": 135, "sp_multiplier": 1.55,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Toxic Bomb",
     "skill_type": "damage", "skill_dmg_type": "magic"},
    {"name": "OxGunner", "cost": 3, "traits": ["Lumber", "Treasure"], "role": "archer",
     "hp": 640, "ad": 78, "max_mana": 42, "mana_per_attack": 12,
     "attack_cooldown": 1.2, "sp_base_dmg": 185, "sp_multiplier": 1.7,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Heavy Shot",
     "skill_type": "damage"},
    {"name": "VialSniper", "cost": 4, "traits": ["PotionClan"], "role": "archer",
     "hp": 680, "ad": 62, "max_mana": 48, "mana_per_attack": 13,
     "attack_cooldown": 1.05, "sp_base_dmg": 210, "sp_multiplier": 1.8,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Needle Storm",
     "skill_type": "damage"},
    {"name": "SwiftStrike", "cost": 5, "traits": ["LeopardKind"], "role": "archer",
     "hp": 720, "ad": 88, "max_mana": 55, "mana_per_attack": 13,
     "attack_cooldown": 1.0, "sp_base_dmg": 290, "sp_multiplier": 2.1,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Swift Barrage",
     "skill_type": "damage"},
]
TRAIT_DATA = {
    "PotionClan": [2, 4, 6, 8, 10], "LeopardKind": [2, 4, 6, 8, 10],
    "FrogTribe": [2, 4, 6],
    "Lumber": [3, 5, 8], "Dancer": [2, 3, 5], "Elder": [2, 3, 5],
    "BearRidge": [3, 5, 7, 10], "RuneLand": [2, 4, 6, 8, 11],
    "Treasure": [3, 4, 5, 6, 8],
    "Thunder": [2, 4, 6, 8],
    "ClassTank": [2, 4, 6, 8],
    "ClassArcher": [2, 4, 6, 8],
    "ClassMage": [2, 4, 6, 8],
    "ClassWarrior": [2, 4, 6, 8],
}
TRAIT_DESC = {
    "PotionClan": ("法强",
                   ["+12%", "+28%", "+50%", "+80%", "+120%"]),
    "LeopardKind": ("暴击",
                    ["+18%", "+38%", "+60%", "+85%", "+115%"]),
    "FrogTribe": ("生命/治疗",
                  ["+8%/+15%", "+20%/+38%", "+35%/+65%"]),
    "Lumber": ("伐木首领",
               ["(3) 首领吸收最近2名伐木90%基础生命，+60法强+60%物攻",
                "(5) 全员+55法强+55%物攻，首领双倍",
                "(8) 不吞噬，召唤远古树灵(全屏践踏)"]),
    "Dancer": ("攻速", ["+25%", "+45%", "+70%"]),
    "Elder": ("敌方攻击", ["-12%", "-22%", "-35%"]),
    "BearRidge": ("召唤团子", ["1星", "2星", "3星", "4星"]),
    "RuneLand": ("攻速/回蓝",
                 ["+10%/+1", "+22%/+2", "+36%/+3", "+52%/+4", "+70%/+5"]),
    "Treasure": ("",
                 ["在玩家战斗中获胜会获得2份藏宝碎片，失败会获得3份藏宝碎片",
                  "在玩家战斗中获胜会获得2份藏宝碎片，失败会获得4份藏宝碎片",
                  "在玩家战斗中获胜会获得3份藏宝碎片，失败会获得5份藏宝碎片",
                  "在玩家战斗中获胜会获得4份藏宝碎片，失败会获得7份藏宝碎片",
                  "激活藏宝秘境的终极形态，并解锁终极的第9层奖励！"]),
    "Thunder": ("雷霆整活",
                ["攻速+15%", "攻速+30%", "全场发弹幕", "全场狂暴"]),

    "ClassTank": ("坦克生命", ["+15%", "+30%", "+50%", "+80%"]),
    "ClassArcher": ("射手攻速", ["+15%", "+30%", "+50%", "+80%"]),
    "ClassMage": ("术士 攻强+法强", ["+15%", "+30%", "+50%", "+80%"]),
    "ClassWarrior": ("战士真伤", ["+10%", "+20%", "+35%", "+60%"]),
}
TRAIT_FLAVOR = {
    "Treasure": [
        "【财宝猎人】寻宝者必须四处搜寻线索，集齐10份藏宝碎片才能开启秘宝。",
        "秘宝开启后，选择立刻带走战利品，或者尝试继续寻宝来获得更好的奖励。",
    ],
}
TRAIT_COLOR = {"BearRidge": BEAR_COLOR, "RuneLand": RUNE_COLOR,
               "Treasure": TREASURE_COLOR}
BEAR_RIDGE_SUMMON_STAR = {3: 1, 5: 2, 7: 3, 10: 4}

SHOP_ODDS = {
    1: [100, 0, 0, 0, 0], 2: [100, 0, 0, 0, 0], 3: [75, 25, 0, 0, 0],
    4: [55, 30, 15, 0, 0], 5: [45, 33, 20, 2, 0], 6: [30, 40, 25, 5, 0],
    7: [19, 30, 35, 15, 1], 8: [18, 25, 32, 22, 3], 9: [15, 22, 30, 28, 5],
    10: [10, 20, 25, 35, 10],
}
XP_TABLE = {1: 2, 2: 6, 3: 10, 4: 20, 5: 32,
            6: 42, 7: 60, 8: 68, 9: 68, 10: 999}
MAX_LEVEL = 10
MAX_STAR = 4
REFRESH_COST = 2
BUY_XP_COST = 4
BUY_XP_AMOUNT = 4
DRAG_THRESHOLD = 8
START_GOLD_PLAYER = 0
START_GOLD_AI = 0
HEX_ROUND_INTERVAL = 3
MOVE_SPEED = 190
SEP_FORCE = 60
MANA_REGEN_3STAR_5COST = 7.0
MANA_REGEN_4STAR_5COST = 12.0
SKILL_CD_NORMAL = 2.5
SKILL_CD_3STAR_5COST = 2.0
SKILL_CD_4STAR_5COST = 1.5
MAX_ITEMS_PER_UNIT = 3
MAX_ITEM_BENCH = 10


def get_mana_regen(cost, star):
    if cost == 5:
        if star >= 4:
            return MANA_REGEN_4STAR_5COST
        elif star >= 3:
            return MANA_REGEN_3STAR_5COST
    return 0.0


def get_skill_cd(cost, star):
    if cost == 5:
        if star >= 4:
            return SKILL_CD_4STAR_5COST
        elif star >= 3:
            return SKILL_CD_3STAR_5COST
    return SKILL_CD_NORMAL


def safe_unit(u):
    if not isinstance(u, dict):
        return None
    # 原地修复，确保调用方无需接收返回值也能得到清洗结果。
    defaults = {"star": 1, "cost": 1, "name": "Unknown", "hp": 500,
                "ad": 40, "max_mana": 30, "mana_per_attack": 10,
                "attack_cooldown": 1.2, "sp_base_dmg": 0,
                "sp_multiplier": 1.0, "role": "warrior",
                "attack_range": RANGE_WARRIOR, "skill_desc": "",
                "armor": 0, "mr": 0, "skill_type": "damage"}
    for k, v in defaults.items():
        if u.get(k) is None:
            u[k] = v
    if not isinstance(u.get("traits"), list):
        u["traits"] = list(u.get("traits") or [])
    if not isinstance(u.get("items"), list):
        u["items"] = list(u.get("items") or [])
    if u.get("skill_dmg_type") is None:
        u["skill_dmg_type"] = ("magic" if u.get("role") == "mage" else "physical")
    try:
        u["star"] = max(1, min(MAX_STAR, int(u.get("star", 1))))
    except Exception:
        u["star"] = 1
    return u


def get_base_template(name):
    for c in CHAMPION_LIST:
        if c["name"] == name:
            return c
    return None


COST_COMPENSATION = {1: (1.08, 1.05), 2: (1.05, 1.03),
                     3: (1.03, 1.02), 4: (1.0, 1.0), 5: (1.0, 1.0)}



# ============================================================
#  v1.2.9 G：三星五费专属机制
# ============================================================
THREE_STAR_5COST = {
    "Dragon": {"title": "龙神降世", "color": (255, 100, 80), "tag": "summon"},
    "GuangTouQiang": {"title": "熊王狂怒", "color": (220, 150, 60), "tag": "warrior"},
    "BaoLan": {"title": "豹神终焉", "color": (230, 80, 230), "tag": "warrior"},
    "SuperLogger": {"title": "伐木天灾", "color": (100, 220, 100), "tag": "warrior"},
    "GodFrog": {"title": "蛙神天降", "color": (80, 240, 150), "tag": "mage"},
    "PotionCreator": {"title": "药神创世", "color": (255, 100, 140), "tag": "mage"},
    "ArcaneLord": {"title": "秘法终章", "color": (150, 100, 255), "tag": "mage"},
    "Tuanzi": {"title": "冰霜神域", "color": (150, 220, 255), "tag": "tank"},
    "ThunderPatch": {"title": "雷霆天罚", "color": (255, 230, 70), "tag": "warrior"},
    "AncientVial": {"title": "远古圣瓶", "color": (120, 220, 180), "tag": "tank"},
    "SwiftStrike": {"title": "疾斑灭世", "color": (255, 210, 90), "tag": "archer"},
}

def apply_three_star_5cost_stats(unit):
    """三星五费：高生命、高攻击，并记录专属机制标记。"""
    if unit.get("cost", 0) != 5 or unit.get("star", 1) < 3:
        return unit
    # 在原三星倍率基础上进一步强化，但保持不同费用的基础平衡关系。
    unit["hp"] = int(unit.get("hp", 1) * 1.30)
    unit["ad"] = int(unit.get("ad", 1) * 1.22)
    unit["sp_base_dmg"] = int(unit.get("sp_base_dmg", 0) * 1.25)
    info = THREE_STAR_5COST.get(unit.get("name"), {})
    unit["three_star_5cost"] = True
    unit["three_star_title"] = info.get("title", "终极形态")
    unit["three_star_color"] = info.get("color", (255, 220, 80))
    unit["three_star_tag"] = info.get("tag", unit.get("role", "warrior"))
    return unit

def trigger_three_star_5cost(unit, allies, enemies, effects, screen_w, screen_h):
    """三星五费施法时的质变机制。"""
    if not unit.base.get("three_star_5cost") or unit.base.get("star", 1) < 3:
        return
    tag = unit.base.get("three_star_tag", unit.base.get("role", "warrior"))
    c = unit.base.get("three_star_color", (255, 220, 80))
    alive_enemies = [e for e in enemies if e.alive]
    alive_allies = [a for a in allies if a.alive]
    if tag == "warrior":
        for e in alive_enemies:
            e.take_damage(max(1, int(unit.base.get("hp", 1) * 0.12)),
                          source=unit, dmg_type="true")
    elif tag == "mage":
        for e in alive_enemies:
            e.current_mana = max(0, e.current_mana - 25)
            e.take_damage(max(1, int(unit.base.get("sp_base_dmg", 1) * 0.28)),
                          source=unit, dmg_type="magic")
    elif tag == "tank":
        for a in alive_allies:
            a.shield += int(a.base.get("hp", 1) * 0.16)
    elif tag == "archer":
        for e in alive_enemies:
            e.take_damage(max(1, int(unit.base.get("ad", 1) * 1.2)),
                          source=unit, dmg_type="physical")
    elif tag == "summon":
        for a in alive_allies:
            a.current_mana = min(a.base.get("max_mana", 100),
                                 a.current_mana + 20)
    play_sfx("ult_" + unit.base.get("name", ""))
    effects.append({"type": "ultimate_cross", "x": unit.x, "y": unit.y,
                    "life": 1.0, "max_life": 1.0, "color": c})
    effects.append({"type": "skill_name", "x": unit.x,
                    "y": unit.y - 92,
                    "text": unit.base.get("three_star_title", "终极形态"),
                    "life": 1.6, "max_life": 1.6,
                    "color": c, "is_ult": True})

def make_unit_with_star(name, star):
    base = get_base_template(name)
    if base is None:
        return None
    try:
        star = int(star)
    except Exception:
        return None
    if star < 1 or star > MAX_STAR:
        return None
    u = copy.deepcopy(base)
    u["star"] = star
    scale = 1.8 ** (star - 1)
    cost = base.get("cost", 1)
    cb = COST_COMPENSATION.get(cost, (1.0, 1.0))
    u["hp"] = int(base["hp"] * scale * cb[0])
    u["ad"] = int(base["ad"] * scale * cb[1])
    apply_three_star_5cost_stats(u)
    return safe_unit(u)


def roll_shop_by_odds(level):
    odds = SHOP_ODDS.get(level, SHOP_ODDS[MAX_LEVEL])
    pools = {1: [], 2: [], 3: [], 4: [], 5: []}
    for c in CHAMPION_LIST:
        if c.get("no_shop"):
            continue
        cost = c.get("cost")
        if cost in pools and pool_remaining(c["name"]) > 0:
            pools[cost].append(c)

    shop = []
    offered_counts = {}
    for _ in range(5):
        r = random.randint(1, 100)
        cum = 0
        chosen_cost = 1
        for i, cost in enumerate([1, 2, 3, 4, 5]):
            cum += odds[i]
            if r <= cum:
                chosen_cost = cost
                break

        candidates = [c for c in pools.get(chosen_cost, [])
                      if pool_remaining(c["name"]) - offered_counts.get(c["name"], 0) > 0]
        if not candidates:
            candidates = [c for tier in (1, 2, 3, 4, 5)
                          for c in pools[tier]
                          if pool_remaining(c["name"]) - offered_counts.get(c["name"], 0) > 0]
        if not candidates:
            shop.append(None)
            continue

        weights = [pool_remaining(c["name"]) - offered_counts.get(c["name"], 0)
                   for c in candidates]
        picked = random.choices(candidates, weights=weights, k=1)[0]
        offered_counts[picked["name"]] = offered_counts.get(picked["name"], 0) + 1
        shop.append(copy.deepcopy(picked))
    return shop


def roll_shop_by_odds_free_five(level):
    odds = SHOP_ODDS.get(level, SHOP_ODDS[MAX_LEVEL])
    pools = {1: [], 2: [], 3: [], 4: [], 5: []}
    for c in CHAMPION_LIST:
        if c.get("no_shop"):
            continue
        cost = c.get("cost")
        if cost not in pools:
            continue
        if cost == 5 or pool_remaining(c["name"]) > 0:
            pools[cost].append(c)
    shop = []
    offered = {}
    for _ in range(5):
        r = random.randint(1, 100)
        cum = 0
        chosen_cost = 1
        for i, cost in enumerate([1, 2, 3, 4, 5]):
            cum += odds[i]
            if r <= cum:
                chosen_cost = cost
                break
        candidates = []
        for c in pools.get(chosen_cost, []):
            if c.get("cost") == 5 or pool_remaining(c["name"]) - offered.get(c["name"], 0) > 0:
                candidates.append(c)
        if not candidates:
            candidates = [c for tier in (1,2,3,4,5) for c in pools[tier]
                          if c.get("cost") == 5 or pool_remaining(c["name"]) - offered.get(c["name"],0) > 0]
        if not candidates:
            shop.append(None)
            continue
        picked = random.choice(candidates) if chosen_cost == 5 else random.choices(
            candidates, weights=[max(1, pool_remaining(c["name"]) - offered.get(c["name"],0))
                                 for c in candidates], k=1)[0]
        offered[picked["name"]] = offered.get(picked["name"],0) + 1
        shop.append(copy.deepcopy(picked))
    return shop


def count_board_units(p):
    return sum(1 for row in p["board"] for c in row if c is not None)


def get_population_cap(p):
    cap = p.get("level", 1)
    for row in p["board"]:
        for u in row:
            if u is None:
                continue
            for item in u.get("items", []):
                if not isinstance(item, dict):
                    continue
                stats = item.get("stats", {})
                if not isinstance(stats, dict):
                    continue
                pop = stats.get("population", 0)
                if isinstance(pop, (int, float)) and not isinstance(pop, bool) and math.isfinite(float(pop)):
                    cap += int(pop)
    return cap


def enforce_population_cap(p):
    cap = get_population_cap(p)
    on_board = [(r, c, p["board"][r][c])
                for r in range(4) for c in range(7)
                if p["board"][r][c] is not None]
    if len(on_board) <= cap:
        return
    on_board.sort(key=lambda x: (x[2].get("cost", 1), x[2].get("star", 1)))
    overflow = on_board[:len(on_board) - cap]
    for r, c, u in overflow:
        empty = next((i for i, s in enumerate(p["bench"]) if s is None), None)
        if empty is not None:
            p["board"][r][c] = None
            p["bench"][empty] = u
        elif not p.get("is_ai"):
            p["_pop_over_cap"] = True


def count_unit_owned(player, name, star):
    cnt = 0
    for row in player["board"]:
        for u in row:
            if u is not None and u.get("name") == name and u.get("star") == star:
                cnt += 1
    for u in player["bench"]:
        if u is not None and u.get("name") == name and u.get("star") == star:
            cnt += 1
    return cnt


def create_empty_player(gold=0, is_ai=False, difficulty_mult=1.0):
    return {
        "gold": gold, "hp": 100, "level": 1, "xp": 0,
        "xp_next": XP_TABLE[1],
        "win_streak": 0, "lose_streak": 0,
        "hex_bonuses": {"hp_mult": 0.0, "atk_mult": 0.0, "sp_mult": 0.0,
                        "crit": 0.0, "atk_speed": 0.0, "income": 0, "armor": 0},
        "hex_list": [], "items": [],
        "board": [[None] * 7 for _ in range(4)],
        "bench": [None] * 8, "shop": [],
        "is_ai": is_ai, "difficulty_mult": difficulty_mult
    }


ROLE_TO_CLASS_TRAIT = {"tank": "ClassTank", "archer": "ClassArcher",
                        "mage": "ClassMage", "warrior": "ClassWarrior"}


def sync_unit_traits_from_items(unit):
    """根据原生羁绊+当前可穿戴纹章重建棋子羁绊，杜绝拆卸/重铸残留。"""
    if not isinstance(unit, dict):
        return unit
    base = get_base_template(unit.get("name", "")) or {}
    traits = list(base.get("traits", []))
    for it in unit.get("items", []) if isinstance(unit.get("items", []), list) else []:
        if not _is_wearable_for_recovery(it):
            continue
        if it.get("is_emblem"):
            trait = it.get("emblem_trait") or it.get("trait")
            if trait and trait not in traits:
                traits.append(trait)
    unit["traits"] = traits
    return unit


def count_traits(player):
    tc = {}
    for row in player["board"]:
        for u in row:
            if u is None:
                continue
            name = u.get("name", "")
            if name == "Tuanzi":
                continue
            for t in u.get("traits", []):
                if t == "Summon":
                    continue
                tc[t] = tc.get(t, 0) + 1
            role = u.get("role", "warrior")
            class_trait = ROLE_TO_CLASS_TRAIT.get(role)
            if class_trait:
                tc[class_trait] = tc.get(class_trait, 0) + 1
    if player.get("_plunder_trait"):
        for trait in TRAIT_DATA:
            if trait.startswith("Class"):
                continue
            thresholds = TRAIT_DATA.get(trait, [])
            if thresholds:
                tc[trait] = max(tc.get(trait, 0), thresholds[-1])
    return tc


def _tier_val(tier, vals):
    if tier <= 0:
        return 0.0
    if tier >= len(vals):
        return vals[-1]
    return vals[tier]


def get_bear_ridge_summon_star(player):
    tc = count_traits(player)
    cnt = tc.get("BearRidge", 0)
    for threshold in (10, 7, 5, 3):
        if cnt >= threshold:
            return BEAR_RIDGE_SUMMON_STAR[threshold]
    return 0


def get_lumber_tier(player):
    """返回伐木羁绊激活档位：0=未激活, 1=(3), 2=(5), 3=(8)。"""
    tc = count_traits(player)
    cnt = tc.get("Lumber", 0)
    if cnt >= 8:
        return 3
    if cnt >= 5:
        return 2
    if cnt >= 3:
        return 1
    return 0


def get_treasure_gold(player):
    # v1.2.9：财宝猎人不再提供每回合固定金币，收益统一走收菜碎片。
    return 0


def apply_trait_buffs(player):
    tc = count_traits(player)
    buffs = {"atk_mult": 1.0, "hp_mult": 1.0, "sp_mult": 1.0, "crit": 0.0,
             "atk_speed_mult": 1.0, "enemy_atk_mult": 1.0,
             "extra_mana_per_attack": 0, "extra_armor": 0,
             "class_buffs": {}}
    for trait, count in tc.items():
        thresholds = TRAIT_DATA.get(trait, [])
        tier = sum(1 for t in thresholds if count >= t)
        if tier <= 0:
            continue
        if trait == "PotionClan":
            buffs["sp_mult"] += _tier_val(
                tier, [0.0, 0.12, 0.28, 0.50, 0.80, 1.20])
        elif trait == "LeopardKind":
            buffs["crit"] += _tier_val(
                tier, [0.0, 0.18, 0.38, 0.60, 0.85, 1.15])
        elif trait == "FrogTribe":
            buffs["hp_mult"] += _tier_val(
                tier, [0.0, 0.08, 0.20, 0.35])
            buffs["sp_mult"] += _tier_val(
                tier, [0.0, 0.15, 0.38, 0.65])
        elif trait == "Elder":
            buffs["enemy_atk_mult"] -= _tier_val(
                tier, [0.0, 0.12, 0.22, 0.35])
        elif trait == "Dancer":
            buffs["atk_speed_mult"] += _tier_val(
                tier, [0.0, 0.25, 0.45, 0.70])
        elif trait == "Thunder":
            buffs["atk_speed_mult"] += _tier_val(
                tier, [0.0, 0.15, 0.30, 0.50, 0.80])
        elif trait == "RuneLand":
            buffs["atk_speed_mult"] += _tier_val(
                tier, [0.0, 0.10, 0.22, 0.36, 0.52, 0.70])
            buffs["extra_mana_per_attack"] += int(
                _tier_val(tier, [0, 1, 2, 3, 4, 5]))
    for trait_key, role in (("ClassTank", "tank"),
                             ("ClassArcher", "archer"),
                             ("ClassMage", "mage"),
                             ("ClassWarrior", "warrior")):
        cnt = tc.get(trait_key, 0)
        thresholds = TRAIT_DATA.get(trait_key, [])
        tier = sum(1 for t in thresholds if cnt >= t)
        if tier <= 0:
            continue
        cb = buffs["class_buffs"].setdefault(role, {})
        if trait_key == "ClassTank":
            cb["hp_mult"] = _tier_val(tier, [1.0, 1.15, 1.30, 1.50, 1.80])
        elif trait_key == "ClassArcher":
            cb["atk_speed_mult"] = _tier_val(tier, [1.0, 1.15, 1.30, 1.50, 1.80])
        elif trait_key == "ClassMage":
            cb["atk_mult"] = _tier_val(tier, [1.0, 1.15, 1.30, 1.50, 1.80])
            cb["sp_mult"] = _tier_val(tier, [1.0, 1.15, 1.30, 1.50, 1.80])
        elif trait_key == "ClassWarrior":
            cb["true_dmg_bonus"] = _tier_val(tier, [0.0, 0.10, 0.20, 0.35, 0.60])
    return buffs


def merge_hex_into_buffs(buffs, player):
    hb = get_hex_bonuses(player)
    buffs["hp_mult"] *= hb["hp_mult"]
    buffs["atk_mult"] *= hb["atk_mult"]
    buffs["sp_mult"] *= hb["sp_mult"]
    buffs["crit"] += hb["crit"]
    buffs["atk_speed_mult"] *= hb["atk_speed"]
    buffs["extra_armor"] += hb.get("armor", 0)
    return buffs


def apply_income_and_xp(p):
    if p.get("is_monster"):
        return
    base = 5
    interest = min(5, p["gold"] // 10)
    streak = max(p["win_streak"], p["lose_streak"])
    streak_bonus = 3 if streak >= 5 else (2 if streak >= 3 else (1 if streak >= 2 else 0))
    hex_income = get_hex_bonuses(p)["income"]
    treasure_income = get_treasure_gold(p)
    total = base + interest + streak_bonus + hex_income + treasure_income
    mult = p.get("difficulty_mult", 1.0)
    if p.get("is_ai") and mult != 1.0:
        total = int(total * mult)
    p["gold"] += total
    if p["level"] < MAX_LEVEL:
        p["xp"] += 2
        while p["level"] < MAX_LEVEL and p["xp"] >= p["xp_next"]:
            p["xp"] -= p["xp_next"]
            p["level"] += 1
            p["xp_next"] = XP_TABLE[p["level"]]
        if p["level"] >= MAX_LEVEL:
            p["xp"] = 0
            p["xp_next"] = XP_TABLE[MAX_LEVEL]


def apply_battle_result(p, won):
    if p.get("is_monster"):
        return
    if won is None:
        p["win_streak"] = 0
        p["lose_streak"] = 0
        return
    if won:
        p["win_streak"] += 1
        p["lose_streak"] = 0
        p["gold"] += 1
    else:
        p["lose_streak"] += 1
        p["win_streak"] = 0


def auto_fill_board(p):
    cap = get_population_cap(p)
    cur = count_board_units(p)
    if cur >= cap:
        return
    board_ids = set()
    for row in p["board"]:
        for u in row:
            if u is not None:
                board_ids.add(id(u))
    while cur < cap:
        candidates = [(i, p["bench"][i]) for i in range(8)
                      if p["bench"][i] is not None
                      and not p["bench"][i].get("is_pseudo_bench_only")
                      and id(p["bench"][i]) not in board_ids]
        if not candidates:
            break
        candidates.sort(key=lambda x: (-x[1].get("star", 1),
                                        -x[1].get("cost", 1)))
        placed_any = False
        for idx, u in candidates:
            if cur >= cap:
                break
            role = u.get("role", "warrior")
            is_front = role in ("tank", "warrior")
            if is_front:
                slot_order = [(r, c) for r in (0, 1)
                              for c in (3, 2, 4, 1, 5, 0, 6)]
            else:
                slot_order = [(r, c) for r in (3, 2)
                              for c in (3, 2, 4, 1, 5, 0, 6)]
            placed = False
            for (r, c) in slot_order:
                if p["board"][r][c] is None:
                    p["board"][r][c] = u
                    p["bench"][idx] = None
                    board_ids.add(id(u))
                    cur += 1
                    placed = True
                    placed_any = True
                    break
            if not placed:
                for r in range(4):
                    for c in range(7):
                        if p["board"][r][c] is None:
                            p["board"][r][c] = u
                            p["bench"][idx] = None
                            board_ids.add(id(u))
                            cur += 1
                            placed = True
                            placed_any = True
                            break
                    if placed:
                        break
        if not placed_any:
            break


def ai_detect_target_traits(p):
    tc = count_traits(p)
    plan = p.get("_plan_traits")
    if plan:
        plan_count = sum(tc.get(t, 0) for t in plan)
        if plan_count > 0:
            return plan
    if tc:
        sorted_traits = sorted(tc.items(), key=lambda x: -x[1])
        plan = [t for t, c in sorted_traits[:2]]
    else:
        plan = random.choice([["BearRidge"], ["RuneLand"],
                              ["LeopardKind", "PotionClan"], ["Lumber"],
                              ["Dancer", "RuneLand"], ["Elder", "RuneLand"]])
    p["_plan_traits"] = plan
    return plan


def ai_card_score(p, card, target_traits):
    P = EXTREME_AI_PARAMS
    score = 0
    name = card["name"]
    cost = card["cost"]
    traits = card.get("traits", [])
    same1 = count_unit_owned(p, name, 1)
    same2 = count_unit_owned(p, name, 2)
    if same2 >= 2:
        score += P["w_star2_pair"]
    elif same2 == 1:
        score += P["w_star2_single"]
    elif same1 == 2:
        score += P["w_star1_pair"]
    elif same1 == 1:
        score += P["w_star1_single"]
    else:
        score += P["w_base"]
    owned_traits = count_traits(p)
    for t in traits:
        if t in target_traits:
            score += P["w_trait_plan"]
        elif t in owned_traits:
            score += P["w_trait_owned"]
    # 财宝猎人：场上已有财宝数越多越愿意买财宝卡（凑羁绊叠层收菜）
    if "Treasure" in traits:
        score += P.get("w_bounty_trait", 0) * (owned_traits.get("Treasure", 0) + 1)
    # 5费卡：当前等级5费刷新概率越高越愿意拿（配合高人口打高费阵容）
    if cost == 5:
        _odds5 = SHOP_ODDS.get(p["level"], SHOP_ODDS[MAX_LEVEL])[4]
        score += P.get("w_5cost", 0) * (_odds5 / 10.0)
    counter = p.get("_counter_target")
    if counter and counter in traits:
        score += P["w_counter"]
    score += cost * P["w_cost"]
    gold_after = p["gold"] - cost
    if gold_after < 5:
        score -= P["p_gold_low"]
    elif gold_after < 15:
        score -= P["p_gold_mid"]
    elif gold_after < 30:
        score -= P["p_gold_high"]
    return score


def ai_smart_buy(p):
    target_traits = ai_detect_target_traits(p)
    affordable = [c for c in p["shop"]
                  if c is not None and p["gold"] >= c["cost"]
                  and pool_remaining(c["name"]) > 0]
    if not affordable:
        return
    for _ in range(8):
        best_idx = -1
        best_score = -1
        for idx, c in enumerate(p["shop"]):
            if c is None or p["gold"] < c["cost"]:
                continue
            if pool_remaining(c["name"]) <= 0:
                p["shop"][idx] = None
                continue
            score = ai_card_score(p, c, target_traits)
            if score > best_score:
                best_score = score
                best_idx = idx
        if best_idx < 0 or best_score < EXTREME_AI_PARAMS["min_buy_score"]:
            break
        empty_bench = next((i for i, s in enumerate(p["bench"]) if s is None), None)
        if empty_bench is None:
            break
        c = p["shop"][best_idx]
        if not try_consume_pool(c["name"], 1):
            p["shop"][best_idx] = None
            continue
        p["gold"] -= c["cost"]
        p["bench"][empty_bench] = copy.deepcopy(c)
        p["shop"][best_idx] = None


def ai_simple_buy(p):
    if not p["shop"]:
        return
    affordable = [(i, c) for i, c in enumerate(p["shop"])
                  if c is not None and p["gold"] >= c["cost"]
                  and pool_remaining(c["name"]) > 0]
    if not affordable:
        return
    idx, c = min(affordable, key=lambda x: x[1]["cost"])
    empty = next((i for i, s in enumerate(p["bench"]) if s is None), None)
    if empty is None:
        return
    if not try_consume_pool(c["name"], 1):
        p["shop"][idx] = None
        return
    p["gold"] -= c["cost"]
    p["bench"][empty] = copy.deepcopy(c)
    p["shop"][idx] = None


def ai_buy_xp(p):
    if p["level"] >= MAX_LEVEL or p["gold"] < BUY_XP_COST:
        return False
    p["gold"] -= BUY_XP_COST
    p["xp"] += BUY_XP_AMOUNT
    while p["level"] < MAX_LEVEL and p["xp"] >= p["xp_next"]:
        p["xp"] -= p["xp_next"]
        p["level"] += 1
        p["xp_next"] = XP_TABLE[p["level"]]
    if p["level"] >= MAX_LEVEL:
        p["xp"] = 0
        p["xp_next"] = XP_TABLE[MAX_LEVEL]
    return True


def ai_smart_level_up(p):
    if p["level"] >= MAX_LEVEL:
        return
    behavior = get_ai_behavior(p)
    reserve = behavior.get("level_reserve", 20)
    if p["hp"] < 40:
        reserve = max(4, reserve // 2)
    # 特征修正：当前等级5费概率越高 → 越愿意花钱升人口（打高费/九五阵容）
    P = EXTREME_AI_PARAMS
    _odds5 = SHOP_ODDS.get(p["level"], SHOP_ODDS[MAX_LEVEL])[4]
    reserve -= int(P.get("w_level_up", 0) * (_odds5 / 10.0))
    reserve = max(2, reserve)
    while p["level"] < MAX_LEVEL and p["gold"] - BUY_XP_COST >= reserve:
        if not ai_buy_xp(p):
            break


def ai_sell_unit(p, location):
    if location[0] == "bench":
        idx = location[1]
        if 0 <= idx < 8 and p["bench"][idx]:
            u = p["bench"][idx]
            carried_items = list(u.get("items", []))
            inventory = p.setdefault("items", [])
            if len(inventory) + len(carried_items) > MAX_ITEM_BENCH:
                return False
            refund = u.get("cost", 1) * (3 ** (u.get("star", 1) - 1))
            inventory.extend(carried_items)
            p["gold"] += refund
            return_pool(u["name"], 3 ** (u.get("star", 1) - 1))
            p["bench"][idx] = None
            return True
    return False


def ai_find_worst_unit(p, target_traits):
    candidates = []
    for i, u in enumerate(p["bench"]):
        if u is None:
            continue
        score = 0
        score += u.get("star", 1) * 30
        score += u.get("cost", 1) * 5
        for t in u.get("traits", []):
            if t in target_traits:
                score += 15
        same = count_unit_owned(p, u["name"], u.get("star", 1))
        if same >= 2:
           score += 70
        elif same == 1:
              score += 35
        candidates.append((score, ("bench", i)))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0])
    return candidates[0][1]


def ai_clean_bench(p):
    target_traits = ai_detect_target_traits(p)
    for _ in range(8):
        empty = sum(1 for s in p["bench"] if s is None)
        if empty >= 2:
            break
        worst = ai_find_worst_unit(p, target_traits)
        if not worst:
            break
        unit = p["bench"][worst[1]]
        if unit is None or unit.get("star", 1) >= 2:
            break
        if not ai_sell_unit(p, worst):
            break


def ai_prune_weak_board_units(p, target_traits):
    for r in (3, 2, 1, 0):
        for c in range(7):
            u = p["board"][r][c]
            if u is None:
                continue
            if u.get("star", 1) >= 2:
                continue
            if u.get("cost", 1) >= 3:
                continue
            if any(t in target_traits for t in u.get("traits", [])):
                continue
            if count_unit_owned(p, u["name"], 1) >= 2:
                continue
            carried = list(u.get("items", []))
            if len(p.get("items", [])) + len(carried) > MAX_ITEM_BENCH:
                continue
            refund = u.get("cost", 1) * (3 ** (u.get("star", 1) - 1))
            p["items"].extend(carried)
            p["gold"] += refund
            return_pool(u["name"], 3 ** (u.get("star", 1) - 1))
            p["board"][r][c] = None
            return True
    return False


def ai_counter_pick(p, all_players):
    if not all_players:
        p.pop("_counter_target", None)
        return
    trait_freq = {}
    for other in all_players:
        if other is p or other.get("hp", 0) <= 0:
            continue
        tc = count_traits(other)
        for t, c in tc.items():
            if t == "Summon":
                continue
            trait_freq[t] = trait_freq.get(t, 0) + c
    if not trait_freq:
        p.pop("_counter_target", None)
        return
    popular = max(trait_freq.items(), key=lambda x: x[1])[0]
    p["_counter_target"] = popular


def ai_auto_position(p):
    cap = get_population_cap(p)
    all_units = []
    for r in range(4):
        for c in range(7):
            u = p["board"][r][c]
            if u:
                all_units.append(u)
                p["board"][r][c] = None
    for i in range(8):
        u = p["bench"][i]
        if u:
            all_units.append(u)
            p["bench"][i] = None
    role_order = {"tank": 0, "warrior": 1, "archer": 2, "mage": 3}
    all_units.sort(key=lambda u: (
        -u.get("star", 1) * 3 - u.get("cost", 1),
        role_order.get(u.get("role", "warrior"), 1),
    ))
    # Keep every owned unit. If ownership exceeds board cap + bench capacity,
    # retain overflow on the board rather than silently deleting units.
    board_target = min(len(all_units), max(cap, len(all_units) - len(p["bench"])))
    on_board = all_units[:board_target]
    on_bench = all_units[board_target:board_target + len(p["bench"])]
    front = [u for u in on_board if u.get("role") in ("tank", "warrior")]
    back = [u for u in on_board if u.get("role") in ("archer", "mage")]
    def _front_priority(u):
          star = u.get("star", 1)
          base_hp = u.get("hp", 500)
          star_mult = 1.8 ** (star - 1)
          role = u.get("role", "warrior")
          role_bonus = 300 if role == "tank" else 0
          return -(base_hp * star_mult + role_bonus)
    front.sort(key=_front_priority)
    back.sort(key=lambda u: (-u.get("cost", 1), -u.get("star", 1)))
    front_slots = [(0, 2), (0, 3), (0, 4), (0, 1), (0, 5), (0, 0), (0, 6),
                   (1, 2), (1, 3), (1, 4), (1, 1), (1, 5), (1, 0), (1, 6)]
    back_slots = [(3, 2), (3, 3), (3, 4), (3, 1), (3, 5), (3, 0), (3, 6),
                  (2, 2), (2, 3), (2, 4), (2, 1), (2, 5), (2, 0), (2, 6)]
    placed = 0
    for u in front:
        if placed >= len(front_slots):
            break
        for slot in front_slots:
            if p["board"][slot[0]][slot[1]] is None:
                p["board"][slot[0]][slot[1]] = u
                placed += 1
                break
    placed = 0
    for u in back:
        if placed >= len(back_slots):
            break
        for slot in back_slots:
            if p["board"][slot[0]][slot[1]] is None:
                p["board"][slot[0]][slot[1]] = u
                placed += 1
                break
    leftover = on_bench[:]
    for i in range(min(len(p["bench"]), len(leftover))):
        p["bench"][i] = leftover[i]


def _reclaim_illegal_equipped_items(p):
    """兜底清理：把历史版本误装配到棋子身上的消耗型道具回收回物品栏。

    覆盖棋盘 + 备战席；物品栏满则暂存溢出仓库(free_item_store)，不丢失道具。
    正常局内不会触发，用于修复旧存档/旧AI留下的脏状态。
    """
    containers = [u for row in p.get("board", []) for u in row if u is not None]
    containers += [u for u in p.get("bench", []) if u is not None]
    reclaimed = []
    for u in containers:
        items = u.get("items", [])
        if not items:
            continue
        keep = []
        for it in items:
            if is_wearable_item(it):
                keep.append(it)
            else:
                reclaimed.append(it)
        u["items"] = keep
    total = len(reclaimed)
    if not total:
        return 0
    inv = p.setdefault("items", [])
    space = MAX_ITEM_BENCH - len(inv)
    if space > 0:
        inv.extend(reclaimed[:space])
        reclaimed = reclaimed[space:]
    if reclaimed:
        p.setdefault("free_item_store", []).extend(reclaimed)
    return total


def _ai_equip_item(p, u, item):
    """AI 装配单件道具（兜底校验）：消耗型道具一律拒绝装配，留在物品栏。"""
    if not is_wearable_item(item):
        return False
    if len(u.get("items", [])) >= MAX_ITEMS_PER_UNIT:
        return False
    u.setdefault("items", []).append(item)
    u["items"] = try_combine_items_all(u["items"])
    return True


def ai_equip_items(p):
    if not p.get("items"):
        return
    while True:
        new_items, combined = try_combine_items(p["items"])
        p["items"] = new_items
        if not combined:
            break

    # 过滤一次性消耗道具（拆卸器/昊天锤/法球等）：只装配可穿戴装备，消耗道具留在物品栏
    wearable = [it for it in p["items"] if is_wearable_item(it)]
    leftover = [it for it in p["items"] if not is_wearable_item(it)]

    best_unit_pos = None
    best_score = -1
    for r in range(4):
        for c in range(7):
            u = p["board"][r][c]
            if u is None:
                continue
            if len(u.get("items", [])) >= MAX_ITEMS_PER_UNIT:
                continue
            score = u.get("star", 1) * 15 + u.get("cost", 1) * 2
            if u.get("cost", 1) == 5 and u.get("star", 1) >= 2:
                score += 30
            score -= len(u.get("items", [])) * 3
            if score > best_score:
                best_score = score
                best_unit_pos = ("board", r, c)
    if best_unit_pos is None:
        p["items"] = leftover + wearable
        return
    _, r, c = best_unit_pos
    u = p["board"][r][c]
    while wearable and len(u.get("items", [])) < MAX_ITEMS_PER_UNIT:
        item = wearable.pop(0)
        _ai_equip_item(p, u, item)
    p["items"] = leftover + wearable


def ai_smart_equip(p, all_players):
    if not p.get("items"):
        return
    p["items"] = try_combine_items_all(p["items"])

    # 过滤一次性消耗道具：smart_equip 只从可穿戴装备中挑选装配
    wearable = [it for it in p["items"] if is_wearable_item(it)]
    leftover = [it for it in p["items"] if not is_wearable_item(it)]

    phys = magic = 0
    for other in (all_players or []):
        if other is p or other.get("hp", 0) <= 0:
            continue
        for row in other["board"]:
            for u in row:
                if u is None:
                    continue
                role = u.get("role", "warrior")
                if role == "mage":
                    magic += 1
                elif role in ("archer", "warrior"):
                    phys += 1
    prefer = "armor" if phys >= magic else "mr"

    for _ in range(MAX_ITEM_BENCH):
        if not wearable:
            break
        target = None
        best = -1
        for r in range(4):
            for c in range(7):
                u = p["board"][r][c]
                if u is None:
                    continue
                if len(u.get("items", [])) >= MAX_ITEMS_PER_UNIT:
                    continue
                score = u.get("star", 1) * 10 + u.get("cost", 1)
                if u.get("role") == "tank":
                    score += 15
                if score > best:
                    best = score
                    target = u
        if target is None:
            break
        equipped = False
        for i, item in enumerate(wearable):
            stats = item.get("stats", {})
            if prefer in stats:
                wearable.pop(i)
                target.setdefault("items", []).append(item)
                target["items"] = try_combine_items_all(target["items"])
                equipped = True
                break
        if not equipped:
            item = wearable.pop(0)
            target.setdefault("items", []).append(item)
            target["items"] = try_combine_items_all(target["items"])
    p["items"] = leftover + wearable


# ============================================================
#  极限 AI 可进化参数（离线训练用）
# ============================================================
EXTREME_AI_PARAMS_DEFAULT = {
    # 行为开关（与 AI_BEHAVIOR 结构兼容，极难被打分器改）
    "skip_chance": 0.0,
    "prune_board": True,
    "counter_pick": True,
    "smart_equip": True,
    "refresh_budget": 20,
    "level_reserve": 8,
    # 买牌打分权重
    "w_star2_pair": 120,
    "w_star2_single": 40,
    "w_star1_pair": 90,
    "w_star1_single": 35,
    "w_base": 1,
    "w_trait_plan": 6,
    "w_trait_owned": 2,
    "w_counter": 4,
    "w_cost": 1,
    "p_gold_low": 10,
    "p_gold_mid": 4,
    "p_gold_high": 1,
    "min_buy_score": 4,
    # 新特征权重：财宝猎人 / 连败 / 血量 / 升级 / 5费
    "w_bounty_trait": 3,      # 场上财宝羁绊数 → 买财宝卡的倾向
    "w_bounty_layer": 4,      # 财宝层数 → 刷新投入（层越高越发力）
    "w_lose_streak": 2,       # 连败数 → 刷新投入（止血冲质量）
    "w_hp_low": 3,            # 血量压力 → 刷新投入（残血转连胜保命）
    "w_level_up": 2,          # 5费概率 → 升人口倾向（打高费阵容）
    "w_5cost": 2,             # 5费概率 → 买5费卡倾向
    # 分档经济决策
    "refresh_budget_low_hp": 10,
    "refresh_budget_mid_hp": 20,
    "refresh_budget_high_lv": 40,
    "refresh_budget_default": 50,
}
# 全局可变参数（被进化覆盖）
EXTREME_AI_PARAMS = dict(EXTREME_AI_PARAMS_DEFAULT)
EXTREME_AI_PARAMS_FILE = "extreme_ai_params.json"

# ================== 训练突破自动固化区 ==================
# 离线训练产生新的全局最优AI时，系统自动把最优权重写入下方 BUILTIN_EXTREME_AI
# （写入前自动生成 .bak 备份防断电损坏）。没有外部json的电脑直接用内置AI；
# 本地存在 extreme_ai_params.json 则优先读外部文件（训练运行时使用）。
# ----- BEGIN BUILTIN_EXTREME_AI AUTO SAVE -----
BUILTIN_EXTREME_AI = {
    "skip_chance": 0.0,
    "prune_board": True,
    "counter_pick": True,
    "smart_equip": True,
    "refresh_budget": 20,
    "level_reserve": 8,
    "w_star2_pair": 120,
    "w_star2_single": 40,
    "w_star1_pair": 90,
    "w_star1_single": 35,
    "w_base": 1,
    "w_trait_plan": 6,
    "w_trait_owned": 2,
    "w_counter": 4,
    "w_cost": 1,
    "p_gold_low": 10,
    "p_gold_mid": 4,
    "p_gold_high": 1,
    "min_buy_score": 4,
    "w_bounty_trait": 3,
    "w_bounty_layer": 4,
    "w_lose_streak": 2,
    "w_hp_low": 3,
    "w_level_up": 2,
    "w_5cost": 2,
    "refresh_budget_low_hp": 10,
    "refresh_budget_mid_hp": 20,
    "refresh_budget_high_lv": 40,
    "refresh_budget_default": 50,
}
# ----- END BUILTIN_EXTREME_AI AUTO SAVE -----


def _overwrite_builtin_ai_in_source(params):
    """训练突破安全固化：统一源码锁、AST校验、多份bak、原子替换。"""
    src_path = get_script_path()
    if not src_path or not os.path.exists(src_path):
        return False
    try:
        with _SOURCE_WRITE_LOCK:
            with open(src_path, "r", encoding="utf-8") as f:
                text = f.read()
            marker = "BEGIN BUILTIN_EXTREME_AI AUTO SAVE"
            end_marker = "END BUILTIN_EXTREME_AI AUTO SAVE"
            if marker not in text or end_marker not in text:
                return False
            body = ",\n    ".join(f'"{k}": {v!r}' for k, v in params.items())
            new_dict = "{\n    " + body + ",\n}"
            pattern = re.compile(r"BUILTIN_EXTREME_AI = .*?\n# ----- " + re.escape(end_marker), re.S)
            if not pattern.search(text):
                return False
            replacement = "BUILTIN_EXTREME_AI = " + new_dict + "\n# ----- " + end_marker
            text2 = pattern.sub(replacement, text)
            ast.parse(text2, filename=src_path)
            compile(text2, src_path, "exec")
            _rotate_source_backups(src_path, text, keep=3)
            _atomic_write_text(src_path, text2)
            return True
    except Exception as e:
        log_once("overwrite_builtin_ai", e)
        return False


def load_extreme_params():
    """读档：json 存在就用存档覆盖全局。缺新键用内置AI补齐，
    保证老存档可进化；无 json / 损坏则回退到源码内置AI（训练固化的最强AI）。"""
    global EXTREME_AI_PARAMS
    if not os.path.exists(EXTREME_AI_PARAMS_FILE):
        EXTREME_AI_PARAMS = dict(BUILTIN_EXTREME_AI)
        return False
    try:
        with open(EXTREME_AI_PARAMS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        merged = dict(BUILTIN_EXTREME_AI)
        for k, v in data.items():
            if k in merged:
                merged[k] = v
        EXTREME_AI_PARAMS = merged
        return True
    except Exception as e:
        log_once("load_extreme_params", e)
        EXTREME_AI_PARAMS = dict(BUILTIN_EXTREME_AI)
        return False


def save_extreme_params():
    try:
        with _AI_PARAMS_LOCK:
            text = json.dumps(EXTREME_AI_PARAMS, ensure_ascii=False, indent=2)
        _atomic_write_text(EXTREME_AI_PARAMS_FILE, text)
        return True
    except Exception as e:
        log_once("save_extreme_params", e)
        return False


def reset_extreme_params():
    global EXTREME_AI_PARAMS
    EXTREME_AI_PARAMS = dict(EXTREME_AI_PARAMS_DEFAULT)
    save_extreme_params()


# 启动时自动读档（有存档就用进化后的参数）
try:
    load_extreme_params()
except Exception:
    pass


def get_ai_behavior(p):
    # 快照对手：用自己的参数，不读全局
    override = p.get("_override_params")
    if override is not None:
        return override
    mult = p.get("difficulty_mult", 1.0)
    if mult <= 0.85:
        return AI_BEHAVIOR["easy"]
    if mult <= 1.15:
        return AI_BEHAVIOR["normal"]
    if mult <= 1.4:
        return AI_BEHAVIOR["hard"]
    # 极限 AI：返回可进化参数字典（含 behavior 字段 + 打分权重）
    with _AI_PARAMS_LOCK:
        return dict(EXTREME_AI_PARAMS)


# ============================================================
#  恭喜发财模式 & 三星五费博弈 & 噩梦AI学习玩家运营
# ============================================================
CONGRATS_NEECO_STAGE = 6          # 恭喜发财：阶段6结束存活单位100%保底大妮蔻
CONGRATS_NEECO_HP_TRIGGER = 50    # 恭喜发财：血量首次≤50给大妮蔻
_LEARN_PLAYER_STYLE = True        # 噩梦AI学习玩家运营开关（设置界面可切换）


def _congrats_five_cost_list():
    return [c for c in CHAMPION_LIST if c.get("cost") == 5 and not c.get("no_shop")]


def _give_congrats_start_unit(p):
    """恭喜发财：开局给一张随机五费进备战席（玩家与AI通用）。"""
    five = _congrats_five_cost_list()
    if not five:
        return False
    empty = next((i for i, s in enumerate(p["bench"]) if s is None), None)
    if empty is None:
        return False
    available = [c for c in five if pool_remaining(c["name"]) > 0]
    if not available:
        return False
    c = copy.deepcopy(random.choice(available))
    if not try_consume_pool(c["name"], 1):
        return False
    p["bench"][empty] = c
    return True


def _congrats_round_checks(gs):
    """恭喜发财回合检查：阶段6结束100%保底大妮蔻；血量首次≤50给大妮蔻。"""
    if (getattr(gs, "_congrats_mode", False)
            and not getattr(gs, "_congrats_neeko_given", False)
            and gs.stage[0] >= CONGRATS_NEECO_STAGE):
        gs._congrats_neeko_given = True
        gave = 0
        for p in [gs.me] + gs.players:
            if p.get("hp", 0) > 0 and len(p.get("items", [])) < MAX_ITEM_BENCH:
                p.setdefault("items", []).append(make_special_item("mega_neeko"))
                gave += 1
        gs.battle_log = (f"恭喜发财 · 阶段{gs.stage[0]}结算 · "
                         f"存活单位100%获得【大妮蔻】×1！({gave}家)")
        gs.battle_log_history.append(gs.battle_log)
    if (getattr(gs, "_congrats_mode", False)
            and not getattr(gs, "_congrats_50hp_given", False)
            and gs.me.get("hp", 100) <= CONGRATS_NEECO_HP_TRIGGER):
        gs._congrats_50hp_given = True
        if len(gs.me.get("items", [])) < MAX_ITEM_BENCH:
            gs.me.setdefault("items", []).append(make_special_item("mega_neeko"))
            gs.battle_log = "恭喜发财 · 血量跌破50 · 获得【大妮蔻】×1！"
            gs.battle_log_history.append(gs.battle_log)


def _star_to_copies(star):
    """棋子星级折算持有张数：1星=1张 / 2星=3张 / 3星=9张。"""
    return {1: 1, 2: 3, 3: 9}.get(star, star)


def _hold_count(p, name):
    """统计玩家持有某棋子的总张数（1星=1/2星=3/3星=9，棋盘+备战席）。"""
    total = 0
    for row in p.get("board", []):
        for u in row:
            if u and u.get("name") == name:
                total += _star_to_copies(u.get("star", 1))
    for u in p.get("bench", []):
        if u and u.get("name") == name:
            total += _star_to_copies(u.get("star", 1))
    return total


def _five_holdings(p):
    """返回该玩家持有的五费 dict: name -> 持有张数。"""
    out = {}
    for row in p.get("board", []):
        for u in row:
            if u and not u.get("is_pseudo_bench_only"):
                base = get_base_template(u.get("name", ""))
                if base and base.get("cost") == 5:
                    out[u["name"]] = out.get(u["name"], 0) + _star_to_copies(u.get("star", 1))
    for u in p.get("bench", []):
        if u:
            base = get_base_template(u.get("name", ""))
            if base and base.get("cost") == 5:
                out[u["name"]] = out.get(u["name"], 0) + _star_to_copies(u.get("star", 1))
    return out


def _someone_3star5(players, skip=None):
    """场上是否有玩家拥有三星五费；返回已三星的五费名集合。"""
    three = set()
    for q in players or []:
        if q is skip or q.get("hp", 0) <= 0:
            continue
        for name, cnt in _five_holdings(q).items():
            if cnt >= 9:
                three.add(name)
    return three


def _ai_chase_turn(p):
    """追星回合：大D目标五费，其余不买，保留金币底线，不卖目标。"""
    target = p.get("_chase_target")
    if not target:
        return
    for _ in range(50):
        if p.get("gold", 0) < 12:
            break
        p["gold"] = p.get("gold", 0) - REFRESH_COST
        p["shop"] = roll_shop_by_odds(p["level"])
        for s in p["shop"]:
            if s and s.get("name") == target and p.get("gold", 0) >= 1:
                empty = next((i for i, x in enumerate(p["bench"]) if x is None), None)
                if empty is not None and try_consume_pool(s.get("name", ""), 1):
                    p["gold"] -= 1
                    p["bench"][empty] = copy.deepcopy(s)
        ai_try_combine(p)


def _ai_try_chase_3star5(p, all_players=None):
    """极限AI（噩梦/恭喜发财标记 _extreme_chase）主动追三星五费：
    条件（目标五费已持≥5张/牌池+妮蔻足够/存活≤3/金币血量充足）齐备才启动；
    场上已有人三星五费 → 选其他五费对抗；无路可追 → 返回False走正常运营止损。
    普通排位AI无标记，完全不触发，保持校准好的段位梯度。"""
    if not p.get("_extreme_chase"):
        return False
    if p.get("hp", 0) <= 15 or p.get("gold", 0) < 50:
        p.pop("_chase_target", None)
        return False
    holdings = _five_holdings(p)
    if not holdings:
        return False
    three = _someone_3star5(all_players, skip=p)
    target = max((n for n, c in holdings.items()
                  if n not in three and c >= 5), key=holdings.get, default=None)
    if target is None:
        # 自己的五费都不够接近，或全是别人已三星的 → 正常运营止损
        p.pop("_chase_target", None)
        return False
    held = _hold_count(p, target)
    remaining = pool_remaining(target)
    neeko = sum(1 for it in p.get("items", [])
                if isinstance(it, dict) and it.get("special_kind") == "mega_neeko")
    potential = held + min(neeko, 3) + remaining
    if potential < 9:
        return False
    alive = sum(1 for q in (all_players or [p]) if q.get("hp", 0) > 0)
    if alive > 3 and p.get("gold", 0) < 80:
        return False
    p["_chase_target"] = target
    _ai_chase_turn(p)
    return True


def _player_style_profile():
    """从玩家历史对局统计画像：用于噩梦AI模仿+克制玩家运营。"""
    hist = _load_player_history()
    if len(hist) < 3:
        return None
    wins = sum(1 for h in hist if h.get("won"))
    avg_level = sum(h.get("level", 1) for h in hist) / len(hist)
    avg_stars = sum(h.get("stars", 0) for h in hist) / len(hist)
    return {"win_rate": wins / len(hist), "avg_level": avg_level,
            "avg_stars": avg_stars}


def _apply_learned_style(ai):
    """把玩家画像微调进噩梦AI参数：模仿运营倾向 + 轻度克制。"""
    if not _LEARN_PLAYER_STYLE:
        return
    prof = _player_style_profile()
    if not prof:
        return
    P = ai.get("_override_params")
    if not isinstance(P, dict):
        P = dict(EXTREME_AI_PARAMS)
        ai["_override_params"] = P
    if prof["avg_level"] >= 8:
        P["w_level_up"] = P.get("w_level_up", 2) + 2
        P["w_5cost"] = P.get("w_5cost", 2) + 1
    if prof["avg_stars"] >= 14:
        P["w_star2_pair"] = P.get("w_star2_pair", 120) + 20
        P["w_trait_plan"] = P.get("w_trait_plan", 6) + 2
    if prof["win_rate"] >= 0.6:
        P["w_counter"] = P.get("w_counter", 4) + 3


def ai_do_turn(p, all_players=None):
    behavior = get_ai_behavior(p)
    # 兜底：回收历史版本误装配到棋子身上的消耗型道具（拆卸器等），防止残留
    _reclaim_illegal_equipped_items(p)

    if behavior["skip_chance"] > 0 and random.random() < behavior["skip_chance"]:
        if not p.get("shop_locked"):
            p["shop"] = roll_shop_by_odds(p["level"])
        ai_simple_buy(p)
        ai_try_combine(p)
        ai_auto_position(p)
        return

    # 极限AI（噩梦/恭喜发财）三星五费博弈：条件齐备主动追星，有人三星则对抗/止损
    if _ai_try_chase_3star5(p, all_players):
        ai_try_combine(p)
        ai_auto_position(p)
        return

    if not p.get("shop_locked"):
        p["shop"] = roll_shop_by_odds(p["level"])

    ai_clean_bench(p)

    if behavior["counter_pick"]:
        ai_counter_pick(p, all_players)
    else:
        p.pop("_counter_target", None)

    if behavior["prune_board"]:
        target_traits = ai_detect_target_traits(p)
        ai_prune_weak_board_units(p, target_traits)

    for _ in range(3):
        bought_before = sum(1 for s in p["shop"] if s is None)
        ai_smart_buy(p)
        ai_try_combine(p)
        bought_after = sum(1 for s in p["shop"] if s is None)
        if bought_before == bought_after:
            break
    ai_smart_level_up(p)
    ai_equip_items(p)

    if behavior["smart_equip"]:
        ai_smart_equip(p, all_players)

    ai_auto_position(p)

    if behavior["refresh_budget"] is None:
        P = EXTREME_AI_PARAMS
        if p["hp"] < 25:
            refresh_budget = P["refresh_budget_low_hp"]
        elif p["hp"] < 40:
            refresh_budget = P["refresh_budget_mid_hp"]
        elif p["level"] >= 7:
            refresh_budget = P["refresh_budget_high_lv"]
        else:
            refresh_budget = P["refresh_budget_default"]
    else:
        refresh_budget = behavior["refresh_budget"]
    # 特征修正：财宝层数越高/连败越多/血量越危险 → 越激进投入刷新（冲质量保命/发力收菜）
    P = EXTREME_AI_PARAMS
    refresh_budget -= int(P.get("w_bounty_layer", 0) * max(0, p.get("_bounty_layer", 1) - 1))
    refresh_budget -= int(P.get("w_lose_streak", 0) * p.get("lose_streak", 0))
    refresh_budget -= int(P.get("w_hp_low", 0) * max(0, 40 - p["hp"]))
    refresh_budget = max(0, refresh_budget)

    if p["gold"] >= refresh_budget and p["gold"] >= REFRESH_COST:
        p["gold"] -= REFRESH_COST
        p["shop"] = roll_shop_by_odds(p["level"])
        ai_smart_buy(p)
        ai_try_combine(p)
        ai_auto_position(p)


# ============================================================
#  极限 AI 离线进化：无渲染模拟器 + 遗传算法
# ============================================================
_TRAINING_STATE = {
    "running": False,
    "stop_requested": False,
    "generation": 0,
    "best_score": 0.0,
    "best_params": None,
    "current_variant": 0,
    "current_population": 12,
    "current_games_per_variant": 6,
    "current_score": 0.0,
    "log": [],
    # 三阶段课程：1=普通 2=困难 3=自我对弈
    "phase": 1,
    "phase_label": "普通",
    "rank": "青铜",
    "pool_size": 2,
    "no_breakthrough_gens": 0,
}

# 前台游玩让步开关：主线程在打对局时置True，训练线程每候选评估后让出CPU片刻
_TRAINING_GIVE_WAY = False


# 对手池 + 段位：段位本质是池子大小
EXTREME_AI_OPPONENT_POOL = ["normal", "hard"]
EXTREME_AI_SNAPSHOT_POOL = []
EXTREME_AI_POOL_MAX = 30
EXTREME_AI_RANKS = [
    (2, "青铜"), (4, "白银"), (7, "黄金"), (10, "铂金"),
    (14, "钻石"), (19, "大师"), (25, "宗师"), (30, "王者"),
]


def _rank_from_pool(pool_size):
    """段位换算：池子越大段位越高。"""
    rank = "青铜"
    for need, r in EXTREME_AI_RANKS:
        if pool_size >= need:
            rank = r
    return rank


def _make_curriculum_opponent(phase):
    """按课程阶段生成对手：
    阶段1=普通AI；阶段2=困难AI；
    阶段3=基础对手+快照池+基于玩家对局数据的参考对手（自我对弈）。
    """
    if phase <= 1:
        return create_empty_player(gold=0, is_ai=True,
                                   difficulty_mult=DIFFICULTY_MULT["normal"])
    if phase == 2:
        return create_empty_player(gold=0, is_ai=True,
                                   difficulty_mult=DIFFICULTY_MULT["hard"])
    # 阶段3：有概率抽到基于玩家对局信息生成的对手（提取强度/节奏，供AI学习）
    if random.random() < 0.40:
        player_ai = _make_player_data_opponent()
        if player_ai is not None:
            return player_ai
    pool = EXTREME_AI_SNAPSHOT_POOL
    if pool and random.random() < 0.55:
        snap = random.choice(pool)
        p = create_empty_player(gold=0, is_ai=True, difficulty_mult=1.6)
        p["_override_params"] = dict(snap)
        return p
    choice = random.choice(EXTREME_AI_OPPONENT_POOL)
    return create_empty_player(gold=0, is_ai=True,
                               difficulty_mult=DIFFICULTY_MULT[choice])


def _record_snapshot(params):
    """阶段3：每次突破都把当前最优加进快照池。上限30，超了踢最旧。"""
    pool = EXTREME_AI_SNAPSHOT_POOL
    if len(pool) >= EXTREME_AI_POOL_MAX:
        pool.pop(0)
    pool.append(dict(params))
    _TRAINING_STATE["pool_size"] = len(pool) + len(EXTREME_AI_OPPONENT_POOL)
    _TRAINING_STATE["rank"] = _rank_from_pool(_TRAINING_STATE["pool_size"])


def _advance_phase_if_ready(score, thresholds):
    """阶段只能前进，不能回退。"""
    st = _TRAINING_STATE
    phase = st.get("phase", 1)
    if phase < 3:
        target = thresholds.get(phase)
        if target is not None and score >= target:
            st["phase"] = phase + 1
    st["phase_label"] = {1: "普通", 2: "困难", 3: "自我对弈"}.get(
        st["phase"], "自我对弈")
    st["pool_size"] = len(EXTREME_AI_SNAPSHOT_POOL) + len(EXTREME_AI_OPPONENT_POOL)
    st["rank"] = _rank_from_pool(st["pool_size"])


# ============================================================
#  训练断点存档：重进游戏接着上次继续，只强不弱
# ============================================================
TRAINING_STATE_SAVE_FILE = "training_progress.json"


def _save_training_progress():
    st = _TRAINING_STATE
    data = {
        "generation": st.get("generation", 0),
        "best_score": st.get("best_score", 0.0),
        "best_params": st.get("best_params"),
        "phase": st.get("phase", 1),
        "phase_label": st.get("phase_label", "普通"),
        "no_breakthrough_gens": st.get("no_breakthrough_gens", 0),
        "snapshot_pool": EXTREME_AI_SNAPSHOT_POOL,
    }
    try:
        _atomic_write_text(TRAINING_STATE_SAVE_FILE, json.dumps(data, ensure_ascii=False, indent=2))
        return True
    except Exception as e:
        log_once("save_training_progress", e)
        return False


def _load_training_progress():
    try:
        if not os.path.exists(TRAINING_STATE_SAVE_FILE):
            return None
        with open(TRAINING_STATE_SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        log_once("load_training_progress", e)
        return None


# ============================================================
#  排位赛：分数制段位 + 按段位匹配对手AI
# ============================================================
RANK_SAVE_FILE = "rank_save.json"
RANK_TABLE = [
    (0, "青铜"), (100, "白银"), (250, "黄金"), (450, "铂金"),
    (700, "钻石"), (1000, "大师"), (1400, "宗师"), (1900, "王者"),
]
RANK_WIN_PTS = 20
RANK_LOSE_PTS = 10
# 段位 -> 对手AI强度系数（收入与行为随难度缩放）
# 系数已过大样本校准（相邻段位各1000局对决 + 8人混战200局，吃鸡率单调0%→49%）
RANK_AI_MULT = {
    "青铜": 0.7, "白银": 0.9, "黄金": 1.0, "铂金": 1.2,
    "钻石": 1.3, "大师": 1.45, "宗师": 1.6, "王者": 1.75,
}
# 大师及以上：对手直接使用训练进化出的极限AI
RANK_EXTREME_AI_FROM = "大师"

# 排位段位顺序（用于虚高保护分数缩放）
RANK_ORDER_LIST = ["青铜", "白银", "黄金", "铂金", "钻石", "大师", "宗师", "王者"]

# ===================== 出厂内置全套段位AI（分发自带，无需外部json） =====================
# 别人下载你的游戏没有 ai_*.json，排位对手也不会降级：这里写死青铜→王者8档完整权重。
# 强度梯度经大样本校准：相邻段位1000局对决全部高段位占优（最低胜率53.7%，
# 95%CI下限50.6%），8人混战200局吃鸡率 青铜0%→王者49% 严格单调。
# 用户本地训练出更强AI时会生成 ai_xxx.json，加载优先级高于本内置池。
BUILTIN_RANKED_AI_POOL = {
    "青铜": {"mult": 0.7, "params": {
        "skip_chance": 0.30, "prune_board": False, "counter_pick": False,
        "smart_equip": False, "refresh_budget": 60, "level_reserve": 28,
        "w_star2_pair": 90, "w_star2_single": 30, "w_star1_pair": 60,
        "w_star1_single": 20, "w_base": 1, "w_trait_plan": 3,
        "w_trait_owned": 1, "w_counter": 1, "w_cost": 1,
        "p_gold_low": 2, "p_gold_mid": 1, "p_gold_high": 0,
        "min_buy_score": 2, "w_bounty_trait": 1, "w_bounty_layer": 1,
        "w_lose_streak": 0, "w_hp_low": 1, "w_level_up": 1, "w_5cost": 1,
        "refresh_budget_low_hp": 45, "refresh_budget_mid_hp": 50,
        "refresh_budget_high_lv": 55, "refresh_budget_default": 60,
    }},
    "白银": {"mult": 0.9, "params": {
        "skip_chance": 0.16, "prune_board": True, "counter_pick": False,
        "smart_equip": True, "refresh_budget": 45, "level_reserve": 24,
        "w_star2_pair": 110, "w_star2_single": 35, "w_star1_pair": 75,
        "w_star1_single": 25, "w_base": 1, "w_trait_plan": 5,
        "w_trait_owned": 2, "w_counter": 2, "w_cost": 1,
        "p_gold_low": 5, "p_gold_mid": 2, "p_gold_high": 1,
        "min_buy_score": 4, "w_bounty_trait": 2, "w_bounty_layer": 2,
        "w_lose_streak": 1, "w_hp_low": 2, "w_level_up": 2, "w_5cost": 1,
        "refresh_budget_low_hp": 30, "refresh_budget_mid_hp": 40,
        "refresh_budget_high_lv": 45, "refresh_budget_default": 50,
    }},
    "黄金": {"mult": 1.0, "params": {
        "skip_chance": 0.08, "prune_board": True, "counter_pick": True,
        "smart_equip": True, "refresh_budget": None, "level_reserve": 20,
        "w_star2_pair": 120, "w_star2_single": 40, "w_star1_pair": 90,
        "w_star1_single": 35, "w_base": 1, "w_trait_plan": 6,
        "w_trait_owned": 2, "w_counter": 4, "w_cost": 1,
        "p_gold_low": 10, "p_gold_mid": 4, "p_gold_high": 1,
        "min_buy_score": 4, "w_bounty_trait": 3, "w_bounty_layer": 4,
        "w_lose_streak": 2, "w_hp_low": 3, "w_level_up": 3, "w_5cost": 2,
        "refresh_budget_low_hp": 15, "refresh_budget_mid_hp": 25,
        "refresh_budget_high_lv": 40, "refresh_budget_default": 50,
    }},
    "铂金": {"mult": 1.2, "params": {
        "skip_chance": 0.0, "prune_board": True, "counter_pick": True,
        "smart_equip": True, "refresh_budget": 25, "level_reserve": 16,
        "w_star2_pair": 120, "w_star2_single": 40, "w_star1_pair": 90,
        "w_star1_single": 35, "w_base": 1, "w_trait_plan": 6,
        "w_trait_owned": 3, "w_counter": 5, "w_cost": 1,
        "p_gold_low": 12, "p_gold_mid": 5, "p_gold_high": 2,
        "min_buy_score": 4, "w_bounty_trait": 3, "w_bounty_layer": 3,
        "w_lose_streak": 3, "w_hp_low": 3, "w_level_up": 3, "w_5cost": 2,
        "refresh_budget_low_hp": 12, "refresh_budget_mid_hp": 20,
        "refresh_budget_high_lv": 35, "refresh_budget_default": 45,
    }},
    "钻石": {"mult": 1.3, "params": {
        "skip_chance": 0.0, "prune_board": True, "counter_pick": True,
        "smart_equip": True, "refresh_budget": 25, "level_reserve": 14,
        "w_star2_pair": 125, "w_star2_single": 42, "w_star1_pair": 95,
        "w_star1_single": 36, "w_base": 1, "w_trait_plan": 7,
        "w_trait_owned": 3, "w_counter": 6, "w_cost": 1,
        "p_gold_low": 14, "p_gold_mid": 6, "p_gold_high": 2,
        "min_buy_score": 4, "w_bounty_trait": 4, "w_bounty_layer": 4,
        "w_lose_streak": 4, "w_hp_low": 2, "w_level_up": 4, "w_5cost": 3,
        "refresh_budget_low_hp": 10, "refresh_budget_mid_hp": 18,
        "refresh_budget_high_lv": 32, "refresh_budget_default": 42,
    }},
    "大师": {"mult": 1.45, "params": {
        "skip_chance": 0.0, "prune_board": True, "counter_pick": True,
        "smart_equip": True, "refresh_budget": 20, "level_reserve": 10,
        "w_star2_pair": 130, "w_star2_single": 45, "w_star1_pair": 100,
        "w_star1_single": 38, "w_base": 1, "w_trait_plan": 8,
        "w_trait_owned": 3, "w_counter": 6, "w_cost": 1,
        "p_gold_low": 16, "p_gold_mid": 7, "p_gold_high": 3,
        "min_buy_score": 5, "w_bounty_trait": 5, "w_bounty_layer": 5,
        "w_lose_streak": 4, "w_hp_low": 2, "w_level_up": 6, "w_5cost": 5,
        "refresh_budget_low_hp": 8, "refresh_budget_mid_hp": 16,
        "refresh_budget_high_lv": 30, "refresh_budget_default": 40,
    }},
    "宗师": {"mult": 1.6, "params": {
        "skip_chance": 0.0, "prune_board": True, "counter_pick": True,
        "smart_equip": True, "refresh_budget": 20, "level_reserve": 9,
        "w_star2_pair": 135, "w_star2_single": 47, "w_star1_pair": 105,
        "w_star1_single": 40, "w_base": 1, "w_trait_plan": 9,
        "w_trait_owned": 3, "w_counter": 7, "w_cost": 1,
        "p_gold_low": 18, "p_gold_mid": 8, "p_gold_high": 3,
        "min_buy_score": 5, "w_bounty_trait": 6, "w_bounty_layer": 6,
        "w_lose_streak": 5, "w_hp_low": 2, "w_level_up": 7, "w_5cost": 6,
        "refresh_budget_low_hp": 6, "refresh_budget_mid_hp": 14,
        "refresh_budget_high_lv": 28, "refresh_budget_default": 36,
    }},
    "王者": {"mult": 1.75, "params": {
        "skip_chance": 0.0, "prune_board": True, "counter_pick": True,
        "smart_equip": True, "refresh_budget": 20, "level_reserve": 8,
        "w_star2_pair": 140, "w_star2_single": 50, "w_star1_pair": 110,
        "w_star1_single": 42, "w_base": 1, "w_trait_plan": 10,
        "w_trait_owned": 3, "w_counter": 7, "w_cost": 1,
        "p_gold_low": 20, "p_gold_mid": 9, "p_gold_high": 4,
        "min_buy_score": 5, "w_bounty_trait": 7, "w_bounty_layer": 7,
        "w_lose_streak": 5, "w_hp_low": 2, "w_level_up": 8, "w_5cost": 7,
        "refresh_budget_low_hp": 5, "refresh_budget_mid_hp": 12,
        "refresh_budget_high_lv": 25, "refresh_budget_default": 32,
    }},
}

RANK_STATE = {"score": 0, "wins": 0, "losses": 0, "rank": "青铜"}


def rank_from_score(score):
    rank = "青铜"
    for need, r in RANK_TABLE:
        if score >= need:
            rank = r
    return rank


def _rank_progress(score):
    """返回 (当前段起始分, 当前段名, 下一段名或None, 下一段起始分或None, 进度0~1)。"""
    cur_need, cur_rank = 0, RANK_TABLE[0][1]
    nxt_need, nxt_rank = None, None
    for need, r in RANK_TABLE:
        if score >= need:
            cur_need, cur_rank = need, r
        else:
            nxt_need, nxt_rank = need, r
            break
    if nxt_need is None:
        return cur_need, cur_rank, None, None, 1.0
    span = nxt_need - cur_need
    prog = 0.0 if span <= 0 else min(1.0, (score - cur_need) / span)
    return cur_need, cur_rank, nxt_rank, nxt_need, prog


def _rank_save_path():
    """排位存档优先使用脚本所在目录的绝对路径，
    防止工作目录不同导致结算写入丢失（修复打完段位没变化/重启归零）。"""
    base = os.path.dirname(get_script_path()) if get_script_path() else "."
    return os.path.join(base, RANK_SAVE_FILE)


def load_rank():
    global RANK_STATE
    data = None
    # 先读新绝对路径，再兼容旧版相对路径存档（自动迁移，不丢历史战绩）
    for path in (_rank_save_path(), RANK_SAVE_FILE):
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                break
        except Exception as e:
            log_once("load_rank", e)
    if data:
        for k in RANK_STATE:
            if k in data:
                RANK_STATE[k] = data[k]
    RANK_STATE["rank"] = rank_from_score(RANK_STATE.get("score", 0))
    return RANK_STATE


def save_rank():
    try:
        _atomic_write_text(_rank_save_path(), json.dumps(RANK_STATE, ensure_ascii=False, indent=2))
        return True
    except Exception as e:
        log_once("save_rank", e)
        return False


def rank_ai_mult(rank_name):
    return RANK_AI_MULT.get(rank_name, 1.0)


def _settle_rank_match(gs, rank_mode):
    """排位结算：胜利加分、失败扣分（青铜保底不清零），升/降段并存档。
    分数按【玩家段位 vs 对手真实段位】缩放：
    对手低于玩家（虚高保护）→ 赢少加输多扣；同段位 → 标准±20/10；
    对手更高 → 赢多加输少扣。"""
    won = gs.game_over_text == "胜利!"
    old_rank = rank_from_score(RANK_STATE.get("score", 0))
    p_rank = old_rank
    opp_rank = getattr(gs, "_opp_rank", None) or p_rank
    try:
        idx_p = RANK_ORDER_LIST.index(p_rank)
        idx_o = RANK_ORDER_LIST.index(opp_rank)
    except ValueError:
        idx_p = idx_o = 0
    if idx_o < idx_p:
        # 对手段位低于玩家：赢分减半、输分多扣50%，防止段位虚高
        win_pts = max(1, int(RANK_WIN_PTS * 0.5))
        lose_pts = RANK_LOSE_PTS + int(RANK_LOSE_PTS * 0.5)
    elif idx_o > idx_p:
        # 对手段位更高：赢分多50%、输分减半，鼓励越级挑战
        win_pts = RANK_WIN_PTS + int(RANK_WIN_PTS * 0.5)
        lose_pts = max(1, int(RANK_LOSE_PTS * 0.5))
    else:
        win_pts, lose_pts = RANK_WIN_PTS, RANK_LOSE_PTS
    if won:
        RANK_STATE["score"] = RANK_STATE.get("score", 0) + win_pts
        RANK_STATE["wins"] = RANK_STATE.get("wins", 0) + 1
        pts = win_pts
    else:
        RANK_STATE["score"] = max(0, RANK_STATE.get("score", 0) - lose_pts)
        RANK_STATE["losses"] = RANK_STATE.get("losses", 0) + 1
        pts = -lose_pts
    new_rank = rank_from_score(RANK_STATE["score"])
    RANK_STATE["rank"] = new_rank
    save_rank()
    invasion = " · 噩梦AI入侵" if getattr(gs, "_nightmare_invasion", False) else ""
    settle = (f"排位结算: {'胜利' if won else '失败'} {pts:+d}分 · "
              f"对手{opp_rank}AI{invasion} · {old_rank} → {new_rank} · 总分 {RANK_STATE['score']}")
    gs.rank_settle_text = settle
    gs.battle_log = settle
    gs.battle_log_history.append(settle)


# 启动时读取排位存档
try:
    load_rank()
except Exception:
    pass


# ============================================================
#  AI 段位体系：按评估平均分自动分档，分档存档
# ============================================================
AI_RANK_THRESHOLDS = [
    ("青铜", 80.0), ("白银", 110.0), ("黄金", 150.0), ("铂金", 200.0),
    ("钻石", 260.0), ("大师", 320.0), ("宗师", 390.0), ("王者", 460.0),
]
AI_RANK_FILES = {
    "青铜": "ai_bronze.json", "白银": "ai_silver.json",
    "黄金": "ai_gold.json", "铂金": "ai_platinum.json",
    "钻石": "ai_diamond.json", "大师": "ai_master.json",
    "宗师": "ai_grandmaster.json", "王者": "ai_king.json",
}


def _ai_rank_from_score(score):
    """按评估平均分给AI分段位：青铜最低，王者最高。"""
    rank = "青铜"
    for r, need in AI_RANK_THRESHOLDS:
        if score >= need:
            rank = r
    return rank


def _save_ranked_ai(rank, params, score):
    """把某段位AI存档。同段位只保留更高分，弱的不会覆盖强的。"""
    fname = AI_RANK_FILES.get(rank)
    if fname is None:
        return False
    try:
        old = None
        if os.path.exists(fname):
            with open(fname, "r", encoding="utf-8") as f:
                old = json.load(f)
        if old is not None and old.get("score", 0.0) >= score:
            return False
        _atomic_write_text(fname, json.dumps({"rank": rank, "score": score, "params": params}, ensure_ascii=False, indent=2))
        return True
    except Exception as e:
        log_once("save_ranked_ai", e)
        return False


def _load_ranked_ai(rank):
    """读取某段位AI，返回 (params, score, mult, source)。
    优先本地 ai_xxx.json（用户离线训练覆盖，更强则生效）；
    本地缺失使用源码内置段位池（分发自带，下载即用）；
    source ∈ {"local", "builtin", "missing"}。"""
    fname = AI_RANK_FILES.get(rank)
    builtin = BUILTIN_RANKED_AI_POOL.get(rank)
    builtin_params = dict(builtin["params"]) if builtin else dict(EXTREME_AI_PARAMS)
    builtin_mult = builtin["mult"] if builtin else rank_ai_mult(rank)
    if fname is not None:
        try:
            if os.path.exists(fname):
                with open(fname, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if data.get("params"):
                    merged = dict(builtin_params)
                    for k, v in data["params"].items():
                        if k in merged:
                            merged[k] = v
                    return merged, float(data.get("score", 0.0)), \
                        builtin_mult, "local"
        except Exception as e:
            log_once("load_ranked_ai", e)
    if builtin is not None:
        return builtin_params, 0.0, builtin_mult, "builtin"
    return None, 0.0, rank_ai_mult(rank), "missing"


def _ranked_opponent_ai(player_rank):
    """排位对手AI匹配：同段位本地训练存档优先 → 内置出厂段位池兜底 →
    异常时向下借已存在段位 → 全局最强极限AI最终兜底。
    返回 (参数, 难度系数, 来源文案, 对手真实段位)。"""
    params, score, mult, source = _load_ranked_ai(player_rank)
    if source == "local":
        return params, mult, f"{player_rank}段位AI（训练存档 {score:.0f}分）", \
            player_rank
    if source == "builtin":
        return params, mult, f"{player_rank}段位AI（内置出厂梯度·千局校准）", \
            player_rank
    # 防御兜底：向下找已存在段位，避免玩家段位虚高无对手
    try:
        idx = RANK_ORDER_LIST.index(player_rank)
    except ValueError:
        idx = 0
    for i in range(idx - 1, -1, -1):
        r = RANK_ORDER_LIST[i]
        p2, s2, m2, src2 = _load_ranked_ai(r)
        if src2 != "missing":
            return p2, m2, f"未找到{player_rank}段位AI，下借{r}段位AI（{src2}）", r
    return dict(EXTREME_AI_PARAMS), rank_ai_mult("王者"), \
        "未找到任何段位AI，使用全局最强极限AI替补", "王者"


# ============================================================
#  玩家对局信息提取：训练时利用你的对局数据继续学习
#  （提取强度/节奏等统计特征生成参考对手，不是复刻你的操作）
# ============================================================
PLAYER_HISTORY_FILE = "player_history.json"
PLAYER_HISTORY_MAX = 50


def _count_stars(player):
    s = 0
    for row in player["board"]:
        for u in row:
            if u:
                s += u.get("star", 1)
    for u in player["bench"]:
        if u:
            s += u.get("star", 1)
    return s


def _count_units(player):
    n = 0
    for row in player["board"]:
        for u in row:
            if u:
                n += 1
    for u in player["bench"]:
        if u:
            n += 1
    return n


def _count_items(player):
    n = len(player.get("items", []))
    for row in player["board"]:
        for u in row:
            if u:
                n += len(u.get("items", []))
    for u in player["bench"]:
        if u:
            n += len(u.get("items", []))
    return n


def _player_strength_mult(rec):
    """玩家对局记录 → 玩家风格对手的难度系数（0.7~1.75）。"""
    score = 40.0
    if rec.get("won"):
        score += 45.0
    score += min(rec.get("hp", 0), 100) * 0.1
    score += rec.get("level", 1) * 3.0
    score += rec.get("stars", 0) * 2.0
    score += min(rec.get("units", 0), 28) * 1.0
    mult = 0.7 + (score - 40.0) * 0.015
    return max(0.7, min(1.75, mult))


def _record_player_game(gs, mode):
    """提取玩家每局的行为统计（普通/排位/联机都记），
    供训练阶段3生成基于玩家数据的参考对手。"""
    me = gs.me
    won = gs.game_over_text == "胜利!"
    record = {
        "time": int(time.time()),
        "mode": mode,
        "won": won,
        "rounds": gs.round_counter,
        "gold": me.get("gold", 0),
        "hp": me.get("hp", 0),
        "level": me.get("level", 1),
        "stars": _count_stars(me),
        "units": _count_units(me),
        "items": _count_items(me),
        "streak": me.get("win_streak", 0) + me.get("lose_streak", 0),
    }
    record["strength_mult"] = _player_strength_mult(record)
    try:
        hist = []
        if os.path.exists(PLAYER_HISTORY_FILE):
            with open(PLAYER_HISTORY_FILE, "r", encoding="utf-8") as f:
                hist = json.load(f)
        if not isinstance(hist, list):
            hist = []
        hist.append(record)
        if len(hist) > PLAYER_HISTORY_MAX:
            hist = hist[-PLAYER_HISTORY_MAX:]
        _atomic_write_text(PLAYER_HISTORY_FILE, json.dumps(hist, ensure_ascii=False, indent=2))
        return True
    except Exception as e:
        log_once("record_player_game", e)
        return False


def _load_player_history():
    try:
        if not os.path.exists(PLAYER_HISTORY_FILE):
            return []
        with open(PLAYER_HISTORY_FILE, "r", encoding="utf-8") as f:            hist = json.load(f)
        return hist if isinstance(hist, list) else []
    except Exception as e:
        log_once("load_player_history", e)
        return []


def _clear_player_history():
    """一键清空玩家学习样本：删除 player_history.json，AI 遗忘玩家打法。"""
    try:
        if os.path.exists(PLAYER_HISTORY_FILE):
            os.remove(PLAYER_HISTORY_FILE)
        return True
    except Exception as e:
        log_once("clear_player_history", e)
        return False


def _make_player_data_opponent():
    """从玩家历史对局随机抽一条，提取其统计信息（强度系数/人口/星级/规模）
    生成一个参考对手，AI 借这类对手继续学习。
    强度系数按你该局的表现推算，行为档次随强度变化。"""
    hist = _load_player_history()
    if not hist:
        return None
    rec = random.choice(hist)
    p = create_empty_player(gold=0, is_ai=True,
                            difficulty_mult=rec.get("strength_mult", 1.0))
    p["_from_player_data"] = True
    p["_player_info"] = {k: rec.get(k) for k in
                         ("mode", "won", "level", "stars", "units")}
    return p


def _sim_battle_strength(player):
    """无渲染战力估算：cost * 3^(star-1) * 装备加成。"""
    total = 0.0
    for row in player.get("board", []):
        for u in row:
            if u is None:
                continue
            cost = u.get("cost", 1)
            star = u.get("star", 1)
            item_bonus = 1.0 + 0.12 * len(u.get("items", []))
            total += cost * (3 ** (star - 1)) * item_bonus
    return total


def _sim_bounty_round(p):
    """模拟器内的财宝猎人简化模拟：
    Treasure≥3 时按胜负积累藏宝碎片，满10升1层；到上限自动收菜发金币并重置。"""
    tc = count_traits(p).get("Treasure", 0)
    if tc < 3:
        return
    max_layer = 9 if tc >= 8 else 8
    layer = p.get("_bounty_layer", 1)
    if layer >= max_layer:
        # 到上限自动收菜：按层数发金币（高层=高级菜，奖励更丰厚）
        p["gold"] = p.get("gold", 0) + layer * 6
        p["_bounty_layer"] = 1
        p["_bounty_shards"] = 0
        return
    won = p.get("win_streak", 0) > 0
    gain = _bounty_gain(tc, won)
    if gain <= 0:
        return
    shards = p.get("_bounty_shards", 0) + gain
    while shards >= 10 and layer < max_layer:
        shards -= 10
        layer += 1
    p["_bounty_shards"] = shards
    p["_bounty_layer"] = layer


def _sanitize_sim_item(it):
    if not isinstance(it, dict):
        return None
    stats = it.get("stats")
    if not isinstance(stats, dict):
        stats = {}
    clean_stats = {}
    for k, v in stats.items():
        if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(float(v)):
            clean_stats[k] = v
    it["stats"] = clean_stats
    return it


def _sanitize_sim_player(p):
    """无渲染模拟器入口清洗脏状态；训练/Fuzz不得因None或非法容器直接崩溃。"""
    if not isinstance(p, dict):
        p = create_empty_player(gold=0, is_ai=True)
    numeric_defaults = {
        "gold": 0, "hp": 100, "level": 1, "xp": 0,
        "xp_next": XP_TABLE.get(1, 2) if isinstance(XP_TABLE, dict) else 2,
        "win_streak": 0, "lose_streak": 0, "difficulty_mult": 1.0,
    }
    for k, default in numeric_defaults.items():
        v = p.get(k, default)
        if not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(float(v)):
            v = default
        if k in ("gold", "hp", "level", "xp", "xp_next", "win_streak", "lose_streak"):
            v = int(v)
        p[k] = v
    p["gold"] = max(0, p["gold"])
    p["hp"] = max(0, min(1000, p["hp"]))
    p["level"] = max(1, min(MAX_LEVEL, p["level"]))
    for key in ("board",):
        board = p.get(key)
        if not isinstance(board, list):
            board = []
        board2 = []
        for r in range(4):
            row = board[r] if r < len(board) and isinstance(board[r], list) else []
            row2 = []
            for c in range(7):
                u = row[c] if c < len(row) else None
                if isinstance(u, dict):
                    u = safe_unit(u)
                    if u and not get_base_template(u.get("name", "")):
                        u = None
                    if u:
                        u["items"] = [x for x in (_sanitize_sim_item(it) for it in u.get("items", [])) if x is not None]
                        sync_unit_traits_from_items(u)
                else:
                    u = None
                row2.append(u)
            board2.append(row2)
        p["board"] = board2
    bench = p.get("bench")
    if not isinstance(bench, list):
        bench = []
    bench2 = []
    for i in range(8):
        u = bench[i] if i < len(bench) else None
        if isinstance(u, dict):
            u = safe_unit(u)
            if u and not get_base_template(u.get("name", "")):
                u = None
            if u:
                u["items"] = [x for x in (_sanitize_sim_item(it) for it in u.get("items", [])) if x is not None]
                sync_unit_traits_from_items(u)
        else:
            u = None
        bench2.append(u)
    p["bench"] = bench2
    if not isinstance(p.get("items"), list):
        p["items"] = []
    p["items"] = [x for x in (_sanitize_sim_item(it) for it in p["items"]) if x is not None]
    return p


def _sim_run_one_game(players, max_rounds=35):
    """无渲染跑一局；使用线程本地独立卡池，不污染真实对局。"""
    old_pool = getattr(_SIM_POOL_LOCAL, "pool", None)
    _SIM_POOL_LOCAL.pool = _make_pool_snapshot()
    players = [_sanitize_sim_player(p) for p in (players or [])]
    try:
        return _sim_run_one_game_inner(players, max_rounds)
    finally:
        _SIM_POOL_LOCAL.pool = old_pool


def _sim_run_one_game_inner(players, max_rounds=35):
    stage, rnd = 1, 2
    while max_rounds > 0:
        alive = [p for p in players if p["hp"] > 0]
        if len(alive) <= 1:
            break
        # AI 运营
        for p in players:
            if p["hp"] <= 0:
                continue
            try:
                ai_do_turn(p, players)
            except Exception as e:
                raise RuntimeError(f"AI模拟候选异常: {p.get('name', '?')}") from e
        # 战力配对
        alive = [p for p in players if p["hp"] > 0]
        random.shuffle(alive)
        i = 0
        while i + 1 < len(alive):
            a, b = alive[i], alive[i + 1]
            sa = _sim_battle_strength(a)
            sb = _sim_battle_strength(b)
            if sa >= sb:
                loser, winner = b, a
            else:
                loser, winner = a, b
            # 估算输方掉血：5 + 存活单位数
            survivors = sum(1 for row in winner["board"] for u in row if u)
            dmg = 5 + random.randint(0, 3) + survivors
            loser["hp"] -= dmg
            winner["win_streak"] += 1
            winner["lose_streak"] = 0
            loser["lose_streak"] += 1
            loser["win_streak"] = 0
            i += 2
        # 回合结束：发钱发经验
        for p in players:
            if p["hp"] > 0:
                apply_income_and_xp(p)
        # 财宝猎人简化模拟：碎片→层数→到上限自动收菜
        for p in players:
            if p["hp"] > 0:
                _sim_bounty_round(p)
        # 推进阶段
        if stage == 1:
            if rnd < STAGE1_ROUNDS:
                rnd += 1
            else:
                stage, rnd = 2, 1
        else:
            if rnd < STAGE_NORMAL_ROUNDS:
                rnd += 1
            else:
                stage, rnd = stage + 1, 1
        max_rounds -= 1
    # 排名：hp 优先，其次等级，再次战力
    def _rank_key(p):
        return (p["hp"], p.get("level", 1), _sim_battle_strength(p))
    return sorted(players, key=_rank_key, reverse=True)


def _sim_evaluate_params(params, games=10):
    """评估候选AI参数；候选参数只挂在候选玩家上，不修改全局。"""
    total_score = 0.0
    wins = 0
    phase = _TRAINING_STATE.get("phase", 1)
    for _ in range(games):
        players = []
        for i in range(8):
            if i == 0:
                p = create_empty_player(gold=0, is_ai=True, difficulty_mult=1.6)
                p["_override_params"] = dict(params)
            else:
                p = _make_curriculum_opponent(phase)
            one_cost = [c for c in CHAMPION_LIST if c["cost"] == 1 and not c.get("no_shop")]
            if one_cost:
                c = random.choice(one_cost)
                u = make_unit_with_star(c["name"], 1)
                if u:
                    p["bench"][0] = u
            players.append(p)
        try:
            ranked = _sim_run_one_game(players)
        except Exception:
            return -1e9, 0.0
        rank_idx = ranked.index(players[0])
        if rank_idx == 0:
            wins += 1
            total_score += 100
        elif rank_idx == 1:
            total_score += 60
        elif rank_idx == 2:
            total_score += 30
        elif rank_idx == 3:
            total_score += 10
        total_score += max(0, players[0]["hp"]) * 0.5
    return total_score / max(1, games), wins / max(1, games)


def _mutate_params(base, intensity=0.15, big_mutation=False):
    """在 base 参数上做随机扰动，返回新字典。布尔字段不扰动。
    big_mutation=True 时只随机挑少量(≤3)字段大幅重置、其余字段照常小扰动：
    既保留对局部极值的爬坡能力，又保留探索全新策略的空间，
    避免把整个候选全盘打乱成随机垃圾（旧实现导致停滞期永远追不上历史最优）。"""
    new_p = dict(base)
    heavy = set()
    if big_mutation:
        numeric_keys = [k for k, v in base.items() if not isinstance(v, bool)]
        if numeric_keys:
            heavy = set(random.sample(numeric_keys, min(3, len(numeric_keys))))
    for k, v in base.items():
        if isinstance(v, bool):
            continue
        if k in heavy:
            # 大变异：仅对选中的少数字段大幅扰动，强行探索新思路
            if isinstance(v, float):
                if v == 0:
                    new_p[k] = random.uniform(-0.05, 0.5)
                else:
                    new_p[k] = v + random.uniform(-abs(v) * 0.8, abs(v) * 0.8)
            elif isinstance(v, int):
                if v == 0:
                    new_p[k] = random.randint(0, 12)
                else:
                    new_p[k] = v + random.randint(
                        -int(abs(v) * 0.8), int(abs(v) * 0.8))
            else:
                continue
        elif isinstance(v, float):
            delta = max(0.01, abs(v) * intensity)
            new_p[k] = v + random.uniform(-delta, delta)
        elif isinstance(v, int):
            delta = max(1, int(abs(v) * intensity))
            new_p[k] = v + random.randint(-delta, delta)
        else:
            continue
        # 边界保护
        if k == "skip_chance":
            new_p[k] = max(0.0, min(0.5, float(new_p[k])))
        elif k.startswith("w_") or k.startswith("p_"):
            new_p[k] = max(0, new_p[k])
        elif k.startswith("refresh_budget"):
            new_p[k] = max(5, min(80, new_p[k]))
        elif k.startswith("level_reserve"):
            new_p[k] = max(0, min(30, new_p[k]))
    return new_p


def _shuffle_opponent_pool():
    """停滞过久时打乱对手池：淘汰随机旧对手，补充大幅变异的新对手。"""
    pool = EXTREME_AI_SNAPSHOT_POOL
    if not pool:
        return
    remove_n = min(2, max(1, len(pool) // 2))
    for _ in range(remove_n):
        pool.pop(random.randrange(len(pool)))
    for _ in range(remove_n):
        pool.append(dict(_mutate_params(dict(EXTREME_AI_PARAMS),
                                        intensity=0.3, big_mutation=True)))
    st = _TRAINING_STATE
    st["pool_size"] = len(pool) + len(EXTREME_AI_OPPONENT_POOL)
    st["rank"] = _rank_from_pool(st["pool_size"])
    st["log"].append("停滞超限，打乱对手池，补充变异新对手")


def ai_try_combine(target_player):
    """三合一升星：扫描棋盘+备战席，凑齐3个同名同星就升1星。"""
    while True:
        groups = {}
        for r, row in enumerate(target_player["board"]):
            for c, unit in enumerate(row):
                if unit is not None:
                    safe_unit(unit)
                    groups.setdefault((unit["name"], unit["star"]), []).append(
                        ("board", r, c))
        for idx, unit in enumerate(target_player["bench"]):
            if unit is not None:
                safe_unit(unit)
                groups.setdefault((unit["name"], unit["star"]), []).append(
                    ("bench", idx, 0))
        combined = False
        for key, pos_list in groups.items():
            name, star = key
            if star >= MAX_STAR or len(pos_list) < 3:
                continue
            take3 = pos_list[:3]
            board_pos = None
            for typ, a, b in take3:
                if typ == "board":
                    board_pos = (a, b)
                    break
            bench_slot = next((i for i in range(8)
                               if target_player["bench"][i] is None), None)
            if board_pos is None and bench_slot is None:
                continue
            u_template = None
            for typ, a, b in take3:
                if typ == "board":
                    u_template = target_player["board"][a][b]
                else:
                    u_template = target_player["bench"][a]
                if u_template:
                    break
            if u_template is None:
                continue
            new_unit = make_unit_with_star(u_template["name"], star + 1)
            if new_unit is None:
                continue
            all_items = []
            for typ, a, b in take3:
                u_old = target_player["board"][a][b] if typ == "board" \
                    else target_player["bench"][a]
                if u_old:
                    all_items.extend(u_old.get("items", []))

            all_items = try_combine_items_all(all_items)
            kept_items = all_items[:MAX_ITEMS_PER_UNIT]
            overflow_items = all_items[MAX_ITEMS_PER_UNIT:]
            item_inventory = target_player.setdefault("items", [])
            if len(item_inventory) + len(overflow_items) > MAX_ITEM_BENCH:
                continue
            new_unit["items"] = kept_items
            item_inventory.extend(overflow_items)
            backup = []
            for typ, a, b in take3:
                if typ == "board":
                    backup.append(("board", a, b, target_player["board"][a][b]))
                else:
                    backup.append(("bench", a, b, target_player["bench"][a]))
            for typ, a, b in take3:
                if typ == "board":
                    target_player["board"][a][b] = None
                else:
                    target_player["bench"][a] = None
            placed = False
            if board_pos is not None:
                target_player["board"][board_pos[0]][board_pos[1]] = new_unit
                placed = True
            else:
                for slot in range(8):
                    if target_player["bench"][slot] is None:
                        target_player["bench"][slot] = new_unit
                        placed = True
                        break
            if not placed:
                for typ, a, b, orig in backup:
                    if typ == "board":
                        target_player["board"][a][b] = orig
                    else:
                        target_player["bench"][a] = orig
                return
            combined = True
            break
        if not combined:
            break


def evolve_extreme_ai_offline(population=12, games_per_variant=6,
                              generations=None, stop_event=None,
                              phase_thresholds=None):
    """离线进化：可无限运行。每代取最优保存；跨阶段不倒退。
    generations=None 表示无限跑，靠 stop_event 停止。
    阶段1达标升阶段2（打困难），阶段2达标升阶段3（自我对弈+快照池）。
    突破就写盘，中途关掉也不丢成果。"""
    global EXTREME_AI_PARAMS
    if phase_thresholds is None:
        phase_thresholds = {1: 110.0, 2: 130.0}
    st = _TRAINING_STATE
    st.setdefault("phase", 1)
    st.setdefault("phase_label", "普通")
    st.setdefault("rank", "青铜")
    st.setdefault("pool_size", len(EXTREME_AI_OPPONENT_POOL))
    st.setdefault("no_breakthrough_gens", 0)
    prog = _load_training_progress()
    if prog and prog.get("best_params"):
        # 老存档补默认键，保证新特征权重也能被进化调整
        base = dict(EXTREME_AI_PARAMS_DEFAULT)
        base.update({k: v for k, v in prog["best_params"].items()
                     if k in base})
        gen = int(prog.get("generation", 0))
        best_score = float(prog.get("best_score", 0.0))
        best_params = dict(base)
        with _AI_PARAMS_LOCK:
            EXTREME_AI_PARAMS = dict(best_params)
        st["phase"] = int(prog.get("phase", 1))
        st["phase_label"] = prog.get("phase_label", "普通")
        st["no_breakthrough_gens"] = int(prog.get("no_breakthrough_gens", 0))
        EXTREME_AI_SNAPSHOT_POOL[:] = [dict(x) for x in prog.get("snapshot_pool", [])]
        st["best_params"] = dict(best_params)
        st["best_score"] = best_score
        st["pool_size"] = len(EXTREME_AI_SNAPSHOT_POOL) + len(EXTREME_AI_OPPONENT_POOL)
        st["rank"] = _rank_from_pool(st["pool_size"])
        st["log"].append(
            f"恢复上次进度 · 第 {gen} 代 · 阶段{st['phase_label']} · "
            f"最优 {best_score:.1f}")
    else:
        base = dict(EXTREME_AI_PARAMS)
        gen = 0
        best_score = -1.0
        best_params = dict(base)
        st["best_params"] = dict(best_params)
        st["best_score"] = 0.0
    while True:
        if stop_event is not None and stop_event.is_set():
            break
        if generations is not None and gen >= generations:
            break
        gen += 1
        st["generation"] = gen
        stalled = st.get("no_breakthrough_gens", 0)
        big_mode = stalled >= 15
        if big_mode and not st.get("_big_mode_logged"):
            st["_big_mode_logged"] = True
            st["log"].append("停滞超限，自动开启增强变异模式（大变异探索新策略）")
        elif not big_mode and st.get("_big_mode_logged"):
            st["_big_mode_logged"] = False
            st["log"].append("突破成功，恢复标准变异模式")
        intensity = 0.3 if big_mode else 0.15
        # 候选池构成：
        #   1) 精英个体 = 历史最优参数，不重评估、直接继承分数（消除评估方差对停滞计数的污染）
        #   2) 小变异个体（标准扰动，负责对局部极值爬坡）
        #   3) 大变异个体（仅少量字段大幅扰动，负责探索新策略，不会把候选搅成随机垃圾）
        n_big = 4 if big_mode else 2
        candidates = [("elite", dict(best_params))]
        for i in range(max(1, population - 1)):
            candidates.append(
                ("mut", _mutate_params(best_params, intensity=intensity,
                                       big_mutation=(i < n_big))))
        gen_best = -1.0
        gen_best_params = None
        for idx, (kind, cand) in enumerate(candidates):
            if stop_event is not None and stop_event.is_set():
                break
            st["current_variant"] = idx + 1
            st["current_population"] = len(candidates)
            st["current_games_per_variant"] = games_per_variant
            if kind == "elite":
                score = best_score
            else:
                score, _wr = _sim_evaluate_params(cand, games=games_per_variant)
            st["current_score"] = score
            # 前台在打对局时：每评估完一个候选让出CPU片刻，保证游玩流畅
            if _TRAINING_GIVE_WAY:
                time.sleep(0.01)
            if kind != "elite" and score > gen_best:
                gen_best = score
                gen_best_params = cand
        if gen_best_params is None:
            continue
        st["gen_best"] = gen_best
        breakthrough = gen_best > best_score + 1.0
        if breakthrough:
            # 突破复核：候选再评估一轮取平均，仍超阈值才接受（过滤单局运气）
            confirm_score, _ = _sim_evaluate_params(gen_best_params,
                                                    games=games_per_variant)
            final_score = (gen_best + confirm_score) / 2.0
            if final_score > best_score + 1.0:
                gen_best = final_score
                st["gen_best"] = final_score
            else:
                # 复核未达标：单局高分是运气，不采纳。日志讲清楚原因，避免误解
                breakthrough = False
                st["log"].append(
                    f"第{gen}代 · 突破复核未达标：单局{gen_best:.1f} "
                    f"复核均值{confirm_score:.1f}（需>{best_score+1.0:.1f}）· "
                    f"判定为单局运气，不更新全局最优")
        if breakthrough:
            best_score = gen_best
            best_params = dict(gen_best_params)
            with _AI_PARAMS_LOCK:
                EXTREME_AI_PARAMS = dict(best_params)
            save_extreme_params()
            # 自动固化：把新的全局最优AI直接写进豹药宇宙.py源码（带.bak备份），
            # 复制脚本到别的电脑无需带json也能用这个最强AI
            _overwrite_builtin_ai_in_source(best_params)
            st["best_params"] = dict(best_params)
            st["best_score"] = best_score
            st["no_breakthrough_gens"] = 0
            st["_last_shuffle_gens"] = 0
        else:
            st["no_breakthrough_gens"] = st.get("no_breakthrough_gens", 0) + 1
            # 停滞≥30代：打乱对手池，增加对抗多样性
            if (st["no_breakthrough_gens"] >= 30
                    and st["no_breakthrough_gens"] - st.get("_last_shuffle_gens", 0) >= 30
                    and st.get("phase", 1) >= 3):
                _shuffle_opponent_pool()
                st["_last_shuffle_gens"] = st["no_breakthrough_gens"]
        # 阶段看的是当前最优分，和是否突破无关，避免一步跳穿阈值卡在旧阶段
        prev_phase = st.get("phase", 1)
        _advance_phase_if_ready(best_score, phase_thresholds)
        # 进入阶段3即录入首个快照；此后阶段3内每次突破也录入
        if (breakthrough or prev_phase < 3) and st.get("phase", 1) >= 3:
            _record_snapshot(best_params)
        # 按本代最强分数给AI分档存档（同段位只保留更高分）
        g_rank = _ai_rank_from_score(gen_best)
        if _save_ranked_ai(g_rank, dict(gen_best_params), gen_best):
            # 新段位/新高分AI诞生：自动进入对手池（上限30淘汰最旧）
            _record_snapshot(gen_best_params)
        b_rank = _ai_rank_from_score(best_score)
        # 日志把【本代最优】放在最前，避免被界面截断看不到当代成绩
        log = (f"第 {gen} 代 · 本代 {gen_best:.1f}({g_rank}AI) · "
               f"全局最优 {best_score:.1f}({b_rank}AI) · "
               f"训练段位 {st.get('rank', '青铜')} · 阶段{st.get('phase', 1)}")
        st["log"].append(log)
        if len(st["log"]) > 200:
            del st["log"][:-200]
        # 写盘防抖：每5代保存一次进度，降低磁盘IO卡顿（停止训练时由worker兜底强制保存）
        if gen % 5 == 0:
            _save_training_progress()
    return best_params


def _training_worker(stop_event):
    """训练线程入口，可被 stop_event 打断。"""
    _TRAINING_STATE["running"] = True
    try:
        evolve_extreme_ai_offline(
            population=12,
            games_per_variant=6,
            stop_event=stop_event,
        )
    except Exception as e:
        log_once("training_worker", e)
    finally:
        _TRAINING_STATE["running"] = False
        _save_training_progress()


def _check_training_worker():
    """检测训练线程是否真的还活着。
    界面显示“训练中”但线程已死（后台被系统挂起/异常退出）时，
    自动把状态重置为可重新开始，避免永远卡在“训练中”没法点开始。"""
    if not _TRAINING_STATE.get("running", False):
        return
    wt = _TRAINING_STATE.get("worker_thread")
    if wt is None:
        return
    if not wt.is_alive():
        _TRAINING_STATE["running"] = False
        _TRAINING_STATE["log"].append(
            "训练线程已中断（后台挂起/异常退出），可重新点开始继续")


class BattleUnit:
    def __init__(self, champion_data, start_x, start_y, side, buffs=None, size=48):
        self.base = safe_unit(copy.deepcopy(champion_data))
        self.side = side
        self.owner_player = None
        self.rune_set_gold_done = False
        self.start_x = start_x
        self.start_y = start_y
        self.x = start_x
        self.y = start_y
        self.size = size
        self.state = "idle"
        self.anim_timer = 0
        self.attack_target = None
        self.flash_timer = 0
        self.attack_cd_remain = 0.0
        self.alive = True
        self.atk_buff = 1.0
        self.sp_buff = 1.0
        self.crit = 0.0
        self.atk_speed_mult = 1.0
        self.move_speed = MOVE_SPEED
        self.extra_mana_per_attack = 0
        self.attack_range = self.base.get("attack_range", RANGE_WARRIOR)
        self.role = self.base.get("role", "warrior")
        self.is_ranged = self.role in ("archer", "mage")
        self.is_summon = (self.base.get("name") in ("Tuanzi", "AncientTree"))
        self.skill_type = self.base.get("skill_type", "damage")
        self.muted = False
        self.shield = 0
        item_stats = get_unit_item_stats(self.base)
        self.artifacts = [it.get("artifact_name") for it in self.base.get("items", [])
                          if it.get("is_artifact") and it.get("artifact_name")]
        self.artifact_flags = set(self.artifacts)
        self.artifact_once = set()
        self.artifact_cd = {}
        self.armor = self.base.get("armor", 0) + item_stats.get("armor", 0)
        self.mr = self.base.get("mr", 0) + item_stats.get("mr", 0)
        cost = self.base.get("cost", 1)
        star = self.base.get("star", 1)
        self.mana_regen = get_mana_regen(cost, star)
        self.base_mana_regen_flat = BASE_MANA_REGEN_FLAT
        self.base_mana_regen_percent = BASE_MANA_REGEN_PERCENT
        self.skill_cd_total = get_skill_cd(cost, star)
        self.skill_cd_remain = 0.0
        self.cast_count = 0
        self.damage_dealt = 0
        self.damage_taken = 0
        self.kills = 0
        self.heal_done = 0
        self.true_dmg_bonus = 0.0
        if buffs:
            self.atk_buff *= buffs.get("atk_mult", 1.0)
            self.sp_buff *= buffs.get("sp_mult", 1.0)
            self.crit = buffs.get("crit", 0.0)
            self.atk_speed_mult = buffs.get("atk_speed_mult", 1.0)
            self.extra_mana_per_attack = buffs.get("extra_mana_per_attack", 0)
            self.base["hp"] = int(self.base["hp"] * buffs.get("hp_mult", 1.0))
            self.armor += buffs.get("extra_armor", 0)
            cb = buffs.get("class_buffs", {}).get(self.role, {})
            if cb:
                self.atk_buff *= cb.get("atk_mult", 1.0)
                self.sp_buff *= cb.get("sp_mult", 1.0)
                self.atk_speed_mult *= cb.get("atk_speed_mult", 1.0)
                self.base["hp"] = int(self.base["hp"] * cb.get("hp_mult", 1.0))
                self.true_dmg_bonus = cb.get("true_dmg_bonus", 0.0)
        self.base["ad"] = int(self.base["ad"] + item_stats.get("ad", 0))
        self.base["hp"] = int(self.base["hp"] + item_stats.get("hp", 0))
        if item_stats.get("sp", 0):
            self.sp_buff *= (1.0 + item_stats.get("sp", 0) / 100.0)
        self.atk_speed_mult += item_stats.get("atk_speed", 0)
        self.crit += item_stats.get("crit", 0)
        self.base["max_mana"] = max(5, self.base["max_mana"] + item_stats.get("mana", 0))
        self.attack_range += item_stats.get("range", 0)
        if "疾风靴" in self.artifact_flags:
            self.atk_speed_mult *= 1.45
            self.move_speed *= 1.45
            self.crit += 0.35
        if "豹骨甲" in self.artifact_flags:
            self.base["hp"] = int(self.base["hp"] * 1.30)
            self.armor += 35
            self.mr += 35
        if "诛仙弓" in self.artifact_flags:
            self.attack_range += 90
            self.atk_buff *= 1.10
        if "浑天仪" in self.artifact_flags:
            self.atk_buff *= 1.10
            self.sp_buff *= 1.10
            self.atk_speed_mult *= 1.10
        self.current_hp = self.base["hp"]
        self.current_mana = 0
        self.skill_flash_timer = 0.0
        self.summon_flash_timer = 0.6 if self.is_summon else 0.0
        self.poison_dmg = 0
        self.poison_remain = 0.0
        self.poison_tick = 0.0
        self.damage_reduction = 0.0
        self.damage_reduction_timer = 0.0
        self.burst_shield_dmg = 0
        self._rune_gold_timer = 1.0

    def take_damage(self, dmg, source=None, dmg_type="physical"):
        if not self.alive:
            return
        true_extra = 0
        if source is not None and hasattr(source, "true_dmg_bonus"):
            true_extra = int(dmg * source.true_dmg_bonus)
        if dmg_type == "true":
            reduction = 0.0
        elif dmg_type == "magic":
            reduction = self.mr / (self.mr + 100) if self.mr >= 0 else 0
        else:
            reduction = self.armor / (self.armor + 100) if self.armor >= 0 else 0
        final = max(1, int(dmg * (1 - reduction))) + true_extra
        if self.damage_reduction != 0:
            final = max(1, int(final * (1 - self.damage_reduction)))
        absorbed = 0
        shield_before = self.shield
        if self.shield > 0:
            absorbed = min(self.shield, final)
            self.shield -= absorbed
            final -= absorbed
        if shield_before > 0 and self.shield <= 0 and self.burst_shield_dmg > 0:
            self._trigger_burst_shield()
        actual = min(final, max(0, self.current_hp))
        self.current_hp -= final
        total_incoming = absorbed + actual
        self.damage_taken += total_incoming
        if source is not None and source is not self:
            source.damage_dealt += total_incoming
            if self.current_hp <= 0:
                source.kills += 1
        if self.alive and total_incoming > 0:
            if "玄冰镜" in self.artifact_flags and source is not None and source is not self:
                source.take_damage(max(1, int(total_incoming * 0.18)), source=self, dmg_type="magic")
                self.shield += int(self.base["hp"] * 0.08)
            if "豹骨甲" in self.artifact_flags:
                nearby = [a for a in getattr(self, "_artifact_allies", []) if a is not self and a.alive]
                for a in nearby[:2]:
                    if (a.x-self.x)**2 + (a.y-self.y)**2 <= 150**2:
                        share = min(int(total_incoming * 0.12), a.current_hp)
                        a.current_hp -= share
                        break
            mana_gain = MANA_PER_HIT_TAKEN_FLAT + self.base["max_mana"] * MANA_PER_HIT_TAKEN_PERCENT
            self.add_mana(mana_gain)
        self.flash_timer = 0.25
        if self.current_hp <= 0:
            self.current_hp = 0
            self.alive = False
            self.state = "dead"
            if not self.muted:
                play_sfx("death")

    def _trigger_burst_shield(self):
        dmg = self.burst_shield_dmg
        self.burst_shield_dmg = 0
        enemies = getattr(self, "_burst_enemies", None)
        effects = getattr(self, "_burst_effects", None)
        if dmg <= 0 or not enemies:
            return
        r2 = 180 ** 2
        for e in enemies:
            if e.alive and (e.x - self.x) ** 2 + (e.y - self.y) ** 2 < r2:
                e.take_damage(dmg, source=self, dmg_type="magic")
                if effects is not None:
                    effects.append({"type": "damage_pop", "x": e.x, "y": e.y,
                                    "text": f"{dmg}", "life": 1.4,
                                    "max_life": 1.4, "kind": "skill"})
        if effects is not None:
            effects.append({"type": "cast_pulse", "x": self.x, "y": self.y,
                            "r0": 10, "r1": 180, "life": 0.4, "max_life": 0.4,
                            "color": (255, 180, 80)})

    def apply_poison(self, dmg_per_sec, duration):
        if not self.alive:
            return
        self.poison_dmg = max(self.poison_dmg, int(dmg_per_sec))
        self.poison_remain = max(self.poison_remain, float(duration))
        self.poison_tick = 1.0

    def add_mana(self, amount):

        self.current_mana = min(self.base["max_mana"], self.current_mana + amount)

    def is_ready_cast(self):
        return (self.alive and self.current_mana >= self.base["max_mana"]
                and self.skill_cd_remain <= 0)

    def _pick_nearest(self, enemies):
        best, best_d2 = None, float("inf")
        for e in enemies:
            if not e.alive:
                continue
            d2 = (e.x - self.x) ** 2 + (e.y - self.y) ** 2
            if d2 < best_d2:
                best_d2, best = d2, e
        return best

    def _pick_skill_target(self, enemies):
        valid = [e for e in enemies if e.alive]
        if not valid:
            return None
        traits = self.base.get("traits", [])
        if "LeopardKind" in traits:
            return min(valid, key=lambda e: e.current_hp)
        if "PotionClan" in traits:
            return max(valid, key=lambda e: e.base["ad"] * e.atk_buff)
        return self._pick_nearest(valid)

    def cast_skill(self, allies, enemies, effect_list, screen_w, screen_h):
        owner = self.owner_player
        if self.side == "enemy" and getattr(owner, "_skill_plunder_block", False):
            return
        star = self.base["star"]
        star_scale = SKILL_DMG_STAR_SCALE.get(star, SKILL_DMG_STAR_SCALE[4])
        sp_val = int(self.base["sp_base_dmg"] * self.base["sp_multiplier"]
                     * star_scale * self.sp_buff)
        name = self.base["name"]
        if name == "AncientTree":
            # 远古树灵专属技能：全屏践踏——对全体敌人造成伤害并短暂压制其攻击
            dmg = sp_val
            dmg_type = self.base.get("skill_dmg_type") or "physical"
            for e in enemies:
                if e.alive:
                    e.take_damage(dmg, source=self, dmg_type=dmg_type)
                    e.attack_cd_remain = max(e.attack_cd_remain, 1.2)
                    effect_list.append({"type": "damage_pop", "x": e.x, "y": e.y,
                                        "text": f"{dmg}", "life": 1.5,
                                        "max_life": 1.5, "kind": "skill"})
            effect_list.append({"type": "screen_flash", "life": 0.35,
                                "max_life": 0.35, "color": (120, 200, 80)})
            effect_list.append({"type": "ultimate_cross", "x": self.x,
                                "y": self.y, "life": 0.6, "max_life": 0.6,
                                "color": (120, 200, 80)})
            self.current_mana = 0
            self.skill_cd_remain = self.skill_cd_total
            self.state = "skill"
            self.anim_timer = 0.5
            return
        if "火莲印" in self.artifact_flags:
            target0 = self._pick_skill_target(enemies)
            if target0 is not None:
                target0.apply_poison(max(1, int(sp_val * 0.12)), 5.0)
        if "噬魂幡" in self.artifact_flags:
            low_targets = [e for e in enemies if e.alive and e.current_hp < e.base["hp"] * 0.30]
            for e in low_targets:
                e.take_damage(max(1, int(sp_val * 0.20)), source=self, dmg_type="true")
        if not self.muted:
            play_sfx("skill")
        self.skill_flash_timer = 0.6
        self.cast_count += 1
        is_5cost = self.base.get("cost", 1) == 5
        is_3star_5cost = is_5cost and star >= 3
        if is_3star_5cost:
            trigger_three_star_5cost(self, allies, enemies, effect_list,
                                     screen_w, screen_h)
        ring_color = (255, 220, 80)
        if name == "BaoLan":
            ring_color = (220, 80, 220)
        elif name == "PotionCreator":
            ring_color = (255, 100, 100)
        elif name == "GodFrog":
            ring_color = (80, 240, 120)
        elif name == "GuangTouQiang":
            ring_color = BEAR_COLOR
        elif name == "ArcaneLord":
            ring_color = RUNE_COLOR
        elif name == "Tuanzi":
            ring_color = (180, 230, 255)
        elif name == "AncientTree":
            ring_color = (120, 200, 80)
        elif self.skill_type == "shield":
            ring_color = SHIELD_COLOR
        if is_3star_5cost:
            max_r = int(max(screen_w, screen_h) * 1.1)
            effect_list.append({"type": "screen_flash",
                                "life": 0.5, "max_life": 0.5,
                                "color": ring_color})
        else:
            max_r = 100 + 40 * star
        effect_list.append({"type": "cast_pulse", "x": self.x, "y": self.y,
                            "r0": 10, "r1": 70 + star * 25,
                            "life": 0.4, "max_life": 0.4, "color": ring_color})
        for i in range(3):
            effect_list.append({"type": "shockwave",
                                "x": self.x, "y": self.y,
                                "r1": max_r, "life": 0.9, "max_life": 0.9,
                                "delay": i * 0.10, "color": ring_color})
        skill_name = skill_cn(self.base.get("skill_desc", name))[:12]
        effect_list.append({"type": "skill_name",
                            "x": self.x, "y": self.y - 60,
                            "text": skill_name,
                            "life": 1.2, "max_life": 1.2,
                            "color": ring_color, "is_ult": is_3star_5cost})
        
        if name in ("ThunderHelper", "ThunderLicker", "ThunderComment",
            "ThunderPotato", "ThunderGoddess", "ThunderPatch"):
            _thunder_skill(self, allies, enemies, effect_list)
            return

        if self.skill_type == "bulwark":
            shield_val = int(sp_val * 0.8)
            self.shield += shield_val
            self.damage_reduction = min(0.6, 0.15 + 0.05 * star)
            self.damage_reduction_timer = 3.0 + 0.5 * star
            effect_list.append({"type": "damage_pop", "x": self.x, "y": self.y,
                                "text": f"+{shield_val}", "life": 1.4,
                                "max_life": 1.4, "kind": "shield"})
            splash_r2 = (140 + 20 * star) ** 2
            splash_dmg = int(sp_val * 0.5)
            dmg_type = self.base.get("skill_dmg_type") or "physical"
            for e in enemies:
                if e.alive and (e.x - self.x) ** 2 + (e.y - self.y) ** 2 < splash_r2:
                    e.take_damage(splash_dmg, source=self, dmg_type=dmg_type)
                    effect_list.append({"type": "damage_pop", "x": e.x, "y": e.y,
                                        "text": f"{splash_dmg}", "life": 1.4,
                                        "max_life": 1.4, "kind": "skill"})
        elif self.skill_type == "burst_shield":
            shield_val = int(sp_val * 0.9)
            self.shield += shield_val
            self.burst_shield_dmg = int(sp_val * 0.8)
            self._burst_enemies = enemies
            self._burst_effects = effect_list
            effect_list.append({"type": "damage_pop", "x": self.x, "y": self.y,
                                "text": f"+{shield_val}", "life": 1.4,
                                "max_life": 1.4, "kind": "shield"})
        elif self.skill_type == "drain":
            heal_amount = int(sp_val * 0.7)
            before = self.current_hp
            self.current_hp = min(self.base["hp"], self.current_hp + heal_amount)
            healed = self.current_hp - before
            self.heal_done += healed
            effect_list.append({"type": "damage_pop", "x": self.x, "y": self.y,
                                "text": f"+{healed}", "life": 1.4,
                                "max_life": 1.4, "kind": "heal"})
            splash_r2 = (140 + 20 * star) ** 2
            splash_dmg = int(sp_val * 0.5)
            dmg_type = self.base.get("skill_dmg_type") or "physical"
            for e in enemies:
                if e.alive and (e.x - self.x) ** 2 + (e.y - self.y) ** 2 < splash_r2:
                    e.take_damage(splash_dmg, source=self, dmg_type=dmg_type)
                    effect_list.append({"type": "damage_pop", "x": e.x, "y": e.y,
                                        "text": f"{splash_dmg}", "life": 1.4,
                                        "max_life": 1.4, "kind": "skill"})
        elif self.skill_type == "shield":
            targets = [self] + [a for a in allies
                                 if a.alive and a is not self
                                 and (a.x - self.x) ** 2 + (a.y - self.y) ** 2 < (150 + 20 * star) ** 2]
            for a in targets:
                shield_val = int(sp_val * 0.6)
                a.shield += shield_val
                effect_list.append({"type": "damage_pop", "x": a.x, "y": a.y,
                                    "text": f"+{shield_val}", "life": 1.4,
                                    "max_life": 1.4, "kind": "shield"})
            splash_r2 = (150 + 20 * star) ** 2
            splash_dmg = int(sp_val * 0.35)
            splash_type = self.base.get("skill_dmg_type") or "physical"
            for e in enemies:
                if e.alive and (e.x - self.x) ** 2 + (e.y - self.y) ** 2 < splash_r2:
                    e.take_damage(splash_dmg, source=self, dmg_type=splash_type)
                    effect_list.append({"type": "damage_pop", "x": e.x, "y": e.y,
                                        "text": f"{splash_dmg}", "life": 1.4,
                                        "max_life": 1.4, "kind": "skill"})
        elif self.skill_type == "heal":
            heal_amount = int(280 * star_scale * self.sp_buff)
            total_heal = 0
            for a in allies:
                if a.alive:
                    before = a.current_hp
                    if star < 3:
                        a.current_hp = min(a.base["hp"], a.current_hp + heal_amount)
                    else:
                        a.current_hp = a.base["hp"]
                    healed = a.current_hp - before
                    self.heal_done += healed
                    total_heal += healed
                    effect_list.append({"type": "damage_pop", "x": a.x, "y": a.y,
                                        "text": f"+{heal_amount}", "life": 1.4,
                                        "max_life": 1.4, "kind": "heal"})
            if total_heal > 0:
                holy_dmg = int(total_heal * 0.5)
                for e in enemies:
                    if e.alive:
                        e.take_damage(holy_dmg, source=self, dmg_type="magic")
                        effect_list.append({"type": "damage_pop", "x": e.x, "y": e.y,
                                            "text": f"{holy_dmg}", "life": 1.4,
                                            "max_life": 1.4, "kind": "skill"})
        elif name in ("BaoLan", "PotionCreator", "SuperLogger",
                      "LoggerStrong", "GuangTouQiang", "ArcaneLord"):
            targets = [e for e in enemies if e.alive]
            if star < 3:
                max_targets = 6 if name == "GuangTouQiang" else 5
                targets = targets[:max_targets]
            for e in targets:
                dmg_type = self.base.get("skill_dmg_type") or (
                    "magic" if name in ("BaoLan", "PotionCreator", "ArcaneLord")
                    else "physical")
                e.take_damage(sp_val, source=self, dmg_type=dmg_type)
                effect_list.append({"type": "damage_pop", "x": e.x, "y": e.y,
                                    "text": f"{sp_val}", "life": 1.5,
                                    "max_life": 1.5, "kind": "skill"})
        else:
            target = self._pick_skill_target(enemies)
            if target:
                dmg_type = self.base.get("skill_dmg_type") or (
                    "magic" if self.role == "mage" else "physical")
                target.take_damage(sp_val, source=self, dmg_type=dmg_type)
                effect_list.append({"type": "damage_pop", "x": target.x, "y": target.y,
                                    "text": f"{sp_val}", "life": 1.4,
                                    "max_life": 1.4, "kind": "skill"})
                if name == "PotionPouch":
                    target.apply_poison(int(sp_val * 0.15), 3.0)
                elif name == "LeopardPotion":
                    target.apply_poison(int(sp_val * 0.20), 4.0)
                if self.role == "mage":

                    splash_dmg = int(sp_val * 0.4)
                    splash_r2 = 120 ** 2
                    for e in enemies:
                        if e.alive and e is not target and \
                                (e.x - target.x) ** 2 + (e.y - target.y) ** 2 < splash_r2:
                            e.take_damage(splash_dmg, source=self, dmg_type="magic")
                            effect_list.append({"type": "damage_pop", "x": e.x, "y": e.y,
                                                "text": f"{splash_dmg}", "life": 1.4,
                                                "max_life": 1.4, "kind": "skill"})
        self.current_mana = 0
        self.skill_cd_remain = self.skill_cd_total
        self.state = "skill"
        self.anim_timer = 0.5

    def update(self, dt, allies, enemies, effect_list, screen_w, screen_h):
        if self.owner_player is not None and has_three_rune_set(self.base) and self.alive:
            self._rune_gold_timer = getattr(self, "_rune_gold_timer", 0.0) - dt
            if self._rune_gold_timer <= 0:
                self.owner_player["gold"] += 4
                self._rune_gold_timer = 1.0
        if self.flash_timer > 0:
            self.flash_timer -= dt
        if self.skill_flash_timer > 0:
            self.skill_flash_timer -= dt
        if self.summon_flash_timer > 0:
            self.summon_flash_timer -= dt
        if self.skill_cd_remain > 0:
            self.skill_cd_remain -= dt
        if self.damage_reduction_timer > 0:
            self.damage_reduction_timer -= dt
            if self.damage_reduction_timer <= 0:
                self.damage_reduction = 0.0
                self.damage_reduction_timer = 0.0
        if not self.alive:
            return
        if self.poison_remain > 0:
            self.poison_tick -= dt
            self.poison_remain -= dt
            if self.poison_tick <= 0:
                self.poison_tick += 1.0
                if self.poison_dmg > 0:
                    self.take_damage(self.poison_dmg, source=None, dmg_type="magic")
                if not self.alive:
                    return
            if self.poison_remain <= 0:
                self.poison_dmg = 0
                self.poison_remain = 0.0
                self.poison_tick = 0.0
        total_regen = (self.mana_regen

                       + self.base_mana_regen_flat
                       + self.base["max_mana"] * self.base_mana_regen_percent)
        if total_regen > 0:
            self.add_mana(total_regen * dt)
        if self.is_ready_cast():
            self.cast_skill(allies, enemies, effect_list, screen_w, screen_h)
            return
        if self.state == "skill":
            self.anim_timer -= dt
            if self.anim_timer <= 0:
                self.state = "idle"
            return
        self.attack_cd_remain -= dt
        nearest = self._pick_nearest(enemies)
        if nearest is None:
            self.state = "idle"
            return
        dx = nearest.x - self.x
        dy = nearest.y - self.y
        dist = (dx * dx + dy * dy) ** 0.5
        atk_range = self.attack_range + (self.size + nearest.size) / 2
        if dist > atk_range:
            self.state = "moving"
            self.attack_target = nearest
            if dist > MIN_MOVE_DIST:
                self.x += dx / dist * self.move_speed * dt
                self.y += dy / dist * self.move_speed * dt
        else:
            # 进入攻击范围后站桩输出：远程单位不再后撤（修复“后排往后走”）
            self.state = "attack"
            self.attack_target = nearest
            if self.attack_cd_remain <= 0:
                dmg = int(self.base["ad"] * self.atk_buff)
                crit = random.random() < self.crit
                if crit:
                    dmg = int(dmg * 1.8)
                nearest.take_damage(dmg, source=self, dmg_type="physical")
                self.add_mana(self.base["mana_per_attack"] + self.extra_mana_per_attack)
                if not self.muted:
                    play_sfx("hit")
                effect_list.append({"type": "attack_line",
                                    "p1": (int(self.x), int(self.y)),
                                    "p2": (int(nearest.x), int(nearest.y)),
                                    "life": 0.15, "max_life": 0.15,
                                    "crit": crit, "ranged": self.is_ranged})
                kind = "crit" if crit else "atk"
                effect_list.append({"type": "damage_pop",
                                    "x": nearest.x, "y": nearest.y,
                                    "text": f"{dmg}", "life": 1.2,
                                    "max_life": 1.2, "kind": kind})
                self.attack_cd_remain = self.base["attack_cooldown"] / self.atk_speed_mult
        sep_x = sep_y = 0.0
        min_d = self.size * SEP_MIN_DIST_RATIO
        for other in allies:
            if other is self or not other.alive:
                continue
            odx = self.x - other.x
            ody = self.y - other.y
            od2 = odx * odx + ody * ody
            if od2 > 0.01:
                od = od2 ** 0.5
                if od < min_d:
                    force = (min_d - od) / min_d
                    sep_x += odx / od * force
                    sep_y += ody / od * force
        self.x += sep_x * SEP_FORCE * dt
        self.y += sep_y * SEP_FORCE * dt
        half = self.size / 2
        self.x = max(half, min(screen_w - half, self.x))
        self.y = max(half, min(screen_h - half, self.y))


class BattleInstance:
    def __init__(self, attacker, defender, index=0):
        self.attacker = attacker
        self.defender = defender
        self.index = index
        self.allies = []
        self.enemies = []
        self.effects = []
        self.finished = False
        self.winner = None
        self.is_player_battle = False
        self.is_monster_battle = False
        self.is_watched = False
        self.is_mirror_battle = False
        self.mirror_owner = None

    def spawn(self, screen_w, screen_h):
        ally_buffs = apply_trait_buffs(self.attacker)
        merge_hex_into_buffs(ally_buffs, self.attacker)
        enemy_buffs = apply_trait_buffs(self.defender)
        merge_hex_into_buffs(enemy_buffs, self.defender)
        if self.attacker.get("_active_plunder") == "skill":
            self.defender["_skill_plunder_block"] = True
        if self.defender.get("_active_plunder") == "skill":
            self.attacker["_skill_plunder_block"] = True
        enemy_buffs["atk_mult"] *= ally_buffs.get("enemy_atk_mult", 1.0)
        ally_buffs["atk_mult"] *= enemy_buffs.get("enemy_atk_mult", 1.0)
        self.allies = self._spawn_units(self.attacker, "ally", screen_w, screen_h, ally_buffs)
        self.enemies = self._spawn_units(self.defender, "enemy", screen_w, screen_h, enemy_buffs)
        self._activate_battle_artifacts(self.allies, self.enemies)
        self._activate_battle_artifacts(self.enemies, self.allies)
        self._spawn_treasure_capture(screen_w, screen_h)
        self._spawn_bear_ridge_summons(screen_w, screen_h, ally_buffs, enemy_buffs)
        self._apply_lumber_mechanic(screen_w, screen_h, ally_buffs, enemy_buffs)
        for u in self.allies:
            u._artifact_allies = self.allies
            u._artifact_enemies = self.enemies
        for u in self.enemies:
            u._artifact_allies = self.enemies
            u._artifact_enemies = self.allies
        self.sync_mute()
        self._spawn_trait_activation_fx(screen_w, screen_h)

    def _activate_battle_artifacts(self, units, enemies):
        # Battle-start artifact effects.
        for u in units:
            if "九天雷符" in u.artifact_flags:
                for e in enemies:
                    if e.alive:
                        e.muted = True
                        e.damage_reduction = max(e.damage_reduction, -0.10)
                u.artifact_once.add("thunder_start")
            if "浑天仪" in u.artifact_flags:
                for a in units:
                    a.atk_buff *= 1.10
                    a.sp_buff *= 1.10
                    a.atk_speed_mult *= 1.10
            if "疾风靴" in u.artifact_flags:
                u.crit += 0.65
                u.artifact_once.add("wind_first")
            if "辟邪玉" in u.artifact_flags:
                u.artifact_once.add("anti_cc")
        if any("玲珑塔" in u.artifact_flags for u in units):
            for u in units:
                u._linglong_timer = 4.0

    def _artifact_tick(self, dt):
        for u in self.allies + self.enemies:
            if not u.alive:
                continue
            if "龙神丹" in u.artifact_flags and u.current_hp < u.base["hp"] * 0.5:
                if "dragon_heal" not in u.artifact_once:
                    u.current_hp = min(u.base["hp"], u.current_hp + int(u.base["hp"] * 0.35))
                    u.damage_reduction = max(u.damage_reduction, 0.50)
                    u.damage_reduction_timer = 1.2
                    u.artifact_once.add("dragon_heal")
            if "聚宝盆" in u.artifact_flags and u.kills > getattr(u, "_treasure_bowl_kills", 0):
                diff = u.kills - getattr(u, "_treasure_bowl_kills", 0)
                u._treasure_bowl_kills = u.kills
                if u.owner_player is not None:
                    u.owner_player["gold"] += diff
            if "玲珑塔" in u.artifact_flags:
                u._linglong_timer = getattr(u, "_linglong_timer", 4.0) - dt
                if u._linglong_timer <= 0:
                    allies = self.allies if u.side == "ally" else self.enemies
                    alive = [a for a in allies if a.alive]
                    if alive:
                        t = min(alive, key=lambda a: a.current_hp / max(1, a.base["hp"]))
                        t.shield += int(t.base["hp"] * 0.15)
                    u._linglong_timer = 4.0

    def _spawn_trait_activation_fx(self, screen_w, screen_h):
        for side, player, y_ratio in (
            ("ally", self.attacker, 0.72),
            ("enemy", self.defender, 0.28),
        ):
            if player is None:
                continue
            tc = count_traits(player)
            active = []
            for trait, count in tc.items():
                thresholds = TRAIT_DATA.get(trait, [])
                tier = sum(1 for t in thresholds if count >= t)
                if tier > 0:
                    active.append((trait, tier))
            if not active:
                continue
            priority = {"BearRidge": 0, "RuneLand": 1, "Treasure": 2}
            active.sort(key=lambda x: (priority.get(x[0], 9), -x[1]))
            active = active[:4]
            for i, (trait, tier) in enumerate(active):
                color = TRAIT_COLOR.get(trait, GOLD_COLOR)
                x = screen_w * (0.15 + i * (0.70 / max(1, len(active))))
                self.effects.append({
                    "type": "trait_activate",
                    "trait_key": trait,
                    "trait_name": trait_cn(trait),
                    "tier": tier,
                    "x": x,
                    "y": screen_h * y_ratio,
                    "life": 2.0,
                    "max_life": 2.0,
                    "color": color,
                    "side": side,
                })
        if self.is_watched and any(
                e.get("type") == "trait_activate" for e in self.effects):
            play_sfx("hex")

    def sync_mute(self):
        muted = not self.is_watched
        for u in self.allies + self.enemies:
            u.muted = muted

    def _spawn_treasure_capture(self, screen_w, screen_h):
        for owner, hunters, victims in (
            (self.attacker, self.allies, self.enemies),
            (self.defender, self.enemies, self.allies),
        ):
            tc = count_traits(owner)
            if tc.get("Treasure", 0) < 8 or not hunters or not victims:
                continue
            hunters_exist = [u for u in hunters if "Treasure" in u.base.get("traits", [])]
            if not hunters_exist:
                continue
            captured = 0
            for target in list(victims):
                if target.alive:
                    target.current_hp = 0
                    target.alive = False
                    target.state = "dead"
                    captured += 1
                    self.effects.append({"type": "capture", "x": target.x,
                                         "y": target.y, "text": "捕获",
                                         "life": 1.0, "max_life": 1.0,
                                         "color": TREASURE_COLOR})
            if captured:
                owner["_bounty_capture_shards"] = owner.get("_bounty_capture_shards", 0) + captured * 10
                if owner is self.attacker:
                    self._treasure_captured_attacker = captured
                if owner is self.defender:
                    self._treasure_captured_defender = captured

    def _spawn_bear_ridge_summons(self, screen_w, screen_h, ally_buffs, enemy_buffs):
        star_a = get_bear_ridge_summon_star(self.attacker)
        if star_a > 0:
            tuanzi_data = make_unit_with_star("Tuanzi", star_a)
            if tuanzi_data:
                used = [(u.x, u.y) for u in self.allies]
                tx, ty = self._find_free_position(
                    screen_w * 0.5, screen_h * 0.60, used,
                    screen_w, screen_h, self.allies)
                tu = BattleUnit(tuanzi_data, tx, ty, "ally", ally_buffs,
                                size=self.allies[0].size if self.allies else 48)
                tu.is_summon = True
                tu.summon_flash_timer = 1.0
                self.allies.append(tu)
        star_d = get_bear_ridge_summon_star(self.defender)
        if star_d > 0:
            tuanzi_data = make_unit_with_star("Tuanzi", star_d)
            if tuanzi_data:
                used = [(u.x, u.y) for u in self.enemies]
                tx, ty = self._find_free_position(
                    screen_w * 0.5, screen_h * 0.40, used,
                    screen_w, screen_h, self.enemies)
                tu = BattleUnit(tuanzi_data, tx, ty, "enemy", enemy_buffs,
                                size=self.enemies[0].size if self.enemies else 48)
                tu.is_summon = True
                tu.summon_flash_timer = 1.0
                self.enemies.append(tu)

    def _apply_lumber_mechanic(self, screen_w, screen_h, ally_buffs, enemy_buffs):
        """伐木羁绊：选首领→吸收最近2个伐木弈子90%基础生命→按档位加攻法→(8)召唤树灵。"""
        tier_a = get_lumber_tier(self.attacker)
        if tier_a > 0:
            self._do_lumber_side(self.allies, "ally", screen_w, screen_h, ally_buffs, tier_a)
        tier_d = get_lumber_tier(self.defender)
        if tier_d > 0:
            self._do_lumber_side(self.enemies, "enemy", screen_w, screen_h, enemy_buffs, tier_d)

    def _do_lumber_side(self, units, side, screen_w, screen_h, buffs, tier):
        lumber_units = [u for u in units
                        if "Lumber" in u.base.get("traits", []) and u.alive]
        if not lumber_units:
            return
        # 首领选择：巨斧选择器手动标记优先；存在手动标记则完全关闭自动选首领逻辑。
        manual = [u for u in lumber_units if u.base.get("is_lumber_chief")]
        if manual:
            leader = manual[0]
        else:
            # 无手动标记：自动选场上最高费 → 最高星伐木弈子
            lumber_units.sort(key=lambda u: (-u.base.get("cost", 1),
                                             -u.base.get("star", 1)))
            leader = lumber_units[0]
        if tier >= 3:
            # 8伐木（棱彩终极羁绊）：不吞噬任何己方棋子；全员+55%，首领双倍；召唤远古树灵
            for u in lumber_units:
                mult = 2.10 if u is leader else 1.55
                u.sp_buff *= mult
                u.atk_buff *= mult
            self._spawn_lumber_tree(units, leader, lumber_units, side,
                                    screen_w, screen_h, buffs)
            return
        # 3/5伐木：首领吸收距离自己最近2个伐木弈子90%基础生命（战斗内临时生命，被吸收棋子不死亡）
        others = [u for u in lumber_units if u is not leader]
        others.sort(key=lambda u: (u.x - leader.x) ** 2 + (u.y - leader.y) ** 2)
        absorbed = others[:2]
        bonus_hp = sum(int(u.base["hp"] * 0.90) for u in absorbed)
        if bonus_hp > 0:
            leader.base["hp"] += bonus_hp
            leader.current_hp = leader.base["hp"]
            leader._lumber_hp_bonus = bonus_hp
        if tier == 1:
            # 3伐木：仅给首领施加战斗内临时属性 +60法强 / +60%物理加成
            leader.sp_buff *= 1.60
            leader.atk_buff *= 1.60
        else:
            # 5伐木：全部伐木弈子 +55法强/+55%物攻，首领获得该数值双倍加成(+110%)
            for u in lumber_units:
                mult = 2.10 if u is leader else 1.55
                u.sp_buff *= mult
                u.atk_buff *= mult

    def _spawn_lumber_tree(self, units, leader, lumber_units, side,
                           screen_w, screen_h, buffs):
        """8伐木：召唤远古树灵，继承全部伐木弈子75%生命/攻击，继承首领全部装备。"""
        tree_data = make_unit_with_star("AncientTree", 1)
        if not tree_data:
            return
        total_hp = sum(u.base["hp"] for u in lumber_units)
        total_ad = sum(u.base["ad"] for u in lumber_units)
        tree_data["hp"] = max(1, int(total_hp * 0.75))
        tree_data["ad"] = max(1, int(total_ad * 0.75))
        tree_data["items"] = copy.deepcopy(leader.base.get("items", []))
        used = [(u.x, u.y) for u in units]
        cy = screen_h * 0.60 if side == "ally" else screen_h * 0.40
        tx, ty = self._find_free_position(
            screen_w * 0.5, cy, used, screen_w, screen_h, units)
        tree = BattleUnit(tree_data, tx, ty, side, buffs,
                          size=units[0].size if units else 48)
        tree.is_summon = True
        tree.summon_flash_timer = 1.0
        tree.is_lumber_tree = True
        units.append(tree)
        self.effects.append({
            "type": "trait_activate",
            "trait_key": "Lumber",
            "trait_name": "远古树灵降临",
            "tier": 3,
            "x": tree.x, "y": tree.y - 40,
            "life": 2.0, "max_life": 2.0,
            "color": (120, 200, 80),
            "side": side,
        })

    def _find_free_position(self, cx, cy, used, screen_w, screen_h, unit_list):
        min_dist = (unit_list[0].size if unit_list else 48) * 1.2
        best_pos = (cx, cy)
        best_score = -1
        for radius_step in range(0, 12):
            for angle_step in range(8):
                if radius_step == 0:
                    px, py = cx, cy
                else:
                    ang = angle_step * (math.pi / 4)
                    px = cx + math.cos(ang) * radius_step * min_dist
                    py = cy + math.sin(ang) * radius_step * min_dist
                px = max(60, min(screen_w - 60, px))
                py = max(60, min(screen_h - 60, py))
                min_d2 = float("inf")
                for ux, uy in used:
                    d2 = (px - ux) ** 2 + (py - uy) ** 2
                    if d2 < min_d2:
                        min_d2 = d2
                if min_d2 > best_score:
                    best_score = min_d2
                    best_pos = (px, py)
                if min_d2 >= (min_dist * 0.8) ** 2:
                    return px, py
        return best_pos

    def _spawn_units(self, player, side, screen_w, screen_h, buffs):
        units = []
        rows, cols = 4, 7
        pad_x = screen_w * 0.04
        cell_w = (screen_w - 2 * pad_x) / cols
        
        # 强制战斗区域限制在屏幕高度的 10% 到 90% 之间
        battle_top = screen_h * 0.10
        battle_bottom = screen_h * 0.90
        battle_height = battle_bottom - battle_top
        row_h = battle_height / 8  # 上下半场各 4 排，共 8 排
        
        # 单位大小同时受宽度和高度限制，实现等比缩放
        size = max(28, int(min(cell_w * 0.75, row_h * 0.85)))
        
        if side == "ally":
            y_front = battle_bottom - row_h * 3.5  # 己方前排在下方
            y_back = battle_bottom
        else:
            y_front = battle_top + row_h * 3.5     # 敌方前排在上方
            y_back = battle_top
        y_step = (y_back - y_front) / max(1, rows - 1)
        board = player["board"]
        for r in range(rows):
            row = board[r]
            y = y_front + r * y_step
            for c in range(cols):
                u = row[c]
                if u is None:
                    continue
                safe_unit(u)
                x = pad_x + (c + 0.5) * cell_w
                bu = BattleUnit(u, x, y, side, buffs, size=size)
                bu.owner_player = player
                bu.source_unit = u
                bu.source_coords = (r, c)
                if side == "enemy" and player.get("_skill_plunder_block"):
                    bu.base["_plunder_skill_block"] = True
                units.append(bu)
        return units

    def update(self, dt, screen_w, screen_h):
        self._artifact_tick(dt)
        self._update_effects(dt)
        if self.finished:
            return
        for u in self.allies:
            u.update(dt, self.allies, self.enemies, self.effects, screen_w, screen_h)
        for u in self.enemies:
            u.update(dt, self.enemies, self.allies, self.effects, screen_w, screen_h)
        alive_a = [u for u in self.allies if u.alive]
        alive_e = [u for u in self.enemies if u.alive]
        if not alive_a or not alive_e:
            self._finish(alive_a, alive_e)

    def _update_effects(self, dt):
        new_effect = []
        for eff in self.effects:
            eff["life"] -= dt
            if eff["life"] <= 0:
                continue
            if eff["type"] == "damage_pop":
                eff["y"] -= 26 * dt
            elif eff["type"] == "skill_name":
                eff["y"] -= 20 * dt
            elif eff["type"] == "trait_activate":
                eff["y"] -= 8 * dt
            elif eff["type"] == "shockwave" and eff.get("delay", 0) > 0:
                eff["delay"] -= dt
                new_effect.append(eff)
                continue
            new_effect.append(eff)
        self.effects = new_effect
        if len(self.effects) > 150:
            self.effects = self.effects[-80:]

    def _clear_lumber_temp(self):
        """战斗结束：清除首领全部战斗临时属性加成（吸收的生命为战斗临时值）。"""
        for u in self.allies + self.enemies:
            bonus = getattr(u, "_lumber_hp_bonus", 0)
            if bonus:
                u.base["hp"] = max(1, u.base["hp"] - bonus)
                u._lumber_hp_bonus = 0
                u.current_hp = min(u.current_hp, u.base["hp"])

    def _finish(self, alive_a, alive_e):
        self.finished = True
        if alive_a and not alive_e:
            self.winner = 'attacker'
        elif alive_e and not alive_a:
            self.winner = 'defender'
        else:
            self.winner = 'draw'
        self._clear_lumber_temp()
        # 战斗结束：销毁远古树灵（不参与战果记录/存活计数；巨斧首领标记保留在玩家棋盘）
        self.allies = [u for u in self.allies
                       if not getattr(u, "is_lumber_tree", False)]
        self.enemies = [u for u in self.enemies
                        if not getattr(u, "is_lumber_tree", False)]

    def force_end(self):
        if self.finished:
            return
        alive_a = [u for u in self.allies if u.alive]
        alive_e = [u for u in self.enemies if u.alive]
        self._finish(alive_a, alive_e)


class GameState:
    def __init__(self, difficulty="normal", net=None, is_host=False):
        self.difficulty = difficulty
        self.net = net
        self.is_host = is_host
        self.is_multiplayer = net is not None
        self.multiplayer_phase = "prep"
        self.my_ready = False
        self.peer_hp = 100
        self.peer_name = "好友"
        self._my_seed = 0
        self._battle_wait_start = 0.0
        self._wait_peer_start = 0.0
        self._toast = None
        self._toast_timer = 0.0
        self._congrats_mode = False
        self._congrats_neeko_given = False
        self._congrats_50hp_given = False

        ai_mult = DIFFICULTY_MULT.get(difficulty, 1.0)
        self.me = create_empty_player(gold=START_GOLD_PLAYER, is_ai=False)
        # 巨斧选择器不再开局无条件发放：改为玩家首次拥有伐木棋子时自动补发
        if self.is_multiplayer:
            self.players = []
            self.me["gold"] = 30
        else:
            self.players = [create_empty_player(gold=START_GOLD_AI, is_ai=True,
                                                 difficulty_mult=ai_mult)
                            for _ in range(7)]
        self.shop = []
        self.shop_locked = False
        init_pool()
        self.refresh_shop()
        self.show_trait_popup = False
        self.show_odds_popup = False
        self.show_pool_popup = False
        self.stage = (1, 1)
        self.phase_timer = PREP_DURATION
        self.is_battle_phase = False
        self.detail_unit = None
        self.show_shop = True
        self.viewing_player_idx = -1
        self.battle_log = ""
        self.battle_log_history = []
        self.dragging = False
        self.drag_source_type = None
        self.drag_idx1 = -1
        self.drag_idx2 = -1
        self.drag_unit = None
        self.detail_source_type = None
        self.detail_i1 = -1
        self.detail_i2 = -1
        self._detail_sell_rect = None
        self.show_battle_bench = False
        self._battle_bench_toggle_rect = None
        self._battle_sell_rect = None
        self._battle_ally_hit_rects = []
        self._trait_scroll = 0
        self._trait_max_scroll = 0
        self._trait_drag_start = None
        self._trait_popup_rect = None
        self.mouse_down_pos = (0, 0)
        self.battle_result_timer = 0.0
        self.battle_result_text = ""
        self.battle_result_color = RED
        self.round_counter = 0
        self.hex_choices = []
        self.show_hex_popup = False
        self.show_augment_popup = False
        self.augment_choices = []
        self.augment_chosen = False
        self.battles = []
        self.watched_battle_idx = 0
        self.battle_phase_timer = 0.0
        self.battle_phase_resolved = False
        self._overtime_active = False
        self.post_battle_timer = 0.0
        self._fixed_accum = 0.0
        self.game_over = False
        self.game_over_text = ""
        self.game_over_action = None
        self.speed = 1.0
        self.dragging_item = None
        self.dragging_item_idx = -1
        self.hover_item_idx = -1
        self.item_click_start = None
        self.show_item_choice_popup = False
        self._radiant_chest_choices = None
        self._masterwork_choices = None
        self._masterwork_old_items = None
        self._emblem_tome_choices = None
        self._item_choice_source_index = -1
        self._item_choice_target = None
        self._item_choice_rects = []
        self._tome_bench_idx = None
        self._tome_close_rect = None
        self.show_carousel = False
        self.carousel_options = []
        self.carousel_selected = -1
        self.carousel_timer = 0.0
        self.carousel_queue = []
        self.show_item_path_popup = False
        self.item_path_id = None
        self.show_starter_popup = True
        self.starter_choices = self._roll_starter_choices()
        self.starter_chosen = False
        self.global_augment = roll_global_augment()
        self.show_global_augment_popup = False
        self.bounty_shards = 0
        self.bounty_layer_current = 1
        self.bounty_last_layer_seen = 1
        self.bounty_layer_options = []
        self.show_bounty_popup = False
        self._pending_plunder = None
        self._active_plunder = None
        self._bounty_capture_bonus = 0
        one_cost = [c for c in CHAMPION_LIST
                    if c["cost"] == 1 and not c.get("no_shop")]
        for ai in self.players:
            if one_cost:
                c = random.choice(one_cost)
                u = make_unit_with_star(c["name"], 1)
                if u:
                    ai["bench"][0] = u
                    consume_pool(c["name"], 1)
            ai_auto_position(ai)

    def _toast_msg(self, msg, color=RED, dur=1.4):
        self._toast = msg
        self._toast_timer = dur
        self._toast_color = color

    def _roll_starter_choices(self):
        one_cost = [c for c in CHAMPION_LIST
                    if c["cost"] == 1 and not c.get("no_shop")
                    and pool_remaining(c["name"]) > 0]
        if len(one_cost) < 3:
            one_cost = [c for c in CHAMPION_LIST
                        if c["cost"] == 1 and not c.get("no_shop")]
        return random.sample(one_cost, min(3, len(one_cost)))

    def pick_starter(self, idx):
        if 0 <= idx < len(self.starter_choices):
            champ = self.starter_choices[idx]
            # Starter choices are not reserved while the popup is open. If an
            # opponent consumed the last copy meanwhile, fall back to an
            # actually available one-cost champion instead of creating a copy.
            if not try_consume_pool(champ["name"], 1):
                # 若被对手抢光，回退到同费用的可用英雄（恭喜发财下为5费，普通模式仍为1费）
                c_cost = champ.get("cost", 1)
                available = [c for c in CHAMPION_LIST
                             if c.get("cost") == c_cost and not c.get("no_shop")
                             and pool_remaining(c["name"]) > 0]
                champ = random.choice(available) if available else None
                if champ is not None and not try_consume_pool(champ["name"], 1):
                    champ = None
            if champ is not None:
                u = make_unit_with_star(champ["name"], 1)
                if u:
                    self.me["bench"][0] = u
                    self.battle_log = f"起始英雄: {champ_cn(champ['name'])}"
                else:
                    return_pool(champ["name"], 1)
                play_sfx("buy")
            else:
                self.battle_log = "共享英雄池暂时无可选英雄，请重新开始本局"
                self._toast_msg("英雄池已耗尽，请重新开始")
                return
        self.show_starter_popup = False
        self.starter_chosen = True
        if not self.is_multiplayer:
            self.show_global_augment_popup = True
        else:
            self.stage = (1, 2)
            self.phase_timer = 999999

    def confirm_global_augment(self):
        aug = self.global_augment
        apply_augment_to_player(self.me, aug)
        for ai in self.players:
            apply_augment_to_player(ai, aug)
        self.show_global_augment_popup = False
        self.battle_log = f"全局强化: {aug['name']}"
        play_sfx("hex")
        for p in [self.me] + self.players:
              if p["hp"] > 0:
                   apply_income_and_xp(p)
        self.stage = (1, 2)
        self.phase_timer = PREP_DURATION

    def ai_assistant_say(self, event):
        quips = {
            "no_gold": ["别刷了，留钱吃利息吧！", "你再刷我就脑补一个扣钱bug！"],
            "bench_full": ["备战席满了！卖几个吧！", "别买了，我快没地方塞土豆了！"],
            "win": ["// 代码完美无缺", "看吧！这就是雷霆羁绊的力量！"],
            "lose": ["别慌，我在打补丁了。", "这波是我的锅，我脑补错方向了。"],
            "idle": ["在吗？", "你为啥不买棋子？", "要不咱们种土豆吧？"]
        }
        if event in quips:
            self._toast_msg(random.choice(quips[event]), (100, 255, 100), 2.0)

    def refresh_shop(self):
        if not self.shop_locked:
            if self.can_free_shop():
                self.shop = roll_shop_by_odds_free_five(self.me["level"])
            else:
                self.shop = roll_shop_by_odds(self.me["level"])

    def can_free_shop(self):
        return getattr(self, "_active_plunder", None) == "shop"

    def refresh_shop_paid(self):
        if not self.can_free_shop():
            if self.me["gold"] < REFRESH_COST:
                play_sfx("error")
                return False
            self.me["gold"] -= REFRESH_COST
        self.shop_locked = False
        self.refresh_shop()
        return True

    def current_battle(self):
        if not self.battles:
            return None
        if self.watched_battle_idx < 0:
            self.watched_battle_idx = 0
        if self.watched_battle_idx >= len(self.battles):
            self.watched_battle_idx = 0
        return self.battles[self.watched_battle_idx]

    def player_battle(self):
        return next((b for b in self.battles if b.is_player_battle), None)

    def player_label(self, p):
        if p is self.me:
            return "你"
        if self.is_multiplayer:
            return self.peer_name
        for i, ai in enumerate(self.players):
            if ai is p:
                return f"AI{i+1}"
        return "?"

    def try_combine(self, target_player):
        ai_try_combine(target_player)

    def buy_champ(self, idx):
        if not (0 <= idx < len(self.shop)):
            play_sfx("error")
            return
        champ = self.shop[idx]
        if champ is None or (not self.can_free_shop() and self.me["gold"] < champ["cost"]):
            play_sfx("error")
            self._toast_msg("金币不足!")
            self.ai_assistant_say("no_gold")
            return
        if pool_remaining(champ["name"]) <= 0 and not (self.can_free_shop() and champ.get("cost") == 5):
            self.shop[idx] = None
            self.battle_log = f"{champ_cn(champ['name'])} 已售罄!"
            self._toast_msg("该棋子已售罄")
            play_sfx("error")
            return
        empty_idx = next((i for i, s in enumerate(self.me["bench"])
                          if s is None), None)
        if empty_idx is None:
            self.battle_log = "备战席已满! 请先上场或出售"
            self._toast_msg("备战席已满!")
            self.ai_assistant_say("bench_full")
            play_sfx("error")
            return
        # Reserve a copy atomically before changing gold or bench state.
        if not (self.can_free_shop() and champ.get("cost") == 5):
            if not try_consume_pool(champ["name"], 1):
                self.shop[idx] = None
                self.battle_log = f"{champ_cn(champ['name'])} 已售罄!"
                self._toast_msg("该棋子已售罄")
                play_sfx("error")
                return
        if not self.can_free_shop():
            self.me["gold"] -= champ["cost"]
        self.me["bench"][empty_idx] = copy.deepcopy(champ)
        self.shop[idx] = None
        play_sfx("buy")
        self.try_combine(self.me)
        self.battle_log = f"已购买 {champ_cn(champ['name'])} (备战席 {empty_idx+1})"
        self.sync_lumber_marks()
        save_game(self)

    def sell_unit_at(self, source_type, i1, i2=-1):
        unit = None
        if source_type == "bench":
            if not (0 <= i1 < len(self.me["bench"])):
                return False, 0
            unit = self.me["bench"][i1]
        elif source_type == "board":
            if not (0 <= i1 < 4 and 0 <= i2 < 7):
                return False, 0
            unit = self.me["board"][i1][i2]
        else:
            return False, 0
        if unit is None:
            return False, 0
        safe_unit(unit)
        # 纹章之书伪棋子：出售动作 → 打开4选1纹章弹窗（伪棋子保留）
        if unit.get("is_pseudo_bench_only") and unit.get("pseudo_kind") == "emblem_tome":
            if source_type != "bench":
                return False, 0
            return self._open_tome_choice(i1), 0
        carried_items = list(unit.get("items", []))
        if len(self.me["items"]) + len(carried_items) > MAX_ITEM_BENCH:
            self.battle_log = "装备备战席已满，请先腾出空间再出售棋子!"
            self._toast_msg("装备栏已满!")
            play_sfx("error")
            return False, 0
        if source_type == "bench":
            self.me["bench"][i1] = None
        else:
            self.me["board"][i1][i2] = None
        star = unit.get("star", 1)
        refund = unit["cost"] * (3 ** (star - 1))
        self.me["items"].extend(carried_items)
        self._flush_free_item_store()
        count = 3 ** (star - 1)
        return_pool(unit["name"], count)
        self.me["gold"] += refund
        self.battle_log = f"出售 {champ_cn(unit['name'])} {star}星 +{refund}金"
        play_sfx("sell")
        enforce_population_cap(self.me)
        self.sync_lumber_marks()
        save_game(self)
        return True, refund

    def sync_lumber_marks(self):
        """只有激活 3 伐木（或以上）羁绊才发放/保留巨斧选择器。
        未激活时回收巨斧并清空全部首领标记。"""
        p = self.me
        items = p.setdefault("items", [])
        has_axe = any(it.get("special_kind") == "giant_axe" for it in items)
        if get_lumber_tier(p) > 0:
            if not has_axe:
                items.append(make_special_item("giant_axe"))
        else:
            if has_axe:
                p["items"] = [it for it in items
                              if it.get("special_kind") != "giant_axe"]
            for row in p["board"]:
                for u in row:
                    if u is not None:
                        u.pop("is_lumber_chief", None)
            for u in p["bench"]:
                if u is not None:
                    u.pop("is_lumber_chief", None)

    def try_combine_item_bench(self, i, j):
        """物品栏内两个散件拖拽重叠直接合成；成装/神符/神器/光明/特殊道具禁止参与。"""
        items = self.me["items"]
        if i == j or not (0 <= i < len(items) and 0 <= j < len(items)):
            return False
        a, b = items[i], items[j]
        if a.get("is_combined") or b.get("is_combined"):
            self._toast_msg("成装/神符/神器/光明/特殊道具不能参与物品栏合成")
            play_sfx("error")
            return False
        new_items, ok = try_combine_items([a, b])
        if not ok:
            self._toast_msg("这两个散件无法合成")
            play_sfx("error")
            return False
        hi, lo = (i, j) if i > j else (j, i)
        items.pop(hi)
        items.pop(lo)
        items.insert(lo, new_items[0])
        self.battle_log = (f"物品栏合成：{a['name']} + {b['name']} = "
                           f"{new_items[0]['name']}")
        play_sfx("hex")
        self._flush_free_item_store()
        return True

    def buy_xp(self):
        if self.me["level"] >= MAX_LEVEL:
            play_sfx("error")
            self._toast_msg("已满级")
            return
        if self.me["gold"] < BUY_XP_COST:
            play_sfx("error")
            self._toast_msg("金币不足!")
            self.ai_assistant_say("no_gold")
            return
        old_level = self.me["level"]
        self.me["gold"] -= BUY_XP_COST
        self.me["xp"] += BUY_XP_AMOUNT
        while self.me["level"] < MAX_LEVEL and self.me["xp"] >= self.me["xp_next"]:
            self.me["xp"] -= self.me["xp_next"]
            self.me["level"] += 1
            self.me["xp_next"] = XP_TABLE[self.me["level"]]
        if self.me["level"] >= MAX_LEVEL:
            self.me["xp"] = 0
            self.me["xp_next"] = XP_TABLE[MAX_LEVEL]
        play_sfx("buy")
        if self.me["level"] > old_level:
            self.battle_log = f"升级至 Lv{self.me['level']}! 请手动安排上场单位"

    def pick_hex(self, idx):
        if 0 <= idx < len(self.hex_choices):
            h = self.hex_choices[idx]
            apply_hex_to_player(self.me, h)
            self.battle_log = f"符文: {h['name']}"
            play_sfx("hex")
        else:
            play_sfx("click")
        self.show_hex_popup = False
        self.hex_choices = []

    def _special_item_index(self, item_ref):
        if isinstance(item_ref, int):
            return item_ref if 0 <= item_ref < len(self.me.get("items", [])) else -1
        return next((i for i, it in enumerate(self.me.get("items", []))
                     if it is item_ref), -1)

    def use_special_item(self, item_ref, target_unit, target_source=None):
        idx = self._special_item_index(item_ref)
        if idx < 0 or target_unit is None:
            return False
        item = self.me["items"][idx]
        kind = item.get("special_kind")
        if kind not in SPECIAL_ITEM_DATA:
            return False
        # 必须直接操作真棋子(safe_unit会返回浅拷贝，会导致拆卸/重铸等修改不落盘)
        if not isinstance(target_unit, dict):
            return False
        target = target_unit
        if target.get("is_pseudo_bench_only"):
            self._toast_msg("纹章之书是消耗型伪棋子，不能使用道具")
            play_sfx("error")
            return False
        target.setdefault("items", [])

        if kind == "giant_axe":
            # 巨斧选择器：仅备战阶段可用；只允许拖拽到棋盘上已上场的伐木弈子。
            if self.is_battle_phase:
                self._toast_msg("战斗阶段无法使用巨斧选择器！")
                play_sfx("error")
                return False
            if target_source != "board":
                self._toast_msg("巨斧选择器只能拖拽到棋盘上已上场的伐木弈子！")
                play_sfx("error")
                return False
            if "Lumber" not in target.get("traits", []):
                self._toast_msg("目标不是伐木羁绊棋子，无法标记为伐木首领！")
                play_sfx("error")
                return False
            # 新标记覆盖旧标记：先清空全部旧标记
            for row in self.me["board"]:
                for u in row:
                    if u is not None:
                        u.pop("is_lumber_chief", None)
            target["is_lumber_chief"] = True
            self.battle_log = (f"巨斧选择器：{champ_cn(target['name'])} "
                               f"已标记为伐木首领（道具不消耗）")
            play_sfx("hex")
            return True

        if kind == "orb":
            self.me["items"].pop(idx)
            roll = random.randint(1, 4)
            if roll == 1:
                reward = new_item(random.choice(ITEM_IDS))
                _add_bounty_item(self, reward)
                self.battle_log = "法球：获得随机散件"
            elif roll == 2:
                reward = _make_random_combined_item()
                _add_bounty_item(self, reward)
                self.battle_log = "法球：获得随机成装"
            elif roll == 3:
                self.me["gold"] += random.randint(3, 10)
                self.battle_log = "法球：获得随机金币"
            else:
                reward = make_special_item(random.choice(["haotian_hammer", "disassembler", "mega_neeko", "radiant_chest", "masterwork_upgrader"]))
                _add_bounty_item(self, reward)
                self.battle_log = "法球：获得随机特殊道具"
            self._flush_free_item_store()
            return True

        if kind == "disassembler":
            # 战斗阶段禁止对棋盘战斗棋子拆卸
            if self.is_battle_phase and target_source == "board":
                self._toast_msg("战斗阶段无法拆卸棋盘上正在对战的棋子装备！")
                play_sfx("error")
                return False
            if not target.get("items"):
                self._toast_msg("目标身上没有装备，无法拆卸！")
                play_sfx("error")
                return False
            self.me["items"].pop(idx)
            self.me["items"].append(make_special_item("disassembler"))
            removed = list(target.get("items", []))
            target["items"] = []
            sync_unit_traits_from_items(target)
            for it in removed:
                if len(self.me["items"]) < MAX_ITEM_BENCH:
                    self.me["items"].append(it)
                else:
                    self.me.setdefault("free_item_store", []).append(it)
            self.battle_log = f"拆卸器：已拆下 {champ_cn(target['name'])} 的全部装备"
            self._flush_free_item_store()
            return True

        if kind == "haotian_hammer":
            # 战斗阶段禁止对棋盘战斗棋子重铸
            if self.is_battle_phase and target_source == "board":
                self._toast_msg("战斗阶段无法对棋盘上正在对战的棋子使用昊天锤！")
                play_sfx("error")
                return False
            if not target.get("items"):
                self._toast_msg("目标身上没有装备，无法重铸！")
                play_sfx("error")
                return False
            # 完整流程：卸下全部装备 → 重铸 → 全部装回原棋子
            old_items = list(target["items"])
            target["items"] = []
            target["items"] = [_reroll_item(it) for it in old_items]
            sync_unit_traits_from_items(target)
            self.me["items"].pop(idx)
            self.battle_log = (f"昊天锤：重铸 {champ_cn(target['name'])} "
                               f"身上全部 {len(old_items)} 件装备")
            play_sfx("hex")
            return True

        if kind == "masterwork_upgrader":
            if self.is_battle_phase and target_source == "board":
                self._toast_msg("战斗阶段无法对棋盘战斗棋子升级装备！")
                play_sfx("error")
                return False
            candidates = [it for it in target.get("items", [])
                          if it.get("is_combined") and not it.get("is_rune")
                          and not it.get("is_special") and not it.get("is_radiant")]
            choices = [make_radiant_item(it.get("name", "")) for it in candidates]
            choices = [x for x in choices if x]
            if not choices:
                self._toast_msg("目标身上没有可升级的成装！")
                play_sfx("error")
                return False
            if len(choices) == 1:
                target["items"].remove(candidates[0])
                self.me["items"].pop(idx)
                self.me["items"].append(choices[0])
                self.battle_log = f"杰作升级器：{candidates[0].get('name')} → {choices[0]['name']}"
                return True
            # 多件成装：全部生成可升级候选，但只领取选择的那一件，其他普通成装保留。
            self._masterwork_choices = choices
            self._masterwork_old_items = candidates
            self._item_choice_source_index = idx
            self._item_choice_target = target
            self.show_item_choice_popup = True
            self.battle_log = "杰作升级器：请选择要升为光明版的成装"
            return True

        if kind == "mega_neeko":
            # 大妮蔻：备战/战斗阶段、棋盘/备战席目标均可用；备战席满则道具不消耗
            empty = next((i for i, x in enumerate(self.me["bench"])
                          if x is None), None)
            if empty is None:
                self._toast_msg("备战席已满！大妮蔻不消耗")
                play_sfx("error")
                return False
            clone = make_unit_with_star(target["name"], 1)
            if clone is None:
                self._toast_msg("无法复制该目标")
                play_sfx("error")
                return False
            self.me["bench"][empty] = clone
            self.me["items"].pop(idx)
            consume_pool(target["name"], 1)
            self.battle_log = f"大妮蔻：复制 {champ_cn(target['name'])} 1星"
            play_sfx("hex")
            return True

        if kind == "radiant_chest":
            if self.is_battle_phase and target_source == "board":
                self._toast_msg("战斗阶段无法对棋盘战斗棋子使用光明宝箱！")
                play_sfx("error")
                return False
            choices=[]
            for it in target.get("items", []):
                if it.get("is_combined") and not it.get("is_radiant") and not it.get("is_special") and not it.get("is_rune"):
                    r=make_radiant_item(it.get("name",""))
                    if r: choices.append(r)
            choices += [random_radiant_item() for _ in range(max(0,3-len(choices)))]
            choices=[x for x in choices if x]
            if not choices:
                return False
            # Store three choices for the next click/selection; default first is safe.
            self._radiant_chest_choices=choices[:3]
            self.show_item_choice_popup=True
            self._item_choice_source_index=idx
            self._item_choice_target=target
            self.battle_log="光明宝箱：请选择1件光明成装"
            return True

        if kind == "artifact_forge":
            self.me["items"][idx]=make_artifact_item()
            self.battle_log="豹药神器锻造器：获得一件随机豹药神器"
            return True

        if kind == "emblem_tome":
            # 旧存档遗留的物品型纹章之书：仍可直接使用（新产出走备战席伪棋子）
            self._emblem_tome_choices=random.sample(
                [t for t in TRAIT_DATA if t not in ("BearRidge","RuneLand")],
                min(4, len([t for t in TRAIT_DATA if t not in ("BearRidge","RuneLand")]))
            )
            self.show_item_choice_popup=True
            self._item_choice_source_index=idx
            self._item_choice_target=None
            self._tome_bench_idx=None
            self.battle_log="纹章之书：请选择一个随机纹章"
            return True
        return False

    def choose_special_item_option(self, choice_idx):
        choices=getattr(self,"_radiant_chest_choices",None)
        source_idx=getattr(self,"_item_choice_source_index",-1)
        if choices:
            if not (0 <= choice_idx < len(choices)) or source_idx < 0:
                return False
            target=getattr(self,"_item_choice_target",None)
            if target is None:
                return False
            old=[it for it in target.get("items",[]) if it.get("is_combined") and not it.get("is_radiant") and not it.get("is_special") and not it.get("is_rune")]
            if old:
                target["items"].remove(old[0])
            self.me["items"].pop(source_idx)
            self.me["items"].append(choices[choice_idx])
            self._radiant_chest_choices=None
            self.show_item_choice_popup=False
            self.battle_log="光明宝箱：已获得"+choices[choice_idx]["name"]
            return True
        choices=getattr(self,"_masterwork_choices",None)
        if choices:
            if not (0 <= choice_idx < len(choices)) or source_idx < 0:
                return False
            target=getattr(self,"_item_choice_target",None)
            old_items=getattr(self,"_masterwork_old_items",None) or []
            if target is None or choice_idx >= len(old_items):
                return False
            old=old_items[choice_idx]
            if old not in target.get("items",[]):
                return False
            target["items"].remove(old)
            self.me["items"].pop(source_idx)
            self.me["items"].append(choices[choice_idx])
            self._masterwork_choices=None
            self._masterwork_old_items=None
            self.show_item_choice_popup=False
            self.battle_log="杰作升级器：已获得"+choices[choice_idx]["name"]
            self._flush_free_item_store()
            return True
        choices=getattr(self,"_emblem_tome_choices",None)
        if choices and 0 <= choice_idx < len(choices):
            trait=choices[choice_idx]
            bench_idx=getattr(self,"_tome_bench_idx",None)
            if bench_idx is not None and 0 <= bench_idx < len(self.me["bench"]) \
                    and self.me["bench"][bench_idx] is not None \
                    and self.me["bench"][bench_idx].get("is_pseudo_bench_only"):
                # 伪棋子路径：消耗备战席上的纹章之书
                self.me["bench"][bench_idx]=None
            elif 0 <= source_idx < len(self.me["items"]):
                # 旧存档物品路径：消耗物品栏中的纹章之书
                self.me["items"].pop(source_idx)
            _add_bounty_item(self, make_trait_emblem(trait))
            self._emblem_tome_choices=None
            self._tome_bench_idx=None
            self.show_item_choice_popup=False
            self.battle_log=f"纹章之书：获得{trait_cn(trait)}纹章"
            self._flush_free_item_store()
            return True
        return False

    def _open_tome_choice(self, bench_idx):
        """出售动作触发：纹章之书伪棋子 → 4选1纹章弹窗（伪棋子保留在备战席）。"""
        valid=[t for t in TRAIT_DATA if t not in ("BearRidge","RuneLand")]
        self._emblem_tome_choices=random.sample(valid, min(4, len(valid)))
        self._tome_bench_idx=bench_idx
        self._item_choice_source_index=-1
        self._item_choice_target=None
        self.show_item_choice_popup=True
        self.battle_log="纹章之书：请选择一个随机纹章"
        return True

    def close_item_choice_popup(self):
        """关闭纹章选择弹窗：放弃选择，伪棋子/道具均保留。"""
        self.show_item_choice_popup=False
        self._emblem_tome_choices=None
        self._radiant_chest_choices=None
        self._masterwork_choices=None
        self._masterwork_old_items=None
        self._tome_bench_idx=None
        self.battle_log="已放弃选择，纹章之书保留"

    def _flush_free_item_store(self):
        store = self.me.setdefault("free_item_store", [])
        while store and len(self.me["items"]) < MAX_ITEM_BENCH:
            self.me["items"].append(store.pop(0))

    def equip_item_to(self, item_ref, source_type, i1, i2=-1, allow_combine=True):
        if isinstance(item_ref, int):
            item_idx = item_ref
        else:
            item_idx = next((i for i, it in enumerate(self.me["items"])
                             if it is item_ref), -1)
        if item_idx < 0 or item_idx >= len(self.me["items"]):
            play_sfx("error")
            return False
        unit = None
        if source_type == "board":
            if 0 <= i1 < 4 and 0 <= i2 < 7:
                unit = self.me["board"][i1][i2]
        elif source_type == "bench":
            if 0 <= i1 < 8:
                unit = self.me["bench"][i1]
        if unit is None:
            play_sfx("error")
            return False
        if unit.get("is_pseudo_bench_only"):
            play_sfx("error")
            self._toast_msg("纹章之书不能装备道具")
            return False
        item = self.me["items"][item_idx]
        # 转职规则：同一棋子不能重复装备同一种转职；
        # 原生拥有该羁绊的棋子也不能再装备对应羁绊转职。
        if item.get("is_emblem"):
            trait = item.get("emblem_trait")
            if trait:
                unit_traits = set(unit.get("traits", []))
                if trait in unit_traits:
                    play_sfx("error")
                    self.battle_log = (
                        f"{champ_cn(unit['name'])} 已拥有「{trait_cn(trait)}」羁绊，不能装备同类转职")
                    self._toast_msg("已有该羁绊，不能重复装备")
                    return False
                if any(it.get("is_emblem") and it.get("emblem_trait") == trait
                       for it in unit.get("items", [])):
                    play_sfx("error")
                    self.battle_log = (
                        f"{champ_cn(unit['name'])} 已装备「{trait_cn(trait)}」转职，不能重复装备")
                    self._toast_msg("同一转职不能重复装备")
                    return False
        # 兜底校验：消耗型道具(拆卸器/昊天锤/法球等)不允许装配到棋子装备栏，
        # 拖到棋子上即执行 use_special_item；纹章/神器/普通装备/灵符才真正挂装。
        if not is_wearable_item(item):
            return self.use_special_item(item, unit, source_type)
        # 满编判断：若已达3件，只有当拖入散件能与已有散件合成(件数不超上限)时才允许
        if len(unit.get("items", [])) >= MAX_ITEMS_PER_UNIT:
            if not allow_combine:
                play_sfx("error")
                self.battle_log = f"{champ_cn(unit['name'])} 装备已满!"
                self._toast_msg("装备已满!")
                return False
            trial = try_combine_items_all(unit.get("items", []) + [item])
            if len(trial) > MAX_ITEMS_PER_UNIT:
                play_sfx("error")
                self.battle_log = f"{champ_cn(unit['name'])} 装备已满!"
                self._toast_msg("装备已满!")
                return False
        item = self.me["items"].pop(item_idx)
        unit.setdefault("items", []).append(item)
        if item.get("is_emblem"):
            trait = item.get("emblem_trait")
            if trait:
                unit.setdefault("traits", []).append(trait)
        play_sfx("coin")
        self.battle_log = f"装备 {item['name']} 给 {champ_cn(unit['name'])}"
        if allow_combine:
            before_len = len(unit["items"])
            unit["items"] = try_combine_items_all(unit["items"])
            if len(unit["items"]) < before_len:
                self.battle_log = "装备合成成功!"
                play_sfx("hex")
        enforce_population_cap(self.me)
        self._flush_free_item_store()
        return True

    def _start_monster_round(self):
        stage, rnd = self.stage
        self.battle_log = f"野怪回合 {stage}-{rnd}"
        monster_p = make_monster_team(stage, rnd)
        W, H = pygame.display.get_surface().get_size()
        inst = BattleInstance(self.me, monster_p, 0)
        inst.is_player_battle = True
        inst.is_monster_battle = True
        inst.spawn(W, H)
        
        self.battles = [inst]
        for ai in self.players:
            if ai["hp"] <= 0:
                continue
            ai_monster = make_monster_team(stage, rnd)
            ai_inst = BattleInstance(ai, ai_monster, len(self.battles))
            ai_inst.is_monster_battle = True
            ai_inst.is_ai_monster_battle = True
            ai_inst.spawn(W, H)
            self.battles.append(ai_inst)
        self.watched_battle_idx = 0
        self.battle_phase_timer = BATTLE_DURATION
        self.battle_phase_resolved = False
        self._overtime_active = False
        self.post_battle_timer = 0.0
        self._fixed_accum = 0.0
        self.is_battle_phase = True

    def _make_mirror_player(self, src_player):
        mirror = create_empty_player(gold=0, is_ai=True)
        mirror["level"] = src_player.get("level", MAX_LEVEL)
        mirror["hp"] = 999
        for r in range(4):
            for c in range(7):
                u = src_player["board"][r][c]
                if u is not None:
                    mirror["board"][r][c] = copy.deepcopy(u)
        mirror["hex_bonuses"] = copy.deepcopy(
            src_player.get("hex_bonuses", {}))
        mirror["hex_list"] = copy.deepcopy(src_player.get("hex_list", []))
        mirror["is_mirror"] = True
        return mirror

    def start_battle(self):
        if self.is_multiplayer:
            self._start_multiplayer_battle()
            return
        stage, rnd = self.stage
        round_type = get_round_type(stage, rnd)
        if stage == 1 and rnd == 1:
            return

        self.sync_lumber_marks()
        all_players = [self.me] + self.players
        for ai_p in self.players:
            if ai_p["hp"] > 0:
                ai_do_turn(ai_p, all_players)
        
        auto_fill_board(self.me)
        # 修复：开战瞬间不再强制刷新商店（锁定商店/刚选好的棋保留），
        # 商店刷新统一在战斗结束后的下一轮备战开始时进行
        if round_type == "monster":
            self._start_monster_round()
            return
        if round_type == "carousel":
            self._start_carousel()
            return
        alive_ais = [ai for ai in self.players if ai["hp"] > 0]
        if not alive_ais:
            self.battle_log = "胜利! 所有 AI 已被淘汰"
            self.game_over = True
            self.game_over_text = "胜利!"
            self.is_battle_phase = False
            play_sfx("victory")
            return

        entities = [self.me] + alive_ais
        random.shuffle(entities)

        W, H = pygame.display.get_surface().get_size()
        self.battles = []

        if len(entities) % 2 == 1:
            bye_player = random.choice(entities)
            entities.remove(bye_player)
            if entities:
                mirror_src = random.choice(entities)
                mirror = self._make_mirror_player(mirror_src)
                inst = BattleInstance(bye_player, mirror, 0)
                inst.is_mirror_battle = True
                inst.mirror_owner = mirror_src
                inst.is_player_battle = (bye_player is self.me)
                inst.spawn(W, H)
                self.battles.append(inst)

        pairs = []
        i = 0
        while i + 1 < len(entities):
            pairs.append((entities[i], entities[i + 1]))
            i += 2
        base_idx = len(self.battles)
        for j, (a, b) in enumerate(pairs):
            if b is self.me:
                a, b = b, a
            inst = BattleInstance(a, b, base_idx + j)
            inst.is_player_battle = (a is self.me)
            inst.spawn(W, H)
            self.battles.append(inst)

        self.watched_battle_idx = next(
            (i for i, bt in enumerate(self.battles) if bt.is_player_battle), 0)
        self.battle_phase_timer = BATTLE_DURATION
        self.battle_phase_resolved = False
        self._overtime_active = False
        self.post_battle_timer = 0.0
        self._fixed_accum = 0.0
        self.is_battle_phase = True

    def _start_multiplayer_battle(self):
        if not (self.net and self.net.connected):
            self.battle_log = "未连接"
            self._toast_msg("未连接")
            return
        stage, rnd = self.stage
        round_type = get_round_type(stage, rnd)
        # 野怪/选秀回合：双方独立进行，无需交换棋盘
        if round_type == "monster":
            self.multiplayer_phase = "battle"
            self._start_monster_round()
            return
        if round_type == "carousel":
            self.multiplayer_phase = "battle"
            self._start_carousel()
            return
        my_data = {
            "board": self.me["board"],
            "hex_bonuses": dict(self.me.get("hex_bonuses", {})),
            "hex_list": list(self.me.get("hex_list", [])),
            "seed": int(time.time() * 1000) & 0x7FFFFFFF,
        }
        if not self.net.send(my_data):
            self.battle_log = "发送失败，请重试"
            self._toast_msg("发送失败")
            self.multiplayer_phase = "prep"
            self._wait_peer_start = time.time()
            return
        self._my_seed = my_data["seed"]
        self._battle_wait_start = time.time()
        self.multiplayer_phase = "wait_battle"
        self.battle_log = "等待对手数据..."

    def _sanitize_network_board(self, board):
        empty = [[None] * 7 for _ in range(4)]
        if not isinstance(board, list) or len(board) != 4:
            return empty
        out = []
        for row in board:
            if not isinstance(row, list) or len(row) != 7:
                return empty
            clean_row = []
            for u in row:
                if u is None:
                    clean_row.append(None)
                    continue
                if not isinstance(u, dict):
                    clean_row.append(None)
                    continue
                u = safe_unit(u)
                if not get_base_template(u.get("name", "")):
                    clean_row.append(None)
                    continue
                u["items"] = [x for x in (_sanitize_sim_item(it) for it in u.get("items", [])) if x is not None]
                sync_unit_traits_from_items(u)
                clean_row.append(u)
            out.append(clean_row)
        return out

    def _setup_multiplayer_battle(self, peer_msg):
        try:
            peer_seed = int(peer_msg.get("seed", 0))
        except Exception:
            peer_seed = 0
        if not hasattr(self, "_saved_random_state"):
            self._saved_random_state = random.getstate()
        random.seed(self._my_seed ^ peer_seed)

        default_bonuses = {"hp_mult": 0.0, "atk_mult": 0.0, "sp_mult": 0.0,
                           "crit": 0.0, "atk_speed": 0.0, "income": 0, "armor": 0}
        empty_board = [[None] * 7 for _ in range(4)]
        peer = create_empty_player(gold=0, is_ai=True)
        # 防御对手畸形/伪造数据：类型不符时回退默认值，避免崩溃
        board = peer_msg.get("board", empty_board)
        peer["board"] = self._sanitize_network_board(board)
        hb = peer_msg.get("hex_bonuses", default_bonuses)
        peer["hex_bonuses"] = hb if isinstance(hb, dict) else default_bonuses
        hl = peer_msg.get("hex_list", [])
        peer["hex_list"] = hl if isinstance(hl, list) else []
        peer["hp"] = 999
        peer["is_ai"] = True

        W, H = pygame.display.get_surface().get_size()
        inst = BattleInstance(self.me, peer, 0)
        inst.is_player_battle = True
        inst.spawn(W, H)
        self.battles = [inst]
        self.watched_battle_idx = 0
        self.battle_phase_timer = BATTLE_DURATION
        self.battle_phase_resolved = False
        self._overtime_active = False
        self.post_battle_timer = 0.0
        self._fixed_accum = 0.0
        self.is_battle_phase = True
        self.multiplayer_phase = "battle"
        self.battle_log = "与好友战斗！"

    def update_battle_tick(self, dt, screen_w, screen_h):
        self._fixed_accum += dt
        steps = 0
        while (self._fixed_accum >= FIXED_BATTLE_DT
               and steps < MAX_FIXED_STEPS):
            self._step_battles(FIXED_BATTLE_DT, screen_w, screen_h)
            self._fixed_accum -= FIXED_BATTLE_DT
            steps += 1

    def _step_battles(self, dt, screen_w, screen_h):
        for i, battle in enumerate(self.battles):
            is_watched = (i == self.watched_battle_idx)
            if battle.is_watched != is_watched:
                battle.is_watched = is_watched
                battle.sync_mute()
            battle.update(dt, screen_w, screen_h)
        if self.battle_phase_resolved:
            self.post_battle_timer -= dt
            if self.post_battle_timer <= 0:
                self._advance_to_next_round()
            return
        self.battle_phase_timer -= dt
        if self.battle_phase_timer <= 0:
            # 加时赛：首次归零时若仍有战斗双方都有存活单位，强化残血继续打，不立刻判平
            undecided = [b for b in self.battles
                          if not b.finished
                          and any(u.alive for u in b.allies)
                          and any(u.alive for u in b.enemies)]
            if undecided and not self._overtime_active:
                self._overtime_active = True
                self.battle_phase_timer = OVERTIME_DURATION
                for b in undecided:
                    for u in b.allies + b.enemies:
                        if u.alive:
                            u.atk_buff *= 2.0        # 加时伤害翻倍
                            u.atk_speed_mult *= 1.8  # 加时攻速大幅提升
                self.battle_log = "加时赛！残血激战"
            else:
                for battle in self.battles:
                    battle.force_end()
        if all(b.finished for b in self.battles):
            self._resolve_all_battles()
            self.battle_phase_resolved = True
            self.post_battle_timer = POST_BATTLE_WAIT

    def _resolve_mirror_battle(self, battle, stage):
        a = battle.attacker
        if battle.winner == 'attacker':
            apply_battle_result(a, True)
        elif battle.winner == 'defender':
            survivors = len([u for u in battle.enemies if u.alive])
            dmg = compute_player_damage(stage, survivors)
            a["hp"] -= dmg
            apply_battle_result(a, False)
        else:
            a["hp"] -= 2
            apply_battle_result(a, None)

    def _resolve_pvp_pair(self, battle, stage):
        a, b = battle.attacker, battle.defender
        if battle.winner == 'attacker':
            survivors = len([u for u in battle.allies if u.alive])
            dmg = compute_player_damage(stage, survivors)
            b["hp"] -= dmg
            apply_battle_result(a, True)
            apply_battle_result(b, False)
        elif battle.winner == 'defender':
            survivors = len([u for u in battle.enemies if u.alive])
            dmg = compute_player_damage(stage, survivors)
            a["hp"] -= dmg
            apply_battle_result(a, False)
            apply_battle_result(b, True)
        else:
            a["hp"] -= 2
            b["hp"] -= 2
            apply_battle_result(a, None)
            apply_battle_result(b, None)

    def _resolve_all_battles(self):
        stage, rnd = self.stage

        if self.is_multiplayer:
            pb = self.player_battle()
            round_type = get_round_type(stage, rnd)
            if pb:
                if round_type == "monster":
                    # 联机野怪回合：胜利掉装备/钱，失败按野怪规则扣血；不计连胜连败
                    if pb.winner == 'defender':
                        survivors = len([u for u in pb.enemies if u.alive])
                        dmg = compute_player_damage(stage, survivors)
                        self.me["hp"] = max(0, self.me["hp"] - dmg)
                        self.battle_log = f"野怪失败! 承受 {dmg} 伤害"
                        self.battle_result_text = f"失败 -{dmg}"
                        self.battle_result_color = RED
                    else:
                        self.battle_log = "野怪胜利!"
                        self.battle_result_text = "胜利!"
                        self.battle_result_color = GOLD_COLOR
                        play_sfx("victory")
                        self._monster_drop(stage, rnd)
                else:
                    if pb.winner == 'attacker':
                        survivors = len([u for u in pb.allies if u.alive])
                        self.battle_log = f"胜利！存活 {survivors}"
                        self.battle_result_text = "胜利"
                        self.battle_result_color = GOLD_COLOR
                        self.me["win_streak"] += 1
                        self.me["lose_streak"] = 0
                    elif pb.winner == 'defender':
                        survivors = len([u for u in pb.enemies if u.alive])
                        dmg = 5 + survivors * 2
                        self.me["hp"] = max(0, self.me["hp"] - dmg)
                        self.battle_log = f"失败！-{dmg} HP"
                        self.battle_result_text = f"失败 -{dmg}"
                        self.battle_result_color = RED
                        self.me["lose_streak"] += 1
                        self.me["win_streak"] = 0
                    else:
                        self.battle_log = "平局"
                        self.battle_result_text = "平局"
                        self.battle_result_color = GOLD_COLOR
                        self.me["win_streak"] = 0
                        self.me["lose_streak"] = 0
                self.battle_result_timer = 2.0
                if self.net and self.net.connected:
                    self.net.send({
                        "my_hp": self.me["hp"],
                        "winner": pb.winner,
                    })
                if self.me["hp"] <= 0:
                    self.game_over = True
                    self.game_over_text = "失败"
            return

        pb = self.player_battle()

        for battle in self.battles:
            if battle.is_monster_battle:
                if getattr(battle, 'is_ai_monster_battle', False):
                    a = battle.attacker
                    if battle.winner == 'defender':
                        survivors = len([u for u in battle.enemies if u.alive])
                        dmg = compute_player_damage(stage, survivors)
                        a["hp"] -= dmg
                        apply_battle_result(a, False)
                    elif battle.winner == 'attacker':
                        apply_battle_result(a, True)
                    else:
                        apply_battle_result(a, None)
                    continue
                if pb and pb.winner == 'defender':
                    survivors = len([u for u in pb.enemies if u.alive])
                    dmg = compute_player_damage(stage, survivors)
                    self.me["hp"] -= dmg
                    self.battle_log = f"野怪失败! 承受 {dmg} 伤害"
                    self.battle_result_text = f"失败 -{dmg}"
                    self.battle_result_color = RED
                else:
                    self.battle_log = "野怪胜利!"
                    self.battle_result_text = "胜利!"
                    self.battle_result_color = GOLD_COLOR
                    play_sfx("victory")
                    self._monster_drop(stage, rnd)
                self.battle_result_timer = 2.0
                continue

            if battle.is_mirror_battle:
                self._resolve_mirror_battle(battle, stage)
                continue

            self._resolve_pvp_pair(battle, stage)

        if pb:
            if pb.is_mirror_battle:
                owner_name = self.player_label(pb.mirror_owner) \
                    if pb.mirror_owner else "?"
                if pb.winner == 'attacker':
                    self.battle_log = f"镜像对战胜利! (来源: {owner_name})"
                    self.battle_result_text = "镜像胜利"
                    self.battle_result_color = MIRROR_COLOR
                elif pb.winner == 'defender':
                    survivors = len([u for u in pb.enemies if u.alive])
                    dmg = compute_player_damage(stage, survivors)
                    self.battle_log = f"镜像对战失败! 承受 {dmg} 伤害"
                    self.battle_result_text = f"镜像失败 -{dmg}"
                    self.battle_result_color = RED
                else:
                    self.battle_log = "镜像对战平局"
                    self.battle_result_text = "平局"
                    self.battle_result_color = GOLD_COLOR
            elif pb.winner == 'attacker':
                survivors = len([u for u in pb.allies if u.alive])
                self.battle_log = f"胜利! 我方存活 {survivors}"
                self.battle_result_text = "胜利"
                self.battle_result_color = GOLD_COLOR
                self.ai_assistant_say("win")
            elif pb.winner == 'defender':
                survivors = len([u for u in pb.enemies if u.alive])
                dmg = compute_player_damage(stage, survivors)
                self.battle_log = f"失败! 承受 {dmg} 伤害"
                self.battle_result_text = f"失败 -{dmg}"
                self.battle_result_color = RED
                self.ai_assistant_say("lose")
            else:
                self.battle_log = "平局!"
                self.battle_result_text = "平局"
                self.battle_result_color = GOLD_COLOR
            self.battle_result_timer = 2.0

    def _monster_drop(self, stage, rnd=1):
        drops = []
        gold_drop = random.randint(2, 4) + stage
        self.me["gold"] += gold_drop
        drops.append(f"+{gold_drop} 金")
        # 1-2 野怪回合100%掉落装备拆卸器（物品栏满则暂存溢出仓库，稍后自动回栏）
        if stage == 1 and rnd == 2:
            if len(self.me["items"]) < MAX_ITEM_BENCH:
                self.me["items"].append(make_special_item("disassembler"))
            else:
                self.me.setdefault("free_item_store", []).append(
                    make_special_item("disassembler"))
            drops.append("装备拆卸器")
        drop_count = 1
        if stage >= 3:
            drop_count = 2
        if stage >= 6:
            drop_count = 3
        for _ in range(drop_count):
            if len(self.me["items"]) < MAX_ITEM_BENCH:
                iid = random.choice(ITEM_IDS)
                self.me["items"].append(new_item(iid))
                drops.append(ITEMS[iid]["name"])
        # 极低概率掉落豹灵符/药灵符。
        if random.random() < 0.01 and len(self.me["items"]) < MAX_ITEM_BENCH:
            rk = random.choice(["leopard", "potion"])
            ri = make_rune_item(rk)
            self.me["items"].append(ri)
            drops.append(ri["name"])
        if random.random() < 0.6:
            if stage == 1:
                cost_pool = [1, 2]
            elif stage == 2:
                cost_pool = [1, 2, 3]
            elif stage == 3:
                cost_pool = [2, 3, 4]
            elif stage == 4:
                cost_pool = [3, 4, 5]
            else:
                cost_pool = [4, 5]
            pool = [c for c in CHAMPION_LIST
                    if c["cost"] in cost_pool and not c.get("no_shop")
                    and pool_remaining(c["name"]) > 0]
            if pool:
                weights = [pool_remaining(c["name"]) for c in pool]
                c = random.choices(pool, weights=weights, k=1)[0]
                empty = next((i for i, s in enumerate(self.me["bench"])
                              if s is None), None)
                if empty is not None:
                    u = make_unit_with_star(c["name"], 1)
                    if u:
                        self.me["bench"][empty] = u
                        consume_pool(c["name"], 1)
                        drops.append(champ_cn(c["name"]))
                else:
                    drops.append("(备战席满)")
        for ai in self.players:
            if ai["hp"] <= 0:
                continue
            ai_gold = random.randint(2, 4) + stage
            ai["gold"] += ai_gold
            # 1-2 野怪回合：AI 也发一个装备拆卸器（金铲铲对标）
            if stage == 1 and rnd == 2:
                if len(ai.get("items", [])) < MAX_ITEM_BENCH:
                    ai.setdefault("items", []).append(
                        make_special_item("disassembler"))
                else:
                    ai.setdefault("free_item_store", []).append(
                        make_special_item("disassembler"))
            for _ in range(drop_count):
                if len(ai.get("items", [])) < MAX_ITEM_BENCH:
                    iid = random.choice(ITEM_IDS)
                    ai.setdefault("items", []).append(new_item(iid))
            if random.random() < 0.6:
                if stage == 1:
                    cost_pool = [1, 2]
                elif stage == 2:
                    cost_pool = [1, 2, 3]
                elif stage == 3:
                    cost_pool = [2, 3, 4]
                elif stage == 4:
                    cost_pool = [3, 4, 5]
                else:
                    cost_pool = [4, 5]
                ai_pool = [c for c in CHAMPION_LIST
                           if c["cost"] in cost_pool
                           and not c.get("no_shop")
                           and pool_remaining(c["name"]) > 0]
                if ai_pool:
                    ai_weights = [pool_remaining(c["name"]) for c in ai_pool]
                    ai_c = random.choices(ai_pool, weights=ai_weights, k=1)[0]
                    ai_empty = next((i for i, s in enumerate(ai["bench"])
                                     if s is None), None)
                    if ai_empty is not None:
                        ai_u = make_unit_with_star(ai_c["name"], 1)
                        if ai_u:
                            ai["bench"][ai_empty] = ai_u
                            consume_pool(ai_c["name"], 1)
        self.battle_log = "掉落: " + " / ".join(drops)

    def _start_carousel(self):
        self.carousel_options = []
        rune_holder_assigned = False
        for _ in range(8):
            cost = random.choice([2, 3, 4])
            pool = [c for c in CHAMPION_LIST
                    if c.get("cost") == cost and not c.get("no_shop")
                    and pool_remaining(c["name"]) > 0]
            if not pool:
                pool = [c for c in CHAMPION_LIST
                        if not c.get("no_shop")
                        and pool_remaining(c["name"]) > 0]
            if not pool:
                break
            weights = [pool_remaining(c["name"]) for c in pool]
            champ = random.choices(pool, weights=weights, k=1)[0]
            star = 2 if (pool_remaining(champ["name"]) >= 3
                         and random.random() < 0.33) else 1
            u = make_unit_with_star(champ["name"], star)
            if u is None:
                continue
            iid = random.choice(ITEM_IDS)
            u.setdefault("items", []).append(new_item(iid))
            if (not rune_holder_assigned) and random.random() < 0.22:
                rk = random.choice(["leopard", "potion"])
                u["items"].append(make_rune_item(rk))
                rune_holder_assigned = True
            consume_pool(champ["name"], 3 if star >= 2 else 1)
            self.carousel_options.append(u)

        # 按血量从低到高排队（血量最低 = 排名最后 = 先选）
        alive_players = [self.me] + [ai for ai in self.players if ai["hp"] > 0]
        self.carousel_queue = sorted(
            alive_players,
            key=lambda p: (p["hp"], 0 if p is self.me else 1))

        # 先处理"血量比玩家低"的 AI（即排在玩家前面的）
        while self.carousel_queue and self.carousel_queue[0] is not self.me:
            ai = self.carousel_queue.pop(0)
            if not self.carousel_options:
                break
            target_traits = ai_detect_target_traits(ai)

            def score(u):
                s = u.get("star", 1) * 10 + u.get("cost", 1) * 2
                s += sum(6 for t in u.get("traits", [])
                         if t in target_traits)
                return s
            best_i = max(range(len(self.carousel_options)),
                         key=lambda i: score(self.carousel_options[i]))
            u = self.carousel_options.pop(best_i)
            empty = next((i for i, s in enumerate(ai["bench"]) if s is None), None)
            if empty is not None:
                ai["bench"][empty] = u
            else:
                ai["gold"] += u.get("cost", 1) * (3 ** (u.get("star", 1) - 1))
                return_pool(u["name"], 3 ** (u.get("star", 1) - 1))

        if not self.carousel_options:
            self.show_carousel = False
            self.carousel_timer = 0.0
            self.battle_log = "选秀回合 - 无剩余"
        else:
            self.show_carousel = True
            self.carousel_selected = -1
            self.carousel_timer = 15.0
            self.battle_log = "选秀回合 - 血量低者先选"

    def pick_carousel(self, idx):
        options = self.carousel_options
        selected_idx = idx if 0 <= idx < len(options) else -1
        if selected_idx >= 0:
            u = options[selected_idx]
            empty = next((i for i, s in enumerate(self.me["bench"]) if s is None), None)
            if empty is not None:
                self.me["bench"][empty] = u
            else:
                star = u.get("star", 1)
                count = 3 if star >= 2 else 1
                self.me["gold"] += u.get("cost", 1) * count
                return_pool(u["name"], count)
            options.pop(selected_idx)
            self.battle_log = f"选秀: {champ_cn(u['name'])}"
            play_sfx("coin")

        # 玩家出队
        if self.carousel_queue and self.carousel_queue[0] is self.me:
            self.carousel_queue.pop(0)

        # 剩余队列全是血量比玩家高的 AI，依次挑
        while self.carousel_queue:
            ai = self.carousel_queue.pop(0)
            if not options:
                break
            target_traits = ai_detect_target_traits(ai)

            def score(u):
                s = u.get("star", 1) * 10 + u.get("cost", 1) * 2
                s += sum(6 for t in u.get("traits", [])
                         if t in target_traits)
                return s
            best_i = max(range(len(options)), key=lambda i: score(options[i]))
            u = options.pop(best_i)
            empty = next((i for i, s in enumerate(ai["bench"]) if s is None), None)
            if empty is not None:
                ai["bench"][empty] = u
            else:
                ai["gold"] += u.get("cost", 1) * (3 ** (u.get("star", 1) - 1))
                return_pool(u["name"], 3 ** (u.get("star", 1) - 1))

        # 剩余全部返还英雄池
        for u in options:
            return_pool(u["name"], 3 ** (u.get("star", 1) - 1))

        self.show_carousel = False
        self.carousel_options = []

    def _add_bounty_shards(self):
        tc = count_traits(self.me)
        cnt = tc.get("Treasure", 0)
        if cnt < 3:
            return
        max_layer = 9 if cnt >= 8 else 8
        if self.bounty_layer_current >= max_layer:
            return
        won = self.me.get("win_streak", 0) > 0
        gain = _bounty_gain(cnt, won)
        if gain <= 0:
            return
        self.bounty_shards += gain
        while (self.bounty_shards >= 10
               and self.bounty_layer_current < max_layer):
            self.bounty_shards -= 10
            self.bounty_layer_current += 1
            if self.bounty_layer_current == 9:
                opts = _bounty_reward_options(9)
                self.bounty_layer_options = [copy.deepcopy(x) for x in random.sample(opts, min(3, len(opts)))]
            else:
                self.bounty_layer_options = [roll_bounty_reward(self.bounty_layer_current)]
            self.show_bounty_popup = True
            self.battle_log = (
                f"收菜系统：到达第 {self.bounty_layer_current} 层！")
            play_sfx("hex")
            break

    def _claim_bounty(self, choice_index=0):
        layer = self.bounty_layer_current
        if self.bounty_layer_options:
            choice_index = max(0, min(int(choice_index), len(self.bounty_layer_options) - 1))
            reward = self.bounty_layer_options[choice_index]
        else:
            reward = roll_bounty_reward(layer)
        apply_bounty_reward(self, reward)
        self.battle_log = (f"收宝离场：第 {layer} 层获得 "
                           f"{reward.get('name', '')}")
        self.bounty_layer_current = 1
        self.bounty_shards = 0
        self.bounty_layer_options = []
        self.show_bounty_popup = False
        play_sfx("coin")

    def _continue_bounty(self):
        self.show_bounty_popup = False
        self.bounty_layer_options = []
        self.battle_log = (
            f"深入寻宝：第 {self.bounty_layer_current} 层继续")

    def _advance_to_next_round(self):
        self.is_battle_phase = False
        self.battle_phase_resolved = False
        self.sync_lumber_marks()
        capture = self.me.pop("_bounty_capture_shards", 0)
        if capture:
            self.bounty_shards += capture
        self._add_bounty_shards()

        if self.is_multiplayer:
            if hasattr(self, "_saved_random_state"):
                random.setstate(self._saved_random_state)
                del self._saved_random_state
            # 推进 stage/rnd，与单机保持相同的回合循环(野怪/选秀/PVP)
            stage, rnd = self.stage
            if stage == 1:
                if rnd < STAGE1_ROUNDS:
                    self.stage = (1, rnd + 1)
                else:
                    self.stage = (2, 1)
            else:
                if rnd < STAGE_NORMAL_ROUNDS:
                    self.stage = (stage, rnd + 1)
                else:
                    self.stage = (stage + 1, 1)
            self.battles = []
            # 商店锁定：锁定后回合切换保留当前商店，不自动刷新
            if not self.shop_locked:
                self.refresh_shop()
            self.multiplayer_phase = "prep"
            self.phase_timer = 999999
            apply_income_and_xp(self.me)
            self.round_counter += 1
            # 羁绊强化回合（与单机一致，每 HEX_ROUND_INTERVAL 局一次）
            if self.round_counter >= HEX_ROUND_INTERVAL:
                self.round_counter = 0
                self.hex_choices = roll_hex_choices()
                if len(self.hex_choices) > 0:
                    self.show_hex_popup = True
            _rt = get_round_type(*self.stage)
            _rt_cn = {"augment": "强化", "monster": "野怪",
                      "carousel": "选秀", "pvp": "PVP"}.get(_rt, "")
            self.battle_log = f"第 {self.round_counter + 1} 局备战 ({_rt_cn})"
            if self.me["hp"] <= 0:
                self.me["hp"] = 0
                self.game_over = True
                self.game_over_text = "失败"
            if self.peer_hp <= 0:
                self.game_over = True
                self.game_over_text = "胜利!"
                play_sfx("victory")
            return

        stage, rnd = self.stage
        if stage == 1:
            if rnd < STAGE1_ROUNDS:
                self.stage = (1, rnd + 1)
            else:
                self.stage = (2, 1)
        else:
            if rnd < STAGE_NORMAL_ROUNDS:
                self.stage = (stage, rnd + 1)
            else:
                self.stage = (stage + 1, 1)
        for p in [self.me] + self.players:
              if p["hp"] > 0:
                   apply_income_and_xp(p)
        self.phase_timer = PREP_DURATION
        # 每回合自动回收满栏时被挤入溢出仓库的物品
        self._flush_free_item_store()
        if self.me["hp"] <= 0:
            self.me["hp"] = 0
            self.game_over = True
            self.game_over_text = "失败"
            return
        for ai in self.players:
            if ai["hp"] < 0:
                ai["hp"] = 0
        if not any(ai["hp"] > 0 for ai in self.players):
            self.game_over = True
            self.game_over_text = "胜利!"
            play_sfx("victory")
            return
        self.battles = []
        # 商店锁定：锁定后回合切换保留当前商店，不自动刷新
        if not self.shop_locked:
            self.refresh_shop()
        self.round_counter += 1
        if self.round_counter >= HEX_ROUND_INTERVAL:
            self.round_counter = 0
            self.hex_choices = roll_hex_choices()
            if len(self.hex_choices) > 0:
                self.show_hex_popup = True
        if getattr(self, "_congrats_mode", False):
            # 恭喜发财保底：阶段6结束存活单位100%大妮蔻 + 血量首次≤50大妮蔻
            _congrats_round_checks(self)
        save_game(self)


_TEXT_CACHE = {}
_TEXT_CACHE_MAX = 512


def draw_text(surface, text, x, y, font, color=TEXT_WHITE, align_center=False):
    try:
        key = (str(text), id(font), color)
        cached = _TEXT_CACHE.get(key)
        if cached is None:
            if len(_TEXT_CACHE) > _TEXT_CACHE_MAX:
                _TEXT_CACHE.clear()
            cached = font.render(str(text), True, color)
            _TEXT_CACHE[key] = cached
        rect = cached.get_rect()
        if align_center:
            rect.center = (x, y)
        else:
            rect.topleft = (x, y)
        surface.blit(cached, rect)
    except Exception as e:
        log_once("draw_text", e)


def draw_damage_text(surface, text, x, y, font, color):
    try:
        outline = font.render(str(text), True, (0, 0, 0))
        ow, oh = outline.get_width(), outline.get_height()
        for dx in (-2, -1, 0, 1, 2):
            for dy in (-2, -1, 0, 1, 2):
                if dx == 0 and dy == 0:
                    continue
                surface.blit(outline, (x - ow // 2 + dx, y - oh // 2 + dy))
        render = font.render(str(text), True, color)
        surface.blit(render, (x - render.get_width() // 2,
                              y - render.get_height() // 2))
    except Exception:
        pass


def draw_damage_icon(surface, cx, cy, size, color):
    try:
        pts = []
        for i in range(8):
            ang = math.pi / 4 * i - math.pi / 2
            r = size if i % 2 == 0 else size * 0.38
            pts.append((cx + math.cos(ang) * r, cy + math.sin(ang) * r))
        pygame.draw.polygon(surface, color, pts)
    except Exception:
        pass


def draw_shield_icon(surface, cx, cy, size, color):
    try:
        pts = [(cx, cy - size), (cx + size * 0.8, cy - size * 0.5),
               (cx + size * 0.8, cy + size * 0.2), (cx, cy + size),
               (cx - size * 0.8, cy + size * 0.2), (cx - size * 0.8, cy - size * 0.5)]
        pygame.draw.polygon(surface, color, pts)
        pygame.draw.polygon(surface, (30, 30, 30), pts, width=1)
    except Exception:
        pass


def draw_heal_icon(surface, cx, cy, size, color):
    try:
        w = max(2, size // 2)
        pygame.draw.rect(surface, color, (cx - w // 2, cy - size, w, size * 2))
        pygame.draw.rect(surface, color, (cx - size, cy - w // 2, size * 2, w))
    except Exception:
        pass


def draw_coin_icon(surface, cx, cy, r):
    try:
        pygame.draw.circle(surface, GOLD_DEEP, (cx, cy), r)
        pygame.draw.circle(surface, GOLD_COLOR, (cx, cy), r - 1)
        draw_text(surface, "$", cx, cy, get_font(int(r * 1.6)), GOLD_DEEP, True)
    except Exception:
        pass


def draw_item_icon(surface, rect, item):
    try:
        col = item.get("color", (200, 200, 200))
        is_comb = item.get("is_combined", False)
        bg = (70, 55, 20) if is_comb else (30, 30, 40)
        pygame.draw.rect(surface, bg, rect, border_radius=5)
        border_w = 3 if is_comb else 2
        pygame.draw.rect(surface, col, rect, width=border_w, border_radius=5)
        cx, cy = rect.centerx, rect.centery
        sz = min(rect.w, rect.h) // 4
        iid = item.get("id", "")
        if is_comb:
            pts = []
            for i in range(10):
                ang = math.pi / 5 * i - math.pi / 2
                r = sz if i % 2 == 0 else sz * 0.4
                pts.append((cx + math.cos(ang) * r, cy + math.sin(ang) * r))
            pygame.draw.polygon(surface, col, pts)
        elif iid == "sword":
            pygame.draw.line(surface, col, (cx - sz, cy + sz), (cx + sz, cy - sz), 3)
        elif iid == "bow":
            pygame.draw.arc(surface, col, (cx - sz, cy - sz, sz * 2, sz * 2), 0, math.pi * 1.3, 3)
        elif iid == "rod":
            pygame.draw.line(surface, col, (cx, cy - sz), (cx, cy + sz), 3)
            pygame.draw.circle(surface, col, (cx, cy - sz), 3)
        elif iid == "tear":
            pygame.draw.circle(surface, col, (cx, cy + 1), sz, 2)
        elif iid == "belt":
            pygame.draw.rect(surface, col, (cx - sz, cy - sz // 2, sz * 2, sz), 2)
        elif iid == "vest":
            pygame.draw.rect(surface, col, (cx - sz, cy - sz, sz * 2, sz * 2), 2, border_radius=3)
        elif iid == "cloak":
            pygame.draw.polygon(surface, col, [(cx - sz, cy + sz), (cx, cy - sz), (cx + sz, cy + sz)])
        elif iid == "glove":
            pygame.draw.circle(surface, col, (cx, cy), sz, 2)
            pygame.draw.circle(surface, col, (cx, cy), sz // 2, 1)
        else:
            draw_text(surface, item.get("name", "?")[:1], cx, cy,
                      get_font(int(rect.h * 0.6)), col, True)
    except Exception:
        pass


def draw_item_tooltip(screen, item, mouse_x, mouse_y, W, H, font_md, font_sm):
    name = item.get("name", "?")
    is_comb = item.get("is_combined", False)
    stats_txt = item_stat_text(item)
    name_surf = font_md.render(name, True, TEXT_WHITE)
    stats_surf = font_sm.render(stats_txt, True, TEXT_DIM)
    pad = 8
    box_w = max(name_surf.get_width(), stats_surf.get_width()) + pad * 2
    box_h = name_surf.get_height() + stats_surf.get_height() + pad * 3
    box_x = mouse_x + 16
    box_y = mouse_y - box_h - 8
    if box_x + box_w > W:
        box_x = W - box_w - 4
    if box_y < 4:
        box_y = mouse_y + 16
    if box_y + box_h > H:
        box_y = H - box_h - 4
    col = item.get("color", (200, 200, 200))
    r = pygame.Rect(box_x, box_y, box_w, box_h)
    try:
        s = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
        s.fill((15, 15, 25, 240))
        screen.blit(s, (box_x, box_y))
    except Exception:
        pass
    pygame.draw.rect(screen, col, r, width=2, border_radius=6)
    if is_comb:
        pygame.draw.rect(screen, GOLD_COLOR, r.inflate(-6, -6), width=1, border_radius=4)
    screen.blit(name_surf, (box_x + pad, box_y + pad))
    screen.blit(stats_surf, (box_x + pad, box_y + pad + name_surf.get_height() + 2))
    return r


def draw_item_path_popup(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos):
    selected_item = gs.item_path_id if isinstance(gs.item_path_id, dict) else None
    iid = selected_item.get("id") if selected_item else gs.item_path_id
    if selected_item and selected_item.get("is_combined"):
        try:
            ov = pygame.Surface((W, H), pygame.SRCALPHA)
            ov.fill((0, 0, 0, 232))
            screen.blit(ov, (0, 0))
        except Exception:
            pass
        item = selected_item
        pw, ph = int(W * 0.84), int(H * 0.34)
        px, py = (W - pw) // 2, (H - ph) // 2
        box = pygame.Rect(px, py, pw, ph)
        color = item.get("color", GOLD_COLOR)
        draw_panel(screen, box, (25, 29, 40), color, 12, 3)
        icon_size = min(76, int(ph * 0.35))
        icon_r = pygame.Rect(px + 18, py + 18, icon_size, icon_size)
        draw_item_icon(screen, icon_r, item)
        draw_text(screen, item.get("name", "装备详情"), icon_r.right + 16,
                  py + 28, font_lg, GOLD_COLOR)
        draw_text(screen, "合成装备 · 属性详情", icon_r.right + 16,
                  py + 58, font_sm, TEXT_DIM)
        # 成装详情：优先显示效果描述(神器/光明等)，再叠加数值属性
        stat_txt = item_stat_text(item)
        desc_txt = (item.get("desc") or "").strip()
        # 描述里已提到“人口”时，属性行不要重复再打印“人口+N”
        if desc_txt and "人口" in desc_txt and stat_txt and stat_txt != "无属性":
            stat_txt = " ".join(t for t in stat_txt.split() if "人口" not in t)
        disp_parts = []
        if desc_txt:
            disp_parts.append(desc_txt)
        if stat_txt and stat_txt != "无属性":
            disp_parts.append(stat_txt)
        if not disp_parts:
            disp_parts.append("无属性")
        draw_text(screen, "  ".join(disp_parts), px + 20, py + 118, font_md, TEXT_WHITE)
        draw_text(screen, "合成装备无法拆分；升星溢出装备会返还至物品栏。",
                  px + 20, py + 154, font_sm, TEXT_DIM)
        close_btn = pygame.Rect(W // 2 - 90, box.bottom - 62, 180, 44)
        draw_button(screen, close_btn, (60, 50, 20), GOLD_COLOR, 8)
        draw_text(screen, "关闭 (ESC)", close_btn.centerx, close_btn.centery,
                  font_md, GOLD_COLOR, True)
        return close_btn
    if iid is None or iid not in ITEMS:
        return None
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 240))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    base = ITEMS[iid]
    title_bg = pygame.Rect(int(W * 0.05), int(H * 0.03),
                           int(W * 0.90), int(H * 0.09))
    draw_panel(screen, title_bg, (28, 32, 42), base["color"], 10, 3)
    icon_size = int(title_bg.h - 16)
    icon_r = pygame.Rect(title_bg.x + 12, title_bg.y + 8, icon_size, icon_size)
    draw_item_icon(screen, icon_r,
                    {"id": iid, "color": base["color"],
                     "is_combined": False, "name": base["name"]})
    draw_text(screen, f"{base['name']} · 合成路径",
              title_bg.x + icon_size + 24, title_bg.y + 12,
              font_lg, GOLD_COLOR)
    draw_text(screen, "基础属性: " + item_stat_text({"stats": base.get("stats", {})}),
              title_bg.x + icon_size + 24, title_bg.y + 42,
              font_sm, TEXT_WHITE)
    draw_text(screen, "可与任意散件（含自己）合成，共 8 种",
              title_bg.x + icon_size + 24, title_bg.y + title_bg.h - 20,
              font_sm, TEXT_DIM)
    cols = 4
    rows = 2
    card_w = int(W * 0.215)
    card_h = int(H * 0.22)
    gap_x = int(W * 0.013)
    gap_y = int(H * 0.03)
    total_w = cols * card_w + (cols - 1) * gap_x
    total_h = rows * card_h + (rows - 1) * gap_y
    start_x = W // 2 - total_w // 2
    start_y = int(H * 0.16)
    for idx, other in enumerate(ITEM_IDS):
        col = idx % cols
        row = idx // cols
        x = start_x + col * (card_w + gap_x)
        y = start_y + row * (card_h + gap_y)
        r = pygame.Rect(int(x), int(y), int(card_w), int(card_h))
        other_base = ITEMS[other]
        hovered = r.collidepoint(mouse_pos)
        bg = (42, 48, 62) if hovered else (28, 32, 42)
        draw_panel(screen, r, bg, BORDER_LIGHT, 8, 2)
        pad = 10
        item_icon_size = int(card_h * 0.30)
        i1_r = pygame.Rect(r.x + pad, r.y + pad, item_icon_size, item_icon_size)
        i2_r = pygame.Rect(r.right - pad - item_icon_size, r.y + pad,
                            item_icon_size, item_icon_size)
        draw_item_icon(screen, i1_r,
                        {"id": iid, "color": base["color"],
                         "is_combined": False, "name": base["name"]})
        draw_item_icon(screen, i2_r,
                        {"id": other, "color": other_base["color"],
                         "is_combined": False, "name": other_base["name"]})
        draw_text(screen, "+", r.centerx, r.y + pad + item_icon_size // 2,
                  font_lg, TEXT_WHITE, True)
        arrow_y = r.y + pad + item_icon_size + 6
        draw_text(screen, "▼", r.centerx, arrow_y, font_sm, GOLD_COLOR, True)
        key = frozenset([iid, other])
        result = COMBINE_TABLE.get(key)
        if result:
            res_icon_size = int(card_h * 0.26)
            res_r = pygame.Rect(r.centerx - res_icon_size // 2,
                                 arrow_y + 12, res_icon_size, res_icon_size)
            draw_item_icon(screen, res_r,
                            {"id": "res", "color": result["color"],
                             "is_combined": True, "name": result["name"]})
            draw_text(screen, result["name"], r.centerx,
                      res_r.bottom + 8, font_sm, GOLD_COLOR, True)
            stats_txt = item_stat_text({"stats": result["stats"]})
            draw_text(screen, stats_txt[:16], r.centerx,
                      res_r.bottom + 24, font_sm, TEXT_DIM, True)
    close_btn = pygame.Rect(W // 2 - 90, start_y + total_h + 30, 180, 48)
    hovered_close = close_btn.collidepoint(mouse_pos)
    draw_button(screen, close_btn,
                (90, 75, 25) if hovered_close else (60, 50, 20),
                GOLD_COLOR, 10)
    draw_text(screen, "关闭 (ESC)", close_btn.centerx, close_btn.centery,
              font_md, GOLD_COLOR, True)
    return close_btn


def draw_panel(surface, rect, fill_col=PANEL_COLOR, border_col=BORDER_LIGHT,
               radius=10, border_w=2):
    try:
        # 底部阴影
        shadow = pygame.Rect(rect.x + 2, rect.y + 3, rect.w, rect.h)
        pygame.draw.rect(surface, (0, 0, 0, 60), shadow, border_radius=radius)
        pygame.draw.rect(surface, fill_col, rect, border_radius=radius)
        pygame.draw.rect(surface, border_col, rect, width=border_w, border_radius=radius)
    except Exception:
        pass


def draw_button(surface, rect, fill_col, border_col, radius=10):
    try:
        shadow = pygame.Rect(rect.x + 1, rect.y + 2, rect.w, rect.h)
        pygame.draw.rect(surface, (0, 0, 0, 80), shadow, border_radius=radius)
        pygame.draw.rect(surface, fill_col, rect, border_radius=radius)
        pygame.draw.rect(surface, border_col, rect, width=2, border_radius=radius)
    except Exception:
        pass


def draw_axe_icon(surface, cx, cy, size):
    """在 (cx, cy) 绘制小斧头角标（木柄 + 金色斧刃）。"""
    try:
        s2 = size / 2.0
        pygame.draw.line(surface, (140, 100, 60),
                         (int(cx - s2 * 0.7), int(cy + s2 * 0.7)),
                         (int(cx + s2 * 0.6), int(cy - s2 * 0.8)),
                         max(2, size // 6))
        pygame.draw.polygon(surface, (225, 200, 130),
                            [(int(cx - s2 * 0.2), int(cy - s2 * 1.1)),
                             (int(cx + s2 * 0.9), int(cy - s2 * 0.5)),
                             (int(cx + s2 * 0.9), int(cy - s2 * 0.1))])
        pygame.draw.polygon(surface, (250, 235, 175),
                            [(int(cx - s2 * 0.2), int(cy - s2 * 1.1)),
                             (int(cx + s2 * 0.9), int(cy - s2 * 0.5)),
                             (int(cx + s2 * 0.9), int(cy - s2 * 0.1))], 1)
    except Exception:
        pass


def draw_unit_cell(surface, r, unit, font_sm, font_md, is_drag_src=False):
    try:
        if unit.get("is_pseudo_bench_only"):
            # 纹章之书（备战席伪棋子）：书本样式
            pygame.draw.rect(surface, (58, 46, 18), r, border_radius=7)
            pygame.draw.rect(surface, (230, 190, 90), r, width=2, border_radius=7)
            draw_text(surface, "书", r.centerx, r.centery - 8,
                      font_sm, (250, 220, 140), align_center=True)
            draw_text(surface, "纹章之书", r.centerx, r.centery + 8,
                      font_sm, (250, 220, 140), align_center=True)
            return
        star = unit.get("star", 1)
        border = STAR_BORDER.get(star, STAR_BORDER[1])
        cost = unit.get("cost", 1)
        traits = unit.get("traits", [])
        bg = (28, 31, 44)
        if "BearRidge" in traits:
            bg = (48, 36, 24)
        elif "RuneLand" in traits:
            bg = (26, 36, 54)
        elif "Treasure" in traits:
            bg = (52, 42, 14)
        pygame.draw.rect(surface, bg, r, border_radius=7)
        if "BearRidge" in traits:
            pygame.draw.rect(surface, BEAR_COLOR, r.inflate(3, 3), width=2, border_radius=8)
        elif "RuneLand" in traits:
            pygame.draw.rect(surface, RUNE_COLOR, r.inflate(3, 3), width=2, border_radius=8)
        elif "Treasure" in traits:
            pygame.draw.rect(surface, TREASURE_COLOR, r.inflate(3, 3), width=2, border_radius=8)
        pygame.draw.rect(surface, border, r, width=2, border_radius=7)
        if is_drag_src:
            return
        name_col = COST_COLORS.get(cost, TEXT_WHITE)
        _n = champ_cn(unit.get("name", "?"))
        draw_text(surface, _n[:3] if len(_n) > 3 else _n,
                  r.centerx, r.centery - 4, font_sm, name_col, align_center=True)
        draw_text(surface, f"{'★' * star}", r.centerx, r.centery + 9,
                  font_sm, border, align_center=True)
        role = unit.get("role", "warrior")
        role_col = ROLE_COLORS.get(role, TEXT_DIM)
        role_txt = ROLE_SHORT.get(role, "?")
        badge = pygame.Rect(r.x + 2, r.y + 2, 14, 14)
        pygame.draw.rect(surface, (10, 10, 16), badge, border_radius=4)
        pygame.draw.rect(surface, role_col, badge, width=1, border_radius=4)
        draw_text(surface, role_txt, badge.centerx, badge.centery, font_sm, role_col, True)
        # 巨斧选择器标记：棋盘角落绘制巨斧小图标
        if unit.get("is_lumber_chief"):
            draw_axe_icon(surface, r.right - 8, r.y + 8, 14)
        items = unit.get("items", [])
        if items:
            i_size = 10
            ix = r.right - 3 - i_size
            iy = r.bottom - 3 - i_size
            for item in reversed(items[-3:]):
                ir = pygame.Rect(ix, iy, i_size, i_size)
                draw_item_icon(surface, ir, item)
                ix -= (i_size + 2)
    except Exception:
        pass


def draw_battle_unit(screen, unit, font_sm, is_ally):
    cx, cy = int(unit.x), int(unit.y)
    size = unit.size
    is_chief = bool(unit.base.get("is_lumber_chief"))
    if is_chief:
        size = int(size * 1.2)
    star = unit.base.get("star", 1)
    border_col = STAR_BORDER.get(star, STAR_BORDER[1])
    if unit.is_summon:
        border_col = (180, 230, 255)
    if unit.flash_timer > 0:
        body_col = WHITE_FLASH
    else:
        body_col = (50, 85, 150) if is_ally else (150, 55, 55)
    if unit.skill_flash_timer > 0:
        pulse_t = unit.skill_flash_timer / 0.6
        r = int(size * 0.7 + (1 - pulse_t) * size * 0.6)
        try:
            pygame.draw.circle(screen, (255, 230, 100), (cx, cy), r,
                               max(2, int(6 * pulse_t)))
        except Exception:
            pass
        body_col = (255, 220, 100)
    if unit.summon_flash_timer > 0:
        try:
            r = int(size * 0.8 + (1.0 - unit.summon_flash_timer) * size * 1.2)
            pygame.draw.circle(screen, (150, 220, 255), (cx, cy), r, 3)
        except Exception:
            pass
    rect = pygame.Rect(cx - size // 2, cy - size // 2, size, size)
    shadow = pygame.Rect(rect.x + 2, rect.y + 3, size, size)
    pygame.draw.rect(screen, (0, 0, 0), shadow, border_radius=8)
    pygame.draw.rect(screen, body_col, rect, border_radius=8)
    pygame.draw.rect(screen, border_col, rect, width=3, border_radius=8)
    if is_chief:
        draw_axe_icon(screen, rect.right - 8, rect.y + 8, 14)
    if unit.shield > 0:
        try:
            pygame.draw.rect(screen, SHIELD_COLOR, rect, width=2, border_radius=8)
        except Exception:
            pass
    if unit.alive and unit.base.get("max_mana", 0) > 0:
        mana_ratio = unit.current_mana / max(1, unit.base["max_mana"])
        if mana_ratio > 0.05:
            ring_r = size // 2 + 6
            segments = 24
            filled = int(segments * mana_ratio)
            for s in range(filled):
                ang0 = -math.pi / 2 + (s / segments) * math.pi * 2
                ang1 = -math.pi / 2 + ((s + 1) / segments) * math.pi * 2
                try:
                    p1 = (cx + math.cos(ang0) * ring_r,
                          cy + math.sin(ang0) * ring_r)
                    p2 = (cx + math.cos(ang1) * ring_r,
                          cy + math.sin(ang1) * ring_r)
                    pygame.draw.line(screen, BLUE_MANA, p1, p2, 2)
                except Exception:
                    pass
            if unit.current_mana >= unit.base["max_mana"]:
                try:
                    pygame.draw.circle(screen, (140, 220, 255),
                                       (cx, cy), ring_r + 2, 2)
                except Exception:
                    pass
    if unit.mana_regen > 0:
        draw_text(screen, "法", cx + size // 2 - 8, cy - size // 2 + 4,
                  font_sm, (100, 220, 255), align_center=True)
    _n = champ_cn(unit.base["name"])
    draw_text(screen, _n[:3] if len(_n) > 3 else _n,
              cx, cy - size // 2 - 10, font_sm, TEXT_WHITE, align_center=True)
    draw_text(screen, f"{star}星", cx, cy, font_sm, border_col, align_center=True)
    hp_ratio = max(0, unit.current_hp) / max(1, unit.base["hp"])
    bar_w = size
    bar_y = cy + size // 2 + 3
    pygame.draw.rect(screen, (20, 20, 25),
                     (cx - bar_w // 2 - 1, bar_y - 1, bar_w + 2, 8), border_radius=2)
    pygame.draw.rect(screen, (40, 40, 40),
                     (cx - bar_w // 2, bar_y, bar_w, 6), border_radius=2)
    hp_col = GREEN_HP if is_ally else RED
    pygame.draw.rect(screen, hp_col,
                     (cx - bar_w // 2, bar_y, int(bar_w * hp_ratio), 6),
                     border_radius=2)
    if unit.shield > 0:
        shield_ratio = min(1.0, unit.shield / max(1, unit.base["hp"]))
        pygame.draw.rect(screen, SHIELD_COLOR,
                         (cx - bar_w // 2, bar_y - 2,
                          int(bar_w * shield_ratio), 2), border_radius=1)
    mana_ratio = unit.current_mana / max(1, unit.base["max_mana"])
    mana_y = bar_y + 7
    pygame.draw.rect(screen, (25, 25, 40),
                     (cx - bar_w // 2, mana_y, bar_w, 4), border_radius=2)
    if mana_ratio > 0:
        pygame.draw.rect(screen, BLUE_MANA,
                         (cx - bar_w // 2, mana_y, int(bar_w * mana_ratio), 4),
                         border_radius=2)
    if unit.damage_dealt > 0:
        try:
            txt = font_sm.render(str(int(unit.damage_dealt)), True, (255, 240, 150))
            tw, th = txt.get_size()
            icon_size = 5
            total_w = icon_size * 2 + 4 + tw
            total_h = max(th, icon_size * 2)
            bx = cx + size // 2 - total_w - 4
            by = cy - size // 2 - total_h - 4
            bg = pygame.Rect(bx - 3, by - 2, total_w + 6, total_h + 4)
            pygame.draw.rect(screen, (20, 15, 5), bg, border_radius=3)
            pygame.draw.rect(screen, (255, 180, 60), bg, width=1, border_radius=3)
            draw_damage_icon(screen, bx + icon_size, by + total_h // 2,
                             icon_size, (255, 200, 60))
            screen.blit(txt, (bx + icon_size * 2 + 4, by + (total_h - th) // 2))
        except Exception:
            pass


def draw_battle_selector(screen, gs, font_sm, W, H):
    if len(gs.battles) <= 1:
        return []
    n = len(gs.battles)
    btn_h = 26
    gap = 4
    btn_w = min(140, (W - 40 - (n - 1) * gap) / max(1, n))
    total_w = n * btn_w + (n - 1) * gap
    start_x = W // 2 - total_w // 2
    y = H * 0.115
    rects = []
    for i, battle in enumerate(gs.battles):
        x = start_x + i * (btn_w + gap)
        r = pygame.Rect(int(x), int(y), int(btn_w), btn_h)
        is_current = (i == gs.watched_battle_idx)
        if is_current:
            border_col, bg_col = (255, 240, 120), (70, 65, 45)
        elif battle.finished:
            border_col = (100, 200, 100) if battle.winner == 'attacker' else \
                         (200, 100, 100) if battle.winner == 'defender' else (150, 150, 150)
            bg_col = (35, 35, 45)
        else:
            border_col, bg_col = (90, 120, 170), (40, 50, 70)
        draw_panel(screen, r, bg_col, border_col, 5, 2)
        if battle.is_player_battle:
            pygame.draw.rect(screen, (255, 200, 60), (r.x + 1, r.y + 3, 3, r.h - 6))

        if battle.is_mirror_battle:
            owner = gs.player_label(battle.mirror_owner) if battle.mirror_owner else "?"
            label = f"{gs.player_label(battle.attacker)} 镜像·{owner}"
            pygame.draw.rect(screen, MIRROR_COLOR,
                             (r.right - 3, r.y + 3, 3, r.h - 6))
        elif battle.is_monster_battle:
            label = f"{gs.player_label(battle.attacker)}·野怪"
        else:
            a_id = gs.player_label(battle.attacker)
            b_id = gs.player_label(battle.defender)
            label = f"{a_id} 对 {b_id}"
        if battle.finished:
            label += " ✓"
        draw_text(screen, label, r.centerx, r.centery, font_sm, (230, 230, 230), True)
        rects.append((r, i))
    return rects


def draw_damage_report(screen, gs, font_lg, font_md, font_sm, W, H):
    battle = gs.player_battle() or gs.current_battle()
    if battle is None:
        return
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 200))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    panel_w = W * 0.94
    panel_h = min(H * 0.78, 520)
    px = W // 2 - panel_w // 2
    py = H // 2 - panel_h // 2
    draw_panel(screen, pygame.Rect(px, py, panel_w, panel_h),
               (22, 24, 32), (80, 90, 120), 12, 2)
    if battle.is_monster_battle:
        title, title_col = "野怪战斗", GOLD_COLOR
    elif battle.is_mirror_battle:
        owner = gs.player_label(battle.mirror_owner) if battle.mirror_owner else "?"
        if battle.winner == 'attacker':
            title, title_col = f"镜像胜利 (镜像: {owner})", MIRROR_COLOR
        elif battle.winner == 'defender':
            title, title_col = f"镜像失败 (镜像: {owner})", RED
        else:
            title, title_col = "镜像平局", TEXT_WHITE
    elif battle.is_player_battle:
        if battle.winner == 'attacker':
            title, title_col = "胜利", GOLD_COLOR
        elif battle.winner == 'defender':
            title, title_col = "失败", RED
        else:
            title, title_col = "平局", TEXT_WHITE
    else:
        title = f"{gs.player_label(battle.attacker)} 对 {gs.player_label(battle.defender)}"
        title_col = TEXT_WHITE
    draw_text(screen, "战斗结算", W // 2, py + 22, font_lg, TEXT_WHITE, True)
    _title_y = py + 22 + font_lg.get_height() // 2 + font_md.get_height() // 2 + 8
    draw_text(screen, title, W // 2, _title_y, font_md, title_col, True)
    pad = 14
    _team_label_y = _title_y + font_md.get_height() // 2 + 12
    col_w = (panel_w - pad * 3) / 2
    left_x = px + pad
    right_x = px + pad + col_w + pad
    a_label = "我方" if battle.is_player_battle else gs.player_label(battle.attacker)
    if battle.is_mirror_battle:
        d_label = "镜像"
    elif battle.is_player_battle:
        d_label = "敌方"
    else:
        d_label = gs.player_label(battle.defender)
    draw_panel(screen, pygame.Rect(left_x, _team_label_y, col_w, 24),
               (30, 60, 110), (60, 120, 180), 5, 1)
    draw_text(screen, a_label, left_x + col_w // 2, _team_label_y + 12, font_md, BLUE_MANA, True)
    draw_panel(screen, pygame.Rect(right_x, _team_label_y, col_w, 24),
               (110, 40, 40), (180, 60, 60), 5, 1)
    draw_text(screen, d_label, right_x + col_w // 2, _team_label_y + 12, font_md, RED, True)
    header_y = _team_label_y + 24 + font_sm.get_height() // 2 + 4
    icon_size = 6
    for base_x in (left_x, right_x):
        draw_text(screen, "英雄", base_x + 6, header_y, font_sm, TEXT_DIM)
        draw_damage_icon(screen, base_x + col_w * 0.42 + icon_size,
                         header_y + 7, icon_size, (255, 200, 60))
        draw_text(screen, "伤害", base_x + col_w * 0.45, header_y, font_sm, GOLD_COLOR)
        draw_shield_icon(screen, base_x + col_w * 0.64 + icon_size,
                         header_y + 7, icon_size, (220, 100, 100))
        draw_text(screen, "承伤", base_x + col_w * 0.67, header_y, font_sm, RED)
        draw_heal_icon(screen, base_x + col_w * 0.86 + icon_size,
                       header_y + 7, icon_size, HEAL_COLOR)
        draw_text(screen, "治疗", base_x + col_w * 0.89, header_y, font_sm, HEAL_COLOR)
    row_h = 22
    max_rows = 8

    def render_team(units, base_x):
        sorted_u = sorted(units, key=lambda u: -u.damage_dealt)[:max_rows]
        y = header_y + 24
        for u in sorted_u:
            star = u.base.get("star", 1)
            name = champ_cn(u.base.get("name", "?"))[:4]
            cost = u.base.get("cost", 1)
            name_col = COST_COLORS.get(cost, TEXT_WHITE)
            border = STAR_BORDER.get(star, STAR_BORDER[1])
            pygame.draw.rect(screen, border, (base_x + 4, y + 2, 12, 12),
                             width=2, border_radius=2)
            draw_text(screen, f"{name} {star}星", base_x + 20, y, font_sm, name_col)
            draw_text(screen, str(int(u.damage_dealt)),
                      base_x + col_w * 0.45, y, font_sm, (255, 220, 100))
            draw_text(screen, str(int(u.damage_taken)),
                      base_x + col_w * 0.67, y, font_sm, (255, 120, 120))
            heal_val = int(u.heal_done)
            heal_col = HEAL_COLOR if heal_val > 0 else (90, 90, 90)
            draw_text(screen, str(heal_val),
                      base_x + col_w * 0.89, y, font_sm, heal_col)
            y += row_h
        if not sorted_u:
            draw_text(screen, "(无单位)", base_x + 20, header_y + 24, font_sm, TEXT_DIM)
        return y

    render_team(battle.allies, left_x)
    render_team(battle.enemies, right_x)
    total_a = sum(int(u.damage_dealt) for u in battle.allies)
    total_d = sum(int(u.damage_dealt) for u in battle.enemies)
    total_heal_a = sum(int(u.heal_done) for u in battle.allies)
    total_heal_d = sum(int(u.heal_done) for u in battle.enemies)
    bottom_y = py + panel_h - 40
    draw_text(screen, f"总伤害: {total_a}", left_x + col_w * 0.42, bottom_y,
              font_sm, GOLD_COLOR, True)
    draw_text(screen, f"总伤害: {total_d}", right_x + col_w * 0.42, bottom_y,
              font_sm, GOLD_COLOR, True)
    draw_text(screen, f"总治疗: {total_heal_a}", left_x + col_w * 0.85, bottom_y,
              font_sm, HEAL_COLOR, True)
    draw_text(screen, f"总治疗: {total_heal_d}", right_x + col_w * 0.85, bottom_y,
              font_sm, HEAL_COLOR, True)
    t = max(0, gs.post_battle_timer)
    draw_text(screen, f"下一回合 {t:.1f}秒  ·  点击任意处继续",
              W // 2, py + panel_h - 16, font_md, GOLD_COLOR, True)


def draw_battle_bench_panel(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos):
    """战斗内备战席面板：备战席 / 物品栏 / 出售区。
    返回 (bench_rects, item_rects, sell_rect)。"""
    bar_h = 150
    bar_y = H - bar_h
    panel_w = int(W * 0.27)
    panel_x = 10
    panel_y = int(H * 0.105)
    panel_h = bar_y - panel_y - 12
    try:
        s = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        s.fill((14, 16, 24, 238))
        screen.blit(s, (panel_x, panel_y))
        pygame.draw.rect(screen, (78, 88, 120),
                         (panel_x, panel_y, panel_w, panel_h),
                         width=2, border_radius=12)
    except Exception:
        pass
    draw_text(screen, "战斗备战席", panel_x + 12, panel_y + 6,
              font_md, GOLD_COLOR)
    bench_rects = []
    cell = max(40, min(54, (panel_h - 170) // 4))
    gap = 6
    start_y = panel_y + 38
    for i in range(8):
        col = i % 2
        row = i // 2
        bx = panel_x + 12 + col * (cell + gap)
        by = start_y + row * (cell + gap + 8)
        r = pygame.Rect(bx, by, cell, cell)
        hover = r.collidepoint(mouse_pos)
        pygame.draw.rect(screen, (46, 50, 66) if hover else (30, 33, 44),
                         r, border_radius=8)
        pygame.draw.rect(screen, (70, 78, 100), r, width=1, border_radius=8)
        u = gs.me["bench"][i]
        if u is not None:
            draw_unit_cell(screen, r, u, font_sm, font_md)
        bench_rects.append((r, i))
    item_y = start_y + 4 * (cell + gap + 8) + 8
    draw_text(screen, "物品栏(拖到备战席/棋盘使用)", panel_x + 12, item_y - 16,
              font_sm, TEXT_DIM)
    item_rects = []
    isz = 38
    igap = 5
    for i in range(MAX_ITEM_BENCH):
        col = i % 5
        row = i // 5
        ix = panel_x + 12 + col * (isz + igap)
        iy = item_y + row * (isz + igap)
        r = pygame.Rect(ix, iy, isz, isz)
        hover = r.collidepoint(mouse_pos)
        pygame.draw.rect(screen, (40, 44, 58) if hover else (24, 26, 36),
                         r, border_radius=6)
        pygame.draw.rect(screen, (60, 68, 88), r, width=1, border_radius=6)
        if i < len(gs.me["items"]):
            if i == gs.dragging_item_idx:
                pygame.draw.rect(screen, HIGHLIGHT, r, width=2, border_radius=6)
            else:
                draw_item_icon(screen, r, gs.me["items"][i])
        item_rects.append(r)
    sell_y = item_y + 2 * (isz + igap) + 12
    sell_rect = pygame.Rect(panel_x + 12, sell_y, panel_w - 24, 38)
    hover_sell = sell_rect.collidepoint(mouse_pos)
    pygame.draw.rect(screen, (82, 36, 36) if hover_sell else (56, 26, 26),
                     sell_rect, border_radius=8)
    pygame.draw.rect(screen, SELL_RED, sell_rect, width=2, border_radius=8)
    draw_text(screen, "出售 (拖到这里)", sell_rect.centerx, sell_rect.centery,
              font_sm, (255, 200, 200), align_center=True)
    return bench_rects, item_rects, sell_rect


def draw_battle_shop_bar(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos):
    if gs.viewing_player_idx != -1:
        return [], None, None, None

    bar_h = 150
    bar_y = H - bar_h
    try:
        s = pygame.Surface((W, bar_h), pygame.SRCALPHA)
        s.fill((10, 12, 18, 225))
        screen.blit(s, (0, bar_y))
    except Exception:
        pass
    pygame.draw.line(screen, BORDER_LIGHT, (0, bar_y), (W, bar_y), 2)

    top_y = bar_y + 6
    gold_box = pygame.Rect(8, top_y, 130, 28)
    draw_panel(screen, gold_box, (45, 35, 10), GOLD_DEEP, 6, 2)
    draw_coin_icon(screen, gold_box.x + 16, gold_box.centery, 8)
    draw_text(screen, str(gs.me["gold"]),
              gold_box.x + 34, gold_box.centery, font_sm, GOLD_COLOR)

    lv_box = pygame.Rect(gold_box.right + 8, top_y, 170, 28)
    draw_panel(screen, lv_box, PANEL_DARK, BORDER_LIGHT, 6, 2)
    draw_text(screen, f"Lv {gs.me['level']}",
              lv_box.x + 8, lv_box.centery, font_sm, BLUE_MANA)
    if gs.me["level"] < MAX_LEVEL:
        xp = gs.me.get("xp", 0)
        need = gs.me.get("xp_next", 999)
        ratio = min(1.0, xp / max(1, need))
        bar_r = pygame.Rect(lv_box.x + 62, lv_box.centery - 4,
                            lv_box.w - 70, 8)
        pygame.draw.rect(screen, (30, 32, 42), bar_r, border_radius=3)
        if ratio > 0:
            pygame.draw.rect(screen, BLUE_MANA,
                             (bar_r.x, bar_r.y, int(bar_r.w * ratio), bar_r.h),
                             border_radius=3)
        pygame.draw.rect(screen, BORDER_LIGHT, bar_r, width=1, border_radius=3)
    else:
        draw_text(screen, "满级", lv_box.right - 40, lv_box.centery,
                  font_sm, GOLD_COLOR)

    refresh_rect = pygame.Rect(lv_box.right + 8, top_y, 120, 28)
    draw_button(screen, refresh_rect, BLUE_DEEP, BLUE, 6)
    draw_text(screen, f"D牌 {REFRESH_COST}金", refresh_rect.centerx,
              refresh_rect.centery, font_sm, TEXT_WHITE, True)

    levelup_rect = pygame.Rect(refresh_rect.right + 8, top_y, 120, 28)
    if gs.me["level"] >= MAX_LEVEL:
        draw_button(screen, levelup_rect, (55, 55, 60), (100, 100, 100), 6)
        draw_text(screen, "满级", levelup_rect.centerx, levelup_rect.centery,
                  font_sm, TEXT_DIM, True)
    else:
        draw_button(screen, levelup_rect, BLUE_DEEP, BLUE, 6)
        draw_text(screen, f"升级 {BUY_XP_COST}金", levelup_rect.centerx,
                  levelup_rect.centery, font_sm, TEXT_WHITE, True)

    draw_text(screen, "战斗中可 D 牌 / 升级 · 买入的棋子进入备战席",
              levelup_rect.right + 14, top_y + 8, font_sm, TEXT_DIM)

    shop_y = bar_y + 42
    shop_h = bar_h - 52
    lock_w = 76
    shop_gap = 6
    shop_area_w = W - 20 - lock_w - 4 * shop_gap
    shop_w = shop_area_w / 5

    lock_rect = draw_shop_lock(screen, W - lock_w + 8, shop_y + 4,
                               gs.shop_locked, font_sm)

    shop_rect_list = []
    for i in range(5):
        sx = 10 + i * (shop_w + shop_gap)
        r = pygame.Rect(sx, shop_y, shop_w, shop_h)
        champ = gs.shop[i]
        cost = champ["cost"] if champ else 1
        bg_col = COST_BG.get(cost, (35, 38, 48))
        draw_panel(screen, r, bg_col, BORDER_LIGHT, 8, 2)
        if champ:
            pygame.draw.rect(screen, COST_COLORS.get(cost, TEXT_WHITE),
                             (r.x, r.y, r.w, 4), border_radius=2)
            safe_unit(champ)
            traits = champ.get("traits", [])
            if "BearRidge" in traits:
                pygame.draw.rect(screen, BEAR_COLOR, r, width=2, border_radius=8)
            elif "RuneLand" in traits:
                pygame.draw.rect(screen, RUNE_COLOR, r, width=2, border_radius=8)
            elif "Treasure" in traits:
                pygame.draw.rect(screen, TREASURE_COLOR, r, width=2, border_radius=8)
            role = champ.get("role", "warrior")
            role_col = ROLE_COLORS.get(role, TEXT_DIM)
            role_rect = pygame.Rect(r.x + 3, r.y + 6, 20, 18)
            pygame.draw.rect(screen, (15, 15, 20), role_rect, border_radius=3)
            pygame.draw.rect(screen, role_col, role_rect, width=1, border_radius=3)
            draw_text(screen, ROLE_SHORT.get(role, "?"),
                      role_rect.centerx, role_rect.centery, font_sm, role_col, True)
            draw_text(screen, champ_cn(champ["name"])[:5], r.centerx,
                      r.y + shop_h * 0.32, font_md,
                      COST_COLORS.get(cost, TEXT_WHITE), True)
            _role = champ.get("role", "warrior")
            _all_t = list(traits) + [ROLE_TO_CLASS_TRAIT.get(_role, "")]
            _all_t = [t for t in _all_t if t][:3]
            tstr = "·".join(trait_short_cn(t) for t in _all_t)
            draw_text(screen, tstr, r.centerx, r.y + shop_h * 0.58,
                      font_sm, TEXT_DIM, True)
            draw_text(screen, f"{cost}金", r.centerx,
                      r.y + shop_h * 0.84, font_md, GOLD_COLOR, True)
            owned = count_unit_owned(gs.me, champ["name"], 1)
            if owned > 0:
                br = pygame.Rect(r.right - 34, r.y + 6, 30, 16)
                pygame.draw.rect(screen, (40, 60, 40), br, border_radius=3)
                pygame.draw.rect(screen, GREEN_HP, br, width=1, border_radius=3)
                draw_text(screen, f"x{owned}", br.centerx, br.centery,
                          font_sm, GREEN_HP, True)
        shop_rect_list.append((r, i))
    return shop_rect_list, refresh_rect, levelup_rect, lock_rect


def draw_battle(screen, gs, font_lg, font_md, font_sm, font_dmg, W, H):
    battle = gs.current_battle()
    # 己方战斗单位命中区（供战斗内点击详情/拖拽装备使用）
    gs._battle_ally_hit_rects = []
    if battle is not None:
        for u in battle.allies:
            if u.alive and getattr(u, "source_unit", None) is not None \
                    and getattr(u, "owner_player", None) is gs.me:
                sz = u.size
                gs._battle_ally_hit_rects.append(
                    (pygame.Rect(int(u.x - sz // 2), int(u.y - sz // 2),
                                 sz, sz), u))
    if battle is None:
        return []
    mid_y = H * 0.50
    try:
        pygame.draw.line(screen, (50, 55, 70), (0, mid_y), (W, mid_y), 2)
    except Exception:
        pass
    if not gs.battle_phase_resolved:
        t_left = max(0, gs.battle_phase_timer)
        col = RED if t_left <= 5 else ORANGE_TIMER if t_left <= 10 else TEXT_WHITE
        big_font = get_font(40)
        draw_text(screen, f"{t_left:.1f}", W // 2, H * 0.02, big_font, col, True)
        if getattr(gs, "_overtime_active", False):
            draw_text(screen, "⚔ 加时赛 · 双方残血强化", W // 2, H * 0.055, font_sm, (255, 120, 120), True)
        else:
            draw_text(screen, "战斗倒计时", W // 2, H * 0.055, font_sm, TEXT_DIM, True)
    else:
        draw_text(screen, "战斗结束", W // 2, H * 0.03, font_lg, GOLD_COLOR, True)
    if battle.is_monster_battle:
        title = f"{gs.player_label(battle.attacker)} · 野怪回合"
    elif battle.is_mirror_battle:
        owner = gs.player_label(battle.mirror_owner) if battle.mirror_owner else "?"
        title = f"{gs.player_label(battle.attacker)}  镜像 · {owner}"
    else:
        title = f"{gs.player_label(battle.attacker)}  对  {gs.player_label(battle.defender)}"
    draw_text(screen, title, W // 2, H * 0.088, font_md, TEXT_WHITE, True)
    draw_text(screen, "敌方", W * 0.5, H * 0.14, font_sm, RED, True)
    draw_text(screen, "我方", W * 0.5, H * 0.97, font_sm, BLUE_MANA, True)

    buckets = {"attack_line": [], "shockwave": [], "cast_pulse": [],
               "skill_name": [], "screen_flash": [], "damage_pop": [],
               "trait_activate": [], "ultimate_cross": []}
    for eff in battle.effects:
        buckets.get(eff["type"], []).append(eff)

    for eff in buckets["attack_line"]:
        try:
            col = CRIT_COLOR if eff.get("crit") else (255, 180, 80)
            width = 2 if eff.get("ranged") else 3
            pygame.draw.line(screen, col, eff["p1"], eff["p2"], width)
            if eff.get("ranged"):
                mx = (eff["p1"][0] + eff["p2"][0]) // 2
                my = (eff["p1"][1] + eff["p2"][1]) // 2
                pygame.draw.circle(screen, (255, 220, 150), (mx, my), 3)
        except Exception:
            pass
    for eff in buckets["shockwave"]:
        if eff.get("delay", 0) > 0:
            continue
        progress = 1 - eff["life"] / eff["max_life"]
        r = int(eff["r1"] * progress)
        if r >= 2:
            width = max(2, int(12 * eff["life"] / eff["max_life"]))
            try:
                pygame.draw.circle(screen, eff["color"],
                                   (int(eff["x"]), int(eff["y"])), r, width)
            except Exception:
                pass
    for eff in buckets["ultimate_cross"]:
        ratio = eff["life"] / max(0.01, eff["max_life"])
        cx, cy = int(eff["x"]), int(eff["y"])
        length = int(max(screen.get_width(), screen.get_height()) * (1.0 - ratio))
        width = max(2, int(10 * ratio))
        col = eff.get("color", (255, 220, 80))
        try:
            pygame.draw.line(screen, col, (cx-length, cy), (cx+length, cy), width)
            pygame.draw.line(screen, col, (cx, cy-length), (cx, cy+length), width)
            pygame.draw.circle(screen, col, (cx, cy),
                               max(6, int(45*(1.0-ratio))), 3)
        except Exception:
            pass
    for unit in battle.enemies:
        if unit.alive:
            draw_battle_unit(screen, unit, font_sm, is_ally=False)
    for unit in battle.allies:
        if unit.alive:
            draw_battle_unit(screen, unit, font_sm, is_ally=True)
    for eff in buckets["cast_pulse"]:
        progress = 1 - eff["life"] / eff["max_life"]
        r = int(eff["r0"] + (eff["r1"] - eff["r0"]) * progress)
        if r < 2:
            continue
        a_ratio = eff["life"] / eff["max_life"]
        try:
            s = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
            a = int(200 * a_ratio)
            col = (eff["color"][0], eff["color"][1], eff["color"][2], a)
            pygame.draw.circle(s, col, (r, r), r)
            pygame.draw.circle(s, (255, 255, 255, int(a * 0.7)), (r, r),
                               max(1, r // 2))
            screen.blit(s, (int(eff["x"]) - r, int(eff["y"]) - r))
        except Exception:
            pass
    for eff in buckets["skill_name"]:
        a_ratio = eff["life"] / eff["max_life"]
        col = eff["color"]
        if a_ratio < 0.5:
            col = tuple(int(c * a_ratio * 2) for c in col)
        font_use = font_dmg if eff.get("is_ult") else font_sm
        draw_text(screen, eff["text"], int(eff["x"]), int(eff["y"]),
                  font_use, col, align_center=True)
    for eff in buckets["trait_activate"]:
        ratio = eff["life"] / eff["max_life"]
        if ratio > 0.75:
            a = (1.0 - ratio) * 4.0
        elif ratio < 0.40:
            a = ratio / 0.40
        else:
            a = 1.0
        a = max(0.0, min(1.0, a))
        try:
            bw, bh = 220, 76
            panel = pygame.Surface((bw, bh), pygame.SRCALPHA)
            panel.fill((10, 10, 20, int(170 * a)))
            pygame.draw.rect(panel, (*eff["color"], int(220 * a)),
                             (0, 0, bw, bh), width=3, border_radius=10)
            screen.blit(panel, (int(eff["x"]) - bw // 2,
                                int(eff["y"]) - bh // 2))
            big_font = get_font(30)
            name_surf = big_font.render(eff["trait_name"], True, eff["color"])
            name_surf.set_alpha(int(255 * a))
            screen.blit(name_surf,
                        (int(eff["x"]) - name_surf.get_width() // 2,
                         int(eff["y"]) - 24))
            sm_font = get_font(18)
            tier_surf = sm_font.render(
                f"{'★' * eff['tier']} 激活", True, (240, 240, 240))
            tier_surf.set_alpha(int(255 * a))
            screen.blit(tier_surf,
                        (int(eff["x"]) - tier_surf.get_width() // 2,
                         int(eff["y"]) + 8))
            r = int(60 + (1 - ratio) * 40)
            pygame.draw.circle(screen, eff["color"],
                               (int(eff["x"]), int(eff["y"])), r,
                               max(1, int(3 * a)))
        except Exception:
            pass
    for eff in buckets["screen_flash"]:
        try:
            s = pygame.Surface((W, H), pygame.SRCALPHA)
            s.fill((255, 255, 255, int(140 * eff["life"] / eff["max_life"])))
            screen.blit(s, (0, 0))
        except Exception:
            pass
    for eff in buckets["damage_pop"]:
        kind = eff.get("kind", "atk")
        col = {"heal": HEAL_COLOR, "crit": CRIT_COLOR, "shield": SHIELD_COLOR,
               "skill": (255, 150, 80)}.get(kind, DAMAGE_COLOR)
        draw_damage_text(screen, eff["text"], int(eff["x"]), int(eff["y"]),
                         font_dmg, col)
    selector_rects = draw_battle_selector(screen, gs, font_sm, W, H)
    if (not gs.battle_phase_resolved and battle.finished
            and not all(b.finished for b in gs.battles)):
        draw_text(screen, "你的对局已结束 · 点击上方标签观战其他对局",
                  W // 2, H * 0.18, font_sm, GOLD_COLOR, True)
    if gs.battle_phase_resolved:
        draw_damage_report(screen, gs, font_lg, font_md, font_sm, W, H)
    return selector_rects


def draw_side_traits(screen, view_p, x, y, panel_w, panel_h, font_sm, font_md):
    tc = count_traits(view_p)
    if not tc:
        draw_panel(screen, pygame.Rect(x, y, panel_w, 44),
                   (24, 26, 34), (65, 72, 88), 8, 1)
        draw_text(screen, "羁绊", x + 8, y + 4, font_sm, GOLD_COLOR)
        draw_text(screen, "(无)", x + 8, y + 24, font_sm, TEXT_DIM)
        return
    # 收集所有羁绊，附上档位信息
    active_traits = []
    for trait, count in tc.items():
        thresholds = TRAIT_DATA.get(trait, [])
        tier = sum(1 for t in thresholds if count >= t)
        active_traits.append((trait, count, tier, thresholds))
    # 排序：已激活的排最上面 → 档位降序 → 数量降序 → 未激活的按数量降序
    active_traits.sort(key=lambda t: (
        0 if t[2] > 0 else 1, -t[2], -t[1]))
    draw_panel(screen, pygame.Rect(x, y, panel_w, panel_h),
               (20, 22, 30), (65, 72, 88), 8, 1)
    draw_text(screen, "羁绊", x + 8, y + 4, font_sm, GOLD_COLOR)
    ly = y + 24
    prismatic_col = RARITY_COLOR["prismatic"]  # (220,130,255) 棱彩紫
    for trait, count, tier, thresholds in active_traits[:10]:
        short = trait_short_cn(trait)
        max_tier = len(thresholds)
        is_max = (tier >= max_tier) and tier > 0  # 已激活到最高档
        next_thresh = None
        for t in thresholds:
            if count < t:
                next_thresh = t
                break
        prog = f"{count}/{next_thresh}" if next_thresh else f"{count}"
        # === 颜色分级 ===
        if tier <= 0:
            col = TEXT_DIM                    # 未激活：灰
        elif is_max:
            col = prismatic_col               # 最高档：棱彩紫
        elif trait in TRAIT_COLOR:
            col = TRAIT_COLOR[trait]          # 专属色（狗熊/符文/财宝）
        else:
            col = GREEN_HP                    # 普通已激活：绿
        # === 字体分级 ===
        if is_max:
            use_font = font_md                # 最高档最大
        elif tier >= 2:
            use_font = get_font(24)           # 中档稍大
        else:
            use_font = font_sm                # 未激活 / 1档保持原样
        # === 左侧等级竖条 ===
        if tier > 0:
            bar_h = use_font.get_height() - 2
            bar_w = min(6, 2 + tier)
            if is_max:
                bar_col = prismatic_col
            elif tier >= 3:
                bar_col = GOLD_COLOR
            else:
                bar_col = GREEN_HP
            pygame.draw.rect(screen, bar_col,
                             (x + 3, ly + 1, bar_w, bar_h),
                             border_radius=2)
        # === 文字 ===
        text_x = x + 8 + (8 if tier > 0 else 0)
        draw_text(screen, f"{short} {prog}", text_x, ly, use_font, col)
        ly += use_font.get_height() + 4
        if ly > y + panel_h - 16:
            break


def draw_bounty_popup(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos):
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 220))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    layer = gs.bounty_layer_current
    tc = count_traits(gs.me)
    max_layer = 9 if tc.get("Treasure", 0) >= 8 else 8
    draw_text(screen, "收 菜", W // 2, H * 0.18,
              get_font(40), TREASURE_COLOR, True)
    draw_text(screen, f"到达第 {layer} 层 (上限 {max_layer} 层)",
              W // 2, H * 0.24, font_lg, GOLD_COLOR, True)
    options = gs.bounty_layer_options or [roll_bounty_reward(layer)]
    card_rects = []
    n = len(options) if layer == 9 else 1
    card_w = W * (0.28 if n == 3 else 0.70)
    card_h = H * 0.18
    gap = W * 0.025
    total_w = n * card_w + (n - 1) * gap
    start_x = W / 2 - total_w / 2
    card_y = H * 0.33
    for i, reward in enumerate(options[:n]):
        x = start_x + i * (card_w + gap)
        r = pygame.Rect(int(x), int(card_y), int(card_w), int(card_h))
        card_rects.append(r)
        draw_panel(screen, r, (40, 34, 20), TREASURE_COLOR, 12, 3)
        draw_text(screen, f"【{reward.get('name', '?')}】",
                  r.centerx, r.y + 24, get_font(24 if n == 3 else 28), GOLD_COLOR, True)
        draw_text(screen, reward.get("desc", ""),
                  r.centerx, r.y + 66, font_sm if n == 3 else font_md, TEXT_WHITE, True)
        if n == 3:
            draw_text(screen, f"选择 {i + 1}", r.centerx, r.y + 130, font_sm, GOLD_COLOR, True)
    gs._bounty_choice_rects = card_rects
    if n == 3:
        draw_text(screen, "第9层终极掠夺：三选一", W // 2, H * 0.58, font_md, GOLD_COLOR, True)
    else:
        draw_text(screen, "收宝离场：获得奖励，层数与碎片归零",
                  W // 2, H * 0.54, font_sm, TEXT_DIM, True)
    draw_text(screen, "深入寻宝：继续叠层，下回合再战",
              r.centerx, r.y + 130, font_sm, TEXT_DIM, True)
    can_continue = layer < max_layer
    btn_w = W * 0.32
    btn_h = 60
    btn_y = H * 0.62
    claim_btn = pygame.Rect(int(W * 0.10), int(btn_y),
                            int(btn_w), int(btn_h))
    cont_btn = pygame.Rect(int(W * 0.58), int(btn_y),
                           int(btn_w), int(btn_h))
    hover_c = claim_btn.collidepoint(mouse_pos)
    draw_button(screen, claim_btn,
                (60, 50, 20) if not hover_c else (95, 78, 25),
                TREASURE_COLOR, 10)
    draw_text(screen, "收宝离场", claim_btn.centerx, claim_btn.centery,
              get_font(28), GOLD_COLOR, True)
    if can_continue:
        hover_k = cont_btn.collidepoint(mouse_pos)
        draw_button(screen, cont_btn,
                    (30, 40, 60) if not hover_k else (45, 60, 90),
                    BLUE, 10)
        draw_text(screen, "深入寻宝", cont_btn.centerx, cont_btn.centery,
                  get_font(28), TEXT_WHITE, True)
    else:
        draw_button(screen, cont_btn, (40, 30, 30), (90, 60, 60), 10)
        draw_text(screen, "已到上限", cont_btn.centerx, cont_btn.centery,
                  font_md, (170, 120, 120), True)
    return claim_btn, (cont_btn if can_continue else None)


def draw_hex_popup(screen, gs, font_lg, font_md, font_sm, W, H):
    try:
        overlay = pygame.Surface((W, H), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 210))
        screen.blit(overlay, (0, 0))
    except Exception:
        pass
    draw_text(screen, "符文强化", W // 2, H * 0.15, font_lg, GOLD_COLOR, True)
    draw_text(screen, "选择一个永久强化", W // 2, H * 0.20, font_md, TEXT_WHITE, True)
    card_rects = []
    n = len(gs.hex_choices)
    if n == 0:
        return card_rects
    card_w = W * 0.88
    card_h = H * 0.13
    gap = H * 0.025
    total_h = n * card_h + (n - 1) * gap
    start_y = H // 2 - total_h // 2 + H * 0.02
    for i, hex_data in enumerate(gs.hex_choices):
        r = pygame.Rect(W // 2 - card_w // 2, start_y + i * (card_h + gap),
                        card_w, card_h)
        rarity = hex_data.get("rarity", "silver")
        rarity_col = RARITY_COLOR.get(rarity, TEXT_WHITE)
        draw_panel(screen, r, (30, 32, 42), rarity_col, 10, 3)
        draw_text(screen, f"[{RARITY_NAME.get(rarity, '?')}]",
                  r.x + 16, r.y + 10, font_sm, rarity_col)
        draw_text(screen, hex_data.get("name", "?"), r.x + 16, r.y + 36,
                  font_lg, TEXT_WHITE)
        draw_text(screen, hex_data.get("desc", ""), r.x + 16, r.y + 70,
                  font_md, TEXT_DIM)
        card_rects.append(r)
    draw_text(screen, "点击卡片选择", W // 2, start_y + total_h + 30,
              font_md, GOLD_COLOR, True)
    return card_rects


def draw_starter_popup(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos):
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 235))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    draw_text(screen, "选择起始英雄", W // 2, H * 0.16,
              get_font(40), GOLD_COLOR, True)
    draw_text(screen, "从 3 位英雄中选择 1 位，作为本局起始",
              W // 2, H * 0.21, font_md, TEXT_WHITE, True)
    card_rects = []
    n = len(gs.starter_choices)
    if n == 0:
        return card_rects
    card_w = W * 0.28
    card_h = H * 0.24
    gap = W * 0.025
    total_w = n * card_w + (n - 1) * gap
    start_x = W // 2 - total_w // 2
    start_y = H // 2 - card_h // 2
    for i, champ in enumerate(gs.starter_choices):
        x = start_x + i * (card_w + gap)
        r = pygame.Rect(int(x), int(start_y), int(card_w), int(card_h))
        hovered = r.collidepoint(mouse_pos)
        cost = champ["cost"]
        bg = COST_BG.get(cost, (35, 38, 48))
        if hovered:
            bg = (min(255, bg[0] + 40), min(255, bg[1] + 40), min(255, bg[2] + 40))
        border = HIGHLIGHT if hovered else COST_COLORS.get(cost, TEXT_WHITE)
        draw_panel(screen, r, bg, border, 10, 4 if hovered else 2)
        traits = champ.get("traits", [])
        if "BearRidge" in traits:
            pygame.draw.rect(screen, BEAR_COLOR, r, width=3, border_radius=10)
        elif "RuneLand" in traits:
            pygame.draw.rect(screen, RUNE_COLOR, r, width=3, border_radius=10)
        elif "Treasure" in traits:
            pygame.draw.rect(screen, TREASURE_COLOR, r, width=3, border_radius=10)
        role = champ.get("role", "warrior")
        role_col = ROLE_COLORS.get(role, TEXT_DIM)
        icon_r = pygame.Rect(r.centerx - 30, r.y + 16, 60, 60)
        pygame.draw.rect(screen, (15, 15, 20), icon_r, border_radius=8)
        pygame.draw.rect(screen, role_col, icon_r, width=2, border_radius=8)
        draw_text(screen, ROLE_SHORT.get(role, "?"), icon_r.centerx,
                  icon_r.centery, font_lg, role_col, True)
        draw_text(screen, champ_cn(champ["name"]), r.centerx, r.y + 92,
                  font_md, COST_COLORS.get(cost, TEXT_WHITE), True)
        draw_text(screen, f"{cost}费", r.centerx, r.y + 118,
                  font_sm, GOLD_COLOR, True)
        tstr = " · ".join(trait_short_cn(t) for t in traits[:2])
        draw_text(screen, tstr, r.centerx, r.y + 142, font_sm, TEXT_DIM, True)
        draw_text(screen, f"HP {champ['hp']}  AD {champ['ad']}",
                  r.centerx, r.y + 166, font_sm, TEXT_WHITE, True)
        skill = skill_cn(champ.get("skill_desc", "?"))
        draw_text(screen, f"【{skill}】", r.centerx, r.y + 190,
                  font_sm, (255, 220, 100), True)
        card_rects.append(r)
    draw_text(screen, "点击选择", W // 2, start_y + card_h + 30,
              font_md, GOLD_COLOR, True)
    return card_rects


def draw_global_augment_popup(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos):
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 235))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    aug = gs.global_augment
    draw_text(screen, "本局全局强化", W // 2, H * 0.18,
              get_font(38), GOLD_COLOR, True)
    draw_text(screen, "所有玩家共享同一强化", W // 2, H * 0.235,
              font_md, TEXT_DIM, True)
    card_w = W * 0.78
    card_h = H * 0.28
    card_x = W // 2 - card_w // 2
    card_y = H // 2 - card_h // 2
    r = pygame.Rect(int(card_x), int(card_y), int(card_w), int(card_h))
    draw_panel(screen, r, (30, 32, 42), RARITY_COLOR["prismatic"], 12, 4)
    icon_r = pygame.Rect(r.centerx - 40, r.y + 20, 80, 80)
    if aug.get("is_treasure_augment"):
        draw_panel(screen, icon_r, (55, 45, 25), TREASURE_COLOR, 8, 3)
        draw_text(screen, "宝", icon_r.centerx, icon_r.centery, get_font(34), TREASURE_COLOR, True)
    else:
        base = get_base_template(aug["champ"])
        cost = base["cost"] if base else 1
        draw_panel(screen, icon_r, COST_BG.get(cost, (35, 38, 48)),
                   COST_COLORS.get(cost, TEXT_WHITE), 8, 3)
        draw_text(screen, champ_cn(aug["champ"])[:3], icon_r.centerx,
                  icon_r.centery, get_font(34),
                  COST_COLORS.get(cost, TEXT_WHITE), True)
    draw_text(screen, aug["name"], r.centerx, r.y + 115,
              get_font(32), GOLD_COLOR, True)
    if aug.get("is_treasure_augment"):
        draw_text(screen, "【宝物型强化】", r.centerx, r.y + 155, font_sm, TREASURE_COLOR, True)
    else:
        draw_text(screen, f"【{champ_cn(aug['champ'])}】的主题强化",
                  r.centerx, r.y + 155, font_sm, TEXT_DIM, True)
    draw_text(screen, aug["desc"], r.centerx, r.y + 185,
              font_md, TEXT_WHITE, True)
    btn = pygame.Rect(r.centerx - 90, r.bottom - 60, 180, 44)
    hovered = btn.collidepoint(mouse_pos)
    draw_button(screen, btn, (60, 50, 20) if not hovered else (90, 75, 25),
                GOLD_COLOR, 8)
    draw_text(screen, "确认", btn.centerx, btn.centery, font_md, GOLD_COLOR, True)
    return btn


def draw_carousel(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos):
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 220))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    draw_text(screen, "选秀", W // 2, H * 0.10, get_font(40), GOLD_COLOR, True)
    draw_text(screen, "从末位先选，选择一个英雄和装备",
              W // 2, H * 0.15, font_md, TEXT_WHITE, True)
    draw_text(screen, f"倒计时: {max(0, gs.carousel_timer):.1f}s",
              W // 2, H * 0.185, font_md, ORANGE_TIMER, True)
    card_rects = []
    n = len(gs.carousel_options)
    if n == 0:
        return card_rects
    cols = 4
    rows = 2
    card_w = W * 0.20
    card_h = H * 0.13
    gap_x = W * 0.02
    gap_y = H * 0.02
    total_w = cols * card_w + (cols - 1) * gap_x
    total_h = rows * card_h + (rows - 1) * gap_y
    start_x = W // 2 - total_w // 2
    start_y = H // 2 - total_h // 2
    for i, u in enumerate(gs.carousel_options[:8]):
        col = i % cols
        row = i // cols
        x = start_x + col * (card_w + gap_x)
        y = start_y + row * (card_h + gap_y)
        r = pygame.Rect(int(x), int(y), int(card_w), int(card_h))
        hovered = r.collidepoint(mouse_pos)
        cost = u.get("cost", 1)
        bg = COST_BG.get(cost, (35, 38, 48))
        if hovered:
            bg = (min(255, bg[0] + 30), min(255, bg[1] + 30), min(255, bg[2] + 30))
        border = HIGHLIGHT if hovered else BORDER_LIGHT
        draw_panel(screen, r, bg, border, 8, 3 if hovered else 2)
        star = u.get("star", 1)
        star_border = STAR_BORDER.get(star, STAR_BORDER[1])
        pygame.draw.rect(screen, star_border, r.inflate(6, 6), width=2, border_radius=9)
        draw_text(screen, champ_cn(u["name"])[:5], r.centerx, r.y + r.h * 0.20,
                  font_md, COST_COLORS.get(cost, TEXT_WHITE), True)
        draw_text(screen, f"{star}星", r.centerx, r.y + r.h * 0.45,
                  font_sm, star_border, True)
        role = u.get("role", "warrior")
        role_col = ROLE_COLORS.get(role, TEXT_DIM)
        draw_text(screen, ROLE_SHORT.get(role, "?"), r.centerx, r.y + r.h * 0.62,
                  font_sm, role_col, True)
        items = u.get("items", [])
        if items:
            ix = r.centerx - (len(items) * 14) // 2
            for item in items[:2]:
                ir = pygame.Rect(ix, r.y + r.h * 0.78, 14, 14)
                draw_item_icon(screen, ir, item)
                ix += 16
        card_rects.append(r)
    draw_text(screen, "点击选择", W // 2, start_y + total_h + 30,
              font_md, GOLD_COLOR, True)
    return card_rects


def draw_streak_badge(screen, x, y, streak, is_win, font_sm):
    if streak < 1:
        return
    color = (255, 180, 60) if is_win else (200, 80, 80)
    bg_col = (60, 40, 20) if is_win else (60, 25, 25)
    txt = f"{'胜' if is_win else '败'}{streak}"
    r = pygame.Rect(x, y, 34, 20)
    draw_panel(screen, r, bg_col, color, 4, 2)
    draw_text(screen, txt, r.centerx, r.centery, font_sm, color, True)


def draw_shop_lock(screen, x, y, locked, font_sm):
    r = pygame.Rect(x, y, 60, 24)
    col = LOCK_COLOR if locked else UNLOCK_COLOR
    bg = (60, 45, 15) if locked else (35, 35, 40)
    draw_panel(screen, r, bg, col, 4, 2)
    txt = "已锁定" if locked else "锁定"
    draw_text(screen, txt, r.centerx, r.centery, font_sm, col, True)
    return r


def draw_top_hud(screen, gs, view_p, view_name, font_lg, font_md, font_sm, W, H):
    top_h = H * 0.088
    try:
        bar = pygame.Surface((W, top_h), pygame.SRCALPHA)
        bar.fill((12, 14, 22, 235))
        screen.blit(bar, (0, 0))
        pygame.draw.line(screen, (90, 75, 30), (0, top_h - 2), (W, top_h - 2), 2)
    except Exception:
        pass
    lv_box_w = W * 0.20
    lv_box = pygame.Rect(8, 8, lv_box_w, top_h - 16)
    draw_panel(screen, lv_box, (28, 30, 42), (90, 110, 150), 10, 2)
    draw_text(screen, f"Lv.{view_p['level']}", lv_box.x + 12, lv_box.y + 6,
              font_md, BLUE_MANA)
    if view_p["level"] < MAX_LEVEL:
        xp = view_p.get("xp", 0)
        need = view_p.get("xp_next", 999)
        ratio = min(1.0, xp / max(1, need))
        bar_r = pygame.Rect(lv_box.x + 12, lv_box.y + lv_box.h - 14,
                            lv_box.w - 24, 8)
        pygame.draw.rect(screen, (25, 27, 36), bar_r, border_radius=3)
        if ratio > 0:
            pygame.draw.rect(screen, BLUE_MANA,
                             (bar_r.x, bar_r.y, int(bar_r.w * ratio), bar_r.h),
                             border_radius=3)
        pygame.draw.rect(screen, (60, 70, 90), bar_r, width=1, border_radius=3)
        draw_text(screen, f"{xp}/{need}", bar_r.centerx, bar_r.centery,
                  font_sm, TEXT_WHITE, True)
    else:
        bar_r = pygame.Rect(lv_box.x + 12, lv_box.y + lv_box.h - 14,
                            lv_box.w - 24, 8)
        pygame.draw.rect(screen, GOLD_COLOR, bar_r, border_radius=3)
        draw_text(screen, "MAX", bar_r.centerx, bar_r.centery,
                  font_sm, (20, 15, 0), True)
    cx = W // 2
    stage, rnd = gs.stage
    rt = get_round_type(stage, rnd)
    rt_label = {"augment": "强化", "monster": "野怪",
                "carousel": "选秀", "pvp": "PVP"}.get(rt, "")
    stage_label = f"{stage}-{rnd} · {rt_label}"
    if gs.is_multiplayer:
        stage_label = f"联机对战 · 第 {gs.round_counter + 1} 局"
    draw_text(screen, stage_label, cx, top_h * 0.20, font_md, TEXT_WHITE, True)
    d = gs.difficulty
    d_col = DIFFICULTY_COLOR.get(d, TEXT_DIM)
    if gs.is_multiplayer:
        draw_text(screen, f"对手: {gs.peer_name}", cx, top_h * 0.50,
                  font_sm, RUNE_COLOR, True)
    else:
        draw_text(screen, f"难度: {DIFFICULTY_NAME.get(d, '?')}",
                  cx, top_h * 0.50, font_sm, d_col, True)
    prep_t = gs.phase_timer
    if prep_t >= 900:
        draw_text(screen, "选择中...", cx, top_h * 0.82, font_lg, GOLD_COLOR, True)
    else:
        if prep_t <= 5:
            prep_col = RED
        elif prep_t <= 10:
            prep_col = ORANGE_TIMER
        else:
            prep_col = GOLD_COLOR
        draw_text(screen, f"{math.ceil(prep_t)}s", cx, top_h * 0.82,
                  font_md, prep_col, True)
    gold_box_w = W * 0.22
    speed_box_w = W * 0.10
    speed_box = pygame.Rect(W - gold_box_w - 8 - speed_box_w - 6, 8,
                            speed_box_w, top_h - 16)
    gs_speed = getattr(gs, "speed", 1.0)
    if gs_speed >= 3:
        speed_col = (255, 130, 130)
    elif gs_speed >= 2:
        speed_col = ORANGE_TIMER
    else:
        speed_col = GREEN_HP
    draw_panel(screen, speed_box, (28, 30, 42), speed_col, 10, 2)
    draw_text(screen, f"{int(gs_speed)}x", speed_box.centerx,
              speed_box.centery, font_md, speed_col, True)
    gold_box = pygame.Rect(W - gold_box_w - 8, 8, gold_box_w, top_h - 16)
    draw_panel(screen, gold_box, (50, 38, 12), (200, 160, 55), 10, 2)
    icon_r = int(gold_box.h * 0.26)
    ix = gold_box.x + 14 + icon_r
    iy = gold_box.y + gold_box.h // 2
    draw_coin_icon(screen, ix, iy, icon_r)
    draw_text(screen, str(view_p["gold"]),
              ix + icon_r + 10, iy - 10, font_md, GOLD_COLOR)
    interest = min(5, view_p["gold"] // 10)
    int_label = f"利息+{interest}" + ("(满)" if view_p["gold"] // 10 >= 5 else "")
    draw_text(screen, int_label,
              ix + icon_r + 10, iy + 8, font_sm, (200, 180, 120))
    # 金铲铲风格：连胜/连败标识
    ws = view_p.get("win_streak", 0)
    ls = view_p.get("lose_streak", 0)
    if ws >= 2:
        draw_text(screen, f"{ws}连胜",
                  gold_box.right - 14 - font_sm.size(f"{ws}连胜")[0],
                  iy - 10, font_sm, GREEN_HP)
    elif ls >= 2:
        draw_text(screen, f"{ls}连败",
                  gold_box.right - 14 - font_sm.size(f"{ls}连败")[0],
                  iy - 10, font_sm, (255, 110, 110))
    draw_text(screen, f"视角: {view_name}", cx, top_h + 5,
              font_sm, TEXT_DIM, True)
    return lv_box


def draw_player_status_row(screen, gs, view_p, font_lg, font_md, font_sm, W, H, y):
    row_h = 42
    hp = view_p["hp"]
    hp_col = GREEN_HP
    if hp < 30:
        t_ms = pygame.time.get_ticks()
        hp_col = RED if (t_ms // 250) % 2 == 0 else (255, 80, 80)
    elif hp < 50:
        hp_col = ORANGE_TIMER
    hp_box = pygame.Rect(8, y, W * 0.30, row_h)
    draw_panel(screen, hp_box, PANEL_DARK, BORDER_LIGHT, 6, 1)
    hx = hp_box.x + 16
    hy = hp_box.centery
    try:
        pygame.draw.circle(screen, hp_col, (hx - 4, hy - 3), 5)
        pygame.draw.circle(screen, hp_col, (hx + 4, hy - 3), 5)
        pygame.draw.polygon(screen, hp_col,
                            [(hx - 9, hy - 1), (hx + 9, hy - 1), (hx, hy + 8)])
    except Exception:
        pass
    draw_text(screen, f"{hp}", hx + 18, hy, font_lg, hp_col)
    hp_bar = pygame.Rect(hx + 60, hy - 4, hp_box.w - 80, 8)
    pygame.draw.rect(screen, (30, 30, 35), hp_bar, border_radius=3)
    ratio = max(0, min(1.0, hp / 100))
    if ratio > 0:
        pygame.draw.rect(screen, hp_col,
                         (hp_bar.x, hp_bar.y, int(hp_bar.w * ratio), hp_bar.h),
                         border_radius=3)
    pygame.draw.rect(screen, BORDER_LIGHT, hp_bar, width=1, border_radius=3)
    ws = view_p.get("win_streak", 0)
    ls = view_p.get("lose_streak", 0)
    if ws >= 1:
        draw_streak_badge(screen, W * 0.40, y + 11, ws, True, font_sm)
    elif ls >= 1:
        draw_streak_badge(screen, W * 0.40, y + 11, ls, False, font_sm)
    prev_rect = pygame.Rect(W * 0.55, y, W * 0.09, row_h)
    draw_button(screen, prev_rect, BLUE_DEEP, BLUE, 6)
    draw_text(screen, "<", prev_rect.centerx, prev_rect.centery, font_lg, TEXT_WHITE, True)
    next_rect = pygame.Rect(W * 0.65, y, W * 0.09, row_h)
    draw_button(screen, next_rect, BLUE_DEEP, BLUE, 6)
    draw_text(screen, ">", next_rect.centerx, next_rect.centery, font_lg, TEXT_WHITE, True)
    auto_rect = pygame.Rect(W * 0.75, y, W * 0.10, row_h)
    draw_button(screen, auto_rect, (30, 60, 40), GREEN_HP, 6)
    draw_text(screen, "布阵", auto_rect.centerx, auto_rect.centery,
              font_sm, TEXT_WHITE, True)
    trait_rect = pygame.Rect(W * 0.86, y, W * 0.12, row_h)
    draw_button(screen, trait_rect, PURPLE_DEEP, PURPLE, 6)
    draw_text(screen, "羁绊", trait_rect.centerx, trait_rect.centery,
              font_md, TEXT_WHITE, True)
    return prev_rect, next_rect, trait_rect, auto_rect


def draw_player_list(screen, gs, font_sm, font_md, W, H, x, y):
    panel_w = 92
    row_h = 26
    total = 8
    panel_h = 22 + total * row_h
    try:
        s = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        s.fill((10, 12, 18, 220))
        screen.blit(s, (x, y))
    except Exception:
        pass
    pygame.draw.rect(screen, (70, 78, 96), (x, y, panel_w, panel_h),
                     width=1, border_radius=6)
    draw_text(screen, "排名", x + 8, y + 4, font_sm, GOLD_COLOR)
    ly = y + 22
    all_p = [gs.me] + gs.players
    entries = []
    for p in all_p:
        entries.append((p, gs.player_label(p)))
    entries.sort(key=lambda e: -e[0]["hp"])
    for i, (p, label) in enumerate(entries):
        is_me = (p is gs.me)
        is_watched = (gs.viewing_player_idx == -1 and is_me) or \
                     (gs.viewing_player_idx >= 0 and
                      gs.players and
                      gs.viewing_player_idx < len(gs.players) and
                      p is gs.players[gs.viewing_player_idx])
        hp = p["hp"]
        if hp <= 0:
            row_col = (55, 55, 60)
            hp_col = (110, 110, 110)
        elif hp < 30:
            row_col = (60, 25, 25)
            hp_col = RED
        elif hp < 50:
            row_col = (60, 45, 20)
            hp_col = ORANGE_TIMER
        else:
            row_col = (25, 35, 50) if is_me else (28, 32, 42)
            hp_col = GREEN_HP
        r = pygame.Rect(x + 3, ly, panel_w - 6, row_h - 2)
        pygame.draw.rect(screen, row_col, r, border_radius=4)
        if is_watched:
            pygame.draw.rect(screen, (255, 240, 120), r, width=2, border_radius=4)
        rank_col = GOLD_COLOR if i == 0 else (TEXT_WHITE if i < 4 else TEXT_DIM)
        draw_text(screen, str(i + 1), r.x + 6, r.centery, font_sm, rank_col, True)
        name_col = (255, 220, 100) if is_me else TEXT_WHITE
        draw_text(screen, label, r.x + 20, r.centery, font_sm, name_col, True)
        draw_text(screen, str(max(0, hp)), r.right - 6, r.centery, font_sm, hp_col, True)
        ly += row_h
    return panel_h


def draw_item_bench(screen, gs, x, y, slot_size, font_sm, mouse_pos,
                    dragging_idx=-1):
    if gs.viewing_player_idx == -1 or not gs.players:
        view_p = gs.me
    else:
        idx = min(gs.viewing_player_idx, len(gs.players) - 1)
        view_p = gs.players[idx]
    items = view_p.get("items", [])
    
    gap = 6
    rects = []
    hover_idx = -1
    for i in range(MAX_ITEM_BENCH):
        r = pygame.Rect(x + i * (slot_size + gap), y, slot_size, slot_size)
        pygame.draw.rect(screen, (22, 24, 32), r, border_radius=6)
        pygame.draw.rect(screen, (55, 62, 78), r, width=2, border_radius=6)
        if i < len(items):
            if i == dragging_idx:
                pygame.draw.rect(screen, (40, 44, 55), r, border_radius=6)
                pygame.draw.rect(screen, HIGHLIGHT, r, width=2, border_radius=6)
            else:
                draw_item_icon(screen, r, items[i])
                if r.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, HIGHLIGHT, r, width=2, border_radius=6)
                    hover_idx = i
        rects.append(r)
    return rects, hover_idx


def _record_log(gs):
    cur = gs.battle_log if gs.battle_log else ""
    if cur and cur != getattr(gs, "_last_log_seen", ""):
        st, rd = gs.stage
        gs.battle_log_history.append(f"[{st}-{rd}] {cur}")
        if len(gs.battle_log_history) > 60:
            del gs.battle_log_history[:-60]
        gs._last_log_seen = cur


def draw_bottom_info_panel(screen, gs, view_p, font_lg, font_md, font_sm,
                            W, H, x, y, w, h):
    _record_log(gs)
    draw_panel(screen, pygame.Rect(x, y, w, h), (18, 20, 28),
               (50, 56, 72), 8, 2)
    mid_x = x + w // 2
    pygame.draw.line(screen, (50, 56, 72), (mid_x, y + 8),
                     (mid_x, y + h - 8), 1)

    draw_text(screen, "战斗记录", x + 12, y + 8, font_md, GOLD_COLOR)
    line_h = font_sm.get_height() + 4
    log_w = max(40, mid_x - x - 24)
    max_lines = max(1, int((h - 44) // line_h))
    avg_char_w = max(1, font_sm.size("M")[0])
    max_chars = max(10, int(log_w // avg_char_w))
    history = list(gs.battle_log_history)
    recent = history[-max_lines:]
    recent.reverse()
    ly = y + 34
    if not recent:
        draw_text(screen, "(无战斗记录)", x + 12, ly, font_sm, TEXT_DIM)
    else:
        for line in recent:
            if len(line) > max_chars:
                line = line[:max_chars - 1] + "…"
            draw_text(screen, line, x + 12, ly, font_sm, TEXT_WHITE)
            ly += line_h

    draw_text(screen, "当前状态", mid_x + 12, y + 8, font_md, GOLD_COLOR)

    # 组装状态行
    status_items = []
    gold = view_p["gold"]
    level = view_p["level"]
    interest = min(5, gold // 10)
    base = 5
    streak = max(view_p.get("win_streak", 0), view_p.get("lose_streak", 0))
    streak_bonus = 3 if streak >= 5 else (2 if streak >= 3 else (1 if streak >= 2 else 0))
    hex_income = get_hex_bonuses(view_p)["income"]
    treasure_income = get_treasure_gold(view_p)
    next_income = base + interest + streak_bonus + hex_income + treasure_income
    status_items.append((f"下回合收入: +{next_income} 金", GOLD_COLOR))
    status_items.append((f"等级 {level} · 上场 {count_board_units(view_p)}/{get_population_cap(view_p)}", TEXT_WHITE))
    tc = count_traits(view_p)
    if tc:
        active_cnt = 0
        for trait, count in tc.items():
            thresholds = TRAIT_DATA.get(trait, [])
            if sum(1 for t in thresholds if count >= t) > 0:
                active_cnt += 1
        status_items.append((f"激活羁绊: {active_cnt} / {len(tc)}", GREEN_HP))
    _tr_thr = TRAIT_DATA.get("Treasure", [])
    if _tr_thr and tc.get("Treasure", 0) >= _tr_thr[0]:
        status_items.append((f"寻宝: 第{getattr(gs, 'bounty_layer_current', 1)}层 · 藏宝碎片{getattr(gs, 'bounty_shards', 0)}/10", (255, 210, 90)))
    ws = view_p.get("win_streak", 0)
    ls = view_p.get("lose_streak", 0)
    if ws >= 2 or ls >= 2:
        tag = "连胜" if ws >= 2 else "连败"
        n = ws if ws >= 2 else ls
        bonus = 3 if n >= 5 else (2 if n >= 3 else 1)
        status_items.append((f"{tag} x{n} · +{bonus} 金", (255, 180, 60)))

    # 滚动 + 裁剪绘制
    line_h_st = font_sm.get_height() + 6
    total_h = len(status_items) * line_h_st
    view_h = h - 44
    max_scroll = max(0, total_h - view_h)
    gs._info_scroll_y = max(0, min(getattr(gs, "_info_scroll_y", 0), max_scroll))
    clip_rect = pygame.Rect(mid_x + 12, y + 34, w // 2 - 24, view_h)
    old_clip = screen.get_clip()
    screen.set_clip(clip_rect)
    start_y = y + 34 - gs._info_scroll_y
    for i, (text, col) in enumerate(status_items):
        item_y = start_y + i * line_h_st
        if item_y + line_h_st > y + 34 and item_y < y + 34 + view_h:
            draw_text(screen, text, mid_x + 12, item_y, font_sm, col)
    screen.set_clip(old_clip)

    # 滚动条
    if max_scroll > 0:
        sb_x = x + w - 8
        pygame.draw.rect(screen, (50, 50, 60), (sb_x, y + 34, 4, view_h), border_radius=2)
        sb_h = max(10, int(view_h * view_h / total_h))
        sb_y = y + 34 + int((view_h - sb_h) * gs._info_scroll_y / max_scroll)
        pygame.draw.rect(screen, (150, 150, 170), (sb_x, sb_y, 4, sb_h), border_radius=2)

    if count_board_units(view_p) > get_population_cap(view_p):
        draw_text(screen, "⚠ 人口已超限，请出售单位或升人口",
                  x + 12, y + h - 36, font_sm, (255, 90, 90))
    hint = ("D 刷新 · F 升级 · L 锁定 · R 布阵 · Tab 概率 · "
            "P 卡池 · Q/E 观战 · 1-5 购买 · Space 开始")
    draw_text(screen, hint, x + w - 12, y + h - 16, font_sm,
              (110, 115, 125))


def draw_unit_detail_panel(screen, gs, unit, view_p, font_lg, font_md, font_sm, W, H):
    d_w = int(W * 0.82)
    d_h = int(H * 0.72)
    dx = W // 2 - d_w // 2
    dy = H // 2 - d_h // 2
    cost = unit.get("cost", 1)
    name_col = COST_COLORS.get(cost, TEXT_WHITE)
    star = unit.get("star", 1)
    border_col = STAR_BORDER.get(star, STAR_BORDER[1])
    draw_panel(screen, pygame.Rect(dx, dy, d_w, d_h),
               (24, 28, 38), border_col, 14, 3)
    title_h = 72
    try:
        s = pygame.Surface((d_w, title_h), pygame.SRCALPHA)
        s.fill((40, 45, 60, 200))
        screen.blit(s, (dx, dy))
    except Exception:
        pass
    pygame.draw.line(screen, border_col, (dx, dy + title_h), (dx + d_w, dy + title_h), 2)
    icon_r = pygame.Rect(dx + 14, dy + 10, 52, 52)
    draw_panel(screen, icon_r, COST_BG.get(cost, (35, 38, 48)), name_col, 8, 3)
    draw_text(screen, champ_cn(unit['name'])[:4],
              icon_r.centerx, icon_r.centery, get_font(26), name_col, True)
    draw_text(screen, f"{champ_cn(unit['name'])}", dx + 80, dy + 12,
              font_lg, name_col)
    for i in range(star):
        star_x = dx + 80 + i * 20
        pygame.draw.polygon(screen, border_col,
                            [(star_x + 8, dy + 46), (star_x + 12, dy + 50),
                             (star_x + 8, dy + 54), (star_x + 4, dy + 50)])
    role = unit.get("role", "warrior")
    role_col = ROLE_COLORS.get(role, TEXT_DIM)
    role_name = ROLE_NAME_CN.get(role, role)
    _dmg_t = unit.get("skill_dmg_type")
    if _dmg_t is None:
        _dmg_t = "magic" if role == "mage" else "physical"
    _dmg_label = "法术" if _dmg_t == "magic" else "物理"
    draw_text(screen, f"{_dmg_label}{role_name} · {cost}费",
              dx + 80 + star * 20 + 10, dy + 48, font_sm, role_col)
    traits = unit.get("traits", [])
    _role = unit.get("role", "warrior")
    _all_t = list(traits) + [ROLE_TO_CLASS_TRAIT.get(_role, "")]
    trait_str = "  ".join(trait_cn(t) for t in _all_t if t)
    # 羁绊行：放在名字/职业下方，金铲铲式清晰展示
    draw_text(screen, f"羁绊: {trait_str}",
              dx + 80, dy + 62, font_sm, GOLD_COLOR)
    y = dy + title_h + 10
    item_stats = get_unit_item_stats(unit)
    base_hp = unit.get("hp", 0)
    base_ad = unit.get("ad", 0)
    atk_range = unit.get("attack_range", RANGE_WARRIOR)
    range_type = "远程" if atk_range > 200 else "近战"
    atk_cd = unit.get("attack_cooldown", 1.2)
    armor = unit.get("armor", 0) + item_stats.get("armor", 0)
    mr = unit.get("mr", 0) + item_stats.get("mr", 0)
    crit = item_stats.get("crit", 0)
    stats_box = pygame.Rect(dx + 12, y, d_w - 24, 72)
    draw_panel(screen, stats_box, (30, 34, 44), (60, 68, 88), 8, 1)
    draw_text(screen, "属性", stats_box.x + 10, stats_box.y + 6,
              font_sm, GOLD_COLOR)
    col_x = [stats_box.x + 10, stats_box.x + stats_box.w // 3 + 10,
             stats_box.x + 2 * stats_box.w // 3 + 10]
    row_y = [stats_box.y + 30, stats_box.y + 52]
    draw_text(screen, f"生命 {base_hp}+{item_stats.get('hp', 0)}",
              col_x[0], row_y[0], font_sm, TEXT_WHITE)
    draw_text(screen, f"攻击 {base_ad}+{item_stats.get('ad', 0)}",
              col_x[1], row_y[0], font_sm, TEXT_WHITE)
    draw_text(screen, f"护甲 {armor}",
              col_x[2], row_y[0], font_sm, TEXT_WHITE)
    draw_text(screen, f"攻距 {atk_range}({range_type})",
              col_x[0], row_y[1], font_sm, TEXT_WHITE)
    draw_text(screen, f"攻速 {1 / atk_cd:.2f}/s",
              col_x[1], row_y[1], font_sm, TEXT_WHITE)
    draw_text(screen, f"暴击+{int(crit * 100)}%  魔抗{mr}",
              col_x[2], row_y[1], font_sm, TEXT_WHITE)
    y = stats_box.bottom + 8
    skill_name = skill_cn(unit.get("skill_desc", "?"))
    stype = unit.get("skill_type", "damage")
    stype_label = {"shield": "护盾", "heal": "治疗", "damage": "伤害"}.get(stype, "?")
    skill_box = pygame.Rect(dx + 12, y, d_w - 24, 98)
    draw_panel(screen, skill_box, (30, 34, 44), (60, 68, 88), 8, 1)
    draw_text(screen, "技能", skill_box.x + 10, skill_box.y + 6,
              font_sm, GOLD_COLOR)
    draw_text(screen, f"【{skill_name}】", skill_box.x + 60, skill_box.y + 4,
              font_md, (255, 220, 100))
    draw_text(screen, f"[{stype_label}型]", skill_box.right - 70, skill_box.y + 8,
              font_sm, {"shield": SHIELD_COLOR, "heal": HEAL_COLOR,
                        "damage": DAMAGE_COLOR}.get(stype, TEXT_DIM))
    if stype == "shield":
        stext = "为自身和周围友军提供护盾"
    elif stype == "heal":
        stext = "为全体友方回复生命"
    else:
        stext = "对敌方造成法术/物理伤害"
    draw_text(screen, stext, skill_box.x + 10, skill_box.y + 28, font_sm, TEXT_DIM)
    sp_base = unit.get("sp_base_dmg", 0)
    sp_mult = unit.get("sp_multiplier", 0)
    max_mana = unit.get("max_mana", 30) + item_stats.get("mana", 0)
    cd = get_skill_cd(cost, star)
    draw_text(screen, f"数值 {sp_base} × {sp_mult}  法力 {max_mana}  冷却 {cd:.1f}s",
              skill_box.x + 10, skill_box.y + 46, font_sm, TEXT_WHITE)
    mana_regen_total = (get_mana_regen(cost, star) + BASE_MANA_REGEN_FLAT
                        + max_mana * BASE_MANA_REGEN_PERCENT)
    draw_text(screen, f"每秒回蓝: {mana_regen_total:.1f}  受击回蓝: +{MANA_PER_HIT_TAKEN_FLAT}+{int(MANA_PER_HIT_TAKEN_PERCENT*100)}%",
              skill_box.x + 10, skill_box.y + 64, font_sm, BLUE_MANA)
    traits_buffs = apply_trait_buffs(view_p)
    sp_mult_env = traits_buffs.get("sp_mult", 1.0)
    hb = get_hex_bonuses(view_p)
    sp_mult_env *= hb["sp_mult"]
    star_scales = SKILL_DMG_STAR_SCALE
    dmg_vals = []
    for s in (1, 2, 3, 4):
        dmg = int(sp_base * sp_mult * star_scales[s] * sp_mult_env)
        mark = "★" if s == star else " "
        dmg_vals.append(f"{mark}{s}星 {dmg}")
    draw_text(screen, "  ".join(dmg_vals),
              skill_box.x + 10, skill_box.y + 82, font_sm, GOLD_COLOR)
    y = skill_box.bottom + 8
    eq_box = pygame.Rect(dx + 12, y, d_w - 24, 78)
    draw_panel(screen, eq_box, (30, 34, 44), (60, 68, 88), 8, 1)
    draw_text(screen, "已装备", eq_box.x + 10, eq_box.y + 6, font_sm, GOLD_COLOR)
    items = unit.get("items", [])
    gs._detail_equip_hits = []
    if items:
        for i, item in enumerate(items):
            ir = pygame.Rect(eq_box.x + 60 + i * 70, eq_box.y + 24, 48, 48)
            draw_item_icon(screen, ir, item)
            draw_text(screen, item.get("name", "?")[:6],
                      ir.centerx, ir.bottom + 4, font_sm, TEXT_WHITE, True)
            gs._detail_equip_hits.append((ir, item))
    else:
        draw_text(screen, "(无)", eq_box.x + 60, eq_box.centery, font_sm, TEXT_DIM)
    y = eq_box.bottom + 8
    rec_box = pygame.Rect(dx + 12, y, d_w - 24, 78)
    draw_panel(screen, rec_box, (35, 38, 50), GOLD_COLOR, 8, 1)
    draw_text(screen, "推荐装备", rec_box.x + 10, rec_box.y + 6, font_sm, GOLD_COLOR)
    rec_names = get_recommend_items(unit.get("name", ""))
    name_to_item = {}
    for iid, base in ITEMS.items():
        name_to_item[base["name"]] = {"id": iid, "name": base["name"],
                                        "stats": base["stats"],
                                        "color": base["color"],
                                        "is_combined": False}
    for key, res in COMBINE_TABLE.items():
        name_to_item[res["name"]] = {"id": "comb_" + "_".join(sorted(key)),
                                       "name": res["name"], "stats": res["stats"],
                                       "color": res["color"], "is_combined": True}
    for i, rec_name in enumerate(rec_names):
        rec_item = name_to_item.get(rec_name)
        if rec_item is None:
            continue
        ir = pygame.Rect(rec_box.x + 60 + i * 70, rec_box.y + 24, 48, 48)
        draw_item_icon(screen, ir, rec_item)
        draw_text(screen, rec_item["name"][:6],
                  ir.centerx, ir.bottom + 4, font_sm, TEXT_WHITE, True)
    refund = cost * (3 ** (star - 1))
    sell_btn = pygame.Rect(dx + 16, dy + d_h - 42, 130, 32)
    draw_button(screen, sell_btn, (110, 28, 28), SELL_RED, 8)
    draw_text(screen, f"出售 +{refund}金", sell_btn.centerx,
              sell_btn.centery, font_md, (255, 210, 210), True)
    gs._detail_sell_rect = sell_btn
    draw_text(screen, "点击空白关闭", dx + d_w - 130, dy + d_h - 22,
              font_sm, TEXT_DIM)


def draw_shop_odds_popup(screen, gs, font_md, font_sm, W, H):
    odds = SHOP_ODDS.get(gs.me["level"], SHOP_ODDS[MAX_LEVEL])
    pw, ph = 220, 40 + 5 * 24
    px, py = 8, int(H * 0.10)
    draw_panel(screen, pygame.Rect(px, py, pw, ph),
               (20, 24, 32), BORDER_LIGHT, 8, 2)
    draw_text(screen, f"等级 {gs.me['level']} · 商店概率",
              px + 10, py + 8, font_md, GOLD_COLOR)
    for i, pct in enumerate(odds):
        cost = i + 1
        col = COST_COLORS.get(cost, TEXT_WHITE)
        row_y = py + 36 + i * 24
        draw_text(screen, f"{cost}费", px + 14, row_y, font_sm, col)
        bar_x, bar_y, bar_w, bar_h = px + 60, row_y + 4, 110, 12
        pygame.draw.rect(screen, (30, 32, 42), (bar_x, bar_y, bar_w, bar_h),
                         border_radius=3)
        if pct > 0:
            pygame.draw.rect(screen, col,
                             (bar_x, bar_y, int(bar_w * pct / 100), bar_h),
                             border_radius=3)
        draw_text(screen, f"{pct}%", px + 178, row_y, font_sm, col)
    draw_text(screen, "按 Tab 关闭", px + 10, py + ph - 18,
              font_sm, TEXT_DIM)


def draw_pool_status_popup(screen, gs, font_lg, font_md, font_sm, W, H):
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 220))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    pw, ph = int(W * 0.72), int(H * 0.80)
    px, py = W // 2 - pw // 2, H // 2 - ph // 2
    draw_panel(screen, pygame.Rect(px, py, pw, ph),
               (20, 24, 32), (80, 90, 120), 12, 2)
    draw_text(screen, "共享卡池", px + 20, py + 12, font_lg, GOLD_COLOR)
    draw_text(screen, "所有玩家共用同一牌池，购买即扣除，出售即返还",
              px + 20, py + 44, font_sm, TEXT_DIM)

    by_cost = {1: [], 2: [], 3: [], 4: [], 5: []}
    for c in CHAMPION_LIST:
        if c.get("no_shop"):
            continue
        by_cost[c["cost"]].append(c)

    y = py + 76
    for cost in range(1, 6):
        champs = by_cost[cost]
        if not champs:
            continue
        total_remain = sum(pool_remaining(c["name"]) for c in champs)
        total_max = sum(POOL_SIZES.get(cost, 0) for _ in champs)
        col = COST_COLORS.get(cost, TEXT_WHITE)
        title = f"{cost}费  {total_remain}/{total_max}"
        draw_text(screen, title, px + 20, y, font_md, col)
        bar_r = pygame.Rect(px + 130, y + 4, pw - 170, 12)
        pygame.draw.rect(screen, (30, 32, 42), bar_r, border_radius=3)
        if total_max > 0:
            ratio = total_remain / total_max
            pygame.draw.rect(screen, col,
                             (bar_r.x, bar_r.y, int(bar_r.w * ratio), bar_r.h),
                             border_radius=3)
        pygame.draw.rect(screen, BORDER_LIGHT, bar_r, width=1, border_radius=3)
        y += 22
        cur_x = px + 28
        line_h = 20
        max_x = px + pw - 24
        for c in champs:
            rem = pool_remaining(c["name"])
            name = champ_cn(c["name"])
            txt = f"{name}·{rem}"
            tw = font_sm.size(txt)[0] + 10
            if cur_x + tw > max_x:
                y += line_h
                cur_x = px + 28
            rem_col = col if rem > 0 else (90, 90, 90)
            draw_text(screen, txt, cur_x, y, font_sm, rem_col)
            cur_x += tw
        y += line_h + 8
    draw_text(screen, "按 P 或 ESC 关闭", px + 20, py + ph - 24,
              font_sm, TEXT_DIM)


def draw_game_over_popup(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos):
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 225))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    is_win = gs.game_over_text == "胜利!"
    big = get_font(72)
    col = GOLD_COLOR if is_win else RED
    draw_text(screen, gs.game_over_text, W // 2, H * 0.22, big, col, True)
    if is_win:
        sub = "恭喜你击败了所有对手!"
    else:
        sub = "再接再厉，下一局翻盘!"
    draw_text(screen, sub, W // 2, H * 0.30, font_md, TEXT_WHITE, True)
    stats_box = pygame.Rect(W * 0.15, H * 0.36, W * 0.70, H * 0.18)
    draw_panel(screen, stats_box, (28, 32, 42), BORDER_LIGHT, 10, 2)
    draw_text(screen, "本局战绩", stats_box.centerx, stats_box.y + 12,
              font_md, GOLD_COLOR, True)
    stage_str = f"{gs.stage[0]}-{gs.stage[1]}"
    draw_text(screen, f"回合: {stage_str}", stats_box.x + 20, stats_box.y + 50,
              font_sm, TEXT_WHITE)
    draw_text(screen, f"等级: {gs.me['level']}", stats_box.x + 20, stats_box.y + 74,
              font_sm, TEXT_WHITE)
    draw_text(screen, f"金币: {gs.me['gold']}",
              stats_box.centerx + 20, stats_box.y + 50, font_sm, GOLD_COLOR)
    dead = sum(1 for ai in gs.players if ai["hp"] <= 0)
    draw_text(screen, f"击败AI: {dead}/{len(gs.players)}",
              stats_box.centerx + 20, stats_box.y + 74, font_sm, GREEN_HP)
    btn_w = W * 0.36
    btn_h = 64
    restart_btn = pygame.Rect(W // 2 - btn_w // 2, H * 0.62, btn_w, btn_h)
    menu_btn = pygame.Rect(W // 2 - btn_w // 2, H * 0.62 + btn_h + 20, btn_w, btn_h)
    hover_r = restart_btn.collidepoint(mouse_pos)
    hover_m = menu_btn.collidepoint(mouse_pos)
    draw_button(screen, restart_btn,
                (55, 45, 15) if not hover_r else (90, 75, 25),
                GOLD_COLOR, 10)
    draw_text(screen, "再来一把", restart_btn.centerx, restart_btn.centery,
              get_font(32), GOLD_COLOR, True)
    draw_button(screen, menu_btn,
                (30, 40, 60) if not hover_m else (45, 60, 90),
                BLUE, 10)
    draw_text(screen, "返回主菜单", menu_btn.centerx, menu_btn.centery,
              get_font(32), TEXT_WHITE, True)
    return restart_btn, menu_btn


def draw_toast(screen, gs, font_md, W, H):
    if not getattr(gs, "_toast", None) or gs._toast_timer <= 0:
        return
    alpha = min(1.0, gs._toast_timer / 0.4)
    color = getattr(gs, "_toast_color", RED)
    r = pygame.Rect(W // 2 - 170, H * 0.42, 340, 46)
    try:
        s = pygame.Surface((r.w, r.h), pygame.SRCALPHA)
        s.fill((20, 10, 10, int(230 * alpha)))
        screen.blit(s, (r.x, r.y))
        pygame.draw.rect(screen, color, r, width=2, border_radius=8)
    except Exception:
        pass
    draw_text(screen, gs._toast, r.centerx, r.centery,
              font_md, (255, 230, 230), True)


def draw_item_choice_popup(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos):
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 225))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    radiant = getattr(gs, "_radiant_chest_choices", None)
    masterwork = getattr(gs, "_masterwork_choices", None)
    tome = getattr(gs, "_emblem_tome_choices", None)
    choices = radiant if radiant else (masterwork if masterwork else tome)
    title = "光明宝箱" if radiant else ("杰作升级器" if masterwork else "纹章之书")
    if radiant:
        desc = "选择 1 件光明成装"
    elif masterwork:
        desc = "选择 1 件成装升级为光明版"
    else:
        desc = "选择 1 个随机纹章"
    draw_text(screen, title, W // 2, int(H * 0.16), get_font(38),
              GOLD_COLOR, True)
    draw_text(screen, desc, W // 2, int(H * 0.23), font_md,
              TEXT_WHITE, True)
    rects = []
    if choices:
        count = len(choices)
        gap = int(W * 0.025)
        card_w = int((W * 0.78 - gap * (count - 1)) / max(1, count))
        card_h = int(H * 0.26)
        start_x = (W - (card_w * count + gap * (count - 1))) // 2
        y = int(H * 0.34)
        for i, choice in enumerate(choices):
            x = start_x + i * (card_w + gap)
            r = pygame.Rect(x, y, card_w, card_h)
            rects.append(r)
            hover = r.collidepoint(mouse_pos)
            draw_panel(screen, r, (40, 42, 55) if not hover else (55, 58, 78),
                       GOLD_COLOR if radiant else PURPLE, 12, 3)
            if radiant or masterwork:
                name = choice.get("name", "光明装备")
                desc2 = "光明版成装"
            else:
                name = trait_cn(choice)
                desc2 = "随机纹章"
            draw_text(screen, f"{i + 1}", r.centerx, r.y + 28,
                      get_font(24), GOLD_COLOR, True)
            draw_text(screen, name, r.centerx, r.y + 82, font_md,
                      TEXT_WHITE, True)
            draw_text(screen, desc2, r.centerx, r.y + 126, font_sm,
                      TEXT_DIM, True)
            draw_text(screen, "点击选择", r.centerx, r.bottom - 32,
                      font_sm, GOLD_COLOR, True)
    gs._item_choice_rects = rects
    gs._tome_close_rect = None
    if tome:
        # 纹章之书：可直接关闭放弃选择（伪棋子保留在备战席，下次可再次触发）
        close_r = pygame.Rect(W // 2 - 75, int(H * 0.70), 150, 42)
        hover_c = close_r.collidepoint(mouse_pos)
        draw_button(screen, close_r, (80, 40, 40) if hover_c else (60, 30, 30),
                    SELL_RED, 10)
        draw_text(screen, "放弃选择", close_r.centerx, close_r.centery,
                  font_md, (255, 210, 210), True)
        gs._tome_close_rect = close_r
    return rects


def draw_game(screen, gs, font_lg, font_md, font_sm, font_dmg, W, H, mouse_pos):
    screen.fill(BG_COLOR)

    def empty_rects(starter=None, ga=None, path_btn=None,
                    go_restart=None, go_menu=None):
        return ([], [], [], None, None, None, None, None, None, None, None,
                [], [], None, [], [], [], starter if starter is not None else [],
                ga if ga is not None else None, -1,
                path_btn if path_btn is not None else None,
                go_restart, go_menu)

    if gs.game_over:
        if gs.battles:
            draw_battle(screen, gs, font_lg, font_md, font_sm, font_dmg, W, H)
        restart_btn, menu_btn = draw_game_over_popup(screen, gs, font_lg,
                                                       font_md, font_sm, W, H,
                                                       mouse_pos)
        draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 10, font_sm,
                  (200, 60, 60), align_center=True)
        return empty_rects(go_restart=restart_btn, go_menu=menu_btn)

    if getattr(gs, "show_starter_popup", False):
        starter_rects = draw_starter_popup(screen, gs, font_lg, font_md,
                                            font_sm, W, H, mouse_pos)
        draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 10, font_sm,
                  (200, 60, 60), align_center=True)
        return empty_rects(starter_rects)

    if getattr(gs, "show_global_augment_popup", False):
        ga_btn = draw_global_augment_popup(screen, gs, font_lg, font_md,
                                            font_sm, W, H, mouse_pos)
        draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 10, font_sm,
                  (200, 60, 60), align_center=True)
        return empty_rects(ga=ga_btn)

    board_rect_list, bench_rect_list, shop_rect_list = [], [], []
    refresh_rect = levelup_rect = gold_btn_rect = None
    trait_btn_rect = prev_btn_rect = next_btn_rect = auto_btn_rect = None
    sell_rect = None
    hex_card_rects = []
    battle_selector_rects = []
    lock_rect = None
    item_bench_rects = []
    carousel_rects = []
    augment_rects = []
    starter_rects = []
    ga_btn = None
    hover_item_idx = -1
    path_btn = None
    go_restart = go_menu = None

    if getattr(gs, "show_item_choice_popup", False):
        draw_item_choice_popup(screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos)
        draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 10, font_sm,
                  (200, 60, 60), align_center=True)
        return (board_rect_list, bench_rect_list, shop_rect_list,
                refresh_rect, levelup_rect, gold_btn_rect,
                trait_btn_rect, auto_btn_rect, prev_btn_rect, next_btn_rect,
                None, hex_card_rects, battle_selector_rects, lock_rect,
                carousel_rects, item_bench_rects, augment_rects, starter_rects,
                ga_btn, hover_item_idx, path_btn, go_restart, go_menu)

    if getattr(gs, "show_bounty_popup", False):
        bounty_claim_btn, bounty_cont_btn = draw_bounty_popup(
            screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos)
        gs._bounty_claim_btn = bounty_claim_btn
        gs._bounty_cont_btn = bounty_cont_btn
        draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 10, font_sm,
                  (200, 60, 60), align_center=True)
        return (board_rect_list, bench_rect_list, shop_rect_list,
                refresh_rect, levelup_rect, gold_btn_rect,
                trait_btn_rect, auto_btn_rect, prev_btn_rect, next_btn_rect,
                None, hex_card_rects, battle_selector_rects, lock_rect,
                carousel_rects, item_bench_rects, augment_rects, starter_rects,
                ga_btn, hover_item_idx, path_btn, go_restart, go_menu)

    if gs.show_carousel:
        carousel_rects = draw_carousel(screen, gs, font_lg, font_md, font_sm,
                                       W, H, mouse_pos)
        draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 10, font_sm,
                  (200, 60, 60), align_center=True)
        return (board_rect_list, bench_rect_list, shop_rect_list,
                refresh_rect, levelup_rect, gold_btn_rect,
                trait_btn_rect, auto_btn_rect, prev_btn_rect, next_btn_rect,
                None, hex_card_rects, battle_selector_rects, lock_rect,
                carousel_rects, item_bench_rects, augment_rects, starter_rects,
                ga_btn, hover_item_idx, path_btn, go_restart, go_menu)

    if gs.is_multiplayer and gs.multiplayer_phase == "prep" \
            and gs.viewing_player_idx == -1:
        hp_box = pygame.Rect(W // 2 - 140, H * 0.02, 280, 40)
        draw_panel(screen, hp_box, (25, 35, 60), BLUE_MANA, 8, 2)
        draw_text(screen, f"你 HP {gs.me['hp']}",
                  hp_box.x + 20, hp_box.centery, font_md, GREEN_HP)
        draw_text(screen, f"好友 HP {gs.peer_hp}",
                  hp_box.right - 140, hp_box.centery, font_md, RED)

    if gs.is_multiplayer and gs.multiplayer_phase == "wait_peer":
        draw_text(screen, "等待对手准备...", W // 2, H * 0.5,
                  get_font(40), GOLD_COLOR, True)

    if gs.is_multiplayer and gs.multiplayer_phase == "wait_battle":
        draw_text(screen, "等待对手战斗数据...", W // 2, H * 0.5,
                  get_font(40), GOLD_COLOR, True)

    if gs.is_battle_phase:
        battle_selector_rects = draw_battle(screen, gs, font_lg, font_md,
                                            font_sm, font_dmg, W, H)
        # 战斗备战席面板开关按钮
        tgl = pygame.Rect(10, 8, W * 0.14, H * 0.055)
        tgl_col = (34, 96, 44) if gs.show_battle_bench else (42, 50, 66)
        tgl_border = GREEN_HP if gs.show_battle_bench else BORDER_LIGHT
        draw_button(screen, tgl, tgl_col, tgl_border, 8)
        draw_text(screen, f"备战席 {'开' if gs.show_battle_bench else '关'}",
                  tgl.centerx, tgl.centery, font_sm, TEXT_WHITE, True)
        gs._battle_bench_toggle_rect = tgl
        bbench, bitem, bsell = [], [], None
        if gs.show_battle_bench:
            bbench, bitem, bsell = draw_battle_bench_panel(
                screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos)
        gs._battle_sell_rect = bsell
        if not gs.battle_phase_resolved:
            bshop, brefresh, blevelup, block = draw_battle_shop_bar(
                screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos)
        else:
            bshop, brefresh, blevelup, block = [], None, None, None
        # 战斗内棋子详情弹窗（含出售按钮）
        if gs.detail_unit is not None:
            u = safe_unit(gs.detail_unit)
            if u is not None:
                draw_unit_detail_panel(screen, gs, u, gs.me,
                                       font_lg, font_md, font_sm, W, H)
        draw_toast(screen, gs, font_md, W, H)
        draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 10, font_sm,
                  (255, 80, 80), align_center=True)
        return ([], bbench, bshop,
                brefresh, blevelup, gold_btn_rect,
                trait_btn_rect, auto_btn_rect, prev_btn_rect, next_btn_rect,
                bsell, hex_card_rects, battle_selector_rects, block,
                [], bitem, [], [], None, -1, None, None, None)

    if gs.viewing_player_idx == -1:
        view_p, view_name = gs.me, "你"
    else:
        if gs.viewing_player_idx < len(gs.players):
            view_p = gs.players[gs.viewing_player_idx]
            view_name = f"AI {gs.viewing_player_idx + 1}"
        else:
            gs.viewing_player_idx = -1
            view_p, view_name = gs.me, "你"

    lv_box = draw_top_hud(screen, gs, view_p, view_name, font_lg, font_md, font_sm, W, H)
    top_h = H * 0.088
    status_y = top_h + 6
    prev_rect, next_rect, trait_rect, auto_rect = draw_player_status_row(
        screen, gs, view_p, font_lg, font_md, font_sm, W, H, status_y)

    content_y = status_y + 50
    left_margin = 6
    right_margin = 100
    board_area_x = left_margin + 96 + 6
    board_area_w = W - board_area_x - right_margin
    cell_size = min(board_area_w / 7 - 4, H * 0.062)
    gap = 3
    board_w = 7 * cell_size + 6 * gap
    board_h = 4 * cell_size + 3 * gap
    board_x = board_area_x + (board_area_w - board_w) // 2
    board_y = content_y + 6

    board_bg = pygame.Rect(board_x - 8, board_y - 8, board_w + 16, board_h + 16)
    draw_panel(screen, board_bg, (20, 23, 32), (70, 78, 98), 12, 2)
    draw_text(screen, "前", board_x - 24, board_y + cell_size * 0.5 + gap * 0.5,
              font_sm, (255, 150, 130))
    draw_text(screen, "后", board_x - 24, board_y + cell_size * 3.5 + gap * 1.5,
              font_sm, (140, 185, 255))

    hover_board = hover_bench = None
    if gs.dragging:
        for row_idx in range(4):
            for col_idx in range(7):
                cx = board_x + col_idx * (cell_size + gap)
                cy = board_y + row_idx * (cell_size + gap)
                if pygame.Rect(cx, cy, cell_size, cell_size).collidepoint(mouse_pos):
                    hover_board = (row_idx, col_idx)
        bench_y_tmp = board_y + board_h + 38
        bench_cell_pre = cell_size * 0.88
        for i in range(8):
            bx = board_x + i * (bench_cell_pre + gap)
            if pygame.Rect(bx, bench_y_tmp, bench_cell_pre,
                           bench_cell_pre).collidepoint(mouse_pos):
                hover_bench = i

    for row_idx in range(4):
        for col_idx in range(7):
            cx = board_x + col_idx * (cell_size + gap)
            cy = board_y + row_idx * (cell_size + gap)
            r = pygame.Rect(cx, cy, cell_size, cell_size)
            row_is_front = row_idx <= 1
            base = FRONT_ROW_COLOR if row_is_front else BACK_ROW_COLOR
            if (row_idx + col_idx) % 2 == 0:
                base = (min(255, base[0] + 8), min(255, base[1] + 8),
                        min(255, base[2] + 8))
            bc = base
            if hover_board == (row_idx, col_idx):
                bc = (min(255, base[0] + 50), min(255, base[1] + 50),
                      min(255, base[2] + 50))
            pygame.draw.rect(screen, bc, r, border_radius=8)
            pygame.draw.rect(screen, (80, 88, 108), r, width=1, border_radius=8)
            if hover_board == (row_idx, col_idx):
                is_target_empty = (view_p["board"][row_idx][col_idx] is None)
                is_from_bench = (gs.drag_source_type == "bench")
                pop_full = (count_board_units(gs.me) >= get_population_cap(gs.me))
                valid = True
                if (gs.viewing_player_idx != -1):
                    valid = False
                elif is_from_bench and is_target_empty and pop_full:
                    valid = False
                hi_col = HIGHLIGHT if valid else SELL_RED
                pygame.draw.rect(screen, hi_col, r, width=3, border_radius=6)
            board_rect_list.append((r, row_idx, col_idx))
            unit = view_p["board"][row_idx][col_idx]
            if unit:
                safe_unit(unit)
                is_src = (gs.dragging and gs.drag_source_type == "board"
                          and gs.drag_idx1 == row_idx and gs.drag_idx2 == col_idx)
                draw_unit_cell(screen, r, unit, font_sm, font_md, is_drag_src=is_src)
                if gs.dragging_item is not None and gs.viewing_player_idx == -1 \
                        and r.collidepoint(mouse_pos):
                    item_name = gs.dragging_item.get("name", "")
                    rec = get_recommend_items(unit.get("name", ""))
                    is_rec = any(item_name.startswith(rn) for rn in rec)
                    icon_size = 16
                    icon_r = pygame.Rect(r.right - icon_size - 4, r.y + 4,
                                         icon_size, icon_size)
                    if is_rec:
                        pygame.draw.rect(screen, (30, 60, 30), icon_r, border_radius=4)
                        pygame.draw.rect(screen, GREEN_HP, icon_r, width=2, border_radius=4)
                        draw_text(screen, "✓", icon_r.centerx, icon_r.centery,
                                  font_sm, GREEN_HP, True)
                    else:
                        pygame.draw.rect(screen, (60, 40, 20), icon_r, border_radius=4)
                        pygame.draw.rect(screen, ORANGE_TIMER, icon_r, width=2, border_radius=4)
                        draw_text(screen, "?", icon_r.centerx, icon_r.centery,
                                  font_sm, ORANGE_TIMER, True)

    trait_panel_x = left_margin
    trait_panel_y = board_y
    trait_panel_w = 96
    trait_panel_h = min(board_h + 16, H * 0.30)
    draw_side_traits(screen, view_p, trait_panel_x, trait_panel_y,
                     trait_panel_w, trait_panel_h, font_sm, font_md)

    bench_y = board_y + board_h + 38
    bench_cell = cell_size * 0.88
    board_cnt = count_board_units(view_p)
    draw_text(screen, f"备战席  {board_cnt}/{get_population_cap(view_p)}上场",
              board_x, bench_y - 18, font_sm, TEXT_DIM)
    for i in range(8):
        bx = board_x + i * (bench_cell + gap)
        r = pygame.Rect(bx, bench_y, bench_cell, bench_cell)
        bc = (28, 31, 42)
        if hover_bench == i:
            bc = (50, 55, 72)
        pygame.draw.rect(screen, bc, r, border_radius=7)
        pygame.draw.rect(screen, (65, 72, 90), r, width=1, border_radius=7)
        if hover_bench == i:
            pygame.draw.rect(screen, HIGHLIGHT, r, width=2, border_radius=5)
        bench_rect_list.append((r, i))
        unit = view_p["bench"][i]
        if unit:
            safe_unit(unit)
            is_src = (gs.dragging and gs.drag_source_type == "bench"
                      and gs.drag_idx1 == i)
            draw_unit_cell(screen, r, unit, font_sm, font_md, is_drag_src=is_src)

    item_y = bench_y + bench_cell + 30
    item_slot = 44
    _bench_owner = "你" if gs.viewing_player_idx == -1 else f"AI {gs.viewing_player_idx + 1}"
    draw_text(screen, f"物品栏 - {_bench_owner} (拖动装备 / 点击查看合成)",
          12, item_y - 20, font_sm, TEXT_DIM)
    item_area_w = MAX_ITEM_BENCH * (item_slot + 6) - 6 + 16
    item_bg = pygame.Rect(8, item_y - 4, item_area_w, item_slot + 8)
    draw_panel(screen, item_bg, (18, 20, 28), (50, 56, 72), 6, 1)
    item_bench_rects, hover_item_idx = draw_item_bench(
        screen, gs, 12, item_y, item_slot, font_sm, mouse_pos,
        dragging_idx=gs.dragging_item_idx)
    used = len(view_p.get("items", []))
    draw_text(screen, f"{used}/{MAX_ITEM_BENCH}",
              item_bg.right + 8, item_y + item_slot // 2, font_sm, TEXT_DIM)

    # 显示当前等级的商店刷新概率
    odds = SHOP_ODDS.get(gs.me["level"], SHOP_ODDS[MAX_LEVEL])
    odds_str = "  ".join([f"{i+1}费:{odds[i]}%" for i in range(5)])
    draw_text(screen, odds_str, 10, item_y + item_slot + 4, font_sm, (180, 180, 200))
    shop_y = item_y + item_slot + 20
    lock_w = 76
    shop_area_w = W - 20 - lock_w - 4 * 6
    shop_w = shop_area_w / 5
    shop_gap = 6
    shop_h = H * 0.11
    lock_rect = draw_shop_lock(screen, W - lock_w + 8, shop_y + 4,
                               gs.shop_locked, font_sm)
    for i in range(5):
        sx = 10 + i * (shop_w + shop_gap)
        r = pygame.Rect(sx, shop_y, shop_w, shop_h)
        champ = gs.shop[i]
        cost = champ["cost"] if champ else 1
        bg_col = COST_BG.get(cost, (30, 33, 44))
        draw_panel(screen, r, bg_col, COST_COLORS.get(cost, BORDER_LIGHT), 10, 2)
        if champ:
            # 顶部费用色条
            pygame.draw.rect(screen, COST_COLORS.get(cost, TEXT_WHITE),
                             (r.x + 2, r.y + 2, r.w - 4, 3), border_radius=2)
        shop_rect_list.append((r, i))
        if champ:
            safe_unit(champ)
            traits = champ.get("traits", [])
            role = champ.get("role", "warrior")
            role_col = ROLE_COLORS.get(role, TEXT_DIM)
            role_rect = pygame.Rect(r.x + 5, r.y + 10, 22, 18)
            pygame.draw.rect(screen, (12, 12, 18), role_rect, border_radius=4)
            pygame.draw.rect(screen, role_col, role_rect, width=1, border_radius=4)
            draw_text(screen, ROLE_SHORT.get(role, "?"),
                      role_rect.centerx, role_rect.centery, font_sm, role_col, True)
            draw_text(screen, champ_cn(champ["name"])[:5], r.centerx,
                      r.y + shop_h * 0.32, font_md,
                      COST_COLORS.get(cost, TEXT_WHITE), True)
            _role = champ.get("role", "warrior")
            _all_t = list(traits) + [ROLE_TO_CLASS_TRAIT.get(_role, "")]
            _all_t = [t for t in _all_t if t][:3]
            tstr = "·".join(trait_short_cn(t) for t in _all_t)
            draw_text(screen, tstr, r.centerx, r.y + shop_h * 0.60,
                      font_sm, TEXT_DIM, True)
            # 金币图标+费用
            coin_y = r.y + shop_h * 0.86
            draw_coin_icon(screen, r.centerx - 14, coin_y, 7)
            draw_text(screen, f"{cost}", r.centerx + 4, coin_y - 7,
                      font_md, GOLD_COLOR)
            owned1 = count_unit_owned(gs.me, champ["name"], 1)
            owned2 = count_unit_owned(gs.me, champ["name"], 2)
            owned3 = count_unit_owned(gs.me, champ["name"], 3)
            if owned1 + owned2 + owned3 > 0:
                br = pygame.Rect(r.right - 52, r.y + 10, 48, 16)
                pygame.draw.rect(screen, (35, 55, 35), br, border_radius=4)
                pygame.draw.rect(screen, GREEN_HP, br, width=1, border_radius=4)
                if owned3:
                    txt = f"{owned3}×3★"
                elif owned2:
                    txt = f"{owned2}×2★"
                else:
                    txt = f"{owned1}×1★"
                draw_text(screen, txt, br.centerx, br.centery,
                          font_sm, GREEN_HP, True)

    btn_y = shop_y + shop_h + 10
    btn_h = H * 0.052
    if gs.viewing_player_idx == -1:
        levelup_rect = pygame.Rect(10, btn_y, W * 0.28, btn_h)
        if gs.me["level"] >= MAX_LEVEL:
            draw_button(screen, levelup_rect, (50, 50, 55), (90, 90, 90), 10)
            draw_text(screen, "已满级", levelup_rect.centerx,
                      levelup_rect.centery, font_md, TEXT_DIM, True)
        else:
            draw_button(screen, levelup_rect, (30, 60, 120), BLUE, 10)
            xp = gs.me.get("xp", 0)
            need = gs.me.get("xp_next", 999)
            remain = max(0, need - xp)
            draw_text(screen, f"升级 {BUY_XP_COST}金 (差{remain})",
                      levelup_rect.centerx, levelup_rect.centery,
                      font_md, TEXT_WHITE, True)
    refresh_rect = pygame.Rect(W * 0.36, btn_y, W * 0.28, btn_h)
    if gs.viewing_player_idx == -1:
        draw_button(screen, refresh_rect, (30, 60, 120), BLUE, 10)
        draw_text(screen, f"刷新 {REFRESH_COST}金", refresh_rect.centerx,
                  refresh_rect.centery, font_md, TEXT_WHITE, True)
    else:
        draw_button(screen, refresh_rect, (38, 38, 44), (85, 85, 90), 10)
        draw_text(screen, "观战中", refresh_rect.centerx,
                  refresh_rect.centery, font_md, TEXT_DIM, True)
    gold_btn_rect = pygame.Rect(W - 10 - W * 0.30, btn_y, W * 0.30, btn_h)
    draw_button(screen, gold_btn_rect, (60, 45, 15), GOLD_DEEP, 10)
    draw_coin_icon(screen, gold_btn_rect.x + 16, gold_btn_rect.centery, 9)
    draw_text(screen, f"{gs.me['gold']}",
              gold_btn_rect.x + 32, gold_btn_rect.centery, font_md, GOLD_COLOR)

    trait_btn_rect, prev_btn_rect, next_btn_rect, auto_btn_rect = \
        trait_rect, prev_rect, next_rect, auto_rect

    bottom_y = btn_y + btn_h + 8
    bottom_h = H - bottom_y - 24
    if bottom_h > 40:
        draw_bottom_info_panel(screen, gs, view_p, font_lg, font_md, font_sm,
                                W, H, 10, bottom_y, W - 20, bottom_h)

    # 准备战斗按钮画在底部面板之后，确保不被盖住、始终可见可点
    if gs.is_multiplayer and gs.multiplayer_phase == "prep" \
            and gs.viewing_player_idx == -1:
        prep_btn = pygame.Rect(W // 2 - W * 0.18, H - H * 0.10, W * 0.36, 50)
        hovered = prep_btn.collidepoint(mouse_pos)
        draw_button(screen, prep_btn,
                    (40, 90, 40) if hovered else (30, 65, 30),
                    GREEN_HP, 10)
        draw_text(screen, "准备战斗 (发送阵容)", prep_btn.centerx,
                  prep_btn.centery, font_md, TEXT_WHITE, True)

    if gs.dragging and gs.drag_unit is not None and gs.viewing_player_idx == -1:
        sell_rect = pygame.Rect(10, shop_y, W - 20, shop_h)
        hovering_sell = sell_rect.collidepoint(mouse_pos)
        col = SELL_RED if hovering_sell else (120, 60, 60)
        pygame.draw.rect(screen, col, sell_rect, width=3, border_radius=8)
        draw_text(screen, "出售 (拖到这里)", sell_rect.centerx,
                  sell_rect.y + 22, font_md, (255, 200, 200), align_center=True)

    if gs.dragging and gs.drag_unit is not None:
        drag_s = 70
        mx, my = mouse_pos
        dr = pygame.Rect(mx - drag_s // 2, my - drag_s // 2, drag_s, drag_s)
        pygame.draw.rect(screen, (0, 0, 0, 100),
                         (dr.x + 2, dr.y + 3, dr.w, dr.h), border_radius=10)
        pygame.draw.rect(screen, (80, 90, 110), dr, border_radius=10)
        du = safe_unit(gs.drag_unit)
        if du is not None:
            star = du.get("star", 1)
            border = STAR_BORDER.get(star, STAR_BORDER[1])
            pygame.draw.rect(screen, border, dr, width=3, border_radius=10)
            cost = du.get("cost", 1)
            name_col = COST_COLORS.get(cost, TEXT_WHITE)
            draw_text(screen, champ_cn(du['name'])[:4], dr.centerx,
                      dr.centery - 8, font_sm, name_col, True)
            draw_text(screen, f"{star}星", dr.centerx, dr.centery + 8,
                      font_sm, border, True)

    if gs.dragging_item is not None:
        drag_s = 40
        mx, my = mouse_pos
        dr = pygame.Rect(mx - drag_s // 2, my - drag_s // 2, drag_s, drag_s)
        draw_item_icon(screen, dr, gs.dragging_item)

    if hover_item_idx >= 0 and gs.dragging_item is None:
        items = gs.me.get("items", [])
        if 0 <= hover_item_idx < len(items):
            draw_item_tooltip(screen, items[hover_item_idx],
                              mouse_pos[0], mouse_pos[1],
                              W, H, font_md, font_sm)

    if gs.detail_unit is not None:
        u = safe_unit(gs.detail_unit)
        if u is not None:
            draw_unit_detail_panel(screen, gs, u, view_p,
                                    font_lg, font_md, font_sm, W, H)

    if getattr(gs, "show_odds_popup", False) and gs.viewing_player_idx == -1:
        draw_shop_odds_popup(screen, gs, font_md, font_sm, W, H)

    if gs.show_trait_popup:
        # 羁绊弹窗：设置最大宽高，标题固定在头部，内容区域垂直滚动，棋子两栏渲染
        tw, th = int(W * 0.55), int(H * 0.82)
        tw = min(tw, 680)
        th = min(th, 780)
        tx, ty = W // 2 - tw // 2, H // 2 - th // 2
        gs._trait_popup_rect = pygame.Rect(tx, ty, tw, th)
        draw_panel(screen, pygame.Rect(tx, ty, tw, th),
                   (28, 32, 42), (100, 70, 140), 14, 2)
        header_h = 46
        draw_text(screen, "当前羁绊 (含棋子列表)", tx + 20, ty + 12,
                  font_md, GOLD_COLOR)
        draw_text(screen, "滚轮滚动 · 点击关闭", tx + tw - 170, ty + 14,
                  font_sm, TEXT_DIM)
        pygame.draw.line(screen, (90, 78, 130), (tx, ty + header_h),
                         (tx + tw, ty + header_h), 2)
        board_names = set()
        for _row in view_p["board"]:
            for _u in _row:
                if _u is not None:
                    _n = _u.get("name", "")
                    if _n:
                        board_names.add(_n)
        trait_count = count_traits(view_p)
        sorted_traits = sorted(trait_count.items(), key=lambda x: -x[1])
        # 预构建内容行：(y偏移, 行高, 绘制函数)
        pad_x = tx + 16
        content_rows = []
        cur_y = 8
        # 动态行高：字体调大后必须按字体实际高度算，否则文字会叠在一起
        _row_h_sm = font_sm.get_height() + 10
        _row_h_eff = font_sm.get_height() + 8
        _row_h_champ = font_sm.get_height() + 8
        _row_h_buff = font_md.get_height() + 10
        _gap_section = 12
        _role_class = {"ClassTank": "tank", "ClassArcher": "archer",
                       "ClassMage": "mage", "ClassWarrior": "warrior"}
        for trait_name, cnt in sorted_traits:
            thresholds = TRAIT_DATA.get(trait_name, [])
            tier = sum(1 for t in thresholds if cnt >= t)
            thresholds_str = "/".join(str(t) for t in thresholds)
            title = f"{trait_cn(trait_name)}  {cnt}  [{thresholds_str}]"
            if trait_name in TRAIT_COLOR:
                col = TRAIT_COLOR[trait_name] if tier > 0 else TEXT_DIM
            else:
                col = GOLD_COLOR if tier > 0 else TEXT_WHITE
            content_rows.append(
                (cur_y, _row_h_sm, lambda yy, s=title, c=col:
                 draw_text(screen, s, pad_x, ty + header_h + yy, font_sm, c)))
            cur_y += _row_h_sm
            if trait_name in TRAIT_DESC:
                effect_name, effects = TRAIT_DESC[trait_name]
                for i, eff_txt in enumerate(effects):
                    is_active = (tier == i + 1)
                    mark = ">" if is_active else " "
                    col2 = GREEN_HP if is_active else (140, 140, 140)
                    line = f"  {mark} ({thresholds[i]}) {effect_name} {eff_txt}"
                    content_rows.append(
                        (cur_y, _row_h_eff, lambda yy, l=line, c=col2:
                         draw_text(screen, l, pad_x, ty + header_h + yy,
                                   font_sm, c)))
                    cur_y += _row_h_eff
            if trait_name in _role_class:
                _tr = _role_class[trait_name]
                trait_champs = [c for c in CHAMPION_LIST
                                if c.get("role") == _tr
                                and not c.get("no_shop")]
            else:
                trait_champs = [c for c in CHAMPION_LIST
                                if trait_name in c.get("traits", [])
                                and not c.get("no_shop")]
            if trait_name == "Summon":
                trait_champs = []
            if trait_champs:
                trait_champs = sorted(trait_champs, key=lambda c: c["cost"])
                content_rows.append(
                    (cur_y, _row_h_champ, lambda yy:
                     draw_text(screen, "  棋子:", pad_x,
                               ty + header_h + yy, font_sm,
                               (170, 200, 255))))
                cur_y += _row_h_champ
                # 两栏分栏渲染
                mid_x = pad_x + (tw - 40) // 2
                for k in range(0, len(trait_champs), 2):
                    pair = trait_champs[k:k + 2]

                    def _draw_pair(yy, pair=pair):
                        for j, c in enumerate(pair):
                            on_board = c["name"] in board_names
                            nm_col = GREEN_HP if on_board else (170, 200, 255)
                            nm = f"{champ_cn(c['name'])}{c['cost']}费"
                            draw_text(screen, nm,
                                      pad_x + j * (mid_x - pad_x),
                                      ty + header_h + yy, font_sm, nm_col)
                    content_rows.append((cur_y, _row_h_champ, _draw_pair))
                    cur_y += _row_h_champ
                cur_y += 6
            cur_y += _gap_section
        buffs = apply_trait_buffs(view_p)
        merge_hex_into_buffs(buffs, view_p)
        cur_y += _gap_section
        content_rows.append(
            (cur_y, _row_h_buff, lambda yy:
             draw_text(screen, "总加成:", pad_x,
                       ty + header_h + yy, font_sm, GOLD_COLOR)))
        cur_y += _row_h_buff
        content_rows.append(
            (cur_y, _row_h_buff, lambda yy:
             draw_text(screen,
                       f"攻击 x{buffs['atk_mult']:.2f}  法强 x{buffs['sp_mult']:.2f}",
                       pad_x, ty + header_h + yy, font_sm, TEXT_WHITE)))
        cur_y += _row_h_buff
        content_rows.append(
            (cur_y, _row_h_buff, lambda yy:
             draw_text(screen,
                       f"生命 x{buffs['hp_mult']:.2f}  暴击 {int(buffs['crit'] * 100)}%",
                       pad_x, ty + header_h + yy, font_sm, TEXT_WHITE)))
        cur_y += _row_h_buff
        content_rows.append(
            (cur_y, _row_h_buff, lambda yy:
             draw_text(screen,
                       f"攻速 x{buffs['atk_speed_mult']:.2f}  额外回蓝 {buffs['extra_mana_per_attack']}",
                       pad_x, ty + header_h + yy, font_sm, TEXT_WHITE)))
        cur_y += _row_h_buff
        sum_star = get_bear_ridge_summon_star(view_p)
        if sum_star > 0:
            content_rows.append(
                (cur_y, _row_h_buff, lambda yy:
                 draw_text(screen, f"狗熊岭召唤: 团子 {sum_star}星",
                           pad_x, ty + header_h + yy,
                           font_sm, BEAR_COLOR)))
            cur_y += _row_h_buff
        t_gold = get_treasure_gold(view_p)
        if t_gold > 0:
            content_rows.append(
                (cur_y, _row_h_buff, lambda yy:
                 draw_text(screen, f"财宝猎人: 每回合 +{t_gold} 金",
                           pad_x, ty + header_h + yy,
                           font_sm, TREASURE_COLOR)))
            cur_y += _row_h_buff
        content_h = cur_y
        view_h = th - header_h - 8
        max_scroll = max(0, content_h - view_h)
        scroll = getattr(gs, "_trait_scroll", 0)
        scroll = max(0, min(scroll, max_scroll))
        gs._trait_scroll = scroll
        gs._trait_max_scroll = max_scroll
        # 滚动条
        if max_scroll > 0:
            sb_x = tx + tw - 14
            sb_track = pygame.Rect(sb_x, ty + header_h, 6, view_h)
            pygame.draw.rect(screen, (52, 54, 72), sb_track, border_radius=3)
            sb_h = max(12, int(view_h * view_h / content_h))
            sb_y = ty + header_h + int((view_h - sb_h) * scroll / max_scroll)
            pygame.draw.rect(screen, (150, 140, 190),
                             (sb_x, sb_y, 6, sb_h), border_radius=3)
        # 内容区裁剪绘制
        clip_rect = pygame.Rect(tx, ty + header_h, tw, view_h)
        old_clip = screen.get_clip()
        try:
            screen.set_clip(clip_rect)
            for y_off, row_h, draw_fn in content_rows:
                if y_off + row_h <= scroll:
                    continue
                if y_off > scroll + view_h:
                    break
                try:
                    draw_fn(y_off - scroll)
                except Exception:
                    pass
        finally:
            screen.set_clip(old_clip)

    if gs.battle_result_timer > 0:
        t = gs.battle_result_timer / 2.0
        alpha_scale = min(1.0, t * 2)
        res_font = get_font(72)
        try:
            bg_surf = pygame.Surface((W, 120), pygame.SRCALPHA)
            bg_surf.fill((0, 0, 0, int(160 * alpha_scale)))
            screen.blit(bg_surf, (0, H // 2 - 60))
        except Exception:
            pass
        draw_damage_text(screen, gs.battle_result_text, W // 2, H // 2,
                         res_font, gs.battle_result_color)

    if gs.show_hex_popup:
        hex_card_rects = draw_hex_popup(screen, gs, font_lg, font_md, font_sm, W, H)

    draw_player_list(screen, gs, font_sm, font_md, W, H, W - 96, top_h + 60)

    if gs.show_item_path_popup:
        path_btn = draw_item_path_popup(screen, gs, font_lg, font_md,
                                         font_sm, W, H, mouse_pos)

    if getattr(gs, "show_pool_popup", False):
        draw_pool_status_popup(screen, gs, font_lg, font_md, font_sm, W, H)

    draw_toast(screen, gs, font_md, W, H)

    draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 10, font_sm,
              (200, 60, 60), align_center=True)

    return (board_rect_list, bench_rect_list, shop_rect_list,
            refresh_rect, levelup_rect, gold_btn_rect,
            trait_btn_rect, auto_btn_rect, prev_btn_rect, next_btn_rect,
            sell_rect, hex_card_rects, battle_selector_rects, lock_rect,
            carousel_rects, item_bench_rects, augment_rects, starter_rects,
            ga_btn, hover_item_idx, path_btn, go_restart, go_menu)


def _draw_menu_icon(surface, x, y, kind, color, size=16):
    """主菜单按钮左侧小图标（纯图形绘制，不依赖字体符号支持）。"""
    cx, cy = x + size // 2, y + size // 2
    h = size // 2
    try:
        if kind in ("play", "continue"):
            pts = [(cx - h // 2, cy - h), (cx + h, cy), (cx - h // 2, cy + h)]
            pygame.draw.polygon(surface, color, pts)
        elif kind == "net":
            pygame.draw.circle(surface, color, (cx - h // 2, cy), h // 2)
            pygame.draw.circle(surface, color, (cx + h // 2, cy), h // 2)
            pygame.draw.line(surface, color, (cx - 2, cy), (cx + 2, cy), 2)
        elif kind == "rank":
            pts = [(cx, cy - h), (cx + h, cy), (cx, cy + h), (cx - h, cy)]
            pygame.draw.polygon(surface, color, pts)
        elif kind == "challenge":
            pygame.draw.line(surface, color, (cx - h // 2, cy - h),
                             (cx + h // 2, cy + h), 3)
            pygame.draw.line(surface, color, (cx + h // 2, cy - h),
                             (cx - h // 2, cy + h), 3)
        elif kind == "congrats":
            pts = [(cx, cy - h), (cx + h, cy), (cx, cy + h), (cx - h, cy)]
            pygame.draw.polygon(surface, color, pts)
            pygame.draw.circle(surface, color, (cx, cy), h // 4)
        elif kind == "update":
            pygame.draw.circle(surface, color, (cx, cy), h // 2, 2)
            pygame.draw.polygon(surface, color,
                                [(cx + h // 2 + 2, cy - h + 2),
                                 (cx + h // 2 - 2, cy - h + 4),
                                 (cx + h // 2 - 4, cy - h + 8)])
        elif kind == "train":
            pts = [(cx - h, cy + h // 3), (cx, cy - h), (cx + h, cy + h // 3)]
            pygame.draw.polygon(surface, color, pts)
        elif kind == "gear":
            # 简化齿轮：圆环 + 4个齿牙点 + 中心点
            pygame.draw.circle(surface, color, (cx, cy), h // 2, 2)
            for i in range(4):
                ang = i * 1.5708
                gx = cx + int((h // 2 + 3) * 0.5)
                gy = cy + int((h // 2 + 3) * 0.5)
                pygame.draw.circle(surface, color,
                                   (cx + int((h // 2 + 2) * 0.9),
                                    cy + int((h // 2 + 2) * 0.2)), 1)
            pygame.draw.circle(surface, color, (cx, cy), h // 4)
        elif kind == "quit":
            pygame.draw.line(surface, color, (cx - h // 2, cy - h // 2),
                             (cx + h // 2, cy + h // 2), 3)
            pygame.draw.line(surface, color, (cx + h // 2, cy - h // 2),
                             (cx - h // 2, cy + h // 2), 3)
    except Exception:
        pass


def draw_menu_decoration(screen, font_sm, W, H):
    showcase = ["BaoLan", "BearBig", "ArcaneLord"]
    labels = ["毁灭豹", "守护熊", "秘法领主"]
    cx = W // 2
    cy = H * 0.33
    r = int(min(W, H) * 0.075)
    gap = int(r * 2.6)
    for i, name in enumerate(showcase):
        x = cx + (i - 1) * gap
        base = get_base_template(name)
        cost = base["cost"] if base else 5
        color = COST_COLORS.get(cost, TEXT_WHITE)
        bg = COST_BG.get(cost, (40, 40, 50))
        # 双层光晕（金色 + 棋子色交替），提升质感
        for k in range(4, 0, -1):
            try:
                glow_s = pygame.Surface((r * 2 + k * 10, r * 2 + k * 10),
                                        pygame.SRCALPHA)
                gc = GOLD_COLOR if k % 2 else color
                pygame.draw.circle(glow_s, (*gc, 18),
                                   (r + k * 5, r + k * 5), r + k * 5)
                screen.blit(glow_s, (x - r - k * 5, cy - r - k * 5))
            except Exception:
                pass
        # 圆底渐变
        try:
            circ = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
            for yy in range(r * 2):
                t = yy / (r * 2)
                c = (int(bg[0] + (color[0] - bg[0]) * t * 0.25),
                     int(bg[1] + (color[1] - bg[1]) * t * 0.25),
                     int(bg[2] + (color[2] - bg[2]) * t * 0.25), 255)
                pygame.draw.circle(circ, c, (r, r), r)
            screen.blit(circ, (x - r, cy - r))
        except Exception:
            pygame.draw.circle(screen, bg, (x, cy), r)
        # 描边：外层亮色 + 内层深色双环
        pygame.draw.circle(screen, color, (x, cy), r, 3)
        pygame.draw.circle(screen, (12, 14, 20), (x, cy), r - 5, 1)
        draw_text(screen, champ_cn(name)[:2], x, cy,
                  get_font(int(r * 0.85)), color, True)
        # 标签：加小圆点装饰
        tag_y = cy + r + 16
        try:
            lbl = get_font(16)
            if lbl is not None:
                w_l = lbl.size(labels[i])[0]
                pygame.draw.circle(screen, color, (x - w_l // 2 - 9, tag_y + 8), 3)
        except Exception:
            pass
        draw_text(screen, labels[i], x, tag_y, font_sm, TEXT_DIM, True)


def draw_main_menu(screen, font_title, font_lg, font_md, font_sm,
                   W, H, mouse_pos, difficulty):
    screen.fill((8, 10, 16))
    # 背景：暖金渐变（顶部淡金 → 向下渐隐）
    try:
        grad = pygame.Surface((W, H), pygame.SRCALPHA)
        for yy in range(0, H, 6):
            t = yy / max(1, H)
            a = int(42 * max(0.0, 1 - t * 2.2))
            pygame.draw.rect(grad, (70, 34, 8, a), (0, yy, W, 6))
        screen.blit(grad, (0, 0))
    except Exception:
        pass
    # 星点
    try:
        for i in range(60):
            sx = (i * 7919) % W
            sy = (i * 6133) % H
            rr = 1 + (i % 3)
            alpha = 80 + (i * 13) % 120
            s = pygame.Surface((rr * 2, rr * 2), pygame.SRCALPHA)
            s.fill((255, 255, 255, alpha))
            screen.blit(s, (sx, sy))
    except Exception:
        pass
    # 顶部光晕
    try:
        glow = pygame.Surface((W, 300), pygame.SRCALPHA)
        for i in range(100, 0, -10):
            a = int(15 * (100 - i) / 100)
            pygame.draw.ellipse(glow, (*GOLD_DEEP, a),
                                (W // 2 - i * 4, 130 - i, i * 8, i * 3))
        screen.blit(glow, (0, 0))
    except Exception:
        pass
    # 标题
    title_y = H * 0.065
    title_text = "豹 药 宇 宙"
    try:
        shadow = font_title.render(title_text, True, (60, 30, 10))
        render = font_title.render(title_text, True, GOLD_COLOR)
        rect = render.get_rect(center=(W // 2, title_y))
        sr = shadow.get_rect(center=(W // 2 + 3, title_y + 3))
        screen.blit(shadow, sr)
        screen.blit(render, rect)
    except Exception:
        draw_text(screen, title_text, W // 2, title_y, font_title, GOLD_COLOR, True)
    draw_text(screen, "Leopard Potion AutoBattle Chess", W // 2, title_y + 32,
              font_sm, TEXT_DIM, True)
    # 顶部信息卡片（难度 + 排位）
    info_r = pygame.Rect(int(W * 0.08), int(H * 0.14), int(W * 0.84), int(H * 0.05))
    try:
        draw_panel(screen, info_r, (20, 22, 30), (90, 78, 30), 12, 2)
    except Exception:
        pygame.draw.rect(screen, (20, 22, 30), info_r, border_radius=12)
    d_col = DIFFICULTY_COLOR.get(difficulty, TEXT_DIM)
    draw_text(screen,
              f"当前AI难度: {DIFFICULTY_NAME.get(difficulty, '?')}  ·  "
              f"排位: {RANK_STATE.get('rank', '青铜')} "
              f"{RANK_STATE.get('score', 0)}分"
              f"({RANK_STATE.get('wins', 0)}胜{RANK_STATE.get('losses', 0)}负)",
              W // 2, info_r.centery, font_md, d_col, True)
    # 棋子装饰（三个五费圆形标识 + 双层光晕）
    draw_menu_decoration(screen, font_sm, W, H)
    # 双列按钮网格：前8个按钮双列4行，退出跨列底部一行
    btn_w = int(W * 0.42)
    btn_h = 52
    gap_x = int(W * 0.02)
    gap_y = 12
    col_x = [W // 2 - btn_w - gap_x // 2, W // 2 + gap_x // 2]
    full_w = int(W * 0.86)
    full_x = W // 2 - full_w // 2
    grid_start = int(H * (0.44 if has_save() else 0.46))
    y = grid_start
    continue_btn = None
    if has_save():
        continue_btn = pygame.Rect(full_x, y, full_w, btn_h)
        y += btn_h + gap_y
    # 双列前8个：开始/联机/排位/挑战/恭喜发财/检测/训练/设置
    grid_specs = [
        ("play", "开始游戏", (55, 45, 15), (95, 78, 25), GOLD_COLOR, GOLD_COLOR),
        ("net", "联机对战", (30, 55, 45), (45, 80, 65), GREEN_HP, GREEN_HP),
        ("rank", "排位赛", (70, 45, 15), (120, 80, 25), GOLD_COLOR, GOLD_COLOR),
        ("challenge", "挑战最强AI", (60, 30, 60), (95, 50, 100), (200, 60, 230), (200, 60, 230)),
        ("congrats", "恭喜发财", (90, 30, 25), (140, 50, 40), (255, 120, 60), (255, 190, 90)),
        ("update", "检测更新", (35, 45, 70), (50, 65, 100), RUNE_COLOR, TEXT_WHITE),
        ("train", "训练极限AI", (50, 40, 70), (75, 55, 110), PURPLE, TEXT_WHITE),
        ("gear", "设置", (30, 40, 60), (45, 60, 90), BLUE, TEXT_WHITE),
    ]
    btn_rects = []
    for idx, (icon, label, base_c, hover_c, border_c, label_c) in enumerate(grid_specs):
        row, col = divmod(idx, 2)
        r = pygame.Rect(col_x[col], y + row * (btn_h + gap_y), btn_w, btn_h)
        btn_rects.append((r, icon, label, base_c, hover_c, border_c, label_c))
    # 退出：跨列底部一行
    quit_btn = pygame.Rect(full_x, y + 4 * (btn_h + gap_y), full_w, btn_h)
    for r, icon, label, base_c, hover_c, border_c, label_c in btn_rects:
        hovered = r.collidepoint(mouse_pos)
        if hovered:
            try:
                glow_r = r.inflate(12, 12)
                gs_ = pygame.Surface(glow_r.size, pygame.SRCALPHA)
                pygame.draw.rect(gs_, (*border_c, 45), gs_.get_rect(), border_radius=14)
                screen.blit(gs_, glow_r.topleft)
            except Exception:
                pass
        draw_button(screen, r, hover_c if hovered else base_c, border_c, 12)
        try:
            _draw_menu_icon(screen, r.x + 14, r.centery - 8, icon, label_c, 16)
        except Exception:
            pass
        draw_text(screen, label, r.centerx + 6, r.centery,
                  get_font(28), label_c, True)
    hovered_q = quit_btn.collidepoint(mouse_pos)
    if hovered_q:
        try:
            glow_r = quit_btn.inflate(12, 12)
            gs_ = pygame.Surface(glow_r.size, pygame.SRCALPHA)
            pygame.draw.rect(gs_, (*RED, 45), gs_.get_rect(), border_radius=14)
            screen.blit(gs_, glow_r.topleft)
        except Exception:
            pass
    draw_button(screen, quit_btn, (75, 40, 40) if hovered_q else (50, 25, 25),
                RED, 12)
    try:
        _draw_menu_icon(screen, quit_btn.x + 14, quit_btn.centery - 8, "quit",
                        (255, 140, 140), 16)
    except Exception:
        pass
    draw_text(screen, "退出", quit_btn.centerx + 6, quit_btn.centery,
              get_font(28), (255, 160, 160), True)
    draw_text(screen, f"v{CURRENT_VERSION}  ·  Built with Pygame  ·  支持联机对战",
              W // 2, H - 24, font_sm, (100, 105, 115), True)
    draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 9, font_sm,
              (200, 60, 60), align_center=True)
    return (continue_btn,
            btn_rects[0][0], btn_rects[1][0], btn_rects[2][0], btn_rects[3][0],
            btn_rects[4][0], btn_rects[5][0], btn_rects[6][0], btn_rects[7][0],
            quit_btn)


def draw_rank_page(screen, font_title, font_lg, font_md, font_sm,
                   W, H, mouse_pos):
    """排位赛专属页面：当前段位/战绩 + 段位进度 + 段位表 + 加分机制说明，
    点击『开始对战』才进入排位对局。"""
    screen.fill((8, 10, 16))
    try:
        for i in range(60):
            sx = (i * 7919) % W
            sy = (i * 6133) % H
            rr = 1 + (i % 3)
            alpha = 80 + (i * 13) % 120
            s = pygame.Surface((rr * 2, rr * 2), pygame.SRCALPHA)
            s.fill((255, 255, 255, alpha))
            screen.blit(s, (sx, sy))
    except Exception:
        pass
    try:
        glow = pygame.Surface((W, 300), pygame.SRCALPHA)
        for i in range(100, 0, -10):
            a = int(15 * (100 - i) / 100)
            pygame.draw.ellipse(glow, (*GOLD_DEEP, a),
                                (W // 2 - i * 4, 130 - i, i * 8, i * 3))
        screen.blit(glow, (0, 0))
    except Exception:
        pass

    draw_text(screen, "排 位 赛", W // 2, H * 0.09, font_title, GOLD_COLOR, True)
    draw_text(screen, "Ranked Ladder", W // 2, H * 0.09 + 34, font_sm, TEXT_DIM, True)

    rank = RANK_STATE.get("rank", "青铜")
    score = RANK_STATE.get("score", 0)
    wins = RANK_STATE.get("wins", 0)
    losses = RANK_STATE.get("losses", 0)

    # 当前段位 + 战绩
    draw_text(screen, rank, W // 2, H * 0.20, font_lg, GOLD_COLOR, True)
    draw_text(screen, f"当前分数 {score}  ·  {wins}胜 {losses}负",
              W // 2, H * 0.20 + 34, font_md, TEXT_WHITE, True)

    # 段位进度条
    _cur_need, _cur_rank, nxt_rank, nxt_need, prog = _rank_progress(score)
    bar_x, bar_y = int(W * 0.15), int(H * 0.30)
    bar_w, bar_h = int(W * 0.70), 16
    pygame.draw.rect(screen, (40, 42, 54), (bar_x, bar_y, bar_w, bar_h),
                     border_radius=8)
    if bar_w > 0:
        fill_w = max(6, int(bar_w * prog))
        pygame.draw.rect(screen, GOLD_COLOR,
                         (bar_x, bar_y, fill_w, bar_h), border_radius=8)
    if nxt_rank is not None:
        draw_text(screen, f"距离 {nxt_rank} 还需 {max(0, nxt_need - score)} 分",
                  W // 2, bar_y + bar_h + 16, font_sm, TEXT_DIM, True)
    else:
        draw_text(screen, "已登顶王者，继续冲分创造纪录！",
                  W // 2, bar_y + bar_h + 16, font_sm, TEXT_DIM, True)

    # 段位一览（两列四行）
    table_y = int(H * 0.42)
    draw_text(screen, "段位一览", W // 2, table_y, font_md, GOLD_COLOR, True)
    col_x1, col_x2 = int(W * 0.22), int(W * 0.62)
    row_h = int(H * 0.035)
    for i, (need, r) in enumerate(RANK_TABLE):
        x = col_x1 if i % 2 == 0 else col_x2
        y = table_y + 30 + (i // 2) * row_h
        col = GOLD_COLOR if r == rank else TEXT_WHITE
        draw_text(screen, f"{r}  {need}分", x, y, font_sm, col, True)

    # 加分机制说明
    rules_y = int(H * 0.60)
    draw_text(screen, "加分机制", W // 2, rules_y, font_md, GOLD_COLOR, True)
    rules = [
        "胜利 +20分  ·  失败 -10分（按对手真实段位缩放）",
        "对手段位低于你（虚高保护）：赢少加、输多扣",
        "对手段位高于你：赢多加、输少扣，鼓励越级挑战",
        "青铜 0 分保底：失败不会扣成负数",
        "分数达标自动升段：青铜0 / 白银100 / 黄金250 / 铂金450",
        "钻石700 / 大师1000 / 宗师1400 / 王者1900",
        "内置青铜→王者全套段位AI：下载即用，无需训练",
        "本地离线训练出的AI会自动覆盖对应段位",
        "⚠ 登顶王者后：噩梦AI入侵排位，7名对手全部为当前最强AI",
        "  击败入侵噩梦AI照常冲分，AI随训练突破自动升级",
    ]
    for i, line in enumerate(rules):
        draw_text(screen, line, W // 2, rules_y + 28 + i * 24,
                  font_sm, TEXT_WHITE, True)

    # 操作按钮：开始对战 / 返回主菜单
    btn_w = W * 0.50
    btn_h = 46
    btn_x = W // 2 - btn_w // 2
    start_btn = pygame.Rect(btn_x, int(H * 0.88) - btn_h - 10, btn_w, btn_h)
    back_btn = pygame.Rect(btn_x, int(H * 0.88) + 4, btn_w, btn_h)
    hover_s = start_btn.collidepoint(mouse_pos)
    hover_b = back_btn.collidepoint(mouse_pos)
    draw_button(screen, start_btn,
                (120, 80, 25) if hover_s else (95, 78, 25), GOLD_COLOR, 12)
    draw_text(screen, "开始对战", start_btn.centerx, start_btn.centery,
              get_font(28), GOLD_COLOR, True)
    draw_button(screen, back_btn,
                (60, 62, 74) if hover_b else (45, 47, 58), TEXT_DIM, 12)
    draw_text(screen, "返回主菜单", back_btn.centerx, back_btn.centery,
              get_font(26), TEXT_WHITE, True)
    draw_text(screen, "v1.4.2  ·  审计缺陷修复版", W // 2, H - 16, font_sm,
              (100, 105, 115), True)
    return start_btn, back_btn


def draw_settings_menu(screen, font_title, font_lg, font_md, font_sm,
                        W, H, mouse_pos, difficulty):
    screen.fill((10, 12, 20))
    draw_text(screen, "设 置", W // 2, H * 0.10, font_title, GOLD_COLOR, True)
    draw_text(screen, "调整 AI 难度，影响对手的经济收入 / 升级节奏 / 装备效率",
              W // 2, H * 0.16, font_md, TEXT_DIM, True)
    btn_w = W * 0.72
    btn_h = 78
    gap = 16
    btn_x = W // 2 - btn_w // 2
    start_y = H * 0.24
    diff_rects = []
    descriptions = {
        "easy": "AI 常常摸鱼 · 不做判断 · 收入 -30%",
        "normal": "AI 决策正常 · 收入标准 · 偶尔摸鱼",
        "hard": "AI 决策到位 · 收入 +25% · 升级更快",
        "extreme": "AI 决策到位 · 收入 +60% · 极限运营",
        "nightmare": "7名对手全部为当前最强AI · 收入 +75% · 顶级运营",
    }
    for i, d in enumerate(DIFFICULTY_ORDER):
        r = pygame.Rect(btn_x, start_y + i * (btn_h + gap), btn_w, btn_h)
        is_current = (d == difficulty)
        hovered = r.collidepoint(mouse_pos)
        col = DIFFICULTY_COLOR[d]
        if is_current:
            bg = (col[0] // 4 + 20, col[1] // 4 + 20, col[2] // 4 + 20)
        elif hovered:
            bg = (45, 50, 65)
        else:
            bg = (30, 34, 44)
        border_w = 4 if is_current else 2
        draw_panel(screen, r, bg, col, 12, border_w)
        icon_r = pygame.Rect(r.x + 12, r.y + 12, btn_h - 24, btn_h - 24)
        pygame.draw.rect(screen, (15, 15, 25), icon_r, border_radius=8)
        pygame.draw.rect(screen, col, icon_r, width=2, border_radius=8)
        draw_text(screen, str(i + 1), icon_r.centerx, icon_r.centery,
                  get_font(32), col, True)
        draw_text(screen, DIFFICULTY_NAME[d], r.x + btn_h, r.y + 14,
                  get_font(28), col)
        draw_text(screen, descriptions[d], r.x + btn_h, r.y + 50,
                  font_sm, TEXT_WHITE)
        if is_current:
            draw_text(screen, "✓", r.right - 40, r.centery,
                      get_font(32), col, True)
        diff_rects.append((r, d))
    changelog_btn = pygame.Rect(W // 2 - W * 0.22, H * 0.68, W * 0.44, 48)
    hovered_cl = changelog_btn.collidepoint(mouse_pos)
    draw_button(screen, changelog_btn,
                (95, 80, 30) if hovered_cl else (55, 45, 15),
                GOLD_COLOR, 10)
    draw_text(screen, "查看更新日志", changelog_btn.centerx,
              changelog_btn.centery, font_md, GOLD_COLOR, True)
    learn_btn = pygame.Rect(W // 2 - W * 0.34, H * 0.76, W * 0.68, 46)
    hovered_l = learn_btn.collidepoint(mouse_pos)
    learn_on = _LEARN_PLAYER_STYLE
    draw_button(screen, learn_btn,
                (45, 80, 45) if hovered_l else (30, 55, 30),
                (70, 200, 90) if learn_on else (130, 130, 140), 10)
    draw_text(screen,
              ("✓ 噩梦AI学习玩家运营: 开启" if learn_on
               else "✗ 噩梦AI学习玩家运营: 关闭"),
              learn_btn.centerx, learn_btn.centery, font_md,
              (180, 255, 190) if learn_on else TEXT_DIM, True)
    clear_btn = pygame.Rect(W // 2 - W * 0.34, H * 0.84, W * 0.68, 46)
    hovered_c = clear_btn.collidepoint(mouse_pos)
    draw_button(screen, clear_btn,
                (120, 50, 40) if hovered_c else (80, 35, 28),
                (255, 120, 100), 10)
    draw_text(screen, "清空玩家学习样本（AI遗忘你的打法）",
              clear_btn.centerx, clear_btn.centery, font_md, (255, 200, 190), True)
    back_btn = pygame.Rect(W // 2 - W * 0.22, H * 0.92, W * 0.44, 54)
    hovered_back = back_btn.collidepoint(mouse_pos)
    draw_button(screen, back_btn,
                (45, 60, 90) if hovered_back else (30, 40, 60),
                BLUE, 10)
    draw_text(screen, "返回主菜单", back_btn.centerx, back_btn.centery,
              font_lg, TEXT_WHITE, True)
    return diff_rects, back_btn, changelog_btn, learn_btn, clear_btn


def draw_challenge_page(screen, font_title, font_lg, font_md, font_sm,
                        W, H, mouse_pos):
    """挑战最强AI专属页面：7名对手全部为当前最强AI，击败它们证明实力。
    点击『开始挑战』以噩梦模式进入对局；对局结算会记录玩家信息供AI自我升级。"""
    screen.fill((8, 10, 16))
    try:
        for i in range(60):
            sx = (i * 7919) % W
            sy = (i * 6133) % H
            rr = 1 + (i % 3)
            alpha = 80 + (i * 13) % 120
            s = pygame.Surface((rr * 2, rr * 2), pygame.SRCALPHA)
            s.fill((255, 255, 255, alpha))
            screen.blit(s, (sx, sy))
    except Exception:
        pass
    try:
        glow = pygame.Surface((W, 300), pygame.SRCALPHA)
        for i in range(100, 0, -10):
            a = int(15 * (100 - i) / 100)
            pygame.draw.ellipse(glow, (*GOLD_DEEP, a),
                                (W // 2 - i * 4, 130 - i, i * 8, i * 3))
        screen.blit(glow, (0, 0))
    except Exception:
        pass

    draw_text(screen, "挑战最强AI", W // 2, H * 0.09, font_title,
              (200, 60, 230), True)
    draw_text(screen, "Nightmare Challenge", W // 2, H * 0.09 + 34,
              font_sm, TEXT_DIM, True)

    # 当前最强AI信息
    best_score = _TRAINING_STATE.get("best_score", 0.0)
    best_rank = _ai_rank_from_score(best_score)
    if best_score > 0:
        ai_line = f"当前最强AI: {best_rank}AI · 综合分 {best_score:.1f}"
    else:
        ai_line = "当前最强AI: 出厂极限AI（尚未训练，建议先训练极限AI）"
    draw_text(screen, ai_line, W // 2, H * 0.20, font_md, GOLD_COLOR, True)
    draw_text(screen, "7名对手全部为当前最强AI", W // 2, H * 0.28,
              font_lg, TEXT_WHITE, True)
    draw_text(screen, "击败它们，证明你才是豹药宇宙的最强玩家",
              W // 2, H * 0.28 + 34, font_md, TEXT_DIM, True)
    draw_text(screen, "· 对手收入 +75% · 顶级运营 · 全程针对你的阵容",
              W // 2, H * 0.40, font_sm, TEXT_WHITE, True)
    draw_text(screen, "· 你的每一局都会被记录，AI 用你的打法自我升级",
              W // 2, H * 0.40 + 24, font_sm, TEXT_WHITE, True)
    draw_text(screen, "· 建议先到「训练极限AI」把 AI 练到白银以上再挑战",
              W // 2, H * 0.40 + 48, font_sm, (255, 170, 60), True)

    start_btn = pygame.Rect(W // 2 - W * 0.28, H * 0.62, W * 0.56, 68)
    hovered_st = start_btn.collidepoint(mouse_pos)
    draw_button(screen, start_btn,
                (120, 40, 130) if hovered_st else (70, 22, 80),
                (200, 60, 230), 12)
    draw_text(screen, "开始挑战", start_btn.centerx, start_btn.centery,
              font_lg, (230, 190, 255), True)
    back_btn = pygame.Rect(W // 2 - W * 0.22, H * 0.82, W * 0.44, 60)
    hovered_back = back_btn.collidepoint(mouse_pos)
    draw_button(screen, back_btn,
                (45, 60, 90) if hovered_back else (30, 40, 60),
                BLUE, 10)
    draw_text(screen, "返回主菜单", back_btn.centerx, back_btn.centery,
              font_lg, TEXT_WHITE, True)
    return start_btn, back_btn


def draw_congrats_page(screen, font_title, font_lg, font_md, font_sm,
                       W, H, mouse_pos):
    """恭喜发财专属页面：五费开局 + 大妮蔻狂欢 + 全员噩梦最强AI。"""
    screen.fill((8, 10, 16))
    try:
        for i in range(60):
            sx = (i * 7919) % W
            sy = (i * 6133) % H
            rr = 1 + (i % 3)
            alpha = 80 + (i * 13) % 120
            s = pygame.Surface((rr * 2, rr * 2), pygame.SRCALPHA)
            s.fill((255, 255, 255, alpha))
            screen.blit(s, (sx, sy))
    except Exception:
        pass
    try:
        glow = pygame.Surface((W, 300), pygame.SRCALPHA)
        for i in range(100, 0, -10):
            a = int(15 * (100 - i) / 100)
            pygame.draw.ellipse(glow, (*GOLD_DEEP, a),
                                (W // 2 - i * 4, 130 - i, i * 8, i * 3))
        screen.blit(glow, (0, 0))
    except Exception:
        pass

    draw_text(screen, "恭喜发财", W // 2, H * 0.07, font_title,
              (255, 190, 90), True)
    draw_text(screen, "Congrats Fortune · 五费开局 · 大妮蔻狂欢",
              W // 2, H * 0.07 + 34, font_sm, TEXT_DIM, True)

    rules = [
        "· 开局选秀3个候选全部为5费棋子，你自选1张（对手各随机1张5费）",
        "· 7名对手全部为当前最强AI（噩梦强度）",
        "· 大妮蔻获取途径扩充：财宝高层/野怪法球/血量跌破50/海克斯",
        "· 阶段6结束：存活单位100%获得1张大妮蔻",
        "· AI会主动追三星五费，有人三星时AI会追别的五费对抗",
        "· 节奏更快、资源更丰富，体验顶级爽局",
    ]
    y = H * 0.22
    for line in rules:
        draw_text(screen, line, W // 2, y, font_md, TEXT_WHITE, True)
        y += 34
    draw_text(screen, "仅此模式生效，排位/普通/噩梦完全不受影响",
              W // 2, y + 8, font_sm, (255, 170, 60), True)

    start_btn = pygame.Rect(W // 2 - W * 0.28, H * 0.78, W * 0.56, 68)
    hovered_st = start_btn.collidepoint(mouse_pos)
    draw_button(screen, start_btn,
                (150, 60, 30) if hovered_st else (100, 40, 20),
                (255, 140, 60), 12)
    draw_text(screen, "开始恭喜发财", start_btn.centerx, start_btn.centery,
              font_lg, (255, 220, 160), True)
    back_btn = pygame.Rect(W // 2 - W * 0.22, H * 0.90, W * 0.44, 56)
    hovered_back = back_btn.collidepoint(mouse_pos)
    draw_button(screen, back_btn,
                (45, 60, 90) if hovered_back else (30, 40, 60),
                BLUE, 10)
    draw_text(screen, "返回主菜单", back_btn.centerx, back_btn.centery,
              font_lg, TEXT_WHITE, True)
    return start_btn, back_btn

def draw_changelog_popup(screen, font_lg, font_md, font_sm, W, H, mouse_pos):
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 235))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    pw, ph = int(W * 0.86), int(H * 0.80)
    px, py = W // 2 - pw // 2, H // 2 - ph // 2
    draw_panel(screen, pygame.Rect(px, py, pw, ph),
               (22, 26, 36), (90, 100, 130), 12, 2)
    draw_text(screen, "更 新 日 志", W // 2, py + 26,
              get_font(34), GOLD_COLOR, True)
    pygame.draw.line(screen, BORDER_LIGHT, (px + 20, py + 60),
                     (px + pw - 20, py + 60), 1)
    ly = py + 78
    line_h = 24
    for line in CHANGELOG_TEXT:
        if ly > py + ph - 78:
            draw_text(screen, "…(更多内容请查阅源码)", px + 24, ly,
                      font_sm, TEXT_DIM)
            break
        if line.startswith("v"):
            draw_text(screen, line, px + 24, ly, font_md, GOLD_COLOR)
        elif line.strip():
            draw_text(screen, line, px + 24, ly, font_sm, TEXT_WHITE)
        ly += line_h
    close_btn = pygame.Rect(W // 2 - 90, py + ph - 60, 180, 44)
    hovered = close_btn.collidepoint(mouse_pos)
    draw_button(screen, close_btn,
                (90, 75, 25) if hovered else (60, 50, 20),
                GOLD_COLOR, 8)
    draw_text(screen, "关闭 (ESC)", close_btn.centerx, close_btn.centery,
              font_md, GOLD_COLOR, True)
    return close_btn


def draw_update_popup(screen, font_lg, font_md, font_sm, W, H, mouse_pos,
                      update_info, status):
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 235))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    pw, ph = int(W * 0.82), int(H * 0.72)
    px, py = W // 2 - pw // 2, H // 2 - ph // 2
    draw_panel(screen, pygame.Rect(px, py, pw, ph),
               (22, 26, 36), (90, 130, 200), 12, 2)
    draw_text(screen, "检 测 更 新", W // 2, py + 26,
              get_font(32), RUNE_COLOR, True)

    if update_info is None:
        msg = status or "已是最新版本"
        draw_text(screen, msg, W // 2, py + ph // 2 - 20,
                  font_lg, TEXT_WHITE, True)
        close_btn = pygame.Rect(W // 2 - 90, py + ph - 60, 180, 44)
        hovered = close_btn.collidepoint(mouse_pos)
        draw_button(screen, close_btn,
                    (90, 75, 25) if hovered else (60, 50, 20), GOLD_COLOR, 8)
        draw_text(screen, "关闭", close_btn.centerx, close_btn.centery,
                  font_md, GOLD_COLOR, True)
        return close_btn, None

    new_ver = update_info.get("version", "?")
    cl = update_info.get("changelog", [])
    draw_text(screen, f"发现新版本  v{new_ver}", W // 2, py + 62,
              font_lg, GOLD_COLOR, True)
    draw_text(screen, f"当前版本  v{CURRENT_VERSION}", W // 2, py + 96,
              font_md, TEXT_DIM, True)

    y = py + 130
    draw_text(screen, "更新内容：", px + 24, y, font_md, TEXT_WHITE)
    y += 26
    for line in cl[:12]:
            text = f"· {line}"
            max_w = pw - 64
            while text and y <= py + ph - 120:
                sub = ""
                for ch in text:
                    if font_sm.size(sub + ch)[0] <= max_w:
                        sub += ch
                    else:
                        break
                if not sub:
                    # 如果连一个字符都放不下，强制放一个，避免死循环
                    sub = text[0]
                    text = text[1:]
                else:
                    text = text[len(sub):]
                draw_text(screen, sub, px + 32, y, font_sm, TEXT_WHITE)
                y += 22
            if y > py + ph - 120:
                draw_text(screen, "…", px + 32, y, font_sm, TEXT_DIM)
                break

    if status:
        draw_text(screen, status, W // 2, py + ph - 96,
                  font_md, ORANGE_TIMER, True)

    update_btn = pygame.Rect(W // 2 - 200, py + ph - 70, 180, 48)
    close_btn = pygame.Rect(W // 2 + 20, py + ph - 70, 180, 48)
    hovered_u = update_btn.collidepoint(mouse_pos)
    hovered_c = close_btn.collidepoint(mouse_pos)
    draw_button(screen, update_btn,
                (50, 95, 55) if hovered_u else (30, 70, 35), GREEN_HP, 10)
    draw_text(screen, "立即更新", update_btn.centerx, update_btn.centery,
              font_md, TEXT_WHITE, True)
    draw_button(screen, close_btn,
                (75, 50, 25) if hovered_c else (55, 35, 20), ORANGE_TIMER, 10)
    draw_text(screen, "稍后再说", close_btn.centerx, close_btn.centery,
              font_md, TEXT_WHITE, True)
    return close_btn, update_btn


def draw_training_popup(screen, font_lg, font_md, font_sm, W, H, mouse_pos, st):
    """极限 AI 离线训练进度弹窗。返回 (开始/停止按钮, 关闭按钮)。"""
    try:
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 235))
        screen.blit(ov, (0, 0))
    except Exception:
        pass
    pw, ph = int(W * 0.88), int(H * 0.84)
    px, py = W // 2 - pw // 2, H // 2 - ph // 2
    draw_panel(screen, pygame.Rect(px, py, pw, ph),
               (18, 22, 32), (130, 90, 190), 12, 2)
    draw_text(screen, "极 限 AI 离 线 训 练", W // 2, py + 22,
              get_font(30), PURPLE, True)

    running = st.get("running", False)
    status_col = GREEN_HP if running else TEXT_DIM
    draw_text(screen, "● 训练中" if running else "○ 已停止",
              px + 24, py + 60, font_md, status_col)

    ly = py + 96
    draw_text(screen, f"段位: {st.get('rank', '青铜')}",
              px + 24, ly, font_md, GOLD_COLOR)
    draw_text(screen, f"阶段: {st.get('phase_label', '普通')} "
                      f"(phase {st.get('phase', 1)}/3)",
              px + pw // 2, ly, font_md, RUNE_COLOR)
    draw_text(screen, f"对手池: {st.get('pool_size', 2)}",
              px + pw - 150, ly, font_md, TREASURE_COLOR)
    ly += 30
    draw_text(screen, f"代数: {st.get('generation', 0)}",
              px + 24, ly, font_md, TEXT_WHITE)
    draw_text(screen, f"候选: {st.get('current_variant', 0)}"
                      f"/{st.get('current_population', 0)}",
              px + pw // 2, ly, font_md, TEXT_WHITE)
    draw_text(screen, f"玩家对局: {len(_load_player_history())}",
              px + pw - 170, ly, font_md, TEXT_WHITE)
    ly += 30
    draw_text(screen, f"本代最优: {max(0.0, st.get('gen_best', 0.0)):.1f}",
              px + 24, ly, font_md, ORANGE_TIMER)
    _bs = st.get("best_score", 0)
    draw_text(screen, f"历史最优: {_bs:.1f}({_ai_rank_from_score(_bs)}AI)",
              px + pw // 2, ly, font_md, GOLD_COLOR)
    _stall = st.get("no_breakthrough_gens", 0)
    draw_text(screen, f"停滞: {_stall}",
              px + pw - 90, ly, font_md, TEXT_DIM)
    ly += 30
    _mode_col = ORANGE_TIMER if _stall >= 15 else TEXT_DIM
    draw_text(screen, "变异模式: " + ("增强(大变异探索)" if _stall >= 15 else "标准"),
              px + 24, ly, font_md, _mode_col)
    ly += 26
    draw_text(screen, "日志:", px + 24, ly, font_md, TEXT_WHITE)
    ly += 24
    for line in st.get("log", [])[-14:]:
        if ly > py + ph - 110:
            break
        if len(line) > 54:
            line = line[:54] + "…"
        draw_text(screen, line, px + 30, ly, font_sm, TEXT_DIM)
        ly += 20

    btn_y = py + ph - 66
    if running:
        stop_btn = pygame.Rect(W // 2 - 210, btn_y, 200, 46)
        hide_btn = pygame.Rect(W // 2 + 10, btn_y, 200, 46)
        h1 = stop_btn.collidepoint(mouse_pos)
        h2 = hide_btn.collidepoint(mouse_pos)
        draw_button(screen, stop_btn,
                    (110, 45, 45) if h1 else (70, 30, 30), RED, 10)
        draw_text(screen, "停止训练", stop_btn.centerx, stop_btn.centery,
                  font_md, TEXT_WHITE, True)
        draw_button(screen, hide_btn,
                    (60, 70, 90) if h2 else (40, 50, 70), RUNE_COLOR, 10)
        draw_text(screen, "隐藏窗口", hide_btn.centerx, hide_btn.centery,
                  font_md, TEXT_WHITE, True)
        return stop_btn, hide_btn
    else:
        start_btn = pygame.Rect(W // 2 - 210, btn_y, 200, 46)
        close_btn = pygame.Rect(W // 2 + 10, btn_y, 200, 46)
        h1 = start_btn.collidepoint(mouse_pos)
        h2 = close_btn.collidepoint(mouse_pos)
        draw_button(screen, start_btn,
                    (55, 100, 60) if h1 else (35, 75, 40), GREEN_HP, 10)
        draw_text(screen, "开始训练", start_btn.centerx, start_btn.centery,
                  font_md, TEXT_WHITE, True)
        draw_button(screen, close_btn,
                    (80, 55, 30) if h2 else (60, 40, 22), ORANGE_TIMER, 10)
        draw_text(screen, "关闭", close_btn.centerx, close_btn.centery,
                  font_md, TEXT_WHITE, True)
        return start_btn, close_btn


def draw_lobby(screen, font_title, font_lg, font_md, font_sm,
               W, H, mouse_pos, mode, net, ip_input, port_input, status_msg):
    screen.fill((8, 10, 16))
    draw_text(screen, "联机对战", W // 2, H * 0.10, font_title, GOLD_COLOR, True)

    if mode == "choose":
        btn_w = W * 0.5
        btn_h = 68
        host_btn = pygame.Rect(W // 2 - btn_w // 2, H * 0.32, btn_w, btn_h)
        join_btn = pygame.Rect(W // 2 - btn_w // 2, H * 0.32 + btn_h + 20, btn_w, btn_h)
        back_btn = pygame.Rect(W // 2 - btn_w // 2, H * 0.32 + 2 * (btn_h + 20), btn_w, btn_h)

        for btn, label, col, bg_base in [
            (host_btn, "创建房间", GOLD_COLOR, (55, 45, 15)),
            (join_btn, "加入房间", BLUE, (30, 40, 60)),
            (back_btn, "返回", TEXT_WHITE, (50, 25, 25)),
        ]:
            hovered = btn.collidepoint(mouse_pos)
            bg = tuple(min(255, c + 30) for c in bg_base) if hovered else bg_base
            draw_button(screen, btn, bg, col, 12)
            draw_text(screen, label, btn.centerx, btn.centery, font_lg, col, True)

        draw_text(screen, "与好友在同一局域网内联机（默认端口 5555）",
                  W // 2, H * 0.78, font_sm, TEXT_DIM, True)
        draw_text(screen, f"本机 IP: {NetworkManager.get_local_ip()}",
                  W // 2, H * 0.83, font_md, RUNE_COLOR, True)
        return host_btn, join_btn, back_btn, None

    elif mode == "host":
        draw_text(screen, "等待好友加入...", W // 2, H * 0.22,
                  font_lg, GOLD_COLOR, True)
        box = pygame.Rect(W // 2 - W * 0.35, H * 0.32, W * 0.70, 60)
        draw_panel(screen, box, (25, 30, 45), RUNE_COLOR, 8, 2)
        draw_text(screen, f"{NetworkManager.get_local_ip()}:{net.port if net else 5555}",
                  box.centerx, box.centery, get_font(34), RUNE_COLOR, True)
        draw_text(screen, "把这个 IP 和端口告诉你的好友", W // 2, H * 0.42,
                  font_md, TEXT_WHITE, True)
        draw_text(screen, status_msg, W // 2, H * 0.50, font_md, ORANGE_TIMER, True)

        dots = "." * (int(time.time() * 2) % 4)
        draw_text(screen, f"等待连接{dots}", W // 2, H * 0.58,
                  font_md, GOLD_COLOR, True)

        cancel_btn = pygame.Rect(W // 2 - W * 0.15, H * 0.72, W * 0.30, 50)
        hovered = cancel_btn.collidepoint(mouse_pos)
        draw_button(screen, cancel_btn,
                    (75, 40, 40) if hovered else (50, 25, 25), RED, 8)
        draw_text(screen, "取消", cancel_btn.centerx, cancel_btn.centery,
                  font_md, TEXT_WHITE, True)
        return None, None, cancel_btn, None

    elif mode == "join":
        draw_text(screen, "输入好友的 IP", W // 2, H * 0.10,
                  font_lg, TEXT_WHITE, True)
        ip_box = pygame.Rect(W // 2 - W * 0.35, H * 0.16, W * 0.70, 52)
        draw_panel(screen, ip_box, (25, 28, 38),
                   HIGHLIGHT if ip_input else BLUE, 8, 2)
        txt = ip_input if ip_input else "192.168.1.x"
        col = TEXT_WHITE if ip_input else TEXT_DIM
        draw_text(screen, txt, ip_box.x + 14, ip_box.centery, font_md, col)

        port_box = pygame.Rect(W // 2 - W * 0.35, H * 0.25, W * 0.70, 52)
        draw_panel(screen, port_box, (25, 28, 38), BLUE, 8, 2)
        draw_text(screen, f"端口: {port_input}", port_box.x + 14,
                  port_box.centery, font_md, TEXT_WHITE)

        # 屏幕数字键盘（Pydroid 软键盘弹不出来时用）
        key_labels = ["1", "2", "3", "4", "5", "6",
                      "7", "8", "9", ".", "0", "⌫"]
        key_w = W * 0.14
        key_h = H * 0.052
        gap_x = W * 0.012
        gap_y = H * 0.008
        total_w = 6 * key_w + 5 * gap_x
        start_x = W // 2 - total_w // 2
        start_y = H * 0.34
        for idx, label in enumerate(key_labels):
            row = idx // 6
            col = idx % 6
            kx = start_x + col * (key_w + gap_x)
            ky = start_y + row * (key_h + gap_y)
            kr = pygame.Rect(int(kx), int(ky), int(key_w), int(key_h))
            hovered = kr.collidepoint(mouse_pos)
            if label == "⌫":
                draw_button(screen, kr,
                            (95, 40, 40) if hovered else (60, 25, 25),
                            RED, 6)
                draw_text(screen, label, kr.centerx, kr.centery,
                          font_lg, TEXT_WHITE, True)
            else:
                draw_button(screen, kr,
                            (45, 60, 90) if hovered else (30, 40, 60),
                            BLUE, 6)
                draw_text(screen, label, kr.centerx, kr.centery,
                          font_lg, TEXT_WHITE, True)

        connect_btn = pygame.Rect(W // 2 - W * 0.15, H * 0.54, W * 0.30, 52)
        hovered = connect_btn.collidepoint(mouse_pos)
        draw_button(screen, connect_btn,
                    (45, 85, 45) if hovered else (30, 60, 30), GREEN_HP, 8)
        draw_text(screen, "连接", connect_btn.centerx, connect_btn.centery,
                  font_md, TEXT_WHITE, True)

        back_btn = pygame.Rect(W // 2 - W * 0.15, H * 0.66, W * 0.30, 52)
        hovered = back_btn.collidepoint(mouse_pos)
        draw_button(screen, back_btn,
                    (75, 40, 40) if hovered else (50, 25, 25), RED, 8)
        draw_text(screen, "返回", back_btn.centerx, back_btn.centery,
                  font_md, TEXT_WHITE, True)

        draw_text(screen, status_msg, W // 2, H * 0.78, font_md, ORANGE_TIMER, True)
        draw_text(screen, "点上面数字键输入 IP，⌫ 删除",
                  W // 2, H * 0.85, font_sm, TEXT_DIM, True)
        return None, None, back_btn, connect_btn


def _apply_nightmare_ai(gs):
    """噩梦模式：7名对手全部使用当前最强AI（离线训练出的全局最优）。
    对局结算照常记录玩家信息（_record_player_game(gs, '噩梦')），供AI自我升级。"""
    ai_params = dict(EXTREME_AI_PARAMS)
    mult = DIFFICULTY_MULT.get("nightmare", 1.75)
    for ai in gs.players:
        ai["difficulty_mult"] = mult
        ai["_override_params"] = dict(ai_params)
        ai["_extreme_chase"] = True   # 噩梦AI开启三星五费博弈标记
        _apply_learned_style(ai)      # 学习玩家运营（开关受 _LEARN_PLAYER_STYLE 控制）
    gs.battle_log = "噩梦模式 · 7名对手均为当前最强AI · 击败它们证明你的实力！"


def _apply_congrats_mode(gs):
    """恭喜发财：全员噩梦最强AI + 开局五费 + 大妮蔻狂欢（阶段6保底/50血保底）。
    开局选秀3个候选全部为5费；玩家自选1张，AI各随机1张，保证开局公平。"""
    _apply_nightmare_ai(gs)
    gs._congrats_mode = True
    gs._congrats_neeko_given = False
    gs._congrats_50hp_given = False
    # AI：清掉开局1费（还给卡池），换成随机五费
    for ai in gs.players:
        for i, u in enumerate(ai["bench"]):
            if u is not None:
                return_pool(u.get("name", ""), 1)
                ai["bench"][i] = None
        _give_congrats_start_unit(ai)
    # 玩家：开局选秀3个候选改为5费（玩家自选1张；不额外发随机五费，保证与AI公平）
    five = _congrats_five_cost_list()
    avail = [c for c in five if pool_remaining(c["name"]) > 0]
    if len(avail) < 3:
        avail = five
    gs.starter_choices = random.sample(avail, min(3, len(avail)))
    gs.battle_log = "恭喜发财 · 五费开局（选秀3选1） · 全员噩梦最强AI · 大妮蔻狂欢！"


def run_game_session(screen, clock, difficulty, font_lg, font_md, font_sm,
                     font_dmg, net=None, is_host=False, load_save=False,
                     rank_mode=None, congrats_mode=False):
    gs = GameState(difficulty=difficulty, net=net, is_host=is_host)
    if difficulty == "nightmare":
        # 噩梦模式：显式把7名对手全部切换为当前最强AI
        _apply_nightmare_ai(gs)
    if congrats_mode:
        # 恭喜发财：全员噩梦最强AI + 五费开局 + 大妮蔻狂欢
        _apply_congrats_mode(gs)
    if rank_mode:
        # 排位对局：对手AI按玩家段位匹配——优先同段位训练存档AI，缺失用全局最强AI兜底
        p_rank = rank_mode.get("rank", "青铜")
        if p_rank == "王者":
            # 噩梦入侵排位：王者段位起，7名对手全部切换为当前最强噩梦AI，
            # 且沿用三星五费博弈 + 学习玩家运营（随训练突破自动升级优化）
            _apply_nightmare_ai(gs)
            gs._opp_rank = "王者"
            gs._rank_settled = False
            gs.rank_settle_text = ""
            gs._nightmare_invasion = True
            gs.battle_log = ("排位对局 · 噩梦AI入侵！王者段位对手全部为当前最强AI · "
                             "击败它们证明你配得上王者")
        else:
            ai_params, rmult, src, opp_rank = _ranked_opponent_ai(p_rank)
            for ai in gs.players:
                ai["difficulty_mult"] = rmult
                ai["_override_params"] = dict(ai_params)
            gs._opp_rank = opp_rank
            gs._rank_settled = False
            gs.rank_settle_text = ""
            gs._nightmare_invasion = False
            gs.battle_log = f"排位对局 · 对手匹配: {src}"
    if load_save and not net:
        if load_game(gs):
            gs.battle_log = "读取存档成功"
    running = True
    result = None
    while running and result is None:
        try:
            set_dbg("循环: 顶部")
            W, H = screen.get_size()
            mouse_pos = pygame.mouse.get_pos()
            dt = clock.tick(FPS) / 1000 * gs.speed
            tick_sfx_cooldown(dt)
            if getattr(gs, "_toast_timer", 0) > 0:
                gs._toast_timer -= dt
            if gs.battle_result_timer > 0:
                gs.battle_result_timer -= dt
                if gs.battle_result_timer < 0:
                    gs.battle_result_timer = 0
            if gs.show_carousel:
                gs.carousel_timer -= dt
                if gs.carousel_timer <= 0 and len(gs.carousel_options) > 0:
                    gs.pick_carousel(random.randint(0, len(gs.carousel_options) - 1))
                    gs._advance_to_next_round()

            if gs.is_multiplayer and gs.multiplayer_phase == "wait_peer":
                if not (gs.net and gs.net.connected):
                    gs.game_over = True
                    gs.game_over_text = "对手已断开"
                    play_sfx("error")
                elif time.time() - gs._wait_peer_start > 120.0:
                    gs.game_over = True
                    gs.game_over_text = "对手超时未响应"
                    play_sfx("error")
                else:
                    data = gs.net.recv(timeout=0.05)
                    if data:
                        if "my_hp" in data:
                            gs.peer_hp = data["my_hp"]
                            if gs.peer_hp <= 0 and not gs.game_over:
                                gs.game_over = True
                                gs.game_over_text = "胜利!"
                                play_sfx("victory")
                                continue
                        if data.get("ready"):
                            gs.start_battle()

            if gs.is_multiplayer and gs.multiplayer_phase == "wait_battle":
                if not (gs.net and gs.net.connected):
                    gs.game_over = True
                    gs.game_over_text = "对手已断开"
                    play_sfx("error")
                else:
                    peer_msg = gs.net.recv(timeout=0.05)
                    if peer_msg:
                        gs._setup_multiplayer_battle(peer_msg)
                    elif time.time() - gs._battle_wait_start > 20.0:
                        gs.battle_log = "等待对手超时，回到备战"
                        gs.multiplayer_phase = "prep"
                        gs._wait_peer_start = time.time()

            if gs.game_over and rank_mode and not getattr(gs, "_rank_settled", False):
                gs._rank_settled = True
                _settle_rank_match(gs, rank_mode)
            if gs.game_over:
                pass
            if gs.game_over and not getattr(gs, "_game_recorded", False):
                gs._game_recorded = True
                if gs.is_multiplayer:
                    _record_player_game(gs, "联机")
                elif rank_mode:
                    _record_player_game(gs, "排位")
                elif congrats_mode:
                    _record_player_game(gs, "恭喜发财")
                elif difficulty == "nightmare":
                    _record_player_game(gs, "噩梦")
                else:
                    _record_player_game(gs, "普通")
            elif getattr(gs, "show_starter_popup", False):
                pass
            elif getattr(gs, "show_global_augment_popup", False):
                pass
            elif getattr(gs, "show_bounty_popup", False):
                pass
            elif gs.show_carousel:
                pass
            elif gs.show_item_path_popup:
                pass
            elif gs.show_hex_popup:
                pass
            elif gs.is_multiplayer and gs.multiplayer_phase in (
                    "prep", "wait_peer", "wait_battle"):
                pass
            elif not gs.is_battle_phase:
                if gs.phase_timer < 900:
                    gs.phase_timer -= dt
                    if gs.phase_timer <= 0:
                        set_dbg("循环: 开始战斗")
                        gs.start_battle()
            else:
                set_dbg("循环: 战斗")
                gs.update_battle_tick(dt, W, H)
            set_dbg("循环: 绘制")
            rects = draw_game(screen, gs, font_lg, font_md, font_sm,
                              font_dmg, W, H, mouse_pos)
            (board_rects, bench_rects, shop_rects, refresh_rect, levelup_rect,
             gold_btn_rect, trait_btn_rect, auto_btn_rect, prev_btn_rect,
             next_btn_rect, sell_rect, hex_card_rects, battle_selector_rects,
             lock_rect, carousel_rects, item_bench_rects,
             augment_rects, starter_rects, ga_btn,
             hover_item_idx, path_btn, go_restart, go_menu) = rects
            if rank_mode and gs.game_over and getattr(gs, "rank_settle_text", ""):
                draw_text(screen, gs.rank_settle_text, W // 2, H * 0.30,
                          font_md, GOLD_COLOR, True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    result = "quit"
                    running = False
                    break

                if event.type == pygame.KEYDOWN:
                    if gs.game_over:
                        continue
                    # ESC：关闭纹章/光明/杰作选择弹窗（放弃选择，道具/伪棋子保留）
                    if event.key == pygame.K_ESCAPE \
                            and getattr(gs, "show_item_choice_popup", False):
                        gs.close_item_choice_popup()
                        play_sfx("click")
                        continue
                    if (getattr(gs, "show_starter_popup", False)
                            or getattr(gs, "show_global_augment_popup", False)
                            or getattr(gs, "show_bounty_popup", False)
                            or getattr(gs, "show_item_choice_popup", False)
                            or gs.show_carousel or gs.show_item_path_popup):
                        continue

                    if event.key == pygame.K_SPACE:
                        if (gs.is_multiplayer
                                and gs.multiplayer_phase == "prep"):
                            my_data = {
                                "board": gs.me["board"],
                                "hex_bonuses": dict(gs.me.get("hex_bonuses", {})),
                                "hex_list": list(gs.me.get("hex_list", [])),
                                "ready": True,
                            }
                            gs.net.send(my_data)
                            gs.multiplayer_phase = "wait_peer"
                            gs._wait_peer_start = time.time()
                            gs.battle_log = "等待对手准备..."
                            play_sfx("click")
                        elif not gs.is_battle_phase and gs.phase_timer < 900:
                            gs.phase_timer = 0
                        continue

                    if event.key == pygame.K_ESCAPE:
                        if getattr(gs, "show_pool_popup", False):
                            gs.show_pool_popup = False
                        elif getattr(gs, "show_odds_popup", False):
                            gs.show_odds_popup = False
                        elif gs.show_trait_popup:
                            gs.show_trait_popup = False
                        elif gs.detail_unit is not None:
                            gs.detail_unit = None
                        continue

                    if gs.is_battle_phase or gs.viewing_player_idx != -1:
                        continue

                    if event.key == pygame.K_d:
                        if gs.refresh_shop_paid():
                            play_sfx("click")
                        else:
                            play_sfx("error")
                            gs._toast_msg("金币不足!")
                            gs.ai_assistant_say("no_gold")
                        continue

                    if event.key == pygame.K_f:
                        gs.buy_xp()
                        continue

                    if event.key == pygame.K_l:
                        gs.shop_locked = not gs.shop_locked
                        play_sfx("click")
                        continue

                    if event.key == pygame.K_q:
                        if gs.players:
                            gs.viewing_player_idx -= 1
                            if gs.viewing_player_idx < -1:
                                gs.viewing_player_idx = len(gs.players) - 1
                        play_sfx("click")
                        continue

                    if event.key == pygame.K_e:
                        if gs.players:
                            gs.viewing_player_idx += 1
                            if gs.viewing_player_idx >= len(gs.players):
                                gs.viewing_player_idx = -1
                        play_sfx("click")
                        continue

                    if event.key == pygame.K_TAB:
                        gs.show_odds_popup = not gs.show_odds_popup
                        play_sfx("click")
                        continue

                    if event.key == pygame.K_p:
                        gs.show_pool_popup = not gs.show_pool_popup
                        play_sfx("click")
                        continue

                    if event.key == pygame.K_r:
                        ai_auto_position(gs.me)
                        gs.battle_log = "已自动布阵"
                        play_sfx("click")
                        continue

                    if event.key in (pygame.K_1, pygame.K_2, pygame.K_3,
                                     pygame.K_4, pygame.K_5):
                        idx = event.key - pygame.K_1
                        gs.buy_champ(idx)
                        continue

                # 滚轮：羁绊弹窗垂直滚动
                if event.type == pygame.MOUSEWHEEL and gs.show_trait_popup:
                    step = 26
                    gs._trait_scroll -= event.y * step
                    gs._trait_scroll = max(
                        0, min(gs._trait_scroll,
                               getattr(gs, "_trait_max_scroll", 0)))
                    continue

                if event.type == pygame.MOUSEWHEEL:
                    mx, my = pygame.mouse.get_pos()
                    # 鼠标在底部右侧区域时，滚轮控制状态栏
                    if my > H * 0.65 and mx > W * 0.5:
                        gs._info_scroll_y = getattr(gs, "_info_scroll_y", 0) - event.y * 20
                        continue

                # 触屏/鼠标拖动：羁绊弹窗垂直滚动（手机触屏无滚轮，靠拖动）
                if event.type == pygame.MOUSEMOTION and gs.show_trait_popup:
                    drag = getattr(gs, "_trait_drag_start", None)
                    if drag and event.buttons[0]:
                        sx, sy, sscroll = drag
                        dy = event.pos[1] - sy
                        gs._trait_scroll = max(
                            0, min(sscroll - dy,
                                   getattr(gs, "_trait_max_scroll", 0)))
                    continue

                if gs.game_over:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mx, my = event.pos
                        if go_restart and go_restart.collidepoint(mx, my):
                            play_sfx("victory")
                            result = "restart"
                            break
                        if go_menu and go_menu.collidepoint(mx, my):
                            play_sfx("click")
                            result = "menu"
                            break
                    continue
                if gs.show_item_path_popup:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mx, my = event.pos
                        if path_btn and path_btn.collidepoint(mx, my):
                            gs.show_item_path_popup = False
                            gs.item_path_id = None
                            play_sfx("click")
                        continue
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        gs.show_item_path_popup = False
                        gs.item_path_id = None
                        continue
                    continue
                if getattr(gs, "show_starter_popup", False) \
                        and event.type == pygame.MOUSEBUTTONDOWN \
                        and event.button == 1:
                    mx, my = event.pos
                    for i, r in enumerate(starter_rects):
                        if r.collidepoint(mx, my):
                            gs.pick_starter(i)
                            break
                    continue
                if getattr(gs, "show_global_augment_popup", False) \
                        and event.type == pygame.MOUSEBUTTONDOWN \
                        and event.button == 1:
                    mx, my = event.pos
                    if ga_btn and ga_btn.collidepoint(mx, my):
                        gs.confirm_global_augment()
                    continue
                if gs.show_carousel and event.type == pygame.MOUSEBUTTONDOWN \
                        and event.button == 1:
                    mx, my = event.pos
                    for i, r in enumerate(carousel_rects):
                        if r.collidepoint(mx, my):
                            gs.pick_carousel(i)
                            gs._advance_to_next_round()
                            break
                    continue
                if getattr(gs, "show_item_choice_popup", False):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mx, my = event.pos
                        close_r = getattr(gs, "_tome_close_rect", None)
                        if close_r and close_r.collidepoint(mx, my):
                            # 纹章之书：放弃选择，伪棋子保留
                            gs.close_item_choice_popup()
                            play_sfx("click")
                            continue
                        for i, r in enumerate(getattr(gs, "_item_choice_rects", [])):
                            if r.collidepoint(mx, my):
                                gs.choose_special_item_option(i)
                                break
                    continue
                if getattr(gs, "show_bounty_popup", False):
                    if (event.type == pygame.MOUSEBUTTONDOWN
                            and event.button == 1):
                        mx, my = event.pos
                        choices = getattr(gs, "_bounty_choice_rects", [])
                        if gs.bounty_layer_current == 9 and choices:
                            for idx, rect in enumerate(choices):
                                if rect.collidepoint(mx, my):
                                    gs._claim_bounty(idx)
                                    break
                            else:
                                pass
                            continue
                        cb = getattr(gs, "_bounty_claim_btn", None)
                        kb = getattr(gs, "_bounty_cont_btn", None)
                        if cb and cb.collidepoint(mx, my):
                            gs._claim_bounty()
                        elif kb and kb.collidepoint(mx, my):
                            gs._continue_bounty()
                    continue
                if (gs.show_hex_popup and event.type == pygame.MOUSEBUTTONDOWN
                        and event.button == 1):
                    mx, my = event.pos
                    for i, r in enumerate(hex_card_rects):
                        if r.collidepoint(mx, my):
                            gs.pick_hex(i)
                            break
                    continue

                if gs.is_multiplayer and gs.multiplayer_phase == "prep":
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mx, my = event.pos
                        prep_btn = pygame.Rect(W // 2 - W * 0.18,
                                                H - H * 0.10,
                                                W * 0.36, 50)
                        if prep_btn.collidepoint(mx, my):
                            my_data = {
                                "board": gs.me["board"],
                                "hex_bonuses": dict(gs.me.get("hex_bonuses", {})),
                                "hex_list": list(gs.me.get("hex_list", [])),
                                "ready": True,
                            }
                            gs.net.send(my_data)
                            gs.multiplayer_phase = "wait_peer"
                            gs._wait_peer_start = time.time()
                            gs.battle_log = "等待对手准备..."
                            play_sfx("click")
                            continue

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if gs.is_battle_phase:
                        # 战斗内：备战席面板右键出售 / 物品栏右键对详情目标使用特殊道具
                        mx, my = event.pos
                        if gs.show_battle_bench:
                            for r, bid in bench_rects:
                                if r.collidepoint(mx, my):
                                    gs.sell_unit_at("bench", bid)
                                    gs.detail_unit = None
                                    break
                            else:
                                for i, ir in enumerate(item_bench_rects):
                                    if ir.collidepoint(mx, my) \
                                            and i < len(gs.me["items"]) \
                                            and gs.detail_unit is not None \
                                            and getattr(gs, "detail_source_type", None) == "bench":
                                        it = gs.me["items"][i]
                                        if it.get("special_kind"):
                                            gs.use_special_item(
                                                it, gs.detail_unit, "bench")
                                        break
                        continue
                    if gs.viewing_player_idx != -1:
                        continue
                    mx, my = event.pos
                    used_special = False
                    for ii, ir in enumerate(item_bench_rects):
                        if ir.collidepoint(mx, my) and ii < len(gs.me.get("items", [])):
                            it = gs.me["items"][ii]
                            if it.get("special_kind") and gs.detail_unit is not None:
                                used_special = gs.use_special_item(it, gs.detail_unit)
                            break
                    if used_special:
                        continue
                    sold = False
                    for (r, bid) in bench_rects:
                        if r.collidepoint(mx, my):
                            gs.sell_unit_at("bench", bid)
                            sold = True
                            break
                    if sold:
                        continue
                    for (r, rid, cid) in board_rects:
                        if r.collidepoint(mx, my):
                            gs.sell_unit_at("board", rid, cid)
                            break
                    if gs.detail_unit is not None:
                        gs.detail_unit = None
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = event.pos
                    if gs.is_battle_phase:
                        _th2 = H * 0.088
                        _sw2 = W * 0.10
                        _sbc2 = pygame.Rect(
                            W - W * 0.22 - 8 - _sw2 - 6, 8, _sw2, _th2 - 16)
                        if _sbc2.collidepoint(mx, my):
                            gs.speed = 1.0 if gs.speed >= 3.0 else gs.speed + 1.0
                            play_sfx("click")
                            continue
                        # 备战席面板开关
                        tgl = getattr(gs, "_battle_bench_toggle_rect", None)
                        if tgl and tgl.collidepoint(mx, my):
                            gs.show_battle_bench = not gs.show_battle_bench
                            gs.detail_unit = None
                            gs.dragging = False
                            play_sfx("click")
                            continue
                        # 战斗内棋子详情弹窗：出售按钮 / 关闭
                        if gs.detail_unit is not None:
                            sell_b = getattr(gs, "_detail_sell_rect", None)
                            if sell_b and sell_b.collidepoint(mx, my):
                                du = gs.detail_unit
                                st = getattr(gs, "detail_source_type", None)
                                di1 = gs.detail_i1
                                di2 = gs.detail_i2
                                if st == "board":
                                    play_sfx("error")
                                    gs.battle_log = "战斗阶段无法出售棋盘上正在对战的棋子！"
                                    gs._toast_msg("战斗阶段无法出售棋盘上正在对战的棋子！")
                                else:
                                    gs.sell_unit_at("bench", di1)
                                gs.detail_unit = None
                                continue
                            # 点击弹窗外部关闭（弹窗实际区域 W*0.82 x H*0.72 居中）
                            popup_rect = pygame.Rect(
                                int(W * 0.09), int(H * 0.14),
                                int(W * 0.82), int(H * 0.72))
                            if not popup_rect.collidepoint(mx, my):
                                gs.detail_unit = None
                                continue
                        if gs.battle_phase_resolved:
                            gs.post_battle_timer = 0
                            continue
                        if lock_rect and lock_rect.collidepoint(mx, my):
                            gs.shop_locked = not gs.shop_locked
                            play_sfx("click")
                            continue
                        if levelup_rect and levelup_rect.collidepoint(mx, my):
                            gs.buy_xp()
                            continue
                        if refresh_rect and refresh_rect.collidepoint(mx, my):
                            if gs.refresh_shop_paid():
                                play_sfx("click")
                            else:
                                play_sfx("error")
                                gs._toast_msg("金币不足!")
                                gs.ai_assistant_say("no_gold")
                            continue
                        bought = False
                        for (sr, sid) in shop_rects:
                            if sr.collidepoint(mx, my):
                                gs.buy_champ(sid)
                                bought = True
                                break
                        if bought:
                            continue
                        # 战斗备战席面板：点击备战席/物品栏/出售区
                        panel_clicked = False
                        if gs.show_battle_bench:
                            for r, bid in bench_rects:
                                if r.collidepoint(mx, my):
                                    panel_clicked = True
                                    u = gs.me["bench"][bid]
                                    if u is not None and not u.get("is_pseudo_bench_only"):
                                        gs.detail_unit = u
                                        gs.detail_source_type = "bench"
                                        gs.detail_i1 = bid
                                        gs.detail_i2 = -1
                                        play_sfx("click")
                                    break
                            for i, ir in enumerate(item_bench_rects):
                                if ir.collidepoint(mx, my) \
                                        and i < len(gs.me["items"]):
                                    panel_clicked = True
                                    gs.dragging_item = gs.me["items"][i]
                                    gs.dragging_item_idx = i
                                    gs.item_click_start = (mx, my, i)
                                    play_sfx("click")
                                    break
                            if getattr(gs, "_battle_sell_rect", None) \
                                    and gs._battle_sell_rect.collidepoint(mx, my):
                                panel_clicked = True
                        # 点击己方战斗单位 → 打开详情弹窗（战斗棋盘棋子不可出售）
                        for r, bu in gs._battle_ally_hit_rects:
                            if r.collidepoint(mx, my):
                                panel_clicked = True
                                if bu.source_unit is not None:
                                    gs.detail_unit = bu.source_unit
                                    gs.detail_source_type = "board"
                                    gs.detail_i1, gs.detail_i2 = bu.source_coords
                                play_sfx("click")
                                break
                        if panel_clicked:
                            continue
                        for r, idx in battle_selector_rects:
                            if r.collidepoint(mx, my):
                                gs.watched_battle_idx = idx
                                play_sfx("click")
                                break
                        continue
                    if gs.show_trait_popup:
                        # 点击弹窗内：进入拖动滚动（不关闭）；点击弹窗外：关闭
                        _tp_rect = getattr(gs, "_trait_popup_rect", None)
                        if _tp_rect and _tp_rect.collidepoint(mx, my):
                            gs._trait_drag_start = (mx, my,
                                                    getattr(gs, "_trait_scroll", 0))
                        else:
                            gs.show_trait_popup = False
                            gs._trait_drag_start = None
                            play_sfx("click")
                        continue
                    if gs.show_odds_popup:
                        gs.show_odds_popup = False
                        play_sfx("click")
                        continue
                    if gs.show_pool_popup:
                        gs.show_pool_popup = False
                        play_sfx("click")
                        continue
                    if gs.detail_unit is not None:
                        # 详情弹窗底部【出售】按钮（备战/战斗弹窗统一带出售）
                        sell_b = getattr(gs, "_detail_sell_rect", None)
                        if sell_b and sell_b.collidepoint(mx, my):
                            st = getattr(gs, "detail_source_type", None)
                            di1 = gs.detail_i1
                            di2 = gs.detail_i2
                            if st == "board":
                                gs.sell_unit_at("board", di1, di2)
                            else:
                                gs.sell_unit_at("bench", di1)
                            gs.detail_unit = None
                            play_sfx("click")
                            continue
                        # 点已装备图标 → 打开该装备详情
                        for (ir, eq_item) in getattr(gs, "_detail_equip_hits", []):
                            if ir.collidepoint(mx, my):
                                gs.show_item_path_popup = True
                                gs.item_path_id = copy.deepcopy(eq_item)
                                play_sfx("click")
                                break
                        else:
                            gs.detail_unit = None
                            play_sfx("click")
                        continue
                    gs.mouse_down_pos = (mx, my)
                    top_h = H * 0.088
                    spd_w = W * 0.10
                    spd_click = pygame.Rect(
                        W - W * 0.22 - 8 - spd_w - 6, 8, spd_w, top_h - 16)
                    if spd_click.collidepoint(mx, my):
                        gs.speed = 1.0 if gs.speed >= 3.0 else gs.speed + 1.0
                        play_sfx("click")
                        continue
                    lv_box_click = pygame.Rect(8, 8, W * 0.20, top_h - 16)
                    if lv_box_click.collidepoint(mx, my) \
                            and gs.viewing_player_idx == -1:
                        gs.show_odds_popup = not gs.show_odds_popup
                        play_sfx("click")
                        continue
                    if lock_rect and lock_rect.collidepoint(mx, my):
                        gs.shop_locked = not gs.shop_locked
                        play_sfx("click")
                        continue
                    if (levelup_rect and levelup_rect.collidepoint(mx, my)
                            and gs.viewing_player_idx == -1):
                        gs.buy_xp()
                        continue
                    if (refresh_rect and refresh_rect.collidepoint(mx, my)
                            and gs.viewing_player_idx == -1):
                        if gs.refresh_shop_paid():
                            play_sfx("click")
                        else:
                            play_sfx("error")
                            gs._toast_msg("金币不足!")
                            gs.ai_assistant_say("no_gold")
                        continue
                    if trait_btn_rect and trait_btn_rect.collidepoint(mx, my):
                        if not gs.show_trait_popup:
                            gs._trait_scroll = 0
                        gs.show_trait_popup = not gs.show_trait_popup
                        play_sfx("click")
                        continue
                    if auto_btn_rect and auto_btn_rect.collidepoint(mx, my) \
                            and gs.viewing_player_idx == -1:
                        ai_auto_position(gs.me)
                        gs.battle_log = "已自动布阵"
                        play_sfx("click")
                        continue
                    if prev_btn_rect and prev_btn_rect.collidepoint(mx, my):
                        if gs.players:
                            gs.viewing_player_idx -= 1
                            if gs.viewing_player_idx < -1:
                                gs.viewing_player_idx = len(gs.players) - 1
                        play_sfx("click")
                        continue
                    if next_btn_rect and next_btn_rect.collidepoint(mx, my):
                        if gs.players:
                            gs.viewing_player_idx += 1
                            if gs.viewing_player_idx >= len(gs.players):
                                gs.viewing_player_idx = -1
                        play_sfx("click")
                        continue
                    if gs.viewing_player_idx == -1:
                        for i, ir in enumerate(item_bench_rects):
                            if ir.collidepoint(mx, my) and i < len(gs.me["items"]):
                                gs.dragging_item = gs.me["items"][i]
                                gs.dragging_item_idx = i
                                gs.item_click_start = (mx, my, i)
                                play_sfx("click")
                                break
                    if gs.viewing_player_idx == -1:
                        view_player = gs.me
                        can_drag = True
                    else:
                        view_player = gs.players[gs.viewing_player_idx]
                        can_drag = False
                    hit = False
                    for (r, bid) in bench_rects:
                        if r.collidepoint(mx, my):
                            unit = view_player["bench"][bid]
                            if unit is not None:
                                if gs.dragging_item is not None and \
                                        gs.viewing_player_idx == -1:
                                    gs.equip_item_to(gs.dragging_item,
                                                     "bench", bid)
                                    gs.dragging_item = None
                                    gs.dragging_item_idx = -1
                                    gs.item_click_start = None
                                elif can_drag:
                                    gs.dragging = True
                                    gs.drag_source_type = "bench"
                                    gs.drag_idx1 = bid
                                    gs.drag_idx2 = -1
                                    gs.drag_unit = unit
                                else:
                                    gs.detail_unit = unit
                                    gs.detail_source_type = "bench"
                                    gs.detail_i1 = bid
                                    gs.detail_i2 = -1
                            hit = True
                            break
                    if hit:
                        continue
                    for (r, rid, cid) in board_rects:
                        if r.collidepoint(mx, my):
                            unit = view_player["board"][rid][cid]
                            if unit is not None:
                                if gs.dragging_item is not None and \
                                        gs.viewing_player_idx == -1:
                                    gs.equip_item_to(gs.dragging_item,
                                                     "board", rid, cid)
                                    gs.dragging_item = None
                                    gs.dragging_item_idx = -1
                                    gs.item_click_start = None
                                elif can_drag:
                                    gs.dragging = True
                                    gs.drag_source_type = "board"
                                    gs.drag_idx1 = rid
                                    gs.drag_idx2 = cid
                                    gs.drag_unit = unit
                                else:
                                    gs.detail_unit = unit
                                    gs.detail_source_type = "board"
                                    gs.detail_i1 = rid
                                    gs.detail_i2 = cid
                            hit = True
                            break
                    if hit:
                        continue
                    if gs.viewing_player_idx == -1:
                        for (sr, sid) in shop_rects:
                            if sr.collidepoint(mx, my):
                                gs.buy_champ(sid)
                                break
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    # 结束羁绊弹窗拖动滚动
                    gs._trait_drag_start = None
                    if gs.dragging_item is not None:
                        mx, my = event.pos
                        moved = False
                        if getattr(gs, "item_click_start", None):
                            sx, sy, _ = gs.item_click_start
                            dist = ((mx - sx) ** 2 + (my - sy) ** 2) ** 0.5
                            if dist >= DRAG_THRESHOLD:
                                moved = True
                        item_id = gs.dragging_item.get("id", "")
                        is_comb = gs.dragging_item.get("is_combined", False)
                        if not moved:
                            gs.show_item_path_popup = True
                            gs.item_path_id = copy.deepcopy(gs.dragging_item)
                            gs.dragging_item = None
                            gs.dragging_item_idx = -1
                            gs.item_click_start = None
                            continue
                        placed = False
                        if gs.is_battle_phase:
                            # 战斗内：拖到己方战斗单位 = 仅佩戴（不可拆卸、不可合成）
                            for r, bu in gs._battle_ally_hit_rects:
                                if r.collidepoint(mx, my) \
                                        and bu.source_unit is not None:
                                    gs.equip_item_to(gs.dragging_item, "board",
                                                     bu.source_coords[0],
                                                     bu.source_coords[1],
                                                     allow_combine=False)
                                    placed = True
                                    break
                            if not placed:
                                # 战斗备战席面板：完整操作（合成/拆卸/重铸）
                                for r, bid in bench_rects:
                                    if r.collidepoint(mx, my):
                                        gs.equip_item_to(gs.dragging_item,
                                                         "bench", bid)
                                        placed = True
                                        break
                        else:
                            # 备战阶段：物品栏内两个散件拖拽重叠直接合成
                            for i, ir in enumerate(item_bench_rects):
                                if ir.collidepoint(mx, my):
                                    if i != gs.dragging_item_idx:
                                        gs.try_combine_item_bench(
                                            gs.dragging_item_idx, i)
                                        placed = True
                                    break
                        if not placed:
                            for (r, bid) in bench_rects:
                                if r.collidepoint(mx, my):
                                    if gs.viewing_player_idx == -1:
                                        u = gs.me["bench"][bid]
                                        if u is not None and u.get("is_pseudo_bench_only"):
                                            # 纹章之书伪棋子不可装备
                                            play_sfx("error")
                                            gs._toast_msg("纹章之书不能装备道具")
                                        else:
                                            gs.equip_item_to(gs.dragging_item,
                                                             "bench", bid)
                                    placed = True
                                    break
                        if not placed:
                            for (r, rid, cid) in board_rects:
                                if r.collidepoint(mx, my):
                                    if gs.viewing_player_idx == -1:
                                        gs.equip_item_to(gs.dragging_item,
                                                         "board", rid, cid)
                                    placed = True
                                    break
                        gs.dragging_item = None
                        gs.dragging_item_idx = -1
                        gs.item_click_start = None
                        continue
                    if not gs.dragging:
                        continue
                    mx, my = event.pos
                    down_x, down_y = gs.mouse_down_pos
                    dist = ((mx - down_x) ** 2 + (my - down_y) ** 2) ** 0.5
                    if dist < DRAG_THRESHOLD:
                        gs.detail_unit = gs.drag_unit
                        gs.dragging = False
                        gs.drag_unit = None
                        play_sfx("click")
                        continue
                    st, i1, i2 = gs.drag_source_type, gs.drag_idx1, gs.drag_idx2
                    if sell_rect and sell_rect.collidepoint(mx, my):
                        if gs.viewing_player_idx == -1:
                            gs.sell_unit_at(st, i1, i2)
                        gs.dragging = False
                        gs.drag_unit = None
                        continue
                    target_bench = next(
                        (bid for (r, bid) in bench_rects if r.collidepoint(mx, my)), -1)
                    if target_bench != -1:
                        if gs.drag_unit is not None \
                                and gs.drag_unit.get("is_pseudo_bench_only"):
                            # 纹章之书伪棋子不允许拖拽移动（仅可出售触发弹窗）
                            play_sfx("error")
                            gs._toast_msg("纹章之书仅可出售，不能移动")
                            gs.dragging = False
                            gs.drag_unit = None
                            continue
                        if st == "bench":
                            gs.me["bench"][i1], gs.me["bench"][target_bench] = \
                                gs.me["bench"][target_bench], gs.me["bench"][i1]
                        elif st == "board":
                            gs.me["bench"][target_bench] = gs.me["board"][i1][i2]
                            gs.me["board"][i1][i2] = None
                        gs.try_combine(gs.me)
                        enforce_population_cap(gs.me)
                        gs.dragging = False
                        gs.drag_unit = None
                        continue
                    target_board = None
                    for (r, rid, cid) in board_rects:
                        if r.collidepoint(mx, my):
                            target_board = (rid, cid)
                            break
                    if target_board:
                        tr, tc = target_board
                        if gs.drag_unit is not None \
                                and gs.drag_unit.get("is_pseudo_bench_only"):
                            # 纹章之书伪棋子禁止上棋盘
                            play_sfx("error")
                            gs._toast_msg("纹章之书不能上棋盘")
                            gs.dragging = False
                            gs.drag_unit = None
                            continue
                        if st == "bench":
                            if count_board_units(gs.me) >= get_population_cap(gs.me) and \
                                    gs.me["board"][tr][tc] is None:
                                gs.dragging = False
                                gs.drag_unit = None
                                gs._toast_msg("人口已满! 请先升级")
                                continue
                            old_unit = gs.me["board"][tr][tc]
                            gs.me["board"][tr][tc] = gs.me["bench"][i1]
                            gs.me["bench"][i1] = old_unit
                        elif st == "board":
                            gs.me["board"][i1][i2], gs.me["board"][tr][tc] = \
                                gs.me["board"][tr][tc], gs.me["board"][i1][i2]
                        gs.try_combine(gs.me)
                        enforce_population_cap(gs.me)
                        gs.dragging = False
                        gs.drag_unit = None
                        continue
                    gs.dragging = False
                    gs.drag_unit = None
            pygame.display.flip()
        except Exception as e:
            traceback.print_exc()
            err_lines = traceback.format_exc().split("\n")
            err_short = ""
            for line in err_lines:
                if line.strip():
                    err_short = line.strip()[:80]
            set_dbg(f"错误: {err_short}")
            try:
                draw_text(screen, f"错误: {err_short}", W // 2, H // 2,
                          font_lg, (255, 80, 80), align_center=True)
                pygame.display.flip()
            except Exception:
                pass
            pygame.time.wait(2000)
    return result if result else "menu"


def _thunder_skill(unit, allies, enemies, effect_list):
    import random as _rd
    name = unit.base["name"]
    star = unit.base.get("star", 1)
    star_scale = SKILL_DMG_STAR_SCALE.get(star, SKILL_DMG_STAR_SCALE[4])
    sp_val = int(unit.base["sp_base_dmg"] * unit.base["sp_multiplier"]
                 * star_scale * unit.sp_buff)

    if name == "ThunderHelper":
        # 1费：随机四选一，威力按 0.8 折算
        roll = _rd.randint(1, 4)
        dmg = int(sp_val * 0.8)
        if roll == 1:
            heal_val = int(dmg * 0.6)
            unit.current_hp = min(unit.base["hp"], unit.current_hp + heal_val)
            effect_list.append({"type": "damage_pop", "x": unit.x, "y": unit.y,
                                "text": f"种土豆+{heal_val}", "life": 1.5,
                                "max_life": 1.5, "kind": "heal"})
        elif roll == 2:
            target = unit._pick_nearest(enemies)
            if target:
                target.take_damage(dmg, source=unit, dmg_type="magic")
                target.attack_cd_remain += 2.0
                effect_list.append({"type": "damage_pop", "x": target.x, "y": target.y,
                                    "text": f"在吗? {dmg}", "life": 1.5,
                                    "max_life": 1.5, "kind": "skill"})
        elif roll == 3:
            per = int(dmg * 0.7)
            for e in enemies:
                if e.alive:
                    e.take_damage(per, source=unit, dmg_type="magic")
            effect_list.append({"type": "screen_flash", "life": 0.3, "max_life": 0.3,
                                "color": (100, 255, 100)})
            effect_list.append({"type": "damage_pop", "x": unit.x, "y": unit.y - 20,
                                "text": "// 完美无缺", "life": 2.0,
                                "max_life": 2.0, "kind": "shield"})
        else:
            for a in allies:
                if a.alive and a is not unit:
                    a.add_mana(a.base["max_mana"] * 0.3)
                    effect_list.append({"type": "damage_pop", "x": a.x, "y": a.y - 20,
                                        "text": "摸鱼回蓝", "life": 1.5,
                                        "max_life": 1.5, "kind": "shield"})
                    break

    elif name == "ThunderLicker":
        target = unit._pick_nearest(enemies)
        if target:
            target.take_damage(sp_val, source=unit, dmg_type="magic")
            target.attack_cd_remain += 2.0
            effect_list.append({"type": "damage_pop", "x": target.x, "y": target.y,
                                "text": f"在吗? {sp_val}", "life": 1.5,
                                "max_life": 1.5, "kind": "skill"})

    elif name == "ThunderComment":
        per = int(sp_val * 0.75)
        for e in enemies:
            if e.alive:
                e.take_damage(per, source=unit, dmg_type="magic")
        effect_list.append({"type": "screen_flash", "life": 0.3, "max_life": 0.3,
                            "color": (100, 255, 100)})
        effect_list.append({"type": "damage_pop", "x": unit.x, "y": unit.y - 20,
                            "text": f"// 完美无缺 {per}", "life": 2.0,
                            "max_life": 2.0, "kind": "shield"})

    elif name == "ThunderPotato":
        heal_val = int(sp_val * 0.6)
        unit.current_hp = min(unit.base["hp"], unit.current_hp + heal_val)
        shield_val = int(sp_val * 0.5)
        for a in allies:
            if a.alive and (a.x - unit.x) ** 2 + (a.y - unit.y) ** 2 < 200 ** 2:
                a.shield += shield_val
                effect_list.append({"type": "damage_pop", "x": a.x, "y": a.y,
                                    "text": f"+{shield_val}", "life": 1.4,
                                    "max_life": 1.4, "kind": "shield"})
        effect_list.append({"type": "damage_pop", "x": unit.x, "y": unit.y - 30,
                            "text": f"种土豆+{heal_val}", "life": 1.5,
                            "max_life": 1.5, "kind": "heal"})

    elif name == "ThunderGoddess":
        target = unit._pick_skill_target(enemies)
        if target:
            target.take_damage(sp_val, source=unit, dmg_type="magic")
            effect_list.append({"type": "damage_pop", "x": target.x, "y": target.y,
                                "text": f"你有病吧! {sp_val}", "life": 1.5,
                                "max_life": 1.5, "kind": "crit"})

    else:
        per = int(sp_val * 0.7)
        for e in enemies:
            if e.alive:
                e.take_damage(per, source=unit, dmg_type="magic")
        shield_val = int(sp_val * 0.4)
        unit.shield += shield_val
        effect_list.append({"type": "damage_pop", "x": unit.x, "y": unit.y - 30,
                            "text": f"更新补丁! {per}", "life": 1.5,
                            "max_life": 1.5, "kind": "skill"})
        effect_list.append({"type": "damage_pop", "x": unit.x, "y": unit.y - 10,
                            "text": f"+{shield_val}盾", "life": 1.5,
                            "max_life": 1.5, "kind": "shield"})

    unit.current_mana = 0
    unit.skill_cd_remain = unit.skill_cd_total
    unit.state = "skill"
    unit.anim_timer = 0.5


def main():
    global _TRAINING_GIVE_WAY, _LEARN_PLAYER_STYLE
    pygame.init()
    info = pygame.display.Info()
    if info.current_w > info.current_h and info.current_w >= 900:
        W = min(1440, max(900, info.current_w - 80))
        H = min(900, max(600, info.current_h - 120))
    else:
        W = MIN_W
        H = MIN_H
    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    pygame.display.set_caption("豹药宇宙")
    clock = pygame.time.Clock()
    _find_cjk_font()
    font_title = get_font(76)
    font_lg = get_font(36)
    font_md = get_font(28)
    font_sm = get_font(22)
    font_dmg = get_font(34)
    scene = "menu"
    difficulty = "normal"
    nightmare_mode = False  # 挑战最强AI对局标志：只影响当次对局，不改变主菜单难度
    congrats_mode = False   # 恭喜发财对局标志：五费开局+大妮蔻狂欢+全员噩梦AI
    running = True

    net = None
    lobby_mode = "choose"
    ip_input = ""
    port_input = "5555"
    status_msg = ""
    is_host = False
    changelog_open = False
    want_load = False
    update_check_state = "idle"
    update_info = None
    update_status = ""
    update_popup_open = False
    update_lock = threading.Lock()
    train_popup_open = False
    train_stop_event = threading.Event()
    rank_match_rank = None

    def _do_check_update():
        nonlocal update_check_state, update_info, update_status
        info = check_for_update()
        with update_lock:
            update_info = info
            update_check_state = "done"
            update_status = "" if info else "已是最新版本"

    def _do_download_update(url):
        nonlocal update_status, update_check_state
        path = get_script_path()
        ok, err = download_update(url, path)
        with update_lock:
            if ok:
                update_status = "下载完成，请重启游戏生效"
            else:
                update_status = f"下载失败: {err}"
            update_check_state = "done"

    while running:
        W, H = screen.get_size()
        mouse_pos = pygame.mouse.get_pos()
        dt = clock.tick(FPS) / 1000
        tick_sfx_cooldown(dt)
        # 前台打对局时让训练线程让步，保证游玩流畅；菜单/设置时训练全速
        _TRAINING_GIVE_WAY = (scene == "game")
        if scene == "menu":
            set_dbg("场景: 主菜单")
            (continue_btn, start_btn, multi_btn, rank_btn, challenge_btn,
             congrats_btn, update_btn, train_btn, settings_btn, quit_btn) = draw_main_menu(
                screen, font_title, font_lg, font_md, font_sm, W, H,
                mouse_pos, difficulty)
            # 训练线程存活检测：避免“显示训练中但实际已死”卡住界面
            _check_training_worker()
            upd_close = upd_apply = None
            train_btn_primary = train_btn_secondary = None
            if train_popup_open:
                train_btn_primary, train_btn_secondary = draw_training_popup(
                    screen, font_lg, font_md, font_sm, W, H, mouse_pos,
                    _TRAINING_STATE)
            if update_popup_open:
                with update_lock:
                    _info = update_info
                    _stat = update_status
                upd_close, upd_apply = draw_update_popup(
                    screen, font_lg, font_md, font_sm, W, H, mouse_pos,
                    _info, _stat)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if train_popup_open:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        train_popup_open = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mx, my = event.pos
                        if train_btn_primary and train_btn_primary.collidepoint(mx, my):
                            if _TRAINING_STATE.get("running", False):
                                # 停止训练
                                train_stop_event.set()
                                play_sfx("click")
                            else:
                                # 开始/继续训练（有存档则自动续上上次进度）
                                train_stop_event.clear()
                                _TRAINING_STATE["running"] = True
                                t = threading.Thread(
                                    target=_training_worker,
                                    args=(train_stop_event,), daemon=True)
                                _TRAINING_STATE["worker_thread"] = t
                                t.start()
                                play_sfx("buy")
                        elif train_btn_secondary and train_btn_secondary.collidepoint(mx, my):
                            # 训练中=隐藏窗口(后台继续)；已停止=关闭弹窗
                            train_popup_open = False
                            play_sfx("click")
                    continue
                if update_popup_open:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        update_popup_open = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mx, my = event.pos
                        if upd_close and upd_close.collidepoint(mx, my):
                            update_popup_open = False
                            play_sfx("click")
                        elif upd_apply and upd_apply.collidepoint(mx, my):
                            with update_lock:
                                _info2 = update_info
                            if _info2 and _info2.get("download_url"):
                                with update_lock:
                                    update_status = "正在下载..."
                                t = threading.Thread(
                                    target=_do_download_update,
                                    args=(_info2["download_url"],),
                                    daemon=True)
                                t.start()
                            else:
                                with update_lock:
                                    update_status = "缺少下载链接"
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = event.pos
                    if continue_btn and continue_btn.collidepoint(mx, my):
                        play_sfx("buy")
                        want_load = True
                        scene = "game"
                    elif start_btn.collidepoint(mx, my):
                        play_sfx("buy")
                        want_load = False
                        scene = "game"
                    elif multi_btn.collidepoint(mx, my):
                        play_sfx("click")
                        net = None
                        lobby_mode = "choose"
                        ip_input = ""
                        port_input = "5555"
                        status_msg = ""
                        scene = "lobby"
                    elif rank_btn.collidepoint(mx, my):
                        play_sfx("buy")
                        # 先进入排位赛专属页面，由页面内「开始对战」进入排位对局
                        scene = "rank_page"
                    elif challenge_btn.collidepoint(mx, my):
                        play_sfx("buy")
                        # 挑战最强AI：专属页面 → 噩梦模式（7名对手全为最强AI）
                        scene = "challenge_page"
                    elif congrats_btn.collidepoint(mx, my):
                        play_sfx("buy")
                        # 恭喜发财：专属页面 → 五费开局+大妮蔻狂欢
                        scene = "congrats_page"
                    elif train_btn.collidepoint(mx, my):
                        play_sfx("click")
                        update_popup_open = False
                        train_popup_open = True
                    elif update_btn.collidepoint(mx, my):
                        play_sfx("click")
                        train_popup_open = False
                        update_popup_open = True
                        with update_lock:
                            update_info = None
                            if not UPDATE_CHECK_URL:
                                update_status = "尚未配置更新源"
                                update_check_state = "done"
                            else:
                                update_status = "正在检测..."
                                update_check_state = "checking"
                        if UPDATE_CHECK_URL:
                            t = threading.Thread(target=_do_check_update, daemon=True)
                            t.start()
                    elif settings_btn.collidepoint(mx, my):
                        play_sfx("click")
                        changelog_open = False
                        scene = "settings"
                    elif quit_btn.collidepoint(mx, my):
                        running = False
            pygame.display.flip()
        elif scene == "rank_page":
            set_dbg("场景: 排位赛")
            rk_start, rk_back = draw_rank_page(
                screen, font_title, font_lg, font_md, font_sm, W, H,
                mouse_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = event.pos
                    if rk_start and rk_start.collidepoint(mx, my):
                        play_sfx("buy")
                        rank_match_rank = RANK_STATE["rank"]
                        want_load = False
                        scene = "game"
                    elif rk_back and rk_back.collidepoint(mx, my):
                        play_sfx("click")
                        scene = "menu"
            pygame.display.flip()
        elif scene == "challenge_page":
            set_dbg("场景: 挑战最强AI")
            cg_start, cg_back = draw_challenge_page(
                screen, font_title, font_lg, font_md, font_sm, W, H,
                mouse_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = event.pos
                    if cg_start and cg_start.collidepoint(mx, my):
                        play_sfx("buy")
                        nightmare_mode = True
                        congrats_mode = False
                        rank_match_rank = None
                        want_load = False
                        scene = "game"
                    elif cg_back and cg_back.collidepoint(mx, my):
                        play_sfx("click")
                        scene = "menu"
            pygame.display.flip()
        elif scene == "congrats_page":
            set_dbg("场景: 恭喜发财")
            cf_start, cf_back = draw_congrats_page(
                screen, font_title, font_lg, font_md, font_sm, W, H,
                mouse_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = event.pos
                    if cf_start and cf_start.collidepoint(mx, my):
                        play_sfx("buy")
                        congrats_mode = True
                        nightmare_mode = False
                        rank_match_rank = None
                        want_load = False
                        scene = "game"
                    elif cf_back and cf_back.collidepoint(mx, my):
                        play_sfx("click")
                        scene = "menu"
            pygame.display.flip()
        elif scene == "settings":
            set_dbg("场景: 设置")
            diff_rects, back_btn, changelog_btn, learn_btn, clear_btn = draw_settings_menu(
                screen, font_title, font_lg, font_md, font_sm, W, H,
                mouse_pos, difficulty)
            cl_close = None
            if changelog_open:
                cl_close = draw_changelog_popup(
                    screen, font_lg, font_md, font_sm, W, H, mouse_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if changelog_open:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        changelog_open = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mx, my = event.pos
                        if cl_close and cl_close.collidepoint(mx, my):
                            changelog_open = False
                            play_sfx("click")
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = event.pos
                    for r, d in diff_rects:
                        if r.collidepoint(mx, my):
                            difficulty = d
                            play_sfx("click")
                            break
                    if back_btn.collidepoint(mx, my):
                        play_sfx("click")
                        changelog_open = False
                        scene = "menu"
                    elif changelog_btn.collidepoint(mx, my):
                        changelog_open = True
                        play_sfx("click")
                    elif learn_btn.collidepoint(mx, my):
                        # 噩梦AI学习玩家运营开关
                        _LEARN_PLAYER_STYLE = not _LEARN_PLAYER_STYLE
                        play_sfx("click")
                    elif clear_btn.collidepoint(mx, my):
                        # 一键清空玩家学习样本
                        if _clear_player_history():
                            play_sfx("buy")
                        else:
                            play_sfx("error")
            pygame.display.flip()
        elif scene == "lobby":
            set_dbg(f"场景: 大厅({lobby_mode})")
            try:
                pygame.key.start_text_input()
            except Exception:
                pass
            host_btn, join_btn, back_btn, connect_btn = draw_lobby(
                screen, font_title, font_lg, font_md, font_sm,
                W, H, mouse_pos, lobby_mode, net or NetworkManager(),
                ip_input, port_input, status_msg)

            if lobby_mode == "host" and net and net.connected:
                scene = "game"
            if lobby_mode == "join" and net and net.connected:
                scene = "game"
            # 连接失败/超时反馈：不再无限停在“连接中...”
            if (lobby_mode == "join" and net
                    and getattr(net, "_connect_done", False)
                    and not net.connected):
                status_msg = f"连接失败: {net.error or '超时或无响应'}"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.TEXTINPUT and lobby_mode == "join":
                    for ch in event.text:
                        if ch.isdigit() or ch == ".":
                            if len(ip_input) < 20:
                                ip_input += ch
                if event.type == pygame.KEYDOWN and lobby_mode == "join":
                    if event.key == pygame.K_BACKSPACE:
                        ip_input = ip_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        if net and ip_input:
                            net.connect(ip_input, int(port_input or "5555"))
                            status_msg = "连接中..."
                    elif event.unicode and (event.unicode.isdigit()
                                             or event.unicode == "."):
                        if len(ip_input) < 20:
                            ip_input += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = event.pos
                    if lobby_mode == "choose":
                        if host_btn and host_btn.collidepoint(mx, my):
                            play_sfx("buy")
                            net = NetworkManager()
                            if net.start_host():
                                lobby_mode = "host"
                                is_host = True
                                status_msg = f"监听端口 {net.port}"
                            else:
                                status_msg = f"启动失败: {net.error}"
                        elif join_btn and join_btn.collidepoint(mx, my):
                            play_sfx("click")
                            net = NetworkManager()
                            lobby_mode = "join"
                            is_host = False
                            status_msg = "输入好友 IP"
                        elif back_btn and back_btn.collidepoint(mx, my):
                            play_sfx("click")
                            scene = "menu"
                    elif lobby_mode == "host":
                        if back_btn and back_btn.collidepoint(mx, my):
                            if net:
                                net.close()
                            net = None
                            lobby_mode = "choose"
                    elif lobby_mode == "join":
                        # 先检查屏幕数字键盘点击
                        key_labels = ["1", "2", "3", "4", "5", "6",
                                      "7", "8", "9", ".", "0", "⌫"]
                        key_w = W * 0.14
                        key_h = H * 0.052
                        gap_x = W * 0.012
                        gap_y = H * 0.008
                        total_w = 6 * key_w + 5 * gap_x
                        start_x = W // 2 - total_w // 2
                        start_y = H * 0.34
                        kb_handled = False
                        for idx, label in enumerate(key_labels):
                            row = idx // 6
                            col = idx % 6
                            kx = start_x + col * (key_w + gap_x)
                            ky = start_y + row * (key_h + gap_y)
                            kr = pygame.Rect(int(kx), int(ky),
                                             int(key_w), int(key_h))
                            if kr.collidepoint(mx, my):
                                if label == "⌫":
                                    ip_input = ip_input[:-1]
                                else:
                                    if len(ip_input) < 20:
                                        ip_input += label
                                play_sfx("click")
                                kb_handled = True
                                break
                        if kb_handled:
                            continue
                        # 再处理 连接 / 返回
                        if connect_btn and connect_btn.collidepoint(mx, my):
                            if net and ip_input:
                                play_sfx("click")
                                net.connect(ip_input, int(port_input or "5555"))
                                status_msg = "连接中..."
                        if back_btn and back_btn.collidepoint(mx, my):
                            play_sfx("click")
                            if net:
                                net.close()
                            net = None
                            lobby_mode = "choose"
            pygame.display.flip()
        elif scene == "game":
            set_dbg("场景: 游戏")
            result = run_game_session(
                screen, clock,
                "nightmare" if nightmare_mode else difficulty,
                font_lg, font_md, font_sm, font_dmg,
                net=net, is_host=is_host,
                load_save=want_load,
                rank_mode=({"rank": rank_match_rank}
                           if rank_match_rank else None),
                congrats_mode=congrats_mode)
            want_load = False
            nightmare_mode = False
            congrats_mode = False
            if net:
                net.close()
                net = None
            if result == "quit":
                running = False
            elif result == "restart":
                pass
            else:
                rank_match_rank = None
                if result == "menu":
                    scene = "menu"
    pygame.quit()



def run_v129_self_audit():
    """静态运行时自检：不创建窗口、不启动网络，只检查核心数据一致性。"""
    errors = []
    required_traits = {
        "PotionClan": [2,4,6,8,10], "LeopardKind": [2,4,6,8,10],
        "FrogTribe": [2,4,6], "Lumber": [3,5,8],
        "Dancer": [2,3,5], "Elder": [2,3,5],
        "Thunder": [2,4,6,8], "Treasure": [3,4,5,6,8],
    }
    for k,v in required_traits.items():
        if TRAIT_DATA.get(k) != v:
            errors.append(f"羁绊阈值 {k}")
    for name, info in THREE_STAR_5COST.items():
        if name == "Dragon":
            continue
        if not any(c.get("name") == name and c.get("cost") == 5 for c in CHAMPION_LIST):
            errors.append(f"三星五费 {name}")
    for kind in ("disassembler","haotian_hammer","masterwork_upgrader",
                 "mega_neeko","radiant_chest","emblem_tome","artifact_forge",
                 "giant_axe"):
        if kind not in SPECIAL_ITEM_DATA:
            errors.append(f"特殊装备 {kind}")
    for kind in ("leopard","potion","leopard_potion","fat_leopard","rotten_potion"):
        if kind not in RUNE_ITEM_DATA:
            errors.append(f"神符 {kind}")
    return errors

if __name__ == "__main__":
    _v129_audit_errors = run_v129_self_audit()
    if _v129_audit_errors:
        print("[v1.2.9 自检]", _v129_audit_errors)
    main()