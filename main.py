from discord_dashboard import create_app

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5008, ssl_context=('ssl/server.csr', 'ssl/server.key'))
    app.run(debug=True, host='0.0.0.0', port=5008)
