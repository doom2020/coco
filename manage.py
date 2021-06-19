"""
程序入口文件
"""
from flaskapp.settings import DEBUG_MODE, SERVER_IP, SERVER_PORT
from flaskapp import create_app


if __name__ == "__main__":
    app = create_app(DEBUG_MODE)
    app.run(host=SERVER_IP, port=SERVER_PORT, debug=DEBUG_MODE)
   