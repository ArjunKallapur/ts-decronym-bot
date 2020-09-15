import config
import json
import praw
import secrets
from tabulate import tabulate
import utils

class DecronymBot:
    '''
    DecronymBot is a class used to represent ts-decronym-bot

    This class uses the praw API to interact with reddit
    '''
    def __init__(self, discography_file : str, songs_file : str):
        '''
        The constructor for `DecronymBot` class. 

        Requires the names of files containing discography and the file to
        write the songs json to. 
        '''
        self.songs = {}
        self.viewed_posts = []
        self.user_name = ""
        self.discography_file = discography_file
        self.songs_file = songs_file
    
    def bot_login(self) -> praw.Reddit:
        '''
        Return logged in reddit instance. 

        Use praw and credentials from `config.py` and `secrets.py` to create an instance that is 
        logged in to reddit
        '''
        #
        #
        #
        # log in using praw
        reddit = praw.Reddit(username = config.USERNAME,
                    password = secrets.PASSWORD,
                    client_id = secrets.CLIENT_ID,
                    client_secret = secrets.CLIENT_SECRET,
                    user_agent = config.USER_AGENT)
        return reddit
    
    def handle_submission(self, submission: praw.models.Submission, songs: dict) -> list:
        '''
        Return list of `(abbreviations, long_form, album)` tuples in a submission. 

        Takes in a submission and searches the submission body and comments for 
        any known acronyms, returns a list of 
        `[(abbreviation, long_form, album_name)]` tuples. 
        '''
        songs_matched = []
        comment_information = []
        #
        #
        #
        # look for abbreviations in the submission body.
        for word in submission.selftext:
            search_key = word.upper()
            if search_key in songs and search_key not in songs_matched:
                songs_matched.append(search_key)
                comment_information.append((search_key, songs[search_key]['long_form'], songs[search_key]['album_name']))
        #
        #
        #
        # do the same for comments on this post
        for comment in submission.comments:
            for word in comment.body:
                search_key = word.upper()
                if search_key in songs and search_key not in songs_matched:
                    songs_matched.append(search_key)
                    comment_information.append((search_key, songs[search_key]['long_form'], songs[search_key]['album_name']))

        return comment_information
    
    def run_bot(self, reddit: praw.Reddit):
        '''
        Run ts-decode-bot indefinitely. 

        Run the ts-decode-bot by fetching recent posts and checking for
        abbreviations in submissions from the subreddit in `config.SUBREDDIT`
        '''
        #
        #
        #
        # load the json into a dict
        try:
            f = open('songs.json', 'r')
        except IOError as err:
            print('Error opening file {0}: {1}'.format('songs.json', err))   
        else:
            songs = json.load(f)
        #
        #
        #
        # read in posts from the subreddit in config.py
        subreddit = reddit.subreddit(config.SUBREDDIT)
        for submission in subreddit.stream.submissions():
            if submission.id not in self.viewed_posts:
                (self.viewed_posts).append(submission.id)
                comment_information = handle_submission(submission, songs)
                if comment_information:
                    # we have stuff to comment
                    comment = self._pretty_print_comment(comment_information)
                    submission.add_comment(comment)
        return
    
    def _pretty_print_comment(self, comment_information : list) -> str:
        '''
        Helper function to pretty print the comment text before commenting it
        \n
        Raises: \n
        `ValueError` if called with an empty list

        '''
        #
        #
        #
        # verify that the list is not empty
        if comment_information:
            return tabulate(comment_information, headers = config.HEADERS, tablefmt = config.TABLEFMT)
        else:
            # list is empty, panic
            raise ValueError('`_pretty_print_comment` called with empty list')

        

if __name__=="__main__":
    pass
