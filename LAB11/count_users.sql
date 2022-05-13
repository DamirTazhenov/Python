CREATE OR REPLACE FUNCTION totalusers(db_name text)
returns integer 
as 
$$
declare 
	total integer;
BEGIN 
   SELECT count(*) into total 
   FROM db_name;   
   RETURN total; 
END; 
$$
language plpgsql
--Select totalusers());  
