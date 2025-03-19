# SHIPCOIN_Imposter
Author: Inalov

## Description

There was a crypto token that claimed it could 'revolutionize' the industry using blockchain, but let's be honest, it was a total flop - it made $0!

However, what's more interesting is another token launched by an APT! This project was also trying to fundraise through an ICO, and what's surprising is how similar it was to the first one: same mission, same website content, even the same TLD!

But enough about that. What's actually important is that an anonymous user suddenly exposed the APT's project on social media.

Your task is to find the ID of the user who made this revelation.

By the way, I almost forgot to mention that this image is all we have from the first project.

Flag format: `FMCTF{Arsenalfan5000}`

## Solution

1. The picture provided is actually a [tweet](https://x.com/shipownerio/status/969628960039587840/) from the original project, `Shipowner`'s Twitter account
2. By searching `"shipowner.io" "apt"` on google we reach to some articles such as the one [Themoloch](https://themoloch.com/infosec/lazarus-group-the-increasingly-infamous-north-korean-hackers/) wrote. In the article we can find out about Lazarus's scam project called "Marine chain"
3. Since the challenge's description hinted us about the TLD, we will search `"MarineChain.io"` on Google
4. There's the [Reddit post](https://www.reddit.com/r/cryptocurrencyscams/comments/8a23za/marine_chainio_north_korea_scam_currency/) mentioned in the description that we have to copy and paste its author's username

NOTE: I got the challenge's idea from [EP 119: Hot Wallets](https://darknetdiaries.com/episode/119/) of Darknet Diaries and I highly encourage you to listen to that episode