execute if entity @a[scores={challenge_start=1..}] run function timer:timer
execute if entity @a[scores={challenge_start=1}] run scoreboard players set @s challenge_h 0
execute if entity @a[scores={challenge_start=1}] run scoreboard players set @s challenge_min 0
execute if entity @a[scores={challenge_start=1}] run scoreboard players set @s challenge_sec 0
execute if entity @a[scores={challenge_start=1..}] run scoreboard players set @s challenge_start 2

execute if score #timer challenge_min matches 0 if score #timer challenge_sec matches 0 if score #timer challenge_tick matches 0 if score #timer challenge_h matches 0 run title @a actionbar [{"text":"» ","color":"dark_gray","bold":true},{"text":"Timer: ","color":"gold","bold":false},{"text":"paused","color":"red","bold":false,"italic":true}]

#Sobald Drache tot, Timer anhalten
execute if entity @a[scores={dragon_dead=1..}] run scoreboard players set @a[scores={challenge_start=1..}] timer_standby 1
execute if entity @a[scores={dragon_dead=1..}] run scoreboard players set @a[scores={challenge_start=1..}] challenge_start 0
execute if entity @a[scores={dragon_dead=1..}] run scoreboard players set @a dragon_dead 0

#Special Case: Wenn Drache mit Betten oder anderweitig stirbt, wird kontrolliert, ob der Spieler ins Portal geht um dann den Timer anzuhalten
execute as @a at @s if block ~ ~ ~ end_portal if block ~ ~-1 ~ bedrock run scoreboard players set @a timer_standby 1
execute if entity @a[scores={timer_standby=1}] run scoreboard players set @a challenge_start 0

#Sobald Spieler tot, Timer anhalten
execute if entity @a[scores={tode=1..}] run gamemode spectator @a
execute if entity @a[scores={tode=1..}] run scoreboard players set @a[scores={challenge_start=1..}] timer_standby 1
execute if entity @a[scores={tode=1..}] run scoreboard players set @a[scores={challenge_start=1..}] challenge_start 0
execute as @a[scores={tode=1..},gamemode=spectator] run scoreboard players set @s tode 0

#Solange timer_standby = 1 -> Timer nur anzeigen, nicht weiterzählen
execute if entity @a[scores={timer_standby=1..}] run execute if score #timer challenge_sec matches 0..9 if score #timer challenge_min matches 0..9 run title @a actionbar [{"text":"» ","color":"dark_gray","bold":true},{"text":"Timer: ","color":"gold","bold":false},{"score":{"name":"#timer","objective":"challenge_h"},"color":"red","bold":false},{"text":":","color":"red","bold":false},{"text":"0","color":"red","bold":false},{"score":{"name":"#timer","objective":"challenge_min"},"color":"red","bold":false},{"text":":","color":"red","bold":false},{"text":"0","color":"red","bold":false},{"score":{"name":"#timer","objective":"challenge_sec"},"color":"red","bold":false}]
execute if entity @a[scores={timer_standby=1..}] run execute if score #timer challenge_sec matches 0..9 if score #timer challenge_min matches 10.. run title @a actionbar [{"text":"» ","color":"dark_gray","bold":true},{"text":"Timer: ","color":"gold","bold":false},{"score":{"name":"#timer","objective":"challenge_h"},"color":"red","bold":false},{"text":":","color":"red","bold":false},{"score":{"name":"#timer","objective":"challenge_min"},"color":"red","bold":false},{"text":":","color":"red","bold":false},{"text":"0","color":"red","bold":false},{"score":{"name":"#timer","objective":"challenge_sec"},"color":"red","bold":false}]
execute if entity @a[scores={timer_standby=1..}] run execute if score #timer challenge_min matches 0..9 if score #timer challenge_sec matches 10.. run title @a actionbar [{"text":"» ","color":"dark_gray","bold":true},{"text":"Timer: ","color":"gold","bold":false},{"score":{"name":"#timer","objective":"challenge_h"},"color":"red","bold":false},{"text":":","color":"red","bold":false},{"text":"0","color":"red","bold":false},{"score":{"name":"#timer","objective":"challenge_min"},"color":"red","bold":false},{"text":":","color":"red","bold":false},{"score":{"name":"#timer","objective":"challenge_sec"},"color":"red","bold":false}] 
execute if entity @a[scores={timer_standby=1..}] run execute if score #timer challenge_min matches 10.. if score #timer challenge_sec matches 10.. run title @a actionbar [{"text":"» ","color":"dark_gray","bold":true},{"text":"Timer: ","color":"gold","bold":false},{"score":{"name":"#timer","objective":"challenge_h"},"color":"red","bold":false},{"text":":","color":"red","bold":false},{"score":{"name":"#timer","objective":"challenge_min"},"color":"red","bold":false},{"text":":","color":"red","bold":false},{"score":{"name":"#timer","objective":"challenge_sec"},"color":"red","bold":false}]