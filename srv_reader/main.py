from flask import Flask
from api import blueprintApi

app = Flask('API')
app.register_blueprint(blueprintApi)

def main():
    app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
    main()