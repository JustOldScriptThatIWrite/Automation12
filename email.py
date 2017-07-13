#! /usr/bin/python
# -*- coding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

class sendEmail(object):
    def getData(self,user,Titl):

        strTo = [user + '@mail.co.il', 's@mail.co.il']
        strFrom = 's@ubi.co.il'
        # Create the root message and fill in the from, to, and subject headers
        self.msgRoot = MIMEMultipart('related')
        self.msgRoot['Subject'] = 'דיווח מתא"מ - ' + Titl
        self.msgRoot['From'] = strFrom
        self.msgRoot['To'] = ", ".join(strTo)
        self.msgRoot.preamble = 'This is a multi-part message in MIME format.'

    def sendFunction(self,sn):

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        self.msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        # We reference the image in the IMG SRC attribute by the ID we give it below

        msgText = MIMEText(
            " <HTML><HEAD><META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; \"/><TABLE ALIGN=\"CENTER\"  DIR=\"rtl\" BORDER=\"0\" WIDTH=\"100%\"\"><TR><TD ALIGN=\"right\"><img src=\"cid:image1\" alt=\"Igud\"></TD></TR></TABLE></HEAD><BODY><H1><CENTER style=\"direction:rtl\">" + Titl + "</CENTER></H1><div id=\"desc\" style=\"float:right;direction:rtl;font-size:20px;\">" + desc + "<b><u></u></b></div><TABLE ALIGN=\"CENTER\" DIR=\"ltr\" BORDER=\"1\" WIDTH=\"50%\">" + RowData + "</TABLE></BODY></HTML> ",
            'html', 'utf-8')

        msgAlternative.attach(msgText)

        # This example assumes the image is in the current directory
        fp = open('/tmp/Scripts/Images/AppVacation/Logo.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        self.msgRoot.attach(msgImage)
        EmailServer = '1.1.1.1'
        try:
            s = smtplib.SMTP(EmailServer)
            s.sendmail(self.strFrom, self.strTo, self.msgRoot.as_string())
            s.quit()
            from time import gmtime, strftime

            file = open('/tmp/EmailLog.txt', 'a')
            file.write('Email of '+sn+' has Sent ------- time:   ' + strftime("%d-%m-%Y   %H:%M:%S", gmtime()) + '\n')
            file.close()
        except smtplib.SMTPException:
            from time import gmtime, strftime

            file = open('/tmp/EmailLog.txt', 'a')
            file.write('Email of '+sn+' does\'nt sent  ------- time:   ' + strftime("%d-%m-%Y   %H:%M:%S",gmtime()) + '\n')
            file.close()