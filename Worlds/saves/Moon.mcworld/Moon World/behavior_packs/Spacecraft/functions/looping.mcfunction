execute @p[tag=!astrocraft] ~~~ scoreboard objectives add takeoff dummy

execute @p[tag=!astrocraft] ~ ~ ~ scoreboard players set @s takeoff 0

tag @a[tag=!astrocraft] add astrocraft
