drop table if exists pswrds;
drop table if exists roles;
drop table if exists statuses;
drop table if exists account;


create table roles
(
    id   serial primary key,
    role text
);
insert into roles (role)
values ('USER');
insert into roles (role)
values ('EMPLOYER');
insert into roles (role)
values ('ADMIN');

create table statuses
(
    id     serial primary key,
    status text
);
insert into statuses (status)
values ('LOCK');
insert into statuses (status)
values ('ACTIVE');

create table account
(
    id             serial PRIMARY KEY,
    login          text not null,
    email          text not null,
    first_name     text,
    mid_name       text,
    last_name      text,
    phone          text,
    rolesRole      text not null,
    statusesStatus text not null
);


insert into account (login, email, first_name, mid_name, last_name, phone, rolesRole, statusesStatus)
values ('Vasya', 'Vasya@mail.ru', 'Vasya', 'Vasiljevich', 'Vasin', '+7896454152', 'EMPLOYER', 'ACTIVE');
insert into account (login, email, first_name, mid_name, last_name, phone, rolesRole, statusesStatus)
values ('Petya', 'Petya@mail.ru', 'Petya', 'Petiljevich', 'Petin', '+7896546152', 'ADMIN', 'LOCK');



create table pswrds
(
    id        serial primary key,
    accountId int references account (id),
    password  text
);

