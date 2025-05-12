*** Variables ***
${CHANNEL}        slack_channelID
${WEBHOOK}        slack_webhook
${BOT_TOKEN}      slack_bot_tokken
${MESSAGE}        Hello from Robot Framework! MESSAGE
${REPLY}          This is a threaded reply!
${FILE_PATH}      D:/Extras/test.png
${TITLE}          Test Screenshot

*** Settings ***
Library           RPA.Windows
Library           testSlack.py
Library           RPA.Slack

*** Test Cases ***
slackTest
    Run Slack

Send Slack Message
    &{message}=    Create Dictionary    text=Hello from Robot Framework! message
    RPA.Slack.Slack Raw Message    ${WEBHOOK}    ${message}

Send Threaded Slack Message
    Send Message And Reply    ${BOT_TOKEN}    ${CHANNEL}    ${MESSAGE}    ${REPLY}

Send Image Link
    Upload File To Slack    ${BOT_TOKEN}    ${CHANNEL}    ${FILE_PATH}    ${TITLE}
