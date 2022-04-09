FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Skyla-Userbot https://github.com/Cangcimenn/Skyla-Userbot /home/Skyla-Userbot/ \
    && chmod 777 /home/Skyla-Userbot \
    && mkdir /home/Skyla-Userbot/bin/
WORKDIR /home/Skyla-Userbot/
COPY ./sample_config.env ./config.env* /home/Skyla-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
