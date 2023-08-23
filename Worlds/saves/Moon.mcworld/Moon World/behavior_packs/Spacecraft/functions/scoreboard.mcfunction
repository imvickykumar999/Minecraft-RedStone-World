scoreboard players add @p[tag=!lua] takeoff 1

execute @p[scores={takeoff=0..20},tag=!lua] ~~~ title @s actionbar Taking off at: 3

execute @p[scores={takeoff=21..40},tag=!lua] ~~~ title @s actionbar Taking off at: 2

execute @p[scores={takeoff=41..60},tag=!lua] ~~~ title @s actionbar Taking off at: 1

execute @p[scores={takeoff=61..80},tag=!lua] ~~~ title @s actionbar Taking off at: 0

execute @p[scores={takeoff=0..80},tag=!chegou] ~~~ execute @e[type=astrocraft:rocket] ~~~ particle minecraft:explosion_manual ~ ~-0.3 ~

execute @p[scores={takeoff=81..1000},tag=!chegou] ~~~ execute @e[type=astrocraft:rocket] ~~~ particle minecraft:basic_flame_particle ~ ~-0.3 ~

execute @p[scores={takeoff=81..1000},tag=!chegou] ~~~ effect @e[type=astrocraft:rocket] levitation 1 5 true

execute @p[scores={takeoff=0..80},tag=!lua] ~~~ camerashake add @p 0.01 5 rotational

