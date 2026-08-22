# Opencode

## Command Set

| Command                              | Purpose                              | Example                                 |
| ------------------------------------ | ------------------------------------ | --------------------------------------- |
| `opencode`                           | Start interactive TUI                | `opencode`                              |
| `opencode <project>`                 | Open a specific project              | `opencode ~/projects/myapp`             |
| `opencode -c`                        | Continue last session                | `opencode -c`                           |
| `opencode -s <session-id>`           | Resume a specific session            | `opencode -s ses_abc123`                |
| `opencode --fork -c`                 | Continue as a new branch/session     | `opencode --fork -c`                    |
| `opencode -m provider/model`         | Select model                         | `opencode -m openai/gpt-5`              |
| `opencode --agent <agent>`           | Use a specific agent                 | `opencode --agent reviewer`             |
| `opencode run "<prompt>"`            | One-shot execution (non-interactive) | `opencode run "Explain this repo"`      |
| `opencode run -f file.py "<prompt>"` | Attach file(s) to a prompt           | `opencode run -f main.py "Review this"` |
| `opencode serve`                     | Start headless server/API            | `opencode serve`                        |
| `opencode session list`              | List saved sessions                  | `opencode session list`                 |
| `opencode session delete <id>`       | Delete a session                     | `opencode session delete ses_abc123`    |
| `opencode export`                    | Export session to JSON               | `opencode export`                       |
| `opencode import session.json`       | Import a session                     | `opencode import session.json`          |
| `opencode stats`                     | View token usage and costs           | `opencode stats --days 30`              |

### Useful flags

| Flag               | Meaning                                         |
| ------------------ | ----------------------------------------------- |
| `-c`, `--continue` | Continue last session                           |
| `-s`, `--session`  | Resume a session by ID                          |
| `--fork`           | Continue without modifying the original session |
| `-m`, `--model`    | Select the model                                |
| `--agent`          | Select an agent                                 |
| `--auto`           | Auto-approve tool permissions                   |
| `-f`, `--file`     | Attach files to a prompt                        |
| `--thinking`       | Show reasoning/thinking blocks (if supported)   |
| `--format json`    | Emit JSON output (good for scripting)           |

### Built-in slash commands (inside the TUI)

| Command     | Action                                        |
| ----------- | --------------------------------------------- |
| `/help`     | Show help                                     |
| `/new`      | Start a new session                           |
| `/clear`    | Alias for `/new`                              |
| `/sessions` | Browse and switch sessions                    |
| `/editor`   | Open your external editor to compose a prompt |
| `/export`   | Export the current conversation to Markdown   |

### Daily workflow

```bash
# Start coding
opencode

# Resume yesterday's work
opencode -c

# List all sessions
opencode session list

# Reopen a specific session
opencode -s ses_xxxxx

# Ask a one-off question
opencode run "Explain this repository"

# Check token usage
opencode stats --days 7
```

## References

- [Opencode](https://opencode.ai/)
