FROM ubuntu:24.04
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install socat
RUN useradd -m user
WORKDIR /home/user
COPY chall .
RUN echo 'FMCTF{test-flag}' > /flag
RUN chown -R root:root /home/user
RUN chmod -R 555 /home/user
CMD ["socat", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:'su user -c ./chall'"]
