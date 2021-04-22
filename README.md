# platform-takehome-assessment
Take home assessment for Platform Engineer candidates.

## What this document is for

You should have received a PDF document with a take home 
assignment. This README document is intended only to help you
set up the environment and get started with this project.

Please reach out to your recruiter if you have any questions!

## Introduction

This repository contains a toy application which 
implements a rudimentary user behavior tracking API. In the
real world, we use third party tools like Segment, Amplitude, 
Mixpanel, etc. for this functionality. For this exercise, though,
we imagine that we need to implement this ourselves.

Note that, for simplification of the exercise, **we are not using
a real database**. The application simply prints an insert
statement to the terminal. 

This API is implemented as an AWS Serverless application 
using the AWS Serverless Application Model (AWS SAM). The 
underlying AWS products which implement the API (if we were 
to actually deploy it) are [AWS Lambda](https://aws.amazon.com/lambda/)
and [AWS API Gateway](https://aws.amazon.com/api-gateway/).

## System requirements

We have tested on Linux and Mac. If you use Windows, we advise 
to use a Linux VM to complete the exercise. If you're not sure 
how to do this, we suggest to start with [VirtualBox](https://www.virtualbox.org/).

## Installation

First, install [Docker](https://www.docker.com/), [git](https://git-scm.com/), 
and [curl](https://curl.se/) (if you don't already have them installed).
See [Docker's installation docs](https://docs.docker.com/engine/install/), 
and use your OS package manager to install curl and git.

After you have Docker, git, and curl installed, install AWS SAM CLI tool. 

### Linux

Download [the AWS SAM CLI zip file](https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip). 
From the location where this file is (probably `~/Downloads`), then you can run:

```bash
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
sudo ./sam-installation/install
```

### Mac

You will need to install [homebrew](https://brew.sh) if you don't already have it. 
Follow [the homebrew installation instructions](https://docs.brew.sh/Installation).

Then you can run:

```bash
brew tap aws/tap
brew install aws-sam-cli
```

### Check that SAM CLI is working

```bash
sam --version
```

If you see `SAM CLI, version 1.22.0` (or similar), it works! 🎉

If you have some issues, check 
[the AWS SAM documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html), 
or reach out to your recruiter if you're really stuck.

## Build, run, test the API

**Warning: you need to re-build the application each time you make 
changes**. AWS SAM unfortunately does not currently support
hot reloading.

Clone this repo, and navigate to the [tracking-service](./tracking-service) subdirectory.
You will run all the following commands from that location.

To build:

```bash
sam build --use-container
```

To run the API locally:

```bash
sam local start-api
```

To test the API:

```bash
curl -H "Content-Type: application/json" -XPOST --data '{"event": "click", "location": "something", "user": "sylvia", "otherParam": "otherVal"}' http://127.0.0.1:3000/track
```

You should see an SQL statement printed in blue to the terminal where the API 
is running. 

## Important files in this repo

* [app.py](tracking-service/tracking_service/app.py) - the application code
* [event.json](tracking-service/events/event.json) - a sample event that the lambda function receives
* [template.yaml](tracking-service/template.yaml) - the SAM configuration file

We expect you'll make changes primarily in `tracking-service/tracking_service/app.py`.

## Note about tests

**We like tests!** They are really important and we write lots of them!
However, in order to keep the problem simple, we've excluded them here. If you
feel that adding tests will help you work through the problem, go for it. 
However, we don't expect it, and won't give extra points for answers that 
include tests. 🙂