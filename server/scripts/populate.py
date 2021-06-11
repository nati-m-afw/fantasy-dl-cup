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
    
    
    p1 = Players(fname="Manu", lname="GK", position="goalkeeper", dept_id=1)
    p3 = Players(fname="Lola", lname="DF", position="defender", dept_id=1)
    p6 = Players(fname="Ni", lname="MD", position="midfielder", dept_id=1)
    p9 = Players(fname="Dude", lname="ST", position="striker", dept_id=1)
    
    # Dep't 2
    p2 = Players(fname="Fanny", lname="Gk", position="goalkeeper", dept_id=2)
    p4 = Players(fname="Abe", lname="DF", position="defender", dept_id=2)
    p7 = Players(fname="Chang", lname="MD", position="midfielder", dept_id=2)
    p10 = Players(fname="Sportsguy", lname="ST", position="striker", dept_id=2)
            
    # Dep't 3   
    p22 = Players(fname="FannyAsGk", lname="Gk", position="goalkeeper", dept_id=3)     
    p5 = Players(fname="Dube", lname="DF", position="defender", dept_id=3)
    p21 = Players(fname="Dube's Bro", lname="MD",position="midfielder",dept_id=3)
    p8 = Players(fname="Meh", lname="ST", position="striker", dept_id=3)

    # Dep't 4
    p12 = Players(fname="Ranjit", lname="GK", position="goalkeeper", dept_id=4)
    p14 = Players(fname="Dud", lname="DF", position="defender", dept_id=4)
    p11 = Players(fname="Sportsguys'sBrother", lname="MD", position="midfielder", dept_id=4)
    p19 = Players(fname="Pla", lname="ST", position="striker", dept_id=4)
    
    
    # Dep't 5
    p13 = Players(fname="Kumal", lname="GK", position="goalkeeper", dept_id=5)
    p15 = Players(fname="Kman", lname="DF", position="defender", dept_id=5)
    p17 = Players(fname="Jman", lname="MD", position="midfielder", dept_id=5)
    p20 = Players(fname="Finally", lname="ST", position="striker", dept_id=5)
        
       
    # Dep't 6 
    p23 = Players(fname="KumalAsDept", lname="GK", position="goalkeeper", dept_id=6)
    p16 = Players(fname="Malik", lname="DF", position="defender", dept_id=6)
    p18 = Players(fname="Q", lname="MD", position="midfielder", dept_id=6)
    p24 = Players(fname="FinallyNO", lname="ST", position="striker", dept_id=6)



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
    gw1 =Gameweek(status='ACTIVE')
    gw2 =Gameweek(status='ALL_UPCOMING')
    gw3 =Gameweek(status='ALL_UPCOMING')
    gw4 =Gameweek(status='ALL_UPCOMING')
    gw5 =Gameweek(status='ALL_UPCOMING')




     # GW1
    m1 =Match(team=1,opponent=2,game_week=1,time="16:00",date="2021-03-03",state=1,score="2v1")
    m2 =Match(team=3,opponent=4,game_week=1,time="16:00",date="2021-03-03",state=1,score="3v0")
    m3 =Match(team=5,opponent=6,game_week=1,time="16:00",date="2021-03-03",state=1,score="4v1")
    
     # GW2
    m4 =Match(team=6,opponent=1,game_week=2,time="16:00",date="2021-04-04",state=1,score="1v3")
    m5 =Match(team=2,opponent=3,game_week=2,time="16:00",date="2021-04-04",state=1,score="1v1")
    m6 =Match(team=5,opponent=4,game_week=2,time="16:00",date="2021-04-04",state=1,score="2v2")
    
     # GW3
    m7 =Match(team=4,opponent=1,game_week=3,time="16:00",date="2021-08-04",state=1,score="0v3")
    m8 =Match(team=5,opponent=3,game_week=3,time="16:00",date="2021-08-04",state=1,score="3v1")
    m9 =Match(team=6,opponent=2,game_week=3,time="16:00",date="2021-08-04",state=1,score="2v2")
    
    # GW4
    m10 =Match(team=2,opponent=4,game_week=4,time="16:00",date="2021-12-04",state=1,score="2v0")
    m11 =Match(team=5,opponent=1,game_week=4,time="16:00",date="2021-12-04",state=1,score="1v1")
    m12 =Match(team=6,opponent=3,game_week=4,time="16:00",date="2021-12-04",state=1,score="1v1")


    # Match Event stats
    # GW1
    
    # Team 1 vs 2
    #Team 1
    e1 =  Event(players_id=3,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0) 
    e2 =  Event(players_id=6,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)
    e3 =  Event(players_id=9,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=0,minutes_played=90,yellow_cards=1,red_cards=0)
    e4 =  Event(players_id=1,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=60,yellow_cards=0,red_cards=1)
    # Team 2
    e5 =  Event(players_id=2,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=90,yellow_cards=1,red_cards=0)
    e6 =  Event(players_id=10,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=80,yellow_cards=0,red_cards=0)
    e7 =  Event(players_id=7,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=60,yellow_cards=0,red_cards=0)
    e8 =  Event(players_id=4,match_id=1,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    
    # Team 3 v 4
    
    # Team 3
    e9 =  Event(players_id=5,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e10 = Event(players_id=8,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=80,yellow_cards=1,red_cards=0)
    e11 = Event(players_id=22,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e12 = Event(players_id=21,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)
    
    # Team 4
    e13 =  Event(players_id=19,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e14 = Event(players_id=14,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=80,yellow_cards=1,red_cards=0)
    e15 = Event(players_id=11,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e16 = Event(players_id=12,match_id=2,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)
   
    # Team 5 v 6
    
    # Team 5
    e17 = Event(players_id=13,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e18 = Event(players_id=15,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=80,yellow_cards=1,red_cards=0)
    e19 = Event(players_id=17,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e20 = Event(players_id=20,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)
    
    # Team 6
    e21 =  Event(players_id=18,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=0,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e22 = Event(players_id=16,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=2,assists_provided=0,minutes_played=80,yellow_cards=1,red_cards=0)
    e23 = Event(players_id=23,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=1,minutes_played=90,yellow_cards=1,red_cards=0)
    e24 = Event(players_id=24,match_id=3,gameweek_id=1,goals_scored=1,goals_conceded=3,assists_provided=0,minutes_played=90,yellow_cards=0,red_cards=0)


    db.session.add_all([
        # Add Departments
        dept1, dept2, dept3, dept4, dept5, dept6
        # Add Players
        ,p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,p21,p22,p23,p24
        # Add Matches
        ,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12
        # Add Gamweeks
        ,gw1,gw2,gw3,gw3,gw4,gw5
        # Add events
        ,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,
        
        # up1,up2,up3,up4
                        ])
  
    db.session.commit()