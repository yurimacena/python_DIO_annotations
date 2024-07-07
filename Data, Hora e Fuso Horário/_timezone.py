from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2), "OSLO"))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3), "SÃO PAULO"))

print(data_oslo)
print(data_sao_paulo)