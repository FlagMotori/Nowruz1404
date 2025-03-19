# Somewhere_Near_The_Bay_Part_1
Author: Inalov

## Description

I've got a panorama picture of a landscape that I downloaded from Google Maps. I bet you can't find the exact location.

What's the location's What3Words? (don't put `\\\` inside the flag)

You might need to use [this](https://renderstuff.com/tools/360-panorama-web-viewer/) or [this](https://photo-sphere-viewer.js.org/playground.html)

Flag: `FMCTF{hedge.preset.shape}`

## Solution

1. By doing a reverse search image on the bus we find out that the location we're looking for has been located at `Acadia National Park`
2. Search `"Acadia National Park" "bus route"` on Google and go the `images` tab to find map of different bus routes at the park
3. By looking at [ISLAND EXPLORER ROUTE FINDER - 2025](https://www.exploreacadia.com/routefinder.html) and knowing the place we're looking for is somewhere near the water, we'll examine different places at the park
4. The place we look for is [Thunder Hole](https://maps.app.goo.gl/WTMbA77h8RdaJz3QA) but since we need the exact location of the [picture](https://maps.app.goo.gl/WTMbA77h8RdaJz3QA) we must turn on Street View mode on Google Maps by clicking on the yellow man icon.
5. The location is `44.320672430751685, -68.18809484595782` and we have to copy and paste it on [what3words](https://what3words.com/)