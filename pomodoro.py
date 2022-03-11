from app import create_app
# from app.models import Pitch, User


app = create_app('development')
app.run(debug=True)

# from app import create_app

# if __name__ == "__main__":
#     app = create_app('development')
#     app.run(debug=True)



