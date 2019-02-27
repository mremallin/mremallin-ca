Title: Solidoodle 3 Back Online
Category: Projects
Tags: 3d-printing
Slug: solidoodle-3-back-online
Authors: Mike Mallin
Summary: Calibration, calibration, calibration...
Date: 2019-02-26
Logo: {static|images/PhoneHolderComplete.JPG}
Gallery:
    {static|images/RiserPart1.JPG}||Part way through the coffee machine riser
    {static|images/RiserPart2.JPG}||About to start the lip
    {static|images/RiserComplete.JPG}||Coffee machine riser completed
    {static|images/PhoneHolderFailure.JPG}||Failed print of a phone holder I found
    {static|images/PhoneHolderComplete.JPG}||The printed phone holder

I have a new project on the way that's going to need a bit of room in my basement. After re-organizing I needed a place for my Solidoodle 3 to live. Turns out there's plenty of space by my desk to keep it around. It was a bit of an ordeal to get it back online and printing nicely.

# Step the First: Where's Solidoodle?
Turns out that Solidoodle went out of business a few years back. This put a bit of a wrench into things as their [site was practically closed](http://www.solidoodle.com/), save for some software links. The software currently posted is not compatible with my (older) printer. The software that does work was a package based on Repetier and Slic3r. I found a site that's still hosting them [here](http://www.soliwiki.com/Official_Solidoodle_Software_Download). The one you would need is the 'Repetier Host Package.'

# Step the Second: Linux?
It's really awesome that there is an available Linux package. Personally, I'd prefer to run a version that's a bit more up to date. In this case, I installed Repetier and Slic3r from the Arch User Repository for my desktop. Now that I had software, I needed calibration information

# Step the Third: Windows?
I installed the Repetier host software on my Windows partition as that's how I used to use it. I knew that worked in the past so that's where I started today. Once it was installed, I spent a bit of time digging through the files for Repetier and Slic3r to get the base settings for the printer to base my own calibrations from.

# Step the Fourth: Calibrate, calibrate some more, and do it again.
After I had the base settings, I followed the [calibration guide](http://wiki.solidoodle.com/solidoodle-1) that I found. Seriously, levelling the bed was one of the best things that improved my print quality since the last time I tried a few years ago. I used to have issues with prints lifting and flying away almost every time. Now it's been reduced to odd or thin parts. I've posted my current settings below for future reference.

# Step the Fifth: What's next?
Printing more things of course! In order to do that, I need software to create the parts. I came across [FreeCAD](https://www.freecadweb.org/) which seems to be a decent drop-in replacement for SolidWorks. I'll talk some more about it and post the part I made in a future post.
[The phone holder showcased is from here.](https://www.thingiverse.com/thing:3109785)

Filament (ABS)
<ul>
    <li>Diameter: 1.74mm</li>
    <li>Extrusion Multiplier: 0.68</li>
    <li>Temperature:</li>
    <ul>
        <li>Extruder: First Layer - 208, Other Layers - 203</li>
        <li>Bed: First Layer - 95, Other Layers - 90</li>
    </ul>
</ul>

Print Settings
<ul>
<u>Layers and perimeters</u>
    <li>Layer height: 0.3mm</li>
    <li>First layer height: 0.35mm</li>
    <li>Vertical shells: 3</li>
    <li>Solid layers: Top - 3, Bottom - 3</li>
    <li>Extra permimeters if needed: Yes</li>
    <li>Avoid crossing perimeters</li>
    <li>Detect thin walls: Yes</li>
    <li>Detect bridging permiters: Yes</li>
    <li>Seam position: Aligned</li>
<u>Infill</u>
    <li>Fill density: 10% (Changes per print)</li>
    <li>Fill pattern: Rectilinear (Changes per print)</li>
    <li>Combine infill every: 1 layer</li>
    <li>Fill gaps: Yes</li>
    <li>Fill angle: 45</li>
    <li>Solid infill threshold area: 70</li>
    <li>Only retract when crossing perimeters: Yes</li>
<u>Skirt and brim</u>
    <li>Loops (minimum): 3</li>
    <li>Distance from object: 5mm</li>
    <li>Skirt height: 1 layer</li>
    <li>Exterior brim width: 3mm</li>
    <li>Interior brim width: 3mm</li>
<u>Speed</u>
    <li>Perimiters: 30mm/s</li>
    <li>-> Small: 30mm/s</li>
    <li>-> External: 70%</li>
    <li>Infill: 50mm/s</li>
    <li>-> Solid: 50mm/s</li>
    <li>-> Top Solid: 50mm/s</li>
    <li>-> Gaps: 20mm/s</li>
    <li>Bridges: 60mm/s</li>
    <li>Support Material: 60mm/s</li>
    <li>Travel: 130mm/s</li>
    <li>First layer speed: 30mm/s</li>
<u>Advanced</u>
    <li>Default extrusion width: 0.42mm</li>
    <li>First layer: 220%</li>
    <li>Infill/perimeters overlap: 55%</li>
</ul>

Printer Settings
<ul>
<u>General</u>
    <li>Bed Shape: x - 195mm, y - 195mm</li>
    <li>Speed: 250000</li>
    <li>G-code flavor: RepRap (Marlin/Sprinter)</li>
<u>Custom G-code</u>
    <li>See below</li>
<u>Extruder 1</u>
    <li>Nozzle diameter: 0.4mm</li>
    <li>Min limit: 0.15mm</li>
    <li>Max limit: 0.3mm</li>
    <li>Extruder offset: x - 0mm, y - 0mm</li>
    <li>Retraction length: 1mm</li>
    <li>Retraction speed: 30mm/s</li>
    <li>Minimum travel after retraction: 2mm</li>
    <li>Retract on layer change: Yes</li>
</ul>
Starting G-code:

>     G21; set mm units
>     G90; set absolute coordinates
>     G28 X0 Y0; home x and y axes
>     G1 X100 Y100 F4000; move extruder above bed
>     G28 Z0; home Z axis
>     G92 E0; reset extrusion distance

End G-code:

>     G92 E0; reset extrusion distance
>     G1 E-3 F1000; linear move, retract 3mm extruder, 1000mm/s feedrate
>     G28 X0 Y0; home X, Y axis
