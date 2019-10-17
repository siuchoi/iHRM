from Test_iHRM import app
from Test_iHRM.app import Token


class Employee:
    def add(self, session, username, mobile, workNumber):
        data = {
            "username": username,
            "mobile": mobile,
            "workNumber": workNumber
        }
        return session.post(app.sampleURL + "user", json=data, headers={"Authorization": "Bearer " + app.Token})

    def update(self, session, username):
        return session.put(app.sampleURL + "user/" + app.ID, json={"username": username},
                           headers={"Authorization": "Bearer " + app.Token})

    def get(self, session):
        return session.get(app.sampleURL + "user/" + app.ID, headers={"Authorization": "Bearer " + app.Token})

    def delete(self, session):
        return session.delete(app.sampleURL + "user/" + app.ID, headers={"Authorization": "Bearer " + app.Token})
