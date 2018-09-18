from app.api import create_app
from app.core.log import logger


app = create_app()


if __name__ == '__main__':
    app.run()
