#!/bin/sh
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Aguardando pela inicialização do Banco de Dados Postgres ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Banco de Dados Postgres Iniciado com sucesso ($POSTGRES_HOST:$POSTGRES_PORT)"