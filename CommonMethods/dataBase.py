# -*- coding: utf-8 -*-
__author__ = 'xuwen'


from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.orm import sessionmaker, mapper
from decimal import *
import relatedTime
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
import sys
import globalData, Data
from pyexcel_xls import XLBook
import random



def db_session():
    db_config = {
        'host': '10.10.13.39',
        'port':3306,
        'user': 'crm',
        'passwd': 'crm@2015',
        'db':'crm',
        'charset':'utf8'
        }
    engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=%s'%(db_config['user'],
                                                                        db_config['passwd'],
                                                                        db_config['host'],
                                                                        db_config['port'],
                                                                        db_config['db'],
                                                                        db_config['charset']), echo=True)
    DB_Session = sessionmaker(bind=engine)
    session = DB_Session()
    return session

# def db_session():
#     db_config = {
#         'host': '10.10.87.38',
#         'port':3306,
#         'user': 'crm',
#         'passwd': 'crm@2015',
#         'db':'crm',
#         'charset':'utf8'
#         }
#     engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=%s'%(db_config['user'],
#                                                                         db_config['passwd'],
#                                                                         db_config['host'],
#                                                                         db_config['port'],
#                                                                         db_config['db'],
#                                                                         db_config['charset']), echo=True)
#     DB_Session = sessionmaker(bind=engine)
#     session = DB_Session()
#     return session


def db_operate_log(phone):
    db_config = {
        'host': '10.10.13.39',
        'port':3306,
        'user': 'crm',
        'passwd': 'crm@2015',
        'db':'crm',
        'charset':'utf8'
        }
    engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=%s'%(db_config['user'],
                                                                        db_config['passwd'],
                                                                        db_config['host'],
                                                                        db_config['port'],
                                                                        db_config['db'],
                                                                        db_config['charset']), echo=True)
    session = db_session()
    metadata = MetaData(engine)
    # operateTable = metadata.tables('b_operate_his')
    b_operate_his = Table(
        'b_operate_his',metadata,
        Column('id', BIGINT(20), primary_key=True),
        Column('bid',CHAR(32), unique=True),
        Column('operate_by', SMALLINT(8)),
        Column('relation_id', CHAR(64), unique=True),
        Column('operate_type', SMALLINT(8)),
        Column('reason', TEXT, unique=True, nullable=True),
        Column('create_time', TIMESTAMP),
        Column('update_time', TIMESTAMP)
    )
    class b_operate_log(object):
        pass
    mapper(b_operate_log, b_operate_his)
    return b_operate_log()

# 扫描培训题库
def scan_question():
    session = db_session()
    for i in session.execute("select * from sys_question").fetchall():
        if(i.answer.encode("utf-8").count("\n") + 1 == 2):
            answer_a = i.answer.encode("utf-8").split("\n")[0]
            answer_b = i.answer.encode("utf-8").split("\n")[1]
            if(answer_a[0:1] != "A"):
                print "题号 " + str(i.id) + " 的A选项有误"
            if(answer_b[0:1] != "B"):
                print "题号 " + str(i.id) + " 的B选项有误"
            if(i.correct_answer != 1 and i.correct_answer != 2):
                print "题号" + str(i.id) + "的正确答案设定有误!"
        elif(i.answer.encode("utf-8").count("\n") + 1 == 4):
            answer_a = i.answer.encode("utf-8").split("\n")[0]
            answer_b = i.answer.encode("utf-8").split("\n")[1]
            answer_c = i.answer.encode("utf-8").split("\n")[2]
            answer_d = i.answer.encode("utf-8").split("\n")[3]
            if(answer_a[0:1] != "A"):
                print "题号 " + str(i.id) + " 的A选项有误"
            if(answer_b[0:1] != "B"):
                print "题号 " + str(i.id) + " 的B选项有误"
            if(answer_c[0:1] != "C"):
                print "题号 " + str(i.id) + " 的C选项有误"
            if(answer_d[0:1] != "D"):
                print "题号 " + str(i.id) + " 的D选项有误"
            if(i.correct_answer != 1 and i.correct_answer != 2 and i.correct_answer != 3 and i.correct_answer != 4):
                print "题号 " + str(i.id) + " 的正确答案设定有误!"
        else:
            print "题号 " + str(i.id) + " 的答案列表有误!"
    print "题库扫描完成!!!"
    session.close()


#删除Bapp用户
def del_buser(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    session.execute("delete from b_call_history where phone = " + str(phone))
    session.commit()
    session.execute("delete from b_chapter_history where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_customer where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_customer_blacklist where phone = " + str(phone))
    session.commit()
    cid = session.execute("select * from b_customer where bid = \'" + bid + "\'").fetchall()
    for i in cid:
        session.execute("delete from b_customer_extend where cid = \'" + i.cid + "\'")
        session.commit()
        session.execute("delete from b_sms_history where cid = \'" + i.cid + "\'")
        session.commit()
    session.execute("delete from b_customer_grab_record where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_express where user_id = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_feebonus_log where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_follow_done where id = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_follow_todo where id = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_kpi where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_kpi_change where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_level_two_feebonus_log where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_message where id = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_monthly_feebonus_log where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_operate_his where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_paymoney where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_play where id = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_play_stock where id = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_play_stock_log where id = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_question_history where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_train_history where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_admission_ticket where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_ad_sac_exam where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_certificate where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_certificate_express where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_contract where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_contract_express where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_exit where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_play where id = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_play_invite where id = \'" + bid + "\'")
    session.commit()
    session.execute("delete from b_user_sac_exam where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from sys_share_relation where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from sys_share_relation where mobilephone = \'" + str(phone) + "\'")
    session.commit()
    session.execute("delete from trade_brokerage where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_commission where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_commission_bal where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_continuous_commission where recommand_bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_continuous_commission_bal where recommand_bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_logasset where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_month_clear where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_recommand_award where recommand_person = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_recommand_award_bal where recommand_person = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_security_guard where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from trade_user where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from wechat_payment where bid = \'" + bid + "\'")
    session.commit()
    session.execute("delete from wechat_user where bid = \'" + bid + "\'")
    session.commit()
    session.close()


#上传身份证审核通过
def approve_id(phone):
    b_operate_record = db_operate_log(phone)
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    b_operate_record.bid = bid
    b_operate_record.operate_by = 10
    b_operate_record.relation_id = ''
    b_operate_record.operate_type = 10
    b_operate_record.reason = "身份信息及从业资格审核通过。"
    b_operate_record.create_time = relatedTime.currenttime()
    b_operate_record.update_time = relatedTime.currenttime()
    session.add(b_operate_record)
    session.execute("update b_user SET id_audit_status = 2 WHERE  mobilephone = " + str(phone))
    session.execute("update b_user SET train_status = 0 WHERE  mobilephone = " + str(phone))
    session.commit()
    session.close()


#修改培训时间
def train_time_start(phone):
    session = db_session()
    bid = session.execute("select * from b_user where mobilephone = \'" + str(phone) + "\'").first().bid
    try:
        session.execute("UPDATE b_chapter_history SET begin_time= '2015-09-05 18:35:44' WHERE bid = (SELECT bid FROM b_user WHERE mobilephone= " + str(phone) + ")")
        session.commit()
    except:
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '1', '1', \'" + str(bid) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '3', \'" + str(bid) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '4', \'" + str(bid) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '5', \'" + str(bid) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '6', \'" + str(bid) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '7', \'" + str(bid) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '8', \'" + str(bid) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
    session.close()


def train_time_end(phone):
    session = db_session()
    session.execute("UPDATE b_chapter_history SET end_time= '2015-09-06 18:35:44' WHERE bid = (SELECT bid FROM b_user WHERE mobilephone= " + str(phone) + ")")
    session.commit()
    session.execute("UPDATE b_chapter_history SET finished= '1' WHERE bid = (SELECT bid FROM b_user WHERE mobilephone= " + str(phone) + ")")
    session.commit()
    session.execute("UPDATE b_train_history SET end_time= '2015-09-19 14:32:09' WHERE bid = (SELECT bid FROM b_user WHERE mobilephone= " + str(phone) + ")")
    session.commit()
    session.execute("UPDATE b_train_history SET finished= '1' WHERE bid = (SELECT bid FROM b_user WHERE mobilephone= " + str(phone) + ")")
    session.commit()
    session.execute("UPDATE b_user SET train_status= '1' where mobilephone= \'" + str(phone) + "\'")
    session.commit()
    session.close()

#获取用户题库
def train_question(phone):
    session = db_session()
    arr = []
    for i in session.execute("select * from b_user WHERE mobilephone = " + str(phone)).fetchall():
        bid = i.bid
    for i in session.execute("select * from b_question_history WHERE bid = \'" + bid + "\'").fetchall():
        id = i.question_id
        for j in session.execute("select * from sys_question WHERE id = " + str(id)).fetchall():
            arr.append(j.correct_answer)
    session.close()
    return arr


#获取用户每道题的选项数
def train_question_count(phone):
    session = db_session()
    arr = []
    for i in session.execute("select * from b_user WHERE mobilephone = " + str(phone)).fetchall():
        bid = i.bid
    for i in session.execute("select * from b_question_history WHERE bid = \'" + bid + "\'").fetchall():
        id = i.question_id
        for j in session.execute("select * from sys_question WHERE id = " + str(id)).fetchall():
            arr.append(j.answer.encode("utf-8").count("\n") + 1)
    session.close()
    return arr


#获取章节完成状态
def chapter_status(a, b, phone):
    session = db_session()
    for i in session.execute("select * from b_chapter_history where bid = (select bid from b_user where mobilephone = " + str(phone) + ")").fetchall():
        return i.finished
    session.close()


#签订合同
def sign_contract(phone):
    b_operate_record = db_operate_log(phone)
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    b_operate_record.bid = bid
    b_operate_record.operate_by = 10
    b_operate_record.relation_id = ''
    b_operate_record.operate_type = 51
    b_operate_record.reason = "新合同已归档生效，有效期截止至：2020-01-01"
    b_operate_record.create_time = relatedTime.currenttime()
    b_operate_record.update_time = relatedTime.currenttime()
    session.add(b_operate_record)
    session.execute("update b_user SET sac_status = 0 WHERE  mobilephone = " + str(phone))
    session.commit()
    session.close()


#生成sac账号
def sac_account(phone, user, password):
    b_operate_record = db_operate_log(phone)
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    b_operate_record.operate_by = 10
    b_operate_record.relation_id = ''
    b_operate_record.operate_type = 70
    b_operate_record.reason = "SAC登录用户名密码变更。用户名：" + str(user) + "密码：" + str(password)
    b_operate_record.create_time = relatedTime.currenttime()
    b_operate_record.update_time = relatedTime.currenttime()
    session.add(b_operate_record)
    session.execute("update b_user SET sac_apply_count = " + str(user) + " where mobilephone = " + str(phone))
    session.execute("update b_user SET sac_apply_password = " + str(password) + " where mobile = " + str(phone))
    session.commit()
    session.close()


# 生成执业证书编号
def sac_certificate(phone, certificate):
    b_operate_record = db_operate_log(phone)
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    b_operate_record.operate_by = 10
    b_operate_record.relation_id = ''
    b_operate_record.operate_type = 71
    b_operate_record.reason = "执业证书编号已更新为：" + str(certificate)
    b_operate_record.create_time = relatedTime.currenttime()
    b_operate_record.update_time = relatedTime.currenttime()
    session.add(b_operate_record)
    session.execute("update b_user SET sac_id = " + str(certificate) + " where mobilephone = " + str(phone))
    session.execute("update b_user SET sac_status = '1' where mobile = " + str(phone))
    session.commit()
    session.close()


# SAC审核
def sac_approve(phone):
    b_operate_record = db_operate_log(phone)
    session = db_session()
    session.execute("update b_user SET sac_status = '2' where mobilephone = " + str(phone))
    session.commit()
    session.close()

# Bweb审核后台显示的经纪人姓名
def broker_name(phone):
    session = db_session()
    user = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first()
    if(user.id_audit_status != '0'):
        return user.name
    else:
        return str(phone)




#0-未上传, 1-已上传未审核, 2-已上传已审核
def uploadid_status(phone):
    session = db_session()
    for i in session.execute("select * FROM b_user WHERE mobilephone = " + str(phone)).fetchall():
        return i.id_audit_status
    session.close()


#-1-锁定, 0-未完成, 1-已完成
def train_status(phone):
    session = db_session()
    for i in session.execute("select * FROM b_user WHERE mobilephone = " + str(phone)).fetchall():
        return i.train_status
    session.close()


#0-未签收, 1-签收
def contract_status(phone):
    session = db_session()
    bid = session.execute("select bid From b_user where mobilephone = \'" + str(phone) + "\'").first().bid
    for i in session.execute("select * FROM b_user_contract WHERE bid = \'" + str(bid) + "\'").fetchall():
        return i.contract_status
    session.close()


#-1-锁定 0-审核/年审不通过 1-已申请帐号 2-审核通过
def sac_status(phone):
    session = db_session()
    for i in session.execute("select * FROM b_user WHERE mobilephone = " + str(phone)).fetchall():
        return i.sac_status
    session.close()

#从业资格考试状态 -1-锁定 0-未通过 1-已考试未审核 2-已完成 3-未考试
def exam_status(phone):
    session = db_session()
    for i in session.execute("select * FROM b_user WHERE mobilephone = " + str(phone)).fetchall():
        return i.sq_exam_status
    session.close()

#获取经纪人信息
def broker_info(phone):
    session = db_session()
    result = session.execute("select * FROM b_user WHERE mobilephone = \'" + str(phone) + "\'").fetchall()
    session.close()
    return result

#获取经纪人客户
def broker_customer(brokerphone):
    session = db_session()
    result = session.execute("select * FROM b_customer WHERE status = 1 and is_bapp_sync = 1 and bid = (SELECT bid FROM b_user WHERE mobilephone = " + str(brokerphone) + ")").fetchall()
    session.close()
    return result


#获取经纪人跟进
def user_follow_done(phone, cid):
    session = db_session()
    result = session.execute("select * From b_follow_done WHERE cid = \'" + cid + "\' and b_userid = (select bid from b_user WHERE mobilephone = " + str(phone) + ")").fetchall()
    session.close()
    return result


#客户跟进数量
def customer_follow_count(cid):
    session = db_session()
    result = session.execute("select * From b_customer WHERE cid = \'" + cid + "\'").first()
    result = result.total_follow - result.total_todo
    session.close()
    return result


#获取经纪人客户的手机号
def customer_mobile(cid):
    session = db_session()
    result = session.execute("select value from b_customer_extend where type = 10 and status = 1 and cid = " + str(cid)).first()
    return result


#删除所有客户:
def del_customer(phone):
    session = db_session()
    session.execute("delete from b_customer WHERE bid = (select bid FROM b_user WHERE mobilephone = " + str(phone) +")")
    session.commit()
    session.close()


#获取具体客户信息
def user_customer(brokerphone, customerphone):
    session = db_session()
    result = session.execute("select * FROM b_customer WHERE status = 1 and is_bapp_sync = 1 and bid = (SELECT bid FROM b_user WHERE mobilephone = " + str(brokerphone) + ") and cid in (select cid from b_customer_extend where type = 10 and value = " + str(customerphone) +")").fetchall()
    session.close()
    return result


#获取经纪人客户状态: 0-未开户, 1-已开户, 2-他人客户, 3-我的客户
def customer_status(brokerphone, customerphone):
    session = db_session()
    bid = session.execute("select bid from b_user WHERE mobilephone = " + str(brokerphone)).first()[0]
    result = session.execute("select * from c_user WHERE loginmobile = " + str(customerphone)).first()
    if(result == None):
        return '未开户'
    elif(result.status == 201):
        return '未开户'
    elif(result.bapp_broker_id == 'gggggggggggggggggggggggggggggggg' and result.status == 401):
        return '已开户'
    elif(result.bapp_broker_id != bid and result.status == 401):
        return '他人客户'
    elif(result.bapp_broker_id == bid and result.status == 401):
        return '我的客户'

#构造他人客户
def other_customer():
    session = db_session()
    session.execute("update c_user SET bapp_broker_id = 'ggggggggggggggggggggggggggggggg1' WHERE loginmobile = '13300000002'")
    session.commit()
    session.close()


#构造我的客户
def mine_customer(phone, customerphone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    session.execute("update c_user SET bapp_broker_id = \'" + bid + "\' WHERE loginmobile = \'" + str(customerphone) + "\'")
    session.commit()
    session.close()


#获取营业部信息
def get_department(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    roleid = session.execute("select * from sys_user_role WHERE user_id = \'" + bid + "\'").first().role_id
    department = session.execute("select * from sys_role WHERE id = " + str(roleid)).first().name
    session.close()
    return department

#获取合同时间
def get_contract_time(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from b_user_contract WHERE bid = \'" + bid + "\'").first()
    begin_time = result.contract_start_time.strftime("%Y-%m-%d")
    end_time = result.contract_end_time.strftime("%Y-%m-%d")
    session.close()
    return  begin_time, end_time


#构造可提现金额
def cash_count(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    session.execute("delete from trade_user WHERE bid = \'" + bid + "\'")
    session.commit()
    session.execute("INSERT INTO trade_user VALUES (\'" + bid + "\', 1234, 0, 0, 0)")
    session.commit()
    result = session.execute("select * from trade_user where bid = \'" + bid + "\'").first().fund_avl
    session.close()
    return result/100.00


#构造KPI数据
def KPI(phone):
    session = db_session()
    lastmonth, thismonth = relatedTime.kpitime()
    operate_time = relatedTime.currenttime()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    session.execute("delete from b_kpi WHERE bid = \'" + bid + "\'")
    session.commit()
    session.execute("INSERT INTO b_kpi VALUES (NULL, \'" + bid + "\', " + lastmonth + ", '100', '0', '8', '1', '1', '0', '-1', '0', '1', '2015-10-29 23:00:04', '2015-10-29 23:00:04');")
    session.commit()
    session.execute("INSERT INTO b_kpi VALUES (NULL, \'" + bid + "\', " + thismonth + ", '100', '0', '8', '1', '1', '0', '-1', '0', '1', '2015-10-29 23:00:04', '2015-10-29 23:00:04');")
    session.commit()
    # session.execute("delete from b_kpi_change where bid = \'" + bid + "\'")
    # session.commit()
    # session.execute("INSERT INTO b_kpi_change VALUES (NULL, \'" + operate_time + "\', \'" + operate_time + "\', '-20', \'" + bid + "\', '减二十分', '112599ff6b757f5ec5e4acbfd17c1d91', '')")
    # session.commit()
    # session.execute("INSERT INTO b_kpi_change VALUES (NULL, \'" + operate_time + "\', \'" + operate_time + "\', '10', \'" + bid + "\', '加十分', '112599ff6b757f5ec5e4acbfd17c1d91', '')")
    # session.commit()
    session.close()


#构造客户交易额以及推荐奖金
def trade_commission(phone, broker):
    # insert_buser(Data.getNumber('register', 'register', 'phoneText', 2))
    # insert_buser(Data.getNumber('register', 'register', 'phoneText', 3))
    # insert_buser(Data.getNumber('register', 'register', 'phoneText', 4))
    # insert_buser(Data.getNumber('register', 'register', 'phoneText', 5))
    # insert_buser(Data.getNumber('register', 'register', 'phoneText', 6))
    # mine_customer(Data.getNumber('register', 'register', 'phoneText', 2), 13300000001)
    # mine_customer(Data.getNumber('register', 'register', 'phoneText', 2), 13300000002)
    # mine_customer(Data.getNumber('register', 'register', 'phoneText', 3), 13300000003)
    # mine_customer(Data.getNumber('register', 'register', 'phoneText', 4), 13300000004)
    # mine_customer(Data.getNumber('register', 'register', 'phoneText', 5), 13300000005)
    # mine_customer(Data.getNumber('register', 'register', 'phoneText', 5), 13300000006)
    # mine_customer(Data.getNumber('register', 'register', 'phoneText', 6), 13300000007)
    # mine_customer(Data.getNumber('register', 'register', 'phoneText', 6), 13300000008)
    session = db_session()
    cust_id = []
    name = []
    lastmonth, thismonth = relatedTime.kpitime()
    now = relatedTime.currenttime()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from c_user where bapp_broker_id = \'" + bid + "\'").fetchall()
    for i in result:
        try:
            cust_id.append(session.execute("select * from trade_fund_account WHERE c_user_id = \'" + str(i.id) + "\'").first().cust_id)
            name.append(i.truename)
        except:
            print ""
    tradetime1, tradetime2, tradetime3, tradetime4, recommandtime1, recommandtime2, recommandtime3, recommandtime4, month1, month2, month3, month4 = relatedTime.tradetime()
    '''
    客户1
    历史业绩：
        前一个月有多个客户多笔交易数据
        前一个月有多个推荐人奖金
        前两个月有１个客户多笔交易数据
        前两个月有０个推荐人奖金
        前三个月有０个客户交易数据
        前三个月有１个推荐人奖金"
    本月业绩：
        本月有１个推荐人奖金
        本月无客户交易数据
    '''
    if(broker == 1):
        session.execute("delete from trade_recommand_award where recommand_person = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + recommandtime4 + "\', NULL, '100.00000', '0.00000', '100.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000001', '100.00000')")
        session.commit()
        insert_buser(14400000001)
        session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + recommandtime2 + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000002', '100.00000')")
        session.commit()
        insert_buser(14400000002)
        session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + recommandtime2 + "\', NULL, '100.00000', '100.00000', '300.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000003', '200.00000')")
        session.commit()
        insert_buser(14400000003)
        session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '300.00000', '400.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000004', '400.00000')")
        session.commit()
        insert_buser(14400000004)
        session.execute("delete from trade_fund_change WHERE change_person = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + recommandtime4 + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c9414400000001', '1', '0')")
        session.commit()
        session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + recommandtime2 + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c9414400000002', '1', '0')")
        session.commit()
        session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + recommandtime2 + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c9414400000003', '1', '0')")
        session.commit()
        session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + recommandtime1 + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c9414400000004', '1', '0')")
        session.commit()
        session.execute("delete from trade_recommand_award_bal where recommand_person = \'" + bid + "\'")
        session.commit()
        # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime4 + "\', NULL, '100.00000', '0.00000', '100.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000001', '100.00000')")
        # session.commit()
        # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime2 + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000002', '100.00000')")
        # session.commit()
        # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime2 + "\', NULL, '100.00000', '100.00000', '300.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000003', '200.00000')")
        # session.commit()
        session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '300.00000', '400.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000004', '100.00000')")
        session.commit()
        session.execute("delete from trade_commission where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime3 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '626.00000', '0.00000', '626.00000', '626.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.15650', '0.04844', '0.27092', '4.52414', '0.00000', '4.52414', '4.52414', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime3 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '10488.00000', '626.00000', '11114.00000', '11114.00000', '15.73000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '2.62200', '0.13108', '0.73320', '12.24372', '4.52414', '16.76786', '16.76786', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '4014.00000', '11114.00000', '15128.00000', '15128.00000', '6.02000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '1.00350', '0.05017', '0.28060', '4.68574', '16.76786', '21.45360', '21.45360', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '1720.00000', '15128.00000', '16848.00000', '16848.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.43000', '0.04570', '0.25562', '4.26868', '21.45360', '25.72228', '25.72228', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '2486.00000', '16848.00000', '19334.00000', '19334.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.62150', '0.04379', '0.24491', '4.08980', '25.72228', '29.81208', '29.81208', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '4960.00000', '19334.00000', '24294.00000', '24294.00000', '7.44000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '1.24000', '0.06200', '0.34680', '5.79120', '29.81208', '35.60328', '35.60328', '0')")
        session.commit()
        session.execute("delete from trade_commission_bal where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_commission_bal VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '4960.00000', '19334.00000', '24294.00000', '24294.00000', '7.44000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '1.24000', '0.06200', '0.34680', '5.79120', '29.81208', '35.60328', '35.60328', '0')")
        session.commit()
        session.execute("delete from trade_security_guard where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_security_guard VALUES (NULL, \'" + bid + "\', '1.68000', '0', '0.00000', '1.68000', '0.00000', '0.00000', '0.00000', '1970-01-01 08:00:00', '0', '50000.00000', \'" + str(month3) +"month payment add sg_fund', \'" + str(month3) +"month payment', '0.00000', '', '2015-12-02 16:48:20', '2015-12-02 16:48:20')")
        session.commit()
        session.execute("INSERT INTO trade_security_guard VALUES (NULL, \'" + bid + "\', '3.56000', '0', '1.68000', '5.24000', '0.00000', '0.00000', '0.00000', '1970-01-01 08:00:00', '0', '50000.00000', \'" + str(month2) +"month payment add sg_fund', \'" + str(month2) +"month payment', '0.00000', '', '2015-12-02 16:48:39', '2015-12-02 16:48:39')")
        session.commit()
        session.execute("delete from trade_month_clear WHERE bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_month_clear VALUES (NULL, \'" + month4 + "\', \'" + bid + "\', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '1.0000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '100.00000', '0.00000', '100.00000', '0.00000', '0.00000', '0.00000', '100.00000', '0.00000', '0.00000', '100.00000', '0.00000', '100.00000', '100.00000', '0.00000', '100.00000', '0')")
        session.commit()
        session.execute("INSERT INTO trade_month_clear VALUES (NULL, \'" + month3 + "\', \'" + bid + "\', '11114.00000', '0.00000', '11114.00000', '20.73000', '0.00000', '16.77000', '0.00000', '16.77000', '0.00000', '16.77000', '1.0000', '0.00000', '0.00000', '16.77000', '1.68000', '0.00000', '1.68000', '15.09000', '0.00000', '15.09000', '0.00000', '100.00000', '100.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '100.00000', '100.00000', '15.09000', '100.00000', '115.09000', '0')")
        session.commit()
        session.execute("INSERT INTO trade_month_clear VALUES (NULL, \'" + month2 + "\', \'" + bid + "\', '13180.00000', '11114.00000', '24294.00000', '23.46000', '0.00000', '35.60000', '16.77000', '52.37000', '0.00000', '35.60000', '1.0000', '0.00000', '0.00000', '35.60000', '3.56000', '1.68000', '5.24000', '32.04000', '15.09000', '47.13000', '200.00000', '100.00000', '300.00000', '0.00000', '0.00000', '0.00000', '200.00000', '0.00000', '0.00000', '200.00000', '100.00000', '300.00000', '232.04000', '115.09000', '347.13000', '0')")
        session.commit()
        session.execute("INSERT INTO trade_month_clear VALUES (NULL, \'" + month1 + "\', \'" + bid + "\', '0.00000', '24294.00000', '24294.00000', '0.00000', '0.00000', '0.00000', '52.37000', '52.37000', '0.00000', '0.00000', '1.0000', '0.00000', '0.00000', '0.00000', '0.00000', '5.24000', '5.24000', '0.00000', '47.13000', '47.13000', '100.00000', '300.00000', '400.00000', '0.00000', '0.00000', '0.00000', '100.00000', '0.00000', '0.00000', '100.00000', '300.00000', '400.00000', '100.00000', '347.13000', '447.13000', '0')")
        session.commit()
    '''
    客户2
    本月业绩：
        本月有０个推荐人奖金
        本月有１个客户一笔交易数据
    '''
    if(broker == 2):
        session.execute("delete from trade_commission where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '626.00000', '0.00000', '626.00000', '626.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.15650', '0.04844', '0.27092', '4.52414', '0.00000', '4.52414', '4.52414', '0')")
        session.commit()
        session.execute("delete from trade_commission_bal where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_commission_bal VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '626.00000', '0.00000', '626.00000', '626.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.15650', '0.04844', '0.27092', '4.52414', '0.00000', '4.52414', '4.52414', '0')")
        session.commit()
        session.execute("delete from trade_security_guard where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_security_guard VALUES (NULL, \'" + bid + "\', '0.45000', '0', '0.00000', '0.45000', '0.00000', '0.00000', '0.00000', '1970-01-01 08:00:00', '0', '50000.00000', \'" + str(month1) +"month payment add sg_fund', \'" + str(month1) +"month payment', '0.00000', '', '2015-12-02 16:48:20', '2015-12-02 16:48:20')")
        session.commit()
        session.execute("delete from trade_month_clear WHERE bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_month_clear VALUES (NULL, \'" + month1 + "\', \'" + bid + "\', '626.00000', '0.00000', '626.00000', '0.00000', '0.00000', '4.52000', '0.00000', '4.52000', '0.00000', '4.52000', '1.0000', '0.00000', '0.00000', '4.52000', '0.45000', '0.00000', '0.45000', '4.07000', '0.00000', '4.07000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '4.07000', '0.00000', '4.07000', '0')")
        session.commit()

    '''
    客户3
    本月业绩：
        本月有１个推荐人奖金
        本月有１个客户多笔交易数据
    '''
    if(broker == 3):
      session.execute("delete from trade_commission where bid = \'" + bid + "\'")
      session.commit()
      session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '626.00000', '0.00000', '626.00000', '626.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.15650', '0.04844', '0.27092', '4.52414', '0.00000', '4.52414', '4.52414', '0')")
      session.commit()
      session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '10488.00000', '626.00000', '11114.00000', '11114.00000', '15.73000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '2.62200', '0.13108', '0.73320', '12.24372', '4.52414', '16.76786', '16.76786', '0')")
      session.commit()
      session.execute("delete from trade_commission_bal where bid = \'" + bid + "\'")
      session.commit()
      session.execute("INSERT INTO trade_commission_bal VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '10488.00000', '626.00000', '11114.00000', '11114.00000', '15.73000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '2.62200', '0.13108', '0.73320', '12.24372', '4.52414', '16.76786', '16.76786', '0')")
      session.commit()
      session.execute("delete from trade_security_guard where bid = \'" + bid + "\'")
      session.commit()
      session.execute("INSERT INTO trade_security_guard VALUES (NULL, \'" + bid + "\', '1.68000', '0', '0.00000', '1.68000', '0.00000', '0.00000', '0.00000', '1970-01-01 08:00:00', '0', '50000.00000', \'" + str(month1) +"month payment add sg_fund', \'" + str(month1) +"month payment', '0.00000', '', '2015-12-02 16:48:20', '2015-12-02 16:48:20')")
      session.commit()
      session.execute("delete from trade_recommand_award where recommand_person = \'" + bid + "\'")
      session.commit()
      session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '0.00000', '100.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000005', '100.00000')")
      session.commit()
      insert_buser(14400000005)
      session.execute("delete from trade_fund_change WHERE change_person = \'" + bid + "\'")
      session.commit()
      session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + recommandtime1 + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c9414400000005', '1', '0')")
      session.commit()
      session.execute("delete from trade_recommand_award_bal where recommand_person = \'" + bid + "\'")
      session.commit()
      session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '0.00000', '100.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000005', '100.00000')")
      session.commit()
      session.execute("delete from trade_month_clear WHERE bid = \'" + bid + "\'")
      session.commit()
      session.execute("INSERT INTO trade_month_clear VALUES (NULL, \'" + month1 + "\', \'" + bid + "\', '11114.00000', '0.00000', '11114.00000', '20.73000', '0.00000', '16.77000', '0.00000', '16.77000', '0.00000', '16.77000', '1.0000', '0.00000', '0.00000', '16.77000', '1.68000', '0.00000', '1.68000', '15.09000', '0.00000', '15.09000', '100.00000', '0.00000', '100.00000', '0.00000', '0.00000', '0.00000', '100.00000', '0.00000', '0.00000', '100.00000', '0.00000', '100.00000', '115.09000', '0.00000', '115.09000', '0')")
      session.commit()

    '''
    客户4
    本月业绩：
        本月有多个推荐人奖金
        本月有多个客户多笔交易数据
    '''
    if(broker == 4):
        session.execute("delete from trade_recommand_award where recommand_person = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000006', '100.00000')")
        session.commit()
        insert_buser(14400000006)
        session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '100.00000', '300.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000007', '200.00000')")
        session.commit()
        insert_buser(14400000007)
        session.execute("delete from trade_fund_change WHERE change_person = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + recommandtime1 + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c9414400000006', '1', '0')")
        session.commit()
        session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + recommandtime1 + "\', '100', \'" + bid + "\', 'ob', '6b4f9f85012b304979c9414400000007', '1', '0')")
        session.commit()
        session.execute("delete from trade_recommand_award_bal where recommand_person = \'" + bid + "\'")
        session.commit()
        # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '0.00000', '100.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000001', '100.00000')")
        # session.commit()
        # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000002', '100.00000')")
        # session.commit()
        # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime2 + "\', NULL, '100.00000', '100.00000', '300.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000003', '200.00000')")
        # session.commit()
        session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000007', '200.00000')")
        session.commit()
        session.execute("delete from trade_commission where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '626.00000', '0.00000', '626.00000', '626.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.15650', '0.04844', '0.27092', '4.52414', '0.00000', '4.52414', '4.52414', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '10488.00000', '626.00000', '11114.00000', '11114.00000', '15.73000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '2.62200', '0.13108', '0.73320', '12.24372', '4.52414', '16.76786', '16.76786', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '4014.00000', '11114.00000', '15128.00000', '15128.00000', '6.02000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '1.00350', '0.05017', '0.28060', '4.68574', '16.76786', '21.45360', '21.45360', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '1720.00000', '15128.00000', '16848.00000', '16848.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.43000', '0.04570', '0.25562', '4.26868', '21.45360', '25.72228', '25.72228', '0')")
        session.commit()
        session.execute("delete from trade_commission_bal where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_commission_bal VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '1720.00000', '15128.00000', '16848.00000', '16848.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.43000', '0.04570', '0.25562', '4.26868', '21.45360', '25.72228', '25.72228', '0')")
        session.commit()
        session.execute("delete from trade_security_guard where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_security_guard VALUES (NULL, \'" + bid + "\', '5.24000', '0', '0.00000', '5.24000', '0.00000', '0.00000', '0.00000', '1970-01-01 08:00:00', '0', '50000.00000', \'" + str(month1) +"month payment add sg_fund', \'" + str(month1) +"month payment', '0.00000', '', '2015-12-02 16:48:39', '2015-12-02 16:48:39')")
        session.commit()
        session.execute("delete from trade_month_clear WHERE bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_month_clear VALUES (NULL, \'" + month1 + "\', \'" + bid + "\', '16848.00000', '0.00000', '16848.00000', '31.75000', '0.00000', '25.72000', '0.00000', '25.72000', '0.00000', '25.72000', '1.0000', '0.00000', '0.00000', '25.72000', '2.57000', '0.00000', '2.57000', '23.15000', '0.00000', '23.15000', '200.00000', '0.00000', '200.00000', '0.00000', '0.00000', '0.00000', '200.00000', '0.00000', '0.00000', '200.00000', '0.00000', '200.00000', '223.15000', '0.00000', '223.15000', '0')")
        session.commit()
    '''
    客户5
    本月业绩：
        本月无业绩数据
        上个月有业绩数据
    '''
    if(broker == 5):
        session.execute("delete from trade_recommand_award where recommand_person = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + recommandtime2 + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000008', '100.00000')")
        session.commit()
        insert_buser(14400000008)
        session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + recommandtime2 + "\', NULL, '100.00000', '100.00000', '300.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000009', '200.00000')")
        session.commit()
        insert_buser(14400000009)
        session.execute("delete from trade_fund_change WHERE change_person = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + recommandtime2 + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c9414400000008', '1', '0')")
        session.commit()
        session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + recommandtime2 + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c9414400000009', '1', '0')")
        session.commit()
        session.execute("delete from trade_recommand_award_bal where recommand_person = \'" + bid + "\'")
        session.commit()
        # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '0.00000', '100.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000001', '100.00000')")
        # session.commit()
        # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime1 + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000002', '100.00000')")
        # session.commit()
        # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime2 + "\', NULL, '100.00000', '100.00000', '300.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000003', '200.00000')")
        # session.commit()
        session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + recommandtime2 + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c9414400000009', '200.00000')")
        session.commit()
        session.execute("delete from trade_commission where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '626.00000', '0.00000', '626.00000', '626.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.15650', '0.04844', '0.27092', '4.52414', '0.00000', '4.52414', '4.52414', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '10488.00000', '626.00000', '11114.00000', '11114.00000', '15.73000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '2.62200', '0.13108', '0.73320', '12.24372', '4.52414', '16.76786', '16.76786', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '4014.00000', '11114.00000', '15128.00000', '15128.00000', '6.02000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '1.00350', '0.05017', '0.28060', '4.68574', '16.76786', '21.45360', '21.45360', '0')")
        session.commit()
        session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '1720.00000', '15128.00000', '16848.00000', '16848.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.43000', '0.04570', '0.25562', '4.26868', '21.45360', '25.72228', '25.72228', '0')")
        session.commit()
        session.execute("delete from trade_commission_bal where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_commission_bal VALUES (NULL, \'" + tradetime2 + "\', '2', '1000', '0', '0', '', NULL, NULL, NULL, \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '1720.00000', '15128.00000', '16848.00000', '16848.00000', '5.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.00000', '0.43000', '0.04570', '0.25562', '4.26868', '21.45360', '25.72228', '25.72228', '0')")
        session.commit()
        session.execute("delete from trade_security_guard where bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_security_guard VALUES (NULL, \'" + bid + "\', '5.24000', '0', '0.00000', '5.24000', '0.00000', '0.00000', '0.00000', '1970-01-01 08:00:00', '0', '50000.00000', \'" + str(month2) +"month payment add sg_fund', \'" + str(month2) +"month payment', '0.00000', '', '2015-12-02 16:48:39', '2015-12-02 16:48:39')")
        session.commit()
        session.execute("delete from trade_month_clear WHERE bid = \'" + bid + "\'")
        session.commit()
        session.execute("INSERT INTO trade_month_clear VALUES (NULL, \'" + month2 + "\', \'" + bid + "\', '16848.00000', '0.00000', '16848.00000', '31.75000', '0.00000', '25.72000', '0.00000', '25.72000', '0.00000', '25.72000', '1.0000', '0.00000', '0.00000', '25.72000', '2.57000', '0.00000', '2.57000', '23.15000', '0.00000', '23.15000', '200.00000', '0.00000', '200.00000', '0.00000', '0.00000', '0.00000', '200.00000', '0.00000', '0.00000', '200.00000', '0.00000', '200.00000', '223.15000', '0.00000', '223.15000', '0')")
        session.commit()


    # session.execute("delete from trade_commission_bal where bid = \'" + bid + "\'")
    # session.commit()
    # # session.execute("insert into trade_commission_bal VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '1234.56000', '0.00000', '1234.56000', '1234.56000', '9.72000', '0.00000', '9.72000', '9.72000', '0.00000', '0.00000', '0.00000', '0.00000', '3.24750', '0.16243', '0.90852', '15.00000', '0.00000', '15.00000', '15.00000', '0')")
    # # session.commit()
    # # print cust_id[0]
    # # session.execute("INSERT INTO trade_commission_bal VALUES (NULL, '20151208', '2', '1274', '0', \'" + cust_id[0] + "', '马会庆 ', 'ac422170f94a9455c3bd4150bda0ba25', '22120.00000', '2160354.88000', '2182474.88000', '702973.88000', '33.18000', '2925.11000', '2958.29000', '1054.47000', '31.22000', '2757.35000', '2788.57000', '995.91000', '3.31800', '0.52259', '1.68720', '27.65221', '2677.65178', '2705.30399', '878.79616', '0')")
    # session.execute("INSERT INTO trade_commission_bal VALUES (NULL, \'" + tradetime0 + "\', '2', '1000', '0', \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '7890.12000', '1234.56000', '9124.68000', '9124.68000', '9.72000', '9.72000', '19.44000', '9.72000', '0.00000', '0.00000', '0.00000', '0.00000', '3.24750', '0.16243', '0.90852', '15.00000', '15.00000', '30.00000', '15.00000', '0')")
    # session.commit()
    # session.execute("delete from trade_commission where bid = \'" + bid + "\'")
    # session.commit()
    # session.execute("insert into trade_commission VALUES (NULL, \'" + tradetime0 + "\', '2', '1000', '0', \'" + cust_id[1] + "\', \'" + name[1] + "\', \'" + bid + "\', '7890.12000', '1234.56000', '9124.68000', '9124.68000', '9.72000', '9.72000', '19.44000', '9.72000', '0.00000', '0.00000', '0.00000', '0.00000', '3.24750', '0.16243', '0.90852', '15.00000', '15.00000', '30.00000', '15.00000', '0')")
    # session.commit()
    # session.execute("INSERT INTO trade_commission VALUES (NULL, \'" + tradetime1 + "\', '2', '1000', '0', \'" + cust_id[0] + "\', \'" + name[0] + "\', \'" + bid + "\', '1234.56000', '0.00000', '1234.56000', '1234.56000', '9.72000', '0.00000', '9.72000', '9.72000', '0.00000', '0.00000', '0.00000', '0.00000', '3.24750', '0.16243', '0.90852', '15.00000', '0.00000', '15.00000', '15.00000', '0')")
    # session.commit()
    # session.execute("delete from trade_month_clear WHERE bid = \'" + bid + "\'")
    # session.commit()
    # session.execute("INSERT INTO trade_month_clear VALUES (NULL, \'" + thismonth + "\', \'" + bid + "\', '9124.68000', '0.00000', '9124.68000', '8000.00000', '0.00000', '8000.00000', '0', '8000.00000', '8000.00000', '1.0000', '20.00000', '30.00000', '7950.00000', '800.00000', '0.00000', '800.00000', '7150.00000', '0.00000', '7150.00000', '200.00000', '0.00000', '200.00000', '3456.00000', '0.00000', '3456.00000', '3656.00000', '13.00000', '20.00000', '3623.00000', '0.00000', '3623.00000', '10773.00000', '0.00000', '10773.00000', '0')")
    # session.commit()
    # session.execute("delete from b_user where bid in ('6b4f9f85012b304979c94ac5e3530b12', '6b4f9f85012b304979c94ac5e3530b13')")
    # session.commit()
    # session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94ac5e3530b12', '被推荐者甲', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '13200000001', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '被推荐者甲', '', '0', '', 'kingbroker_6b4f9f85012b304979c94ac5e3530b12', '0', '0')")
    # session.commit()
    # session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94ac5e3530b13', '被推荐者乙', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '13200000002', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '被推荐者乙', '', '0', '', 'kingbroker_6b4f9f85012b304979c94ac5e3530b13', '0', '0')")
    # session.commit()
    # session.execute("delete from trade_fund_change WHERE change_person = \'" + bid + "\'")
    # session.commit()
    # session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + now + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c94ac5e3530b12', '1', '0')")
    # session.commit()
    # session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + now + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c94ac5e3530b13', '1', '0')")
    # session.commit()
    # session.execute("delete from trade_recommand_award_bal where recommand_person = \'" + bid + "\'")
    # session.commit()
    #
    #
    # # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + now + "\', '100.00000', '0.00000', '100.00000', \'" + bid + "\', '6b4f9f85012b304979c94ac5e3530b12', '100.00000')")
    # # session.commit()
    #
    #
    # session.execute("INSERT INTO trade_recommand_award_bal VALUES (NULL, NULL, \'" + now + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c94ac5e3530b13', '200.00000')")
    # session.commit()
    # session.execute("delete from trade_recommand_award where recommand_person = \'" + bid + "\'")
    # session.commit()
    # session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + now + "\', NULL, '100.00000', '0.00000', '100.00000', \'" + bid + "\', '6b4f9f85012b304979c94ac5e3530b12', '100.00000')")
    # session.commit()
    # session.execute("INSERT INTO trade_recommand_award VALUES (NULL, NULL, \'" + now + "\', NULL, '100.00000', '100.00000', '200.00000', \'" + bid + "\', '6b4f9f85012b304979c94ac5e3530b13', '200.00000')")
    # session.commit()
    # session.execute("delete from trade_security_guard where bid = \'" + bid + "\'")
    # session.commit()
    # session.execute("INSERT INTO trade_security_guard VALUES (NULL, \'" + bid + "\', '800.00000', '0', '0.00000', '800.00000', '0.00000', '0.00000', '0.00000', '1970-01-01 08:00:00', '0', '50000.00000', \'" + str(thismonth) +"month payment add sg_fund', \'" + str(thismonth) +"month payment', '0.00000', '', \'" + now +"\', \'" + now + "\')")
    # session.commit()
    # session.execute("delete from trade_continuous_commission WHERE recommand_bid = \'" + bid + "\'")
    # session.commit()
    # session.execute("INSERT INTO trade_continuous_commission VALUES (NULL, '0', \'" + tradetime0 + "\', \'" + cust_id[0] + "\', 'd3b36dbdb13f68f029ae0fbc6736d771', \'" + bid + "\', '789352.00000', '0.00000', '789352.00000', '789352.00000', '0.00000', '789352.00000', \'" + now + "\')")
    # session.commit()
    # session.execute("INSERT INTO trade_continuous_commission VALUES (NULL, '0', \'" + tradetime1 + "\', \'" + cust_id[1] + "\', 'd3b36dbdb13f68f029ae0fbc6736d772', \'" + bid + "\', '120000.00000', '0.00000', '120000.00000', '120000.00000', '0.00000', '120000.00000', \'" + now + "\')")
    # session.commit()
    # session.execute("delete from trade_continuous_commission_bal WHERE recommand_bid = \'" + bid + "\'")
    # session.commit()
    # session.execute("INSERT INTO trade_continuous_commission_bal VALUES (NULL, '0', \'" + tradetime0 + "\', \'" + cust_id[0] + "\', 'd3b36dbdb13f68f029ae0fbc6736d771', \'" + bid + "\', '789352.00000', '0.00000', '789352.00000', '789352.00000', '0.00000', '789352.00000', \'" + now + "\')")
    # session.commit()
    # session.execute("INSERT INTO trade_continuous_commission_bal VALUES (NULL, '0', \'" + tradetime1 + "\', \'" + cust_id[1] + "\', 'd3b36dbdb13f68f029ae0fbc6736d772', \'" + bid + "\', '120000.00000', '0.00000', '120000.00000', '120000.00000', '0.00000', '120000.00000', \'" + now + "\')")
    # session.commit()
    # session.close()

#构造推荐列表
def share_relation(phone):
    session = db_session()
    now = relatedTime.currenttime()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from sys_share_link where user_code = \'" + bid + "\' and product_type_id = '1'").first()
    invite_code = result.invite_code
    link_id = result.link_id
    session.execute("delete from sys_share_relation WHERE bid = \'" + bid + "\'")
    session.commit()
    for i in range(13300000001, 13300000202):
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '0', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
    for i in range(13300000202, 13300000403):
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '1000', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
    for i in range(13300000403, 13300000604):
        session.execute("delete from b_user where bid = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(i) + "\', '推荐', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(i) + "\', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '推荐', '', '0', '', '', '0')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(i) + "\' where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '1002', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
    for i in range(13300000604, 13300000806):
        session.execute("delete from b_user where bid = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(i) + "\', '推荐', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(i) + "\', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '推荐', '', '0', '', '', '0')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(i) + "\' where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '1001', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
    for i in range(13300000806, 13300001000):
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '-1', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
    session.close()

#构造不同状态的推荐关系
def share_relation_status(phone):
    session = db_session()
    now = relatedTime.currenttime()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from sys_share_link where user_code = \'" + bid + "\' and product_type_id = '1'").first()
    invite_code = result.invite_code
    link_id = result.link_id
    # session.execute("delete from sys_share_relation WHERE bid = \'" + bid + "\'")
    # session.commit()
    # session.execute("delete from trade_fund_change where change_person = \'" + bid + "\'")
    # session.commit()
    # for i in range(13300000001, 13300000202):
    #     session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '0', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
    #     session.commit()
    # for i in range(13300000202, 13300000403):
    #     session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '1000', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
    #     session.commit()
    #未确认资格
    for i in range(15100000001, 15100000121):
        session.execute("delete from b_user where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(i) + "\', '推荐', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(i) + "\', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '0', '1', '-1', '0', '0', '我', '', '0', NULL, '', '0', '0', '1', '1')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(i) + "\' where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("delete from sys_share_relation where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '1000', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
        session.execute("delete from trade_fund_change where change_person = \'" + bid + "\' and relate_person = '6b4f9f85012b304979c94" + str(i) + "\'")
        session.commit()
    #未签订合同
    for i in range(15100000121, 15100000241):
        session.execute("delete from b_user where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(i) + "\', '推荐', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(i) + "\', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '-1', '0', '0', '我', '', '0', NULL, '', '0', '0', '1', '1')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(i) + "\' where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("delete from sys_share_relation where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '1003', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
        session.execute("delete from trade_fund_change where change_person = \'" + bid + "\' and relate_person = '6b4f9f85012b304979c94" + str(i) + "\'")
        session.commit()
    #已签订合同
    for i in range(15100000241, 15100000361):
        session.execute("delete from b_user_contract where bid = '6b4f9f85012b304979c94" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c94" + str(i) + "\', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
        session.commit()
        session.execute("delete from b_user where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(i) + "\', '推荐', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(i) + "\', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '-1', '0', '0', '我', '', '0', NULL, '', '0', '0', '1', '1')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(i) + "\' where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("delete from sys_share_relation where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '1002', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
        session.execute("delete from trade_fund_change where change_person = \'" + bid + "\' and relate_person = '6b4f9f85012b304979c94" + str(i) + "\'")
        session.commit()
    #挂靠完成
    for i in range(15100000361, 15100000481):
        session.execute("delete from b_user where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(i) + "\', '推荐', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(i) + "\', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '0', '0', '推荐', '', '0', NULL, '', '0', '0', '1', '1')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(i) + "\' where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("delete from sys_share_relation where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '1001', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
        session.execute("delete from trade_fund_change where change_person = \'" + bid + "\' and relate_person = '6b4f9f85012b304979c94" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO trade_fund_change VALUES (NULL, \'" + now + "\', '100', \'" + bid + "\', 'bb', '6b4f9f85012b304979c94" + str(i) + "\', '0', '0')")
        session.commit()
    #推荐无效
    for i in range(15100000481, 15100000601):
        session.execute("delete from b_user where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("delete from sys_share_relation where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(i) + "\', '推荐', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(i) + "\', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '0', '0', '推荐', '', '0', NULL, '', '0', '0', '1', '1')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(i) + "\' where mobilephone = \'" + str(i) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '-1', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
        session.commit()
    # for i in range(13300000951, 13300001000):
    #     session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + bid + "\', \'" + str(link_id) + "\', '1', \'" + str(i) + "\', '-1', '100', \'" + now + "\', \'" + now + "\', '0', '0')")
    #     session.commit()
    session.close()

#获取业绩数据
def get_kpi_info(phone):
    session = db_session()
    month = []
    kpi_point = []
    create_time = []
    kpi_change = []
    reason = []
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from b_kpi WHERE bid = \'" + bid + "\' ORDER BY month DESC").fetchall()
    for i in result:
        month.append(str(i.month)[0:4] + '年' + str(i.month)[4:6] + '月' )
        kpi_point.append(str(i.kpi_point))
    result = session.execute("select * from b_kpi_change where bid = \'" + bid + "\' ORDER BY update_time ASC").fetchall()
    for i in result:
        create_time.append(str(i.create_time).split(' ')[0])
        kpi_change.append(str(i.kpi_change))
        reason.append(i.reason)
    return month, kpi_point, create_time, kpi_change, reason

#获取交易额数据
def get_trade_commission(i):
    session = db_session()
    month_trade_amount = []
    cust_trade_amount = []
    month = []
    phone = Data.getNumber('register', 'register', 'phoneText', i)
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from trade_month_clear where bid = \'" + bid + "\' ORDER BY date DESC").fetchall()
    trade_total_amount = str(result[0].amount_month_after.quantize(Decimal('0.00')))
    for i in result:
        month.append(str(i.date)[0:4] + '年' + str(i.date)[4:6] + '月')
        month_trade_amount.append(str(i.amount_cur_month.quantize(Decimal('0.00'))))
        temp = session.execute("select sum(amount_trade) from trade_commission where bid = \'" + bid + "\' and bizdate like '" + str(i.date)[0:6] + "%' GROUP BY cust_id ORDER BY 'id' ASC").fetchall()
        for i in range(0, len(temp)):
            temp[i] = str(temp[i][0].quantize(Decimal('0.00')))
        cust_trade_amount.append(temp)
    session.close()
    return trade_total_amount, month, month_trade_amount, cust_trade_amount

#获取收入数据
def get_income_info(phone):
    session = db_session()
    month = []
    month_detail = []
    commission = []
    recommand_award = []
    tax = []
    month_income = []
    month_risk_amount = []
    month_commission_tax = []
    month_recommand_tax = []
    recommand_name = []
    risk_month=[]
    month_risk_amount_detail = []
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from trade_month_clear where bid = \'" + bid + "\' ORDER BY date DESC").fetchall()
    income_total_amount = str(result[0].fund_cm_after.quantize(Decimal('0.00')))
    risk_amount = str(result[0].fund_sg_after.quantize(Decimal('0.00')))
    for i in result:
        month.append(str(i.date)[0:4] + '年' + str(i.date)[4:6] + '月')
        if(str(i.date)[4:5] == '0'):
            month_detail.append(str(i.date)[0:4] + '年' + str(i.date)[5:6] + '月')
        else:
            month_detail.append(str(i.date)[0:4] + '年' + str(i.date)[4:6] + '月')
        commission.append(str(i.commission_ft.quantize(Decimal('0.00'))))
        recommand_award.append(str(i.reference_combine.quantize(Decimal('0.00'))))
        tax.append('-' + str((i.commission_ft + i.reference_combine - i.fund_current_month).quantize(Decimal('0.00'))))
        month_income.append(str(i.fund_current_month.quantize(Decimal('0.00'))))
        if(str(i.fund_security_guard.quantize(Decimal('0.00'))) != '0.00'):
            month_risk_amount.append(str(i.fund_security_guard.quantize(Decimal('0.00'))))
            risk_month.append(str(i.date)[0:4] + '年' + str(i.date)[4:6] + '月')
        month_risk_amount_detail.append('-' + str(i.fund_security_guard.quantize(Decimal('0.00'))))
        month_commission_tax.append('-' + str((i.commission_ft - i.commission_should_get).quantize(Decimal('0.00'))))
        month_recommand_tax.append('-' + str((i.reference_combine - i.fund_income_reference).quantize(Decimal('0.00'))))
        result = session.execute("select * from trade_recommand_award where recommand_person = \'" + bid + "\' and reference_date like '" + str(i.date)[0:4] + '-' + str(i.date)[4:6] + "%'").fetchall()
        temp = []
        for j in result:
            temp.append(session.execute("select name from b_user where bid = \'" + j.recommanded_person + "\'").first())
        recommand_name.append(temp)
    session.close()
    return income_total_amount, risk_amount, month, commission, recommand_award, tax, month_income, month_risk_amount, month_commission_tax, month_recommand_tax, recommand_name, risk_month, month_risk_amount_detail, month_detail

#获取本月业绩数据
def get_current_mon_info(phone):
    session = db_session()
    thismonth = relatedTime.kpitime()[1]
    current_kpi_change = []
    current_reason = []
    current_createtime = []
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    current_kpipoint = session.execute("select * from b_kpi where bid = \'" + bid + "\' and month = \'" + thismonth + "\'").first().kpi_point
    current_kpipoint = str(current_kpipoint)
    current_commission = session.execute("select * from trade_commission_bal where bid = \'" + bid + "\'")
    if(current_commission.rowcount != 0):
        current_commission = str(current_commission.first().amount_cur_month.quantize(Decimal('0.00')))
    else:
        current_commission = '0.00'
    current_recommand = session.execute("select * from trade_recommand_award_bal where recommand_person = \'" + bid + "\'")
    if(current_recommand.rowcount != 0):
        current_recommand = str(current_recommand.first().amount_current_month.quantize(Decimal('0.00')))
    else:
        current_recommand = '0.00'
    result = session.execute("select * from b_kpi_change where bid = \'" + bid + "\' and create_time like '" + thismonth[0:4] + "-" + thismonth[4:6] +"%\' ORDER BY update_time ASC").fetchall()
    for i in result:
        current_kpi_change.append(str(i.kpi_change))
        current_reason.append(i.reason)
        current_createtime.append(str(i.create_time)[0:10])
    return current_kpipoint, current_commission, current_recommand, thismonth, current_kpi_change, current_reason, current_createtime


#获取本月交易额数据
def get_current_trade_commission(phone):
    session = db_session()
    thismonth = relatedTime.kpitime()[1]
    current_cust_trade_amount = []
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from trade_commission_bal where bid = \'" + bid + "' and bizdate like \'" + thismonth + "%\'").first()
    if(len(result) != 0):
        current_trade_amount = str(result.amount_cur_month.quantize(Decimal('0.00')))
    else:
        current_trade_amount = '0.00'
    temp = session.execute("select sum(amount_trade) from trade_commission where bid = \'" + bid + "\' and bizdate like  \'" + thismonth + "%\' GROUP BY cust_id ORDER BY 'id' ASC").fetchall()
    for i in range(0, len(temp)):
        current_cust_trade_amount.append(str(temp[0][i].quantize(Decimal('0.00'))))
    session.close()
    return current_trade_amount, current_cust_trade_amount

#获取本月推荐奖金
def get_current_recommand_info(phone):
    session = db_session()
    thismonth = relatedTime.kpitime()[1]
    current_recommand_name = []
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    # current_continunous_commission = session.execute("select sum(amount_recommanded_current_month) from trade_continuous_commission_bal where recommand_bid = \'" + bid + "\' and bizdate[0:6] =  \'" + thismonth + "\'").first()
    current_recommand_item = session.execute("select * from trade_recommand_award where recommand_person = \'" + bid + "\' and reference_date like \'" + thismonth[0:4] + '-' + thismonth[4:6] + "%'").fetchall()
    for i in current_recommand_item:
        temp = session.execute("select name from b_user where bid = \'" + i.recommanded_person + "\'").first()
        current_recommand_name.append(temp)
    session.close()
    return current_recommand_name

#删除我的客户
def delete_customer(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    session.execute("delete from b_customer where bid = \'" + bid + "\'")
    session.commit()
    session.close()


#获取佣金调整信息
def get_brokerage(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from trade_brokerage where bid = \'" + bid + "\'").first()
    commission = result.commission
    cust_id = result.cust_id




#插入b_user
def insert_buser(phone):
    session = db_session()
    session.execute("delete from b_user where mobilephone = \'" + str(phone) + "\'")
    session.commit()
    session.execute("delete from b_user_contract where bid = '6b4f9f85012b304979c94" + str(phone) + "\'")
    session.commit()
    session.execute("delete from sys_user_role where user_id = '6b4f9f85012b304979c94" + str(phone) + "\'")
    session.commit()
    session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c94" + str(phone) + "\', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
    session.commit()
    session.execute("INSERT INTO sys_user_role VALUES (NULL, '2', '6b4f9f85012b304979c94" + str(phone) + "\', '21', '1', '0', '2016-01-20 14:39:24', '2016-01-20 14:39:24')")
    session.commit()
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '推荐', '1', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(phone) + "\', '0.0015', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37','0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '1', '0', '推荐', '', '0', NULL, '', '0', '0', '1', '1', '08310001', '2016-04-26 21:46:04', '2')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\' where mobilephone = \'" + str(phone) + "\'")
    session.commit()
    session.close()

#登出bwx
def logout_bwx(phone):
    session = db_session()
    session.execute("update wechat_user set bid = '' where mobilephone = \'" + str(phone) + "\'")
    session.commit()
    session.close()

#删除bwx准考证附件
def del_attachment(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    session.execute("delete from b_user_admission_ticket where bid = \'" + bid + "\'")
    session.commit()


#删除推荐关系
def del_share_relation(phone):
    session = db_session()
    session.execute("delete from sys_share_relation where mobilephone = \'" + str(phone) + "\'")
    session.commit()
    session.close()


#删除Capp用户
def delete_cuser(phone):
    session = db_session()
    cid = session.execute("select * from c_user where loginmobile = \'" + str(phone) + "\'").first().id
    session.execute("delete from c_self_stock where cid = " + str(cid))
    session.commit()
    session.execute("delete from c_user_belong_log where c_user_id = \'" + str(cid) + "\'")
    session.commit()
    session.execute("delete from portfolios where owner = 'imaster_" + str(cid) + "\'")
    session.commit()
    session.execute("delete from portfolio_comments where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_favourites where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_holdings where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_performance where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_rebalancings where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_reference where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from rebalancings where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from trade_fund_account where c_user_id = (select id from c_user where loginmobile = " + str(phone) + ")")
    session.commit()
    session.execute("delete from c_user where loginmobile = " + str(phone))
    session.commit()
    session.execute("delete from sd_customer where mobileno = " + str(phone))
    session.commit()
    session.close()

#构造联系人
def add_customer(phone):
    #删除所有的客户
    del_customer(phone)
    #删除Bapp和Capp客户信息
    for i in range(18000000001, 18000000021):
        try:
            del_buser(i)
            delete_cuser(i)
        except:
            continue
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    #未开户：经纪宝-未注册，投资大师-未注册：18000000001
    # session.execute("insert into b_customer VALUES (NULL, 'd1de087448ed048be05ed23abe51b8270d614060fbdd4c0eb6abf18000000001', '未开户00', '1', \'" + bid + "\', '1', '2015-09-09 17:59:04', '2015-09-09 17:59:05', '1010', '2015-09-09 17:59:05', '0', '0', '2015-09-09 17:59:05')")
    # session.commit()
    #未开户：经纪宝-未注册，投资大师-已注册：18000000002
    session.execute("INSERT INTO c_user VALUES (NULL, 'gggggggggggggggggggggggggggggggg', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000002', '', '', '1', '1977-07-17', '', '', '未开户01', '201', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '1', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000002'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000002'")
    session.commit()
    # session.execute("insert into b_customer VALUES (NULL, 'd1de087448ed048be05ed23abe51b8270d614060fbdd4c0eb6abf18000000002', '未开户00', '1', \'" + bid + "\', '1', '2015-09-09 17:59:04', '2015-09-09 17:59:05', '1010', '2015-09-09 17:59:05', '0', '0', '2015-09-09 17:59:05')")
    # session.commit()
    #未开户：经纪宝-已注册，投资大师-未注册：18000000003
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000003', '未开户10', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000003', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '0', '1', '-1', '未开户10', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c9418000000003', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000003' where mobilephone = '18000000003'")
    session.commit()
    #未开户：经纪宝-已注册，投资大师-已注册：18000000004
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000004', '未开户11', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000004', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '0', '1', '-1', '未开户11', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c9418000000004', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000004' where mobilephone = '18000000004'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, 'gggggggggggggggggggggggggggggggg', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000004', '', '', '1', '1977-07-17', '', '', '未开户11', '201', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '1', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000004'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000004'")
    session.commit()
    #未开户：经纪宝-已挂靠，投资大师-未注册：18000000005
    session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c9418000000005', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
    session.commit()
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000005', '未开户20', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000005', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '未开户20', '', '0', '', 'kingbroker_6b4f9f85012b304979c9418000000005', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000005' where mobilephone = '18000000005'")
    session.commit()
    #已开户：经纪宝-未注册，投资大师-已开户：18000000006
    session.execute("INSERT INTO c_user VALUES (NULL, 'gggggggggggggggggggggggggggggggg', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000006', '', '', '1', '1977-07-17', '', '', '已开户02', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '1', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000006'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000006'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '81106510001', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '18000000006', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000006'").first().id
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', '81106510001', '18000000006', '0.00015000', '0.00000', '已开户02', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    #已开户：经纪宝-已注册，投资大师-已开户：18000000007
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000007', '已开户12', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000007', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '0', '1', '-1', '已开户12', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c9418000000007', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000007' where mobilephone = '18000000007'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, 'gggggggggggggggggggggggggggggggg', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000007', '', '', '1', '1977-07-17', '', '', '已开户12', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '1', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000007'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000007'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '81106510002', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '18000000007', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000007'").first().id
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', '81106510002', '18000000007', '0.00015000', '0.00000',  '已开户12', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    #已开户：经纪宝-已挂靠，投资大师-已开户：18000000008
    session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c9418000000008', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
    session.commit()
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000008', '已开户22', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000008', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '已开户22', '', '0', '', 'kingbroker_6b4f9f85012b304979c9418000000008', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000008' where mobilephone = '18000000008'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, 'gggggggggggggggggggggggggggggggg', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000008', '', '', '1', '1977-07-17', '', '', '已开户22', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000008'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000008'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '81106510003', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '18000000008', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000008'").first().id
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', '81106510003', '18000000008', '0.00015000', '0.00000',  '已开户22', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    #我的客户：经纪宝-未注册，投资大师-已注册：18000000009
    session.execute("INSERT INTO c_user VALUES (NULL, \'" + bid + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000009', '', '', '1', '1977-07-17', '', '', '我的客户01', '201', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000009'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000009'")
    session.commit()
    #我的客户：经纪宝-未注册，投资大师-已开户：18000000010
    session.execute("INSERT INTO c_user VALUES (NULL, \'" + bid + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000010', '', '', '1', '1977-07-17', '', '', '我的客户02', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000010'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000010'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '81106510004', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '18000000010', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000010'").first().id
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', '81106510004', '18000000010', '0.00015000', '0.00000',  '我的客户02', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    #我的客户：经纪宝-已注册，投资大师-已注册：18000000011
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000011', '我的客户11', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000011', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '0', '1', '-1', '我的客户11', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c9418000000011', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000011' where mobilephone = '18000000011'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, \'" + bid + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000011', '', '', '1', '1977-07-17', '', '', '我的客户11', '201', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000011'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000011'")
    session.commit()
    #我的客户：经纪宝-已注册，投资大师-已开户：18000000012
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000012', '我的客户12', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000012', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '0', '1', '-1', '我的客户12', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c9418000000012', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000012' where mobilephone = '18000000012'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, \'" + bid + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000012', '', '', '1', '1977-07-17', '', '', '我的客户12', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000012'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000012'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '81106510005', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '18000000012', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000012'").first().id
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', '81106510005', '18000000012', '0.00015000', '0.00000',  '我的客户12', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    #我的客户：经纪宝-已挂靠，投资大师-已注册：18000000013
    session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c9418000000013', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
    session.commit()
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000013', '我的客户21', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000013', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '我的客户21', '', '0', '', 'kingbroker_6b4f9f85012b304979c9418000000013', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000013' where mobilephone = '18000000013'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, \'" + bid + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000013', '', '', '1', '1977-07-17', '', '', '我的客户21', '201', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000013'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000013'")
    session.commit()
    #我的客户：经纪宝-已挂靠，投资大师-已开户：18000000014
    session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c9418000000014', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
    session.commit()
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000014', '我的客户22', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000014', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '我的客户22', '', '0', '', 'kingbroker_6b4f9f85012b304979c9418000000014', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000014' where mobilephone = '18000000014'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, \'" + bid + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000014', '', '', '1', '1977-07-17', '', '', '我的客户22', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000014'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000014'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '81106510006', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '18000000014', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000014'").first().id
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', '81106510006', '18000000014', '0.00015000', '0.00000',  '我的客户22', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    #他人客户：经纪宝-未注册，投资大师-已注册：18000000015
    session.execute("INSERT INTO c_user VALUES (NULL, 'ggggggggggggggggggggggggggggggg1', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000015', '', '', '1', '1977-07-17', '', '', '他人客户01', '201', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000015'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000015'")
    session.commit()
    #他人客户：经纪宝-未注册，投资大师-已开户：18000000016
    session.execute("INSERT INTO c_user VALUES (NULL, 'ggggggggggggggggggggggggggggggg1', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000016', '', '', '1', '1977-07-17', '', '', '他人客户02', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000016'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000016'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '81106510007', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '18000000016', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000016'").first().id
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', '81106510007', '18000000016', '0.00015000', '0.00000',  '他人客户02', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    #他人客户：经纪宝-已注册，投资大师-已注册：18000000017
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000017', '他人客户11', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000017', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '0', '1', '-1', '他人客户11', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c9418000000017', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000017' where mobilephone = '18000000017'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, 'ggggggggggggggggggggggggggggggg1', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000017', '', '', '1', '1977-07-17', '', '', '他人客户11', '201', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000017'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000017'")
    session.commit()
    #他人客户：经纪宝-已注册，投资大师-已开户：18000000018
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000018', '他人客户12', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000018', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '0', '1', '-1', '他人客户12', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c9418000000018', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000018' where mobilephone = '18000000018'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, 'ggggggggggggggggggggggggggggggg1', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000018', '', '', '1', '1977-07-17', '', '', '他人客户12', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000018'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000018'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '81106510008', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '18000000018', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000018'").first().id
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', '81106510008', '18000000018', '0.00015000', '0.00000',  '他人客户12', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    #他人客户：经纪宝-已挂靠，投资大师-已注册：18000000019
    session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c9418000000019', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
    session.commit()
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000019', '他人客户21', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000019', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '他人客户21', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c9418000000019', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000019' where mobilephone = '18000000019'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, 'ggggggggggggggggggggggggggggggg1', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000019', '', '', '1', '1977-07-17', '', '', '他人客户21', '201', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000019'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000019'")
    session.commit()
    #他人客户：经纪宝-已挂靠，投资大师-已开户：18000000020
    session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c9418000000020', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
    session.commit()
    session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c9418000000020', '他人客户22', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', '18000000020', '0.0015', 'e10adc3949ba59abbe56e057f20f883e', '0', '2010', '', '4', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '2', '2', '1', '2', '他人客户22', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c9418000000020', '0', '0', '0', '1')")
    session.commit()
    session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c9418000000020' where mobilephone = '18000000020'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, 'ggggggggggggggggggggggggggggggg1', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '18000000020', '', '', '1', '1977-07-17', '', '', '他人客户22', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '0', '', '1', '', '', '1', '1')")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000020'").first().id
    session.execute("update c_user set client_id = 'imaster_" + str(cuser_id) + "\' where loginmobile = '18000000020'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '81106510009', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '18000000020', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = '18000000020'").first().id
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', '81106510009', '18000000020', '0.00015000', '0.00000',  '他人客户22', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    for i in range(18000000001, 18000000021):
        buser = session.execute("select * from b_user where mobilephone = \'" + str(i) + "\'").first()
        cuser = session.execute("select * from c_user where loginmobile = \'" + str(i) + "\'").first()
        if(buser != None):
            session.execute("update b_user set client_id = 'kingbroker_" + buser.bid + "\' where mobilephone = \'" + str(i) + "\'")
            session.commit()
        if(cuser != None):
            session.execute("update c_user set client_id = 'imaster_" + str(cuser.id) + "\' where loginmobile = \'" + str(i) + "\'")
            session.commit()
    session.close()


#不同状态的经纪人
def broker_status(phone, status):
    session = db_session()
    try:
        del_buser(phone)
    except:
        print 'no this broker'
    if(status == 'register'):#注册完成
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '', '0', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '', '', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '0', '-1', '-1', '-1', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
    elif(status == 'id_loaded'):#上传完身份证
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '', '', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '1', '-1', '-1', '-1', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
    elif(status == 'id_fail'):#身份证审核不通过
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '', '', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '3', '-1', '-1', '-1', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
    elif(status == 'id_pass'):#身份证审核通过
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '', '', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '2', '1', '-1', '-1', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
    elif(status == 'exam_fail'):#考试不通过
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '', '', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '2', '0', '-1', '-1', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
    elif(status == 'exam_pass'):#考试通过
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '', '', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '2', '2', '0', '-1', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
    elif(status == 'train_ready'):#可以答题
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '', '', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '2', '2', '0', '-1', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '1', '1', '6b4f9f85012b304979c94" + str(phone) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '3', '6b4f9f85012b304979c94" + str(phone) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '4', '6b4f9f85012b304979c94" + str(phone) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '5', '6b4f9f85012b304979c94" + str(phone) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '6', '6b4f9f85012b304979c94" + str(phone) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '7', '6b4f9f85012b304979c94" + str(phone) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
        session.execute("INSERT INTO b_chapter_history VALUES (NULL, '2', '8', '6b4f9f85012b304979c94" + str(phone) + "\', '2015-09-07 21:21:44', NULL, '0')")
        session.commit()
    elif(status == 'train_pass'):#答题完成
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '', '', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '2', '2', '1', '-1', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
    elif(status == 'contract_ready'):#已发送合同
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '123@qq.com', '北京', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '2', '2', '1', '-1', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
        session.execute("INSERT INTO sys_user_role VALUES (NULL, '2', '6b4f9f85012b304979c94" + str(phone) + "\', '21', '1', '2016-01-20 14:39:24', '2016-01-20 14:39:24')")
        session.commit()
        session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c94" + str(phone) + "\', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '0', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
        session.commit()
    elif(status == 'contract_pass'):#已签订合同
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '1', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '', '', '', '0', '', '0', '123@qq.com', '北京', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '2', '2', '1', '0', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
        session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c94" + str(phone) + "\', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
        session.commit()
        session.execute("INSERT INTO sys_user_role VALUES (NULL, '2', '6b4f9f85012b304979c94" + str(phone) + "\', '21', '1', '2016-01-20 14:39:24', '2016-01-20 14:39:24')")
        session.commit()
    elif(status == 'sac_pass'):#SAC通过
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '经纪人" + str(phone) + "\', '1', '汉', '0000-00-00 00:00:00', '2014-05-10 00:00:00', '2024-05-10 00:00:00', '天津市公安局西青分局', '14072" + str(phone) + "\', '天津市西青区西青经济开发区微六路14号', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', '34f85ca80ec353d3052b8a2d3973a0c5', '0', '1011', '', '4', '0', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123123', '123123', '123123', '0', '', '0', '123@qq.com', '北京', 'e3e1f6db621de805f2d6cce21e339f9c', 'e3e1f6db621de805f2d6cce21e339f9c', '0', '0', '1', '', '1', '2', '2', '1', '2', '昵称" + str(phone) + "\', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '1', '0')")
        session.commit()
        session.execute("INSERT INTO b_user_contract VALUES (NULL, '00000000000000000000000000000000', '6b4f9f85012b304979c94" + str(phone) + "\', NULL, NULL, '2000-01-01 00:00:00', '2020-10-13 00:00:00', '4', NULL, NULL, NULL, '2000-01-01 16:33:36', NULL, NULL, '0000-00-00 00:00:00', NULL, '0', '0', '1', '2015-10-15 16:33:36', '2015-10-15 16:33:36')")
        session.commit()
        session.execute("INSERT INTO sys_user_role VALUES (NULL, '2', '6b4f9f85012b304979c94" + str(phone) + "\', '21', '1', '2016-01-20 14:39:24', '2016-01-20 14:39:24')")
        session.commit()
    elif(status == 'quiet_register'):
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '', '0', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '', '', '', '', '', '', '', '', \'" + str(phone) + "\', '0.0008', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', '0', '2020', '', '1', '0', '2016-01-20 10:30:21', '2016-01-20 10:30:21', '', '', '', '', '0', '', '0', '', '', '00000000000000000000000000000000', '00000000000000000000000000000000', '0', '0', '1', '', '1', '0', '-1', '-1', '-1', '经纪人', '', '0', NULL, 'kingbroker_6b4f9f85012b304979c94" + str(phone) + "\', '1', '2', '0')")
        session.commit()
    session.close()

#获取未处理的工单信息
def get_work_order(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    id = session.execute("select * from sys_work_order WHERE user_id = \'" + str(bid) + "\' and status = '0'").first().id
    session.close()
    return id

#添加Capp用户
def add_cuser():
    file_path = globalData.PATH + '/TestData/CappData.xlsx'
    workbook = XLBook(file_path)
    test_data = dict(workbook.sheets())
    worksheet = test_data.get("capp")
    nrows = len(worksheet)
    mobile = []
    cust_id = []
    for i in range(0, nrows):
        mobile.append(str(worksheet[i][0]).split(".")[0])
        cust_id.append(str(worksheet[i][1]).split(".")[0])
    # print mobile[1]
    # print cust_id[1]
    session = db_session()
    for i in range(0, len(mobile)):
        session.execute("delete from c_user where loginmobile = \'" + mobile[i] + "\'")
        session.commit()
        session.execute("INSERT INTO c_user VALUES (NULL, '6b4f9f85012b304979c94" + mobile[i] + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', \'" + mobile[i] + "\', '', '', '1', '1977-07-17', '', '', '投资大师" + mobile[i] + "\', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '1', '', '1', '1', '', '', '1')")
        # session.execute("INSERT INTO c_user VALUES (NULL, '6b4f9f85012b304979c94" + mobile[i] + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', \'" + mobile[i] + "\', '', '', '1', '1977-07-17', '', '', '投资大师" + mobile[i] + "\', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32')")
        session.commit()
        cuser = session.execute("select * from c_user where loginmobile = " + mobile[i]).first()
        if(cuser != None):
            session.execute("update c_user set client_id = 'imaster_" + str(cuser.id) + "\' where loginmobile = \'" + mobile[i] + "\'")
            session.commit()
        session.execute("delete from sd_customer where fund_account = \'" + cust_id[i] + "\'")
        session.commit()
        session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'" + cust_id[i] + "\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'" + mobile[i] + "\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
        session.commit()
        cuser_id = session.execute("select * from c_user where loginmobile = \'" + mobile[i] + "\'").first().id
        session.execute("delete from trade_fund_account where c_user_id = \'" + str(cuser_id) + "\' or cust_id = \'" + cust_id[i] + "\'")
        session.commit()
        session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', \'" + cust_id[i] + "\',  \'" + cust_id[i] + "\', \'" + mobile[i] + "\', '0.00015000', '0.00000', '投资大师" + mobile[i] + "\', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '2016-03-20 15:24:45', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
        session.commit()
    session.close()


#添加Capp用户
def insert_cuser(phone):
    session = db_session()
    session.execute("delete from c_user where loginmobile = \'" + str(phone) + "\'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', \'" + str(phone) + "\', '', '', '1', '1977-07-17', '', '', '投资大师" + str(phone) + "\', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '1', '', '1', '', '', '', '')")
    session.commit()
    cuser = session.execute("select * from c_user where loginmobile = " + str(phone)).first()
    if(cuser != None):
        session.execute("update c_user set client_id = 'imaster_" + str(cuser.id) + "\' where loginmobile = \'" + str(phone) + "\'")
        session.commit()
    session.execute("delete from sd_customer where fund_account = \'" + str(phone) + "\'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'" + str(phone) + "\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'" + str(phone) + "\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = \'" + str(phone) + "\'").first().id
    session.execute("delete from trade_fund_account where c_user_id = \'" + str(cuser_id) + "\' or cust_id = \'" + str(phone) + "\'")
    session.commit()
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', \'" + str(phone) + "\', \'" + str(phone) + "\', '0.00015000', '0.00000', '投资大师" + str(phone) + "\', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    session.close()

#构造推荐链:1-个人，2-考场，3-机构，4-Capp
def invite_code(recommandphone, recommandedphone, relation):
    session = db_session()
    if(relation == 1):
        insert_buser(recommandphone)
        result = session.execute("select * from b_user WHERE mobilephone = \'" + str(recommandphone) + "\'").first()
        bid = result.bid
        nickname = result.nickname
        invite_code = random_code(5)
        session.execute("DELETE FROM sys_share_link WHERE user_code = \'" + str(bid) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_link VALUES (NULL, 'http://w.url.cn/s/abcdefg', \'" + nickname + "\', \'" + str(bid) + "\', \'" + str(recommandphone) + "\', '1', 'e717196e2218cd1f23e118d744a7bc21', \'" + invite_code + "\', '0', '0', '0', '0', '0', '0', '1', '2016-03-16 15:14:00', '2016-03-23 19:42:43', '0')")
        session.commit()
        link_id = session.execute("SELECT * from sys_share_link WHERE user_code = \'" + str(bid) + "\' and product_type_id = '1'").first().link_id
        session.execute("DELETE FROM sys_share_relation WHERE mobilephone = \'" + str(recommandedphone) + "\' AND product_type_id = '1' AND bid = \'" + str(bid) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + str(bid) + "\', \'" + str(link_id) + "\', '1', \'" + str(recommandedphone) + "\', '1000', '100', '2016-03-16 15:15:11', '2016-03-23 18:01:05', '0', '0')")
        session.commit()
        session.execute("DELETE FROM b_user WHERE mobilephone = \'" + str(recommandedphone) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(recommandedphone) + "\', '推荐', '1', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(recommandedphone) + "\', '0.0015', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', '0', '2010', '', '1', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '0', '2', '1', '2', '-1', '0', '推荐', '', '0', NULL, '', '0', '0', '1', '1', '08310001', '2016-04-26 21:46:04', '2')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(recommandedphone) + "\' where mobilephone = \'" + str(recommandedphone) + "\'")
        session.commit()
    elif(relation == 2):
        insert_orgnization(recommandphone, 1)
        result = session.execute("SELECT * from o_user WHERE c_mobilephone = \'" + str(recommandphone) + "\'").first()
        bid = result.oid
        nickname = result.oname
        invite_code = random_code(5)
        session.execute("DELETE FROM sys_share_link WHERE user_code = \'" + str(bid) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_link VALUES (NULL, 'http://w.url.cn/s/abcdefg', \'" + nickname + "\', \'" + str(bid) + "\', \'" + str(recommandphone) + "\', '1', 'e717196e2218cd1f23e118d744a7bc21', \'" + invite_code + "\', '0', '0', '0', '0', '0', '0', '1', '2016-03-16 15:14:00', '2016-03-23 19:42:43', '20')")
        session.commit()
        link_id = session.execute("SELECT * from sys_share_link WHERE user_code = \'" + str(bid) + "\' and product_type_id = '1'").first().link_id
        session.execute("DELETE FROM sys_share_relation WHERE mobilephone = \'" + str(recommandedphone) + "\' AND product_type_id = '1' AND bid = \'" + str(bid) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + str(bid) + "\', \'" + str(link_id) + "\', '1', \'" + str(recommandedphone) + "\', '1000', '100', '2016-03-16 15:15:11', '2016-03-23 18:01:05', '20', '0')")
        session.commit()
        session.execute("DELETE FROM b_user WHERE mobilephone = \'" + str(recommandedphone) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(recommandedphone) + "\', '推荐', '1', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(recommandedphone) + "\', '0.0015', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', '0', '2010', '', '1', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '0', '2', '1', '2', '-1', '0', '推荐', '', '0', NULL, '', '0', '0', '1', '1', '08310001', '2016-04-26 21:46:04', '2')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(recommandedphone) + "\' where mobilephone = \'" + str(recommandedphone) + "\'")
        session.commit()
    elif(relation == 3):
        insert_orgnization(recommandphone, 2)
        result = session.execute("SELECT * from o_user WHERE c_mobilephone = \'" + str(recommandphone) + "\'").first()
        bid = result.oid
        nickname = result.oname
        invite_code = random_code(5)
        session.execute("DELETE FROM sys_share_link WHERE user_code = \'" + str(bid) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_link VALUES (NULL, 'http://w.url.cn/s/abcdefg', \'" + nickname + "\', \'" + str(bid) + "\', \'" + str(recommandphone) + "\', '1', 'e717196e2218cd1f23e118d744a7bc21', \'" + invite_code + "\', '0', '0', '0', '0', '0', '0', '1', '2016-03-16 15:14:00', '2016-03-23 19:42:43', '10')")
        session.commit()
        link_id = session.execute("SELECT * from sys_share_link WHERE user_code = \'" + str(bid) + "\' and product_type_id = '1'").first().link_id
        session.execute("DELETE FROM sys_share_relation WHERE mobilephone = \'" + str(recommandedphone) + "\' AND product_type_id = '1' AND bid = \'" + str(bid) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + str(bid) + "\', \'" + str(link_id) + "\', '1', \'" + str(recommandedphone) + "\', '1000', '100', '2016-03-16 15:15:11', '2016-03-23 18:01:05', '10', '0')")
        session.commit()
        session.execute("DELETE FROM b_user WHERE mobilephone = \'" + str(recommandedphone) + "\'")
        session.commit()
        session.execute("INSERT INTO b_user VALUES (NULL, '6b4f9f85012b304979c94" + str(recommandedphone) + "\', '推荐', '1', '1', '汉', '0000-00-00 00:00:00', '2011-02-18 00:00:00', '2031-02-18 00:00:00', '阳江市公安局', '310108197801134859', '上海市杨浦区政立路1585弄36号302室', '', '', '', 'd439b49d158c3424a623c3cc22a4f3c0', '', \'" + str(recommandedphone) + "\', '0.0015', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', '0', '2010', '', '1', '4', '2015-09-10 17:54:52', '2015-09-18 14:57:37', '0000-00-00 00:00:00', '', '123456', '123456', '123456', '0', '', '0', '861770969@qq.com', '上海市杨浦区政立路1585弄36号302室', 'd6a0078df5f56793f0fbb5babcc631f5', 'd6a0078df5f56793f0fbb5babcc631f5', '0', '0', '0', '', '1', '0', '2', '1', '2', '-1', '0', '推荐', '', '0', NULL, '', '0', '0', '1', '1', '08310001', '2016-04-26 21:46:04', '2')")
        session.commit()
        session.execute("update b_user set client_id = 'kingbroker_6b4f9f85012b304979c94" + str(recommandedphone) + "\' where mobilephone = \'" + str(recommandedphone) + "\'")
        session.commit()
    elif(relation == 4):
        insert_buser(recommandphone)
        result = session.execute("SELECT * FROM b_user WHERE mobilephone = \'" + str(recommandphone) + "\'").first()
        bid = result.bid
        nickname = result.nickname
        invite_code = random_code(5)
        session.execute("DELETE FROM sys_share_link WHERE user_code = \'" + str(bid) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_link VALUES (NULL, 'http://w.url.cn/s/abcdefg', \'" + nickname + "\', \'" + str(bid) + "\', \'" + str(recommandphone) + "\', '2', 'e717196e2218cd1f23e118d744a7bc21', \'" + invite_code + "\', '0', '0', '0', '0', '0', '0', '1', '2016-03-16 15:14:00', '2016-03-23 19:42:43', '0')")
        session.commit()
        link_id = session.execute("SELECT * from sys_share_link WHERE user_code = \'" + str(bid) + "\' and product_type_id = '2'").first().link_id
        session.execute("DELETE FROM sys_share_relation WHERE mobilephone = \'" + str(recommandedphone) + "\'  AND product_type_id = '2' AND bid = \'" + str(bid) + "\'")
        session.commit()
        session.execute("INSERT INTO sys_share_relation VALUES (NULL, \'" + str(bid) + "\', \'" + str(link_id) + "\', '2', \'" + str(recommandedphone) + "\', '1000', '100', '2016-03-16 15:15:11', '2016-03-23 18:01:05', '0', '0')")
        session.commit()
    session.close()
    return invite_code




#构造考场机构/合作机构:1-考场机构，2-合作机构
def insert_orgnization(phone, type):
    session = db_session()
    if(type == 1):
        session.execute("DELETE FROM o_user WHERE c_mobilephone = \'" + str(phone) + "\'")
        session.commit()
        session.execute("INSERT INTO o_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '1',  '考场" + str(phone) + "\', '', '', \'" + str(phone) + "\', 'e10adc3949ba59abbe56e057f20f883e', '0', '1', '2016-04-07 00:14:20', '2016-04-07 00:14:20', '20', '', '', \'" + str(phone) + "\', '联系人" + str(phone) + "\', '0', '0', '', '', '', 'jzsecogn_6b4f9f85012b304979c94" + str(phone) + "\')")
        session.commit()
    elif(type == 2):
        session.execute("DELETE FROM o_user WHERE c_mobilephone = \'" + str(phone) + "\'")
        session.commit()
        session.execute("INSERT INTO o_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '1', '机构" + str(phone) + "\', '', '', \'" + str(phone) + "\', 'e10adc3949ba59abbe56e057f20f883e', '0', '1', '2016-04-07 00:14:20', '2016-04-07 00:14:20', '10', '', '', \'" + str(phone) + "\', '联系人" + str(phone) + "\', '0', '0', '', '', '', 'jzsecogn_6b4f9f85012b304979c94" + str(phone) + "\')")
        session.commit()

#随机产生邀请码
def random_code(i):
    code = ''
    for j in range(0, i):
        k = random.randint(1, 3)
        if(k == 1):
            code += str(chr(random.randint(48, 57)))
        elif(k == 2):
            code += str(chr(random.randint(97, 122)))
        elif(k == 3):
            code += str(chr(random.randint(65, 90)))
    return code

#禁用基准照
def uncheckmugshot(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    result = session.execute("select * from b_user_certificate where bid = \'" + str(bid) + "\' and cer_type = '901'").fetchall()
    if(result != None):
        session.execute("delete from b_user_certificate where bid = \'" + str(bid) + "\' and cer_type = '901'")
        session.commit()
    session.execute("insert into b_user_certificate values(NULL, '" + str(bid) + "', '1', '2016-04-27 12:00:51', '2016-04-27 12:00:51', '901', 'a19bdd967145ce8a7b90dbd1d358d292', NULL)")
    session.commit()
    session.close()

#禁用身份证过期提醒
def uncheckdailymsg_id(phone):
    session = db_session()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    session.execute("update b_message set notice = '0' and is_bapp_sync = '1' where b_userid = \'" + str(bid) + "\' and type = '3'")
    session.commit()
    session.close()

def get_buser_password(phone):
    session = db_session()
    password = session.execute("select * from b_user where mobilephone = " + str(phone)).first().password
    session.close()
    return password



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #扫描题库
    # scan_question()
    #增加Bapp经纪人
    # insert_buser(15210262169)
    # insert_buser(15210262170)
    # insert_buser(15210262171)
    # insert_buser(15210262172)
    # insert_buser(15210262173)
    #删除Bapp经纪人
    # del_buser(18001284533)
    #修改培训时间
    # train_time_start(18610640885)
    # train_time_end(18610640885)
    #构造KPI数据
    # KPI(18001284533)
    #构造业绩数据
    # trade_commission(15210262169, 1)
    # trade_commission(15210262170, 2)
    # trade_commission(15210262171, 3)
    # trade_commission(15210262172, 4)
    # trade_commission(15210262173, 5)
    #构造推荐列表
    # share_relation(18001284533)
    #获取KPI信息
    # print get_kpi_info(15210262168)
    #获取交易数据
    # print get_trade_commission(15210262169)
    #获取收入数据
    # print get_income_info(15210262169)
    #添加经纪人
    # insert_buser(15210262173)
    #取消微信公众号绑定
    # logout_bwx(18611358845)
    #删除考场活动准考证附件
    # del_attachment(18611358845)
    #构造我的客户
    # mine_customer(15210262169, 13300000001)
    # mine_customer(15210262169, 13300000002)
    # mine_customer(15210262170, 13300000003)
    # mine_customer(15210262171, 13300000004)
    # mine_customer(15210262172, 13300000005)
    # mine_customer(15210262172, 13300000006)
    # mine_customer(15210262173, 13300000007)
    # mine_customer(15210262173, 13300000008)
    #删除推荐关系
    # del_share_relation(15501253283)
    #构造可提现金额
    # cash_count(13212345671)
    #删除客户
    # del_customer(18001284500)
    #构造推荐列表
    # share_relation_status(15313717521)
    #构造客户列表
    # add_customer(18001284500)
    #构造不同挂靠状态的经纪人
    # broker_status(18900000001, 'register')
    # broker_status(18900000002, 'id_loaded')
    # broker_status(18900000003, 'id_fail')
    # broker_status(18900000004, 'id_pass')
    # broker_status(18900000005, 'exam_fail')
    # broker_status(18900000006, 'exam_pass')
    # broker_status(18900000007, 'train_ready')
    # broker_status(18900000008, 'train_pass')
    # broker_status(18900000009, 'contract_ready')
    # broker_status(18900000010, 'contract_pass')
    # broker_status(18900000011, 'sac_pass')
    # broker_status(18900000012, 'quiet_register')
    #获取本月考核数据
    # print get_current_mon_info(15210262169)
    #获取本月客户交易额数据
    # print get_current_trade_commission(15210262170)
    #获取本月推荐奖数据
    # print get_current_recommand_info(15210262171)
    #禁用基准大头照
    # uncheckmugshot(15210262168)
    #禁用身份证过期提醒
    # uncheckdailymsg_id(15210262168)
    #获取经纪人密码
    # print get_buser_password(15210262168)


    # uploadid_status(15210262168)
    # approve_id(15210262168)
    # print train_question(15210262168)
    # print train_question_count(15210262168)[0]
    # print chapter_status(1, 1, 15210262168)
    # print chapter_status(1, 2, 15210262168)
    # sign_contract(15210262168)
    # print broker_name(15210262168)
    # print len(user_info(15311578835))
    # print uploadid_status(15210262168)
    # if(user_customer(15210262168)[1][2] == unicode('张三','utf-8')):
    #     print 'ok'
    # for i in range(0, 5):
    #     print user_customer(15210262168)[i][2]
    # print len(user_follow_done(15210262168, user_customer(15210262168)[0][1]))
    # print user_customer(15210262168)[1][1]
    # for i in range(0, 5):
    #     print user_customer(15210262168)[i][2]
    #     print customer_status(15210262168, user_customer(15210262168)[i][1])
    # del_customer(15210262168)
    # print user_customer(15210262168, 18001284533)
    # if(broker_customer(15210262168) == []):
    #     print 'ok'
    # if(broker_customer(15210262168) != []):
    #     print 'no'
    # print broker_customer(15210262168)
    # print broker_info(15210262168)
    # other_customer()
    # mine_customer(18001284533, 13300000041)
    # print customer_follow_count('8653306360887dae241b320aaab157128efa8b4649064c998dccb74e3506dd56')
    # print broker_info(15210262168)[0][44]
    # print get_department(15210262168)
    # print get_contract_time(15210262168)
    # print cash_count(15210262168)
    # share_relation_status(18611358845)
    # print invite_code(12300000000, 15210262166, 1)