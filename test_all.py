#!/usr/bin/python3
"""test all relationships and creation of each class"""

import models
from models.county import County
from models.town import Town
from models.user import User
from models.business import Business
from models.video import Video
from models.image import Image
from models.category import Category
from models import storage

# cratetion of a county
county = County(name="Tran_Nzoia")
county.save()

# cratetion of a town
town = Town(county_id=county.id, name="Kitale")
town.save()

# creation of a user
user = User(email="njoro@gmail.com", password="cansttell", county_id=county.id, town_id=town.id)
user.save()

# creation of a category
category = Category(name="food")
category.save()

# creation of a business
business = Business(name="Dairy", user_id=user.id, county_id=county.id, category_id=category.id, description="testingonly", exact_location="testsstreet")
business.save()

# creatinon od a video
video = Video(business_id=business.id, url="https://example.com/sample.mp4", description="myhotel")
video.save()

# image
image = Image(business_id=business.id, url="https://example.com/sample.jpg", description="avaikable")
image.save()

storage.save()
print("OK")
