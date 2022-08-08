db_config = {
    "host": "localhost",
    "username": "docker",
    "password": "docker",
    "database": "exampledb"
}


db_queries = {
    'get_rates': "SELECT \
	CASE WHEN a.count < 3 THEN null ELSE a.price END AS price, \
	d.day, \
	a.count \
FROM \
( \
	SELECT ( \
		generate_series( \
			%(date_from)s, %(date_to)s, '1 day'::interval \
		) \
	)::date as day \
) d \
LEFT OUTER JOIN ( \
	SELECT AVG(price) AS price, day, COUNT(*) AS count \
	FROM prices \
	WHERE \
		(orig_code = %(origin)s or orig_code in (select code from ports where parent_slug = %(origin)s)) AND \
		(dest_code = %(destination)s or dest_code in (select code from ports where parent_slug = %(destination)s)) AND \
		day >= %(date_from)s AND \
		day <= %(date_to)s \
	GROUP BY day \
) AS a ON d.day = a.day \
ORDER BY day DESC"
}
