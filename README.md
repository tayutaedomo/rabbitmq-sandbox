# rabbitmq-sandbox
RabbitMQ と Python を使った検証

## 試したこと
- [x] docker (docker-compose) での RabbitMQ の起動
- [x] poetry 環境の構築
- [x] シンプルな publish & subscribe
- [x] RabbitMQ を使った pytest でのテスト
- [x] モックを使った pytest
- [x] 手動 ACT での subscribe
- [x] TTL でのメッセージの削除
- [x] 手動 ACT でのキューへの再登録とリトライ上限
- [ ] Maxlen でのキューの登録上限
