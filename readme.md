# Benchmark

## Results

| Endpoint                     | Framework  | Reqs/sec | Latency   | Throughput   |
|------------------------------|------------|----------|-----------|--------------|
| /records/post_pg             | FastAPI    | 634.89   | 6.33ms    | 246.93KB/s   |
|                              | Litestar   | 714.76   | 5.68ms    | 278.61KB/s   |
|                              | net/http   | 2041.79  | 1.93ms    | 787.78KB/s   |
| /records/post_ch             | FastAPI    | 184.74   | 21.73ms   | 70.61KB/s    |
|                              | Litestar   | 204.61   | 19.62ms   | 79.13KB/s    |
|                              | net/http   | 1262.49  | 3.16ms    | 483.32KB/s   |
| /records/get_pg              | FastAPI    | 92.27    | 112.18ms  | 8.85MB/s     |
|                              | Litestar   | 106.69   | 97.83ms   | 10.14MB/s    |
|                              | net/http   | 1000.61  | 9.94ms    | 95.56MB/s    |
| /records/get_ch              | FastAPI    | 57.11    | 176.44ms  | 5.57MB/s     |
|                              | Litestar   | 57.74    | 173.92ms  | 5.65MB/s     |
|                              | net/http   | 868.53   | 11.49ms   | 86.89MB/s    |
| /records/replicate_pg_to_ch  | FastAPI    | 0.77     | 1.36s     | 249.25/s     |
|                              | Litestar   | 1.03     | 1.39s     | 246.58/s     |
|                              | net/http   | 0.99     | 1.30s     | 221.44/s     |
| /records/replicate_ch_to_pg  | FastAPI    | 14.44    | 77.42ms   | 4.21KB/s     |
|                              | Litestar   | 15.12    | 76.61ms   | 4.32KB/s     |
|                              | net/http   | 6.91     | 347.71ms  | 821.86/s     |

## Анализ производительности

### POST операции (/records/post_pg и /records/post_ch)
- net/http показывает значительно лучшую производительность по сравнению с FastAPI и Litestar для обоих эндпоинтов.
- Для /records/post_pg net/http обрабатывает 2041.79 запросов в секунду, что примерно в 3 раза больше, чем FastAPI и Litestar.
- Для /records/post_ch net/http также лидирует с 1262.49 запросов в секунду, что в 6-7 раз больше, чем у конкурентов.

### GET операции (/records/get_pg и /records/get_ch)
1. /records/get_pg:
   - net/http показывает значительно лучшую производительность, обрабатывая 1000.61 запросов в секунду, что примерно в 10 раз больше, чем FastAPI и Litestar.
   - Латентность net/http (9.94ms) также намного ниже, чем у FastAPI (112.18ms) и Litestar (97.83ms).
   - Пропускная способность net/http (95.56MB/s) примерно в 10 раз выше, чем у конкурентов.

2. /records/get_ch:
   - net/http снова демонстрирует превосходную производительность с 868.53 запросов в секунду, что более чем в 15 раз превышает показатели FastAPI и Litestar.
   - Латентность net/http (11.49ms) значительно ниже, чем у FastAPI (176.44ms) и Litestar (173.92ms).
   - Пропускная способность net/http (86.89MB/s) примерно в 15 раз выше, чем у других фреймворков.

### Репликация данных
- Для /records/replicate_pg_to_ch все три фреймворка показывают схожую производительность (около 1 req/s).
- Для /records/replicate_ch_to_pg net/http показывает меньше запросов в секунду (6.91), но значительно большую пропускную способность (821.86/s) по сравнению с FastAPI и Litestar.

## Выводы

1. net/http демонстрирует исключительную производительность для всех операций чтения и записи, значительно превосходя FastAPI и Litestar.
2. Разница в производительности особенно заметна при работе с ClickHouse (/records/get_ch), где net/http показывает более чем 15-кратное улучшение по сравнению с другими фреймворками.
3. Латентность net/http во всех случаях значительно ниже, что указывает на гораздо более быстрый отклик.
4. Пропускная способность net/http также значительно выше, что позволяет обрабатывать больший объем данных в единицу времени.
5. В операциях репликации net/http показывает сопоставимые или лучшие результаты по пропускной способности.

Общий вывод: net/http демонстрирует превосходную производительность во всех сценариях, особенно в операциях чтения и записи. Это подчеркивает эффективность net/http для высокопроизводительных приложений, требующих обработки большого количества запросов с минимальной задержкой. Однако при выборе фреймворка следует учитывать и другие факторы, такие как удобство разработки, экосистема и специфические требования проекта.

## Bash Commands

### FastAPI

```bash
bombardier -c 4 -n 1000 127.0.0.1:8000/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 4 -n 1000 127.0.0.1:8000/records/post_ch -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 10 -n 1000 127.0.0.1:8000/records/get_pg -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 10 -n 1000 127.0.0.1:8000/records/get_ch -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 1 -n 1 127.0.0.1:8000/records/replicate_pg_to_ch -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
bombardier -c 1 -n 1 127.0.0.1:8000/records/replicate_ch_to_pg -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

### Litestar

```bash
bombardier -c 4 -n 1000 127.0.0.1:8001/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 4 -n 1000 127.0.0.1:8001/records/post_ch -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 10 -n 1000 127.0.0.1:8001/records/get_pg -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 10 -n 1000 127.0.0.1:8001/records/get_ch -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 1 -n 1 127.0.0.1:8001/records/replicate_pg_to_ch -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
bombardier -c 1 -n 1 127.0.0.1:8001/records/replicate_ch_to_pg -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

### net/http

```bash
bombardier -c 4 -n 1000 127.0.0.1:8080/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 4 -n 1000 127.0.0.1:8080/records/post_ch -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 10 -n 1000 127.0.0.1:8080/records/get_pg -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 10 -n 1000 127.0.0.1:8080/records/get_ch -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
bombardier -c 1 -n 1 127.0.0.1:8080/records/replicate_pg_to_ch -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
bombardier -c 1 -n 1 127.0.0.1:8080/records/replicate_ch_to_pg -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```
