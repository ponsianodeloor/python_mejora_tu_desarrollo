import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Contenido de mi correo')

msg['Subject'] = 'Asunto del correo'
msg['From']='ponsianodeloor@gmail.com'
msg['To']='ponsianodeloor@outlook.com'

mail_server = smtplib.SMTP('smtp.gmail.com', 587)
mail_server.ehlo()
mail_server.starttls()
mail_server.ehlo()
mail_server.login('ponsianodeloor@gmail.com', 'cfkczxbkryybyysf')
mail_server.sendmail('ponsianodeloor@gmail.com', 'ponsianodeloor@outlook.com', msg.as_string())
mail_server.close()