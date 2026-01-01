from setting import *
from random import randint
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
from time import time
from collections import deque

def pos_rand(w: int, h: int):
    return (randint(0,h-1),randint(0,w-1))

def count_bomb(pos: tuple, oth: list) -> str:
    x, y = pos
    x -= 1
    y -= 1
    s = 0
    for iy in range(y,y+3):
        for ix in range(x,x+3):
            if ((ix,iy) in oth) and ((ix,iy) != pos):
                s += 1
    return str(s)

class Kletka:
    def __init__(self,pos: tuple, val: str, active=False):
        self.y, self.x = pos
        self.val = val
        self.active = active

    @property
    def pos(self) -> tuple:
        return (self.x,self.y)
    
class Table:
    class clock:
        def __init__(self, time=int(time()), active=False):
            self.time_start = time
            self.active = active

        def info(self) -> str:
            res = '0:0'
            if self.active:
                allsec = int(time()) - self.time_start + 1
                minute, second = int(allsec // 60), int(allsec % 60)
                if allsec % 60 >= 10:
                    res = f"{minute}:{second}"
                else:
                    res = f"{minute}:0{second}"
            return res

        
    def __init__(self, poly: str, usid: int, chid: int, sesid: int,cb=CBOMBS[0]):
        self.user_id = usid
        self.chat_id = chid
        self.session_id = sesid
        self.w, self.h = [int(p) for p in poly.split('x')]
        self.bomb_pos = []
        self.bomb_count = cb
        self.void_poly = (self.w*self.h) - self.bomb_count
        self.map = []
        self.markup = InlineKeyboardMarkup(row_width=8)
        self.time_clock = self.clock()

    def generic_map(self, ipos: tuple):
        cur_map = []
        cy, cx = ipos
        cp = [(y,x) for y in range(cy-1,cy+2) for x in range(cx-1,cx+2)]
        for ind in range(self.bomb_count):
            cur_pos = pos_rand(self.w, self.h)
            while (cur_pos in self.bomb_pos) or (cur_pos in cp): cur_pos = pos_rand(self.w, self.h)
            self.bomb_pos.append(cur_pos)
        for i in range(self.h):
            cur_map.append('')
            for ii in range(self.w):
                if not ((i,ii) in self.bomb_pos):
                    char = str(count_bomb((i,ii),self.bomb_pos))
                    cur_map[i] += char
                else:
                    cur_map[i] += 'b'
        self.map = [[Kletka((i,ii),cur_map[i][ii],False) for ii in range(self.w)] for i in range(self.h)]
        self.time_clock.active = True
        self.time_clock.time_start = time()

    def flood_fill(self, pos: tuple):
        quene = deque([pos])
        visited = set()
        while quene:
            y, x = quene.popleft()
            if (y, x) in visited: continue
            visited.add((y, x))
            cell: Kletka = self.map[y][x]
            if not cell.active: 
                cell.active = True
                self.void_poly -= 1
            if cell.val != '0': continue
            for i in range(max(0, y-1),min(self.h, y+2)):
                for j in range(max(0, x-1), min(self.w, x+2)):
                    if not (i, j) in visited: quene.append((i, j))

    def update_markup(self):
        need_rebuild = False
        try:
            kb = self.markup.keyboard
            if (len(kb) != self.h) or any(len(row) != self.w for row in kb[-1]):
                need_rebuild = True
        except Exception: need_rebuild = True

        if need_rebuild:
            for r in range(self.h):
                for c in range(self.w):
                    kletka = self.map[r][c]
                    if kletka.active:
                        self.markup.keyboard[r][c] = InlineKeyboardButton(text=MAPGAME[kletka.val],callback_data=f"{c}.{r}")
                    
    def __str__(self):
        return f"{self.w}x{self.h} {self.bomb_count} бомб"
    
    @property
    def get_present(self)  -> int:
        bombcoin = 1
        minute = int(self.markup.keyboard[-1][-1].text.split(':')[0])
        if self.bomb_count == CBOMBS[3]:
            if minute < 2: bombcoin += 4
            if (minute >= 2) and (minute < 5): bombcoin += 3
            if (minute >= 5) and (minute < 10): bombcoin += 2
        if self.bomb_count == CBOMBS[2]:
            if minute < 2: bombcoin += 3
            if (minute >= 2) and (minute < 5): bombcoin += 2
            if (minute >= 5) and (minute < 10): bombcoin += 1
        if self.bomb_count == CBOMBS[1]:
            if minute < 2: bombcoin += 2
            if (minute >= 2) and (minute < 5): bombcoin += 1
        return bombcoin

    @property
    def get_void(self) -> str:
        void = ''
        for m in self.map:
            void += "0"*self.w+'|'
        void = void.rstrip('|')
        return void
    
    @property
    def win(self) -> bool:
        return self.void_poly == 0

class User:
    def __init__(self,id):
        pass

class PremiumGroups:
    def __init__(self,grid: int):
        self.id = grid
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(days=30)

    # def generator_card(MaxSize: int, i: int) -> str:
    #     conv_s = str(i)
    #     res = '0'*(MaxSize-len(conv_s))+conv_s
    #     return res
    
    @property
    def info(self) -> str:
        return f"Тамомшавии ПРО: {self.end_time}"
    
class UniversalKey(PremiumGroups): #new
    def __init__(self, grid: int, lenkey: int, count: int):
        super().__init__(grid)
        secret = "abcdefghijklmnopqrstuvwxyz"
        secret += secret.upper()
        secret += "0123456789"
        self.key = ''.join([secret[randint(0,len(secret)-1)] for k in range(lenkey)])
        self.count = count

    @property
    def info(self) -> str:
        return f"Тамомшавии калид: {self.end_time}\nМиқдори калид: {self.count}"