import server


class TestLogin:

    # modification du contenu des varaiables
    def setup(self):
        server.competitions = [
                {
                    "name": "Spring Festival",
                    "date": "2020-03-27 10:00:00",
                    "numberOfPlaces": "5"
                },
                {
                    "name": "Fall Classic",
                    "date": "2020-10-22 13:30:00",
                    "numberOfPlaces": "3"
                }
            ]

        server.clubs = [
            {
                "name": "Test",
                "email": "test@test.co",
                "points": "13"
            }]

    # vérifier connexion avec email invalide
    def test_incorrect_login(self, client):

        rv = client.post('/showSummary', data=dict(
            email="to@trt.fr"))
        assert rv.status_code == 200
        html = rv.get_data(as_text=True)
        assert "<li>Sorry, that email wasn&#39;t found</li>" in html

    # vérifier connexion avec email valide
    def test_correct_login(self, client):

        rv = client.post('/showSummary', data=dict(
            email="test@test.co"))
        assert rv.status_code == 200