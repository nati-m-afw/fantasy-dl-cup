from main import db, Players, Dept, Users, userPlayers,Match

def populate():
    userPlayers.query.delete()
    Players.query.delete()
    Dept.query.delete()
    Users.query.delete()
    Match.query.delete()

    dept1 = Dept(id=1,dName='IT')
    dept2 = Dept(id=2,dName='Mech')
    dept3 = Dept(id=3,dName='Elec')
    dept4 = Dept(id=4,dName='SE')
    dept5 = Dept(id=5,dName='Chemical')
    dept6 = Dept(id=6,dName='BioMed')

    p1 = Players(fname="Manu", lname="GK", position="goalkeeper", dept_id=1)
    p2 = Players(fname="Fanny", lname="Gk", position="goalkeeper", dept_id=2)
    p3 = Players(fname="Lola", lname="DF", position="defender", dept_id=1)
    p4 = Players(fname="Abe", lname="DF", position="defender", dept_id=2)
    p5 = Players(fname="Dube", lname="DF", position="defender", dept_id=3)
    p6 = Players(fname="Ni", lname="MD", position="midfielder", dept_id=1)
    p7 = Players(fname="Chang", lname="MD", position="midfielder", dept_id=2)
    p8 = Players(fname="Meh", lname="MD", position="striker", dept_id=3)
    p9 = Players(fname="Dude", lname="ST", position="striker", dept_id=1)
    p10 = Players(fname="Sportsguy", lname="ST", position="striker", dept_id=2)
    p11 = Players(fname="Sportsguys'sBrother", lname="MD", position="midfielder", dept_id=4)
    p12 = Players(fname="Ranjit", lname="GK", position="goalkeeper", dept_id=4)
    p13 = Players(fname="Kumal", lname="GK", position="goalkeeper", dept_id=5)
    p14 = Players(fname="Dud", lname="DF", position="defender", dept_id=4)
    p15 = Players(fname="Kman", lname="DF", position="defender", dept_id=5)
    p16 = Players(fname="Malik", lname="DF", position="defender", dept_id=6)
    p17 = Players(fname="Jman", lname="MD", position="midfielder", dept_id=5)
    p18 = Players(fname="Q", lname="MD", position="midfielder", dept_id=6)
    p19 = Players(fname="Pla", lname="ST", position="striker", dept_id=4)
    p20 = Players(fname="Finally", lname="ST", position="striker", dept_id=5)

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



     # GW1
    m1 =Match(team=1,opponent=2,game_week=1,time="16:00",date="2021-23-03",state=0,score="")
    m2 =Match(team=3,opponent=4,game_week=1,time="16:00",date="2021-23-03",state=0,score="")
    m3 =Match(team=5,opponent=6,game_week=1,time="16:00",date="2021-23-03",state=0,score="")
    
     # GW2
    m4 =Match(team=6,opponent=1,game_week=2,time="16:00",date="2021-04-04",state=0,score="")
    m5 =Match(team=2,opponent=3,game_week=2,time="16:00",date="2021-04-04",state=0,score="")
    m6 =Match(team=5,opponent=4,game_week=2,time="16:00",date="2021-04-04",state=0,score="")
    
     # GW3
    m7 =Match(team=5,opponent=1,game_week=3,time="16:00",date="2021-08-04",state=0,score="")
    m8 =Match(team=5,opponent=3,game_week=3,time="16:00",date="2021-08-04",state=0,score="")
    m9 =Match(team=6,opponent=4,game_week=3,time="16:00",date="2021-08-04",state=0,score="")
    
    # GW4
    m10 =Match(team=1,opponent=4,game_week=4,time="16:00",date="2021-12-04",state=0,score="")
    m11 =Match(team=5,opponent=2,game_week=4,time="16:00",date="2021-12-04",state=0,score="")
    m12 =Match(team=6,opponent=3,game_week=4,time="16:00",date="2021-12-04",state=0,score="")




    db.session.add_all([
        dept1, dept2, dept3, dept4, dept5, dept6,
                         p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,
                        m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12
                        # ,u1,u2,u3,up5,up6,up7,up8,up9
                        ])
    # up1,up2,up3,up4,up5,up6,up7,up8,up9
    db.session.commit()