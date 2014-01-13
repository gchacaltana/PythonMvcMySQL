PythonMvcMySQL
==============

Example describes how to use Python with MySQL.

Database example:

```sql
create database bookstore charset 'utf8';

create table categories (id_category int not null auto_increment primary key,name varchar(45) not null);

create table books (id_book bigint not null auto_increment primary key, id_category int not null, name varchar(200) not null, price decimal(7,2) default 0,date_created datetime);
```
