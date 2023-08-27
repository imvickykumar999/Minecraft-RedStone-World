
# https://pypi.org/project/anvil-parser/
import anvil

# Create a new region with the `EmptyRegion` class at 0, 0 (in region coords)
region = anvil.EmptyRegion(0, 0)

# Create `Block` objects that are used to set blocks
note_block = anvil.Block('minecraft', 'note_block')
repeater = anvil.Block('minecraft', 'repeater')

stone = anvil.Block('minecraft', 'stone')
oak_button = anvil.Block('minecraft', 'oak_button')

for z in range(1, 20):
    region.set_block(stone, 1, 79, z)

for z in range(1, 21, 2):
    region.set_block(note_block, 1, 80, z)

for z in range(0, 20, 2):
    region.set_block(repeater, 1, 80, z)

region.set_block(oak_button, 1, 80, 0)
# anvil.errors.OutOfBoundsCoordinates: Block (1, 80, -1) is not inside this region

# Save to a file
region.save('Demo_World/region/r.0.0.mca')
