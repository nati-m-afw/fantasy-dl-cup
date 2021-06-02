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

    dept1 = Dept(id=1,dName='IT')
    dept2 = Dept(id=2,dName='Mech')
    dept3 = Dept(id=3,dName='Elec')
    dept4 = Dept(id=4,dName='SE')
    dept5 = Dept(id=5,dName='Chemical')
    dept6 = Dept(id=6,dName='BioMed')

    # Dep't 1
    p1 = Players(id=1,fname="Manu", lname="GK", position="goalkeeper", dept_id=1)
    p3 = Players(id=3,fname="Lola", lname="DF", position="defender", dept_id=1)
    p6 = Players(id=6,fname="Ni", lname="MD", position="midfielder", dept_id=1)
    p9 = Players(id=9,fname="Dude", lname="ST", position="striker", dept_id=1)
    
    # Dep't 2
    p2 = Players(id=2,fname="Fanny", lname="Gk", position="goalkeeper", dept_id=2)
    p4 = Players(id=4,fname="Abe", lname="DF", position="defender", dept_id=2)
    p7 = Players(id=7,fname="Chang", lname="MD", position="midfielder", dept_id=2)
    p10 = Players(id=10,fname="Sportsguy", lname="ST", position="striker", dept_id=2)
            
    # Dep't 3   
    p22 = Players(id=22,fname="FannyAsGk", lname="Gk", position="goalkeeper", dept_id=3)     
    p5 = Players(id=5,fname="Dube", lname="DF", position="defender", dept_id=3)
    p21 = Players(id=21,fname="Dube's Bro", lname="MD",position="midfielder",dept_id=3)
    p8 = Players(id=8,fname="Meh", lname="ST", position="striker", dept_id=3)

    # Dep't 4
    p12 = Players(id=12,fname="Ranjit", lname="GK", position="goalkeeper", dept_id=4)
    p14 = Players(id=14,fname="Dud", lname="DF", position="defender", dept_id=4)
    p11 = Players(id=11,fname="Sportsguys'sBrother", lname="MD", position="midfielder", dept_id=4)
    p19 = Players(id=19,fname="Pla", lname="ST", position="striker", dept_id=4)
    
    
    # Dep't 5
    p13 = Players(id=13,fname="Kumal", lname="GK", position="goalkeeper", dept_id=5)
    p15 = Players(id=15,fname="Kman", lname="DF", position="defender", dept_id=5)
    p17 = Players(id=17,fname="Jman", lname="MD", position="midfielder", dept_id=5)
    p20 = Players(id=20,fname="Finally", lname="ST", position="striker", dept_id=5)
        
       
    # Dep't 6 
    p23 = Players(id=23,fname="KumalAsDept", lname="GK", position="goalkeeper", dept_id=6)
    p16 = Players(id=16,fname="Malik", lname="DF", position="defender", dept_id=6)
    p18 = Players(id=18,fname="Q", lname="MD", position="midfielder", dept_id=6)
    p24 = Players(id=24,fname="FinallyNO", lname="ST", position="striker", dept_id=6)



    # u1 = Users(fname="Swift",lname="Books",teamname="satellites")
    # u2 = Users(fname="Dean",lname="Smith",teamname="this_team")
    # u3 = Users(fname="Users3",lname="third",teamname="rope")


    # up1 = userPlayers(user_id=1,players_id=4)
    # up2 = userPlayers(user_id=1,players_id=5)
    # up3 = userPlayers(user_id=1,players_id=6)
    # up4 = userPlayers(user_id=1,players_id=7)
  


    # up5 = userPlayers(user_id=2,players_id=4,status="active")
    # up6 = userPlayers(user_id=2,players_id=5, status="active")
    # up7 = userPlayers(user_id=2,players_id=6, status="active")
    # up8 = userPlayers(user_id=3,players_id=7, status="active")
    # up9 = userPlayers(user_id=3,players_id=8, status="active")

    #Gameweeks
    gw1 =Gameweek(id=1,status='ALL_UPCOMING')
    gw2 =Gameweek(id=2,status='ALL_UPCOMING')
    gw3 =Gameweek(id=3,status='ALL_UPCOMING')
    gw4 =Gameweek(id=4,status='ALL_UPCOMING')
    gw5 =Gameweek(id=5,status='ALL_UPCOMING')




     # GW1
    m1 =Match(id=1,team=1,opponent=2,game_week=1,time="16:00",date="2021-03-03",state=0,score="")
    m2 =Match(id=2,team=3,opponent=4,game_week=1,time="16:00",date="2021-03-03",state=0,score="")
    m3 =Match(id=3,team=5,opponent=6,game_week=1,time="16:00",date="2021-03-03",state=0,score="")
    
     # GW2
    m4 =Match(id=4,team=6,opponent=1,game_week=2,time="16:00",date="2021-04-04",state=0,score="")
    m5 =Match(id=5,team=2,opponent=3,game_week=2,time="16:00",date="2021-04-04",state=0,score="")
    m6 =Match(id=6,team=5,opponent=4,game_week=2,time="16:00",date="2021-04-04",state=0,score="")
    
     # GW3
    m7 =Match(id=7,team=5,opponent=1,game_week=3,time="16:00",date="2021-08-04",state=0,score="")
    m8 =Match(id=8,team=5,opponent=3,game_week=3,time="16:00",date="2021-08-04",state=0,score="")
    m9 =Match(id=9,team=6,opponent=4,game_week=3,time="16:00",date="2021-08-04",state=0,score="")
    
    # GW4
    m10 =Match(id=10,team=1,opponent=4,game_week=4,time="16:00",date="2021-12-04",state=0,score="")
    m11 =Match(id=11,team=5,opponent=2,game_week=4,time="16:00",date="2021-12-04",state=0,score="")
    m12 =Match(id=12,team=6,opponent=3,game_week=4,time="16:00",date="2021-12-04",state=0,score="")


    # Match Event stats
    # GW1
    
    # Team 1 vs 2
    #Team 1
    e1 =  Event(id=1,players_id=3,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0) 
    e2 =  Event(id=2,players_id=6,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)
    e3 =  Event(id=3,players_id=9,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=0,minutes_played=90,yellow_cards=1,red_cards=0)
    e4 =  Event(id=4,players_id=1,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=60,yellow_cards=0,red_cards=1)
    # Team 2
    e5 =  Event(id=5,players_id=2,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=90,yellow_cards=1,red_cards=0)
    e6 =  Event(id=6,players_id=10,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=80,yellow_cards=0,red_cards=0)
    e7 =  Event(id=7,players_id=7,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=60,yellow_cards=0,red_cards=0)
    e8 =  Event(id=8,players_id=4,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    
    # Team 3 v 4
    
    # Team 3
    e9 =  Event(id=9,players_id=5,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e10 = Event(id=10,players_id=8,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=80,yellow_cards=1,red_cards=0)
    e11 = Event(id=11,players_id=22,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e12 = Event(id=12,players_id=21,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)
    
    # Team 4
    e13 =  Event(id=13,players_id=19,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e14 = Event(id=14,players_id=14,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=80,yellow_cards=1,red_cards=0)
    e15 = Event(id=15,players_id=11,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e16 = Event(id=16,players_id=12,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)
   
    # Team 5 v 6
    
    # Team 5
    e17 = Event(id=17,players_id=13,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e18 = Event(id=18,players_id=15,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=80,yellow_cards=1,red_cards=0)
    e19 = Event(id=19,players_id=17,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e20 = Event(id=20,players_id=20,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)
    
    # Team 6
    e21 =  Event(id=21,players_id=18,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e22 = Event(id=22,players_id=16,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=80,yellow_cards=1,red_cards=0)
    e23 = Event(id=23,players_id=23,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e24 = Event(id=24,players_id=24,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)
    

    db.session.add_all([
        # Add Departments
        dept1, dept2, dept3, dept4, dept5, dept6,
        # Add Players
        p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,p21,p22,p23,p24,
        # Add Matches
        m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,
        # Add Gamweeks
        gw1,gw2,gw3,gw3,gw4,gw5,
        # Add events
        e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24
        # ,e13,e14,e15,e16,e17,e18,e18,e19,e20
        # Add User Players
                        # ,u1,u2,u3,up5,up6,up7,up8,up9
                        ])
  
    db.session.commit()