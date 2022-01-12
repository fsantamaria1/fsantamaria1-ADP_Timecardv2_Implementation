

class Timecard:

    def __init__(self, associateOId: str, workerId: str,
                 firstName: str, lastName: str,
                 payPeriodStart, payPeriodEnd, date,
                 paycode: str, hours, exceptions: str,
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
        self.ClockInTime1 = clockIns[0]
        self.ClockOutTime1 = clockOuts[0]
        self.ClockInTime2 = ''
        if len(clockIns) > 1:
            self.ClockInTime2 = clockIns[1]
        self.ClockOutTime2 = ''
        if len(clockOuts) > 1:
            self.ClockOutTime2 = clockOuts[1]

    def csvStr(self):
        return '"' + self.AssociateOID + '","' + \
            self.WorkerID + '","' + \
            self.FirstName + '","' + \
            self.LastName + '","' + \
            self.PayPeriodStart + '","' + \
            self.Date + '","' + \
            self.RegularHours() + '","' + \
            self.OverTimeHours() + '","' + \
            self.SalaryHours() + '","' + \
            self.Exceptions + '","' + \
            self.ClockInTime1 + '","' + \
            self.ClockOutTime1 + '","' + \
            self.ClockInTime2 + '","' + \
            self.ClockOutTime2 + '"'

    def csvStr_2(self):
        return '"' + self.AssociateOID + '","' + \
            self.WorkerID + '","' + \
            self.FirstName + '","' + \
            self.LastName + '","' + \
            self.PayPeriodStart + '","' + \
            self.Date + '","' + \
            self.Hours + '","' + \
            self.PayCode + '","' + \
            self.Exceptions + '","' + \
            self.ClockInTime1 + '","' + \
            self.ClockOutTime1 + '","' + \
            self.ClockInTime2 + '","' + \
            self.ClockOutTime2 + '"'

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
