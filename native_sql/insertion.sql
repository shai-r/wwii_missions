insert into Countries (country_name)
select distinct target_country
FROM mission
where target_country is not NULL
on conflict (country_name) do nothing;

insert into Cities (city_name, country_id, latitude, longitude)
select distinct
    m.target_city,
    c.country_id,
    m.target_latitude::decimal,
    m.target_longitude::decimal
from mission m
join Countries c on m.country = c.country_name
where m.target_city is not null
on conflict (city_name) do nothing;

insert into TargetTypes (target_type_name)
select distinct target_type
from mission
where target_type is not null
on conflict (target_type_name) do nothing;

insert into Targets (target_industry, target_priority, city_id, target_type_id)
select distinct
    m.target_industry,
	m.target_priority::integer,
    ci.city_id,
    tt.target_type_id
from mission m
inner join Cities ci on m.target_city = ci.city_name
inner join TargetTypes tt on m.target_type = tt.target_type_name
where m.target_id is not NULL and m.target_industry is not null
on conflict (target_id) do nothing;