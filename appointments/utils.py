from calendar import HTMLCalendar
from .models import AppointmentsCalendar


class Calendar(HTMLCalendar):
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
                # print(appointment.confirmed)
            else:
                li = '<li class="unconfirmed">'
                # print(appointment.confirmed)
            listItem = li + f'{appointment.get_html_url}: <span>{appointment.time}</span></li>'
            d += listItem
            print(d)
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
