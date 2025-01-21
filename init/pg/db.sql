create table if not exists public.health_check (
    status TEXT,
    created timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

insert into public.health_check (status)
values ('ready')
;
