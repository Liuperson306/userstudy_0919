import streamlit as st
import poplib
from email.parser import BytesParser
from email.policy import default
import os

def download_txt_attachment_pop3(myemail, password, dataset, save_path='./'):
    try:
        # POP3 服务器地址和端口
        pop3_server = 'pop.126.com'
        subject_to_search = f'{dataset}'  # 以 {dataset} 开头的邮件主题

        # 连接到 POP3 服务器
        mail_server = poplib.POP3_SSL(pop3_server, 995)
        mail_server.user(myemail)
        mail_server.pass_(password)

        # 获取邮件数量
        num_messages = len(mail_server.list()[1])

        for i in range(num_messages, 0, -1):  # 从最新的邮件开始遍历
            # 获取邮件的原始内容
            raw_email = b'\n'.join(mail_server.retr(i)[1])
            
            # 解析邮件
            email_message = BytesParser(policy=default).parsebytes(raw_email)

            subject = email_message['Subject']
            if subject and subject.startswith(subject_to_search):  # 检查邮件主题
                print(f'找到符合条件的邮件：{subject}')

                # 遍历邮件的各个部分，查找附件
                for part in email_message.walk():
                    # 处理 .txt 类型的附件
                    if part.get_content_type() == 'text/plain' and part.get_filename() and part.get_filename().endswith('.txt'):
                        filename = part.get_filename()
                        filepath = os.path.join(save_path, filename)

                        # 将附件保存到本地
                        with open(filepath, 'wb') as f:
                            f.write(part.get_payload(decode=True))
                        print(f'附件 {filename} 已下载到 {filepath}')
                        break  # 下载第一个符合条件的附件后跳出循环

        # 关闭与邮件服务器的连接
        mail_server.quit()

    except Exception as e:
        print(f'发生错误: {str(e)}')

# 使用示例
myemail = st.secrets["my_email"]["email"]  
password =  st.secrets["my_email"]["password"]

dataset = "BIWI"
download_txt_attachment_pop3(myemail, password, dataset, save_path='./attachments/')
