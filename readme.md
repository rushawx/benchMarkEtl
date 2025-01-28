# benchmark

## FastAPI

```bash
bombardier -c 4 -n 1000 127.0.0.1:8000/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec       634.89     148.09    1048.36
Latency        6.33ms     3.59ms    60.39ms

Throughput:   246.93KB/s

```bash
bombardier -c 4 -n 1000 127.0.0.1:8000/records/post_ch -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec       184.74      45.73     385.86
Latency       21.73ms     4.85ms    72.16ms

Throughput:    70.61KB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/get_pg -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec       215.41     444.08    1077.05
Latency       82.15ms     0.00us    82.15ms

Throughput:     1.20MB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/get_ch -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec        31.80      50.28      95.39
Latency       51.17ms     0.00us    51.17ms

Throughput:     1.78MB/s


```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/replicate_pg_to_ch -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

Statistics        Avg      Stdev        Max
Reqs/sec         0.77       6.30      52.37
Latency         1.36s     0.00us      1.36s

Throughput:     249.25/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/replicate_ch_to_pg -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

Statistics        Avg      Stdev        Max
Reqs/sec        14.44      26.37      57.77
Latency       77.42ms     0.00us    77.42ms

Throughput:     4.21KB/s

## Litestar

```bash
bombardier -c 4 -n 1000 127.0.0.1:8001/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec       714.76     166.26    1515.92
Latency        5.68ms     2.23ms    29.87ms

Throughput:   278.61KB/s

```bash
bombardier -c 4 -n 1000 127.0.0.1:8001/records/post_ch -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec       204.61      50.51     404.12
Latency       19.62ms     4.69ms    59.77ms

Throughput:    79.13KB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8001/records/get_pg -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec        51.54       0.00     103.08
Latency       29.11ms     0.00us    29.11ms

Throughput:     3.23MB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8001/records/get_ch -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec        51.67       0.00     103.34
Latency       30.75ms     0.00us    30.75ms

Throughput:     2.98MB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8001/records/replicate_pg_to_ch -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

Statistics        Avg      Stdev        Max
Reqs/sec         1.03       8.58      72.28
Latency         1.39s     0.00us      1.39s

Throughput:     246.58/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8001/records/replicate_ch_to_pg -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

Statistics        Avg      Stdev        Max
Reqs/sec        15.12      27.61      60.49
Latency       76.61ms     0.00us    76.61ms

Throughput:     4.32KB/s
