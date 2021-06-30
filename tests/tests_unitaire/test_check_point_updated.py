import server


class TestPointsClubsUpdated:

    # modification du contenu des variables
    def setup(self):
        server.competitions = [{
                "name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "15"
                },
                {
                "name": "Spring",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "12"
            }]

        server.clubs = [{
                "name": "Test",
                "email": "test@test.co",
                "points": "14"
            }]

    def test_correct_route(self, client):
        rv = client.post('/purchasePlaces', data=dict(
            places=4,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200

    def test_incorrect_route(self, client):
        rv = client.post('/purchasePlace', data=dict(
            places=4,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 404