
class Oracle(DBInterface):
   def connect(self):
       print('Connecting to Oracle Database...')
   def disconnect(self):
       print('Disconnecting to Oracle Database...')

class Sybase(DBInterface):
   def connect(self):
       print('Connecting to Sybase Database...')
   def disconnect(self):
       print('Disconnecting to Sybase Database...')

dbname=input('Enter Database Name either Oracle or Sybase:')
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()