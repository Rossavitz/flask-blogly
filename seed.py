from models import User, db
from app import app

db.drop_all()
db.create_all()

User.query.delete()

ross = User(
    first_name="Ross",
    last_name="Cummings",
    image_url="https://people.com/thmb/QYvd4bDjMXZbm6XacFf73RxEW4E=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(729x88:731x90):format(webp)/10-Year-Old-Boy-Starts-Petition-to-Change-Nerd-Glasses-Emoji-112923-bec304032f7a45e2aa4957e003755126.jpg",
)

john = User(
    first_name="Michael",
    last_name="Jordan",
    image_url="https://cdn.nba.com/headshots/nba/latest/1040x760/893.png",
)
jeannine = User(first_name="Jeannine", last_name="Vestuto")

db.session.add(ross)
db.session.add(john)
db.session.add(jeannine)

db.session.commit()
