import json
from Timecard import Timecard

class ResponseFilter:

    # Return Dictionary of json string
    @staticmethod
    def deserialize(son: str):
        # dictionary = json.loads(response.text)
        pass

    @staticmethod
    def createTimecard(son: dict):
        # son is from list of timecards

        # Timecard Collection
        TC = []

        #if(son.keys().__contains__('associateOID'))
        associateOid = son['associateOID']
        workerId = son['workerID']
        firstName = son['personLegalName']['givenName']
        lastName = son['personLegalName']['familyName1']

        for timeCards in son["timeCards"]:
            payPeriodStart = timeCards['timePeriod']['startDate']
            payPeriodEnd = timeCards['timePeriod']['endDate']
            print("  StartP")
            print(payPeriodStart)
            print("  EndP")
            print(payPeriodEnd)

            #date
            #regular hours
            #overtime hours
            #salary hours
            #clockIns
            entryDate = ''
            clockIns = []  # need to make array of ins

            clockOuts = []  # need to make array of outs
            hours = ''
            payCode = ''
            startExcept = {"": ""}
            endExcept = ''
            exceptions = ''
            # May not exist. Check keys for it
            if "dayEntries" in timeCards.keys():
                # Day entries is a list
                for dayEntry in timeCards["dayEntries"]:
                    # Grab Date
                    if "entryDate" in dayEntry.keys():
                        entryDate = dayEntry["entryDate"]
                        print("  Date")
                        print(entryDate)
                    # Check for Time Entries
                    if "timeEntries" in dayEntry.keys():
                        # Time Entries is a list
                        tec = 0
                        for timeEntry in dayEntry["timeEntries"]:
                            # Start Time
                            if "startPeriod" in timeEntry.keys():
                                # Grab ClockIn DateTime
                                if "startDateTime" in timeEntry["startPeriod"]:
                                    clockIns.append(timeEntry["startPeriod"]["startDateTime"])
                                    #
                                    # if clockIns[0] != "":
                                    #     clockIns[1] = timeEntry["startPeriod"]["startDateTime"]
                                    # else:
                                    #     clockIns[0] = timeEntry["startPeriod"]["startDateTime"]
                                    print("  IN")
                                    print(clockIns)
                            # End Time
                            if "endPeriod" in timeEntry.keys():
                                # Grab Clock out DateTime
                                if "endDateTime" in timeEntry["endPeriod"].keys():
                                    clockOuts.append(timeEntry["endPeriod"]["endDateTime"])
                                #     # clockOuts = timeEntry["endPeriod"]["endDateTime"]
                                #     # Check for first Clock out
                                #     if clockOuts[0] != "":
                                #         clockOuts[1] = timeEntry["endPeriod"]["endDateTime"]
                                #     else:
                                #         clockOuts[0] = timeEntry["endPeriod"]["endDateTime"]
                                print("  OUT")
                                print(clockOuts)
                            # Check for Entry Totals
                            if "entryTotals" in timeEntry.keys():
                                # Entry Totals is a list
                                for entryTotals in timeEntry["entryTotals"]:
                                    # Check for timeDuration (hours)
                                    if "timeDuration" in entryTotals.keys():
                                        hours = entryTotals["timeDuration"]
                                        print("  Hours")
                                        print(hours)
                                    # Check for Pay Code
                                    if "payCode" in entryTotals.keys():
                                        # Check for Code Value
                                        if "codeValue" in entryTotals["payCode"].keys():
                                            # Need to find a way to have more than one paycode
                                            payCode = entryTotals["payCode"]["codeValue"]
                                            print("  PayCode")
                                            print(payCode)

                            # Exceptions
                            if "exceptions" in timeEntry.keys():
                                # Exceptions is list
                                for exc in timeEntry['exceptions']:
                                    if exceptions != '':
                                        exceptions = exceptions + ', ' + exc['exceptionDescription']
                                        # print(exc['exceptionDescription'])
                                    else:
                                        exceptions = exc['exceptionDescription']
                                        # print(exc['exceptionDescription'])
                            print("  Except")
                            print(exceptions)

                            # Increment time entry count
                            tec += 1

            # Create TimeCard
            newCard = Timecard(associateOid, workerId, firstName, lastName,
                               payPeriodStart, payPeriodEnd, entryDate, payCode,
                               hours, exceptions, clockIns, clockOuts)
            TC.append(newCard)

        return TC

