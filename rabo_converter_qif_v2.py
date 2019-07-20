#!/usr/bin/env python3

"""Converts Rabobank CSV to QIF"""
import datetime as dt
import os
import pandas as pd
from qifparse import qif


def main():
    today = str(dt.date.today())
    # format_str required for interpretating date by qifparse
    format_str = "%Y-%m-%d"

    # check current directory for matching files by Rabobank
    flist = []
    for file in os.listdir("."):
        if (
            file.endswith(".csv")
            and (file.startswith("CSV_A"))
            or file.startswith("CSV_O")
        ):
            flist.append(file)

    # iterate csv-files and generate related qif file(s)
    for f in flist:
        df = pd.read_csv(f, thousands=",", encoding="latin1")

        # define list of accounts and rename columns
        alist = df["IBAN/BBAN"].unique().tolist()

        columndict = {
            "Datum": "date",
            "Naam tegenpartij": "payee",
            "Omschrijving-1": "memo",
            "Bedrag": "amount",
        }
        df.rename(columns=columndict, inplace=True)
        df.loc[:, "amount"] = df["amount"] / 100

        # establish qif_obj
        qif_obj = qif.Qif()
        for a in alist:

            acc = qif.Account(name=str(a))
            qif_obj.add_account(acc)
            print(acc)

            for index, row in df[df["IBAN/BBAN"] == a].iterrows():
                # print(index,row)
                tr = qif.Transaction()
                tr.amount = row["amount"]
                tr.date = dt.datetime.strptime(row["date"], format_str)
                tr.payee = row["payee"]
                tr.memo = row["memo"]
                # tr.to_account = itag
                acc.add_transaction(tr, header="!Type:Bank")
                print(tr)
        fname = "Import_" + today + "_" + str(f) + "_.qif"
        with open(fname, "w") as output:
            output.write(str(qif_obj))

            # remove original file
            # os.remove(f)


main()
