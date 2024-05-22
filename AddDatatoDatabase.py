import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-system-dee5c-default-rtdb.firebaseio.com/"
})



ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Avhik Biswas",
            "major": "App Dev",
            "starting_year": 2020,
            "total_attendance": 40,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2023-11-11 00:54:34"
        },
    "852741":
        {
            "name": "samir maity ",
            "major": "Full Stack",
            "starting_year": 2021,
            "total_attendance": 55,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2023-12-12 00:54:34"
        },
    "963852":
        {
            "name": "Aritra Bera",
            "major": "MERN Stack",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-01-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)