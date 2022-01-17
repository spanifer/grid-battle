import gspread
from google.oauth2.service_account import Credentials
from src.helpers import center

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('grid_battle')
high_scores = SHEET.worksheet('high_scores')


def get_scores(msg='Fetching High Scores...'):
    '''Prints an optional message before sending the request
    Returns scores list with header sliced'''
    print(msg)
    return high_scores.get_all_values()[1:]


def is_high_score(scores, new_score):
    '''Checks if new_score is in top 10 by compareing it to
    the last element of the concatenated and sorted list'''
    if len(scores) < 10:
        return True
    if new_score is not sort_scores(scores, new_score).pop():
        return True
    return False


def sort_scores(scores, new_score):
    '''Append new score to scores
    Sorts the list by shot count value'''
    scores.append(new_score)
    return scores.sort(key=lambda r: int(r[1]))


def add_to_scores(score, index):
    '''Insert row to index
    NOTE: This somehow runs in sync'''
    high_scores.delete_rows(11)
    high_scores.insert_row(score, index+1)


def print_high_scores(scores=None):
    '''Prints the high scores fetched from sheet'''
    if not scores:
        scores = get_scores('')

    print('\n')
    print(center('High Scores', 80))
    print('\n')

    rank = 0
    for [name, shot_count], i in zip(scores, range(len(scores))):
        prev_shot_count = None
        try:
            prev_shot_count = scores[i-1][1]
        except StopIteration:
            pass
        if prev_shot_count != shot_count:
            rank += 1
        print(center(
            f'{rank} {name}    {shot_count}', 80))
