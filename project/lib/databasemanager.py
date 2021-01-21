
import sqlite3
import os

class dbMan():
    databasename = "parkDataBase.db"
    databaseAbsolute = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res/db/" + databasename
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res/db")
    
    def createTables(self):
        try:
            open(self.databaseAbsolute)
        except IOError:
            open(self.databaseAbsolute, "w+")
            conn = self.createConnection()
            c = conn.cursor()
            try:
                c.execute("CREATE TABLE results (id_resul INTEGER PRIMARY KEY, dni_patient VARCHAR(9), resul VARCHAR(100), comment TEXT, FOREIGN KEY(dni_patient) REFERENCES patients(dni_patient))")
                c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username varchar(100), password varchar(100));")
                c.execute("insert into users (id, username, password) values (0,'admin','" + "1234" + "');")   
                c.execute("CREATE TABLE patients (dni_patient VARCHAR(9) PRIMARY KEY, sip INTEGER, name VARCHAR(100), surname VARCHAR(100), phone INTEGER, mail VARCHAR(100), height INTEGER, weight INTEGER, date_of_birth INTEGER, gender VARCHAR(2), diagnostic_date INTEGER, park_phase INTEGER, imc INTEGER, medication VARVHAR(1000), face_path VARVHAR(1000),body_path VARVHAR(1000),user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id_user));")                       
            except sqlite3.DatabaseError as e:
                print(e) 
            conn.commit()                                
            conn.close()
    
    def createConnection(self):
            try:
                conn = sqlite3.connect(self.databaseAbsolute)
            except Error as e:
                print(e)
            return conn
        
    def verifyUser(self, username, password):
        conn = self.createConnection()
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
        conn =  self.createConnection()
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

    def createPatient(self, name, dni, user_id, sip, surname, birth, diagnostic, medication, phone, mail, height, weight, gender, phase, imc, face_path, body_path):
        conn =  self.createConnection()
        if (name == "" or name == None or dni == "" or dni == None or sip == "" or sip == None):
            return None
        c = conn.cursor()
        c.execute("select dni_patient from patients where dni_patient = '" + dni +"'")
        data = c.fetchall()
        if not data:
            print ('not found')
            c.execute("INSERT INTO patients(dni_patient, sip, name, surname, phone, mail, height, weight, date_of_birth, gender, diagnostic_date, park_phase, imc, medication,face_path, body_path, user_id) VALUES ('" + dni +"','" + sip +"','" + name +"','" + surname +"','" + phone +"','" + mail +"','" + height +"','" + weight +"','" + birth +"','" + gender +"','" + diagnostic +"','" + phase +"','" + imc +"','" + medication +"','" + face_path +"','" + body_path +"','"+str(user_id)+"')")
        #else:
            #print ('found')
        conn.commit()
        conn.close()
        self.getPatientsList()
        
    def createResult(self, result, dni, comment):
        conn =  self.createConnection()
        c = conn.cursor()
        c.execute("INSERT INTO results(dni_patient, resul, comment) VALUES ('" + dni +"', '" + str(result) +"', '" + comment + "')")
        conn.commit()
        conn.close()

    def getResultList(self, dni):
        lst = []
        conn =  self.createConnection()
        c = conn.cursor()
        #c.execute("SELECT resul from results where dni_patient = '" + dni + "'")
        c.execute("SELECT * from results;")
        rows = c.fetchall()
        borrResult = ""
        for r in rows:
            for a in r:
                borrResult = borrResult + str(a) + ";"
            lst.append(borrResult)
            borrResult = ""
        conn.commit()
        conn.close()
        return lst

    def getPatientsList(self):
        conn =  self.createConnection()
        c = conn.cursor()
        c.execute("SELECT * FROM patients")
        rows = c.fetchall()
        lst = []
        pacient = ""
        for row in rows:
            for e in row:
                pacient= pacient+(str(e) + ":")
            lst.append(pacient)
            pacient = ""
        conn.commit()
        conn.close()
        return lst
    
    def getPatientInfo(self, dni):
        lst = []
        conn =  self.createConnection()
        c = conn.cursor()
        c.execute("SELECT * FROM patients where dni_patient = '" + dni + "'")
        rows = c.fetchall()
        for r in rows:
            for a in r:
                lst.append(a)
        conn.commit()
        conn.close()
        return lst
    
    def alterTablePatients(self,name, dni, surname, birth, diagnostic, medication, phone, mail, height, weight, gender, phase, imc, face_path, body_path):
        conn = self.createConnection()
        c = conn.cursor()
        c.execute("UPDATE patients SET name = '" + name + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET surname = '" + surname + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET phone = '" + phone + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET mail = '" + mail + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET height = '" + height + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET weight = '" + weight + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET date_of_birth = '" + birth + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET gender = '" + gender + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET diagnostic_date = '" + diagnostic + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET park_phase = '" + phase + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET imc = '" + imc + "' WHERE dni_patient = '" + dni + "'")
        c.execute("UPDATE patients SET medication = '" + medication + "' WHERE dni_patient = '" + dni + "'")
        if (face_path != ""):
            c.execute("UPDATE patients SET face_path = '" + face_path + "' WHERE dni_patient = '" + dni + "'")
        if (body_path != ""):
            c.execute("UPDATE patients SET body_path = '" + body_path + "' WHERE dni_patient = '" + dni + "'")
        conn.commit()
        conn.close()
        return True