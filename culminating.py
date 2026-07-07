"""
Here are the APA citations for your references:

Photo References
All base cards (ace, king, queen, jack, etc…).
    (n.d.). Balatro. Retrieved from https://www.nexusmods.com/balatro/mods/131
All jokers.
    (n.d.). Balatro Wiki. Retrieved from https://balatrogame.fandom.com/wiki/Jokers
All Blinds.
    (n.d.). Balatro Wiki. Retrieved from https://balatrogame.fandom.com/wiki/Blinds_and_Antes
Font Download
    Managore. (n.d.). M6x11. Retrieved from https://managore.itch.io/m6x11
Backing Track
    FrogRadio. (2024, March 14). Main Theme (1 Hour) - Balatro [Video]. YouTube. http://www.youtube.com/watch?v=Y_EVa7P9w-s
Info Button 
    (n.d.). Retrieved from https://www.freeiconspng.com/img/6086
Coding References
straight concept inspiration
    stackoverflow. (2016). Identifying a straight from poker using python. Retrieved from https://stackoverflow.com/questions/34684816/identifying-a-straight-from-poker-using-python

Pygame Zero Help.
(n.d.). Retrieved from https://app.readthedocs.org/projects/pygame-zero/downloads/pdf/latest/
(n.d.). Retrieved from https://docs.google.com/document/d/1AMdIZqkLNseAYPWFs1YUPNRug4uXMgt0vApsWCK8wzg/edit?tab=t.0#heading=h.aa2z3weuwkwz

"""

import os

os.environ["SDL_VIDEO_WINDOW_POS"] = "0,0"
import random, pgzrun, math, time
from pgzhelper import *

# from pgz zero cheat sheet

WIDTH = 1300
HEIGHT = 950

# Varables
info_button = Actor('info.png')
background = Actor("placeholder.png")
card_actors = []
app = Actor("placeholder.png")
app.stage = "title"
game = Actor("placeholder.png")
hands_info = Actor('base_hand.png')
hands_info.state = 'hands'
game.stage = "clear"
# draw is for gameplay. i.e. selecting cards
# clear is to completely remove already prexisting cards
# stall is to have a period of which the gameplay is visible
# math is for the adding of the bonusxmult total
# Won is to change blind
max_card = 5
cards_selected = []
box_draw = False
joker_output = []
jokers = []
joker_actors_nongame = []
joker_actors_ingame = []
hand_type = None
card_count = 0
bonus_count = 0
mult_count = 0
card_count = 0
jrd_mode = False 
randomised_cards = None
cards_stored = []
cards_used = []
blinds = []
blind = Actor("small_blind.png", (248, 100))
# stages: small, big, boss (boss will have an randint to call)
blind.stage = "small"
# Base set of cards Format = [suit,rank,image,value]
base_blind = [300, 800, 2000, 50, 11000]
ante_count = 1
round_count = 0
discard_count = 3
discard_total = 0
play_count = 3
play_total = 0
blind_requirement = None
boss = None
used_ante = []
chip = Actor("chips.png")
chip2 = Actor("chips.png")
chip3 = Actor("chips.png")
chip_count = 0
music.play("theme.mp3")
win_popup = Actor("win_screen.png")
win_button = Actor("win_button.png")
money = 0
joker_hover = False
joker_indeck = []
joker_pos_ingame = None
joker_pos_nongame = None
restricted_suit = None

#joker varables 
current_mult = 20
bonus_total = 0
current_bonus = 50
current_mult_multi = 2
empty = 5
total_cards_discarded = 0
total_cards_discarded_two = 0
hand_types = []

#End game varables
end_screen = Actor('ending_screen.png')
jokers_bought = 0
jokers_sold = 0
cards_discarded = 0
most_played_hand = []
best_hand = 0
cards_counted = 0
hands_played = 0

cards = [
    ["spade", "14", "0.png", 11],
    ["spade", "2", "1.png", 2],
    ["spade", "3", "2.png", 3],
    ["spade", "4", "3.png", 4],
    ["spade", "5", "4.png", 5],
    ["spade", "6", "5.png", 6],
    ["spade", "7", "6.png", 7],
    ["spade", "8", "7.png", 8],
    ["spade", "9", "8.png", 9],
    ["spade", "10", "9.png", 10],
    ["spade", "11", "10.png", 10],
    ["spade", "12", "11.png", 10],
    ["spade", "13", "12.png", 10],
    ["club", "14", "13.png", 11],
    ["club", "2", "14.png", 2],
    ["club", "3", "15.png", 3],
    ["club", "4", "16.png", 4],
    ["club", "5", "17.png", 5],
    ["club", "6", "18.png", 6],
    ["club", "7", "19.png", 7],
    ["club", "8", "20.png", 8],
    ["club", "9", "21.png", 9],
    ["club", "10", "22.png", 10],
    ["club", "11", "23.png", 10],
    ["club", "12", "24.png", 10],
    ["club", "13", "25.png", 10],
    ["heart", "14", "26.png", 11],
    ["heart", "2", "27.png", 2],
    ["heart", "3", "28.png", 3],
    ["heart", "4", "29.png", 4],
    ["heart", "5", "30.png", 5],
    ["heart", "6", "31.png", 6],
    ["heart", "7", "32.png", 7],
    ["heart", "8", "33.png", 8],
    ["heart", "9", "34.png", 9],
    ["heart", "10", "35.png", 10],
    ["heart", "11", "36.png", 10],
    ["heart", "12", "37.png", 10],
    ["heart", "13", "38.png", 10],
    ["diamond", "14", "39.png", 11],
    ["diamond", "2", "40.png", 2],
    ["diamond", "3", "41.png", 3],
    ["diamond", "4", "42.png", 4],
    ["diamond", "5", "43.png", 5],
    ["diamond", "6", "44.png", 6],
    ["diamond", "7", "45.png", 7],
    ["diamond", "8", "46.png", 8],
    ["diamond", "9", "47.png", 9],
    ["diamond", "10", "48.png", 10],
    ["diamond", "11", "49.png", 10],
    ["diamond", "12", "50.png", 10],
    ["diamond", "13", "51.png", 10],
]

def nuke_game():
    """Completely resets all game variables including progress"""
    global card_actors, cards_selected, box_draw, joker_output, jokers, joker_actors_nongame
    global hand_type, card_count, bonus_count, mult_count, randomised_cards, cards_stored
    global cards_used, blinds, blind, base_blind, ante_count, discard_count, joker_indeck
    global discard_total, blind_requirement, boss, used_ante, chip_count, hand_types
    global play_count, play_total, round_count, money, win_popup, win_button
    global current_mult, bonus_total, current_bonus, current_mult_multi, empty, total_cards_discarded
    global joker_actors_ingame, joker_pos_ingame, joker_pos_nongame, restricted_suit
    global hands_played, jokers_bought, jokers_sold, cards_discarded, most_played_hand, best_hand, cards_counted

    # Reset all game state variables
    reset_game_state()

    # Reset permanent progress variables
    money = 0
    round_count = 0
    ante_count = 1
    hands_played = 0
    jokers_bought = 0
    jokers_sold = 0
    cards_discarded = 0
    cards_counted = 0
    best_hand = 0
    most_played_hand.clear()

    # Reset joker-related variables
    joker_indeck.clear()
    joker_actors_ingame.clear()
    joker_pos_ingame = None
    joker_pos_nongame = None

    # Reset blind/boss variables
    blind.stage = "small"
    blind.image = "small_blind.png"
    restricted_suit = None
    used_ante.clear()

    # Reset joker modifiers
    current_mult = 20
    bonus_total = 0
    current_bonus = 50
    current_mult_multi = 2
    empty = 5
    total_cards_discarded = 0
    total_cards_discarded_two = 0

    # Reset UI elements
    win_popup.midtop = (640, HEIGHT)
    win_button.midtop = (645, win_popup.y - 20)

    # Reload game data
    get_jokers()
    get_blinds()
    get_boss()
    joker_printing()

def reset_game_state():
    """Resets in-game state variables while preserving progress stats"""
    global card_actors, cards_selected, box_draw, joker_output
    global hand_type, card_count, bonus_count, mult_count, randomised_cards, cards_stored
    global cards_used, blind_requirement, chip_count, hand_types
    global discard_count, discard_total, play_count, play_total

    # Reset card-related variables
    card_actors.clear()
    cards_selected.clear()
    box_draw = False
    card_count = 0
    randomised_cards = None
    cards_stored.clear()
    cards_used.clear()
    hand_type = None
    hand_types.clear()

    # Reset scoring variables
    bonus_count = 0
    mult_count = 0
    chip_count = 0

    # Reset game state variables
    game.stage = "clear"
    blind_requirement = None

    # Reset counters (but preserve round progress)
    discard_count = 3
    discard_total = 0
    play_count = 3
    play_total = 0

    # Reset UI elements
    win_popup.midtop = (640, HEIGHT)
    win_button.midtop = (645, win_popup.y - 20)

#unlocks the secret mode/joker
def on_key_down(key):
    global jrd_mode
    if keyboard.J and keyboard.R and keyboard.D:
        jrd_mode = True
 
# money math and blind changer i.e small -> big -> boss
def money_maker():
    global money
    global round_count
    global play_count
    global ante_count
    global joker_indeck
    if blind.stage == "small":
        money += 3
        blind.stage = "big"
    elif blind.stage == "big":
        money += 4
        blind.stage = "boss"
    else:
        money += 5
        blind.stage = 'small'
        ante_count += 1
    money += play_count
    round_count += 1
    joker_indeck_name = []
    for i in joker_indeck:
        joker_indeck_name.append(i[1])
    if joker_indeck_name.count(["golden","golden_joker.png","$3 at the end of each round","cash_joker",3]) == 1:
        golden()

#shows the money process without it changing stages, this is purely for display 
def money_display():
    global money
    global joker_indeck
    money_display = 0
    global play_count
    if blind.stage == "small":
        money_display += 3
    elif blind.stage == "big":
        money_display += 4
    else:
        money_display += 5
    money_display += play_count
    joker_indeck_name = []
    for i in joker_indeck:
        joker_indeck_name.append(i[1])
    if joker_indeck.count(["golden","golden_joker.png","$3 at the end of each round","cash_joker",3]) == 1:
        golden()
    return money_display

# gets jokers from the joker.txt file
def get_jokers():
    global jokers
    global current_mult
    global bonus_total
    global current_bonus
    global current_mult_multi
    global empty
    global current_cards_discarded
    jokers.clear()
    file = open("joker_save.txt")

    contents = file.read()

    for joker in contents.splitlines():

        jokers.append(eval(joker))

    file.close()
get_jokers()

def shop_jokers():
    global jokers
    global joker_actors_ingame
    global joker_indeck
    global jrd_mode
    
    joker_actors_ingame.clear()
    random_picks = []
    ran_num = None
    already_bought = []
    for i in joker_indeck:
        already_bought.append(i[2])
    # if secret mode is on it'll allow for the last/secret joker to be selected
    if jrd_mode == False:
        while len(random_picks) < 3:
            ran_num = random.randint(0,len(jokers) - 2)
            if random_picks.count(ran_num) == 0 and already_bought.count(ran_num) == 0: 
                random_picks.append(ran_num)
    else:
        while len(random_picks) < 3:
            ran_num = random.randint(0,len(jokers) - 1)
            if random_picks.count(ran_num) == 0 and already_bought.count(ran_num) == 0: 
                random_picks.append(ran_num)
    random_jokers = {}
    #creates the acutal jokers for the shop
    for i in random_picks:
        random_jokers[i] = Actor(jokers[i][1])
        random_jokers[i].selected = False
        random_jokers[i].bought = False
        # FORMAT joker_actors_ingame
        # Actor, Joker, Randomised Number
        joker_actors_ingame.append([random_jokers[i],jokers[i],i])

    #gets blinds from the blinds.txt file 
def get_blinds():
    global blinds
    blinds.clear()

    file = open("blinds.txt")

    contents = file.read()
    suit = "suit"

    for blind in contents.splitlines():

        blinds.append(eval(blind))

    file.close()

get_blinds()

#gets a boss every single ante if the boss is 'the suit' it'll creat the restricted suit in the function 
def get_boss():
    global boss
    global blinds
    global restricted_suit
    random_boss = random.randint(2, 7)
    boss = blinds[random_boss]
    if boss[0] == "The Suit":
        suits = ['spade', 'diamond', 'heart', 'club']
        restricted_suit = suits[random.randint(0,3)]

# Every Joker Function
def acrobat():
    global mult_count
    global play_count
    if play_count == 1:
        mult_count *= 3
def baron(rank):
    global mult_count
    # Format [actor,[suit,rank,image,value],randomised value]
    if int(rank) == 13:
        mult_count *= 1.5
def bootstraps():
    global mult_count
    global money

    mult_count += (money//5) * 3
def bull():
    global bonus_count
    global money

    bonus_count += (money//2) * 5
def burning_joker():
    global total_cards_discarded
    global bonus_count
    bonus_count += (total_cards_discarded) * 2
def cavendish():
    global mult_count
    global joker_indeck
    removing = None
    for i in joker_indeck:
        if i[1][0] == "cavendish":
            removing = i
    mult_count *= 3

    random_chance = random.randint(1,10)
    if random_chance == 3:
        joker_indeck.remove(removing)
def club_check(suit):
    global mult_count
    if suit == 'club':
        mult_count += 3
def dementia():
    global mult_count
    global hand_types
    global hand_type
    if hand_types.count(hand_type) > 0:
        mult_count *= 3
    hand_types.append(hand_type)
def diamond_check(suit):
    global mult_count
    if suit == 'diamond':
        mult_count += 3
def flush_joker():
    global hand_type
    global bonus_count
    if hand_type == 'flush' or hand_type == 'straight flush' or hand_type == 'royal flush':
        bonus_count += 70
def golden():
    global money
    money += 3
def half():
    global cards_selected
    global mult_count
    if len(cards_selected) <= 3:
        mult_count += 20
def heart_check(suit):
    global mult_count
    if suit == 'heart':
        mult_count += 3
def hit_the_road(rank):
    global bonus_count
    if int(rank) == 11:
        bonus_count += 25
def ice_cream():
    global current_bonus
    global bonus_count
    global joker_indeck
    removing = None
    for i in joker_indeck:
        if i[1][0] == "ice cream":
            removing = i
    bonus_count += current_bonus
    current_bonus -= 5
    if current_bonus == 0:
        joker_indeck.remove(removing)
def joker():
    global mult_count
    global bonus_count
    mult_count += 4
    bonus_count += 4 
def monarch(rank):
    global mult_count
    if int(rank) == 12:
        mult_count += 18
def pair_joker():
    global hand_type
    global bonus_count
    if hand_type == 'pair' or hand_type == 'three of a kind' or hand_type == "four of a kind" or hand_type == "full house":
        bonus_count += 15
def popcorn():
    global current_mult
    global mult_count
    global joker_indeck
    removing = None
    for i in joker_indeck:
        if i[1][0] == "popcorn":
            removing = i
    mult_count += current_mult
    current_mult -= 4
    if current_mult == 0:
        joker_indeck.remove(removing)
def ramen():
    global current_mult_multi
    global mult_count
    global joker_indeck
    global total_cards_discarded_two
    removing = None
    for i in joker_indeck:
        if i[1][0] == "ramen":
            removing = i
    if current_mult_multi <= 0:
        joker_indeck.remove(removing)
    mult_count *= current_mult_multi
    current_mult_multi = 2 - (0.1*total_cards_discarded_two)
def runner():
    global bonus_total
    global hand_type
    global bonus_count

    if hand_type == 'straight' or hand_type == 'straight flush' or hand_type == 'royal flush':
        bonus_total += 15
    bonus_count += bonus_total
def spade_check(suit):
    global mult_count
    if suit == 'spade':
        mult_count += 3
def straight_joker():
    global hand_type
    global bonus_count
    if hand_type == 'straight' or hand_type == 'straight flush' or hand_type == 'royal flush':
        bonus_count += 70
def triplet_joker():
    global hand_type
    global bonus_count
    if hand_type == 'three of a kind' or hand_type == "four of a kind" or hand_type == "full house":
        bonus_count += 40
def two_pair_joker():
    global hand_type
    global bonus_count
    if hand_type == 'two pair' or hand_type == 'full house':
        bonus_count += 40
def void():
    global empty
    global mult_count
    global joker_indeck
    empty = 5 - len(joker_indeck)
    if empty != 0:
        mult_count *= empty
def jrd():
    global bonus_count
    global mult_count
    global joker_indeck
    removing = None
    for i in joker_indeck:
        if i[1][0] == "JRD":
            removing = i
    pick = random.randint(1,2)
    mult_count += random.randint(1,500)
    bonus_count += random.randint(1,10000)
    mult_count *= random.randint(1,10)
    if pick == 1:
        joker_indeck.remove(removing)

#The base requirement math for the blinds small 1x, big is 1.5x, boss is 2x on most occasions 
def blind_math():
    global base_blind
    global blind_requirement
    global ante_count
    global boss
    if blind.stage == "small":
        blind_requirement = base_blind[ante_count - 1]
    elif blind.stage == "big":
        blind_requirement = int(base_blind[ante_count - 1] * 1.5)
    elif blind.stage == "boss":
        if boss[0] == "The Wall":
            blind_requirement = base_blind[ante_count - 1] * 4
        elif boss[0] == "The Base":
            blind_requirement = base_blind[ante_count - 1]
        else:
            blind_requirement = base_blind[ante_count - 1] * 2

# Gets the random order of cards for the game stage
def card_generation(cards):
    global cards_stored
    global cards_used
    card_selection = []
    card_ordered = []
    card_selection_off = False
    card_count = len(cards_stored)

    for i in cards_stored:
        card_selection.append(i[1])
    cards_stored.clear()
    while card_selection_off != True:
        # card_selected = random number from 0 to one less than the totel of cards (51)
        card_selected = random.randint(0, len(cards) - 1)
        if card_count >= 8:
            card_selection_off = True
            # if more than 8 it'll stop
        else:
            if (
                card_selection.count(card_selected) >= 1
                or cards_used.count(card_selected) >= 1
            ):
                pass
                # move on and do nothing if it is already inside of the cards _selected
            elif 52 - len(cards_used) >= 8:
                card_selection.append(card_selected)
                # card_selection = random number
                card_count += 1
                card_selected = None
            else:
                app.stage = "game_over"
    for i in card_selection:
        # card_ordered = cards[card][1](rank,randomised number)
        card_ordered.append([int(cards[i][1]), i])

    card_ordered.sort(reverse=True)
    # rank is needed for the sort here
    return card_ordered

def get_rank(item):
    return int(
        item[1][1]
    )  # looks at all cards selected, gets the rank via [1][1] and sorts by high to low

#does all card movement ie card movement in the start of game stage or the movement to the middle in the card math stage 
def card_movement():

    global card_actors
    global cards_selected
    card_stop = 330
    card_placement_x = 258
    y = 353
    if app.stage == "title":
        card_stop = 330
        card_placement_x = 257
    else:
        for i in card_actors:
            card_stop += 92
            if i[0].x > card_stop:
                i[0].x -= 23
    if app.stage == "game":
        for i in card_actors:
            if i[0].selected:
                if i[0].y > 600:
                    i[0].y -= 5
                else:
                    i[0].y = 600
            else:
                if i[0].y < 623:
                    i[0].y += 5
                else:
                    i[0].y = 623
        if game.stage == "stall":
            cards_selected.sort(key=get_rank, reverse=True)
            for i in cards_selected:
                card_placement_x += 161
                if i[0].x != card_placement_x:
                    i[0].x = card_placement_x
                if i[0].y != y:
                    i[0].y = y

# checks for the type of base hand the cards selected are 
def hand_check():

    global hand_type
    global cards_selected
    global mult_count
    global bonus_count
    global hand_types
    global joker_indeck
    heart_count = 0
    diamond_count = 0
    club_count = 0
    spade_count = 0
    card_numbers = []
    cards_suit_value = []
    for i in cards_selected:
        cards_suit_value.append(i[1])

    for i in cards_suit_value:
        card_numbers.append(int(i[1]))
        if i[0] == "heart":
            heart_count += 1
        if i[0] == "diamond":
            diamond_count += 1
        if i[0] == "club":
            club_count += 1
        if i[0] == "spade":
            spade_count += 1

    card_numbers.sort(reverse=True)
    if (
        is_royal(card_numbers, heart_count, diamond_count, club_count, spade_count)
        and len(card_numbers) == 5
    ):
        hand_type = "royal flush"
        bonus_count = 100
        mult_count = 10
    elif (
        is_straight_flush(
            card_numbers, heart_count, diamond_count, club_count, spade_count
        )
        and len(card_numbers) == 5
    ):
        hand_type = "straight flush"
        bonus_count = 100
        mult_count = 8
    elif is_four_of_a_kind(card_numbers):
        hand_type = "four of a kind"
        bonus_count = 60
        mult_count = 7
    elif is_full_house(card_numbers) and len(card_numbers) == 5:
        hand_type = "full house"
        bonus_count = 40
        mult_count = 4
    elif heart_count == 5 or diamond_count == 5 or club_count == 5 or spade_count == 5:
        hand_type = "flush"
        bonus_count = 35
        mult_count = 4
    elif is_straight(card_numbers) and len(card_numbers) == 5:
        hand_type = "straight"
        bonus_count = 30
        mult_count = 4
    elif is_three_of_a_kind(card_numbers):
        hand_type = "three of a kind"
        bonus_count = 30
        mult_count = 3
    elif is_two_pair(card_numbers):
        hand_type = "two pair"
        bonus_count = 20
        mult_count = 2
    elif is_pair(card_numbers):
        hand_type = "pair"
        bonus_count = 10
        mult_count = 2
    elif len(card_numbers) == 0:
        hand_type = None
        bonus_count = 0
        mult_count = 0
    else:
        hand_type = "high card"
        bonus_count = 5
        mult_count = 1

# all math involving jokers inside the math process aka per card play i.e diamond cards being counted while the cards are in play 
def joker_math_inhand(rank,suit):
    global joker_indeck
    joker_indeck_name = []

    for i in joker_indeck:
        joker_indeck_name.append(i[1][0])

    if joker_indeck_name.count('baron') == 1:
        baron(rank)
    if joker_indeck_name.count('club') == 1:
        club_check(suit)
    if joker_indeck_name.count('diamond') == 1:
        diamond_check(suit)
    if joker_indeck_name.count('heart') == 1:
        heart_check(suit)
    if joker_indeck_name.count('hit the road') == 1:
        hit_the_road(rank)
    if joker_indeck_name.count('monarch') == 1:
        monarch(rank)
    if joker_indeck_name.count('spade') == 1:
        spade_check(suit)
        
# the math invovling all jokers cards outside of play i.e void doing the empty mult after all the bonus and mult are talllied up 
def joker_math():
    global joker_indeck
    global jokers

    joker_indeck_name = []

    for i in joker_indeck:
        joker_indeck_name.append(i[1][0])

    if joker_indeck_name.count("flush") == 1:
        flush_joker()
    if joker_indeck_name.count("ice cream") == 1:
        ice_cream()
    if joker_indeck_name.count("acrobat") ==1 :
        acrobat()
    if joker_indeck_name.count("bootstraps") == 1:
        bootstraps()
    if joker_indeck_name.count("bull") == 1:
        bull()
    if joker_indeck_name.count("burning joker") == 1:
        burning_joker()
    if joker_indeck_name.count("cavendish") == 1:
        cavendish()
    if joker_indeck_name.count("dementia") == 1:
        dementia()
    if joker_indeck_name.count("half") == 1:
        half()
    if joker_indeck_name.count("joker") == 1:
        joker()
    if joker_indeck_name.count("pair") == 1:
        pair_joker()
    if joker_indeck_name.count("popcorn") == 1:
        popcorn()
    if joker_indeck_name.count("ramen") == 1:
        ramen()
    if joker_indeck_name.count("runner") == 1:
        runner()
    if joker_indeck_name.count("straight") == 1:
        straight_joker()
    if joker_indeck_name.count("triplet") == 1:
        triplet_joker()
    if joker_indeck_name.count("two pair") == 1:
        two_pair_joker()
    if joker_indeck_name.count("void") == 1:
        void()
    if joker_indeck_name.count('JRD') == 1:
        jrd()

    get_jokers()
    for i in joker_indeck:
        for j in jokers:
            if i[1][0] == j[0]:
                joker_indeck.remove(i)
                joker_indeck.append([i[0],j,i[2]])

#counts the amount of bonus gained from each card a = 11, k,q,j,10 = 10, 9 = 9, etc..
#if the boss is the face or the suit it'll check for the restriction before adding the mult if it does hit the restriction it wont add
#this also counts the joker in hand, so the jokers can be counted during play
# restircts by hand type too, i.e four of a kind only counts the 4 common cards the other card ex 44445 the 5 card wont count
def hand_math():    
    global hand_type
    global cards_selected
    global card_actors
    global mult_count
    global bonus_count
    global randomised_cards
    global cards_stored
    global cards_used
    global restricted_suit
    global boss
    global most_played_hand
    global cards_counted
    card_values = []
    most_played_hand.append(hand_type)
    # cards selected format = [actor, [suit, rank, photo, value], randomised value])
    for i in cards_selected:
        card_values.append(int(i[1][1]))
    # card values is just the rank as [1][1] = second list, second value
    if (
        hand_type == "royal_flush"
        or hand_type == "flush"
        or hand_type == "straight"
        or hand_type == "full house"
        or hand_type == "straight flush"
    ):
        for actor,values, randomised_value in cards_selected: 
            if boss[0] == "The Suit" and blind.stage == "boss":
                if values[0] == restricted_suit:
                    pass
                else:
                    bonus_count += values[3]
                    cards_counted += 1
                    joker_math_inhand(values[1],values[0])
            elif boss[0] == "The Face" and blind.stage == "boss":
                if int(values[1]) > 10 and int(values[1]) != 14:
                    pass
                else:
                    bonus_count += values[3]
                    joker_math_inhand(values[1],values[0]) 
                    cards_counted += 1
            else:
                bonus_count += values[3]
                joker_math_inhand(values[1],values[0])
                cards_counted += 1

    elif hand_type == "four of a kind":
        for actor,values, randomised_value in cards_selected:
            if card_values.count(int(values[1])) == 4:
                if boss[0] == "The Suit" and blind.stage == "boss":
                    if values[0] == restricted_suit:
                        pass
                    else:
                        bonus_count += values[3]
                        joker_math_inhand(values[1],values[0]) 
                        cards_counted += 1
                elif boss[0] == "The Face" and blind.stage == "boss":
                    if int(values[1]) > 10 and int(values[1]) != 14:
                        pass
                    else:
                        bonus_count += values[3]
                        joker_math_inhand(values[1],values[0])
                        cards_counted += 1
                else:
                    bonus_count += values[3]
                    joker_math_inhand(values[1],values[0])
                    cards_counted += 1
    elif hand_type == "two pair":
        for actor,values, randomised_value in cards_selected:
            if card_values.count(int(values[1])) == 2:
                if boss[0] == "The Suit" and blind.stage == "boss":
                    if values[0] == restricted_suit:
                        pass
                    else:
                        bonus_count += values[3] 
                        joker_math_inhand(values[1],values[0])
                        cards_counted += 1
                elif boss[0] == "The Face" and blind.stage == "boss":
                    if int(values[1]) > 10 and int(values[1]) != 14:
                        pass
                    else:
                        bonus_count += values[3] 
                        joker_math_inhand(values[1],values[0])
                        cards_counted += 1
                else:
                    bonus_count += values[3] 
                    joker_math_inhand(values[1],values[0])
                    cards_counted += 1
    elif hand_type == "three of a kind":
        for actor,values, randomised_value in cards_selected:
            if card_values.count(int(values[1])) == 3:
                if boss[0] == "The Suit" and blind.stage == "boss":
                    if values[0] == restricted_suit:
                        pass
                    else:
                        bonus_count += values[3]  
                        joker_math_inhand(values[1],values[0])
                        cards_counted += 1
                elif boss[0] == "The Face" and blind.stage == "boss":
                    if int(values[1]) > 10 and int(values[1]) != 14:
                        pass
                    else:
                        bonus_count += values[3] 
                        joker_math_inhand(values[1],values[0])
                        cards_counted += 1
                else:
                    bonus_count += values[3] 
                    joker_math_inhand(values[1],values[0])
                    cards_counted += 1
    elif hand_type == "pair":
        for actor,values, randomised_value in cards_selected:
            if card_values.count(int(values[1])) == 2:
                if boss[0] == "The Suit" and blind.stage == "boss":
                    if values[0] == restricted_suit:
                        pass
                    else:
                        bonus_count += values[3]  
                        joker_math_inhand(values[1],values[0])
                        cards_counted += 1
                elif boss[0] == "The Face" and blind.stage == "boss":
                    if int(values[1]) > 10 and int(values[1]) != 14:
                        pass
                    else:
                        bonus_count += values[3] 
                        joker_math_inhand(values[1],values[0])
                        cards_counted += 1
                else:
                    bonus_count += values[3] 
                    joker_math_inhand(values[1],values[0])
                    cards_counted += 1
    else:
        if boss[0] == "The Suit" and blind.stage == "boss":
            if cards_selected[0][1][0] == restricted_suit:
                pass
            else:
                bonus_count += cards_selected[0][1][3] 
                cards_counted += 1
                joker_math_inhand(cards_selected[0][1][1],cards_selected[0][1][0])
        elif boss[0] == "The Face" and blind.stage == "boss":
            if int(cards_selected[0][1][1]) > 10 and int(cards_selected[0][1][1]) != 14:
                pass
            else:
                bonus_count += cards_selected[0][1][3]
                cards_counted += 1
                joker_math_inhand(cards_selected[0][1][1],cards_selected[0][1][0])
        else:
            bonus_count += cards_selected[0][1][3]
            cards_counted += 1
            joker_math_inhand(cards_selected[0][1][1],cards_selected[0][1][0])
#card deletion function for either discards or after playing hand 
def card_deletion():
    global cards_selected
    global cards_used
    global card_actors
    global cards_stored
    for i in cards_selected:
        cards_used.append(i[2][1])
        card_actors.remove(i)
    for i in card_actors:
        cards_stored.append(i[2])

# every hand check
def is_royal(cards, c, h, d, s):
    if sorted(cards) == [10, 11, 12, 13, 14] and (c == 5 or h == 5 or d == 5 or s == 5):
        return True
    else:
        return False
def is_full_house(cards):
    found_three = False
    found_two = False
    for i in cards:
        if cards.count(i) == 3:
            found_three = True
        elif cards.count(i) == 2:
            found_two = True
    if found_three and found_two:
        return True
    else:
        return False
def is_two_pair(cards):
    pairs = 0
    for i in cards:
        if cards.count(i) == 2:
            pairs += 1
    if pairs == 4:
        return True
    else:
        return False
def is_straight_flush(cards, c, h, d, s):
    if len(cards) < 5:
        return False
    else:
        if is_straight(cards) and (c == 5 or h == 5 or d == 5 or s == 5):
            return True
def is_straight(cards):
    if len(cards) < 5:
        return False
    else:
        if cards[0] != 14:
            if (
                cards[0] - cards[1] == 1
                and cards[1] - cards[2] == 1
                and cards[2] - cards[3] == 1
                and cards[3] - cards[4] == 1
            ):
                return True
        else:
            if (
                cards[1] - cards[2] == 1
                and cards[2] - cards[3] == 1
                and cards[3] - cards[4] == 1
                and cards[4] - 1 == 1
            ):
                return True
            elif (
                cards[0] - cards[1] == 1
                and cards[1] - cards[2] == 1
                and cards[2] - cards[3] == 1
                and cards[3] - cards[4] == 1
            ):
                return True
            # got inspriation from https://stackoverflow.com/questions/34684816/identifying-a-straight-from-poker-using-python
        return False
def is_four_of_a_kind(cards):
    for i in cards:
        if cards.count(i) == 4:
            return True
    return False
def is_three_of_a_kind(cards):
    for i in cards:
        if cards.count(i) == 3:
            return True
    return False
def is_pair(cards):
    for i in cards:
        if cards.count(i) == 2:
            return True
    return False

#this is for the joker screen, this places the jokers in the correct areas 
def joker_printing():
    global joker_actor
    global jokers
    jokers_showing = {}
    x = 88
    y = 130
    for i in jokers:
        jokers_showing[i[0]] = Actor(str(i[1]))
        joker_actors_nongame.append([jokers_showing[i[0]],i[0]])
        jokers_showing[i[0]].pos = (x, y)
        jokers_showing[i[0]].description = i[2]
        jokers_showing[i[0]].title = i[0]
        x += 140
        if x > 1248:
            y += 200
            x = 90
            
#Bosses 
def the_water(): 
    global discard_count
    discard_count = 0
def the_base():
    global play_count
    play_count = 1 

def card_printing():
    global card_list
    global cards
    global card_actors
    global randomised_cards

    # where the red deck is on the screen
    card_spacing = 1209
    cards_showing = {}

    card_actors.clear()
    for i in randomised_cards:
        cards_showing[i[1]] = Actor(cards[i[1]][2])
        # for all interactions with cards
        card_actors.append([cards_showing[i[1]], cards[i[1]][0:4], i])
        # for all interactions with cards outside of this functions
        # order = actor, (suit, rank, image, value), randomised number)
        # cards[i[1]][0:4] = from card # random. (suit, rank, image, value)
        # randomised cards for removal of it in the next steps
        cards_showing[i[1]].pos = (card_spacing, 623)
        cards_showing[i[1]].scale = 0.65
        cards_showing[i[1]].selected = False
        # from pgzrun cheat sheet
joker_printing()
#drawing UI for the game screen
def draw_game_phase():
    global hand_type
    global card_actors
    global bonus_count
    global mult_count
    global blind_requirement
    global chip_count
    global discard_count
    global play_count
    global money
    global blinds
    global boss
    global restricted_suit
    global joker_indeck
    # change background to game backgroun
    background.image = "game_background.png"
    background.scale = 1.65
    background.draw()
    # adds the boxes for the discard, play, and menu buttons

    BOX2 = Rect((442, 455), (200, 75))
    BOX3 = Rect((802, 455), (200, 75))
    BOX = Rect((34, 555), (111, 110))
    BOX4 = Rect((34,427),(111,110))
    screen.draw.filled_rect(BOX4,'purple')
    screen.draw.filled_rect(BOX,'orange')
    screen.draw.rect(BOX, "black")
    screen.draw.rect(BOX4, "black")
    screen.draw.filled_circle((248, 100), 51, (23, 87, 56))

    screen.draw.text(
        'TITLE',
        color="white",
        pos=(58, 602),
        fontname="pixel.ttf",
        fontsize=30,
    )

    screen.draw.text(
        'HAND INFO',
        color="white",
        pos=(42, 473),
        fontname="pixel.ttf",
        fontsize=25,
    )

    blind.scale = 1.5
    if blind.stage == "small":
        blind_selected = blinds[0]
        blind.image = blinds[0][2]
    elif blind.stage == "big":
        blind_selected = blinds[1]
        blind.image = blinds[1][2]
    elif blind.stage == "boss":
        blind_selected = boss 
        blind.image = boss[2]
    screen.draw.text(
        str(play_count).upper(),
        color="white",
        pos=(185, 472),
        fontname="pixel.ttf",
        fontsize=40,
    )
    screen.draw.text(
        str(discard_count).upper(),
        color="white",
        pos=(271, 472),
        fontname="pixel.ttf",
        fontsize=40,
    )
    screen.draw.text(
        str(ante_count).upper(),
        color="white",
        pos=(177, 635),
        fontname="pixel.ttf",
        fontsize=30,
    )
    screen.draw.text(
        str(round_count).upper(),
        color="white",
        pos=(273, 635),
        fontname="pixel.ttf",
        fontsize=30,
    )
    screen.draw.text(
        f"${str(money).upper()}",
        color=(205, 170, 66),
        pos=(175, 542),
        fontname="pixel.ttf",
        fontsize=40,
    )
    blind.draw()
    screen.draw.text(
        str(blind_requirement).upper(),
        color="white",
        pos=(82, 162),
        fontname="pixel.ttf",
        fontsize=40,
    )
    if blind.stage == "boss":
        screen.draw.text(
            str(boss[1]).upper(),
            color="white",
            pos=(50, 92),
            fontname="pixel.ttf",
            fontsize=12,
            width = 120,
            lineheight=1
        )
    screen.draw.text(
        str(blind_selected[0]).upper(),
        color="white",
        pos=(50, 74),
        fontname="pixel.ttf",
        fontsize=20,
        width = 120,
        lineheight=1
    )
    screen.draw.text(
        str(chip_count).upper(),
        color="white",
        pos=(210, 162),
        fontname="pixel.ttf",
        fontsize=40,
    )

    chip.pos = (66, 176)
    chip.scale = 0.5
    chip.draw()
    chip2.pos = (189, 176)
    chip2.scale = 0.5
    chip2.draw()
    for i in joker_indeck:
            if i[0].selected == True:
                box = Rect((i[0].x-60,i[0].y-122),(120,50))
                screen.draw.filled_rect(box, "red")
                screen.draw.rect(box,'black')
                screen.draw.text(
                    f"SELL! ${str(int(i[1][4]/2)).upper()}",
                    fontname="pixel.ttf",
                    color="white",
                    midtop=(i[0].x,i[0].y-106),
                    fontsize=25,
                    width=105,
                    lineheight=1.5
                   )
    if(blind.stage == 'boss' and boss[0] == "The Suit"):
        screen.draw.text(
                f"{restricted_suit}s are the restricted suit. They will not be in play.",
                color='white',
                pos=(370, 238),
                fontname="pixel.ttf",
                fontsize=35,
            )
    if(blind.stage == 'boss' and boss[0] == 'The Face'):
        screen.draw.text(
                f"faces are restricted. They will not be in play.",
                color='white',
                pos=(420, 238),
                fontname="pixel.ttf",
                fontsize=35,
            )
    if(blind.stage == 'boss' and boss[0] == "The Psychic" and len(cards_selected) < 5):
        screen.draw.filled_rect(BOX2, (42, 78, 110))
        screen.draw.rect(BOX2, "black")
        if hand_type != None:
            screen.draw.filled_rect(BOX3, (222, 102, 102))
            screen.draw.rect(BOX3, "black")
            screen.draw.text(
                "DISCARD",
                color='white',
                pos=(843, 478),
                fontname="pixel.ttf",
                fontsize=40,
            )
            screen.draw.text(
                "Hand is under 5 cards. This will not play.",
                color='white',
                pos=(420, 238),
                fontname="pixel.ttf",
                fontsize=40,
            )
        else:
            screen.draw.filled_rect(BOX3, (175, 114, 115))
            screen.draw.rect(BOX3, "black")
            screen.draw.text(
                "DISCARD",
                color=(192, 192, 192),
                pos=(843, 478),
                fontname="pixel.ttf",
                fontsize=40,
            )
        screen.draw.text(
            "PLAY",
            color=(192, 192, 192),
            pos=(504, 478),
            fontname="pixel.ttf",
            fontsize=40,
        )
    elif hand_type != None:
        screen.draw.text(
            str(hand_type).upper(),
            color="white",
            pos=(52, 246),
            fontname="pixel.ttf",
            fontsize=40,
        )
        screen.draw.text(
            str(bonus_count).upper(),
            color="white",
            pos=(52, 308),
            fontname="pixel.ttf",
            fontsize=40,
        )
        screen.draw.text(
            str(mult_count).upper(),
            color="white",
            pos=(200, 308),
            fontname="pixel.ttf",
            fontsize=40,
        )
        screen.draw.filled_rect(BOX2, (11, 83, 148))
        screen.draw.rect(BOX2, "black")
        if discard_count != 0:

            screen.draw.filled_rect(BOX3, (222, 102, 102))
            screen.draw.text(
                "DISCARD",
                color="white",
                pos=(843, 478),
                fontname="pixel.ttf",
                fontsize=40,
            )
        else:
            screen.draw.filled_rect(BOX3, (175, 114, 115))
            screen.draw.text(
                "DISCARD",
                color=(192, 192, 192),
                pos=(843, 478),
                fontname="pixel.ttf",
                fontsize=40,
            )

        screen.draw.rect(BOX3, "black")
        screen.draw.text(
            "PLAY",
            color="white",
            pos=(504, 478),
            fontname="pixel.ttf",
            fontsize=40,
        )
        chip3.pos = (129, 380)
        chip3.scale = 0.5
        chip3.draw()
    else:
        screen.draw.filled_rect(BOX2, (42, 78, 110))
        screen.draw.filled_rect(BOX3, (175, 114, 115))
        screen.draw.rect(BOX2, "black")
        screen.draw.rect(BOX3, "black")
        screen.draw.text(
            "DISCARD",
            color=(192, 192, 192),
            pos=(843, 478),
            fontname="pixel.ttf",
            fontsize=40,
        )
        screen.draw.text(
            "PLAY",
            color=(192, 192, 192),
            pos=(504, 478),
            fontname="pixel.ttf",
            fontsize=40,
        )
    for actor in card_actors:
        # draws actors
        actor[0].draw()

    if game.stage == "win" or game.stage == "win_stall":
        display = money_display()
        win_popup.scale = 1.75
        win_button.scale = 1.5
        win_popup.draw()
        win_button.draw()
        screen.draw.text(
            f"You Won. ${display}",
            color='white',
            pos=(win_button.x-60, win_button.y- 105),
            fontname="pixel.ttf",
            fontsize=60,
        )
        joker_indeck_name = []
        for i in joker_indeck:
            joker_indeck_name.append(i[1])
        if (joker_indeck_name.count(["golden","golden_joker.png","$3 at the end of each round","cash_joker",3]) != 1):
            screen.draw.text(
                f"${display - play_count} from {app.stage} blind.",
                color='white',
                pos=(win_button.x-250, win_button.y + 60),
                fontname="pixel.ttf",
                fontsize=40,
            )
            screen.draw.text(
                f"${play_count} from hands remaining.",
                color='white',
                pos=(win_button.x-250, win_button.y + 125),
                fontname="pixel.ttf",
                fontsize=40,
            )
        else:
            screen.draw.text(
                f"${display - play_count - 3} from {app.stage} blind.",
                color='white',
                pos=(win_button.x-250, win_button.y + 60),
                fontname="pixel.ttf",
                fontsize=40,
            )
            screen.draw.text(
                f"$3 from golden joker.",
                color=(205, 170, 66),
                pos=(win_button.x-250, win_button.y + 190),
                fontname="pixel.ttf",
                fontsize=40,
            )
            screen.draw.text(
                f"${play_count} from hands remaining.",
                color='white',
                pos=(win_button.x-250, win_button.y + 125),
                fontname="pixel.ttf",
                fontsize=40,
            )
# drawing UI for joker screen
def draw_title_screen():
    info_button.scale = 0.2
    background.image = "title_background.png"
    BOX = Rect((325, 487), (339, 134))
    BOX2 = Rect((685, 487), (290, 134))
    info_button.pos = (50,50)
    background.scale = 1.65
    background.draw()
    info_button.draw()
    screen.draw.rect(BOX, "white")
    screen.draw.rect(BOX2, "white")
    screen.draw.text(
        "<- INFO BUTTON",
        fontname="pixel.ttf",
        color="white",
        midleft=(85, 50),
        fontsize=40,
        width = 550
        )

#drawing UI for joker screen
def draw_joker_screen():
    global joker_actors_nongame
    background.image = "title_background.png"
    background.scale = 1.65
    background.draw()
    BOX = Rect((0, 0), (1300, 950))
    BOX2 = Rect((1150, 440), (120, 180))
    screen.draw.filled_rect(BOX, (56, 120, 89))
    screen.draw.filled_rect(BOX2, "darkslateblue")
    screen.draw.rect(BOX2, "black")
    screen.draw.text(
        "EXIT",
        pos=(1175, 440 + (71)),
        fontname="pixel.ttf",
        color="white",
        fontsize=40,
    )
    for actor, name in joker_actors_nongame:
        if name != 'JRD':
            actor.draw()
            

#drawing UI for shop
def draw_shop_phase():
    global joker_actors_ingame
    background.image = "shop_background.png"
    background.scale = 1.65
    background.draw()
    BOX = Rect((34, 555), (111, 110))
    BOX4 = Rect((34,427),(111,110))
    screen.draw.filled_rect(BOX4,'purple')
    screen.draw.filled_rect(BOX,'orange')
    screen.draw.text(
        'TITLE',
        color="white",
        pos=(58, 602),
        fontname="pixel.ttf",
        fontsize=30,
    )

    screen.draw.text(
        'HAND INFO',
        color="white",
        pos=(42, 473),
        fontname="pixel.ttf",
        fontsize=25,
    )
    screen.draw.text(
        str(play_count).upper(),
        color="white",
        pos=(185, 472),
        fontname="pixel.ttf",
        fontsize=40,
    )
    screen.draw.text(
        str(discard_count).upper(),
        color="white",
        pos=(271, 472),
        fontname="pixel.ttf",
        fontsize=40,
    )
    screen.draw.text(
        str(ante_count).upper(),
        color="white",
        pos=(177, 635),
        fontname="pixel.ttf",
        fontsize=30,
    )
    screen.draw.text(
        str(round_count).upper(),
        color="white",
        pos=(273, 635),
        fontname="pixel.ttf",
        fontsize=30,
    )
    screen.draw.text(
        f"${str(money).upper()}",
        color=(205, 170, 66),
        pos=(175, 542),
        fontname="pixel.ttf",
        fontsize=40,
    )
    box = Rect((386,422),(269,98))
    screen.draw.filled_rect(box,(175, 114, 115))
    screen.draw.rect(box,'black')
    screen.draw.text(
        f"NEXT ROUND",
        color='white',
        pos=(435, 455),
        fontname="pixel.ttf",
        fontsize=40,
    )
    for i in joker_actors_ingame:
        i[0].draw()
        if i[0].selected == True:
            box = Rect((i[0].x-60,i[0].y-122),(120,50))
            screen.draw.filled_rect(box, "blue")
            screen.draw.rect(box,'black')
            screen.draw.text(
                f"BUY! ${str(i[1][4]).upper()}",
                fontname="pixel.ttf",
                color="white",
                midtop=(i[0].x,i[0].y-106),
                fontsize=25,
                width=105,
                lineheight=1.5
               )
    for i in joker_indeck:
        if i[0].selected == True:
            box = Rect((i[0].x-60,i[0].y-122),(120,50))
            screen.draw.filled_rect(box, "red")
            screen.draw.rect(box,'black')
            screen.draw.text(
                f"SELL! ${str(int(i[1][4]/2)).upper()}",
                fontname="pixel.ttf",
                color="white",
                midtop=(i[0].x,i[0].y-106),
                fontsize=25,
                width=105,
                lineheight=1.5
               )

# prints the jokers for the shop
def joker_shop_printing():
    global joker_actors_ingame
    x = 787
    for i in joker_actors_ingame:
        i[0].scale = 0.8
        i[0].pos = (x, 469)
        x += 172
# this shows when the joker is selected by moving the joker up when selected and back down when not selected 
def joker_movement():
    global joker_actors_ingame

    for i in joker_actors_ingame:

        if i[0].selected == True:
            if i[0].y > 446:
                i[0].y -= 5
            else:
                i[0].y = 446
        else:
            if i[0].y < 469:
                i[0].y += 5
            else:
                i[0].y = 469
# when in gameplay this is the function to show the title and decription of the joker 
def draw_hover_joker():
    global joker_actors_ingame
    global joker_indeck
    global joker_pos_ingame
    # FORMAT joker_actors_ingame
    # Actor, Joker, Randomised Number
    x = joker_pos_ingame[0]
    y = joker_pos_ingame[1]
    BOX = Rect((x - 60, y - 20), (120, 210))
    BOX2 = Rect((x - 55, y - 15), (110, 42))
    BOX3 = Rect((x - 55, y + 35), (110, 150))
    screen.draw.filled_rect(BOX, (56, 120, 89))
    screen.draw.filled_rect(BOX2, (23, 87, 56))
    screen.draw.filled_rect(BOX3, (23, 87, 56))
    screen.draw.text(
        joker_output[0].upper(),
        fontname="pixel.ttf",
        color="white",
        midtop=(x, y-5),
        fontsize=20,
    )
    screen.draw.text(
        joker_output[1].upper(),
        fontname="pixel.ttf",
        color="white",
        midtop=(x, y + 45),
        fontsize=15,
        width=105,
        lineheight=1.5
       )
# when in joker screen this is the function to show the title and decription of the joker
def box_drawing():
    global joker_output
    global joker_pos_nongame
    x = joker_pos_nongame[0]
    y = joker_pos_nongame[1]
    if y < 400:
        BOX = Rect((x - 100, y - 20), (200, 250))
        BOX2 = Rect((x - 95, y - 15), (190, 42))
        BOX3 = Rect((x - 95, y + 35), (190, 190))
        screen.draw.filled_rect(BOX, (56, 120, 89))
        screen.draw.filled_rect(BOX2, (23, 87, 56))
        screen.draw.filled_rect(BOX3, (23, 87, 56))
        screen.draw.text(
            joker_output[1].upper(),
            fontname="pixel.ttf",
            color="white",
            midtop=(x, y-5),
            fontsize=30,
        )
        screen.draw.text(
            joker_output[0].upper(),
            fontname="pixel.ttf",
            color="white",
            midtop=(x, y + 40),
            fontsize=25,
            width=185,
            lineheight=1.5
        )
    else:
        BOX = Rect((x - 100, y - 220), (200, 250))
        BOX2 = Rect((x - 95, y - 215), (190, 42))
        BOX3 = Rect((x - 95, y - 165), (190, 190))
        screen.draw.filled_rect(BOX, (56, 120, 89))
        screen.draw.filled_rect(BOX2, (23, 87, 56))
        screen.draw.filled_rect(BOX3, (23, 87, 56))
        screen.draw.text(
            joker_output[1].upper(),
            fontname="pixel.ttf",
            color="white",
            midtop=(x, y-205),
            fontsize=30,
        )
        screen.draw.text(
            joker_output[0].upper(),
            fontname="pixel.ttf",
            color="white",
            midtop=(x, y - 155),
            fontsize=25,
            width=185,
            lineheight=1.5
        )
# ending screens (winning or losing)
def draw_end_screens():
    global ante_count
    global round_count
    global boss
    global jokers_bought
    global jokers_sold
    global cards_discarded
    global most_played_hand
    global best_hand
    global blinds
    global cards_counted
    blind2 = Actor('placeholder.png')
    blind2.scale = 1.5
    most_played = None
    most_played_count = 0
    blind_name = None
    if blind.stage == 'small':
        blind_name = 'small blind'
        blind2.image = blinds[0][2]
    elif blind.stage == 'big':
        blind_name = 'big blind'
        blind2.image = blinds[1][2]
    else:
        blind_name = boss[0]
        blind2.image = boss[2]
    for i in most_played_hand:
        if most_played_hand.count(i) > most_played_count:
            most_played = i
            most_played_count = most_played_hand.count(i)
    end_screen.y = HEIGHT / 2
    end_screen.right = WIDTH
    end_screen.scale = 1.8 
    end_screen.draw()

    blind2.pos = (end_screen.x+ 433, end_screen.y + 38)
    blind2.draw()
    screen.draw.text(
        f"{ante_count}",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 500, end_screen.y-131),
        fontsize=50,
    )
    screen.draw.text(
        f"Ante",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 388, end_screen.y-131),
        fontsize=50,
    )
    screen.draw.text(
        f"{jokers_bought}",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 257, end_screen.y-133),
        fontsize=45,
    )
    screen.draw.text(
        f"Jokers Bought",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 154, end_screen.y-125),
        fontsize=23,
    )
    screen.draw.text(
        f"{jokers_bought}",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 257, end_screen.y-133),
        fontsize=45,
    )
    screen.draw.text(
        f"Cards Used",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 154, end_screen.y-58),
        fontsize=23,
    )
    screen.draw.text(
        f"{cards_counted}",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 257, end_screen.y-65),
        fontsize=45,
    )
    screen.draw.text(
        f"{cards_discarded}",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 257, end_screen.y),
        fontsize=45,
    )
    screen.draw.text(
        f"Cards Discarded",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 154, end_screen.y+9),
        fontsize=21,
    )
    screen.draw.text(
        f"Jokers Sold",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 154, end_screen.y-194),
        fontsize=23,
    )
    screen.draw.text(
        f"{jokers_sold}",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 257, end_screen.y-202),
        fontsize=45,
    )
    screen.draw.text(
        f"{round_count}",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 500, end_screen.y-202),
        fontsize=50,
    )
    screen.draw.text(
        f"Round",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 398, end_screen.y-202),
        fontsize=50,
    )
    screen.draw.text(
        f"Most Played Hand",
        fontname='pixel.ttf',
        color = 'white',
        midtop = (end_screen.x + 195, end_screen.y - 267),
        fontsize = 30)
    screen.draw.text(
        f"{most_played} ({most_played_count})",
        fontname='pixel.ttf',
        color = 'white',
        topleft = (end_screen.x + 318, end_screen.y - 267),
        fontsize = 30)
    chip4 = Actor('chips.png')
    chip4.scale = 0.5
    chip4.pos = (end_screen.x + 328, end_screen.y - 325)
    chip4.draw()
    screen.draw.text(
        f"Best Hand",
        fontname='pixel.ttf',
        color = 'white',
        midtop = (end_screen.x + 195, end_screen.y - 340),
        fontsize = 45)
    screen.draw.text(
        f"{best_hand}",
        fontname='pixel.ttf',
        color = 'white',
        topleft = (end_screen.x + 350, end_screen.y - 340),
        fontsize = 45)
    screen.draw.text(
        f"{hands_played}",
        fontname="pixel.ttf",
        color="white",
        midtop=(end_screen.x + 258, end_screen.y+64),
        fontsize=45,
    )
    screen.draw.text(
        f"Hands Played",
        fontname="pixel.ttf",
        color="white",
        midleft=(end_screen.x + 90, end_screen.y+81),
        fontsize=25,
    )
    screen.draw.text(
        f"TO MENU",
        fontname="pixel.ttf",
        color="white",
        midleft=(end_screen.x + 240, end_screen.y+203),
        fontsize=40,
    )
    screen.draw.text(
        f"RESTART",
        fontname="pixel.ttf",
        color="white",
        midleft=(end_screen.x + 240, end_screen.y+151),
        fontsize=40,
    )
    if app.stage == 'game_over':
        screen.draw.text(
            'YOU LOSE',
            fontname="pixel.ttf",
            color="white",
            midtop=(end_screen.x + 320, end_screen.y-465),
            fontsize=90,
            ocolor=(222, 102, 102),
            owidth =1, 
        )
        screen.draw.text(
            f'you lost to {blind_name}',
            fontname="pixel.ttf",
            color="white",
            midtop=(end_screen.x + 430, end_screen.y-52),
            fontsize=20
        )
    else:
        screen.draw.text(
            'YOU WIN!',
            fontname="pixel.ttf",
            color="white",
            midtop=(end_screen.x + 320, end_screen.y-465),
            fontsize=90,
            ocolor=(11, 83, 148),
            owidth =1, 
        )
        screen.draw.text(
            f'you won to {blind_name}',
            fontname="pixel.ttf",
            color="white",
            midtop=(end_screen.x + 430 , end_screen.y-52),
            fontsize=20
        )
# hand info screen
def draw_hand_info():
    box = Rect(((WIDTH/2 - 300),(HEIGHT/2 - 400)),(600,570))
    box2 =  Rect(((WIDTH/2 - 290),(HEIGHT/2 - 390)),(90,30))
    screen.draw.filled_rect(box,(56, 120, 89))
    screen.draw.rect(box,'black')
    screen.draw.filled_rect(box2,'darkred')
    screen.draw.rect(box2,'black')
    screen.draw.text(
            f'<- BACK',
            fontname="pixel.ttf",
            color="white",
            midtop=((WIDTH/2 - 250),(HEIGHT/2 - 384)),
            fontsize=25,
        )
    screen.draw.text(
            f'INFO',
            fontname="pixel.ttf",
            color="white",
            midtop=((WIDTH/2),(HEIGHT/2 - 360)),
            fontsize=90,
            ocolor = 'black',
            owidth = 1,
        )
    hands_info.image = 'base_hand.png'

    hands_info.scale = 0.5
    hands_info.pos = (WIDTH/2,HEIGHT/2 - 50)
    hands_info.draw()

#info screen
def draw_info():
    box = Rect(((WIDTH/2 - 300),(HEIGHT/2 - 400)),(600,570))
    box2 = Rect(((WIDTH/2 - 280),(HEIGHT/2 - 240)),(560,390))
    box3 = Rect(((WIDTH/2 - 100),(HEIGHT/2)),(200,80))
    screen.draw.filled_rect(box,(56, 120, 89))
    screen.draw.rect(box,'black')
    screen.draw.filled_rect(box2,(23, 87, 56))
    screen.draw.filled_rect(box3,'red')
    screen.draw.rect(box3,'black')
    screen.draw.text(
            f'EXIT',
            fontname="pixel.ttf",
            color="white",
            pos=((WIDTH/2 - 45),(HEIGHT/2 +20)),
            fontsize=50,
            ocolor = 'black',
            owidth = 1,
        )
    screen.draw.text(
            f'INFO',
            fontname="pixel.ttf",
            color="white",
            midtop=((WIDTH/2),(HEIGHT/2 - 360)),
            fontsize=90,
            ocolor = 'black',
            owidth = 1,
        )
    screen.draw.text(
        "Play poker hands to earn chips. Each ante has a chip goal you must reach using a limited number of hands. Stronger hands score more chips, but smart upgrades and synergies are key. ",
        fontname="pixel.ttf",
        color="white",
        midtop=((WIDTH/2),(HEIGHT/2 - 230)),
        fontsize=20,
        width = 550
        )
    screen.draw.text(
        "Use jokers and card combos to boost your score. After each round, buy new cards and plan ahead, each ante gets harder. Survive all 3 antes and beat the final chip goal to win. ",
        fontname="pixel.ttf",
        color="white",
        midtop=((WIDTH/2),(HEIGHT/2 - 160)),
        fontsize=20,
        width = 550
        )
    screen.draw.text(
        "Survive all 3 antes and beat the final chip goal to win. Keep your deck tight, play smart, and go all-in when it counts.",
        fontname="pixel.ttf",
        color="white",
        midtop=((WIDTH/2),(HEIGHT/2 - 90)),
        fontsize=20,
        width = 550
        )
    screen.draw.text(
        "HAVE FUN!!!",
        fontname="pixel.ttf",
        color="white",
        midtop=((WIDTH/2),(HEIGHT/2 - 40)),
        fontsize=40,
        width = 550
        )
    screen.draw.text(
        "p.s. (When jokers are reffering to 'bonus' or 'mult', the first is the blue number and the second is the red)",
        fontname="pixel.ttf",
        color="white",
        midtop=((WIDTH/2),(HEIGHT/2 + 100)),
        fontsize=20,
        width = 550
        )


def on_mouse_down(pos):

    global cards_selected
    global max_card
    global card_actors
    global randomised_cards
    global cards
    global card_count
    global hand_type
    global cards_used
    global chip_count
    global play_count
    global play_total
    global discard_count
    global joker_actor_ingame
    global money
    global joker_indeck
    global total_cards_discarded
    global total_cards_discarded_two
    global jokers_bought
    global jokers_sold
    global save_app_stage
    x = pos[0]
    y = pos[1]
    if app.stage == 'game_over' or app.stage == 'winner':
        # reset or main menu button after winning or losing the game 
        if x > end_screen.x + 117 and x < end_screen.x + 501:
            if y > end_screen.y + 127 and y < end_screen.x + 170:
                nuke_game()
                app.stage = 'game'
            if y > end_screen.y + 177 and y < end_screen.y + 220:
                nuke_game()
                app.stage = 'title'
    if app.stage == "title":
        if info_button.collidepoint(pos) == True:
            #info button to display
            app.stage = 'info'
        if (x > 325 and x < 664) and (y > 487 and y < 621):
            # resets EVERYTHING when going back to title
            nuke_game()
            app.stage = "game"
            game.stage = "clear"
            cards_used.clear()

        if (x > 685 and x < 975) and (y > 487 and y < 621):
            #jokers display button
            app.stage = "joker_display"
    if app.stage == 'info':
        #returns to the title screen
        if (x > WIDTH/2 - 100 and x < WIDTH/2 + 100) and (y > HEIGHT/2 and y <HEIGHT/2 + 80):
            app.stage = 'title'
    if app.stage == 'hand_info':
        # return to the saved app stage 
        if (x > WIDTH/2 -290 and x < WIDTH/2 -200) and (y > HEIGHT/2 -390 and y < HEIGHT -360):
            app.stage = save_app_stage
    if app.stage == "joker_display":
        #return to title
        if (x > 1150 and x < 1270) and (y > 440 and y < 620):
            app.stage = "title"
    if app.stage == "shop":
        #hand info screen button
        if (x > 34 and x < 145) and (y > 427 and y <537):
            save_app_stage = app.stage
            app.stage = 'hand_info'
        #title screen feature 
        if (x > 34 and x < 145) and (y > 555 and y < 666):
            app.stage = "title"
            nuke_game()
        # next round feature 
        if pos[0] > 386 and pos[0] < 655 and pos[1] > 422 and pos[1] < 520:
            app.stage = "game"
        for i in joker_indeck:
            # joker selling system
            if i[0].selected == True:
                if pos[0] > i[0].x-60 and pos[1] > i[0].y-110 and pos[0] < i[0].x + 60 and pos[1] < i[0].y - 72 :
                    i[0].bought = False
                    i[0].selected = False
                    joker_indeck.remove(i)
                    money += int(i[1][4]/2)
                    jokers_sold +=1 
            if i[0].collidepoint(pos) == True:
                if i[0].selected != True:
                    i[0].selected = True

                else:
                    i[0].selected = False
        for i in joker_actors_ingame:
            # joker buying system
            if i[0].selected == True:
                if pos[0] > i[0].x-60 and pos[1] > i[0].y-110 and pos[0] < i[0].x+60 and pos[1] < i[0].y-72 :
                    if money >= i[1][4]:
                        i[0].bought = True
                        i[0].selected = False
                        joker_actors_ingame.remove(i)
                        joker_indeck.append(i)
                        money -= i[1][4]
                        jokers_bought += 1
                        if i[1][0] == 'ice cream':
                            current_bonus = 50
                        if i[1][0] == 'runner':
                            bonus_total = 0
                        if i[1][0] == 'ramen':
                            current_mult_multi = 20
                            total_cards_discarded_two = 0
                        if i[1][0] == 'popcorn':
                            current_mult = 20
                        if i[1][0] == 'burning_joker':
                            total_cards_discarded = 0
            # checks for joker selection 
            if i[0].collidepoint(pos) == True:
                if i[0].selected != True:
                    i[0].selected = True

                else:
                    i[0].selected = False

    if app.stage == "game":
        #checks for boss blinds 
        if blind.stage == 'boss':
            if boss[0] == "The Water":
                the_water()
            if boss[0] == "The Base":
                the_base()
        #return to title screen button
        if (x > 34 and x < 145) and (y > 555 and y < 666):
            app.stage = "title"
            nuke_game()
        #hand info button
        if (x > 34 and x < 145) and (y > 427 and y <537):
            save_app_stage = app.stage
            app.stage = 'hand_info'
        if app.stage != "game_over":
            for i in joker_indeck:
                if i[0].selected == True:
                    #selling joker function
                    if pos[0] > i[0].x-60 and pos[1] > i[0].y-110 and pos[0] < i[0].x + 60 and pos[1] < i[0].y - 72 :
                        i[0].bought = False
                        i[0].selected = False
                        joker_indeck.remove(i)
                        money += int(i[1][4]/2)
                        jokers_sold += 1
                # selecting and deselecting jokers 
                if i[0].collidepoint(pos) == True:
                    if i[0].selected != True:
                        i[0].selected = True

                    else:
                        i[0].selected = False
            if game.stage == "draw":
                # cards clicking mechanic
                for actors in card_actors:
                    # checks for collide point if already true turns flase vice versa
                    if actors[0].collidepoint(pos) == True:
                        if actors[0].selected:
                            actors[0].selected = False
                            card_count -= 1
                            cards_selected.remove(actors)
                        elif card_count < max_card:
                            actors[0].selected = True
                            card_count += 1
                            cards_selected.append(actors)
                        hand_check()
                        
                # checks for collision for the play button
                if (
                    (x > 442 and x < 642)
                    and (y > 455 and y < 530)
                    and hand_type != None
                ):
                    if boss[0]== "The Psychic" and blind.stage == "boss": 
                        if len(cards_selected) == 5:
                            game.stage = "card_check"
                    else:
                        game.stage = "card_check"

                # checks for collision for the discard button
                elif (
                    (x > 802 and x < 1002)
                    and (y > 455 and y < 530)
                    and discard_count > 0
                    and hand_type != None
                ):
                    game.stage = "discard"
            if game.stage == "card_check":
                # does the main math processing
                hand_math()
                joker_math()
                game.stage = "stall"
                play_count -= 1
                play_total += 1
                clock.schedule_unique(stalling, 1)
            if game.stage == "win_stall":
                #checks if you pressed the win function if so it moves to the shop stage 
                if win_button.collidepoint(pos) == True:
                    money_maker()
                    app.stage = "shop"
                    reset_game_state()
                    shop_jokers()
                    joker_shop_printing()
                    
# a stalling function for visuals
def stalling():
    game.stage = 'math'

# for every joker hovering mechinanic 
def on_mouse_move(pos):
    global joker_actors_nongame
    global joker_actors_ingame
    global box_draw
    global jokers
    global joker_output
    global joker_hover
    global joker_pos_ingame
    global joker_pos_nongame
    global joker_indeck
    box_draw = False
    joker_hover = False
    if app.stage == "joker_display":
        for actor, name in joker_actors_nongame:
            if name != 'JRD':
                if actor.collidepoint(pos):
                    box_draw = True
                    joker_pos_nongame = actor.pos
                    joker_output = [actor.description, actor.title]
    if app.stage == "shop":
        for actor in joker_actors_ingame:
            if actor[0].collidepoint(pos) and actor[0].selected != True:
                joker_hover = True
                joker_pos_ingame = actor[0].pos
                joker_output = [actor[1][0],actor[1][2]]
    if app.stage == "game" or app.stage == "shop":
        for actor in joker_indeck:
            if actor[0].collidepoint(pos) and actor[0].selected != True:
                joker_hover = True
                joker_pos_ingame = actor[0].pos
                joker_output = [actor[1][0],actor[1][2]]

#jokers in deck
def draw_jokers_indeck():
    global joker_indeck
    global current_mult
    global bonus_total
    global current_bonus
    global current_mult_multi
    global empty
    global current_cards_discarded
    x = 431
    if len(joker_indeck) != 0:
        for i in joker_indeck:
            i[0].scale = 0.8
            i[0].pos = (x, 122)
            i[0].draw()
            x += 150

def update():
    global card_count
    global cards_selected
    global randomised_cards
    global cards
    global hand_type
    global used_ante
    global discard_count
    global discard_total
    global mult_count
    global bonus_count
    global chip_count
    global play_count
    global restricted_suit
    global total_cards_discarded
    global total_cards_discarded_two
    global best_hand
    global cards_discarded
    global hands_played 
    background.pos = (WIDTH / 2, HEIGHT / 2)
    card_movement()
    joker_movement()
    # checks if you have won the game 
    if ante_count == 4:
        app.stage = 'winner'

    # gets an new boss every ante 
    if used_ante.count(ante_count) < 1:
        get_boss()
        used_ante.append(ante_count)

    # basic clear for the main game stages 
    if game.stage == "clear":
        for actors in cards_selected:
            actors[0].selected = False
        card_count = 0
        card_deletion()
        cards_selected.clear()
        hand_type = None
        game.stage = "generate"
        win_popup.midtop = (640, HEIGHT)
        win_button.midtop = (645, win_popup.y - 20)
        
    # discard feature
    if game.stage == "discard":
        discard_total += 1
        discard_count -= 1
        for actors in cards_selected:
            actors[0].selected = False
            total_cards_discarded += 1
            total_cards_discarded_two += 1
            cards_discarded += 1 
        card_count = 0
        card_deletion()
        cards_selected.clear()
        hand_type = None
        game.stage = "generate"
    # this generated the blind requirement and gets the starting cards 
    if game.stage == "generate":
        blind_math()
        randomised_cards = card_generation(cards)
        card_printing()
        game.stage = "draw"

    # math for the chip count 
    if game.stage == "math":
        chip_count += bonus_count * mult_count
        if bonus_count * mult_count > best_hand:
            best_hand = bonus_count * mult_count
        hands_played += 1 
        game.stage = 'win'

    # checks for win and losses 
    if game.stage == "win":
        if chip_count >= int(blind_requirement):
            if win_popup.bottom > HEIGHT:
                win_popup.y -= 40
                win_button.y = win_popup.y - 20
            else:
                win_popup.bottom = HEIGHT
                win_button.y = win_popup.y - 20

            if win_popup.bottom == HEIGHT:
                game.stage = "win_stall"
        else:
            game.stage = "clear"
        if play_count == 0 and chip_count <= int(blind_requirement):
            app.stage = "game_over"

def draw():
    global box_draw
    global joker_hover
    global info
    screen.clear()
    if app.stage == "title":
        draw_title_screen()
    elif app.stage == 'info':
        draw_info()
    elif app.stage == "game":
        draw_game_phase()
    elif app.stage == "shop":
        draw_shop_phase()
    if app.stage == "shop" or app.stage == "game":
        draw_jokers_indeck()
        if joker_hover == True:
            draw_hover_joker()
    if app.stage == 'hand_info':
        draw_hand_info()
    elif app.stage == "joker_display":
        draw_joker_screen()
        if box_draw == True:
            box_drawing()
    elif app.stage == "game_over" or app.stage == "winner":
        draw_game_phase()
        draw_end_screens()

pgzrun.go()