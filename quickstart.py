from __future__ import print_function
from gettext import Catalog

import os.path

import google

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "osca.settings")

import django
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User

from osca.wsgi import *
from catalog.models import Coop, Member, Officer, AllergySeverity, Allergy, Budget
from django.db import models

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType





os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osca.settings')
django.setup()


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'credentials.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1xrmD6ofC6BPy_S8iyrRNQi1uIbhem9b4vXLX58ZgGB4'
SAMPLE_RANGE_NAME = 'B2:M'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = credentials
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    '''if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())'''

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])







        for row in values:

            firstname = row[1]
            lastname = row[2]

            myusername = firstname+lastname
            checkuser = User.objects.filter(username=myusername).exists()
           
            if checkuser is False:
                newemail = row[0]

                tNumber = row[3]
                coop = row[4]
                coop = Coop.objects.get(name = coop)

                hours = 5
                pronouns = row[5]
                timeAid = 0
                if row[6]:
                    timeAid = int(row[6])
                hours = hours - timeAid
                restrictions = row[7]
                officer = False
                if row[8] == "Yes":
                    officer = True

                positions = None
                positionHours = None
                emergency = False

                if officer:
                    positions = row[9]
                    if row[10]:
                        positionHours = int(row[10])
                    else:
                         positionHours = 0
                    hours = hours - positionHours
                    emergency = False
                    if row[10]:
                        emergency = True

                user = User.objects.create_user(username = myusername, first_name = firstname, last_name = lastname, email = newemail, password = tNumber)
                                          
                if tNumber[0] == 't' or 'T':
                    tNumber = tNumber[1:]
                newMember = Member(first_name = firstname, last_name = lastname, tnumber = tNumber, coop = coop, pronouns = pronouns, time_aid = timeAid)
                newMember.save()
                if officer:
                    newOfficer = Officer(coop = coop, member = newMember, position_name = positions, hours_required = hours, emergency_contact = emergency)
                    officerperm = Permission.objects.get(codename='add_officer')
                    user.user_permissions.add(officerperm)

                user.save()
                print(f"{firstname}, {lastname}, {pronouns}, {positions}")
                '''
                newMember.save()
                if officer:
                    newOfficer = Officer(coop = coop, member = row, position_name = positions, hours_required = hours, emergency_contact = emergency)
                '''
                


        if not values:
            print('No data found.')
            return


    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
