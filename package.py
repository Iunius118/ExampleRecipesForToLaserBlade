import datetime
import shutil

base_file_name = 'ExampleRecipesForToLaserBlade-v4-'

date = datetime.date.today().strftime("%Y%m%d")
zip_name = 'out/' + base_file_name + date
shutil.make_archive(zip_name, 'zip', root_dir='src')
