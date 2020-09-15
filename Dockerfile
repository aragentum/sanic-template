ARG PYTHON_VERSION=3.8.5
ARG PYTHON_PACKAGE=sanic_template
ARG WORKDIR=/usr/src/app

FROM python:${PYTHON_VERSION}
ARG PYTHON_PACKAGE
ARG WORKDIR

# Meta information
LABEL version="0.0.1"
LABEL description="Container with Sanic Template API service"

# Internal params
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHON_PACKAGE ${PYTHON_PACKAGE}

# Adding sanic user and group
RUN set -o errexit -o nounset \
    && echo "Adding sanic user and group" \
    && groupadd --system --gid 1000 sanic \
    && useradd --system --gid sanic --uid 1000 --shell /bin/bash --no-create-home sanic \
    && mkdir --parents ${WORKDIR} && chown -R sanic:sanic ${WORKDIR}

USER sanic

# Preparing of environment
WORKDIR ${WORKDIR}

# Add a launcher
COPY --chown=sanic:sanic ./entrypoint.sh ./
RUN chmod +x ./entrypoint.sh

# Installation of dependencies
COPY --chown=sanic:sanic ./requirements/development.txt ./requirements.txt

# Use root privilegies to install packages
USER root
RUN pip install --no-cache-dir -r ./requirements.txt
USER sanic

# Add a source code
COPY --chown=sanic:sanic ./migrations ./migrations
COPY --chown=sanic:sanic ./alembic.ini ./alembic.ini
COPY --chown=sanic:sanic ./manage.py ./manage.py
COPY --chown=sanic:sanic ./${PYTHON_PACKAGE} ./${PYTHON_PACKAGE}

# Removing of unused parts (use root privilegies)
USER root
RUN rm -rf ./requirements.txt
USER sanic

# Launcher
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000
