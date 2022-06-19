drop table if exists links;

create table links (
    id integer primary key autoincrement,
    original_url text not null,
    short_id text not null,
    views_amount int not null
);
