import server


class TestBookingPastCompet:

    # modification du contenu des variables
    def setup(self):
        server.competitions = [{
                "name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "15"
                },
                {
                "name": "Spring",
                "date": "2022-03-27 10:00:00",
                "numberOfPlaces": "12"
            }]

        server.clubs = [{
                "name": "Test",
                "email": "test@test.co",
                "points": "14"
            }]

    # tester une url correcte
    def test_correct_route(self, client):

        rv = client.get('/book/Spring/Test')
        assert rv.status_code == 200

    # tester une url fausse
    def test_incorrect_route(self, client):

        rv = client.get('/book/Spring/Tests')
        assert rv.status_code == 500
