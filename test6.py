import datetime


now = datetime.datetime.now()
delta = datetime.timedelta(hours=72, minutes=50, seconds=20)
print(now + delta)

delta2 = [int(x) for x in "72 50 20".split()]
print(delta2)

mnt_correction, sc = divmod(now.second + delta2[2], 60)
hr_correction, mnt = divmod(now.minute + delta2[1] + mnt_correction, 60)
d_correction, hr = divmod(now.hour + delta2[0] + hr_correction, 24)
d = (now.day + d_correction) % 30

print(now.year, now.month, d, hr, mnt, sc)