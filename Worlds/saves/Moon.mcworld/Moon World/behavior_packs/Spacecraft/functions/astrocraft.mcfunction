tag @s add chegou
tag @s add lua

execute @s[tag=lua] ~~~ structure load moon 20000 150 20000 0_degrees x block_by_block

execute @s[tag=lua] ~~~ tp @e[type=astrocraft:rocket] 20011 180 20009

tp 20037 190 20011
effect @s slow_falling 10 1 true





