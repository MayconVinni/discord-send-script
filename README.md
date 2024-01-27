# discord-send-script

Python code to send entire scripts to Discord text channels.
Inspired by [SendScriptWhatsApp](https://github.com/Matt-Fontes/SendScriptWhatsApp).

## Arguments

This program uses `argparse` to handle terminal arguments and making the program easier to use.

### Positional

`filename` The filename of the script inside the 'scripts' directory.

`channel_id` ID of the text channel where the script will be sent.

`token` Token of the user.

### Options

`-d TIME, --delay TIME` Delay before sending another message (in seconds).
Default to `1.0` to avoid HTTP error 429 (Too Many Requests).

`-v, --verbose` Prints in the terminal the lines sent, the ID of all messages sent and its content.

### Example

```
python main.py shrek.txt 1234567890 TOKEN_HERE_ISiDjNDLsOSoFKFnFl --delay=2.0 --verbose
```

This will send the entire script of `shrek.txt`
line by line every `2.0` seconds (`--delay=2.0`)
to the channel of the ID `1234567890`
by using your token `TOKEN_HERE_ISiDjNDLsOSoFKFnFl`
and will print the line, the ID and the content of the message sent in the terminal (`--verbose`).

## Questions and Answers

Some questions and answers before you can start using this program.

### I can use my bot token?

I already tested it and no, you can't. (I tested with `"Bot TOKEN_HERE_ISiDjNDLsOSoFKFnFl"` instead of just `TOKEN_HERE_ISiDjNDLsOSoFKFnFl`.)

### Is this against Discord's TOS?

Idk, but it prob is.
