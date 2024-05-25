from app import create_app

app = create_app()

if __name__ == "__main__": # Start the web browser
    app.run(debug=True)