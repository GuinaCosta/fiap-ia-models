FROM python:3.10.0b2
COPY . /stop-app
WORKDIR /stop-app
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
ENTRYPOINT ["python"]
CMD ["statusmodel-stock.py"]