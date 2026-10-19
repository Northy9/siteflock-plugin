# Siteflock plugin for Claude

Siteflock is a website builder and host for agencies that make websites for
local businesses: plumbers, electricians, cleaners, dentists and other trades.
This plugin works with Claude. It connects Claude to your Siteflock agency
workspace and adds a skill that tells Claude how to use it well.

With it, Claude can:

- Turn a Google Maps listing into a concept website you can text to the
  business owner (a "quick pitch").
- Start client websites from your templates and write or change their content
  as previews you keep or discard.
- Add photos from the business's own website or a free stock library.
- Work through the publish checklist and ask you to approve publishing.
- Add a client's custom domain, give you the DNS records and check when it is
  live.

Claude never publishes a website, moves one to Trash or removes a domain by
itself. It sends you an approve link, and nothing happens until you sign in to
siteflock.app and press Approve. Approve links expire after 30 minutes.

## What's inside

- `.mcp.json`: the Siteflock connector, a remote MCP server at
  `https://siteflock.app/api/mcp`. It contains no keys or passwords. You sign
  in with your own Siteflock account (OAuth) the first time Claude uses it.
- `skills/siteflock-website-builder`: instructions only, no code. Claude reads
  them when you ask for a website for a local business, a pitch site, or to
  publish or update one.

## Before you start

You need a Siteflock account with an agency (team) workspace:
https://siteflock.app. When you connect, choose the workspaces Claude may use
and a level: Read only, Build drafts, or Build and request approvals. You can
pause or disconnect Claude at any time in Siteflock under Settings → Agents.

## Install

In Claude Code:

```
/plugin marketplace add Northy9/siteflock-plugin
/plugin install siteflock@siteflock-plugins
```

Then run `/mcp`, choose `plugin:siteflock:siteflock` and sign in to Siteflock.

In claude.ai or Claude Desktop: add Siteflock from the Connectors directory
(or as a custom connector with the URL `https://siteflock.app/api/mcp`), then
add this plugin from the plugin directory. If you only want the skill, zip
the `skills/siteflock-website-builder` folder (the folder itself at the top
of the ZIP) and upload it under Customize → Skills. The skill needs the
connector to do anything.

Try: "Build a website for a plumber in Brisbane" or "Make a pitch site for
this Google Maps link".

## What it sends and fetches

The skill itself runs nothing. Everything goes through the Siteflock connector,
signed in as you:

- Tool arguments you or Claude provide (business names, phone numbers,
  suburbs, website text, domains) are sent to siteflock.app and saved in your
  workspace as website drafts.
- When asked, Siteflock looks businesses up on Google Places using your
  workspace's own Google key and quota, reads a business's public website, and
  searches Pixabay or Pexels for free stock photos.
- Preview links are public to anyone who has the link until they expire or
  you turn them off. Websites become public only after you approve
  publishing.
- Siteflock records which tool was used and whether it worked, not what was
  sent or returned, and deletes those records after 90 days.

Privacy policy: https://siteflock.app/privacy-policy
Terms: https://siteflock.app/terms-of-service
Help and the full tool list: https://siteflock.app/connect
Support: https://siteflock.app/contact

Siteflock is an independent product. It is not made, endorsed or sponsored by
Anthropic. "Claude" is a trademark of Anthropic.

## License

MIT. See `LICENSE`.
