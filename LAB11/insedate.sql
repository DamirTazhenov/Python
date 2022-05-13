create or replace procedure add_update_user(
	usname varchar,
	phonumber varchar
)
as $$
declare
exist varchar;
begin
    update phonebook_lab11
    set phone_number = $3
    where (phonebook.usname = $1);
    IF NOT FOUND THEN
        insert into phonebook_lab11(usname,phonumber) values ($1, $2);
    END IF;
end;
$$
language plpgsql