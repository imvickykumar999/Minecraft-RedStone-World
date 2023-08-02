
from nbt import nbt
nbtfile = nbt.NBTFile("level.dat", 'rb')

data = nbtfile["Data"]
# data = nbtfile["Data"]['GameRules']

for tag in data.tags:
    print(tag.tag_info())

    if isinstance(tag, nbt.TAG_Compound):
        for i in tag.tags:
            print('\t', i.tag_info())

'''
TAG_String('doWardenSpawning'): true
TAG_String('globalSoundEvents'): true
TAG_String('tntExplosionDropDecay'): false
TAG_String('doFireTick'): true
TAG_String('maxCommandChainLength'): 65536
TAG_String('doVinesSpread'): true
TAG_String('fireDamage'): true
TAG_String('reducedDebugInfo'): false
TAG_String('waterSourceConversion'): true
TAG_String('disableElytraMovementCheck'): false
TAG_String('lavaSourceConversion'): false
TAG_String('announceAdvancements'): true
TAG_String('drowningDamage'): true
TAG_String('commandBlockOutput'): true
TAG_String('forgiveDeadPlayers'): true
TAG_String('doMobSpawning'): true
TAG_String('maxEntityCramming'): 24
TAG_String('disableRaids'): false
TAG_String('doWeatherCycle'): true
TAG_String('mobExplosionDropDecay'): true
TAG_String('doDaylightCycle'): true
TAG_String('showDeathMessages'): true
TAG_String('doTileDrops'): true
TAG_String('universalAnger'): false
TAG_String('playersSleepingPercentage'): 100
TAG_String('snowAccumulationHeight'): 1
TAG_String('doInsomnia'): true
TAG_String('blockExplosionDropDecay'): true
TAG_String('doImmediateRespawn'): false
TAG_String('naturalRegeneration'): true
TAG_String('doMobLoot'): true
TAG_String('fallDamage'): true
TAG_String('keepInventory'): false
TAG_String('doEntityDrops'): true
TAG_String('doLimitedCrafting'): false
TAG_String('mobGriefing'): true
TAG_String('randomTickSpeed'): 3
TAG_String('spawnRadius'): 10
TAG_String('commandModificationBlockLimit'): 32768
TAG_String('doTraderSpawning'): true
TAG_String('freezeDamage'): true
TAG_String('logAdminCommands'): true
TAG_String('spectatorsGenerateChunks'): true
TAG_String('sendCommandFeedback'): true
TAG_String('doPatrolSpawning'): true
'''