create table if not exists author(
    id int primary key auto_increment,
    name varchar(20) default 'Hit9',
    email varchar(30) default '',
    description varchar(100) default '',
    url varchar(100) default ''
) engine=innodb default charset=utf8;


create table if not exists blog(
    id int primary key auto_increment,
    name varchar(40) default '',
    description varchar(100) default '',
    disqus varchar(40) default ''
) engine=innodb default charset=utf8;


create table if not exists post(
    id int primary key auto_increment,
    title varchar(40),
    title_pic varchar(100) default '',
    datetime datetime,
    body text,
    published tinyint default 0
) engine=innodb default charset=utf8;


create table if not exists admin(
    id int primary key auto_increment,
    passwd varchar(33)
) engine=innodb default charset=utf8;


/* initialize data */

insert into admin set passwd='21232f297a57a5a743894a0e4a801fc3'; /* default passwd: admin */
insert into blog set name='Ihybits By Florije', description='ToBe && ToDo';
insert into author set name='Florije', url='http://ihybits.com/', email='florije1988@gmail.com';
insert into post set title='Hello World!', body='**Hello world!**', title_pic='http://image.xinli001.com/20131112/173544f582b307f22319cc.jpg',
datetime = '2014-1-11 11:11:11', published=1;
