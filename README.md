# [r/TaylorSwift](https://www.reddit.com/r/TaylorSwift/) Decronym Bot

This is a reddit bot that provides long versions for song abbreviations used on the [Taylor Swift subreddit](https://www.reddit.com/r/TaylorSwift/)

## ...Why?

American singer-songwriter Taylor Swift has 8 full-length studio albums, and over 150 songs. She has won 10 Grammys, and has the record for the highest number  of single-day streams for any female artist on Spotify.

Given this large discography, Taylor Swift's music is the subject of lots of online discussion, with Tumblr and Reddit being top destinations for fan theories and speculation. Often, long time Taylor Swift fans (so called "Swifties") use abbreviations for songs which leads to posts [like this](https://www.reddit.com/r/TaylorSwift/comments/g5v7fx/every_time_theres_a_post_with_a_song_acronym_i/) from newer fans

From the post:
> Every time there’s a song acronym I feel bad not knowing them. Personally it’s not obvious and I always try to dig through my brain trying to figure it out. Am I the only one? I need a pop up or something for me to figure this out cause sometimes I end up just giving up and so I skip the post.

Now, to help newer fans out, we'd have to monitor every new post coming in and then check if the posts or any comments use uncommon abbreviations. Even in lockdown, a constant Reddit vigil doesn't sound like much fun. So why not automate it?

## Bot Implementation Details and Code

Now up!

```text

Project Structure
ts-decronym-bot
├── .gitignore          # tells git what files to ignore
├── README.md           # this file
├── bot.py              # the code for the bot
├── config.py           # contains global settings
├── discography.json    # contains discography of the artist
├── requirements.txt    # project dependencies
├── songs.json          # bot-generated file containing acronyms
└── utils.py            # contains utility scripts

```

Feel free to take a look and open a pull request if!

## TODOS

* Add unit tests for the `DecronymBot` class
* Make certain config items command line options
