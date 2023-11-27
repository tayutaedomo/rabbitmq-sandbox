# rabbitmq-sandbox
RabbitMQ と Python を使った検証

## 必要なもの
- Node.js
- Docker/Docker Compose
- Python/Poetry
- direnv

## セットアップ
### git clone
```bash
$ git clone git@github.com:tayutaedomo/rabbitmq-sandbox.git
$ cd rabbitmq-sandbox
```

### 環境変数
```bash
$ cp .env.sample .env
$ direnv allow .
```

### Poetry
```bash
$ poetry install
```

## 試したこと
- [x] docker (docker-compose) での RabbitMQ の起動
  - `npm run rabbitmq:up`
  - `npm run admin:open`
  - `npm run rabbitmq:down`
- [x] poetry 環境の構築
- [x] シンプルな publish & subscribe
  - `npm run publish:hello`
  - `npm run subscribe:hello`
- [x] RabbitMQ を使った pytest でのテスト
  - `npm run test:mq`
- [x] モックを使った pytest
  - `npm run test:mock`
- [x] 手動 ACK での subscribe
  - 未確認メッセージの発生と確認
  - `npm run publish:auto_ack "message"`
  - `npm run publish:auto_ack "raise_error"`
  - `npm run subscribe:auto_ack`
- [x] TTL でのメッセージの削除
- [x] 手動 ACK でのメッセージの nack とキューへの再登録とリトライ上限
  - `npm run publish:auto_ack "raise_error"`
  - `npm run subscribe:auto_ack:2`
- [x] 手動 ACK でのメッセージの reject とキューへの再登録とリトライ上限
  - `npm run publish:auto_ack "raise_error"`
  - `npm run subscribe:auto_ack:3`
- [x] Max length でのキューの登録上限
  - `npm run publish:max_len "message1"`
  - `npm run publish:max_len "message2"`
  - `npm run publish:max_len "message3"`
  - `npm run subscribe:max_len`
- [x] GitHub Actions での pytest 実行
- [x] docker コンテナで subscribe を起動
  - `npm run subscriber:up`
  - `npm run subscriber:publish "message"`
  - `npm run subscriber:down`
- [x] subscriber のヘルスチェック
  - pgrep ではプロセスがハングアップしていないかどうかまでは確認できない。
- [x] キューのメッセージ数を確認するコマンド
  - `subscriber:count:grep`
  - `subscriber:count:jq`
