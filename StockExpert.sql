drop table if exists experts;
create table experts(
	id integer primary key autoincrement,
	expert_name varchar(80) not null,
	expert_email varchar(120) unique not null,
	expert_score integer null,
	expert_details text null
);

drop table if exists companies;
create table companies(
	id integer primary key autoincrement,
	company_name varchar(80) not null,
	company_website varchar(120) unique null,
	company_details text null
);

drop table if exists variable_type;
create table variable_type(
	variable_name varchar(100) primary key
);

drop table if exists expert_reviews;
create table expert_reviews(
	id integer primary key autoincrement,
	expert_id integer REFERENCES experts(id),
	company_id integer REFERENCES companies(id),
	variable_name varchar(100) REFERENCES variable_type(variable_name),
	upper_bound_value integer not null,
	lower_bound_value integer not null,
	created_date varchar(50)not null,
	created_time varchar(50) not null
);
