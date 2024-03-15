FROM python:3.13.0a4-alpine
COPY . /app
WORKDIR /app
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
ENTRYPOINT ["python"]
CMD ["teste.py"]
EXPOSE 5000