FROM python:3.10.0b2
COPY . /logica
WORKDIR /logica
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
ENTRYPOINT ["python"]
CMD ["k-means.py"]