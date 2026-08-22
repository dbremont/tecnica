# PyTorch

> **PyTorch** is an open-source deep learning framework that provides flexible and dynamic computational graphs, enabling efficient development, training, and deployment of machine learning models, especially for research and production in neural networks.

## Install

`pip install torch`

## Core Abstractions

> Here’s a table summarizing the core abstractions in PyTorch, a popular deep learning framework:

| **Abstraction** | **Description** | **Key Classes/Functions** | **Example Usage** |
| --- | --- | --- | --- |
| **`torch.Tensor`** | The central data structure for storing multi-dimensional arrays and performing operations. | `torch.tensor()`, `torch.Tensor` | `t = torch.tensor([1.0, 2.0, 3.0])` |
| **`torch.nn.Module`** | Base class for all neural network modules, including layers and models. | `torch.nn.Module`, `torch.nn.Linear` | `model = torch.nn.Linear(in_features, out_features)` |
| **`torch.optim`** | Optimization algorithms for training models by updating parameters based on gradients. | `torch.optim.SGD`, `torch.optim.Adam` | `optimizer = torch.optim.Adam(model.parameters(), lr=0.001)` |
| **`torch.autograd`** | Automatic differentiation engine that powers neural network training by computing gradients. | `torch.autograd.grad`, `torch.autograd.backward` | `loss.backward()` |
| **`torch.nn.functional`** | Functional interface for various operations and activation functions used in neural networks. | `torch.nn.functional.relu`, `torch.nn.functional.cross_entropy` | `torch.nn.functional.relu(x)` |
| **`torch.utils.data`** | Tools for managing datasets and data loading, including data transformations and batching. | `torch.utils.data.Dataset`, `torch.utils.data.DataLoader` | `DataLoader(dataset, batch_size=64)` |
| **`torch.cuda`** | Utilities for leveraging GPU acceleration and managing CUDA tensors. | `torch.cuda.is_available()`, `torch.cuda.device` | `tensor.to('cuda')` |
| **`torch.jit`** | Tools for optimizing and serializing PyTorch models for production deployment. | `torch.jit.script`, `torch.jit.trace` | `torch.jit.script(model)` |
| **`torch.nn.init`** | Functions for initializing weights in neural network layers. | `torch.nn.init.xavier_uniform_`, `torch.nn.init.zeros_` | `torch.nn.init.xavier_uniform_(layer.weight)` |
| **`torch.onnx`** | Tools for exporting PyTorch models to the ONNX (Open Neural Network Exchange) format. | `torch.onnx.export` | `torch.onnx.export(model, dummy_input, "model.onnx")` |

## Broadcasting

> In PyTorch, **broadcasting** is a powerful mechanism that allows tensors of different shapes to be automatically expanded so they can be used together in arithmetic operations (like addition, multiplication, etc.) without explicitly reshaping them.

**Broadcasting** only works if:

- **Dimensions** are equal, or
- **One** of them is 1, or
- **One** tensor has fewer dimensions (it gets prepended with 1s)

```python
import torch

a = torch.tensor([[1], [2], [3]])  # Shape: (3, 1)
b = torch.tensor([10, 20, 30])     # Shape: (3,)

result = a + b  # b is broadcast to shape (3, 3)
print(result)
```

## Deep Learning Frameworks

Here's a table summarizing popular deep learning frameworks:

| **Framework** | **Description** | **Primary Use Cases** | **Key Features** |
| --- | --- | --- | --- |
| **TensorFlow** | An open-source library developed by Google for numerical computation and large-scale machine learning. | Deep learning, neural networks, large-scale machine learning | Flexible architecture, supports distributed computing, TensorBoard for visualization |
| **Keras** | A high-level neural networks API, written in Python and capable of running on top of TensorFlow. | Rapid prototyping, easy-to-use interface | User-friendly API, supports multiple backends (TensorFlow, Theano, CNTK) |
| **PyTorch** | An open-source machine learning library developed by Facebook's AI Research lab, known for its dynamic computation graph. | Research, dynamic neural networks, flexible experimentation | Dynamic computation graph, strong support for GPU acceleration, extensive library |
| **MXNet** | An open-source deep learning framework designed for both efficiency and flexibility. | Scalability, efficient computation on various hardware | Support for both symbolic and imperative programming, efficient distributed training |
| **Caffe** | A deep learning framework developed by the Berkeley Vision and Learning Center (BVLC). | Image classification, convolutional networks | Fast training, modular architecture, strong support for computer vision tasks |
| **Chainer** | A deep learning framework that uses a "define-by-run" approach, allowing for dynamic computation graphs. | Research, dynamic neural networks | Flexible design, supports complex architectures, easy debugging |
| **Theano** | An open-source numerical computation library that allows for efficient computation of mathematical expressions. | Research, efficient numerical computation | Early framework for symbolic differentiation, strong support for GPU acceleration |
| **JAX** | A library developed by Google for high-performance numerical computing, with automatic differentiation. | High-performance computing, research | Auto-differentiation, NumPy-compatible API, efficient computation on GPUs and TPUs |
| **ONNX** | Open Neural Network Exchange, a framework-agnostic format for representing machine learning models. | Model interoperability, cross-framework compatibility | Facilitates model transfer between different deep learning frameworks |

## References

- https://pytorch.org/
- https://en.wikipedia.org/wiki/PyTorch
- https://github.com/pytorch/pytorch
- https://blog.ezyang.com/2019/05/pytorch-internals/