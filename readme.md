# benchmark

```bash
bombardier -c 4 -n 1000000 127.0.0.1:8000/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec       664.88     108.66     914.18
Latency        6.01ms     1.57ms    53.22ms

Throughput:   260.12KB/s

```bash
bombardier -c 4 -n 10000 127.0.0.1:8000/records/post_ch -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec       171.11      49.46     369.25
Latency       23.44ms     6.02ms   166.17ms

Throughput:    65.45KB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/get_pg -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec        10.31      31.11     103.08
Latency      190.44ms     0.00us   190.44ms

Throughput:     5.15MB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/get_ch -m GET -H 'accept: application/json' -H 'Content-Type: application/json';
```

Statistics        Avg      Stdev        Max
Reqs/sec         4.39      15.26      57.08
Latency      257.17ms     0.00us   257.17ms

Throughput:     3.54MB/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/replicate_pg_to_ch -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

Statistics        Avg      Stdev        Max
Reqs/sec         0.07       2.08      61.04
Latency        17.21s     0.00us     17.21s

Throughput:      19.75/s

```bash
bombardier -c 1 -n 1 127.0.0.1:8000/records/replicate_ch_to_pg -m POST -H 'accept: application/json' -H 'Content-Type: application/json' -t 6000s;
```

Statistics        Avg      Stdev        Max
Reqs/sec         8.14      43.11     236.13
Latency      562.64ms     0.00us   562.64ms

Throughput:     601.10/s