from locust import HttpUser, task, between

class ReqresUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_user(self):
        self.client.get("/api/users/2")
