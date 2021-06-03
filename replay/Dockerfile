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
  libwebsockets-dev \
  python3 \
  python3-pip
RUN pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir prompt_toolkit
RUN git clone https://github.com/tsl0922/ttyd
RUN mkdir ttyd/build \
  && cd ttyd/build \
  && cmake .. \
  && make install
RUN cd / \
  && rm -r ttyd
RUN apt remove -y \
  build-essential \
  cmake \
  git \
  && apt autoremove -y \
  && apt autoclean
COPY ./ /data
COPY play /usr/local/bin/
RUN chown root:root /usr/local/bin/play
RUN chmod 755 /usr/local/bin/play
RUN useradd -ms /bin/bash term
USER term
WORKDIR /home/term
EXPOSE 3000
CMD play
