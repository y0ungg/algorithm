from datetime import datetime
from datetime import timedelta
d = datetime.today() + timedelta(hours=9)
print(d.strftime('%Y-%m-%d'))