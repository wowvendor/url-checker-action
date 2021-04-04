URL checker action
===
[![Test](https://github.com/wowvendor/url-checker-action/actions/workflows/test.yml/badge.svg)](https://github.com/wowvendor/url-checker-action/actions/workflows/test.yml)

This action check urls.

## Inputs

### `url`

**Required** URL to check.

### `status`
**Required** Success status code. Default `200`.

### `method`
**Required** Method for URL. Default `get`.

### `user`
User for base auth

### `password`
Password for base auth

## Example usage

```
uses: wowvendor/url-checker-action@v1
with:
  url: https://www.google.com/
  status: 200
  method: get
```
