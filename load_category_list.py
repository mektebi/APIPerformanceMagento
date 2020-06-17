from locust import HttpLocust ,TaskSet ,task
import json
import requests
import urllib3


urllib3.disable_warnings()

class UserBehaviour(TaskSet) :

    def on_start(self) :
        self.access_token = 'uulbfv3bozwp0wbvyax39o0348elq21f'

    @task(1)
    def get_categories(self):
        response = self.client.get('/rest/V1/categories',  headers={'Authorization': 'Bearer {}'.format(self.access_token)})
        print(response.content)



class User(HttpLocust) :
    task_set = UserBehaviour
    min_wait = 30000
    max_wait = 70000
    host = 'https://m2.leanscale.com'