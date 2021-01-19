import sqlite3
import os

class dbMan():
    databasename = "parkDataBase.db"
    
    def createTables(self):
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res")
        try:
            open(self.databasename)
        except IOError:
            open(self.databasename, "w+")
            conn = sqlite3.connect(self.databasename)
            c = conn.cursor()
            try:
                c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username varchar(100), password varchar(100));")
                c.execute("insert into users (id, username, password) values (0,'admin','" + "1234" + "');")   
                c.execute("CREATE TABLE IF NOT EXISTS patients (dni_patient VARCHAR(9) PRIMARY KEY, sip INTEGER, name VARCHAR(100), surname VARCHAR(100), phone INTEGER, mail VARCHAR(100), height INTEGER, weight INTEGER, date_of_birth INTEGER, gender VARCHAR(2), diagnostic_date INTEGER, park_phase INTEGER, imc INTEGER, medication VARVHAR(1000), user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id_user))")                                    
                c.execute("insert into patients (dni_patients, sip, name, surname, phone, mail, height, weight, date_of_birth, gender, diagnostic_date, park_phase, imc, medication, user_id) values ('10101010F', 10101010, )")
                c.execute("CREATE TABLE IF NOT EXISTS results (id_resul INTEGER PRIMARY KEY, dni_patient VARCHAR(9), resul VARCHAR(100), FOREIGN KEY(dni_patient) REFERENCES patients(dni_patient))")                                       
            except sqlite3.DatabaseError as e:
                print(e) 
            conn.commit()                                
            conn.close()
    
    def createConnection(self):
            try:
                conn = sqlite3.connect(self.databasename)
            except Error as e:
                print(e)
            return conn
            
    '''def createUsersTable(self):
        try:
            open(self.databasename)
        except IOError:
            open(self.databasename, "w+")
            conn = self.createConnection()
            c = conn.cursor()
            try:
                c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username varchar(100), password varchar(100));")
                c.execute("insert into users (id, username, password) values (0,'admin','" + "admin" + "');")   
                c.execute("CREATE TABLE IF NOT EXISTS patients (dni_patient VARCHAR(9) PRIMARY KEY, name VARCHAR(100), user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id_user))")                                    
                c.execute("CREATE TABLE IF NOT EXISTS results (id_resul INTEGER PRIMARY KEY, dni_patient VARCHAR(9), resul VARCHAR(100), FOREIGN KEY(dni_patient) REFERENCES patients(dni_patient))")                                       
            except sqlite3.DatabaseError as e:
                print(e) 
            conn.commit()                                
            conn.close()'''

    '''def verifyUser(self, username, password):
        conn = sqlite3.connect(self.databasename) 
        c = conn.cursor()
        c.execute("select username from users where username = ?", (username))
        data = c.fetchall()
        if not data:
            print ('Incorrect user or password')
        else:
            #NOT implemented
            print ('found')
        conn.commit()
        conn.close()
        return 0'''
        
    def verifyUser(self, username, password):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("select username from users where username='" + username + "';")
        data1 = c.fetchall()
        if not data1:
            self.labelInfo.setText("Wrong username and password")
            return None
        else:
            c.execute("select * from users where username='" + str(username) + "' and password='" + str(password) + "';")
            data2 = c.fetchall()
            if not data2:
                self.labelInfo.setText("Wrong password")
                return None
            else:
                return data2[0]    #User Found
        conn.commit()
        conn.close()
        
    def createUser(self, username, password):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("select username from users where username = '" + username +"'")
        data = c.fetchall()
        if not data:
            #print ('not found')
            c.execute("INSERT INTO users(username, password) VALUES (?,?)", (username, password))
        #else:
            #print ('found')
        conn.commit()
        conn.close()
        
    '''def createPatientTable(self):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        #c.execute("CREATE TABLE IF NOT EXISTS patients (id_patient INTEGER PRIMARY KEY, name VARCHAR(100), user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id_user) ON DELETE CASCASDE ON UPDATE CASCASDE)")   
        c.execute("CREATE TABLE IF NOT EXISTS patients (dni_patient VARCHAR(9) PRIMARY KEY, name VARCHAR(100), user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id_user))")                                    
        conn.close()'''

    def createPatient(self, name, dni, user_id):
        conn = sqlite3.connect(self.databasename)
        if (name == "" or name == None or dni == "" or dni == None):
            return None
        c = conn.cursor()
        c.execute("select dni_patient from patients where dni_patient = '" + dni +"'")
        data = c.fetchall()
        if not data:
            #print ('not found')
            c.execute("INSERT INTO patients(dni_patient, name, user_id) VALUES ('" + dni +"','" + name +"','" + str(user_id) +"')")
        #else:
            #print ('found')
        conn.commit()
        conn.close()
        self.getPatientsList()
        
    '''def createResultsTable(self):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS results (id_resul INTEGER PRIMARY KEY, dni_patient VARCHAR(9), resul VARCHAR(100), FOREIGN KEY(dni_patient) REFERENCES patients(dni_patient))")                                       
        conn.close()'''
        
    def createResult(self, resul, dni):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("INSERT INTO results(dni_patient, resul) VALUES ('" + dni +"', '" + resul +"')")
        conn.commit()
        conn.close()

    def getResultList(self, dni):#
        lst = []
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("SELECT resul from results where dni_patient = '" + dni + "'")
        rows = c.fetchall()
        for r in rows:
            for a in r:
                lst.append(a)
        conn.commit()
        conn.close()
        return lst

    def getPatientsList(self):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("SELECT * FROM patients")
        rows = c.fetchall()
        lst = []
        for row in rows:
            if (row[0] != None and row[1] != None):
                lst.append(row[0] + ":" + row[1])
        #lst = []
        #for pat in c.execute("Select * from patients"):
        #    lst.append(pat)
        conn.commit()
        conn.close()
        return lst
    
    def getPatientInfo(self, dni):
        lst = []
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("SELECT * FROM patients where dni_patient = '" + dni + "'")
        rows = c.fetchall()
        for r in rows:
            for a in r:
                lst.append(a)
        #lst = []
        #for pat in c.execute("Select * from patients"):
        #    lst.append(pat)
        conn.commit()
        conn.close()
        return lst