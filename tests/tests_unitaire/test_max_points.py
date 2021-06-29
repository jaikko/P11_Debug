import server


class Test12MaxPointsCompet:

    def setup(self):
        server.clubs = [{
            "name": "Test",
            "email": "test@test.co",
            "points": "13"
        }]

        server.competitions = [{
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "15"
            },
            {
            "name": "Spring",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "14"
        }]

    # nombre de points inférieurs à 12
    def test_correct_number(self, client):
        rv = client.post('/purchasePlaces', data=dict(
            places=3,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200

    # nombre de points supérieur à 12
    def test_incorrect_number(self, client):
        rv = client.post('/purchasePlaces', data=dict(
            places=13,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200
        html = rv.get_data(as_text=True)
        assert '<li>You can&#39;t reserve more than 12 places</li>' in html
