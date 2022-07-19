# libraries
import pandas
from google.cloud import bigquery

# variables
project_id = 'trans-run-356410'

# Quantos contratos (tokens) estão sendo criados por bloco?


def contrato_bloco():
    print('Questão 1:')
    print('Quantos contratos (tokens) estão sendo criados por bloco?')
    df = pandas.io.gbq.read_gbq(
        '''
    SELECT COUNT(number) as Contrato
    FROM `bigquery-public-data.crypto_ethereum.blocks`
    ''',
        project_id=project_id, dialect='standard'
    )
    print(df)
    df.to_excel('contratos.xlsx', sheet_name='contratos', index=False)

# Quantos blocos estão sendo criados em um dia?


def bloco_dia():
    print('Questão 2:')
    print('Quantos blocos estão sendo criados em um dia?')
    df = pandas.io.gbq.read_gbq(
        '''
    SELECT date(block_timestamp) AS DIA, COUNT(block_number) AS BLOCK_CREATED_DAY
    FROM `bigquery-public-data.crypto_ethereum.contracts`
    WHERE block_timestamp >= '2022-07-10'
    GROUP BY date(block_timestamp)
    LIMIT 10
    ''',
        project_id=project_id, dialect='standard'
    )
    print(df)
    df.to_excel('bloco_dia.xlsx', sheet_name='bloco_dia', index=False)

# Em relação aos últimos 15 dias, qual foi a variação na quantidade de blocos contendo tokens em um dia?


def variacao():
    print('Questão 3:')
    print('Em relação aos últimos 15 dias, qual foi a variação na quantidade de blocos contendo tokens em um dia?')
    df = pandas.io.gbq.read_gbq(
        '''
    SELECT date(block_timestamp) AS DIA, COUNT(block_number) AS BLOCK_VARIATION
    FROM `bigquery-public-data.crypto_ethereum.tokens`
    WHERE block_timestamp >= '2022-07-05' 
    GROUP BY date(block_timestamp)
    LIMIT 15
    ''',
        project_id=project_id, dialect='standard'
    )

    df.to_excel('variacao.xlsx', sheet_name='variacao', index=False)
    print(df)

# Qual o bloco que gerou contratos (tokens) e utilizou mais taxa (gas)? Informar o nome de todos os tokens contidos neste bloco


def bloco_gas():
    print('Questão 4:')
    print('Qual o bloco que gerou contratos (tokens) e utilizou mais taxa (gas)? Informar o nome de todos os tokens contidos neste bloco')
    df = pandas.io.gbq.read_gbq(
        '''
        SELECT name, A.block_timestamp, A.block_number, gas_used, transaction_count
        FROM `bigquery-public-data.crypto_ethereum.contracts` A
        INNER JOIN `bigquery-public-data.crypto_ethereum.blocks` B
        ON (
        A.block_timestamp = B.timestamp
        )
        INNER JOIN `bigquery-public-data.crypto_ethereum.transactions` C
        ON (
        A.block_hash = C.block_hash
        )
        INNER JOIN `bigquery-public-data.crypto_ethereum.tokens` D
        ON (
        B.timestamp = D.block_timestamp
        )
        WHERE A.block_timestamp >= '2022-07-10' 
        GROUP BY A.block_timestamp, A.block_number, gas_used, transaction_count, name
        ORDER BY gas_used DESC
            ''',
        project_id=project_id, dialect='standard'
    )
    # Remove timezone from columns
    df['block_timestamp'] = df['block_timestamp'].dt.tz_localize(None)
    df.to_excel('bloco_gas.xlsx', sheet_name='bloco_gas', index=False)
    print(df)


def run_all():
    contrato_bloco()
    bloco_dia()
    variacao()
    bloco_gas()


if __name__ == '__main__':
    run_all()
