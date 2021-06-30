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
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "12"
            }]

        server.clubs = [{
                "name": "Test",
                "email": "test@test.co",
                "points": "14"
            }]

    # bloquer réservation d'une compétition expirée
    def test_booking(self, client):

        rv = client.get('/book/Spring/Test')
        assert rv.status_code == 200
        html = rv.get_data(as_text=True)
        assert '<li>Competition expired</li>' in html
