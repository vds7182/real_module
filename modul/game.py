import models
import random
import settings
from exeption import game_over
def attack(player,enemy):
    attack_result=fight(player,enemy)
    if(attack_result==0):
        print('draw')
    if (attack_result == 1):
        print('You hit him ')
        settings.enemy_live-=1
    if (attack_result == -1):
        print('You missed')
    return f"Enemy's HP:{settings.enemy_live}"
def defence(player,enemy):
    defence_result=fight(player, enemy)
    print(defence_result)
    if (defence_result == 0):
        print('draw')
    if (defence_result == 1):
        print( 'You blocked him succssefully')
    if (defence_result == -1):
        print('You get hit')
        settings.player_live-=1
    return f"Your's HP:{settings.player_live}"
def fight(player,enemy):
    if player==1 and enemy==2:
        return 1
    if player==1 and enemy==3:
        return -1
    if player==1 and enemy==1:
        return 0
    if player==2 and enemy==3:
        return 1
    if player==2 and enemy==1:
        return -1
    if player==2 and enemy==2:
        return 0
    if player==3 and enemy==1:
        return 1
    if player== 3 and enemy==2:
        return -1
    if player==3 and enemy==3:
        return 0

print("Welcome to the game\nPlease enter your nickname")
name=input()
save_player_live=settings.player_live
save_enemy_live=settings.enemy_live
print("Please select action\n1.Start\n2.Clear leaderboard\n3.Exit")
start=input()
if start=='1':
    # character=1
    # enemy_character=random.randint(1,3)
    # final_character=models.Player(character)
    # final_enemy_character = models.Enemy(enemy_character)
    # character_class=final_character.player_class(character)
    # enemy_class=final_enemy_character.enemy_class(enemy_character)
    count_of_enemys_death=1
    score=0
    count_of_rounds = 1
    while(settings.player_live>0):
        print("Choose your class to attack the enemy\n1.Wizard\n2.Warrior\n3.Rogue")
        character = int(input())
        final_character = models.Player(character)
        character_class = final_character.player_class(character)
        enemy_character = random.randint(1, 3)
        final_enemy_character = models.Enemy(enemy_character)
        final_enemy_character = models.Enemy(enemy_character)
        print("You selected: "+final_character.player_class(character)+'\nEnemy selected: '+final_enemy_character.enemy_class(enemy_character))
        print(attack(character, enemy_character))
        if settings.enemy_live==0:
            count_of_enemys_death += 1
            new_enemy_lives=models.Lives(settings.enemy_live,count_of_enemys_death)
            final_enemy_lives=new_enemy_lives.next_level(settings.enemy_live,count_of_enemys_death)
            count_of_rounds+=1
            check_score=models.Score(settings,score)
            final_score=check_score.count_score(settings.enemy_live,score)
            score=final_score
            print("You win the battle congratulations!\nBut be careful with the next enemy\nThis is your score "+str(final_score)+'\n Get ready for the next battle'+'\n Round '+str(count_of_rounds))
            settings.enemy_live=final_enemy_lives
        print("Choose your class to defend yourself\n1.Wizard\n2.Warrior\n3.Rogue")
        character = int(input())
        final_character = models.Player(character)
        character_class = final_character.player_class(character)
        enemy_character = random.randint(1, 3)
        final_enemy_character = models.Enemy(enemy_character)
        final_enemy_character = models.Enemy(enemy_character)
        print("You selected: " + final_character.player_class(character) + '\nEnemy selected: ' + final_enemy_character.enemy_class(enemy_character))
        print(defence(character, enemy_character))
        if settings.player_live==0:
            file_leader=open("score.txt",'a')
            file_leader.write(name)
            file_leader.write(' ')
            file_leader.write(str(score))
            file_leader.write('\n')
            print(game_over(settings.player_live))
            print('Wanna try again (y/n)')
            choise=input()
            if(choise=='y'):
                settings.player_live=save_player_live
            else:
                print('Bye')
                break
if start=="2":
    with open("score.txt", 'r+') as f:
        f.truncate()
    #я тут нету особо комманд поэтому я решил вместо help написать это