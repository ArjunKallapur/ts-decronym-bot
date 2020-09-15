# TODO: write unit tests for this
'''
This file contains utility scripts used to generate `songs.json`, and other
templates used by the bot
'''
import json

def convert_discography_to_songs():
    '''
    Writes discography into short forms - with side effects. 

    converts `discography.json` into `songs.json` which follows the following 
    convention - \n
    `SHORTFORM : {long_form, album_name}`
    '''
    # TODO: make the file names command line arguments, hard coded for now
    #
    #
    #
    # declare the dict of acronyms to (long_form, album_name)
    abbreviations = {}
    # open the json file
    try:
        f = open('discography.json', 'r')
    except IOError as err:
        print('Error opening file {0}: {1}'.format('discography.json', err))   
    #
    #
    #
    # read the json file into a dictionary
    try:
        discography = json.load(f)
    except ValueError as err:
        print('{0} is not a valid JSON file; error: {1}', 'discography.json', err)
    #
    #
    #
    # loop through the albums
    for album in discography['albums']:
        # loop through each song, see if it may need to be decronym-ed
        for track in album['tracks']:
            # check the number of words in the track name
            track_words = track['name'].split()
            if len(track_words) > 1:
                # if the track has more than one word, make the abbreviation
                abbreviation = "".join(w[0] for w in track_words)
                # check that the abbreviation doesn't exist
                if abbreviation in abbreviations:
                    print('Duplicate key: {0}, value: {1}'.format(abbreviation, track))
                # if the abbreviation doesn't exist, add it to the dict
                else:
                    abbreviations[abbreviation] = {'long_form' : track['name'], 'album_name' : album['name']}
    #
    #
    #
    # write the dict into `songs.json`
    try:
        of = open('songs.json', 'w')
    except IOError as err:
        print('Unable to open file {0} due to error: {1}'.format('songs.json', err))
    else:
        json.dump(abbreviations, of)
    return

if __name__== "__main__":
        convert_discography_to_songs()