create table if not exists records (
    id serial primary key,
    text text not null,
    create_at timestamp default current_timestamp
);

create table if not exists public.health_check (
    status text,
    created timestamp with time zone default current_timestamp
);

insert into public.health_check (status)
values ('ready')
;
