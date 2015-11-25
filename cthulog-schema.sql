CREATE TABLE if not exists cthulog(stamp timestamp default current_timestamp not null, author varchar(128), title varchar(256), content text);
