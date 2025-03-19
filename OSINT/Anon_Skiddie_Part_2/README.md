# Anon_Skiddie_Part_2
Author: Inalov

## Description

This dude is really ambitious. He literally begged us to let him attend our post-event meeting and we said yes.

Since he's not good at time management, our organizer sent him the event's `.ics` file and asked him to import it to his calendar. What can go wrong?


Flag: `FMCTF{M4Y83_1M_n07_7H47_4n0Nym0U5}`

## Solution

### 1st option
1. Go the Google calendar
2. Paste the Email we've found in the `Search for people` section and hit Enter
3. An event will show up on the calendar
4. Click on the event and copy the string on the description section `1PDw-S4ZXQbGuKBNayEz6XqtiA6tl1lcOBT4nI1IFaac`
5. Paste it at the end of a [Google Drive URL](https://docs.google.com/document/d/1PDw-S4ZXQbGuKBNayEz6XqtiA6tl1lcOBT4nI1IFaac)
6. Copy the base64 string and decode it

### 2nd option
Using Ghunt as its documents instructs by providing the email we've found from the previous challenge
