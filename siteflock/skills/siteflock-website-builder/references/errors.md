# Siteflock error codes

Each failed tool call returns a code and a plain-English message. What to do:

## Connection and permissions

| Code | What to do |
| --- | --- |
| `PERMISSION_LEVEL` | The connection's level is too low. Ask the person to reconnect Siteflock with a higher level (Build drafts, or Build and request approvals). |
| `ROLE_REQUIRED` | The person's role in this workspace does not allow it (many tools are for owners only). Tell the person. |
| `WORKSPACE_REQUIRED` | More than one workspace: pass `accountSlug` from `whoami`. |
| `WORKSPACE_NOT_ALLOWED` | The connection was not given that workspace. Ask the person to reconnect and tick it. |
| `WORKSPACE_NOT_FOUND` | Call `whoami` for the current list. |
| `CONNECTION_INACTIVE` | Paused or revoked. The person can resume it in Siteflock under Settings → Agents. |
| `RECONNECT_REQUIRED` | Siteflock can't confirm the connection meets the person's 2-step sign-in rule. Ask them to disconnect and reconnect in Settings → Agents. |
| `RATE_LIMITED` | Wait a minute, then try again. |

## Drafts and photos

| Code | What to do |
| --- | --- |
| `SITE_NOT_FOUND` | Find the website with `list_clients` (it may be in Trash). |
| `REVISION_CONFLICT` | The website changed. Call `get_site` again and use the new `draftRevision`. |
| `PROPOSAL_NOT_FOUND` | The preview was kept, discarded or expired. Preview the change again. |
| `CHANGE_REJECTED` | The detail names the rule that was broken. Fix the operations and preview again. |
| `TEMPLATE_NOT_FOUND` | Use `list_templates` and pick one with `canStartNewSite`. |
| `EMAIL_REQUIRED` | This template needs an email address. Ask the person for one. |
| `PHOTO_NOT_FOUND` | Use `list_site_photos`, or `request_photo_upload` so the person can add one. |
| `PHOTO_IMPORT_FAILED` | Pick another photo. |
| `STOCK_PHOTOS_UNAVAILABLE` | Ask the person to upload photos with `request_photo_upload`. |
| `REVISION_NOT_FOUND` | Use `list_site_history`. |
| `IN_PROGRESS` | Wait a few seconds and retry with the same `requestId`. |
| `FORM_LINK_INVALID` | The detail names the field. Ask the person for the GoHighLevel form link or embed code again. |

## Quick pitch

| Code | What to do |
| --- | --- |
| `GOOGLE_NOT_CONNECTED` | The workspace has no Google key. Ask the person for the business details instead. |
| `GOOGLE_LIMITED` | The workspace's Google limit was reached (daily, or per minute). Wait a minute, or ask the person for the details. |
| `GOOGLE_UNAVAILABLE` | Try once more; then ask the person for the details. |
| `MAPS_LINK_INVALID` | Ask for the Maps share link again, or use `query` with name and suburb. |
| `PLACE_NOT_FOUND` | Check the spelling, add the suburb, or ask for the Maps link. |
| `WEBSITE_ADDRESS_INVALID`, `WEBSITE_NOT_HTML` | Use the business's public home page address (private and IP addresses are refused). |
| `WEBSITE_UNREACHABLE` | The site didn't answer over https. Ask the person for the details, or try later. |
| `WEBSITE_REDIRECTS_ELSEWHERE` | The site sends visitors elsewhere. Ask the person whether that address is the business's own before reading it. |

## Publishing and domains

| Code | What to do |
| --- | --- |
| `SITE_NOT_READY` | The detail lists what is missing. Work through `get_readiness` and ask again. |
| `APPROVAL_NOT_FOUND` | Use the `approvalId` that the approval request returned. |
| `APPROVAL_ALREADY_DECIDED` | Call `get_approval_status`. |
| `DOMAIN_INVALID` | Use the bare name, e.g. `example.com.au`. |
| `DOMAIN_TAKEN` | The domain is on another Siteflock website. Remove it there first. |
| `DOMAIN_NOT_FOUND` | Check `get_hosting_status`, or add it with `add_site_domain`. |

## Anything else

| Code | What to do |
| --- | --- |
| `INVALID_INPUT` | Re-read the tool's description and fix the input. |
| `BUILDER_DISABLED` | Website editing is switched off for this Siteflock. Tell the person. |
| `INTERNAL` | Try once more; if it fails again, report it with `report_problem_or_suggestion`. |
