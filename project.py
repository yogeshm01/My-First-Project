import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",password="yogesh@01",database="airport")

cur=con.cursor()

cur.execute("insert into flights values ('AA001','Vistara','Lko','Chennai','2023-11-12','10:00','2023-11-13','2:00','16','Boeing 777')")
cur.execute("insert into flights values ('6E123','IndiGo','Lko','Mng.','2023-11-12','6:00','2023-11-12','14:00','8','Airbus A321')")
cur.execute("insert into flights values ('SG107','SpiceJet','Lko','Delhi','2023-11-12','8:00','2023-11-13','12:00','4','Boeing 737')")
cur.execute("insert into flights values ('6E138','IndiGo','Lko','TRV','2023-11-12','22:00','2023-11-13','15:00','17','Airbus A320')")
cur.execute("insert into flights values ('AA002','Vistara','Lko','Gaya','2023-11-12','4:00','2023-11-12','9:00','5','Embraer E-Jet')")
cur.execute("insert into flights values ('6E127','IndiGo','Lko','BOM','2023-11-12','16:00','2023-11-12','21:00','5','Airbus A320')")
cur.execute("insert into flights values ('SG101','SpiceJet','Lko','Jaipur','2023-11-12','11:00','2023-11-13','17:00','6','Boeing 737')")
cur.execute("insert into flights values ('6E139','IndiGo','Lko','Surat','2023-11-12','12:00','2023-11-13','1:00','13','Airbus A320')")
cur.execute("insert into flights values ('SG107','SpiceJet','Lko','Cochin','2023-11-12','20:00','2023-11-13','17:00','21','Bombardier Q400')")

cur.execute("insert into Passenger values ('ABC123','Rajesh Kumar','Vistara','10:00','2:00','Lko','Chennai')")
cur.execute("insert into Passenger values ('CDG124', 'Pooja Mishra','Vistara','10:00','2:00','Lko','Chennai')")
cur.execute("insert into Passenger values ('XWY234', 'Sandeep Singh','Vistara','4:00','9:00','Lko','Gaya')")
cur.execute("insert into Passenger values ('UDJ346', 'Neha Sharma','Vistara','10:00','2:00','Lko','Chennai')")
cur.execute("insert into Passenger values ('BFE463', 'Rahul Jaiswal','Vistara','4:00','9:00','Lko','Gaya')")
cur.execute("insert into Passenger values ('AHD432', 'David Paul','IndiGo','6:00','14:00','Lko','Mangalore')")
cur.execute("insert into Passenger values ('GHS364', 'Sanjiv Pandey','IndiGo','16:00','21:00','Lko','BOM')")
cur.execute("insert into Passenger values ('IFK632', 'Riya Singh','IndiGo','16:00','21:00','Lko','BOM')")
cur.execute("insert into Passenger values ('PEO890', 'Yashika Shukla','IndiGo','6:00','14:00','Lko','Mangalore')")
cur.execute("insert into Passenger values ('RYE345', 'Shreya Sharma','IndiGo','16:00','21:00','Lko','BOM')")
cur.execute("insert into Passenger values ('URD348', 'Yash Sen','IndiGo','22:00','15:00','Lko','TRV')")
cur.execute("insert into Passenger values ('YUD349', 'Anushka Pathak','IndiGo','22:00','15:00','Lko','TRV')")
cur.execute("insert into Passenger values ('ISF352', 'Kartik Mishra','SpiceJet','11:00','17:00','Lko','Jaipur')")
cur.execute("insert into Passenger values ('PSW245', 'Pragya Pal','SpiceJet','11:00','17:00','Lko','Jaipur')")
cur.execute("insert into Passenger values ('YDH234','Srishti Singh','SpiceJet', '8:00','12:00','Lko','Delhi')")
cur.execute("insert into Passenger values ('LED399', 'Amit Shukla','SpiceJet','8:00','12:00','Lko','Delhi')")
cur.execute("insert into Passenger values ('WQA999', 'Muskan Sharma','SpiceJet','20:00','17:00','Lko','Cochin')")
cur.execute("insert into Passenger values ('MDS872', 'Ananya Rai','SpiceJet','20:00','17:00','Lko','Cochin')")


con.commit()


def format_timedelta(td):
    # Convert a timedelta to hours and minutes (HH:MM)
    minutes, _ = divmod(td.total_seconds(), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02d}:{int(minutes):02d}"

def details():
    
    p=input("Enter PNR of the Passenger:")
    cur.execute(f"select * from passenger where pnr='{p}'")
    r=cur.fetchall()
    if r:
        for row in r:
            
            pnr, name, airline, departure_time, arrival_time, source, destination = row
            
            # Convert time values to a more readable format
            departure_time_str = str(departure_time)
            arrival_time_str = str(arrival_time)
            
            a=f"PNR: {pnr}"
            b=f"Name: {name}"
            c=f"Airline: {airline}"
            d=f"Departure Time: {departure_time_str}"
            e=f"Arrival Time: {arrival_time_str}"
            f=f"Source: {source}"
            g=f"Destination: {destination}"
        l=[a,b,c,d,e,f,g]
        print(l)
    
    else:
        print("No records found for the provided PNR.")
        

    d = input("Enter departure time: ")
    cur.execute(f"SELECT * FROM flights WHERE dept_time = '{d}'")
    rs = cur.fetchall()
    
    if rs:
        for i in rs:
            fno, airline, dept_apt, dest_apt, dept_date, arvl_date, dept_time, arvl_time, duration, aircraft_type=i
            dept_time_str=str(dept_time)
            arvl_time_str=str(arvl_time)
            a=f"FNO: {fno}"
            b=f"Airline: {airline}"
            c=f"DEPT_APT: {dept_apt}"
            d=f"DEST_APT: {dest_apt}"
            e=f"DEPT_DATE:{dept_date}"
            f=f"ARVL_DATE:{arvl_date}"
            g=f"DEPT_TIME:{dept_time_str}"
            h=f"ARVL_TIME:{arvl_time_str}"
            i=f"duration:{duration}"
            j=f"aircraft_type:{aircraft_type}"
        l=[a,b,c,d,e,f,g,h,i,j]
        print(l)
        
    else:
        print("No flights found for the provided departure time.")

def alldetails():
    cur.execute(f"select * from passenger ")
    r=cur.fetchall()
    for row in r:
        
        pnr, name, airline, departure_time, arrival_time, source, destination = row
        
        # Convert time values to a more readable format
        departure_time_str = str(departure_time)
        arrival_time_str = str(arrival_time)
        
        a=f"PNR: {pnr}"
        b=f"Name: {name}"
        c=f"Airline: {airline}"
        d=f"Departure Time: {departure_time_str}"
        e=f"Arrival Time: {arrival_time_str}"
        f=f"Source: {source}"
        g=f"Destination: {destination}"
        l=[a,b,c,d,e,f,g]
        print(l)

def update():
    p=input("enter pnr of a passenger to update records:")
    print("which detail you want to update? \n 1. PNAME \n 2. Airline \n 3. Departure Time \n 4. Arrival Time\n 5. Departure Airport \n 6. Destination Airport ")
    ch= int(input("enter choice (1/2/3/4/5/6):"))
    
    
            
    if ch==1:
        z=input("enter New Name of Passenger:")
        cur.execute(f"update passenger set PName='{z}' where pnr='{p}'")
        y=cur.execute(f"select * from passenger where pname='{z}'")
        r=cur.fetchall()
        if r:
            for i in r:
                pnr, name, airline, departure_time, arrival_time, source, destination = i
                departure_time_str = str(departure_time)
                arrival_time_str = str(arrival_time)
                
                a=f"PNR: {pnr}"
                b=f"Name: {name}"
                c=f"Airline: {airline}"
                d=f"Departure Time: {departure_time_str}"
                e=f"Arrival Time: {arrival_time_str}"
                f=f"Source: {source}"
                g=f"Destination: {destination}"
            l=[a,b,c,d,e,f,g]
            print(l)
                
        else:
            print("No flights found for the provided PNR.")
            
    if ch==2:
        x=input("enter New Airline Name:")
        cur.execute(f"update passenger set Airline='{x}' where pnr='{p}'")
        y=cur.execute(f"select * from passenger where Airline='{x}'")
        r=cur.fetchall()
        if r:
            for i in r:
                pnr, name, airline, departure_time, arrival_time, source, destination = i
                departure_time_str = str(departure_time)
                arrival_time_str = str(arrival_time)
                
                a=f"PNR: {pnr}"
                b=f"Name: {name}"
                c=f"Airline: {airline}"
                d=f"Departure Time: {departure_time_str}"
                e=f"Arrival Time: {arrival_time_str}"
                f=f"Source: {source}"
                g=f"Destination: {destination}"
            l=[a,b,c,d,e,f,g]
            print(l)
                
        else:
            print("No flights found for the provided PNR.")
            
    if ch==3:
        x=input("enter New Departure Time")
        cur.execute(f"update passenger set Dept_Time='{x}' where pnr='{p}'")
        y=cur.execute(f"select * from passenger where pnr='{p}'")
        r=cur.fetchall()
        if r:
            for i in r:
                pnr, name, airline, departure_time, arrival_time, source, destination = i
                departure_time_str = str(departure_time)
                arrival_time_str = str(arrival_time)
                
                a=f"PNR: {pnr}"
                b=f"Name: {name}"
                c=f"Airline: {airline}"
                d=f"Departure Time: {departure_time_str}"
                e=f"Arrival Time: {arrival_time_str}"
                f=f"Source: {source}"
                g=f"Destination: {destination}"
            l=[a,b,c,d,e,f,g]
            print(l)
        else:
            print("No flights found for the provided PNR.")
            
    if ch==4:
        x=input("enter New Arrival Time:")
        cur.execute(f"update passenger set Arvl_Time='{x}' where pnr='{p}'")
        y=cur.execute(f"select * from passenger where pnr='{p}'")
        r=cur.fetchall()
        if r:
            for i in r:
                pnr, name, airline, departure_time, arrival_time, source, destination = i
                departure_time_str = str(departure_time)
                arrival_time_str = str(arrival_time)
                
                a=f"PNR: {pnr}"
                b=f"Name: {name}"
                c=f"Airline: {airline}"
                d=f"Departure Time: {departure_time_str}"
                e=f"Arrival Time: {arrival_time_str}"
                f=f"Source: {source}"
                g=f"Destination: {destination}"
            l=[a,b,c,d,e,f,g]
            print(l)
              
        else:
            print("No flights found for the provided PNR.")
            
    if ch==5:
        x=input("Enter New Departure Airport:")
        cur.execute(f"update passenger set Dept_Apt='{x}' where pnr='{p}'")
        y=cur.execute(f"select * from passenger where pnr='{p}'")
        r=cur.fetchall()
        if r:
            for i in r:
                pnr, name, airline, departure_time, arrival_time, source, destination = i
                departure_time_str = str(departure_time)
                arrival_time_str = str(arrival_time)
                
                a=f"PNR: {pnr}"
                b=f"Name: {name}"
                c=f"Airline: {airline}"
                d=f"Departure Time: {departure_time_str}"
                e=f"Arrival Time: {arrival_time_str}"
                f=f"Source: {source}"
                g=f"Destination: {destination}"
            l=[a,b,c,d,e,f,g]
            print(l)
                
        else:
            print("No flights found for the provided PNR.")
            
    if ch==6:
        x=input("Enter New Destination Airport:")
        cur.execute(f"update passenger set Dest_Apt='{x}' where pnr='{p}'")
        y=cur.execute(f"select * from passenger where pnr='{p}'")
        r=cur.fetchall()
        if r:
            for i in r:
                pnr, name, airline, departure_time, arrival_time, source, destination = i
                departure_time_str = str(departure_time)
                arrival_time_str = str(arrival_time)
                
                a=f"PNR: {pnr}"
                b=f"Name: {name}"
                c=f"Airline: {airline}" 
                d=f"Departure Time: {departure_time_str}"
                e=f"Arrival Time: {arrival_time_str}"
                f=f"Source: {source}"
                g=f"Destination: {destination}"
            l=[a,b,c,d,e,f,g]
            print(l)
                
        else:
            print("No flights found for the provided PNR.")
        
        
'''    
def cancel():
    p=input("enter PNR to Cancel the Flight:")
    cur.execute(f"delete from passenger where pnr='{p}'")
    r=cur.fetchall()
    if r:
        print("flight cancelled")
    else:
        print("passenger not found")
'''

def cancel():
    p = input("Enter PNR to Cancel the Flight: ")
    cur.execute(f"DELETE FROM passenger WHERE pnr = '{p}'")
    

    if cur.rowcount > 0:
        print("Flight canceled")
    else:
        print("Passenger not found")

def checkin():
    x = input("Enter PNR of passenger to Check-in")
    cur.execute(f"SELECT * FROM flights f, passenger p WHERE f.Dept_time = p.Dept_time AND PNR = '{x}'")
    r = cur.fetchall()

    if r:
        for row in r:
            print("Passenger record:")
            for i, column_value in enumerate(row):
                print(f"{cur.description[i][0]:<15}: {column_value}")
    else:
        print("Passenger not found.")

def add():
    a=input("Enter PNR of Passenger:")
    b=input("Enter Name of the Passenger:")
    c=input("Enter Name of Airline:")
    d=input("Enter Departure Time:")
    e=input("Enter Arrival Time:")
    f=input("Enter Departure Airport:")
    g=input("Enter Destination Airport:")
    cur.execute("insert into passenger value ('{}','{}','{}','{}','{}','{}','{}')". format (a,b,c,d,e,f,g))
    print("records inserted succesfully")

    
def charge():
    x=int(input("enter weight of lugguage(in kg):"))
    if x>10:
        c=(x-10)*100
        print("extra charge of lugguage is:",'₹',c)
    else:
        print("no extra charge")
'''
while True:
    print('*****Chaudhary Charan Singh International Airport*****')
    print("1. Show details of a Passenger.")
    print("2. Show Details of all Passengers.")
    print("3. Update Records of a Passenger. ")
    print("4. Cancel the flight.")
    print("5. Check-in.")
    print("6. Add records of a New Passenger. ")
    print("7. Extra Luggage Charge. ")
    
    ch=int(input("Enter your choice(1,2,3,4,5,6,7):"))
    if ch==1:
        details()
    if ch==2:
        alldetails()
    if ch==3:
        update()
    if ch==4:
        cancel()
    if ch==5:
        checkin()
    if ch==6:
        add()
    if ch==7:
        charge()
    else:
        print("enter correct choice...")
'''

while True:
    print('*****Chaudhary Charan Singh International Airport*****')
    print("1. Show details of a Passenger.")
    print("2. Show Details of all Passengers.")
    print("3. Update Records of a Passenger. ")
    print("4. Cancel the flight.")
    print("5. Check-in.")
    print("6. Add records of a New Passenger. ")
    print("7. Extra Luggage Charge. ")
    
    ch = int(input("Enter your choice(1,2,3,4,5,6,7):"))
    
    if ch == 1:
        details()
    elif ch == 2:
        alldetails()
    elif ch == 3:
        update()
    elif ch == 4:
        cancel()
    elif ch == 5:
        checkin()
    elif ch == 6:
        add()
    elif ch == 7:
        charge()
    else:
        print("Enter correct choice...")



