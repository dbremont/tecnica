> …
> 

```bash
curl https://robust-manually-flounder.ngrok-free.app/api/generate -d '{
  "model": "qwen:0.5b",
  "prompt": "Why is the sky blue?"
}'

http://127.0.0.1:11434/ 
```

```bash
curl https://robust-manually-flounder.ngrok-free.app/api/tags
```

```bash
curl -X POST https://robust-manually-flounder.ngrok-free.app/api/pull -d '{ "name": "qwen:0.5b" }'
```

## References

- https://ollama.com/library/qwen:0.5b
- https://github.com/ollama/ollama
- https://platform.openai.com/docs/api-reference/introduction
- https://github.com/ollama/ollama/blob/main/docs/api.md
- https://github.com/ggml-org/llama.cpp
