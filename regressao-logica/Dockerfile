FROM python:3
COPY . /logica
WORKDIR /logica
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
ENTRYPOINT ["python"]
CMD ["regressao-logica-xy.py"]