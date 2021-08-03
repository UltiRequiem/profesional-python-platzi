from datetime import datetime
import pytz

bogota_date = datetime.now(pytz.timezone("America/Bogota"))

print(bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))
