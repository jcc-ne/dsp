# The football.csv file contains the results from the English Premier League.
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season
# (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them).
# Write a program to read the file,
# then print the name of the team with the smallest
# difference in 'for' and 'alainst' goals.
# The below skeleton is optional.  You can use it or you
# can write the script with an approach of your choice.


import csv


def read_data(data='football.csv'):
    # COMPLETE THIS FUNCTION
    rows = []
    with open(data, 'r') as f:
        r = csv.reader(f)
        cols = r.next()
        for row in r:
            rows.append(row)
    return cols, rows


class football(object):
    def __init__(self):
        self.cols, self.rows = read_data()

    def get_min_score_difference(self, flagVerbose=False):
        # COMPLETE THIS FUNCTION
        idx_goals = self.cols.index('Goals')
        idx_goalsallowed = self.cols.index('Goals Allowed')

        mindiff = 999
        minteam = None
        for i, self.row in enumerate(self.rows):
            diff = abs(int(self.row[idx_goals]) -
                       int(self.row[idx_goalsallowed]))
            team = self.get_team(i)
            if diff < mindiff:
                mindiff = diff
                minteam = team
            if flagVerbose:
                print '{} diff {}'.format(team, diff)
        return mindiff, minteam

    def get_team(self, index_value):
        # COMPLETE THIS FUNCTION
        idx_team = self.cols.index('Team')
        return self.rows[index_value][idx_team]


fbl = football()
diff, team = fbl.get_min_score_difference(flagVerbose=True)
print '\n---------- Results ---------'
print 'min_diff =', diff
print 'team = ', team
