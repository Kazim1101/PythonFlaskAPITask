Steps to run the api
1- Run the docker-compose.yml
    this will pull image and start the two docket container
    a- "postgres" DB container
    b- "adminer" container for connecting with postgrest DB via browzer

2- Execute the rate.sql dump in postgres DB by using below cmds
    a- cat rates.sql | docker exec -i practice_database_1 psql -U docker -d exampledb
    b- verify the result can be done by cli or adminer console
        i-  docker exec -it practice_database_1 /bin/bash -c "PGPASSWORD=docker psql --username docker exampledb" 
        ii- \dt+  (show all tables and size)

3- Run the app.py file

4- url to access => http://127.0.0.1:3000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main


Steps to Run testcase
1- Run the test_rates_api.py file

NOTE:
You can find the execute sample request on root/api_sample_requests.pdf 