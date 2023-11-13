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
- [x] 手動 ACT での subscribe
  - 未確認メッセージの発生と確認
  - `npm run publish:auto_act "message"`
  - `npm run publish:auto_act "raise_error"`
  - `npm run subscribe_auto_act`
- [x] TTL でのメッセージの削除
- [x] 手動 ACT でのキューへの再登録とリトライ上限
  - `npm run publish:auto_act "raise_error"`
  - `npm run subscribe:auto_act:2`
- [x] Maxlen でのキューの登録上限
  - `npm run publish:max_len "message1"`
  - `npm run publish:max_len "message2"`
  - `npm run publish:max_len "message3"`
  - `npm run subscribe:max_len`
