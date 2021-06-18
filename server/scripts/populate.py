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

    
    # Dep't 2 Mechanical
    p2 = Players(fname="Addis", lname="Markos", position="goalkeeper", dept_id=2)
    p4 = Players(fname="Matios", lname="Soit", position="defender", dept_id=2)
    p7 = Players(fname="Kaleb", lname="Lak", position="midfielder", dept_id=2)
    p10 = Players(fname="Tesfahun", lname="Nuha", position="striker", dept_id=2)
    
    
            
    # Dep't 3  Electrical
    p22 = Players(fname="Atalale", lname="Elal", position="goalkeeper", dept_id=3)     
    p5 = Players(fname="Sami", lname="Ima", position="defender", dept_id=3)
    p21 = Players(fname="Temesgen", lname="Negs",position="midfielder",dept_id=3)
    p8 = Players(fname="Biruk", lname="Kuri", position="striker", dept_id=3)
    

    # Dep't 4 Software
    p12 = Players(fname="Elias", lname="Melaku", position="goalkeeper", dept_id=4)
    p14 = Players(fname="Abel", lname="Leb", position="defender", dept_id=4)
    p11 = Players(fname="Abraham", lname="Mahar", position="midfielder", dept_id=4)
    p19 = Players(fname="Nahom", lname="Tamru", position="striker", dept_id=4)
    


    
    
    # Dep't 5 Chemical
    p13 = Players(fname="Yeabsira", lname="Aris", position="goalkeeper", dept_id=5)
    p15 = Players(fname="Aman", lname="A", position="defender", dept_id=5)
    p17 = Players(fname="Amant", lname="T", position="midfielder", dept_id=5)
    p20 = Players(fname="Habtamu", lname="Lingerew", position="striker", dept_id=5)
    

        
       
    # Dep't 6 Biomedical
    p23 = Players(fname="Yared", lname="Der", position="goalkeeper", dept_id=6)
    p16 = Players(fname="Yonas", lname="Sonar", position="defender", dept_id=6)
    p18 = Players(fname="Mikiyas", lname="Sayik", position="midfielder", dept_id=6)
    p24 = Players(fname="Yonathan", lname="Yg", position="striker", dept_id=6)
 

    

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
    ######################################################################################################################
     # GW2
    
    # Team 1 vs 2
    #Team 1
    e25 =  Event(players_id=3,match_id=1,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0) 
    e26 =  Event(players_id=6,match_id=1,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e27 =  Event(players_id=9,match_id=1,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e28 =  Event(players_id=1,match_id=1,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    # Team2
    e29 =  Event(players_id=2,match_id=1,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e30 =  Event(players_id=10,match_id=1,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e31 =  Event(players_id=7,match_id=1,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e32 =  Event(players_id=4,match_id=1,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 3 v 4
    # Team 3
    e33 =  Event(players_id=5,match_id=2,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e34 = Event(players_id=8,match_id=2,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e35 = Event(players_id=22,match_id=2,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e36 = Event(players_id=21,match_id=2,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 4
    e37 =  Event(players_id=19,match_id=2,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e38 = Event(players_id=14,match_id=2,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e39 = Event(players_id=11,match_id=2,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e40 = Event(players_id=12,match_id=2,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
   
    # Team 5 v 6

    # Team 5
    e41 = Event(players_id=13,match_id=3,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e42 = Event(players_id=15,match_id=3,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e43 = Event(players_id=17,match_id=3,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e44 = Event(players_id=20,match_id=3,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 6
    e45 =  Event(players_id=18,match_id=3,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e46 = Event(players_id=16,match_id=3,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e47 = Event(players_id=23,match_id=3,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e48 = Event(players_id=24,match_id=3,gameweek_id=2,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    ##############################################################################################################################################
    # GW3
    
    # Team 1 vs 2
    #Team 1
    e49 =  Event(players_id=3,match_id=1,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0) 
    e50 =  Event(players_id=6,match_id=1,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e51 =  Event(players_id=9,match_id=1,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e52 =  Event(players_id=1,match_id=1,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    # Team2
    e53 =  Event(players_id=2,match_id=1,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e54 =  Event(players_id=10,match_id=1,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e55 =  Event(players_id=7,match_id=1,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e56 =  Event(players_id=4,match_id=1,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 3 v 4
    # Team 3
    e57 =  Event(players_id=5,match_id=2,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e58 = Event(players_id=8,match_id=2,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e59 = Event(players_id=22,match_id=2,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e60 = Event(players_id=21,match_id=2,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 4
    e61 =  Event(players_id=19,match_id=2,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e62 = Event(players_id=14,match_id=2,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e63 = Event(players_id=11,match_id=2,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e64 = Event(players_id=12,match_id=2,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
   
    # Team 5 v 6

    # Team 5
    e65 = Event(players_id=13,match_id=3,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e66 = Event(players_id=15,match_id=3,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e67 = Event(players_id=17,match_id=3,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e68 = Event(players_id=20,match_id=3,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 6
    e69 =  Event(players_id=18,match_id=3,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e70 = Event(players_id=16,match_id=3,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e71 = Event(players_id=23,match_id=3,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e72 = Event(players_id=24,match_id=3,gameweek_id=3,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    ##############################################################################################################################################
    
    # GW4
    
    # Team 1 vs 2
    #Team 1
    e73 =  Event(players_id=3,match_id=1,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0) 
    e74 =  Event(players_id=6,match_id=1,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e75 =  Event(players_id=9,match_id=1,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e76 =  Event(players_id=1,match_id=1,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    # Team2
    e77 =  Event(players_id=2,match_id=1,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e78 =  Event(players_id=10,match_id=1,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e79 =  Event(players_id=7,match_id=1,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e80 =  Event(players_id=4,match_id=1,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)

    # Team 3 v 4
    # Team 3
    e81 =  Event(players_id=5,match_id=2,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e82 = Event(players_id=8,match_id=2,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e83 = Event(players_id=22,match_id=2,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e84 = Event(players_id=21,match_id=2,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 4
    e85 =  Event(players_id=19,match_id=2,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e86 = Event(players_id=14,match_id=2,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e87 = Event(players_id=11,match_id=2,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e88 = Event(players_id=12,match_id=2,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
   
    # Team 5 v 6

    # Team 5
    e89 = Event(players_id=13,match_id=3,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e90 = Event(players_id=15,match_id=3,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e91 = Event(players_id=17,match_id=3,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e92 = Event(players_id=20,match_id=3,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 6
    e93 =  Event(players_id=18,match_id=3,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e94 = Event(players_id=16,match_id=3,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e95 = Event(players_id=23,match_id=3,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e96 = Event(players_id=24,match_id=3,gameweek_id=4,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    ##############################################################################################################################################
    # GW5
    
    # Team 1 vs 4
    #Team 1
    e97 =  Event(players_id=3,match_id=1,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0) 
    e98 =  Event(players_id=6,match_id=1,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e99 =  Event(players_id=9,match_id=1,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e100 =  Event(players_id=1,match_id=1,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    # Team2
    e101 =  Event(players_id=2,match_id=1,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e102 =  Event(players_id=10,match_id=1,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e103 =  Event(players_id=7,match_id=1,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e104 =  Event(players_id=4,match_id=1,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 3 v 4
    # Team 3
    e105 =  Event(players_id=5,match_id=2,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e106 = Event(players_id=8,match_id=2,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e107 = Event(players_id=22,match_id=2,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e108 = Event(players_id=21,match_id=2,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 4
    e109 =  Event(players_id=19,match_id=2,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e110 = Event(players_id=14,match_id=2,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e111 = Event(players_id=11,match_id=2,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e112 = Event(players_id=12,match_id=2,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
   
    # Team 5 v 6

    # Team 5
    e113= Event(players_id=13,match_id=3,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e114 = Event(players_id=15,match_id=3,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e115 = Event(players_id=17,match_id=3,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e116 = Event(players_id=20,match_id=3,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    
    # Team 6
    e117 =  Event(players_id=18,match_id=3,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e118 = Event(players_id=16,match_id=3,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e119 = Event(players_id=23,match_id=3,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    e120 = Event(players_id=24,match_id=3,gameweek_id=5,goals_scored=0,goals_conceded=0,assists_provided=0,minutes_played=0,yellow_cards=0,red_cards=0)
    ##############################################################################################################################################
    
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
        e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,
        e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,
        e73,e74,e75,e76,e77,e78,e79,e80,e81,e82,e83,e84,e85,e86,e87,e88,e89,e90,e91,e92,e93,e94,e95,e96,
        e99,e100,e101,e102,e103,e104,e105,e106,e107,e108,e109,e110,e111,e112,e113,e114,e115,e116,e117,e118,e119,e120
        
        # up1,up2,up3,up4
                        ])
  
    db.session.commit()