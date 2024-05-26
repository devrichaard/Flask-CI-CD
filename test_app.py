from main import app

def test_app():
    response = app.test_client().get('/v1/resultados_nba')
    assert response.status_code == 200