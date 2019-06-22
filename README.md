# Ulauncher Netlify

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-netlify)
[![CircleCI](https://img.shields.io/circleci/build/github/brpaz/ulauncher-netlify.svg?style=for-the-badge)](https://circleci.com/gh/brpaz/ulauncher-netlify)
![License](https://img.shields.io/github/license/brpaz/ulauncher-netlify.svg?style=for-the-badge)


> [ulauncher](https://ulauncher.io/) Extension to easy access your [Netlify](https://netlify.com) projects.

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 3
* [Netlify](https://netlify.com) account and a [Personal Access token](https://app.netlify.com/user/applications).

## Install

First install project dependencies:

```make deps```

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-netlify```

## Usage

* Before usage you need to configure your Netlify "access_token" in plugin preferences.
* The results from the Netlify API are cached by 1h.
* Tap "enter" on a result item will open the respective site while "Alt+Enter" will open the admin of the site in Netlify.

## Development

```
make link
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.


## Contributing

Contributions, issues and Features requests are welcome.

## Show your support

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


## License 

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.
