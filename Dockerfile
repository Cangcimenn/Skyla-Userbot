FROM vckyouuu/geezprojects:buster

RUN git clone -b Skyla-Userbot https://github.com/Cangcimenn/Skyla-Userbot  /home/userbot/ \
    && chmod 777 /home/Skyla-Userbot \
    && mkdir /home/Skyla-Userbot/bin/

WORKDIR /home/userbot/

CMD [ "bash", "start" ]
