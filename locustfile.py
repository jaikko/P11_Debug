from locust import HttpUser, task, between


class Locust(HttpUser):
  
    wait_time = between(1, 2.5)
    
    def on_start(self):
        
        self.client.get('/')
        self.client.post('/showSummary', data = dict(
            email = "john@simplylift.co"
        ))

    @task
    def booking(self):
        self.client.get("/book/Spring Festival/Simply Lift")
    
    @task
    def booking_places(self):
        self.client.post("/purchasePlaces", data = dict(
            places=1,
            competition="Spring Festival",
            club = "Simply Lift"
        ))
