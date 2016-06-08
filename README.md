# smtplib-sample

## How to use

```
>cd path\to\dir

path\to\dir>git clone https://github.com/thinkAmi-sandbox/smtplib-sample.git

path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

(env) >python gmail_sender.py
finished: sendmail_with_ehlo_using_smtp
finished: sendmail_without_ehlo_using_smtp
finished: sendmail_using_smtp_ssl
finished: send_message_using_smtp_ssl
```

　    
## Tested Envrionment

- Windows10 x64
- Python 3.5.1 32bit

　  
## Related Blog (Written in Japanese)

[Python3.5 + smtplib.SMTP_SSL.send_message()で、Gmailからメールを送信する - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/06/09/062528)