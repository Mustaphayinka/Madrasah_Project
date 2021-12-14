from application import app


if __name__ =='__main__':
    app.secret_key = 'secretkey'
    app.run(debug = True)
