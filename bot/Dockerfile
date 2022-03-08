FROM leonsec/xssbot:v1

#WORKDIR /var/xssbot/

# 复制文件和目录
COPY ./bot.py /var/xssbot/
COPY ./conf.yaml /var/xssbot/
COPY ./run.sh /
# RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
# RUN pip3 install yaml -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip2 install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip2 install ruamel.yaml==0.15.98 -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD  /run.sh 