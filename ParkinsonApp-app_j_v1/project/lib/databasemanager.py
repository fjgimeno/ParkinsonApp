import sqlite3

class dbMan():
    databasename = "parkDataBase.db"
    def createConnection(self):
            try:
                conn = sqlite3.connect(self.databasename)
            except Error as e:
                print(e)
            return conn
            
    def createUsersTable(self):
        try:
            open(self.databasename)
            print("YEH que lhe obert")
        except IOError:
            open(self.databasename, "w+")
            conn = self.createConnection()
            c = conn.cursor()
            try:
                c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username varchar(100), password varchar(100));")
                c.execute("insert into users (id, username, password) values (0,'admin','" + str(hash("admin")) + "');")   
            except sqlite3.DatabaseError as e:
                print(e) 
            conn.commit()                                
            conn.close()

    def verifyUser(self, username, password):
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
        
    def createPatientTable(self):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        #c.execute("CREATE TABLE IF NOT EXISTS patients (id_patient INTEGER PRIMARY KEY, name VARCHAR(100), user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id_user) ON DELETE CASCASDE ON UPDATE CASCASDE)")   
        c.execute("CREATE TABLE IF NOT EXISTS patients (dni_patient VARCHAR(9) PRIMARY KEY, name VARCHAR(100), user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id_user))")                                    
        conn.close()

    def createPatient(self, name, dni, user_id):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("select dni_patient from patients where dni_patient = '" + dni +"'")
        data = c.fetchall()
        if not data:
            #print ('not found')
            c.execute("INSERT INTO patients(dni_patient, name, user_id) VALUES ('" + dni +"','" + name +"','" + user_id +"')")
        #else:
            #print ('found')
        conn.commit()
        conn.close()
        
    def createResultsTable(self):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS results (id_resul INTEGER PRIMARY KEY, dni_patient VARCHAR(9), resul VARCHAR(100), FOREIGN KEY(dni_patient) REFERENCES patients(dni_patient))")                                       
        conn.close()
        
    def createResult(self, resul, dni):
        conn = sqlite3.connect(self.databasename)
        c = conn.cursor()
        c.execute("INSERT INTO results(dni_patient, resul) VALUES ('" + dni +"', '" + resul +"')")
        conn.commit()
        conn.close()