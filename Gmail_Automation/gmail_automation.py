import smtplib
from termcolor import colored
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def main():
    print(colored("WELCOME to AK automation tool").center(80,'-'),"blue")
    print("---->Press 1 to send mail without attachment ")
    print("---->Press 2 to send mail with attachment ")
    n=int(input("Enter your option"))
    from_mail=input("Enter the sender's mail id : ")
    fname1=input("Enter the path of the reviever's mail text file :")
    recievers=filesy(fname1)
    fname2=input("Write the msg in file and Enter the path of the text file here :")    
    fmsg=open(fname2,"r")
    msg=fmsg.read() 
    fmsg.close()
    sub=input("Enter the Subject of the mail :")
    pas=input("Enter the password of sender,s mail : ")
    if(n==1):
        mailsend1(from_mail,recievers,msg,pas,sub)
    elif(n==2):
        atta=input("Enter the path of attachment with extension : ")
        mailsend1(from_mail,recievers,msg,pas,sub,atta)
    print(colored("WELCOME to AK automation tool").center(80,'-'),"blue")    
        
#https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none        

def filesy(lists):
    with open(lists,"r") as wrdlist:
        for word in wrdlist:
            yield word.rstrip()
        
        
def mailsend1(from_mail,recievers,msg,pas,sub):
    for reci_mail in recievers:
        msga = MIMEMultipart()  
        msga['From'] = from_mail 
        msga['To'] = reci_mail 
        msga['Subject'] = sub
        msga.attach(MIMEText(msg, 'plain')) 
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(from_mail, pas)
        text=msga.as_string()
        s.sendmail(from_mail, reci_mail, text)
        s.quit()        
        

def sendmail2(from_mail,recievers,msg,pas,sub,atta):
    msga = MIMEMultipart()  
    msga['From'] = from_mail 
    msga['Subject'] = sub
    msga.attach(MIMEText(msg, 'plain')) 
    attachment = open(atta, "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % atta) 
    msga.attach(p) 
    for reci_mail in recievers:
        msga['To'] = reci_mail
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(from_mail, pas) 
        text = msga.as_string() 
        s.sendmail(from_mail, reci_mail, text)  
        s.quit() 
    print(colored("WELCOME to AK automation tool").center(80,'-'),'blue')   
        
        
        
if __name__=="__main__":
    main()        