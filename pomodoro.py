from app import create_app


app = create_app('development')
app.run(debug=True)

# from app import create_app

# if __name__ == "__main__":
#     app = create_app('development')
#     app.run(debug=True)



