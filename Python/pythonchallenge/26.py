"""

import email, smtplib
apology = email.Message.Message()
apology.add_header('To', 'leopold.moz@pythonchallenge.com')
apology.add_header('From', "your email address")
apology.add_header('Subject', 'Apology')
apology.set_payload('Sorry!')
print apology.as_string()
server = smtplib.SMTP('localhost')
server.sendmail(apology['from'], apology['to'], apology.as_string())

server.quit()
"""
