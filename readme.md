# benchmark

## Results

Вот комбинированная таблица для сравнения производительности FastAPI, Litestar, net/http:

| Endpoint                     | Framework  | Reqs/sec | Latency   | Throughput   |
|------------------------------|------------|----------|-----------|--------------|
| /records/post_pg             | FastAPI    | 634.89   | 6.33ms    | 246.93KB/s   |
|                              | Litestar   | 714.76   | 5.68ms    | 278.61KB/s   |
|                              | net/http   | 2041.79  | 1.93ms    | 787.78KB/s   |
| /records/post_ch             | FastAPI    | 184.74   | 21.73ms   | 70.61KB/s    |
|                              | Litestar   | 204.61   | 19.62ms   | 79.13KB/s    |
|                              | net/http   | 1262.49  | 3.16ms    | 483.32KB/s   |
| /records/get_pg              | FastAPI    | 215.41   | 82.15ms   | 1.20MB/s     |
|                              | Litestar   | 51.54    | 29.11ms   | 3.23MB/s     |
|                              | net/http   | 271.43   | 40.92ms   | 2.31MB/s     |
| /records/get_ch              | FastAPI    | 31.80    | 51.17ms   | 1.78MB/s     |
|                              | Litestar   | 51.67    | 30.75ms   | 2.98MB/s     |
|                              | net/http   | 18.21    | 57.38ms   | 1.69MB/s     |
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
- Для /records/get_pg net/http показывает хорошие результаты (271.43 req/s), превосходя FastAPI и Litestar.
- Однако для /records/get_ch net/http уступает обоим фреймворкам с 18.21 req/s.

### Репликация данных
- Для /records/replicate_pg_to_ch все три фреймворка показывают схожую производительность (около 1 req/s).
- Для /records/replicate_ch_to_pg net/http показывает меньше запросов в секунду (6.91), но значительно большую пропускную способность (821.86/s) по сравнению с FastAPI и Litestar.

## Выводы

1. net/http демонстрирует превосходную производительность для POST операций, значительно опережая FastAPI и Litestar.
2. Для GET операций результаты net/http неоднозначны: лучше для PostgreSQL, но хуже для ClickHouse.
3. В операциях репликации net/http показывает сопоставимые или лучшие результаты по пропускной способности.
4. Латентность net/http в большинстве случаев ниже, что указывает на более быстрый отклик.

Общий вывод: net/http показывает отличные результаты, особенно в операциях записи и работе с PostgreSQL. Однако для некоторых сценариев, особенно при работе с ClickHouse, FastAPI и Litestar могут иметь преимущества. Выбор фреймворка должен зависеть от конкретных требований проекта и преобладающих типов операций.

Sources


## Bash Commands

### FastAPI

```bash
bombardier -c 4 -n 1000 127.0.0.1:8000/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

```bash
bombardier -c 4 -n 1000 127.0.0.1:8000/records/post_ch -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/get_pg -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/get_ch -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/replicate_pg_to_ch -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/replicate_ch_to_pg -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

### Litestar

```bash
bombardier -c 4 -n 1000 127.0.0.1:8001/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

```bash
bombardier -c 4 -n 1000 127.0.0.1:8001/records/post_ch -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

```bash
bombardier -c 1 -n 1 127.0.0.1:8001/records/get_pg -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

```bash
bombardier -c 1 -n 1 127.0.0.1:8001/records/get_ch -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

```bash
bombardier -c 1 -n 1 127.0.0.1:8001/records/replicate_pg_to_ch -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

```bash
bombardier -c 1 -n 1 127.0.0.1:8001/records/replicate_ch_to_pg -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

### net/http

```bash
bombardier -c 4 -n 1000 127.0.0.1:8080/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```
Statistics        Avg      Stdev        Max
Reqs/sec      2041.79     575.32    2659.46
Latency        1.93ms     2.06ms    29.89ms

Throughput:   787.78KB/s

```bash
bombardier -c 4 -n 1000 127.0.0.1:8080/records/post_ch -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```
Statistics        Avg      Stdev        Max
Reqs/sec      1262.49     338.63    1643.37
Latency        3.16ms     2.06ms    30.07ms

Throughput:   483.32KB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8080/records/get_pg -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```
Statistics        Avg      Stdev        Max
Reqs/sec       271.43     429.16     814.28
Latency       40.92ms     0.00us    40.92ms

Throughput:     2.31MB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8080/records/get_ch -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```
Statistics        Avg      Stdev        Max
Reqs/sec        18.21      28.80      54.64
Latency       57.38ms     0.00us    57.38ms

Throughput:     1.69MB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8080/records/replicate_pg_to_ch -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```
Statistics        Avg      Stdev        Max
Reqs/sec         0.99       7.94      64.52
Latency         1.30s     0.00us      1.30s

Throughput:     221.44/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8080/records/replicate_ch_to_pg -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```
Statistics        Avg      Stdev        Max
Reqs/sec         6.91      28.54     124.36
Latency      347.71ms     0.00us   347.71ms

Throughput:     821.86/s