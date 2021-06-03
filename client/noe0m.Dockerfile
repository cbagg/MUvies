FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y \
  build-essential \
  zlib1g-dev \
  libpcre3-dev \
  libgnutls28-dev \
  cmake \
  git \
  libjson-c-dev \
  libwebsockets-dev
RUN git clone https://github.com/scandum/tintin
RUN git clone https://github.com/tsl0922/ttyd
RUN mkdir ttyd/build \
  && cd ttyd/build \
  && cmake .. \
  && make install
COPY noe0m.patch /tintin/
RUN cd /tintin \
  && patch -p1 < noe0m.patch
RUN cd /tintin/src \
  && ./configure \
  && make install
RUN cd / \
  && rm -r tintin ttyd
RUN apt remove -y \
  build-essential \
  cmake \
  git \
  && apt autoremove -y \
  && apt autoclean
COPY webtin /usr/local/bin/
RUN chown root:root /usr/local/bin/webtin
RUN chmod 755 /usr/local/bin/webtin
RUN useradd -ms /bin/bash term
USER term
WORKDIR /home/term
EXPOSE 3000
CMD ["webtin"]
