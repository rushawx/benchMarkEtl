# benchmark

## Results

Вот комбинированная таблица для сравнения производительности FastAPI и Litestar:

| Endpoint                     | Framework  | Reqs/sec | Latency   | Throughput   |
|------------------------------|------------|----------|-----------|--------------|
| /records/post_pg             | FastAPI    | 634.89   | 6.33ms    | 246.93KB/s   |
|                              | Litestar   | 714.76   | 5.68ms    | 278.61KB/s   |
| /records/post_ch             | FastAPI    | 184.74   | 21.73ms   | 70.61KB/s    |
|                              | Litestar   | 204.61   | 19.62ms   | 79.13KB/s    |
| /records/get_pg              | FastAPI    | 215.41   | 82.15ms   | 1.20MB/s     |
|                              | Litestar   | 51.54    | 29.11ms   | 3.23MB/s     |
| /records/get_ch              | FastAPI    | 31.80    | 51.17ms   | 1.78MB/s     |
|                              | Litestar   | 51.67    | 30.75ms   | 2.98MB/s     |
| /records/replicate_pg_to_ch  | FastAPI    | 0.77     | 1.36s     | 249.25/s     |
|                              | Litestar   | 1.03     | 1.39s     | 246.58/s     |
| /records/replicate_ch_to_pg  | FastAPI    | 14.44    | 77.42ms   | 4.21KB/s     |
|                              | Litestar   | 15.12    | 76.61ms   | 4.32KB/s     |

### Примечания:
- В таблице указаны значения для каждого эндпоинта с разделением по фреймворкам.
- **Reqs/sec**: количество запросов в секунду.
- **Latency**: средняя задержка.
- **Throughput**: объем данных, обрабатываемых в секунду.

Эта таблица позволяет легко сравнить производительность двух фреймворков на одном наборе тестов для различных эндпоинтов и операций!

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
