These are roughly the same “tier” as Bubble Tea in terms of making terminal UX feel like a real app, and you can wire any LLM backend (OpenAI, Anthropic, local models) into them.

Shell glam helpers (Gum equivalents)
If you specifically like Gum’s “make shell scripts glamorous without writing Go,” you’ve got some analogous tools:

Gum itself – still the gold standard here, but worth calling out since Charm position it exactly as “a tool for glamorous shell scripts,” giving you inputs, selects, spinners, etc., via CLI subcommands.

PTerm (Go) – Not shell-only, but a Go module that beautifies console output: progress bars, tables, trees, text inputs, select menus, charts. It’s a nice alternative if you don’t want Bubble Tea’s Elm-ish model but still want polish.

For JS and Python you’d typically assemble this from prompt libraries (e.g., Enquirer, Inquirer, Rich, Textual), rather than a single “gum-like” binary.

For “LLMs in bash but pretty,” a realistic pattern is: Gum (or Enquirer/Rich-style CLIs) as the UX layer, a thin Go/Python/TS wrapper that talks to your LLM.

LLM-specific TUIs
These are closer to what Crush/Mods are aiming at: turnkey “LLM in the terminal, but nice.”

llm-tui (Rust) – TUI to chat with LLMs via llm-cli. Features multi-conversation chat, multiple model support, clipboard copy, and remote command support. Quite close to a terminal-native ChatGPT client.

ollama-term – TUI for managing and chatting with local models via Ollama; lets you pick models, run chats, and manage instances, all in a terminal UI.

These are good reference architectures if you want to roll your own Go or Python TUI around, say, OpenAI/Anthropic + local embeddings, but keep the “glamorous” look.

Where I’d start for “cool LLMs in the shell”
Given you’re already looking at Charm:

Go + Bubble Tea + Lip Gloss + Bubbles (Charm stack) if you want full control but maximum vibe.

Rust + Ratatui if you want performance and strong typing, inspired by llm-tui and ollama-term.

Python + Textual if you want quick iteration and rich widgets, especially for agentic workflows that change often.

If you tell me language/runtime and whether you want “just pretty prompts” vs a full-blown TUI (panes, tabs, history, etc.), I can sketch a minimal “glam” LLM client architecture for that stack.
