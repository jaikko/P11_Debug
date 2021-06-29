import server
import pytest


class TestPointsClubs:

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
                "points": "4"
            }]

    # nombre de points suffisants

    def test_correct_number(self, client):

        rv = client.post('/purchasePlaces', data=dict(
            places=3,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200

    # nombre de points insuffisants
    def test_incorrect_number(self, client):

        rv = client.post('/purchasePlaces', data=dict(
            places=5,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200
        html = rv.get_data(as_text=True)
        assert '<li>You don&#39;t have enougth point or the number entered is greater than the number of places remaining</li>' in html
