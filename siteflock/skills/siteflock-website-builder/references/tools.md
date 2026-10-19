# Siteflock connector tools

The connector at `https://siteflock.app/api/mcp` has 36 tools. The level is the
lowest permission level a connection needs (read < build < approve). "Owners"
means workspace owners only. Tools marked **approve link** never act: they
return a link the person opens on siteflock.app to approve or decline.

## Workspace and clients

| Tool | Level | What it does |
| --- | --- | --- |
| `whoami` | read | Signed-in user, permission level, workspaces, quick pitch outline. |
| `list_clients` | read | Clients and their stage (waiting, review, building, ready, live). |
| `list_templates` | read | Website templates; `canStartNewSite` marks the ones a new site can use. |
| `report_problem_or_suggestion` | read | Sends a bug report or idea to the workspace's Feedback inbox. |
| `get_footer_credit` | read | Whether the "Built with Siteflock" footer link is on. |
| `set_footer_credit` | build (primary owner) | Turns the footer link on or off. Ask first. |

## Drafts

| Tool | Level | What it does |
| --- | --- | --- |
| `get_site` | read | A website's saved draft, template release and `draftRevision`. |
| `get_readiness` | read | What is left before the website can be published. |
| `get_site_fields` | read | Editable fields, their limits and kind (`wording` or `facts`). |
| `create_client_site` | build | Starts a new client website as a draft. |
| `preview_site_changes` | build | Prepares changes as a preview; nothing is saved yet. |
| `keep_site_changes` | build | Saves a preview as a new draft version (after the person agrees). |
| `discard_site_changes` | build | Throws a preview away. |
| `list_site_history` | read | Saved versions, newest first. |
| `restore_site_revision` | build | Copies an earlier version into a new draft version (undo). |
| `connect_site_form` | build (owners) | Connects the business's GoHighLevel quote and contact forms. |

## Photos

| Tool | Level | What it does |
| --- | --- | --- |
| `list_site_photos` | read | Uploaded photos and the template's photo spots. |
| `request_photo_upload` | read | A link where the person uploads photos in Siteflock. |
| `place_site_photo` | build | Previews a photo in a photo spot; keep with `keep_site_changes`. |
| `search_stock_photos` | read | Searches Pixabay or Pexels (free licence) for general spots. |
| `import_stock_photo` | build | Copies a stock photo into the website's photos. |
| `import_website_photo` | build | Copies a photo from the business's own recorded website. |

## Quick pitch

| Tool | Level | What it does |
| --- | --- | --- |
| `lookup_google_business` | build | Finds a business on Google Maps with the workspace's own Google key and quota. |
| `read_business_website` | read | Reads a business's public website (home page plus up to 4 pages). |
| `set_business_website` | build | Records which website is the business's own. |
| `share_site_preview` | build | Public, expiring preview link to the latest draft (shown once). |
| `stop_sharing_site_preview` | build | Turns the preview link off. |

## Publishing and hosting

| Tool | Level | What it does |
| --- | --- | --- |
| `request_publish` | approve | **Approve link** to publish the current draft (checks readiness first). |
| `move_to_trash` | approve | **Approve link** to move up to 50 websites to Trash. |
| `get_approval_status` | read | Whether a request is pending, approved, done, failed, declined, cancelled or expired. |
| `cancel_approval` | approve | Withdraws an undecided request. |
| `get_hosting_status` | read | Live address, domains with next steps, recent publishes. |

## Domains

| Tool | Level | What it does |
| --- | --- | --- |
| `add_site_domain` | build (owners) | Adds a client's domain and returns the DNS records to add. |
| `set_domain_connection` | build (owners) | Switches a domain between DNS records and nameservers. |
| `check_domain_live` | read | Checks a domain's DNS, HTTPS and live page now. |
| `remove_site_domain` | approve (owners) | **Approve link** to remove a domain from a website. |
