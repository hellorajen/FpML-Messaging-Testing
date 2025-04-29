FROM python:3.9
RUN pip install lxml
COPY fpml_server.py fpml-5-10.xsd ./
CMD ["python", "fpml_server.py"]