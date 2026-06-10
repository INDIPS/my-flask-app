# Game Setup Link Guard

A Chrome/Edge Manifest V3 extension that scans links on live pages, verifies link domains against an allowlist, and blocks unauthorized clicks before navigation.

## Features

- Captures link clicks early with a content script.
- Blocks links whose domains are not in the allowlist.
- Scans all links on the page and marks them as verified or blocked.
- Supports dynamic pages through `MutationObserver`.
- Popup shows current page link/domain counts and lets you allow the current site.
- Options page lets you manage allowed domains.

## Load locally

1. Open Chrome or Edge.
2. Go to `chrome://extensions` or `edge://extensions`.
3. Enable **Developer mode**.
4. Click **Load unpacked**.
5. Select this `link-guard-extension` folder.

## How it works

The extension uses `chrome.storage.sync` to keep an allowlist of domains. A clicked link is allowed only when its hostname exactly matches an allowed domain or is a subdomain of an allowed domain.

Example: allowing `example.com` also allows `www.example.com` and `docs.example.com`.

## Notes

This extension blocks browser navigation from normal link clicks. It cannot guarantee blocking every possible script-driven redirect from a page. For stronger protection, browser-level webRequest/declarativeNetRequest policies would be needed.
