import socket

import google_auth_httplib2
import httplib2
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest

socket.setdefaulttimeout(15 * 60)

SCOPE = "https://www.googleapis.com/auth/spreadsheets"


class GoogleSheet:
    def __init__(
        self,
        spreadsheet_id: str,
        sheet_name: str,
        secrets,
        sheet_start: str,
        sheet_end: str,
    ):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.sheet_start = sheet_start
        self.sheet_end = sheet_end
        self.gsheet_connector = self.connect(secrets)
        self.dataframe = self.collect()

    def connect(self, secrets):
        # Create a connection object.
        credentials = service_account.Credentials.from_service_account_info(
            secrets,
            scopes=[SCOPE],
        )

        # Create a new Http() object for every request
        def build_request(http, *args, **kwargs):
            new_http = google_auth_httplib2.AuthorizedHttp(
                credentials, http=httplib2.Http()
            )
            return HttpRequest(new_http, *args, **kwargs)

        authorized_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http=httplib2.Http()
        )
        service = build(
            "sheets",
            "v4",
            requestBuilder=build_request,
            http=authorized_http,
        )
        gsheet_connector = service.spreadsheets()
        return gsheet_connector

    def collect(self) -> pd.DataFrame:
        values = (
            self.gsheet_connector.values()
            .get(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!{self.sheet_start}:{self.sheet_end}",
            )
            .execute()
        )

        df = pd.DataFrame(values["values"])
        df.columns = df.iloc[0]
        df = df[1:]
        return df

    def insert(self, row) -> None:
        values = (
            self.gsheet_connector.values()
            .append(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!{self.sheet_start}:{self.sheet_end}",
                body=dict(values=[row]),
                valueInputOption="USER_ENTERED",
            )
            .execute()
        )
