import datetime
import shutil

baseFileName = 'ExampleRecipesForToLaserBlade-v4-'

date = datetime.date.today().strftime("%Y%m%d")
zipname = 'out/' + baseFileName + date
shutil.make_archive(zipname, 'zip', root_dir='src')
