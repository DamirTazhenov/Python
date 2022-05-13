create or replace function getAll(lim integer, ofs integer )
    returns setof phonebook
as
$$
begin
    return query
        select * from phonebook limit $1 offset $2;
end;
$$ language plpgsql;