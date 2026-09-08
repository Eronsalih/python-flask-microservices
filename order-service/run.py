# run.py
from application import create_app, db
from flask_migrate import Migrate
from application import models

app = create_app()
migrate = Migrate(app, db)

@app.route('/health')
def health():
    return 'OK', 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
