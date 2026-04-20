# Dashboard Spec

Required Layer-2 panels:
1. Latency P50/P95/P99: `latency_p50`, `latency_p95`, `latency_p99`
2. Traffic/QPS: `traffic`
3. Error rate: từ `error_breakdown` + `traffic`
4. Cost: `avg_cost_usd` và/hoặc `total_cost_usd`
5. Tokens in/out: `tokens_in_total`, `tokens_out_total`
6. Quality: `quality_avg`

Quality bar:
- default time range = 1 hour
- auto refresh every 15-30 seconds
- visible threshold/SLO line
- units clearly labeled
- no more than 6-8 panels on the main layer

## Screenshot:
![Dashboard UI](Screenshot_2026-04-20_at_17.31.30.png)




