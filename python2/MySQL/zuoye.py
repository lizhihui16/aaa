
select user_id count(user_id) from comment
group by user_id 
order by count(user_id) DESC
limit 10










create table customers(
c_id int primary key auto_increment,
c_name varchar(20),
c_age tinyint unsigned,
c_sex enum('M','F'),
c_city varchar(20),
c_salary float(12,2)
);

insert into customers values
(1,'Zhangsan',25,'M','Beijing',8000),
(2,'Lisi',30,'F','Sahnghai',10000),
(3,'Wangwu',27,'M','Shenzhen',8000);



create table orders(
o_id int,
o_name varchar(30),
o_price float(12,2),
foreign key(o_id)
references customers(c_id)
on delete cascade
on update cascade
);

insert into orders values
(1,"iphone",5288),
(1,"ipad",3299),
(3,"mate9",3688),
(2,"iwatch",2222),
(2,"r11",4400);


select * from customers 
where c_salary>4000 or c_age<29
limit 2;

update customers set c_salary=c_salary*1.15
where c_age>=25 
and (c_city='beijing' or c_city='shanghai')
#c_city in('beijing','shanghai')

select * from customers
where c_city='beijing'
order by c_salary DESC 
limit 1

select * from customers
order by c_salary limit 1;

select * from customers 
inner join orders  on c_salary>5000
and c_id=o_id;
#或
select * from customers where
o_id in(select c_id from customers where 
c_salary>5000);




alter table orders drop foreign key o_id;


