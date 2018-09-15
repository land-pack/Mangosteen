from app.api import create_app
from app.core.log import logger


app = create_app()
app.config['APPLICATION_ROOT'] = '/api/v1/'


if __name__ == '__main__':
    app.run()
