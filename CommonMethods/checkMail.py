# -*- coding: utf-8 -*-
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from email import parser


def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        # print content_type
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        # 邮件的From, To, Subject存在于根对象上:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    # 需要解码Subject字符串:
                    value = decode_str(value)
                else:
                    # 需要解码Email地址:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        # 如果邮件对象是一个MIMEMultipart,
        # get_payload()返回list，包含所有的子对象:
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            # 递归打印每一个子对象:
            print_info(part, indent + 1)
    else:
        # 邮件对象不是一个MIMEMultipart,
        # 就根据content_type判断:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            # 纯文本或HTML内容:
            content = msg.get_payload(decode=True)
            # 要检测文本编码:
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            # 不是文本,作为附件处理:
            print('%sAttachment: %s' % ('  ' * indent, content_type))


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def contractMail(mailtype, mailname, password):
    server = poplib.POP3('pop.' + str(mailtype) + '.com')
    server.user(mailname)
    server.pass_(password)
    resp, mails, octets = server.list()
    for i in range(1, len(server.list()[1]) + 1):
        resp, lines, octets = server.retr(i)
        msg = Parser().parsestr('\r\n'.join(lines))
        addrfrom = str(msg.get('From'))
        try:
            addrfrom.index('Kingbroker@jzsec.com')
            start_addr = addrfrom.index('<')
            end_addr = addrfrom.index('>')
            subject = decode_str(msg.get('Subject'))
            if(subject == unicode("[经纪宝]九州证券有限公司证券经纪人委托代理合同及相关资料", 'utf-8')):
                return True
            else:
                return False
        except Exception, e:
            print ''
    # 关闭连接:
    server.quit()


def delete_mail(mailtype, mailname, password):
    server = poplib.POP3('pop.' + mailtype + '.com')
    server.user(mailname)
    server.pass_(password)
    resp, mails, octets = server.list()
    for i in range(1, len(server.list()[1]) + 1):
        server.dele(i)
    server.quit()


def contractmailCount(mailtype, mailname, password):
    server = poplib.POP3('pop.' + mailtype + '.com')
    server.user(mailname)
    server.pass_(password)
    resp, mails, octets = server.list()
    count = 0
    for i in range(1, len(server.list()[1]) + 1):
        resp, lines, octets = server.retr(i)
        msg = Parser().parsestr('\r\n'.join(lines))
        addrfrom = str(msg.get('From'))
        try:
            addrfrom.index('Kingbroker@jzsec.com')
            start_addr = addrfrom.index('<')
            end_addr = addrfrom.index('>')
            if(decode_str(msg.get('Subject')) == unicode("[经纪宝]九州证券有限公司证券经纪人委托代理合同及相关资料", 'utf-8')):
                count = count + 1
        except Exception, e:
            print ''
    return count
    # 关闭连接:
    server.quit()

def sacmailCount(mailtype, mailname, password):
    server = poplib.POP3('pop.' + mailtype + '.com')
    server.user(mailname)
    server.pass_(password)
    resp, mails, octets = server.list()
    count = 0
    for i in range(1, len(server.list()[1]) + 1):
        resp, lines, octets = server.retr(i)
        msg = Parser().parsestr('\r\n'.join(lines))
        addrfrom = str(msg.get('From'))
        try:
            addrfrom.index('Kingbroker@jzsec.com')
            start_addr = addrfrom.index('<')
            end_addr = addrfrom.index('>')
            if(decode_str(msg.get('Subject')) == unicode("[经纪宝]执业证书申请教程", 'utf-8')):
                count = count + 1
        except Exception, e:
            print ''
    return count
    # 关闭连接:
    server.quit()

# if __name__ == '__main__':
#     # delete_mail('163', '18001284533@163.com', 'xw009326')
#     contractMail('163', '18001284533@163.com', 'xw009326')
#     print contractmailCount('163', '18001284533@163.com', 'xw009326')
#     print sacmailCount('163', '18001284533@163.com', 'xw009326')
#     print sacmailCount('163', '18001284533@163.com', 'xw009326')
