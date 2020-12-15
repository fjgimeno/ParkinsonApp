import databasemanager

dbman = databasemanager.dbMan()

dbman.createUsersTable()
dbman.createUser("TEST","1234")
dbman.createPatientTable()
dbman.createPatient("TESTPATIENT", "20202020E", "0")
dbman.createResultsTable()
dbman.createResult("0000:0000:0000", "20202020E")