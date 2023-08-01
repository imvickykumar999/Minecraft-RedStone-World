scoreboard players add #timer challenge_tick 1

execute if score #timer challenge_tick matches 20 run scoreboard players add #timer challenge_sec 1
execute if score #timer challenge_tick matches 20 run scoreboard players set #timer challenge_tick 0

execute if score #timer challenge_sec matches 60 run scoreboard players add #timer challenge_min 1
execute if score #timer challenge_sec matches 60 run scoreboard players set #timer challenge_sec 0

execute if score #timer challenge_min matches 60 run scoreboard players add #timer challenge_h 1
execute if score #timer challenge_min matches 60 run scoreboard players set #timer challenge_min 0

execute if score #timer challenge_sec matches 0..9 if score #timer challenge_min matches 0..9 run title @a actionbar [{"text":"» ","color":"dark_gray","bold":true},{"text":"Timer: ","color":"gold","bold":false},{"score":{"name":"#timer","objective":"challenge_h"},"color":"gold","bold":true},{"text":":","color":"gold","bold":true},{"text":"0","color":"gold","bold":true},{"score":{"name":"#timer","objective":"challenge_min"},"color":"gold","bold":true},{"text":":","color":"gold","bold":true},{"text":"0","color":"gold","bold":true},{"score":{"name":"#timer","objective":"challenge_sec"},"color":"gold","bold":true}]
execute if score #timer challenge_sec matches 0..9 if score #timer challenge_min matches 10.. run title @a actionbar [{"text":"» ","color":"dark_gray","bold":true},{"text":"Timer: ","color":"gold","bold":false},{"score":{"name":"#timer","objective":"challenge_h"},"color":"gold","bold":true},{"text":":","color":"gold","bold":true},{"score":{"name":"#timer","objective":"challenge_min"},"color":"gold","bold":true},{"text":":","color":"gold","bold":true},{"text":"0","color":"gold","bold":true},{"score":{"name":"#timer","objective":"challenge_sec"},"color":"gold","bold":true}]
execute if score #timer challenge_min matches 0..9 if score #timer challenge_sec matches 10.. run title @a actionbar [{"text":"» ","color":"dark_gray","bold":true},{"text":"Timer: ","color":"gold","bold":false},{"score":{"name":"#timer","objective":"challenge_h"},"color":"gold","bold":true},{"text":":","color":"gold","bold":true},{"text":"0","color":"gold","bold":true},{"score":{"name":"#timer","objective":"challenge_min"},"color":"gold","bold":true},{"text":":","color":"gold","bold":true},{"score":{"name":"#timer","objective":"challenge_sec"},"color":"gold","bold":true}] 
execute if score #timer challenge_min matches 10.. if score #timer challenge_sec matches 10.. run title @a actionbar [{"text":"» ","color":"dark_gray","bold":true},{"text":"Timer: ","color":"gold","bold":false},{"score":{"name":"#timer","objective":"challenge_h"},"color":"gold","bold":true},{"text":":","color":"gold","bold":true},{"score":{"name":"#timer","objective":"challenge_min"},"color":"gold","bold":true},{"text":":","color":"gold","bold":true},{"score":{"name":"#timer","objective":"challenge_sec"},"color":"gold","bold":true}]
