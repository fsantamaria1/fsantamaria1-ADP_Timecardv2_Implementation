import json
from Timecard import Timecard, Timecardv2, TimeEntry
from decimal import Decimal

class ResponseFilter:

    @staticmethod
    def parseTime(timestr: str):
        # YYYY-MM-DDTHH:MM:SS-5:00
        # Time starts at "T"
        time2 = timestr[timestr.index("T") + 1:]  # HH:MM:SS-5:00
        # Timezone starts at "-"
        return time2[:time2.index("-")]  # HH:MM:SS

    @staticmethod
    def parseHours(hourstr: str):
        # PTnH
        ho = '0'
        min = '0'
        if "M" in hourstr:
            if "H" in hourstr:
                # PTnHnM
                ho = hourstr[2:hourstr.index("H")]
                min = hourstr[hourstr.index("H") + 1:hourstr.index("M")]
            else:
                #PTnM
                min = hourstr[2:hourstr.index("M")]
        elif "H" in hourstr:
            #PTnH
            ho = hourstr[2:hourstr.index("H")]
            min = 0

        hour = Decimal(ho)
        minute = Decimal(min)

        hour = hour + minute / Decimal(60)

        return hour

    @staticmethod
    def MakeTimeEntry(timeEntry: dict, periodStart, periodEnd):

        date = ''
        hours = ''
        payCode = ''
        clockIns = []
        clockOuts = []
        exceptions = ''

        # Entry Date
        if "entryDate" in timeEntry.keys():
            date = timeEntry["entryDate"]
            print(date)
        else:
            print("Missing Entry Date")

        # Start Time
        if "startPeriod" in timeEntry.keys():
            # Grab ClockIn DateTime
            if "startDateTime" in timeEntry["startPeriod"]:
                clockIns.append(ResponseFilter.parseTime(timeEntry["startPeriod"]["startDateTime"]))
                print("  IN")
                print(clockIns)
        else:
            print("Missing Start Period")
        # End Time
        if "endPeriod" in timeEntry.keys():
            # Grab Clock out DateTime
            if "endDateTime" in timeEntry["endPeriod"].keys():
                clockOuts.append(ResponseFilter.parseTime(timeEntry["endPeriod"]["endDateTime"]))
                if len(clockIns) < len(clockOuts):
                    clockIns.append("")
            print("  OUT")
            print(clockOuts)
        else:
            print("Missing End Period")
        # Check for Entry Totals
        if "entryTotals" in timeEntry.keys():
            # Entry Totals is a list
            for entryTotals in timeEntry["entryTotals"]:
                # Check for timeDuration (hours)
                if "timeDuration" in entryTotals.keys():
                    hours = ResponseFilter.parseHours(entryTotals["timeDuration"])
                    print("  Hours")
                    print(hours)
                else:
                    print("Missing Time Duration")
                # Check for Pay Code
                if "payCode" in entryTotals.keys():
                    # Check for Code Value
                    if "codeValue" in entryTotals["payCode"].keys():
                        # Need to find a way to have more than one paycode
                        payCode = entryTotals["payCode"]["codeValue"]
                        print("  PayCode")
                        print(payCode)
                else:
                    print("Missing Paycode")
        else:
            print("Missing Entry Totals")

        # Exceptions
        if "exceptions" in timeEntry.keys():
            # Exceptions is list
            for exc in timeEntry['exceptions']:
                if exceptions != '':
                    exceptions = exceptions + ', ' + exc['exceptionDescription']
                else:
                    exceptions = exc['exceptionDescription']
        print("  Except")
        print(exceptions)

        return TimeEntry(periodStart, periodEnd, date,
                       payCode, hours, exceptions,
                       clockIns, clockOuts)

    @staticmethod
    def MakeTimecard(teamTimeCard):
        # son is from list of timecards

        TC = []

        for timeCard in teamTimeCard:
            associateOid = timeCard['associateOID']
            workerId = timeCard['workerID']['idValue']
            firstName = timeCard['personLegalName']['givenName']
            print(firstName)
            lastName = timeCard['personLegalName']['familyName1']
            print(lastName)

            for timeCards in timeCard["timeCards"]:
                payPeriodStart = timeCards['timePeriod']['startDate']
                payPeriodEnd = timeCards['timePeriod']['endDate']
                print("  StartP")
                print(payPeriodStart)
                print("  EndP")
                print(payPeriodEnd)

                # date
                # regular hours
                # overtime hours
                # salary hours
                # clockIns

                #TimeEntry List
                TE = []

                # May not exist. Check keys for it
                if "dayEntries" in timeCards.keys():
                    # Day entries is a list
                    for dayEntry in timeCards["dayEntries"]:
                        # Check for Time Entries
                        if "timeEntries" in dayEntry.keys():

                            # Time Entries is a list
                            for timeEntry in dayEntry["timeEntries"]:
                                TE.append(ResponseFilter.MakeTimeEntry(timeEntry,
                                                        payPeriodStart,
                                                        payPeriodEnd))
                        else:
                            print("Missing Time Entry")
                else:
                    print("Missing Day Entries")

                # Create TimeCard
                newCard = Timecardv2(associateOid, workerId,
                                     firstName, lastName,
                                     TE)
                TC.append(newCard)
        return TC

    @staticmethod
    def timeCardHell(son: dict):
        # I'm about to commit a crime

        # Timecard Collection
        TC = []

        if type(son) is dict:
            # Is a dictionary. Check for team time cards
            if "teamTimeCards" in son.keys():
                TC.extend(ResponseFilter.MakeTimecard(son["teamTimeCards"]))
        elif type(son) is list:
            for tch in son:
                TC.extend(ResponseFilter.timeCardHell(tch))
        else:
            print("SKIPPED SOMETHING SKIPPED SOMETHING SKIPPED SOMETHING")
        return TC

