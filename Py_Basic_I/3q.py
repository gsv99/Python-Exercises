from datetime import datetime
import pytz

SaoPauloTz = pytz.timezone("America/Sao_Paulo") 
timeInSaoPaulo = datetime.now(SaoPauloTz)
currentTimeInSaoPaulo = timeInSaoPaulo.strftime("%d de %B de %Y às %H:%M:%S")

print(f"The current date/time in São Paulo is: {currentTimeInSaoPaulo}")