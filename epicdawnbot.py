# Class/Assignment: CS3080 Final Project
# Names: Jisop Lee, Ben Martin
# Description: This program manages bot commands and allows usage of the card handler program for
# Discord users.

import main
import discord
from discord.ext import commands

# Global variables
tourney_members = []
tournament_host = ''
tournament_in_progress = False


# Needs Intents.members to be True
intents = discord.Intents.default()
intents.members = True

# Initialize client
client = commands.Bot(command_prefix='!', intents=intents)


# Message for when the bot is online. Primarily for testing.
@client.event
async def on_ready():

    print('Epic Dawn Bot is now online and running.')
    # general_channel = client.get_channel(786992346666500139)
    # await general_channel.send('I\'m up and running!')


# Greeting for new member. Tags member.
@client.event
async def on_member_join(member):
    print('New member ' + str(member) + ' joined.')
    general_channel = client.get_channel(786992346666500139)
    await general_channel.send('It\'s Time to Duel, ' + str(member.mention) + '!')


# Message for a user who leaves, or gets kicked/banned. Does not tag user.
@client.event
async def on_member_remove(member):
    print('Member ' + str(member) + ' removed.')
    general_channel = client.get_channel(786992346666500139)
    await general_channel.send('The heart of the cards is no longer with ' + str(member) + '. Farewell, friend.')


# Command to start a Battle Pack: Epic Dawn tournament.
@client.command(name='new')
async def new(context):

    global tournament_in_progress
    global tourney_members
    global tournament_host

    # Initialize tournament
    if tournament_in_progress:

        # Reply to whoever typed the command
        num_members = len(tourney_members)
        message = 'Tournament is already in progress ({} member(s) signed up). Enter !join to enter, or ' \
                  '!begin to start the tournament.'.format(num_members)
    else:

        # Set tourney status to True
        tournament_in_progress = True
        print('Tournament has started.')
        tournament_host = context.message.author
        print('Tournament host is ' + str(tournament_host))
        message = 'Waiting for members in queue (min. 1). Enter !join to enter, or !begin to start the tournament.'

    await context.message.channel.send(content=message)


# Command for a member to join the tournament queue.
@client.command(name='join')
async def join(context):

    global tournament_in_progress
    global tourney_members

    if tournament_in_progress:

        # Add member to list
        if context.message.author in tourney_members:

            message = 'You are already in queue, ' + str(context.message.author.mention) + '.'
        else:
            entrant = context.message.author
            tourney_members.append(entrant)
            print(str(entrant) + ' joined the entry queue.')
            message = 'Added ' + str(entrant.mention) + ' to the entry queue (' \
                      + str(len(tourney_members)) + ' entrant(s) now). Enter !unjoin to leave entry queue.'
    else:

        # No tournament in progress, nothing to join
        message = 'No tournament to join. Enter !new to host one.'

    await context.message.channel.send(content=message)


# Command to remove self from the tournament queue.
@client.command(name='unjoin')
async def unjoin(context):

    global tournament_in_progress
    global tourney_members

    if tournament_in_progress:

        leaver = context.message.author

        # Check if member is in list
        if leaver in tourney_members:

            tourney_members.remove(leaver)
            print(str(leaver) + ' has left the entry queue.')
            message = 'Removed you from entry queue, ' + str(leaver.mention) + '.'

        # Error message for non-entrant
        else:

            message = 'You are not in the entry queue, ' + str(leaver.mention) + '.'
    else:

        # No tournament in progress, nothing to join
        message = 'No tournament to un-join. Enter !new to host one.'

    await context.message.channel.send(content=message)


# Command that cancels a tournament.
@client.command(name='cancel')
async def cancel(context):

    global tournament_in_progress
    global tourney_members
    global tournament_host

    if tournament_in_progress:

        # First check that user is the host
        canceller = context.message.author

        if canceller == tournament_host:

            # Cancel code
            tournament_in_progress = False
            tourney_members.clear()
            tournament_host = ''
            message = 'Tournament has been cancelled by host.'
            print(message)
        else:

            # Error message
            message = 'You are not the host. Only ' + str(tournament_host.mention) + ' can cancel.'
    else:

        # No tournament in progress, nothing to join
        message = 'No concurrent tournament to cancel.'

    await context.message.channel.send(content=message)


# Command to begin the tournament process:
# 1. The bot will DM each member and:
# 1-1. Generate a Deck, showing the contents of all 10 Battle Pack: Epic Dawn packs.
# 1-2. Upload a .ydk file with all of the Deck's contents.
# 2. The bot will close the tournament, allowing a new tournament to initialize.
@client.command(name='begin')
async def begin(context):

    global tournament_in_progress
    global tourney_members
    global tournament_host

    # Check that tournament is running
    if tournament_in_progress and context.message.author == tournament_host:

        # Check that there are at least 1 member(s)
        if len(tourney_members) > 0:

            # DM each member
            generate_decks = 'Generating Deck lists and .ydk files. Please check your DMs.'
            print(generate_decks)
            await context.message.channel.send(content=generate_decks)
            members_tag = ''
            for member in tourney_members:

                members_tag += str(member.mention) + ' '

                # Generate deck
                dm_message = 'Here are your Battle Pack: Epic Dawn pulls:\n\n'
                user_deck = main.generate_deck(main.bp_epic_dawn())
                card_index = 0

                # Print each pack result
                for card in user_deck:

                    # Pack number
                    if card_index % 5 == 0:
                        pack_number = int(card_index / 5) + 1
                        dm_message += 'Pack number {}:\n```'.format(str(pack_number))

                    # Print card contents in form BP01-EN(id): (name) (Rarity)
                    dm_message += 'BP01-EN' + str(card['id']).zfill(3)
                    dm_message += ': ' + card['name']
                    dm_message += ' (' + card['rarity'] + ')'

                    # Check if end of pack
                    if card_index % 5 == 4:
                        dm_message += '```\n'

                        # Send DM
                        await member.send(dm_message)
                        dm_message = ''
                    else:
                        dm_message += '\n'

                    # Increment card_index
                    card_index += 1

                # Generate a .ydk file
                main.generate_ydk(user_deck)

                # Send user the file
                user_file = discord.File('./bp_epic_dawn.ydk')
                await member.send(file=user_file)

            # Tag all members
            await context.message.channel.send(content=members_tag)

            # Create final message
            message = 'All Decks and .ydk files sent.\n\n'
            message += 'Tournament Instructions:\n1. Download bp_epic_dawn.ydk.' \
                       '\n2. Go to https://duelingbook.com/html5 .\n3. Log in or create an account.\n'
            message += '4. Go to Deck Constructor.\n5. Click Import Deck and load bp_epic_dawn.ydk.\n'
            message += '6. Make sure that your Main Deck has a **minimum of 30 cards.**\n'
            message += '7. Save Deck, Exit, enter Duel Room, and have fun!\n\n'
            message += 'Contact tournament host ' + str(tournament_host.mention) + ' for additional information.'

            # Reset everything
            tournament_in_progress = False
            tourney_members.clear()
            tournament_host = ''
            print('Tourney complete.')

        else:

            message = 'You need at least 1 member(s) joining. Enter !join to enter queue.'

    else:

        if context.message.author != tournament_host and tournament_host != '':
            message = 'Only the tournament host can begin the tourney.'
        else:
            # No tournament in progress, nothing to join
            message = 'No current tournament in progress. Enter !new to start a tournament.'

    await context.message.channel.send(content=message)


# Command that displays all commands.
@client.command(name='commands')
async def commands(context):
    message = '**!new** - creates a tournament queue\n**!join** - puts user into tournament queue\n'
    message += '**!unjoin** - removes user from tournament queue\n**!begin** - runs tournament procedure\n'
    message += '**!cancel** - (host) cancels current tournament queue\n**!commands** - displays all commands'

    await context.message.channel.send(content=message)

client.run('Nzg2OTQ4ODE5MDYwMjYwODg2.X9N1Mw.d5p-SVt4XOPIw5yMPe1hX19WYrM')
