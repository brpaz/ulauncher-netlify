# Ulauncher Netlify

> [ulauncher](https://ulauncher.io/) Extension to easy access your [Netlify](https://netlify.com) projects.

## Usage

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-netlify```

## Usage

* Before usage you need to configure your Netlify "access_token" in plugin preferences.
* The results from the Netlify API are cached by 1h.
* Tap "enter" on a result item will open the respective site while "Alt+Enter" will open the admin of the site in Netlify.

## Development

```
git clone https://github.com/brpaz/ulauncher-netlify
cd ~/.cache/ulauncher_cache/extensions/ulauncher-netlify
ln -s <repo_location> ulauncher-netlify
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## License 

MIT
