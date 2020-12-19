from calendar import HTMLCalendar
from .models import AppointmentsCalendar
from datetime import datetime, timedelta
import calendar


""" Code for Calendar take and modified from the following sources:
    https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html
    https://medium.com/@unionproject88/django-and-python-calendar-e647a8eccff6
    https://www.geeksforgeeks.org/python-calendar-module/ """


class Calendar(HTMLCalendar):
    """ Constructs a monthly calendar and populates with appointments """
    def __init__(self, year=None, month=None, user=None):
        self.year = year
        self.month = month
        self.user = user
        super(Calendar, self).__init__()

    def formatday(self, day, appointments):
        """ Formats a day as a td & filters events by day """
        appointments_per_day = appointments.filter(date__day=day)
        d = ''
        appointmentList = []
        for appointment in appointments_per_day:
            if self.user:
                if appointment.user == self.user:
                    appointmentList.append(getAppointmentDict(appointment))
            else:
                appointmentList.append(getAppointmentDict(appointment))

        for item in sortAppointmentList(appointmentList, 'appointmentTime'):
            d += item['listItem']

        if day != 0 and d:
            return f'<td class="appointment"><span class="date">{day}</span><ul>{d}</ul></td>'
        elif day != 0:
            return f"<td><span class='date'>{day}</span><ul>{d}</ul></td>"
        else:
            return "<td class='no-date'></td>"

    def formatweek(self, theweek, appointments):
        """ Formats a week as a tr """
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, appointments)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        """ Formats a month as a table & filter & events by year and month """
        appointments = AppointmentsCalendar.objects.filter(date__year=self.year, date__month=self.month)
        cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, appointments)}\n'
        return cal


def convertToDatetime(date, time):
    """ Converts previous or next month date from GET request into datetime object """
    getDate = []
    getTime = []
    if date and time:
        for item in date.split('/'):
            getDate.append(int(item))

        for item in time.split(':'):
            getTime.append(int(item))
        print(getTime[0])
        print(getTime[1])
        convertDate = datetime(getDate[2], getDate[1], getDate[0], getTime[0], getTime[1])
    else:
        convertDate = datetime.today()
    return convertDate


def get_date(req_day):
    """ Converts string date from form into datetime object """
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()


def prev_month(d):
    """ Gets previous month using datetime & timedelta & converts to url string query """
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    """ Gets next month using calendar & timedelta & converts to url string query """
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_footer():
    """ Adds footer section to bottom of calendar table """
    currentYear = datetime.now().date().strftime('%Y')
    footer = f'</table><footer><div class="footer-copyright"><div id="copyRight">2011 - {currentYear} © Thomas Jones - All Rights Reserved</div></div><div class="footer-nav"><a href="#" id="backToTop" class="back-to-top btn-float active" title="Back to top"><i class="fas fa-chevron-circle-up fa-2x"></i></a></div></footer>'
    return footer


def getAppointmentDict(obj):
    """ Takes appointments obj & constructs dict of calendar HTML list item & appointment time """
    if obj.confirmed is True:
        li = '<li class="confirmed">'
    else:
        li = '<li class="unconfirmed">'
    appointmentTime = int(obj.time[0:2])
    listItem = li + f'{obj.get_html_url}: <span>{obj.time}</span></li>'
    appointmentDict = {
        'appointmentTime': appointmentTime,
        'listItem': listItem,
    }
    return appointmentDict


def sortAppointmentList(appointmentList, key):
    """ Takes list of dicts containing calendar HTML list items & sorts by time """
    def _sortFunc(appointmentList):
        return appointmentList[key]
    appointmentList.sort(key=_sortFunc)
    return appointmentList
