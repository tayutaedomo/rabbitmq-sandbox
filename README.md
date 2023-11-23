# rabbitmq-sandbox
RabbitMQ と Python を使った検証

## 試したこと
- [x] docker (docker-compose) での RabbitMQ の起動
  - `npm run compose:up`
  - `npm run open:admin`
  - `npm run compose:down`
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
