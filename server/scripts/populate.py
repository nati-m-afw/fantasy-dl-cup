from main import db, Players, Dept, Users, userPlayers,Match, Gameweek, Event



def populate():
    userPlayers.query.delete()
    Event.query.delete()
    Players.query.delete()
    Dept.query.delete()
    Users.query.delete()
    Match.query.delete()
    Gameweek.query.delete()
    Event.query.delete()
    
   

    dept1 = Dept(id=1,dName='InfoTech')
    dept2 = Dept(id=2,dName='Mechanical')
    dept3 = Dept(id=3,dName='Electrical')
    dept4 = Dept(id=4,dName='Software')
    dept5 = Dept(id=5,dName='Chemical')
    dept6 = Dept(id=6,dName='BioMedical')
    
    
    # Dep't 1 IT
    
    
    p1 = Players(fname="Michael", lname="Alemayehu", position="goalkeeper", dept_id=1)
    p3 = Players(fname="Zekarias", lname="Alemu", position="defender", dept_id=1)
    p6 = Players(fname="Kevin", lname="Shitaye", position="midfielder", dept_id=1)
    p9 = Players(fname="Beken", lname="Adugna", position="striker", dept_id=1)
    # p25 = Players(fname="Barok", lname="Dagim", position="defender", dept_id=1)
    # p26 = Players(fname="Lola", lname="Alonne", position="midfielder", dept_id=1)
    # p27 = Players(fname="Tekle", lname="Tk", position="midfielder", dept_id=1)
    
    # Dep't 2 Mechanical
    p2 = Players(fname="Addis", lname="Markos", position="goalkeeper", dept_id=2)
    p4 = Players(fname="Matios", lname="Soit", position="defender", dept_id=2)
    p7 = Players(fname="Kaleb", lname="Lak", position="midfielder", dept_id=2)
    p10 = Players(fname="Tesfahun", lname="Nuha", position="striker", dept_id=2)
    # p28 = Players(fname="Kidus", lname="Kd", position="defender", dept_id=2)
    # p29 = Players(fname="Sofonias", lname="Sainof", position="midfielder", dept_id=2)
    # p30 = Players(fname="Sports", lname="Guy", position="striker", dept_id=2)
    
            
    # Dep't 3  Electrical
    p22 = Players(fname="Atalale", lname="Elal", position="goalkeeper", dept_id=3)     
    p5 = Players(fname="Sami", lname="Ima", position="defender", dept_id=3)
    p21 = Players(fname="Temesgen", lname="Negs",position="midfielder",dept_id=3)
    p8 = Players(fname="Biruk", lname="Kuri", position="striker", dept_id=3)
    # p31 = Players(fname="Abenezer", lname="Rez", position="striker", dept_id=3)
    # p32 = Players(fname="Desta", lname="Atse", position="defender", dept_id=3)
    # p33 = Players(fname="Hannibal", lname="Fehmi", position="midfielder", dept_id=3)

    # Dep't 4 Software
    p12 = Players(fname="Elias", lname="Melaku", position="goalkeeper", dept_id=4)
    p14 = Players(fname="Abel", lname="Leb", position="defender", dept_id=4)
    p11 = Players(fname="Abraham", lname="Mahar", position="midfielder", dept_id=4)
    p19 = Players(fname="Nahom", lname="Tamru", position="striker", dept_id=4)
    # p34 = Players(fname="Biniyam", lname="Mayin", position="midfielder", dept_id=4)
    # p35 = Players(fname="Biruk", lname="Seaman", position="striker", dept_id=4)
    # p36 = Players(fname="Bemnet", lname="Uteb", position="defender", dept_id=4)


    
    
    # Dep't 5 Chemical
    p13 = Players(fname="Yeabsira", lname="Aris", position="goalkeeper", dept_id=5)
    p15 = Players(fname="Aman", lname="A", position="defender", dept_id=5)
    p17 = Players(fname="Amant", lname="T", position="midfielder", dept_id=5)
    p20 = Players(fname="Habtamu", lname="Lingerew", position="striker", dept_id=5)
    # p37 = Players(fname="Lingerew", lname="Habtamu", position="striker", dept_id=5)
    # p38 = Players(fname="Ebenezer", lname="Eman", position="defender", dept_id=5)
    # p39 = Players(fname="Chem", lname="Lin", position="midfielder", dept_id=5)

        
       
    # Dep't 6 Biomedical
    p23 = Players(fname="Yared", lname="Der", position="goalkeeper", dept_id=6)
    p16 = Players(fname="Yonas", lname="Sonar", position="defender", dept_id=6)
    p18 = Players(fname="Mikiyas", lname="Sayik", position="midfielder", dept_id=6)
    p24 = Players(fname="Yonathan", lname="Yg", position="striker", dept_id=6)
    # p40 = Players(fname="Mike", lname="Copy", position="striker", dept_id=6)
    # p41 = Players(fname="Iyoas", lname="T", position="midfielder", dept_id=6)
    # p42 = Players(fname="Cinder", lname="Bear", position="defender", dept_id=6)

    

    #Gameweeks
    gw1 =Gameweek(status='ALL_UPCOMING')
    gw2 =Gameweek(status='ALL_UPCOMING')
    gw3 =Gameweek(status='ALL_UPCOMING')
    gw4 =Gameweek(status='ALL_UPCOMING')
    gw5 =Gameweek(status='ALL_UPCOMING')


    #GW1
    m1 =Match(team=4,opponent=5,game_week=1,time="16:00",date="2021-03-03",state=0,score="")
    m2 =Match(team=6,opponent=2,game_week=1,time="16:00",date="2021-03-03",state=0,score="")
    m3 =Match(team=1,opponent=3,game_week=1,time="16:00",date="2021-03-03",state=0,score="")

    #GW2
    m4 =Match(team=2,opponent=4,game_week=2,time="16:00",date="2021-10-03",state=0,score="")
    m5 =Match(team=1,opponent=5,game_week=2,time="16:00",date="2021-10-03",state=0,score="")
    m6 =Match(team=6,opponent=3,game_week=2,time="16:00",date="2021-10-03",state=0,score="")

    #GW3
    m7 =Match(team=4,opponent=1,game_week=3,time="16:00",date="2021-17-03",state=0,score="")
    m8 =Match(team=2,opponent=3,game_week=3,time="16:00",date="2021-17-03",state=0,score="")
    m9 =Match(team=5,opponent=6,game_week=3,time="16:00",date="2021-17-03",state=0,score="")

    #GW4
    m10=Match(team=3,opponent=4,game_week=4,time="16:00",date="2021-24-03",state=0,score="")
    m11=Match(team=6,opponent=1,game_week=4,time="16:00",date="2021-24-03",state=0,score="")
    m12=Match(team=5,opponent=2,game_week=4,time="16:00",date="2021-24-03",state=0,score="")

    #GW5
    m13 =Match(team=4,opponent=6,game_week=5,time="16:00",date="2021-31-03",state=0,score="")
    m14 =Match(team=3,opponent=5,game_week=5,time="16:00",date="2021-31-03",state=0,score="")
    m15 =Match(team=1,opponent=2,game_week=5,time="16:00",date="2021-31-03",state=0,score="")


    # Match Event stats
    # GW1
    
    # Team 1 vs 2
    #Team 1
    e1 =  Event(players_id=3,match_id=1,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0) 
    e2 =  Event(players_id=6,match_id=1,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e3 =  Event(players_id=9,match_id=1,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e4 =  Event(players_id=1,match_id=1,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    # Team2
    e5 =  Event(players_id=2,match_id=1,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e6 =  Event(players_id=10,match_id=1,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e7 =  Event(players_id=7,match_id=1,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e8 =  Event(players_id=4,match_id=1,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 3 v 4
    # Team 3
    e9 =  Event(players_id=5,match_id=2,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e10 = Event(players_id=8,match_id=2,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e11 = Event(players_id=22,match_id=2,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e12 = Event(players_id=21,match_id=2,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 4
    e13 =  Event(players_id=19,match_id=2,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e14 = Event(players_id=14,match_id=2,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e15 = Event(players_id=11,match_id=2,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e16 = Event(players_id=12,match_id=2,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
   
    # Team 5 v 6

    # Team 5
    e17 = Event(players_id=13,match_id=3,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e18 = Event(players_id=15,match_id=3,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e19 = Event(players_id=17,match_id=3,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e20 = Event(players_id=20,match_id=3,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 6
    e21 =  Event(players_id=18,match_id=3,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e22 = Event(players_id=16,match_id=3,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e23 = Event(players_id=23,match_id=3,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e24 = Event(players_id=24,match_id=3,gameweek_id=1,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    db.session.add_all([
        # Add Departments
        dept1, dept2, dept3, dept4, dept5, dept6
        # Add Players
        ,p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,p21,p22,p23,p24
        # Add Matches
        ,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15
        # Add Gamweeks
        ,gw1,gw2,gw3,gw3,gw4,gw5
        # Add events
        ,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,
        
        # up1,up2,up3,up4
                        ])
  
    db.session.commit()