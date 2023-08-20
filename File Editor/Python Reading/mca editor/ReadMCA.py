
# pip install anvil-parser
import anvil

region = anvil.Region.from_file('region/r.0.0.mca')
# region = anvil.Region.from_file('entities/r.0.0.mca')
# region = anvil.Region.from_file('poi/r.0.0.mca')

print(region)
# <anvil.region.Region object at 0x0000025BD83A2F70>

# x_z_chunk = region.get_chunk(0,0)
# print(x_z_chunk)

'''
nbt.py", line 543, in __getitem__
    raise KeyError("Tag %s does not exist" % key)
KeyError: 'Tag Level does not exist'
'''

# # You can also provide the region file name instead of the object
# chunk = anvil.Chunk.from_region(region, 0, 0)

# # If `section` is not provided, will get it from the y coords
# # and assume it's global
# block = chunk.get_block(0, 0, 0)

# print(block) # <Block(minecraft:air)>
# print(block.id) # air
# print(block.properties) # {}

# -------------------

# print(help(region))

'''
<anvil.region.Region object at 0x0000011273A62AF0>
Help on Region in module anvil.region object:

class Region(builtins.object)
 |  Region(data: bytes)
 |
 |  Read-only region
 |
 |  Attributes
 |  ----------
 |  data: :class:`bytes`
 |      Region file (``.mca``) as bytes
 |
 |  Methods defined here:
 |
 |  __init__(self, data: bytes)
 |      Makes a Region object from data, which is the region file content
 |
 |      Returns the NBT data for a chunk
 |
 |      Parameters
 |      ----------
 |      chunk_x
 |          Chunk's X value
 |      chunk_z
 |          Chunk's Z value
 |
 |      Raises
 |      ------
 |      anvil.GZipChunkData
 |          If the chunk's compression is gzip
 |
 |      and the length of the chunk in sectors of 4KiB
 |
 |      Will return ``(0, 0)`` if chunk hasn't been generated yet
 |
 |      Parameters
 |      ----------
 |      chunk_x
 |          Chunk's X value
 |      chunk_z
 |          Chunk's Z value
 |
 |  get_chunk(self, chunk_x: int, chunk_z: int) -> 'anvil.Chunk'
 |      Returns the chunk at given coordinates,
 |
 |      Parameters
 |      ----------
 |      chunk_x
 |          Chunk's X value
 |      chunk_z
 |          Chunk's Z value
 |
 |
 |      :rtype: :class:`anvil.Chunk`
 |
 |  Class methods defined here:
 |
 |  from_file(file: Union[str, BinaryIO]) from builtins.type
 |
 |      Parameters
 |      ----------
 |      file
 |          Either a file path or a file object
 |
 |  Static methods defined here:
 |
 |  header_offset(chunk_x: int, chunk_z: int) -> int
 |      Returns the byte offset for given chunk in the header
 |
 |      Parameters
 |      ----------
 |      chunk_x
 |          Chunk's X value
 |      chunk_z
 |          Chunk's Z value
 |
 |  Data descriptors defined here:
 |
 |  data

None
'''