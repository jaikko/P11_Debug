import server


class TestDisplayPointsClubs:

    # modification du contenu des variables
    def setup(self):
        server.clubs = [{
                "name": "Test",
                "email": "test@test.co",
                "points": "4"
            }]

    # page existe
    def test_correct_route(self, client):

        rv = client.get('/list')
        assert rv.status_code == 200

    # page non existante
    def test_incorrect_route(self, client):

        rv = client.get('/lists')
        assert rv.status_code == 404
