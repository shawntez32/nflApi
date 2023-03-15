import datetime as dt
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
from nflData import *
import os

dirname = os.path.dirname(__file__)

now = dt.datetime.now()
todays_date = dt.date(now.year,now.month,now.day)
sample_list = []

class NflTeam:
    w = 0
    l = 0

    def __init__(self,Name='',Day='',OT='',Opp='',Tm='',Opp2='',Cmp='',Att='',Yds='',TD='',Int='',Sk='',Yds2='',YA='',NYA='',CmpP='',Rate='',Att2='',Yds3='',YA2='',TD2='',FGM='',FGA='',XPM='',XPA='',Pnt='',Yds4='',DConv3='',DAtt3='',DConv4='',DAtt4='',ToP='',oName='',oDay='',oOT='',oOpp='',oTm='',oOpp2='',oCmp='',oAtt='',oYds='',oTD='',oInt='',oSk='',oYds2='',oYA='',oNYA='',oCmpP='',oRate='',oAtt2='',oYds3='',oYA2='',oTD2='',oFGM='',oFGA='',oXPM='',oXPA='',oPnt='',oYds4='',oDConv3='',oDAtt3='',oDConv4='',oDAtt4='',oToP=''):
        self.days  = Day
        self.dates  = Date
        self.ots  = OT
        self.opps  = Opp
        self.tms  = Tm
        self.opp2s  = Opp2
        self.cmps  = Cmp
        self.atts  = Att
        self.ydss  = Yds
        self.tds  = TD
        self.ints  = Int
        self.sks  = Sk
        self.yds2  = Yds2
        self.yas  = YA
        self.nyas  = NYA
        self.cmpps  = CmpP
        self.rates  = Rate
        self.att2s  = Att2
        self.yds3s  = Yds3
        self.ya2s  = YA2
        self.td2s  = TD2
        self.fgms  = FGM
        self.fgas  = FGA
        self.xpms  = XPM
        self.xpas  = XPA
        self.pnts  = Pnt
        self.yds4s  = Yds4
        self.dconv3s  = DConv3
        self.datt3s  = DAtt3
        self.dconv4s  = DConv4
        self.datt4s  = DAtt4
        self.tops  = ToP
        self.odays  = oDay
        self.odates  = oDate
        self.oots  = oOT
        self.oopps  = oOpp
        self.otms  = oTm
        self.oopp2s  = oOpp2
        self.ocmps  = oCmp
        self.oatts  = oAtt
        self.oydss  = oYds
        self.otds  = oTD
        self.oints  = oInt
        self.osks  = oSk
        self.oyds2  = oYds2
        self.oyas  = oYA
        self.onyas  = oNYA
        self.ocmpps  = oCmpP
        self.orates  = oRate
        self.oatt2s  = oAtt2
        self.oyds3s  = oYds3
        self.oya2s  = oYA2
        self.otd2s  = oTD2
        self.ofgms  = oFGM
        self.ofgas  = oFGA
        self.oxpms  = oXPM
        self.oxpas  = oXPA
        self.opnts  = oPnt
        self.oyds4s  = oYds4
        self.odconv3s  = oDConv3
        self.odatt3s  = oDAtt3
        self.odconv4s  = oDConv4
        self.odatt4s  = oDAtt4
        self.otops  = oToP

    def get_stats(self,team,year):
        self.w = 0
        self.l = 0
        team = team
        year = year
        filename = os.path.join(dirname, f'nflDb/{team}-{year}-stats.db')
        conn = sqlite3.connect(filename)
        cur = conn.cursor()
        try:
            cur.execute('SELECT * FROM Stats')
        except:
            cur.execute('SELECT * FROM Statz')
        rows = cur.fetchall()
        selected_team = rows[0:int(len(rows) // 2 - 1)]
        opp_team = rows[int(len(rows)) // 2:-1]
        results = [selected_team,opp_team]
        print(results)
        conn.close()
        return results

    def last2(self,team,year):
        self.w = 0
        self.l = 0
        team = team
        year = year
        conn = sqlite3.connect(f'{team}-{year}-stats.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Stats')
        rows = cur.fetchall()
        team_stats = pd.DataFrame(rows, columns=['Day','OT','Opp','Tm','Opp2','Cmp','Att','Yds','TD','Int','Sk','Yds2','YA','NYA','CmpP','Rate','Att2','Yds3','YA2','TD2','FGM','FGA','XPM','XPA','Pnt','Yds4','DConv3','DAtt3','DConv4','DAtt4','ToP'])
        self.days  = team_stats['Day'].head(2)
        self.ots  = team_stats['OT'].head(2)
        self.opps  = team_stats['Opp'].head(2)
        self.tms  = team_stats['Tm'].head(2)
        self.opp2s  =team_stats['Opp2'].head(2)
        self.cmps  = team_stats['Cmp'].head(2)
        self.atts  = team_stats['Att'].head(2)
        self.ydss  = team_stats['Yds'].head(2)
        self.tds  = team_stats['TD'].head(2)
        self.ints  = team_stats['Int'].head(2)
        self.sks  = team_stats['sks'].head(2)
        self.yds2  = team_stats['Yds2'].head(2)
        self.yas  = team_stats['YA'].head(2)
        self.nyas  = team_stats['NYA'].head(2)
        self.cmpps  = team_stats['CmpP'].head(2)
        self.rates  = team_stats['Rate'].head(2)
        self.att2s  = team_stats['Att2'].head(2)
        self.yds3s  = team_stats['Yds3'].head(2)
        self.ya2s  = team_stats['YA2'].head(2)
        self.td2s  = team_stats['TD2'].head(2)
        self.fgms  = team_stats['FGM'].head(2)
        self.fgas  = team_stats['FGA'].head(2)
        self.xpms  = team_stats['XPM'].head(2)
        self.xpas  = team_stats['XPA'].head(2)
        self.pnts  = team_stats['Pnt'].head(2)
        self.yds4s  = team_stats['Yds4'].head(2)
        self.dconv3s  = team_stats['DConv3'].head(2)
        self.datt3s  = team_stats['DAtt3'].head(2)
        self.dconv4s  = team_stats['DConv4'].head(2)
        self.datt4s  = team_stats['DAtt4'].head(2)
        self.otops  = team_stats['ToP'].tail(2)
        self.odays  = team_stats['Day'].tail(2)
        self.oots  = team_stats['OT'].tail(2)
        self.oopps  = team_stats['Opp'].tail(2)
        self.otms  = team_stats['Tm'].tail(2)
        self.oopp2s  =team_stats['Opp2'].tail(2)
        self.ocmps  = team_stats['Cmp'].tail(2)
        self.oatts  = team_stats['Att'].tail(2)
        self.oydss  = team_stats['Yds'].tail(2)
        self.otds  = team_stats['TD'].tail(2)
        self.oints  = team_stats['Int'].tail(2)
        self.osks  = team_stats['sks'].tail(2)
        self.oyds2  = team_stats['Yds2'].tail(2)
        self.oyas  = team_stats['YA'].tail(2)
        self.onyas  = team_stats['NYA'].tail(2)
        self.ocmpps  = team_stats['CmpP'].tail(2)
        self.orates  = team_stats['Rate'].tail(2)
        self.oatt2s  = team_stats['Att2'].tail(2)
        self.oyds3s  = team_stats['Yds3'].tail(2)
        self.oya2s  = team_stats['YA2'].tail(2)
        self.otd2s  = team_stats['TD2'].tail(2)
        self.ofgms  = team_stats['FGM'].tail(2)
        self.ofgas  = team_stats['FGA'].tail(2)
        self.oxpms  = team_stats['XPM'].tail(2)
        self.oxpas  = team_stats['XPA'].tail(2)
        self.opnts  = team_stats['Pnt'].tail(2)
        self.oyds4s  = team_stats['Yds4'].tail(2)
        self.odconv3s  = team_stats['DConv3'].tail(2)
        self.odatt3s  = team_stats['DAtt3'].tail(2)
        self.odconv4s  = team_stats['DConv4'].tail(2)
        self.odatt4s  = team_stats['DAtt4'].tail(2)
        self.otops  = team_stats['ToP'].tail(2)

    def last4(self,team,year):
        self.w = 0
        self.l = 0
        team = team
        year = year
        conn = sqlite3.connect(f'{team}-{year}-stats.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Stats')
        rows = cur.fetchall()
        team_stats = pd.DataFrame(rows, columns=['Day','OT','Opp','Tm','Opp2','Cmp','Att','Yds','TD','Int','Sk','Yds2','YA','NYA','CmpP','Rate','Att2','Yds3','YA2','TD2','FGM','FGA','XPM','XPA','Pnt','Yds4','DConv3','DAtt3','DConv4','DAtt4','ToP'])
        team_stats_div1 = team_stats.head(16)
        team_stats_div2 = team_stats.tail(16)
        self.days  = team_stats_div1['Day'].tail(4)
        self.ots  = team_stats_div1['OT'].tail(4)
        self.opps  = team_stats_div1['Opp'].tail(4)
        self.tms  = team_stats_div1['Tm'].tail(4)
        self.opp2s  =team_stats_div1['Opp2'].tail(4)
        self.cmps  = team_stats_div1['Cmp'].tail(4)
        self.atts  = team_stats_div1['Att'].tail(4)
        self.ydss  = team_stats_div1['Yds'].tail(4)
        self.tds  = team_stats_div1['TD'].tail(4)
        self.ints  = team_stats_div1['Int'].tail(4)
        self.sks  = team_stats_div1['sks'].tail(4)
        self.yds2  = team_stats_div1['Yds2'].tail(4)
        self.yas  = team_stats_div1['YA'].tail(4)
        self.nyas  = team_stats_div1['NYA'].tail(4)
        self.cmpps  = team_stats_div1['CmpP'].tail(4)
        self.rates  = team_stats_div1['Rate'].tail(4)
        self.att2s  = team_stats_div1['Att2'].tail(4)
        self.yds3s  = team_stats_div1['Yds3'].tail(4)
        self.ya2s  = team_stats_div1['YA2'].tail(4)
        self.td2s  = team_stats_div1['TD2'].tail(4)
        self.fgms  = team_stats_div1['FGM'].tail(4)
        self.fgas  = team_stats_div1['FGA'].tail(4)
        self.xpms  = team_stats_div1['XPM'].tail(4)
        self.xpas  = team_stats_div1['XPA'].tail(4)
        self.pnts  = team_stats_div1['Pnt'].tail(4)
        self.yds4s  = team_stats_div1['Yds4'].tail(4)
        self.dconv3s  = team_stats_div1['DConv3'].tail(4)
        self.datt3s  = team_stats_div1['DAtt3'].tail(4)
        self.dconv4s  = team_stats_div1['DConv4'].tail(4)
        self.datt4s  = team_stats_div1['DAtt4'].tail(4)
        self.tops  = team_stats['ToP'].tail(4)
        self.odays  = team_stats_div2['Day'].tail(4)
        self.oots  = team_stats_div2['OT'].tail(4)
        self.oopps  = team_stats_div2['Opp'].tail(4)
        self.otms  = team_stats_div2['Tm'].tail(4)
        self.oopp2s  =team_stats_div2['Opp2'].tail(4)
        self.ocmps  = team_stats_div2['Cmp'].tail(4)
        self.oatts  = team_stats_div2['Att'].tail(4)
        self.oydss  = team_stats_div2['Yds'].tail(4)
        self.otds  = team_stats_div2['TD'].tail(4)
        self.oints  = team_stats_div2['Int'].tail(4)
        self.osks  = team_stats_div2['sks'].tail(4)
        self.oyds2  = team_stats_div2['Yds2'].tail(4)
        self.oyas  = team_stats_div2['YA'].tail(4)
        self.onyas  = team_stats_div2['NYA'].tail(4)
        self.ocmpps  = team_stats_div2['CmpP'].tail(4)
        self.orates  = team_stats_div2['Rate'].tail(4)
        self.oatt2s  = team_stats_div2['Att2'].tail(4)
        self.oyds3s  = team_stats_div2['Yds3'].tail(4)
        self.oya2s  = team_stats_div2['YA2'].tail(4)
        self.otd2s  = team_stats_div2['TD2'].tail(4)
        self.ofgms  = team_stats_div2['FGM'].tail(4)
        self.ofgas  = team_stats_div2['FGA'].tail(4)
        self.oxpms  = team_stats_div2['XPM'].tail(4)
        self.oxpas  = team_stats_div2['XPA'].tail(4)
        self.opnts  = team_stats_div2['Pnt'].tail(4)
        self.oyds4s  = team_stats_div2['Yds4'].tail(4)
        self.odconv3s  = team_stats_div2['DConv3'].tail(4)
        self.odatt3s  = team_stats_div2['DAtt3'].tail(4)
        self.odconv4s  = team_stats_div2['DConv4'].tail(4)
        self.odatt4s  = team_stats_div2['DAtt4'].tail(4)
        self.otops  = team_stats_div2['ToP'].tail(4)

    def last8(self,team,year):
        self.w = 0
        self.l = 0
        team = team
        year = year
        conn = sqlite3.connect(f'{team}-{year}-stats.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Stats')
        rows = cur.fetchall()
        team_stats = pd.DataFrame(rows, columns=['Day','OT','Opp','Tm','Opp2','Cmp','Att','Yds','TD','Int','Sk','Yds2','YA','NYA','CmpP','Rate','Att2','Yds3','YA2','TD2','FGM','FGA','XPM','XPA','Pnt','Yds4','DConv3','DAtt3','DConv4','DAtt4','ToP'])
        team_stats_div1 = team_stats.head(16)
        team_stats_div2 = team_stats.tail(16)
        self.days  = team_stats_div1['Day'].tail(8)
        self.ots  = team_stats_div1['OT'].tail(8)
        self.opps  = team_stats_div1['Opp'].tail(8)
        self.tms  = team_stats_div1['Tm'].tail(8)
        self.opp2s  =team_stats_div1['Opp2'].tail(8)
        self.cmps  = team_stats_div1['Cmp'].tail(8)
        self.atts  = team_stats_div1['Att'].tail(8)
        self.ydss  = team_stats_div1['Yds'].tail(8)
        self.tds  = team_stats_div1['TD'].tail(8)
        self.ints  = team_stats_div1['Int'].tail(8)
        self.sks  = team_stats_div1['sks'].tail(8)
        self.yds2  = team_stats_div1['Yds2'].tail(8)
        self.yas  = team_stats_div1['YA'].tail(8)
        self.nyas  = team_stats_div1['NYA'].tail(8)
        self.cmpps  = team_stats_div1['CmpP'].tail(8)
        self.rates  = team_stats_div1['Rate'].tail(8)
        self.att2s  = team_stats_div1['Att2'].tail(8)
        self.yds3s  = team_stats_div1['Yds3'].tail(8)
        self.ya2s  = team_stats_div1['YA2'].tail(8)
        self.td2s  = team_stats_div1['TD2'].tail(8)
        self.fgms  = team_stats_div1['FGM'].tail(8)
        self.fgas  = team_stats_div1['FGA'].tail(8)
        self.xpms  = team_stats_div1['XPM'].tail(8)
        self.xpas  = team_stats_div1['XPA'].tail(8)
        self.pnts  = team_stats_div1['Pnt'].tail(8)
        self.yds4s  = team_stats_div1['Yds4'].tail(8)
        self.dconv3s  = team_stats_div1['DConv3'].tail(8)
        self.datt3s  = team_stats_div1['DAtt3'].tail(8)
        self.dconv4s  = team_stats_div1['DConv4'].tail(8)
        self.datt4s  = team_stats_div1['DAtt4'].tail(8)
        self.tops  = team_stats['ToP'].tail(8)
        self.odays  = team_stats_div2['Day'].tail(8)
        self.oots  = team_stats_div2['OT'].tail(8)
        self.oopps  = team_stats_div2['Opp'].tail(8)
        self.otms  = team_stats_div2['Tm'].tail(8)
        self.oopp2s  =team_stats_div2['Opp2'].tail(8)
        self.ocmps  = team_stats_div2['Cmp'].tail(8)
        self.oatts  = team_stats_div2['Att'].tail(8)
        self.oydss  = team_stats_div2['Yds'].tail(8)
        self.otds  = team_stats_div2['TD'].tail(8)
        self.oints  = team_stats_div2['Int'].tail(8)
        self.osks  = team_stats_div2['sks'].tail(8)
        self.oyds2  = team_stats_div2['Yds2'].tail(8)
        self.oyas  = team_stats_div2['YA'].tail(8)
        self.onyas  = team_stats_div2['NYA'].tail(8)
        self.ocmpps  = team_stats_div2['CmpP'].tail(8)
        self.orates  = team_stats_div2['Rate'].tail(8)
        self.oatt2s  = team_stats_div2['Att2'].tail(8)
        self.oyds3s  = team_stats_div2['Yds3'].tail(8)
        self.oya2s  = team_stats_div2['YA2'].tail(8)
        self.otd2s  = team_stats_div2['TD2'].tail(8)
        self.ofgms  = team_stats_div2['FGM'].tail(8)
        self.ofgas  = team_stats_div2['FGA'].tail(8)
        self.oxpms  = team_stats_div2['XPM'].tail(8)
        self.oxpas  = team_stats_div2['XPA'].tail(8)
        self.opnts  = team_stats_div2['Pnt'].tail(8)
        self.oyds4s  = team_stats_div2['Yds4'].tail(8)
        self.odconv3s  = team_stats_div2['DConv3'].tail(8)
        self.odatt3s  = team_stats_div2['DAtt3'].tail(8)
        self.odconv4s  = team_stats_div2['DConv4'].tail(8)
        self.odatt4s  = team_stats_div2['DAtt4'].tail(8)
        self.otops  = team_stats_div2['ToP'].tail(8)

x = NflTeam()
results = x.get_stats('rai',2022)