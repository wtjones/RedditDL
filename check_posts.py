from application_context import ApplicationContext
import argparse


""" Use this file for requesting posts. This can be setup as a scheduled task using cron or scheduler of choice."""
def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--subreddit', required=True, help='SubReddit to query')
    parser.add_argument('--getType', required=True,help='Type of request valid options:"get_top","get_rising","get_new"')
    parser.add_argument('--limit', required=True,help='Max records to pull.')
 
    args = parser.parse_args()
    ac = ApplicationContext()
    ac.enqueueGetPostsFromReddit(args.subreddit, args.getType, args.limit)
     
if __name__ == "__main__":
    # execute only if run as a script
    main()