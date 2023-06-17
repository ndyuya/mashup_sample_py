FROM python:3.11.4-alpine3.18

ARG project_dir=/web/project

ADD project $project_dir
ADD requirements.txt $project_dir

WORKDIR $project_dir
RUN pip install -r requirements.txt

CMD ["python","main.py"]
