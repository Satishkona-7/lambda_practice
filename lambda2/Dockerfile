FROM public.ecr.aws/lambda/python:3.12

COPY common/ ${LAMBDA_TASK_ROOT}/common/

COPY lambda2/src/ ${LAMBDA_TASK_ROOT}/

COPY lambda2/requirements.txt .

RUN pip install -r requirements.txt

CMD ["app.lambda_handler"]