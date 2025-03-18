FROM ubuntu:24.04
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install socat python3
RUN useradd -m user
WORKDIR /home/user
COPY chall .
COPY run.py .
RUN echo 'FMCTF{ee50454652a4496e0fd80e6919f6ca28}' > /flag
RUN chown -R root:root /home/user
RUN chmod -R 555 /home/user
CMD ["socat", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:'su user -c ./run.py'"]
