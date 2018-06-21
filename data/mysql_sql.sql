SELECT * FROM coinradar.focuscoin;
select * from coinradar.coinbasicinfo;

create table coinradar.exchange(exname varchar(255) unique ) ;

select * from coinradar.exchange;
select count(1) from coinradar.exchange;

insert into coinradar.exchange(exname) values('OKEx');

delete from coinradar.exchange where exname = 'ACX' or exname = 'OKEx';

drop table coinradar.exchange;


