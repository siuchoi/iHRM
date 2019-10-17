from Test_iHRM.app import sampleURL


class AdminLogin:
    def post_login(self, session, mobile, password):
        # data = {
        #     "mobile": "13800000002", "password": "123456"
        # }
        return session.post(sampleURL + "login", json={"mobile": mobile, "password": password})

    def post_add_one(self, session):
        data = {
            "username": "tom",
            "mobile": "13012340001",
            "timeOfEntry": "2019-07-01",
            "formOfEmployment": 1,
            "workNumber": "1322131",
            "departmentName": "开发部",
            "departmentId": "1066240656856453120",
            "correctionTime": "2019-11-30"
        }
        myHeader = {"Authorization": "Bearer " + tv}
        return session.post(sampleURL + "/api/sys/user", json=data, header=myHeader)

    def put_alter_one(self):
        pass

    def get_query_one(self):
        pass

    def delete_remove_one(self):
        pass
