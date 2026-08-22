# Aider

> This is a horrible docs - improved:

TODO:

- [ ] What is computational complexity of Aider? Memory - Storage - CPU - GPU?

- [ ]  https://aider.chat/
- [ ]  https://openrouter.ai/docs/quickstart

```bash
python3 -m pip install aider-install
aider-install

# Change directory into your codebase
cd /to/your/project

# DeepSeek
aider --model deepseek --api-key deepseek=<key>

# Claude 3.7 Sonnet
aider --model sonnet --api-key anthropic=<key>

# o3-mini
aider --model o3-mini --api-key openai=<key>
```

```bash

export OPENROUTER_API_KEY="your_openrouter_api_key"
aider --model openrouter/deepseek/deepseek-r1-0528:free

curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -d '{
  "model": "deepseek/deepseek-r1-0528:free",
  "messages": [
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
}'

aider "Generate a concise git commit message based on this diff:" -f <(gd)
```

```bash
# Ollama
```

Configuration:

- https://aider.chat/docs/config/aider_conf.html

## References

- https://aider.chat/
