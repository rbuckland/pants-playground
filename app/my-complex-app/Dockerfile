FROM python:3.11 as base

COPY /*.whl /tmp

# we need to install the wheel from our private pypi
RUN pip install /tmp/*.whl && \
    rm /tmp/*.whl
