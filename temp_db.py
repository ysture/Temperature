
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime


cred = credentials.Certificate("./firebase_adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

temp = 25.3
sensor_id = '3m'
time_stamp = datetime.now()

doc_ref = db.collection(u'temperatures').document()
doc_ref.set({
    u'sensor-id':u'{}'.format(sensor_id),
    u'temperature': u'{}'.format(temp),
    u'timestamp': u'{}'.format(time_stamp.strftime("%Y-%m-%d %H:%M"))
})

'''
import pyrebase

config = {     
  "apiKey": "AIzaSyDAc9vXb263-UxC8WKkiggpmfWB5k3qLHw",
  "authDomain": "temperature-1d377.firebaseapp.com",
  "databaseURL": "temperature-1d377.appspot.com",
  "storageBucket": "https://temperature-1d377.firebaseio.com/temp%203m/8EIWbxJtYwm0srJzpewu"
}

firebase = pyrebase.initialize_app(config)
'''