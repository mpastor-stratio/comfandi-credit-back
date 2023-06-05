#docker rmi camiloriguer/ingesta 
#docker build -f Dockerfile -t credito_web:5.0 . 
#sudo docker run credito_web:3.0
#sudo docker ps -ls
#sudo docker rm id_ejecucion
#sudo docker rmi id_imagen
#sudo docker run credito_web:2.0
#docker push camiloriguer/ingesta
# sudo docker run -p 5000:5000 credito_web:5.0

FROM python:3.8-slim

WORKDIR /web_page


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN export FLASK_APP=app.py
RUN export FLASK_DEBUG=1
COPY . .
RUN chmod -R 400 certis/usuario-pg-analitica.key
RUN chmod -R 400 certis/usuario-pg-analitica.crt
RUN chmod -R 400 certis/postgresCA.crt
RUN chmod -R 400 certis/cert.pem
RUN chmod -R 400 certis/key.pem

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "--certfile", "certis/cert.pem", "--keyfile", "certis/key.pem", "wsgi:app"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"] 
