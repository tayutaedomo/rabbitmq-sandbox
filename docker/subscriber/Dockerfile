FROM python:3.9

RUN pip install poetry

WORKDIR /app

# Poetry
# 依存関係のインストールを高速化するためにビルド時の仮想環境の作成を無効化
ENV POETRY_VIRTUALENVS_CREATE=false
# 変更を最小限とするために最低限のファイルのみのコピーとする
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

COPY . .
CMD ["python", "-u", "./rabbitmq_sandbox/subscribe_auto_ack_docker.py"]
