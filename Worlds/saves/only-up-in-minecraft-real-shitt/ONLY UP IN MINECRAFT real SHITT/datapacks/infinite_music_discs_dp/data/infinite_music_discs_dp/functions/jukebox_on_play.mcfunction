tag @s add imd_is_playing
execute if data block ~ ~ ~ RecordItem.tag.CustomModelData run tag @s add imd_has_custom_disc
execute as @s[tag=imd_has_custom_disc] run function infinite_music_discs_dp:pre_play
