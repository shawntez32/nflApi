import sqlite3
import requests
from bs4 import BeautifulSoup

Week  = []
Day  = []
Date  = []
OT  = []
Opp  = []
Tm  = []
Opp2  = []
Cmp  = []
Att  = []
Yds  = []
TD  = []
Int  = []
Sk  = []
Yds2  = []
YA  = []
NYA  = []
Cmp  = []
Rate  = []
Att2  = []
Yds3  = []
YA2  = []
TD2  = []
FGM  = []
FGA  = []
XPM  = []
XPA  = []
Pnt  = []
Yds4  = []
DConv3  = []
DAtt3  = []
DConv4  = []
DAtt4  = []
ToP  = []
oDate = []

def nfldb(nfl_team,year):
    nfl_team = nfl_team
    year = year
    sample_list = []
    s = 'stats'
    a = 0
    b = 0
    content = requests.get('https://www.pro-football-reference.com/teams/{}/{}/gamelog/'.format(str.lower(nfl_team),year))
    soup = BeautifulSoup(content.content, 'html.parser')
    td = soup.find_all('td')
    for td1 in td:
        sample_list.append(td1.text)
        Day  = sample_list[1::35]
        Date  = sample_list[2::35]
        OT  = sample_list[4::35]
        Opp  = sample_list[6::35]
        Tm  = sample_list[7::35]
        Opp2  = sample_list[8::35]
        Cmp  = sample_list[9::35]
        Att  = sample_list[10::35]
        Yds  = sample_list[11::35]
        TD  = sample_list[12::35]
        Int  = sample_list[13::35]
        Sk  = sample_list[14::35]
        Yds2  = sample_list[15::35]
        YA  = sample_list[16::35]
        NYA  = sample_list[17::35]
        CmpP  = sample_list[18::35]
        Rate  = sample_list[19::35]
        Att2  = sample_list[20::35]
        Yds3  = sample_list[21::35]
        YA2  = sample_list[22::35]
        TD2  = sample_list[23::35]
        FGM  = sample_list[24::35]
        FGA  = sample_list[25::35]
        XPM  = sample_list[26::35]
        XPA  = sample_list[27::35]
        Pnt  = sample_list[28::35]
        Yds4  = sample_list[29::35]
        DConv3  = sample_list[30::35]
        DAtt3  = sample_list[31::35]
        DConv4  = sample_list[32::35]
        DAtt4  = sample_list[33::35]
        ToP  = sample_list[34::35]
        Stats = { 'Day ' : Day,' Date ' : Date,' OT ' : OT,' Opp ' : Opp,' Tm ' : Tm,' Opp2 ' : Opp2,' Cmp ' : Cmp,' Att ' : Att,' Yds ' : Yds,' TD ' : TD,' Int ' : Int,' Sk ' : Sk,' Yds2 ' : Yds2,' YA ' : YA,' NYA ' : NYA,' Cmp% ' : Cmp,' Rate ' : Rate,' Att2 ' : Att2,' Yds3 ' : Yds3,' YA2 ' : YA2,' TD2 ' : TD2,' FGM ' : FGM,' FGA ' : FGA,' XPM ' : XPM,' XPA ' : XPA,' Pnt ' : Pnt,' Yds4 ' : Yds4,' DConv3 ' : DConv3,' DAtt3 ' : DAtt3,' DConv4 ' : DConv4,' DAtt4 ' : DAtt4,' ToP ' : ToP}
        conn = sqlite3.connect('{}-{}-{}.db'.format(nfl_team,year,s))
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Stats(Day TEXT,Date TEXT,OT TEXT,Opp TEXT,Tm TEXT,Opp2 TEXT,Cmp TEXT,Att TEXT,Yds TEXT,TD TEXT,Int TEXT,Sk TEXT,Yds2 TEXT,YA TEXT,NYA TEXT,CmpP TEXT,Rate TEXT,Att2 TEXT,Yds3 TEXT,YA2 TEXT,TD2 TEXT,FGM TEXT,FGA TEXT,XPM TEXT,XPA TEXT,Pnt TEXT,Yds4 TEXT,DConv3 TEXT,DAtt3 TEXT,DConv4 TEXT,DAtt4 TEXT,ToP TEXT)""")
    for e in Date:
        days  = Day[a]
        dates  = Date[a]
        ots  = OT[a]
        opps  = Opp[a]
        tms  = Tm[a]
        opp2s  = Opp2[a]
        cmps  = Cmp[a]
        atts  = Att[a]
        ydss  = Yds[a]
        tds  = TD[a]
        ints  = Int[a]
        sks  = Sk[a]
        yds2  = Yds2[a]
        yas  = YA[a]
        nyas  = NYA[a]
        cmpps  = CmpP[a]
        rates  = Rate[a]
        att2s  = Att2[a]
        yds3s  = Yds3[a]
        ya2s  = YA2[a]
        td2s  = TD2[a]
        fgms  = FGM[a]
        fgas  = FGA[a]
        xpms  = XPM[a]
        xpas  = XPA[a]
        pnts  = Pnt[a]
        yds4s  = Yds4[a]
        dconv3s  = DConv3[a]
        datt3s  = DAtt3[a]
        dconv4s  = DConv4[a]
        datt4s  = DAtt4[a]
        tops  = ToP[a]
        cur.execute("INSERT INTO Stats(Day,Date,OT,Opp,Tm,Opp2,Cmp,Att,Yds,TD,Int,Sk,Yds2,YA,NYA,CmpP,Rate,Att2,Yds3,YA2,TD2,FGM,FGA,XPM,XPA,Pnt,Yds4,DConv3,DAtt3,DConv4,DAtt4,ToP) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (days,dates,ots,opps,tms,opp2s,cmps,atts,ydss,tds,ints,sks,yds2,yas,nyas,cmpps,rates,att2s,yds3s,ya2s,td2s,fgms,fgas,xpms,xpas,pnts,yds4s,dconv3s,datt3s,dconv4s,datt4s,tops))
        conn.commit()
        try:
            a += 1
        except:
            pass