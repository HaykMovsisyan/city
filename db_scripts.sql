create table category
(
    id   serial,
    name varchar
);

create table product
(
    id  integer not null
        constraint unique_product_id
            unique,
    name          varchar,
    category_name varchar,
    photo_url     varchar
);

create table price
(
    id             serial
        primary key,
    product_id     integer,
    price          double precision,
    discount_price double precision,
    timestamp      timestamp default now() not null
);