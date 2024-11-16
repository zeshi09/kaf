# Хрононимы Костромской области

Этот проект посвящен картографированию хрононимов Костромской области для их изучения в рамках научной деятельности кафедры русского языка, общего языкознания и речевой коммуникации Уральского Федерального универсетита. Все данные, которые представлены в репозитории являются интеллектуальной собственностью топонимической лаборатории кафедры.

```dockerfile
FROM ubuntu  
RUN apt udpate && apt upgrade -y
RUN apt install -y python3 python3-pip sqlite3 git
RUN pip3 install flask 
RUN git clone https://github.com/zeshi09/kaf.git
RUN cd kaf
ENTRYPOINT FLASK_APP=/root/kaf/app.py flask run --host=0.0.0.0 --port=5000
```
