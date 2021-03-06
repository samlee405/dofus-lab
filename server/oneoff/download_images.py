import os
import re
import requests
import shutil
from app import db
from app.database.model_item import ModelItem
from app.database.model_spell import ModelSpell

app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folder = os.path.join(app_root, "static", "images", "spells")

# image_urls = db.session.query(ModelItem.image_url).all()
image_urls = db.session.query(ModelSpell.image_url).all()

for num, (image_url,) in enumerate(image_urls, start=1):
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        print("downloaded", num, "/", len(image_urls))
        filename = re.search("\d+\.png", image_url)[0]
        path = os.path.join(folder, filename)
        with open(path, "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            print("wrote to", path)
