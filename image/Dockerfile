FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash ednonlabs

RUN mkdir -p /opt/ednonhackaboss
COPY --chown=ednonlabs:root ednonhackaboss/ /opt/ednonhackaboss/
COPY --chown=ednonlabs:root image/entrypoint/initdb.sh /opt/ednonhackaboss/
RUN chmod 755 /opt/ednonhackaboss/initdb.sh
WORKDIR /opt/ednonhackaboss

RUN pip install -r requirements.txt

USER ednonlabs
EXPOSE 8000

ENTRYPOINT ["/opt/ednonhackaboss/initdb.sh"]