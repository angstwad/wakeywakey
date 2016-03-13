# wakeywakey
Continuously mark your Slack presence as active - never appear away!

## Installation

```
pip install wakeywakey
```

or

```
pip install git+https://github.com/angstwad/wakeywakey.git
```

## Use

### Generate Slack Token

The easiest solution is to generate a test token in the [Slack API](https://api.slack.com/docs/oauth-test-tokens) or follow the docs [http://api.slack.com/web](http://api.slack.com/web).

### Running App

By default, `wakeywakey` runs forever and doesn't generate any output unless the Slack API returns an error.

```
$ wakeywakey <your-token-here>
```

`wakeywakey`'s arguments:

```
positional arguments:
  token                 Slack OAuth token

optional arguments:
  -h, --help            show this help message and exit
  --run-once            Sets user as active and exits.
  -i INTERVAL, --interval INTERVAL
                        Interval (seconds) at which Slack API is contacted.
                        Default: 300
```

### Running Forever on OS X

As I'm an OS X user, I figured I'd make this a bit easier for you to run at login like I do.

Below is an example _launchd_ job file.  Copy this to a new file and:

 * replace with your client OAuth test key
 * update path to `wakeywakey` to actual path after install (you can find this by running `which wakeywakey` in the terminal)

My example plist runs with an interval of 60 seconds.

Install this file to `~/Library/LaunchAgents/com.angstwad.wakeywakey.plist`.  You'll need to log out and log back in (I think) in order for this to take effect or will need to be manually loaded with `launchctl`.

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<true/>
	<key>Label</key>
	<string>com.angstwad.wakeywakey</string>
	<key>Program</key>
	<string>/path/to/wakeywakey</string>
	<key>ProgramArguments</key>
	<array>
		<string>/path/to/wakeywakey</string>
		<string>-i</string>
		<string>60</string>
		<string>your oauth token goes here</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
</dict>
</plist>

```
