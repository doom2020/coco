"""
程序入口文件
"""
from flaskapp.settings import DEBUG_MODE
from flaskapp import create_app


if __name__ == "__main__":
    app = create_app(DEBUG_MODE)
    app.run(host='0.0.0.0', port=5000, debug=DEBUG_MODE)
   