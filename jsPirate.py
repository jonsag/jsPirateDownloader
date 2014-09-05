#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import getopt, sys, os

from myFunctions import parseXml, onError, inFilePart, getVideos

##### handle arguments #####
url = ""
inFile = ""
name = ""
setQuality = ""
listOnly = False

try:
    myopts, args = getopt.getopt(sys.argv[1:],'u:f:n:q:l' , ['url=', 'file=', 'name=', 'quality=', '--list'])

except getopt.GetoptError as e:
    onError(1, str(e))

if len(sys.argv) == 1: # no options passed
    onError(2, 2)

for option, argument in myopts:
    if option in ('-u', '--url'):
        url = argument
    elif option in ('-f', '--file'):
        inFile = argument
        if not os.path.isfile(inFile):
            onError(4, inFile)
    elif option in ('-n', '--name'):
        name = argument
    elif option in ('-q', '--quality'):
        setQuality = int(argument)
    elif option in ('-l', '--list'):
        listOnly = True

if url and not name:
    onError(5, 5)
elif name and not url:
    onError(6, 6)

if url:
    downloads = parseXml(url, name, setQuality)
elif inFile:
    downloads = inFilePart(inFile, setQuality)

if not listOnly:
    if downloads:
        infoDownloaded = getVideos(downloads)
    else:
        infoDownloaded = ""
        print "\nCould not find any streams to download"
else:
    print "\nListing only"
    if downloads:
        for line in downloads:
            print line

for line in infoDownloaded:
    print "\nVideo: %s" % line['videoName']
    print "-------------------------------------------------------------------------"
    print "File size: %s b" % line['fileSize']
    print "File size: %s" % line['fileSizeMeasure']
    print "Duration: %s ms" % line['duration']
    print "Duration: %s" % line['durationFormatted']
    print "Overall bit rate: %s bps" % line['overallBitRate']
    print "Overall bit rate: %s" % line['overallBitRateMeasure']

    print "\nVideo format: %s" % line['videoFormat']
    print "Video codec ID: %s" % line['videoCodecId']
    print "Video bit rate: %s bps" % line['videoBitRate']
    print "Video bit rate: %s" % line['videoBitRateMeasure']
    print "Width: %s px" % line['width']
    print "Height: %s px" % line['height']
    print "Frame rate: %s fps" % line['frameRate']
    print "Frame count: %s" % line['frameCount']

    print "\nAudio format: %s" % line['audioFormat']
    print "Audio codec ID: %s" % line['audioCodecId']
    print "Audio bit rate: %s bps" % line['audioBitRate']
    print "Audio bit rate: %s" % line['audioBitRateMeasure']

    print "\nSubtitles: %s" % line['subName']
    print "-------------------------------------------------------------------------"
    print "File size: %s b" % line['subSize']
    print "Number of lines: %s" % line['subLines']
