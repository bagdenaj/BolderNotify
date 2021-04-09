from crontab import CronTab

cron = CronTab(tabfile='bolder.tab')
job = cron.new(command='python test.py')
job.every(1).minutes()
#job.hour.on(7)

for result in cron.run_scheduler():
    print("This was printed to stdout by the process.")

for item in cron:
	print(item)

cron.write()