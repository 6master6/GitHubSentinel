import schedule
import time

class Scheduler:
    def __init__(self, config):
        self.config = config

    def start(self, subscription_manager, notification_system, report_generator):
        interval = self.config.get("schedule_interval", "daily")
        
        if interval == "daily":
            schedule.every().day.at(self.config.get("daily_time", "00:00")).do(
                self.run, subscription_manager, notification_system, report_generator
            )
        elif interval == "weekly":
            schedule.every().monday.at(self.config.get("weekly_time", "00:00")).do(
                self.run, subscription_manager, notification_system, report_generator
            )
        
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    def run(self, subscription_manager, notification_system, report_generator):
        updates = subscription_manager.fetch_updates()
        report = report_generator.generate_report(updates)
        notification_system.send_notifications(report)
