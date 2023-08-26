FROM python:3.8.10-slim
WORKDIR /xsb

# install python dependencies and expose port
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000

# copy directories
COPY templates templates
COPY helpers helpers
COPY static static
COPY data data
COPY app.py app.py
COPY start.sh start.sh

# start server
CMD ["./start.sh"]