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
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, appointments):
        appointments_per_day = appointments.filter(date__day=day)
        d = ''
        for appointment in appointments_per_day:
            if appointment.confirmed:
                li = '<li class="confirmed">'
            else:
                li = '<li class="unconfirmed">'
            listItem = li + f'{appointment.get_html_url}: <span>{appointment.time}</span></li>'
            d += listItem
        if day != 0 and d:
            return f'<td class="appointment"><span class="date">{day}</span><ul> {d} </ul></td>'
        elif day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        else:
            return "<td class='no-date'></td>"

    # formats a week as a tr
    def formatweek(self, theweek, appointments):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, appointments)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        appointments = AppointmentsCalendar.objects.filter(date__year=self.year, date__month=self.month)

        cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, appointments)}\n'
        return cal


def convertToDatetime(date):
    """ Converts previous or next month date from GET request into datetime object """
    getDate = []
    if date:
        for item in date.split('/'):
            getDate.append(int(item))
        convertDate = datetime(getDate[2], getDate[1], getDate[0])
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
    footer = f'</table><footer><div class="footer-copyright"><div id="copyRight">2011 - {currentYear} © Thomas Jones - All Rights Reserved</div></div></footer>'
    return footer
