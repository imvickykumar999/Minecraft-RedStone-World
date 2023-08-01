scoreboard objectives add challenge_start trigger
scoreboard players enable @a challenge_start

scoreboard objectives add timer_standby dummy
scoreboard players set @a timer_standby 0

scoreboard objectives add challenge_h dummy
scoreboard objectives add challenge_min dummy
scoreboard objectives add challenge_sec dummy
scoreboard objectives add challenge_tick dummy

scoreboard objectives add tode deathCount
scoreboard objectives add dragon_dead minecraft.killed:minecraft.ender_dragon
scoreboard players set @a dragon_dead 0
scoreboard players set @a tode 0

scoreboard objectives add life health
scoreboard objectives setdisplay list life

effect give @a minecraft:poison 2 1 true
effect give @a minecraft:regeneration 2 255 true

scoreboard players set @a challenge_start 0
scoreboard players set #timer challenge_tick 0
scoreboard players set #timer challenge_sec 0
scoreboard players set #timer challenge_min 0
scoreboard players set #timer challenge_h 0

tellraw @a {"text":"Datapack loaded!","color":"green"}