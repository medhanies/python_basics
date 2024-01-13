import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'localhost'
database = 'University'
username = 'sa'
password = '#095417Boy'  
cnxn = pyodbc.connect('DRIVER={/opt/homebrew/lib/libmsodbcsql.18.dylib};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# tcp:myserver.database.windows.net

# print(pyodbc.drivers())