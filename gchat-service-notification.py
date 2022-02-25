#!/usr/bin/env python3
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--longdatetime', help='LONGDATETIME ($icinga.long_date_time$)', required=True)
parser.add_argument('-e', '--servicename', help='SERVICENAME ($service.name$)', required=True)
parser.add_argument('-l', '--hostname', help='HOSTNAME ($host.name$)', required=True)
parser.add_argument('-n', '--hostdisplayname', help='HOSTDISPLAYNAME ($host.display_name$)', required=True)
parser.add_argument('-o', '--serviceoutput', help='SERVICEOUTPUT ($service.output$)', required=True)
parser.add_argument('-r', '--useremail', help='USEREMAIL ($user.email$)', required=True)
parser.add_argument('-s', '--servicestate', help='SERVICESTATE ($service.state$)', required=True)
parser.add_argument('-t', '--notificationtype', help='NOTIFICATIONTYPE ($notification.type$)', required=True)
parser.add_argument('-u', '--servicedisplayname', help='SERVICEDISPLAYNAME ($service.display_name$)', required=True)
parser.add_argument('-W', '--gchat_webhook_url', help='GCHAT_WEBHOOK_URL ($gchat_webhook_url$)', required=True)
parser.add_argument('-4', '--hostaddress', help='HOSTADDRESS ($address$)')
parser.add_argument('-6', '--hostaddress6', help='HOSTADDRESS6 ($address6$)')
parser.add_argument('-b', '--notificationauthorname', help='NOTIFICATIONAUTHORNAME ($notification.author$)')
parser.add_argument('-c', '--notificationcomment', help='NOTIFICATIONCOMMENT ($notification.comment$)')
parser.add_argument('-i', '--icinga2weburl', help='ICINGAWEB2URL ($notification_icingaweb2url$)')
parser.add_argument('-f', '--mailfrom', help='MAILFROM ($notification_mailfrom$)')
parser.add_argument('-v', '--verbose', type=bool, help='Verbose ($notification_sendtosyslog$)')
args = parser.parse_args()

notification_message = f'''
{args.servicedisplayname} on {args.hostdisplayname} is {args.servicestate}!

Info:   {args.serviceoutput}

When:   {args.longdatetime}
Service:{args.servicename}
Host:   {args.hostname}
'''

if args.hostaddress:
    notification_message += f'IPv4:   {args.hostaddress}\n'
if args.hostaddress6:
    notification_message += f'IPv6:   {args.hostaddress6}\n'
if args.notificationcomment:
    notification_message += f'Comment by {args.notificationauthorname}:   {args.notificationcomment}\n'
if args.icinga2weburl:
    notification_message += f'URL:    {args.icinga2weburl}/monitoring/service/show?host={args.hostname}&service={args.servicename}\n'

r = requests.post(args.gchat_webhook_url, json={'text': notification_message})
if r.status_code >= 400:
    print(r.text)
    exit(1)

