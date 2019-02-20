作业:
    1.把/etc/passwd 导入到数据表　userinfo
create database db1;

use db1;

create table userinfo(
yonghu varchar(20),
mima varchar(20),
uid int,
gid int,
tarena varchar(30),
zhuml varchar(200),
denglml varchar(200)
)charset=utf8;

alter table userinfo modify tarena varchar(200);

show variables like 'secure_file_priv'

sudo cp /etc/passwd  /var/lib/mysql-files/;

load data infile "/var/lib/mysql-files/passwd"
into table userinfo
fields terminated by ":"
lines terminated by "\n";

    2.在userinfo表的第一列添加１个id 字段，主键，自增长，显示
    宽度为３，位数不够用０填充

alter table userinfo add id int(3) zerofill primary key auto_increment first;




select * from userinfo