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

    def test_booking(self, client):
        rv = client.post('/purchasePlaces', data=dict(
            places=4,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200
        html = rv.get_data(as_text=True)
        assert '<h2>Welcome, test@test.co </h2>' in html
        assert 'Points available: 10' in html
        assert '<li>Great-booking complete!</li>' in html
