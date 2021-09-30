import matplotlib.pyplot as py
import datetime


taipei = [80, 60, 70, 30, 30, 40, 30]
taichung = [60, 50, 30, 10, 20, 10, 40]
tainan = [20, 10, 0, 10, 10, 20, 30]
weekdays = ['Mon.', 'Tues.', 'Wed.', 'Thur.', 'Fri.', 'Sat.', 'Sun.']

py.style.use('ggplot')
py.plot(weekdays, taipei, color = 'b', label='Taipei', marker='o')
py.plot(weekdays, taichung, color = 'gold', label='Taichung', marker='o')
py.plot(weekdays, tainan, color = 'tab:olive', label='Tainan', marker='o')
py.xlabel('Day')
py.ylabel('Probability(%)')
py.ylim(0, 100)
py.yticks(range(0, 100, 20))
py.legend(loc='upper right')
py.show()
