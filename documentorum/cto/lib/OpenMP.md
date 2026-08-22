> OpenMP is a standard, not an implementation. There are multiple implementations. Two are mainstream: **GOMP** associated with GCC and IOMP associated to Clang (and ICC).
> 

### OpenMP Implementation Comparison Table

| Feature | GCC | LLVM/Clang | Intel Compiler | Microsoft Visual C++ |
| --- | --- | --- | --- | --- |
| **Latest Version Supported** | OpenMP 5.0 | OpenMP 5.0 | OpenMP 5.1 | OpenMP 2.0 |
| **Operating Systems** | Linux, macOS, Windows | Linux, macOS, Windows | Linux, macOS, Windows | Windows |
| **Parallel Constructs** | Excellent | Excellent | Excellent | Limited |
| **Tasking Support** | Full | Full | Full | None |
| **SIMD Support** | Full | Full | Full | None |
| **Offloading Support** | GPU (limited) | None | GPU, FPGA | None |
| **Performance Optimization** | High | Moderate-High | Very High | Moderate |
| **Ease of Use** | Moderate | High | High | Moderate |
| **Community and Support** | Very High | High | Moderate | Moderate |

## OpenMP Tools

**OpenMP (Open Multi-Processing)** is a set of compiler directives, libraries, and runtime functions that support multi-platform shared-memory parallel programming in C, C++, and Fortran. It enables developers to write parallel code easily by annotating sections of the program that should run concurrently.

| **Tool Type** | **Tool Name** | **Description** |
| --- | --- | --- |
| **Compiler Support** | **GCC (GNU Compiler Collection)** | GCC supports OpenMP through the `-fopenmp` flag, enabling parallelization in C, C++, and Fortran code. |
|  | **Clang/LLVM** | Clang/LLVM supports OpenMP with the `-fopenmp` flag and provides a more modern compiler toolchain for parallel applications. |
|  | **Intel Compiler** | Intel's C++ and Fortran compilers support OpenMP with optimizations tailored for Intel hardware. |
| **Performance Optimization** | **Intel VTune Profiler** | A performance profiling tool that helps identify and optimize bottlenecks in parallel OpenMP applications, especially for Intel hardware. |
|  | **Gprof** | A profiling tool available in GCC that can be used to analyze the performance of OpenMP applications. |
| **Debugging Tools** | **TotalView** | A debugger that provides advanced support for OpenMP parallel applications, allowing for debugging in multi-threaded environments. |
|  | **GDB (GNU Debugger)** | A general-purpose debugger that supports debugging OpenMP applications with multi-threaded environments. |
| **Memory Analysis Tools** | **Valgrind** | A tool for memory debugging, memory leak detection, and profiling, often used for OpenMP code to ensure efficient memory use in parallel applications. |
| **Profiling Tools** | **OpenMP Profiler (OMP)** | A profiler specifically designed for OpenMP, allowing developers to track performance and optimize parallel regions of code. |
|  | **PAPI (Performance API)** | PAPI provides a set of tools for accessing the performance monitoring counters in CPUs, often used to gather metrics in OpenMP parallel regions. |
| **Visualization Tools** | **KCachegrind/ QCacheGrind** | Profiling visualization tools that help visualize the performance of OpenMP parallel applications by generating call graphs and performance metrics. |
|  | **TAU (Tuning and Analysis Utilities)** | A comprehensive profiling and tracing toolkit that supports OpenMP and other parallel programming models. |
| **Documentation and Tutorials** | **OpenMP Official Documentation** | The official documentation provides guidance on how to use OpenMP constructs effectively, including tutorials and best practices for parallelism. |
|  | **OpenMP Tutorials (various)** | Various online tutorials and guides (from both the official site and third-party resources) help users learn how to write and optimize OpenMP code. |

## Hello World

```c
// gcc -o hello_world_omp hello_world_omp.c -fopenmp
// ./hello_world_omp
// OMP_NUM_THREADS number of threasds

#include <stdio.h>
#include <omp.h>

int main() {
    #pragma omp parallel
    {
        int ID = omp_get_thread_num();
        printf("Hello from thread %d\n", ID);
    }
    return 0;
}
```

## References

- [GOMP](https://gcc.gnu.org/projects/gomp/)
- [GNU libgomp](https://gcc.gnu.org/onlinedocs/gcc-6.3.0/libgomp/)
- https://hpc-tutorials.llnl.gov/openmp/
- https://github.com/gcc-mirror/gcc/tree/master/libgomp
- [OpenMP Application Programming](https://www.openmp.org/spec-html/5.0/openmp.html)
- https://www.openmp.org/resources/openmp-compilers-tools/
- http://www.cs.uoregon.edu/research/tau/home.php