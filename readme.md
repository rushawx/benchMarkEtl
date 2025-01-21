# benchmark

```bash
bombardier -c 4 -n 1000000 127.0.0.1:8000/records/post_pg -m POST -b '{"text": "Hello"}' -H 'accept: application/json' -H 'Content-Type: application/json';
```