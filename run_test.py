import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

#获取该文件路径
def get_path():
    proDir = os.path.split(os.path.realpath(__file__))[0]
    return proDir
#运行脚本
def run_test(testcase=[],*devices):
    devices_list = list(devices)
    print(testcase)
    print(devices_list)
    for dev in devices_list:
        for case in testcase:
            base_path = get_path()
            test_case = os.path.join(base_path,case)
            report_path = os.path.join(base_path,'report')
            report_name = case.split('.')[0]
            outfile = os.path.join(report_path,report_name) + '.html'
            implement_case = 'airtest run ' + test_case + ' --device Android:///'+ dev + ' --log ' + report_path
            implement_report = 'airtest report ' + test_case + ' --log_root ' + report_path + ' --outfile ' + outfile
            print(implement_case)
            print(implement_report)
            os.system(implement_case)
            os.system(implement_report)
#获取测试报告文件
def get_report_file():
    base_path = get_path()
    report_list = []
    report_path = os.path.join(base_path,'report')
    dir_list = os.listdir(report_path)
    file_suffix = '.html'
    for index in dir_list:
        if file_suffix in index:
            report_list.append(os.path.join(report_path,index))
    return report_list


#发送邮件
def send_email():
    report_list = get_report_file()
    mail_host = 'smtp.hostuc.com'
    sender = 'wentao.chen@iris-technologies.com.cn'
    receivers = 'zhiyi.you@iris-technologies.com.cn'
    username = 'wentao.chen@iris-technologies.com.cn'
    password = 'iris123'
    mail_port = 25
    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("APP自动化测试组", 'utf-8')
    message['To'] =  Header("各位同事及领导", 'utf-8')
    message['Subject'] = Header('APP自动化测试报告', 'utf-8')
    #邮件正文
    message.attach(MIMEText("""Hi all:\n \t 利星行APP自动化测试结果详情见附件。""", 'plain', 'utf-8'))
    #构造附件
    for report_file in report_list:
        file_name = report_file.split('\\')[-1]
        with open(report_file,'rb') as f:
            att = MIMEText(f.read(), 'html','utf-8')
            att["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att["Content-Disposition"] = 'attachment; filename=%s' %file_name
            message.attach(att)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, int(mail_port))    # 25 为 SMTP 端口号
        smtpObj.login(username,password)
        smtpObj.sendmail(sender,receivers, message.as_string())
        print(u"邮件发送成功")
        f.close()
    except smtplib.SMTPException as e:
        print(u"Error: 无法发送邮件",e)


#主函数
if __name__ == "__main__":

    #print(get_path())
    testcase = ['test_lsh_login.air']
    run_test(testcase,"JTJ4C15C15014538")
    send_email()

