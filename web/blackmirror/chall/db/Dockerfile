FROM mysql:9.0

COPY setup.sql /tmp/setup.sql
RUN sed -i "s/%REDACTED_TABLE_NAME%/FLAG_`cat /dev/urandom | head -c 12 | od -A n -v -t x1  | tr -d \" \n\"`/g" /tmp/setup.sql
RUN sed -i "s/%FLAG_REDACTED%/MOTORI{SOME_L33T_HERE}/g" /tmp/setup.sql
RUN mv /tmp/setup.sql /docker-entrypoint-initdb.d/
RUN chmod -R 775 /docker-entrypoint-initdb.d