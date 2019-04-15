# LED QC Utility

LED video tile QC tool used to determine tile edges on existing, built video walls.
You can input tile width and height to adapt to any sized tile/wall.
I added max height and width to reduce chances of incorrect inputs or drawing a canvas that is far too large.

It will draw a white edge on the last pixel on each edge of the LED tile, so you can determine what tile you need to repair using the grid pattern.

The "a" key will invert the canvas to determine if any of the edge pixels are miscolored or damaged.
The "q" key will close out of the canvas.

I would eventually like to implement a way to save the canvas, so you don't have to reinput tile size or keep cmd.exe opened.
