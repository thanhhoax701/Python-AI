import smtplib
import config

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

password = config.my_pass
server.login("hoab1908387@student.ctu.edu.vn", password)

msg = f"""\
Subject: 2023
Xin chao cac ban!
"""

server.sendmail("hoab1908387@student.ctu.edu.vn", "tth1610.vl@gmail.com", msg)

server.quit()
