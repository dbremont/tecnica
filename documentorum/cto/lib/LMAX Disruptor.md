> [LMAX](https://www.lmax.com/) aims to be the fastest trading platform in the world. Clearly, in order to achieve this we needed to do something special to  achieve very low-latency and high-throughput with our Java platform. Performance testing showed that using queues to pass data between stages
of the system was introducing latency, so we focused on optimising this  area.
> 

## References

- ThompsonMartin, Farley, D., Barker, M., Gee, P., Stewart, A. (n.d.). LMAX Disruptor: High performance alternative to bounded queues for exchanging data between concurrent threads. Retrieved July 16, 2022, from https://lmax-exchange.github.io/disruptor/disruptor.html