# -*- coding: utf-8 -*-
"""
豹药宇宙 - 自走棋
Changelog:
  v1.2.8 检测更新与界面优化版
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
from collections import deque

pygame.display.init()
pygame.font.init()
AUDIO_OK = False
try:
    pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=1024)
    AUDIO_OK = True
except Exception:
    AUDIO_OK = False

FPS = 60
FIXED_BATTLE_DT = 1.0 / 60.0
MAX_FIXED_STEPS = 12
MIN_W, MIN_H = 540, 960
BG_COLOR = (14, 16, 22)
PANEL_COLOR = (35, 38, 48)
PANEL_DARK = (24, 26, 34)
TEXT_WHITE = (235, 235, 240)
TEXT_DIM = (140, 145, 155)
GOLD_COLOR = (255, 210, 90)
GOLD_DEEP = (200, 150, 40)
ORANGE_TIMER = (255, 160, 60)
GREEN_HP = (90, 220, 90)
RED = (220, 70, 70)
BLUE = (60, 110, 200)
BLUE_DEEP = (35, 65, 130)
PURPLE = (120, 70, 180)
PURPLE_DEEP = (70, 40, 110)
BLUE_MANA = (40, 160, 255)
WHITE_FLASH = (255, 255, 255)
HIGHLIGHT = (255, 240, 120)
SELL_RED = (200, 60, 60)
CRIT_COLOR = (255, 230, 60)
DAMAGE_COLOR = (255, 80, 80)
HEAL_COLOR = (80, 255, 120)
SHIELD_COLOR = (140, 200, 255)
LOCK_COLOR = (255, 200, 60)
UNLOCK_COLOR = (130, 130, 130)
BORDER_LIGHT = (70, 78, 96)
BEAR_COLOR = (200, 130, 60)
RUNE_COLOR = (140, 200, 255)
TREASURE_COLOR = (255, 200, 60)
FRONT_ROW_COLOR = (90, 45, 45)
BACK_ROW_COLOR = (40, 55, 90)
MIRROR_COLOR = (180, 130, 255)
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

DIFFICULTY_MULT = {"easy": 0.7, "normal": 1.0, "hard": 1.25, "extreme": 1.6}
DIFFICULTY_NAME = {"easy": "简单", "normal": "普通",
                    "hard": "困难", "extreme": "极限"}
DIFFICULTY_ORDER = ["easy", "normal", "hard", "extreme"]
DIFFICULTY_COLOR = {"easy": (120, 220, 120), "normal": (110, 170, 240),
                     "hard": (255, 170, 60), "extreme": (230, 80, 80)}

CURRENT_VERSION = "1.2.8"
# 更新源：填你自己的远程 version.json 地址（GitHub raw 即可）
# 留空 "" 则关闭检测更新
UPDATE_CHECK_URL = "https://raw.githubusercontent.com/sqw3340/leopard-universe/main/version.json"

CHANGELOG_TEXT = [
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
            "download_url": data.get("download_url", "") or "",
        }
    except Exception as e:
        log_once("check_for_update", e)
        return None


def download_update(url, save_path, timeout=30):
    if not url:
        return False, "下载链接为空"
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "BaoYaoUniverse"})
        tmp_path = save_path + ".new"
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read()
        if len(content) < 500:
            return False, "文件过小"
        with open(tmp_path, "wb") as f:
            f.write(content)
        try:
            if os.path.exists(save_path):
                backup = save_path + ".bak"
                if os.path.exists(backup):
                    os.remove(backup)
                os.replace(save_path, backup)
        except Exception:
            pass
        os.replace(tmp_path, save_path)
        return True, ""
    except Exception as e:
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
        return
    try:
        data = {
            "version": 1,
            "difficulty": gs.difficulty,
            "me": gs.me,
            "players": gs.players,
            "stage": gs.stage,
            "round_counter": gs.round_counter,
            "shop": gs.shop,
            "shop_locked": gs.shop_locked,
            "global_augment": gs.global_augment,
            "pool_remaining": dict(_pool_remaining),
            "battle_log_history": gs.battle_log_history[-20:],
        }
        with open(SAVE_FILE, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        log_once("save_game", e)


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


def load_game(gs):
    if not has_save():
        return False
    try:
        with open(SAVE_FILE, "rb") as f:
            data = pickle.load(f)
        gs.difficulty = data.get("difficulty", gs.difficulty)
        gs.me = data.get("me", gs.me)
        gs.players = data.get("players", gs.players)
        gs.stage = tuple(data.get("stage", (1, 1)))
        gs.round_counter = data.get("round_counter", 0)
        gs.shop = data.get("shop", [])
        gs.shop_locked = data.get("shop_locked", False)
        gs.global_augment = data.get("global_augment", gs.global_augment)
        saved_pool = data.get("pool_remaining")
        if saved_pool:
            with _pool_lock:
                _pool_remaining.clear()
                _pool_remaining.update(saved_pool)
        gs.battle_log_history = data.get("battle_log_history", [])
        gs.show_starter_popup = False
        gs.show_global_augment_popup = False
        gs.starter_chosen = True
        gs.phase_timer = PREP_DURATION
        gs.is_battle_phase = False
        gs.game_over = False
        gs.battles = []
        return True
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
            payload = pickle.dumps(data)
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
                    return None
                length = int.from_bytes(header, "big")
                if length <= 0 or length > 10_000_000:
                    return None
                self._pending_len = length
            data = self._recv_exact(self._pending_len)
            if data is None:
                return None
            self._pending_len = None
            return pickle.loads(data)
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


def init_pool():
    global _pool_remaining
    with _pool_lock:
        _pool_remaining = {}
        for c in CHAMPION_LIST:
            if c.get("no_shop"):
                continue
            _pool_remaining[c["name"]] = POOL_SIZES.get(c["cost"], 20)


def consume_pool(name, count=1):
    """Consume available shared copies safely; returns the number consumed."""
    count = max(0, int(count))
    with _pool_lock:
        if name not in _pool_remaining or count <= 0:
            return 0
        consumed = min(count, _pool_remaining[name])
        _pool_remaining[name] -= consumed
        return consumed


def try_consume_pool(name, count=1):
    """Atomically reserve copies, preventing a stale shop from overselling."""
    count = max(0, int(count))
    with _pool_lock:
        if name not in _pool_remaining or _pool_remaining[name] < count:
            return False
        _pool_remaining[name] -= count
        return True


def return_pool(name, count=1):
    count = max(0, int(count))
    with _pool_lock:
        if name not in _pool_remaining or count <= 0:
            return 0
        base = get_base_template(name)
        cap = POOL_SIZES.get(base.get("cost", 1), 20) if base else 20
        before = _pool_remaining[name]
        _pool_remaining[name] = min(cap, before + count)
        return _pool_remaining[name] - before


def pool_remaining(name):
    with _pool_lock:
        return _pool_remaining.get(name, 20)


CHAMP_NAME_CN = {
    "BearBig": "熊大", "BearTwo": "熊二", "GuangTouQiang": "光头强",
    "JiJi": "吉吉", "MaoMao": "毛毛", "FeiBo": "肥波",
    "BengBeng": "蹦蹦", "TuTu": "涂涂", "LaoE": "老鳄", "FeiFei": "肥肥",
    "Tuanzi": "团子",
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
        return pygame.mixer.Sound(buffer=buf.tobytes())
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
_sfx_cooldown = {k: 0.0 for k in
                 ("hit", "skill", "death", "sell", "hex",
                  "click", "buy", "error", "coin", "victory")}


def play_sfx(name):
    if not AUDIO_OK:
        return
    if _sfx_cooldown.get(name, 0) > 0:
        return
    snd = {"hit": SND_HIT, "skill": SND_SKILL, "death": SND_DEATH,
           "sell": SND_SELL, "hex": SND_HEX, "click": SND_CLICK,
           "buy": SND_BUY, "error": SND_ERROR, "coin": SND_COIN,
           "victory": SND_VICTORY}.get(name)
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
ITEM_IDS = list(ITEMS.keys())

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


def new_item(iid):
    return {"id": iid, "name": ITEMS[iid]["name"],
            "stats": dict(ITEMS[iid]["stats"]), "color": ITEMS[iid]["color"],
            "is_combined": False}


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
                          "color": r["color"], "is_combined": True}
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


def roll_global_augment():
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
    {"name": "FeiBo", "cost": 2, "traits": ["BearRidge", "Treasure"],
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
    {"name": "MaoMao", "cost": 2, "traits": ["BearRidge", "Treasure"],
     "role": "archer",
     "hp": 500, "ad": 62, "max_mana": 32, "mana_per_attack": 12,
     "attack_cooldown": 1.1, "sp_base_dmg": 120, "sp_multiplier": 1.5,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Banana Barrage",
     "skill_type": "damage"},
    {"name": "JiJi", "cost": 3, "traits": ["BearRidge", "Treasure"],
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
    {"name": "GuangTouQiang", "cost": 5, "traits": ["BearRidge", "Treasure"],
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
     "traits": ["PotionClan", "LeopardKind", "RuneLand"],
     "role": "warrior",
     "hp": 720, "ad": 60, "max_mana": 42, "mana_per_attack": 12,
     "attack_cooldown": 1.2, "sp_base_dmg": 165, "sp_multiplier": 1.7,
     "attack_range": RANGE_WARRIOR, "star": 1, "skill_desc": "Poison Assault",
"skill_type": "damage", "skill_dmg_type": "magic"},
    {"name": "SweatyElder", "cost": 3, "traits": ["Elder", "RuneLand"],
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
    {"name": "SuperLogger", "cost": 5, "traits": ["Lumber", "Treasure"],
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

    {"name": "RuneArcher", "cost": 3, "traits": ["RuneLand", "Treasure"],
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
    {"name": "ArcaneLord", "cost": 5, "traits": ["RuneLand", "Treasure"],
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
    {"name": "FrogBulwark", "cost": 2, "traits": ["FrogTribe", "RuneLand"], "role": "tank",
     "hp": 900, "ad": 45, "max_mana": 44, "mana_per_attack": 10,
     "attack_cooldown": 1.45, "sp_base_dmg": 175, "sp_multiplier": 1.5,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Gel Shield",
     "skill_type": "drain"},
    {"name": "BearFortress", "cost": 3, "traits": ["BearRidge"], "role": "tank",
     "hp": 1080, "ad": 55, "max_mana": 48, "mana_per_attack": 10,
     "attack_cooldown": 1.45, "sp_base_dmg": 220, "sp_multiplier": 1.7,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Roar Guard",
     "skill_type": "shield"},
    {"name": "PotionKeep", "cost": 3, "traits": ["PotionClan", "RuneLand"], "role": "tank",
     "hp": 1050, "ad": 48, "max_mana": 46, "mana_per_attack": 10,
     "attack_cooldown": 1.5, "sp_base_dmg": 230, "sp_multiplier": 1.7,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Vial Fortress",
     "skill_type": "shield", "skill_dmg_type": "magic"},
    {"name": "ThornGuard", "cost": 4, "traits": ["LeopardKind", "RuneLand"], "role": "tank",
     "hp": 1220, "ad": 58, "max_mana": 50, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 280, "sp_multiplier": 1.8,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Thorn Burst",
     "skill_type": "burst_shield"},
    {"name": "OxBastion", "cost": 4, "traits": ["Lumber", "RuneLand"], "role": "tank",
     "hp": 1280, "ad": 58, "max_mana": 52, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 285, "sp_multiplier": 1.85,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Ox Aegis",
     "skill_type": "drain", "skill_dmg_type": "magic"},
    {"name": "AncientVial", "cost": 5, "traits": ["PotionClan", "RuneLand"], "role": "tank",
     "hp": 1500, "ad": 70, "max_mana": 60, "mana_per_attack": 10,
     "attack_cooldown": 1.4, "sp_base_dmg": 350, "sp_multiplier": 2.1,
     "attack_range": RANGE_TANK, "star": 1, "skill_desc": "Ancestral Boil",
     "skill_type": "burst_shield", "skill_dmg_type": "magic"},
    {"name": "LeopardBow", "cost": 1, "traits": ["LeopardKind", "Treasure"], "role": "archer",
     "hp": 490, "ad": 55, "max_mana": 30, "mana_per_attack": 13,
     "attack_cooldown": 1.1, "sp_base_dmg": 110, "sp_multiplier": 1.4,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Venom Bolt",
     "skill_type": "damage"},
    {"name": "FrogBomb", "cost": 2, "traits": ["FrogTribe", "RuneLand"], "role": "archer",
     "hp": 540, "ad": 52, "max_mana": 34, "mana_per_attack": 12,
     "attack_cooldown": 1.15, "sp_base_dmg": 135, "sp_multiplier": 1.55,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Toxic Bomb",
     "skill_type": "damage", "skill_dmg_type": "magic"},
    {"name": "OxGunner", "cost": 3, "traits": ["Lumber", "Treasure"], "role": "archer",
     "hp": 640, "ad": 78, "max_mana": 42, "mana_per_attack": 12,
     "attack_cooldown": 1.2, "sp_base_dmg": 185, "sp_multiplier": 1.7,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Heavy Shot",
     "skill_type": "damage"},
    {"name": "VialSniper", "cost": 4, "traits": ["PotionClan", "RuneLand"], "role": "archer",
     "hp": 680, "ad": 62, "max_mana": 48, "mana_per_attack": 13,
     "attack_cooldown": 1.05, "sp_base_dmg": 210, "sp_multiplier": 1.8,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Needle Storm",
     "skill_type": "damage"},
    {"name": "SwiftStrike", "cost": 5, "traits": ["LeopardKind", "RuneLand"], "role": "archer",
     "hp": 720, "ad": 88, "max_mana": 55, "mana_per_attack": 13,
     "attack_cooldown": 1.0, "sp_base_dmg": 290, "sp_multiplier": 2.1,
     "attack_range": RANGE_ARCHER, "star": 1, "skill_desc": "Swift Barrage",
     "skill_type": "damage"},
]
TRAIT_DATA = {
    "PotionClan": [2, 4, 6, 8], "LeopardKind": [2, 4], "FrogTribe": [2, 3],
    "Lumber": [2, 4], "Dancer": [2], "Elder": [2],
    "BearRidge": [3, 5, 7, 10], "RuneLand": [2, 4, 6, 8, 11],
    "Treasure": [2, 4, 6, 8],
    "Thunder": [2, 4, 6],
    "ClassTank": [2, 4, 6, 8],
    "ClassArcher": [2, 4, 6, 8],
    "ClassMage": [2, 4, 6, 8],
    "ClassWarrior": [2, 4, 6, 8],
}
TRAIT_DESC = {
    "PotionClan": ("法强", ["+12%", "+28%", "+50%", "+80%"]),
    "LeopardKind": ("暴击", ["+18%", "+38%"]),
    "FrogTribe": ("生命/治疗", ["+8%/+15%", "+20%/+38%"]),
    "Lumber": ("最大生命", ["+12%", "+28%"]),
    "Dancer": ("攻速", ["+25%"]),
    "Elder": ("敌方攻击", ["-12%"]),
    "BearRidge": ("召唤团子", ["1星", "2星", "3星", "4星"]),
    "RuneLand": ("攻速/回蓝",
                 ["+10%/+1", "+22%/+2", "+36%/+3", "+52%/+4", "+70%/+5"]),
    "Treasure": ("每回合金币", ["+1", "+3", "+6", "+10"]),
    "Thunder": ("雷霆整活", ["攻速+15%", "攻速+30%", "全场发弹幕"]),
    "ClassTank": ("坦克生命", ["+15%", "+30%", "+50%", "+80%"]),
    "ClassArcher": ("射手攻速", ["+15%", "+30%", "+50%", "+80%"]),
    "ClassMage": ("术士 攻强+法强", ["+15%", "+30%", "+50%", "+80%"]),
    "ClassWarrior": ("战士真伤", ["+10%", "+20%", "+35%", "+60%"]),
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
    u = dict(u)
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
        u["skill_dmg_type"] = "physical"
    return u


def get_base_template(name):
    for c in CHAMPION_LIST:
        if c["name"] == name:
            return c
    return None


COST_COMPENSATION = {1: (1.08, 1.05), 2: (1.05, 1.03),
                     3: (1.03, 1.02), 4: (1.0, 1.0), 5: (1.0, 1.0)}


def make_unit_with_star(name, star):
    base = get_base_template(name)
    if base is None:
        return None
    u = copy.deepcopy(base)
    u["star"] = star
    scale = 1.8 ** (star - 1)
    cost = base.get("cost", 1)
    cb = COST_COMPENSATION.get(cost, (1.0, 1.0))
    u["hp"] = int(base["hp"] * scale * cb[0])
    u["ad"] = int(base["ad"] * scale * cb[1])
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


def count_board_units(p):
    return sum(1 for row in p["board"] for c in row if c is not None)


def get_population_cap(p):
    cap = p.get("level", 1)
    for row in p["board"]:
        for u in row:
            if u is None:
                continue
            for item in u.get("items", []):
                cap += item.get("stats", {}).get("population", 0)
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


def count_traits(player):
    seen_names = set()
    tc = {}
    for row in player["board"]:
        for u in row:
            if u is None:
                continue
            name = u.get("name", "")
            if name == "Tuanzi":
                continue
            if name in seen_names:
                continue
            seen_names.add(name)
            for t in u.get("traits", []):
                if t == "Summon":
                    continue
                tc[t] = tc.get(t, 0) + 1
            role = u.get("role", "warrior")
            class_trait = ROLE_TO_CLASS_TRAIT.get(role)
            if class_trait:
                tc[class_trait] = tc.get(class_trait, 0) + 1
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


def get_treasure_gold(player):
    tc = count_traits(player)
    cnt = tc.get("Treasure", 0)
    for threshold, gold in ((8, 10), (6, 6), (4, 3), (2, 1)):
        if cnt >= threshold:
            return gold
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
            buffs["sp_mult"] += _tier_val(tier, [0.0, 0.12, 0.28, 0.50, 0.80])
        elif trait == "LeopardKind":
            buffs["crit"] += _tier_val(tier, [0.0, 0.18, 0.38])
        elif trait == "Lumber":
            buffs["hp_mult"] += _tier_val(tier, [0.0, 0.12, 0.28])
        elif trait == "FrogTribe":
            buffs["hp_mult"] += _tier_val(tier, [0.0, 0.08, 0.20])
            buffs["sp_mult"] += _tier_val(tier, [0.0, 0.15, 0.38])
        elif trait == "Elder":
            buffs["enemy_atk_mult"] -= 0.12
        elif trait == "Dancer":
            buffs["atk_speed_mult"] += 0.25
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
    score = 0
    name = card["name"]
    cost = card["cost"]
    traits = card.get("traits", [])
    same1 = count_unit_owned(p, name, 1)
    same2 = count_unit_owned(p, name, 2)
    if same2 >= 2:
        score += 120
    elif same2 == 1:
        score += 40
    elif same1 == 2:
        score += 90
    elif same1 == 1:
        score += 35
    else:
        score += 1
    for t in traits:
        if t in target_traits:
            score += 6
        elif t in count_traits(p):
            score += 2
    counter = p.get("_counter_target")
    if counter and counter in traits:
        score += 4
    score += cost
    gold_after = p["gold"] - cost
    if gold_after < 5:
        score -= 10
    elif gold_after < 15:
        score -= 4
    elif gold_after < 30:
        score -= 1
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
        if best_idx < 0 or best_score < 4:
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


def ai_equip_items(p):
    if not p.get("items"):
        return
    while True:
        new_items, combined = try_combine_items(p["items"])
        p["items"] = new_items
        if not combined:
            break

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
        return
    _, r, c = best_unit_pos
    u = p["board"][r][c]
    while p["items"] and len(u.get("items", [])) < MAX_ITEMS_PER_UNIT:
        item = p["items"].pop(0)
        u.setdefault("items", []).append(item)
        u["items"] = try_combine_items_all(u["items"])


def ai_smart_equip(p, all_players):
    if not p.get("items"):
        return
    p["items"] = try_combine_items_all(p["items"])

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
        if not p["items"]:
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
        for i, item in enumerate(p["items"]):
            stats = item.get("stats", {})
            if prefer in stats:
                p["items"].pop(i)
                target.setdefault("items", []).append(item)
                target["items"] = try_combine_items_all(target["items"])
                equipped = True
                break
        if not equipped:
            item = p["items"].pop(0)
            target.setdefault("items", []).append(item)
            target["items"] = try_combine_items_all(target["items"])


def get_ai_behavior(p):
    mult = p.get("difficulty_mult", 1.0)
    if mult <= 0.85:
        return AI_BEHAVIOR["easy"]
    if mult <= 1.15:
        return AI_BEHAVIOR["normal"]
    if mult <= 1.4:
        return AI_BEHAVIOR["hard"]
    return AI_BEHAVIOR["extreme"]


def ai_do_turn(p, all_players=None):
    behavior = get_ai_behavior(p)

    if behavior["skip_chance"] > 0 and random.random() < behavior["skip_chance"]:
        if not p.get("shop_locked"):
            p["shop"] = roll_shop_by_odds(p["level"])
        ai_simple_buy(p)
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
          if p["hp"] < 25:
               refresh_budget = 10
          elif p["hp"] < 40:
               refresh_budget = 20
          elif p["level"] >= 7:
               refresh_budget = 40
          else:
               refresh_budget = 50
    else:
           refresh_budget = behavior["refresh_budget"]

    if p["gold"] >= refresh_budget:
        p["gold"] -= REFRESH_COST
        p["shop"] = roll_shop_by_odds(p["level"])
        ai_smart_buy(p)
        ai_try_combine(p)
        ai_auto_position(p)


def ai_try_combine(target_player):
    for _ in range(20):
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


class BattleUnit:
    def __init__(self, champion_data, start_x, start_y, side, buffs=None, size=48):
        self.base = safe_unit(copy.deepcopy(champion_data))
        self.side = side
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
        self.is_summon = (self.base.get("name") == "Tuanzi")
        self.skill_type = self.base.get("skill_type", "damage")
        self.muted = False
        self.shield = 0
        item_stats = get_unit_item_stats(self.base)
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

    def take_damage(self, dmg, source=None, dmg_type="physical"):
        if not self.alive:
            return
        true_extra = 0
        if source is not None and hasattr(source, "true_dmg_bonus"):
            true_extra = int(dmg * source.true_dmg_bonus)
        if dmg_type == "magic":
            reduction = self.mr / (self.mr + 100) if self.mr >= 0 else 0
        else:
            reduction = self.armor / (self.armor + 100) if self.armor >= 0 else 0
        final = max(1, int(dmg * (1 - reduction))) + true_extra
        if self.damage_reduction > 0:
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
        star = self.base["star"]
        star_scale = SKILL_DMG_STAR_SCALE.get(star, SKILL_DMG_STAR_SCALE[4])
        sp_val = int(self.base["sp_base_dmg"] * self.base["sp_multiplier"]
                     * star_scale * self.sp_buff)
        name = self.base["name"]
        if not self.muted:
            play_sfx("skill")
        self.skill_flash_timer = 0.6
        self.cast_count += 1
        is_5cost = self.base.get("cost", 1) == 5
        is_3star_5cost = is_5cost and star >= 3
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
        elif self.is_ranged and dist < RANGED_KEEP_DIST:
            self.state = "moving"
            self.attack_target = nearest
            dx_from_start = self.x - self.start_x
            dy_from_start = self.y - self.start_y
            back_dist = (dx_from_start ** 2 + dy_from_start ** 2) ** 0.5
            if back_dist < RANGED_BACKOFF_LIMIT and dist > MIN_MOVE_DIST:

                self.x -= dx / dist * self.move_speed * RANGED_BACKOFF_SPEED * dt
                self.y -= dy / dist * self.move_speed * RANGED_BACKOFF_SPEED * dt
        else:
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
        enemy_buffs["atk_mult"] *= ally_buffs.get("enemy_atk_mult", 1.0)
        ally_buffs["atk_mult"] *= enemy_buffs.get("enemy_atk_mult", 1.0)
        self.allies = self._spawn_units(self.attacker, "ally", screen_w, screen_h, ally_buffs)
        self.enemies = self._spawn_units(self.defender, "enemy", screen_w, screen_h, enemy_buffs)
        self._spawn_bear_ridge_summons(screen_w, screen_h, ally_buffs, enemy_buffs)
        self.sync_mute()
        self._spawn_trait_activation_fx(screen_w, screen_h)

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
        size = max(38, int(cell_w * 0.80))
        if side == "ally":
            y_front, y_back = screen_h * 0.54, screen_h * 0.90
        else:
            y_front, y_back = screen_h * 0.46, screen_h * 0.10
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
                units.append(BattleUnit(u, x, y, side, buffs, size=size))
        return units

    def update(self, dt, screen_w, screen_h):
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

    def _finish(self, alive_a, alive_e):
        self.finished = True
        if alive_a and not alive_e:
            self.winner = 'attacker'
        elif alive_e and not alive_a:
            self.winner = 'defender'
        else:
            self.winner = 'draw'

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

        ai_mult = DIFFICULTY_MULT.get(difficulty, 1.0)
        self.me = create_empty_player(gold=START_GOLD_PLAYER, is_ai=False)
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
                available = [c for c in CHAMPION_LIST
                             if c.get("cost") == 1 and not c.get("no_shop")
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
            self.shop = roll_shop_by_odds(self.me["level"])

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
        if champ is None or self.me["gold"] < champ["cost"]:
            play_sfx("error")
            self._toast_msg("金币不足!")
            self.ai_assistant_say("no_gold")
            return
        if pool_remaining(champ["name"]) <= 0:
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
        if not try_consume_pool(champ["name"], 1):
            self.shop[idx] = None
            self.battle_log = f"{champ_cn(champ['name'])} 已售罄!"
            self._toast_msg("该棋子已售罄")
            play_sfx("error")
            return
        self.me["gold"] -= champ["cost"]
        self.me["bench"][empty_idx] = copy.deepcopy(champ)
        self.shop[idx] = None
        play_sfx("buy")
        self.try_combine(self.me)
        self.battle_log = f"已购买 {champ_cn(champ['name'])} (备战席 {empty_idx+1})"
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
        count = 3 ** (star - 1)
        return_pool(unit["name"], count)
        self.me["gold"] += refund
        self.battle_log = f"出售 {champ_cn(unit['name'])} {star}星 +{refund}金"
        play_sfx("sell")
        enforce_population_cap(self.me)
        save_game(self)
        return True, refund

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

    def equip_item_to(self, item_ref, source_type, i1, i2=-1):
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
        if len(unit.get("items", [])) >= MAX_ITEMS_PER_UNIT:
            play_sfx("error")
            self.battle_log = f"{champ_cn(unit['name'])} 装备已满!"
            self._toast_msg("装备已满!")
            return False
        item = self.me["items"].pop(item_idx)
        unit.setdefault("items", []).append(item)
        play_sfx("coin")
        self.battle_log = f"装备 {item['name']} 给 {champ_cn(unit['name'])}"
        before_len = len(unit["items"])
        unit["items"] = try_combine_items_all(unit["items"])
        if len(unit["items"]) < before_len:
            self.battle_log = "装备合成成功!"
            play_sfx("hex")
        enforce_population_cap(self.me)
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
        stage, rnd = self.stage
        round_type = get_round_type(stage, rnd)
        if stage == 1 and rnd == 1:
            return

        if self.is_multiplayer:
            self._start_multiplayer_battle()
            return

        
        all_players = [self.me] + self.players
        for ai_p in self.players:
            if ai_p["hp"] > 0:
                ai_do_turn(ai_p, all_players)
        
        auto_fill_board(self.me)
        
        self.refresh_shop()
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
        self.post_battle_timer = 0.0
        self._fixed_accum = 0.0
        self.is_battle_phase = True

    def _start_multiplayer_battle(self):
        if not (self.net and self.net.connected):
            self.battle_log = "未连接"
            self._toast_msg("未连接")
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

    def _setup_multiplayer_battle(self, peer_msg):
        peer_seed = int(peer_msg.get("seed", 0))
        if not hasattr(self, "_saved_random_state"):
            self._saved_random_state = random.getstate()
        random.seed(self._my_seed ^ peer_seed)

        peer = create_empty_player(gold=0, is_ai=True)
        peer["board"] = peer_msg.get("board",
                                     [[None] * 7 for _ in range(4)])
        peer["hex_bonuses"] = peer_msg.get(
            "hex_bonuses",
            {"hp_mult": 0.0, "atk_mult": 0.0, "sp_mult": 0.0, "crit": 0.0,
             "atk_speed": 0.0, "income": 0, "armor": 0})
        peer["hex_list"] = peer_msg.get("hex_list", [])
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
            if pb:
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
                    self._monster_drop(stage)
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

    def _monster_drop(self, stage):
        drops = []
        gold_drop = random.randint(2, 4) + stage
        self.me["gold"] += gold_drop
        drops.append(f"+{gold_drop} 金")
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

    def _advance_to_next_round(self):
        self.is_battle_phase = False
        self.battle_phase_resolved = False

        if self.is_multiplayer:
            if hasattr(self, "_saved_random_state"):
                random.setstate(self._saved_random_state)
                del self._saved_random_state
            self.battles = []
            self.shop_locked = False
            self.refresh_shop()
            self.multiplayer_phase = "prep"
            self.phase_timer = 999999
            apply_income_and_xp(self.me)
            self.round_counter += 1
            self.battle_log = f"第 {self.round_counter + 1} 局备战"
            if self.me["hp"] <= 0:
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
        self.shop_locked = False
        self.refresh_shop()
        self.round_counter += 1
        if self.round_counter >= HEX_ROUND_INTERVAL:
            self.round_counter = 0
            self.hex_choices = roll_hex_choices()
            if len(self.hex_choices) > 0:
                self.show_hex_popup = True
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
        draw_text(screen, item_stat_text(item), px + 20, py + 118,
                  font_md, TEXT_WHITE)
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
               radius=8, border_w=2):
    try:
        pygame.draw.rect(surface, fill_col, rect, border_radius=radius)
        pygame.draw.rect(surface, border_col, rect, width=border_w, border_radius=radius)
    except Exception:
        pass


def draw_button(surface, rect, fill_col, border_col, radius=8):
    try:
        pygame.draw.rect(surface, fill_col, rect, border_radius=radius)
        pygame.draw.rect(surface, border_col, rect, width=2, border_radius=radius)
    except Exception:
        pass


def draw_unit_cell(surface, r, unit, font_sm, font_md, is_drag_src=False):
    try:
        star = unit.get("star", 1)
        border = STAR_BORDER.get(star, STAR_BORDER[1])
        cost = unit.get("cost", 1)
        traits = unit.get("traits", [])
        bg = (35, 38, 50)
        if "BearRidge" in traits:
            bg = (50, 38, 25)
        elif "RuneLand" in traits:
            bg = (28, 38, 55)
        elif "Treasure" in traits:
            bg = (55, 45, 15)
        pygame.draw.rect(surface, bg, r, border_radius=6)
        if "BearRidge" in traits:
            pygame.draw.rect(surface, BEAR_COLOR, r.inflate(4, 4), width=2, border_radius=7)
        elif "RuneLand" in traits:
            pygame.draw.rect(surface, RUNE_COLOR, r.inflate(4, 4), width=2, border_radius=7)
        elif "Treasure" in traits:
            pygame.draw.rect(surface, TREASURE_COLOR, r.inflate(4, 4), width=2, border_radius=7)
        pygame.draw.rect(surface, border, r, width=3, border_radius=6)
        if is_drag_src:
            return
        name_col = COST_COLORS.get(cost, TEXT_WHITE)
        draw_text(surface, champ_cn(unit.get("name", "?"))[:4],
                  r.centerx, r.centery - 5, font_sm, name_col, align_center=True)
        draw_text(surface, f"{star}星", r.centerx, r.centery + 8,
                  font_sm, border, align_center=True)
        role = unit.get("role", "warrior")
        role_col = ROLE_COLORS.get(role, TEXT_DIM)
        role_txt = ROLE_SHORT.get(role, "?")
        badge = pygame.Rect(r.x + 2, r.y + 2, 13, 13)
        pygame.draw.rect(surface, (15, 15, 20), badge, border_radius=3)
        pygame.draw.rect(surface, role_col, badge, width=1, border_radius=3)
        draw_text(surface, role_txt, badge.centerx, badge.centery, font_sm, role_col, True)
        items = unit.get("items", [])
        if items:
            i_size = 9
            ix = r.right - 2 - i_size
            iy = r.bottom - 2 - i_size
            for item in reversed(items[-3:]):
                ir = pygame.Rect(ix, iy, i_size, i_size)
                draw_item_icon(surface, ir, item)
                ix -= (i_size + 2)
    except Exception:
        pass


def draw_battle_unit(screen, unit, font_sm, is_ally):
    cx, cy = int(unit.x), int(unit.y)
    size = unit.size
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
    draw_text(screen, champ_cn(unit.base["name"])[:4],
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
    draw_text(screen, title, W // 2, py + 48, font_md, title_col, True)
    pad = 14
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
    draw_panel(screen, pygame.Rect(left_x, py + 72, col_w, 24),
               (30, 60, 110), (60, 120, 180), 5, 1)
    draw_text(screen, a_label, left_x + col_w // 2, py + 84, font_md, BLUE_MANA, True)
    draw_panel(screen, pygame.Rect(right_x, py + 72, col_w, 24),
               (110, 40, 40), (180, 60, 60), 5, 1)
    draw_text(screen, d_label, right_x + col_w // 2, py + 84, font_md, RED, True)
    header_y = py + 104
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
               "trait_activate": []}
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
                   (24, 26, 34), (60, 66, 80), 5, 1)
        draw_text(screen, "羁绊", x + 8, y + 3, font_sm, GOLD_COLOR)
        draw_text(screen, "(无)", x + 8, y + 24, font_sm, TEXT_DIM)
        return
    active_traits = []
    for trait, count in tc.items():
        thresholds = TRAIT_DATA.get(trait, [])
        tier = sum(1 for t in thresholds if count >= t)
        active_traits.append((trait, count, tier))
    priority = {"BearRidge": 0, "RuneLand": 1, "Treasure": 2}
    active_traits.sort(key=lambda t: (priority.get(t[0], 9), -t[2], -t[1]))
    draw_panel(screen, pygame.Rect(x, y, panel_w, panel_h),
               (20, 22, 30), (60, 66, 80), 5, 1)
    draw_text(screen, "羁绊", x + 8, y + 3, font_sm, GOLD_COLOR)
    ly = y + 24
    for trait, count, tier in active_traits[:8]:
        short = trait_short_cn(trait)
        thresholds = TRAIT_DATA.get(trait, [])
        next_thresh = None
        for t in thresholds:
            if count < t:
                next_thresh = t
                break
        prog = f"{count}/{next_thresh}" if next_thresh else f"{count}"
        if trait in TRAIT_COLOR:
            col = TRAIT_COLOR[trait] if tier > 0 else TEXT_DIM
        else:
            col = GREEN_HP if tier > 0 else TEXT_DIM
        is_big = trait in ("BearRidge", "RuneLand", "Treasure")
        if is_big:
            draw_text(screen, f"{short} {prog}", x + 8, ly, font_md, col)
        else:
            draw_text(screen, f"{short} {prog}", x + 8, ly, font_sm, col)
        ly += 22


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
    base = get_base_template(aug["champ"])
    cost = base["cost"] if base else 1
    draw_panel(screen, icon_r, COST_BG.get(cost, (35, 38, 48)),
               COST_COLORS.get(cost, TEXT_WHITE), 8, 3)
    draw_text(screen, champ_cn(aug["champ"])[:3], icon_r.centerx,
              icon_r.centery, get_font(34),
              COST_COLORS.get(cost, TEXT_WHITE), True)
    draw_text(screen, aug["name"], r.centerx, r.y + 115,
              get_font(32), GOLD_COLOR, True)
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
        bar.fill((10, 12, 18, 230))
        screen.blit(bar, (0, 0))
        pygame.draw.line(screen, BORDER_LIGHT, (0, top_h - 2), (W, top_h - 2), 2)
    except Exception:
        pass
    lv_box_w = W * 0.20
    lv_box = pygame.Rect(8, 8, lv_box_w, top_h - 16)
    draw_panel(screen, lv_box, PANEL_DARK, BORDER_LIGHT, 8, 2)
    draw_text(screen, f"等级 {view_p['level']}", lv_box.x + 10, lv_box.y + 6,
              font_md, BLUE_MANA)
    if view_p["level"] < MAX_LEVEL:
        xp = view_p.get("xp", 0)
        need = view_p.get("xp_next", 999)
        ratio = min(1.0, xp / max(1, need))
        bar_r = pygame.Rect(lv_box.x + 10, lv_box.y + lv_box.h - 14,
                            lv_box.w - 20, 8)
        pygame.draw.rect(screen, (30, 32, 42), bar_r, border_radius=3)
        if ratio > 0:
            pygame.draw.rect(screen, BLUE_MANA,
                             (bar_r.x, bar_r.y, int(bar_r.w * ratio), bar_r.h),
                             border_radius=3)
        pygame.draw.rect(screen, BORDER_LIGHT, bar_r, width=1, border_radius=3)
        draw_text(screen, f"{xp}/{need}", bar_r.centerx, bar_r.centery,
                  font_sm, TEXT_WHITE, True)
    else:
        bar_r = pygame.Rect(lv_box.x + 10, lv_box.y + lv_box.h - 14,
                            lv_box.w - 20, 8)
        pygame.draw.rect(screen, GOLD_COLOR, bar_r, border_radius=3)
        draw_text(screen, "满级", bar_r.centerx, bar_r.centery,
                  font_sm, (0, 0, 0), True)
    cx = W // 2
    stage, rnd = gs.stage
    rt = get_round_type(stage, rnd)
    rt_label = {"augment": "强化", "monster": "野怪",
                "carousel": "选秀", "pvp": "PVP"}.get(rt, "")
    stage_label = f"回合 {stage}-{rnd} ({rt_label})"
    if gs.is_multiplayer:
        stage_label = f"联机对战 · 第 {gs.round_counter + 1} 局"
    draw_text(screen, stage_label, cx, top_h * 0.22, font_md, TEXT_WHITE, True)
    d = gs.difficulty
    d_col = DIFFICULTY_COLOR.get(d, TEXT_DIM)
    if gs.is_multiplayer:
        draw_text(screen, f"对手: {gs.peer_name}", cx, top_h * 0.52,
                  font_sm, RUNE_COLOR, True)
    else:
        draw_text(screen, f"AI难度: {DIFFICULTY_NAME.get(d, '?')}",
                  cx, top_h * 0.52, font_sm, d_col, True)
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
        draw_text(screen, f"备战 {math.ceil(prep_t)}s", cx, top_h * 0.82,
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
    draw_panel(screen, speed_box, PANEL_DARK, speed_col, 8, 2)
    draw_text(screen, f"{int(gs_speed)}x", speed_box.centerx,
              speed_box.centery, font_md, speed_col, True)
    gold_box = pygame.Rect(W - gold_box_w - 8, 8, gold_box_w, top_h - 16)
    draw_panel(screen, gold_box, (45, 35, 10), GOLD_DEEP, 8, 2)
    icon_r = int(gold_box.h * 0.28)
    ix = gold_box.x + 14 + icon_r
    iy = gold_box.y + gold_box.h // 2 - 3
    draw_coin_icon(screen, ix, iy, icon_r)
    draw_text(screen, str(view_p["gold"]),
              ix + icon_r + 8, iy - 8, font_md, GOLD_COLOR)
    interest = min(5, view_p["gold"] // 10)
    draw_text(screen, f"利息 +{interest}",
              ix + icon_r + 8, iy + 8, font_sm, TEXT_DIM)
    draw_text(screen, f"当前视角: {view_name}", cx, top_h + 6,
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
    line_h = 18
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
    ry = y + 34
    gold = view_p["gold"]
    level = view_p["level"]
    interest = min(5, gold // 10)
    base = 5
    streak = max(view_p.get("win_streak", 0), view_p.get("lose_streak", 0))
    streak_bonus = 3 if streak >= 5 else (2 if streak >= 3 else (1 if streak >= 2 else 0))
    hex_income = get_hex_bonuses(view_p)["income"]
    treasure_income = get_treasure_gold(view_p)
    next_income = base + interest + streak_bonus + hex_income + treasure_income
    draw_text(screen, f"下回合收入: +{next_income} 金",
              mid_x + 12, ry, font_sm, GOLD_COLOR)
    ry += 20
    draw_text(screen, f"等级 {level} · 上场 {count_board_units(view_p)}/{get_population_cap(view_p)}",
              mid_x + 12, ry, font_sm, TEXT_WHITE)
    ry += 20
    tc = count_traits(view_p)
    if tc:
        active_cnt = 0
        for trait, count in tc.items():
            thresholds = TRAIT_DATA.get(trait, [])
            if sum(1 for t in thresholds if count >= t) > 0:
                active_cnt += 1
        draw_text(screen, f"激活羁绊: {active_cnt} / {len(tc)}",
                  mid_x + 12, ry, font_sm, GREEN_HP)
    ws = view_p.get("win_streak", 0)
    ls = view_p.get("lose_streak", 0)
    if ws >= 2 or ls >= 2:
        ry += 20
        tag = "连胜" if ws >= 2 else "连败"
        n = ws if ws >= 2 else ls
        bonus = 3 if n >= 5 else (2 if n >= 3 else 1)
        draw_text(screen, f"{tag} x{n} · +{bonus} 金",
                  mid_x + 12, ry, font_sm, (255, 180, 60))
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
    trait_str = " / ".join(trait_cn(t) for t in _all_t if t)
    draw_text(screen, f"羁绊: {trait_str}",
              dx + d_w - 12, dy + 16, font_sm, TEXT_WHITE)
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
    if items:
        for i, item in enumerate(items):
            ir = pygame.Rect(eq_box.x + 60 + i * 70, eq_box.y + 24, 48, 48)
            draw_item_icon(screen, ir, item)
            draw_text(screen, item.get("name", "?")[:6],
                      ir.centerx, ir.bottom + 4, font_sm, TEXT_WHITE, True)
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
    draw_text(screen, f"出售: {refund} 金", dx + 16, dy + d_h - 22,
              font_sm, GOLD_COLOR)
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
        prep_btn = pygame.Rect(W // 2 - W * 0.18, H - H * 0.10, W * 0.36, 50)
        hovered = prep_btn.collidepoint(mouse_pos)
        draw_button(screen, prep_btn,
                    (40, 90, 40) if hovered else (30, 65, 30),
                    GREEN_HP, 10)
        draw_text(screen, "准备战斗 (发送阵容)", prep_btn.centerx,
                  prep_btn.centery, font_md, TEXT_WHITE, True)

    if gs.is_multiplayer and gs.multiplayer_phase == "wait_peer":
        draw_text(screen, "等待对手准备...", W // 2, H * 0.5,
                  get_font(40), GOLD_COLOR, True)

    if gs.is_multiplayer and gs.multiplayer_phase == "wait_battle":
        draw_text(screen, "等待对手战斗数据...", W // 2, H * 0.5,
                  get_font(40), GOLD_COLOR, True)

    if gs.is_battle_phase:
        battle_selector_rects = draw_battle(screen, gs, font_lg, font_md,
                                            font_sm, font_dmg, W, H)
        if not gs.battle_phase_resolved:
            bshop, brefresh, blevelup, block = draw_battle_shop_bar(
                screen, gs, font_lg, font_md, font_sm, W, H, mouse_pos)
        else:
            bshop, brefresh, blevelup, block = [], None, None, None
        draw_toast(screen, gs, font_md, W, H)
        draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 10, font_sm,
                  (255, 80, 80), align_center=True)
        return (board_rect_list, bench_rect_list, bshop,
                brefresh, blevelup, gold_btn_rect,
                trait_btn_rect, auto_btn_rect, prev_btn_rect, next_btn_rect,
                None, hex_card_rects, battle_selector_rects, block,
                [], [], [], [], None, -1, None, None, None)

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
    draw_panel(screen, board_bg, (22, 25, 34), (60, 68, 90), 10, 2)
    draw_text(screen, "前", board_x - 22, board_y + cell_size * 0.5 + gap * 0.5,
              font_sm, (255, 140, 120))
    draw_text(screen, "后", board_x - 22, board_y + cell_size * 3.5 + gap * 1.5,
              font_sm, (140, 180, 255))

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
                base = (min(255, base[0] + 6), min(255, base[1] + 6),
                        min(255, base[2] + 6))
            bc = base
            if hover_board == (row_idx, col_idx):
                bc = (min(255, base[0] + 40), min(255, base[1] + 40),
                      min(255, base[2] + 40))
            pygame.draw.rect(screen, bc, r, border_radius=6)
            pygame.draw.rect(screen, (70, 78, 96), r, width=1, border_radius=6)
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
    draw_text(screen, f"备战席  ({board_cnt}/{get_population_cap(view_p)} 上场)",
              board_x, bench_y - 18, font_sm, TEXT_DIM)
    for i in range(8):
        bx = board_x + i * (bench_cell + gap)
        r = pygame.Rect(bx, bench_y, bench_cell, bench_cell)
        bc = (32, 35, 45)
        if hover_bench == i:
            bc = (55, 60, 75)
        pygame.draw.rect(screen, bc, r, border_radius=5)
        pygame.draw.rect(screen, (70, 78, 96), r, width=1, border_radius=5)
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
        bg_col = COST_BG.get(cost, (35, 38, 48))
        draw_panel(screen, r, bg_col, BORDER_LIGHT, 8, 2)
        if champ:
            pygame.draw.rect(screen, COST_COLORS.get(cost, TEXT_WHITE),
                             (r.x, r.y, r.w, 4), border_radius=2)
        shop_rect_list.append((r, i))
        if champ:
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
            role_rect = pygame.Rect(r.x + 3, r.y + 8, 20, 18)
            pygame.draw.rect(screen, (15, 15, 20), role_rect, border_radius=3)
            pygame.draw.rect(screen, role_col, role_rect, width=1, border_radius=3)
            draw_text(screen, ROLE_SHORT.get(role, "?"),
                      role_rect.centerx, role_rect.centery, font_sm, role_col, True)
            draw_text(screen, champ_cn(champ["name"])[:5], r.centerx,
                      r.y + shop_h * 0.30, font_md,
                      COST_COLORS.get(cost, TEXT_WHITE), True)
            _role = champ.get("role", "warrior")
            _all_t = list(traits) + [ROLE_TO_CLASS_TRAIT.get(_role, "")]
            _all_t = [t for t in _all_t if t][:3]
            tstr = "·".join(trait_short_cn(t) for t in _all_t)
            draw_text(screen, tstr, r.centerx, r.y + shop_h * 0.58,
                      font_sm, TEXT_DIM, True)
            draw_text(screen, f"{cost}金", r.centerx,
                      r.y + shop_h * 0.85, font_md, GOLD_COLOR, True)
            owned1 = count_unit_owned(gs.me, champ["name"], 1)
            owned2 = count_unit_owned(gs.me, champ["name"], 2)
            owned3 = count_unit_owned(gs.me, champ["name"], 3)
            if owned1 + owned2 + owned3 > 0:
                br = pygame.Rect(r.right - 50, r.y + 8, 46, 16)
                pygame.draw.rect(screen, (40, 60, 40), br, border_radius=3)
                pygame.draw.rect(screen, GREEN_HP, br, width=1, border_radius=3)
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
            draw_button(screen, levelup_rect, (55, 55, 60), (100, 100, 100), 8)
            draw_text(screen, "已满级", levelup_rect.centerx,
                      levelup_rect.centery, font_md, TEXT_DIM, True)
        else:
            draw_button(screen, levelup_rect, BLUE_DEEP, BLUE, 8)
            xp = gs.me.get("xp", 0)
            need = gs.me.get("xp_next", 999)
            remain = max(0, need - xp)
            draw_text(screen, f"升级 {BUY_XP_COST}金 (还差{remain})",
                      levelup_rect.centerx, levelup_rect.centery,
                      font_md, TEXT_WHITE, True)
    refresh_rect = pygame.Rect(W * 0.36, btn_y, W * 0.28, btn_h)
    if gs.viewing_player_idx == -1:
        draw_button(screen, refresh_rect, BLUE_DEEP, BLUE, 8)
        draw_text(screen, f"刷新 {REFRESH_COST}金", refresh_rect.centerx,
                  refresh_rect.centery, font_md, TEXT_WHITE, True)
    else:
        draw_button(screen, refresh_rect, (40, 40, 45), (90, 90, 90), 8)
        draw_text(screen, "观战中", refresh_rect.centerx,
                  refresh_rect.centery, font_md, TEXT_DIM, True)
    gold_btn_rect = pygame.Rect(W - 10 - W * 0.30, btn_y, W * 0.30, btn_h)
    draw_button(screen, gold_btn_rect, (55, 42, 15), GOLD_DEEP, 8)
    draw_coin_icon(screen, gold_btn_rect.x + 18, gold_btn_rect.centery, 9)
    draw_text(screen, f"{gs.me['gold']}",
              gold_btn_rect.x + 34, gold_btn_rect.centery, font_md, GOLD_COLOR)

    trait_btn_rect, prev_btn_rect, next_btn_rect, auto_btn_rect = \
        trait_rect, prev_rect, next_rect, auto_rect

    bottom_y = btn_y + btn_h + 8
    bottom_h = H - bottom_y - 24
    if bottom_h > 40:
        draw_bottom_info_panel(screen, gs, view_p, font_lg, font_md, font_sm,
                                W, H, 10, bottom_y, W - 20, bottom_h)

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
        tw, th = int(W * 0.55), int(H * 0.82)
        tx, ty = W // 2 - tw // 2, H // 2 - th // 2
        draw_panel(screen, pygame.Rect(tx, ty, tw, th),
                   (28, 32, 42), (100, 70, 140), 12, 2)
        draw_text(screen, "当前羁绊 (含棋子列表)", tx + 20, ty + 14,
                  font_md, GOLD_COLOR)
        board_names = set()
        for _row in view_p["board"]:
            for _u in _row:
                if _u is not None:
                    _n = _u.get("name", "")
                    if _n:
                        board_names.add(_n)
        trait_count = count_traits(view_p)
        line_y = ty + 50
        sorted_traits = sorted(trait_count.items(), key=lambda x: -x[1])
        for trait_name, cnt in sorted_traits:
            thresholds = TRAIT_DATA.get(trait_name, [])
            tier = sum(1 for t in thresholds if cnt >= t)
            thresholds_str = "/".join(str(t) for t in thresholds)
            title = f"{trait_cn(trait_name)}  {cnt}  [{thresholds_str}]"
            if trait_name in TRAIT_COLOR:
                col = TRAIT_COLOR[trait_name] if tier > 0 else TEXT_DIM
            else:
                col = GOLD_COLOR if tier > 0 else TEXT_WHITE
            draw_text(screen, title, tx + 20, line_y, font_sm, col)
            line_y += 20
            if trait_name in TRAIT_DESC:
                effect_name, effects = TRAIT_DESC[trait_name]
                for i, eff_txt in enumerate(effects):
                    is_active = (tier == i + 1)
                    mark = ">" if is_active else " "
                    col2 = GREEN_HP if is_active else (140, 140, 140)
                    line = f"  {mark} ({thresholds[i]}) {effect_name} {eff_txt}"
                    draw_text(screen, line, tx + 20, line_y, font_sm, col2)
                    line_y += 18
            _role_class = {"ClassTank": "tank", "ClassArcher": "archer",
                           "ClassMage": "mage", "ClassWarrior": "warrior"}
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
                max_x = tx + tw - 30
                cur_x = tx + 20
                cur_y = line_y
                draw_text(screen, "  棋子: ", cur_x, cur_y, font_sm,
                          (170, 200, 255))
                cur_x += font_sm.size("  棋子: ")[0]
                first_in_line = True
                for c in trait_champs:
                    on_board = c["name"] in board_names
                    nm_col = GREEN_HP if on_board else (170, 200, 255)
                    nm = f"{champ_cn(c['name'])}{c['cost']}费"
                    sep = "" if first_in_line else "、"
                    sep_w = font_sm.size(sep)[0] if sep else 0
                    nm_w = font_sm.size(nm)[0]
                    if cur_x + sep_w + nm_w > max_x:
                        cur_x = tx + 20
                        cur_y += 16
                        sep = ""
                        sep_w = 0
                        first_in_line = True
                    if sep:
                        draw_text(screen, sep, cur_x, cur_y, font_sm,
                                  (170, 200, 255))
                        cur_x += sep_w
                    draw_text(screen, nm, cur_x, cur_y, font_sm, nm_col)
                    cur_x += nm_w
                    first_in_line = False
                line_y = cur_y + 16
            line_y += 6
        buffs = apply_trait_buffs(view_p)
        merge_hex_into_buffs(buffs, view_p)
        line_y += 6
        draw_text(screen, "总加成:", tx + 20, line_y, font_sm, GOLD_COLOR)
        line_y += 22
        draw_text(screen, f"攻击 x{buffs['atk_mult']:.2f}  法强 x{buffs['sp_mult']:.2f}",
                  tx + 20, line_y, font_sm, TEXT_WHITE)
        line_y += 20
        draw_text(screen, f"生命 x{buffs['hp_mult']:.2f}  暴击 {int(buffs['crit'] * 100)}%",
                  tx + 20, line_y, font_sm, TEXT_WHITE)
        line_y += 20
        draw_text(screen, f"攻速 x{buffs['atk_speed_mult']:.2f}  额外回蓝 {buffs['extra_mana_per_attack']}",
                  tx + 20, line_y, font_sm, TEXT_WHITE)
        sum_star = get_bear_ridge_summon_star(view_p)
        if sum_star > 0:
            line_y += 20
            draw_text(screen, f"狗熊岭召唤: {sum_star}星团子",
                      tx + 20, line_y, font_sm, (180, 230, 255))
        t_gold = get_treasure_gold(view_p)
        if t_gold > 0:
            line_y += 20
            draw_text(screen, f"财宝猎人: 每回合 +{t_gold} 金",
                      tx + 20, line_y, font_sm, TREASURE_COLOR)
        draw_text(screen, "点击关闭", tx + 20, ty + th - 28, font_sm, TEXT_DIM)

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


def draw_menu_decoration(screen, font_sm, W, H):
    showcase = ["BaoLan", "BearBig", "ArcaneLord"]
    labels = ["毁灭豹", "守护熊", "秘法领主"]
    cx = W // 2
    cy = H * 0.36
    r = int(min(W, H) * 0.075)
    gap = int(r * 2.6)
    for i, name in enumerate(showcase):
        x = cx + (i - 1) * gap
        for k in range(3, 0, -1):
            try:
                glow_s = pygame.Surface((r * 2 + k * 8, r * 2 + k * 8),
                                         pygame.SRCALPHA)
                pygame.draw.circle(glow_s, (*GOLD_COLOR, 20),
                                   (r + k * 4, r + k * 4), r + k * 4)
                screen.blit(glow_s, (x - r - k * 4, cy - r - k * 4))
            except Exception:
                pass
        base = get_base_template(name)
        cost = base["cost"] if base else 5
        color = COST_COLORS.get(cost, TEXT_WHITE)
        pygame.draw.circle(screen, COST_BG.get(cost, (40, 40, 50)), (x, cy), r)
        pygame.draw.circle(screen, color, (x, cy), r, 3)
        draw_text(screen, champ_cn(name)[:2], x, cy,
                  get_font(int(r * 0.85)), color, True)
        draw_text(screen, labels[i], x, cy + r + 18,
                  font_sm, TEXT_DIM, True)


def draw_main_menu(screen, font_title, font_lg, font_md, font_sm,
                    W, H, mouse_pos, difficulty):
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
    title_y = H * 0.10
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
    draw_text(screen, "Leopard Potion AutoBattle Chess", W // 2, title_y + 40,
              font_sm, TEXT_DIM, True)
    d_col = DIFFICULTY_COLOR.get(difficulty, TEXT_DIM)
    draw_text(screen, f"当前AI难度: {DIFFICULTY_NAME.get(difficulty, '?')}",
              W // 2, title_y + 70, font_md, d_col, True)
    draw_menu_decoration(screen, font_sm, W, H)
    btn_w = W * 0.50
    btn_h = 56
    gap = 12
    btn_x = W // 2 - btn_w // 2
    start_y = H * 0.53
    continue_btn = None
    if has_save():
        continue_btn = pygame.Rect(btn_x, start_y - btn_h - gap, btn_w, btn_h)
    start_btn = pygame.Rect(btn_x, start_y, btn_w, btn_h)
    multi_btn = pygame.Rect(btn_x, start_y + btn_h + gap, btn_w, btn_h)
    update_btn = pygame.Rect(btn_x, start_y + 2 * (btn_h + gap), btn_w, btn_h)
    settings_btn = pygame.Rect(btn_x, start_y + 3 * (btn_h + gap), btn_w, btn_h)
    quit_btn = pygame.Rect(btn_x, start_y + 4 * (btn_h + gap), btn_w, btn_h)
    btn_list = []
    if continue_btn is not None:
        btn_list.append((continue_btn, "继续游戏", (30, 60, 40), (45, 90, 60), GREEN_HP))
    btn_list += [
        (start_btn, "开始游戏", (55, 45, 15), (95, 78, 25), GOLD_COLOR),
        (multi_btn, "联机对战", (30, 55, 45), (45, 80, 65), GREEN_HP),
        (update_btn, "检测更新", (35, 45, 70), (50, 65, 100), RUNE_COLOR),
        (settings_btn, "设置", (30, 40, 60), (45, 60, 90), BLUE),
        (quit_btn, "退出", (50, 25, 25), (75, 40, 40), RED),
    ]
    for btn, label, base_col, hover_col, border in btn_list:
        hovered = btn.collidepoint(mouse_pos)
        draw_button(screen, btn, hover_col if hovered else base_col, border, 12)
        if label == "开始游戏":
            label_col = GOLD_COLOR
        elif label in ("联机对战", "继续游戏"):
            label_col = GREEN_HP
        else:
            label_col = TEXT_WHITE
        draw_text(screen, label, btn.centerx, btn.centery,
                  get_font(28), label_col, True)
    draw_text(screen, "v1.2.8  ·  Built with Pygame  ·  支持联机对战",
              W // 2, H - 22, font_sm, (100, 105, 115), True)
    draw_text(screen, f"调试: {DBG_LAST}", W // 2, H - 8, font_sm,
              (200, 60, 60), align_center=True)
    return continue_btn, start_btn, multi_btn, update_btn, settings_btn, quit_btn


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
    changelog_btn = pygame.Rect(W // 2 - W * 0.22, H * 0.72, W * 0.44, 52)
    hovered_cl = changelog_btn.collidepoint(mouse_pos)
    draw_button(screen, changelog_btn,
                (95, 80, 30) if hovered_cl else (55, 45, 15),
                GOLD_COLOR, 10)
    draw_text(screen, "查看更新日志", changelog_btn.centerx,
              changelog_btn.centery, font_md, GOLD_COLOR, True)
    back_btn = pygame.Rect(W // 2 - W * 0.22, H * 0.82, W * 0.44, 60)
    hovered_back = back_btn.collidepoint(mouse_pos)
    draw_button(screen, back_btn,
                (45, 60, 90) if hovered_back else (30, 40, 60),
                BLUE, 10)
    draw_text(screen, "返回主菜单", back_btn.centerx, back_btn.centery,
              font_lg, TEXT_WHITE, True)
    return diff_rects, back_btn, changelog_btn

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
        draw_text(screen, f"· {line}", px + 32, y, font_sm, TEXT_WHITE)
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


def run_game_session(screen, clock, difficulty, font_lg, font_md, font_sm,
                     font_dmg, net=None, is_host=False, load_save=False):
    gs = GameState(difficulty=difficulty, net=net, is_host=is_host)
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

            if gs.game_over:
                pass
            elif getattr(gs, "show_starter_popup", False):
                pass
            elif getattr(gs, "show_global_augment_popup", False):
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    result = "quit"
                    running = False
                    break

                if event.type == pygame.KEYDOWN:
                    if gs.game_over:
                        continue
                    if (getattr(gs, "show_starter_popup", False)
                            or getattr(gs, "show_global_augment_popup", False)
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
                        if gs.me["gold"] >= REFRESH_COST:
                            gs.me["gold"] -= REFRESH_COST
                            gs.shop_locked = False
                            gs.refresh_shop()
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
                    if gs.is_battle_phase or gs.viewing_player_idx != -1:
                        continue
                    mx, my = event.pos
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
                            if gs.me["gold"] >= REFRESH_COST:
                                gs.me["gold"] -= REFRESH_COST
                                gs.shop_locked = False
                                gs.refresh_shop()
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
                        for r, idx in battle_selector_rects:
                            if r.collidepoint(mx, my):
                                gs.watched_battle_idx = idx
                                play_sfx("click")
                                break
                        continue
                    if gs.show_trait_popup:
                        gs.show_trait_popup = False
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
                        if gs.me["gold"] >= REFRESH_COST:
                            gs.me["gold"] -= REFRESH_COST
                            gs.shop_locked = False
                            gs.refresh_shop()
                            play_sfx("click")
                        else:
                            play_sfx("error")
                            gs._toast_msg("金币不足!")
                            gs.ai_assistant_say("no_gold")
                        continue
                    if trait_btn_rect and trait_btn_rect.collidepoint(mx, my):
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
                        for (r, bid) in bench_rects:
                            if r.collidepoint(mx, my):
                                if gs.viewing_player_idx == -1:
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
    font_title = get_font(64)
    font_lg = get_font(30)
    font_md = get_font(22)
    font_sm = get_font(16)
    font_dmg = get_font(26)
    scene = "menu"
    difficulty = "normal"
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
        if scene == "menu":
            set_dbg("场景: 主菜单")
            continue_btn, start_btn, multi_btn, update_btn, settings_btn, quit_btn = \
                draw_main_menu(
                    screen, font_title, font_lg, font_md, font_sm, W, H,
                    mouse_pos, difficulty)
            upd_close = upd_apply = None
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
                    elif update_btn.collidepoint(mx, my):
                        play_sfx("click")
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
        elif scene == "settings":
            set_dbg("场景: 设置")
            diff_rects, back_btn, changelog_btn = draw_settings_menu(
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
            result = run_game_session(screen, clock, difficulty,
                                       font_lg, font_md, font_sm, font_dmg,
                                       net=net, is_host=is_host,
                                       load_save=want_load)
            want_load = False
            if net:
                net.close()
                net = None
            if result == "quit":
                running = False
            elif result == "restart":
                pass
            elif result == "menu":
                scene = "menu"
    pygame.quit()


if __name__ == "__main__":
    main()