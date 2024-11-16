# Хрононимы Костромской области

Этот проект посвящен картографированию хрононимов Костромской области для их изучения в рамках научной деятельности кафедры русского языка, общего языкознания и речевой коммуникации Уральского Федерального универсетита. Все данные, которые представлены в репозитории являются интеллектуальной собственностью топонимической лаборатории кафедры.

```dockerfile
FROM ubuntu  
RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-pip sqlite3 git
RUN apt install -y python3-flask 
WORKDIR /root
RUN git clone https://github.com/zeshi09/kaf.git
WORKDIR /root/kaf
ENTRYPOINT flask run --host="0.0.0.0" --port=5000
```
