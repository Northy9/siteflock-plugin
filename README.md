# Siteflock plugins for Claude

This repository is a plugin marketplace (`siteflock-plugins`) with one plugin,
`siteflock`, which works with Claude. It connects Claude to a Siteflock agency
workspace so Claude can build, host and publish websites for local businesses
such as plumbers, electricians, cleaners and dentists: quick pitch sites from
a Google Maps listing, drafts you preview and keep, publishing you approve on
siteflock.app, and custom domains.

Install in Claude Code:

```
/plugin marketplace add Northy9/siteflock-plugin
/plugin install siteflock@siteflock-plugins
```

What the plugin contains, what it sends and fetches, and how to use it in
claude.ai are described in the plugin's own README: `siteflock/README.md`.

Layout:

- `.claude-plugin/marketplace.json`: the marketplace catalog.
- `siteflock/.claude-plugin/plugin.json`: the plugin manifest.
- `siteflock/.mcp.json`: the Siteflock connector (`https://siteflock.app/api/mcp`,
  OAuth sign-in, no credentials in the repository).
- `siteflock/skills/siteflock-website-builder/`: the skill (instructions only).

Siteflock is an independent product, not made, endorsed or sponsored by
Anthropic. MIT licensed; see `LICENSE`.
