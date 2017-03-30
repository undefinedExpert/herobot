from urllib import parse
from datetime import datetime, timezone



ip_data = 'a%3A1%3A%7Bs%3A7%3A%221.2.3.4%22%3Bs%3A19%3A%222017-03-29T22%3A37%3A46%22%3B%7D'
# ip_data = 'a%3A1%3A%7Bs11%3A%2213.45.26.66%22%3Bs19%3A%222017-03-29T23%3A39%3A05%22%3B%7D'

decoded = parse.unquote_plus(ip_data)

ips = decoded.split('s:')
print(ips)

ip_old = ips[1]
ip_new = '%d:"%s";' % (len('13.45.26.66'), '13.45.26.66')


ips[1] = ip_new

ip_date_old = ips[2]
# czas serwerowy = -2h
time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
ip_date_new = '%d:"%s";}' % (len(time), str(time))

ips[2] = ip_date_new

modified_cookie = 's'.join(ips)

print(modified_cookie)
print(decoded)

encoded = parse.quote_plus(modified_cookie, encoding='utf-8').replace('%25', '%')

print(encoded)

print(encoded == ip_data)

final = 'a%3A1%3A%7Bs11%3A%2213.45.26.66%22%3Bs2017-03-29T23%3A15%3A59'