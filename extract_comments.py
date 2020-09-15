# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.firefox.options import Options
import sys
import time
import calendar
from bs4 import BeautifulSoup as bs
import json
import re
import requests
import datefinder
import re
import lxml
from find_feedback_id import feedback_id,doc_id


link='https://www.facebook.com/api/graphql/'

payload=f'doc_id={doc_id}&variables=%7B%22after%22%3Anull%2C%22before%22%3Anull%2C%22displayCommentsFeedbackContext%22%3A%22%7B%5C%22bump_reason%5C%22%3A0%2C%5C%22comment_expand_mode%5C%22%3A1%2C%5C%22comment_permalink_args%5C%22%3A%7B%5C%22comment_id%5C%22%3Anull%2C%5C%22reply_comment_id%5C%22%3Anull%2C%5C%22filter_non_supporters%5C%22%3Anull%7D%2C%5C%22interesting_comment_fbids%5C%22%3A%5B%5D%2C%5C%22is_location_from_search%5C%22%3Afalse%2C%5C%22last_seen_time%5C%22%3Anull%2C%5C%22log_ranked_comment_impressions%5C%22%3Atrue%2C%5C%22probability_to_comment%5C%22%3A0%2C%5C%22story_location%5C%22%3A9%2C%5C%22story_type%5C%22%3A0%7D%22%2C%22displayCommentsContextEnableComment%22%3Afalse%2C%22displayCommentsContextIsAdPreview%22%3Afalse%2C%22displayCommentsContextIsAggregatedShare%22%3Afalse%2C%22displayCommentsContextIsStorySet%22%3Afalse%2C%22feedLocation%22%3A%22PERMALINK%22%2C%22feedbackID%22%3A%22{feedback_id}%3D%22%2C%22feedbackSource%22%3A2%2C%22first%22%3A48%2C%22focusCommentID%22%3Anull%2C%22includeNestedComments%22%3Atrue%2C%22isInitialFetch%22%3Afalse%2C%22isComet%22%3Afalse%2C%22containerIsFeedStory%22%3Atrue%2C%22containerIsWorkplace%22%3Afalse%2C%22containerIsLiveStory%22%3Afalse%2C%22containerIsTahoe%22%3Afalse%2C%22last%22%3Anull%2C%22scale%22%3A1%2C%22topLevelViewOption%22%3Anull%2C%22useDefaultActor%22%3Atrue%2C%22viewOption%22%3Anull%2C%22UFI2CommentsProvider_commentsKey%22%3Anull%7D&server_timestamps=true'


headers = { 
    
"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',


"content-type": 'application/x-www-form-urlencoded',


"sec-fetch-site": 'same-origin',

}

### Request 
response=requests.post(link, headers=headers,data=payload)

#load data
data=json.loads(response.text)

### extract start cursor

extract_st_cursor=data['data']['feedback']['display_comments']['page_info']['start_cursor']

payload=f'doc_id={doc_id}&variables=%7B%22after%22%3A%22{extract_st_cursor}%22%2C%22before%22%3Anull%2C%22displayCommentsFeedbackContext%22%3A%22%7B%5C%22bump_reason%5C%22%3A0%2C%5C%22comment_expand_mode%5C%22%3A1%2C%5C%22comment_permalink_args%5C%22%3A%7B%5C%22comment_id%5C%22%3Anull%2C%5C%22reply_comment_id%5C%22%3Anull%2C%5C%22filter_non_supporters%5C%22%3Anull%7D%2C%5C%22interesting_comment_fbids%5C%22%3A%5B%5D%2C%5C%22is_location_from_search%5C%22%3Afalse%2C%5C%22last_seen_time%5C%22%3Anull%2C%5C%22log_ranked_comment_impressions%5C%22%3Atrue%2C%5C%22probability_to_comment%5C%22%3A0%2C%5C%22story_location%5C%22%3A9%2C%5C%22story_type%5C%22%3A0%7D%22%2C%22displayCommentsContextEnableComment%22%3Afalse%2C%22displayCommentsContextIsAdPreview%22%3Afalse%2C%22displayCommentsContextIsAggregatedShare%22%3Afalse%2C%22displayCommentsContextIsStorySet%22%3Afalse%2C%22feedLocation%22%3A%22PERMALINK%22%2C%22feedbackID%22%3A%22{feedback_id}%3D%22%2C%22feedbackSource%22%3A2%2C%22first%22%3A48%2C%22focusCommentID%22%3Anull%2C%22includeNestedComments%22%3Atrue%2C%22isInitialFetch%22%3Afalse%2C%22isComet%22%3Afalse%2C%22containerIsFeedStory%22%3Atrue%2C%22containerIsWorkplace%22%3Afalse%2C%22containerIsLiveStory%22%3Afalse%2C%22containerIsTahoe%22%3Afalse%2C%22last%22%3Anull%2C%22scale%22%3A1%2C%22topLevelViewOption%22%3Anull%2C%22useDefaultActor%22%3Atrue%2C%22viewOption%22%3Anull%2C%22UFI2CommentsProvider_commentsKey%22%3Anull%7D&server_timestamps=true'

headers = { 
"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',


"content-type": 'application/x-www-form-urlencoded',


"sec-fetch-site": 'same-origin',

}

### Request 
response1=requests.post(link, headers=headers,data=payload)

data2=json.loads(response1.text)

extract_data=data2['data']['feedback']['display_comments']['edges']


import datetime


def extract_comments(yt):
        
        # post_id
        pt_id=yt['node']['legacy_token']
        post_id=pt_id.partition('_')[0] 
        
        
        #comments_date
        comt_date=datetime.datetime.fromtimestamp(int(yt['node']['created_time']))
        
        #comments_author_name
        author_name=yt['node']['author']['name']
        
        #author_id
        author_id=yt['node']['author']['id']
    
        #comments_message
        message_cmt=yt['node']['body']['text']
        
        #comments_id
        ct_id=yt['node']['legacy_token']
        comment_id=ct_id.partition('_')[2] 
        
        #comments_url
        comment_url=yt['node']['url']
        
        return post_id,comt_date,comment_id,author_name,author_id,message_cmt,comment_url
        
 

postBigDict = list()

   
while (True):
    
    for item in extract_data:
        
        try:
            postDict = dict()
        
            post_id,comt_date,comment_id,author_name,author_id,message_cmt,comment_url=extract_comments(item)

            postDict['PostId'] = post_id
            postDict['Comment_Date'] = str(comt_date)
            postDict['Comment_id']=comment_id
            postDict['Comment_author_name'] =author_name
            postDict['Comment_author_id']=author_id
            postDict['Comment_Message'] = message_cmt
            postDict['Comment_url'] = comment_url

            #Add to check
            postBigDict.append(postDict)
        
        except:
            pass


    extract_end_cursor=data2['data']['feedback']['display_comments']['page_info']['end_cursor'] 
        
    extract_next_page=data2['data']['feedback']['display_comments']['page_info']['has_next_page'] 

    if extract_end_cursor != None:
        
        payload=f'doc_id={doc_id}&variables=%7B%22after%22%3A%22{extract_end_cursor}%22%2C%22before%22%3Anull%2C%22displayCommentsFeedbackContext%22%3A%22%7B%5C%22bump_reason%5C%22%3A0%2C%5C%22comment_expand_mode%5C%22%3A1%2C%5C%22comment_permalink_args%5C%22%3A%7B%5C%22comment_id%5C%22%3Anull%2C%5C%22reply_comment_id%5C%22%3Anull%2C%5C%22filter_non_supporters%5C%22%3Anull%7D%2C%5C%22interesting_comment_fbids%5C%22%3A%5B%5D%2C%5C%22is_location_from_search%5C%22%3Afalse%2C%5C%22last_seen_time%5C%22%3Anull%2C%5C%22log_ranked_comment_impressions%5C%22%3Atrue%2C%5C%22probability_to_comment%5C%22%3A0%2C%5C%22story_location%5C%22%3A9%2C%5C%22story_type%5C%22%3A0%7D%22%2C%22displayCommentsContextEnableComment%22%3Afalse%2C%22displayCommentsContextIsAdPreview%22%3Afalse%2C%22displayCommentsContextIsAggregatedShare%22%3Afalse%2C%22displayCommentsContextIsStorySet%22%3Afalse%2C%22feedLocation%22%3A%22PERMALINK%22%2C%22feedbackID%22%3A%22{feedback_id}%3D%22%2C%22feedbackSource%22%3A2%2C%22first%22%3A48%2C%22focusCommentID%22%3Anull%2C%22includeNestedComments%22%3Atrue%2C%22isInitialFetch%22%3Afalse%2C%22isComet%22%3Afalse%2C%22containerIsFeedStory%22%3Atrue%2C%22containerIsWorkplace%22%3Afalse%2C%22containerIsLiveStory%22%3Afalse%2C%22containerIsTahoe%22%3Afalse%2C%22last%22%3Anull%2C%22scale%22%3A1%2C%22topLevelViewOption%22%3Anull%2C%22useDefaultActor%22%3Atrue%2C%22viewOption%22%3Anull%2C%22UFI2CommentsProvider_commentsKey%22%3Anull%7D&server_timestamps=true'
        
        ### recursive function
        response1=requests.post(link, headers=headers,data=payload)
    
        data2=json.loads(response1.text)
        
        extract_data=data2['data']['feedback']['display_comments']['edges']
    else:
        break

     
with open('./postBigDict.json','w', encoding='utf-8') as file:
    file.write(json.dumps(postBigDict, indent=3,ensure_ascii=False).encode('utf-8').decode())
  




    
   

