from decimal import Decimal

class TimeEntry:

    def __init__(self, payPeriodStart, payPeriodEnd, date,
                paycode: str, hours: Decimal, exceptions: str,
                clockIns: [], clockOuts: []):
        self.PayPeriodStart = payPeriodStart
        self.PayPeriodEnd = payPeriodEnd
        self.Date = date
        self.PayCode = paycode
        self.Hours = hours
        self.Exceptions = exceptions
        self.ClockIns = clockIns
        self.ClockOuts = clockOuts

    def RegularHours(self):
        if self.PayCode == "REGULAR":
            return self.Hours
        else:
            return 0

    def OverTimeHours(self):
        if self.PayCode == "OT":
            return self.Hours
        else:
            return 0

    def SalaryHours(self):
        if self.PayCode == "REGSAL":
            return self.Hours
        else:
            return 0

    def CsvStr(self):
        clockwatch = self.ClockIns
        output = '"' + self.PayPeriodStart + '","' + \
            self.PayPeriodEnd + '","' + \
            self.Date + '","' + \
            self.Hours.__str__() + '","' + \
            self.PayCode + '","' + \
            self.Exceptions

        if len(self.ClockIns) == 0:
            self.ClockIns.append('')
        if len(self.ClockOuts) == 0:
            self.ClockOuts.append('')

        for t in range(len(self.ClockIns)):
            output = output + '","' + \
                    self.ClockIns[t] + '","' + self.ClockOuts[t]

        output = output + '"\n'
        return output

class Timecardv2:

    def __init__(self, associateOId: str, workerId: str,
                 firstName: str, lastName: str,
                 timeentries: []):
        self.AssociateOID = associateOId
        self.WorkerID = workerId
        self.FirstName = firstName
        self.LastName = lastName
        self.Entries = timeentries

    def CsvStr(self):
        output = ''
        for TE in self.Entries:
            output = output + self.AssociateOID + '","' + \
                self.WorkerID + '","' + \
                self.FirstName + '","' + \
                self.LastName + '",' + \
                TE.CsvStr()
        return output

class Timecard:

    def __init__(self, associateOId: str, workerId: str,
                 firstName: str, lastName: str,
                 payPeriodStart, payPeriodEnd, date,
                 paycode: str, hours: Decimal, exceptions: str,
                 clockIns: [], clockOuts: []):
        self.AssociateOID = associateOId
        self.WorkerID = workerId
        self.FirstName = firstName
        self.LastName = lastName
        self.PayPeriodStart = payPeriodStart
        self.PayPeriodEnd = payPeriodEnd
        self.Date = date
        self.PayCode = paycode
        self.Hours = hours
        self.Exceptions = exceptions
        self.ClockIns = clockIns
        self.ClockOuts = clockOuts


    @staticmethod
    def csvTitles():
        return '"Associate_ID","Worker_ID","First_Name","Last_Name","Pay_Period_Start","Pay_Period_End","Date","Regular_Hours","Overtime_Hours","Salary_Hours","Exceptions","Clock-In_Time_1","Clock-Out_Time_1","Clock-In_Time_2","Clock-Out_Time_2"\n'

    def CsvStr(self):
        pass

    def csvStr(self):
        output = '"' + self.AssociateOID + '","' + \
            self.WorkerID + '","' + \
            self.FirstName + '","' + \
            self.LastName + '","' + \
            self.PayPeriodStart + '","' + \
            self.PayPeriodEnd + '","' + \
            self.Date + '","' + \
            self.RegularHours().__str__() + '","' + \
            self.OverTimeHours().__str__() + '","' + \
            self.SalaryHours().__str__() + '","' + \
            self.Exceptions
        # output = output + self.RegularHours()
        # output = output + '","'
        # output = output + self.OverTimeHours()
        # output = output + '","'
        # output = output + self.SalaryHours()
        # output = output + '","' + self.Exceptions
        for t in range(0, len(self.ClockIns) - 1):
            output = output + '","' + \
                    self.ClockIns[t] + '","' + self.ClockOuts[t]
        output = output + '"\n'
        return output
    # def csvStr_2(self):
    #     return '"' + self.AssociateOID + '","' + \
    #         self.WorkerID + '","' + \
    #         self.FirstName + '","' + \
    #         self.LastName + '","' + \
    #         self.PayPeriodStart + '","' + \
    #         self.Date + '","' + \
    #         self.Hours + '","' + \
    #         self.PayCode + '","' + \
    #         self.Exceptions + '","' + \
    #         self.ClockInTime1 + '","' + \
    #         self.ClockOutTime1 + '","' + \
    #         self.ClockInTime2 + '","' + \
    #         self.ClockOutTime2 + '"'

    def PayType(self):
        switcher = {
            "REGSAL": "REGULAR SALARY",
            "REGULAR": "REGULAR",
            "UPT": "UNPAID TIME OFF",
            "PTO": "PAID TIME OFF",
            "SAL VACATION": "SALARY VACATION",
            "VACATION": "VACATION",
            "OVERTIME": "OVERTIME",
            "HOLIDAY": "HOLIDAY",
            "FF-PSL-EE": "WHO",
            "FF-FMLA": "WHAT",
            "FF-PSL-FAM": "WHERE"
        }
        return switcher[self.PayCode]

    def RegularHours(self):
        if self.PayCode == "REGULAR":
            return self.Hours
        else:
            return 0

    def OverTimeHours(self):
        if self.PayCode == "OT":
            return self.Hours
        else:
            return 0

    def SalaryHours(self):
        if self.PayCode == "REGSAL":
            return self.Hours
        else:
            return 0
