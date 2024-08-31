from src.config import Config
from src.scheduler import Scheduler
from src.subscription import SubscriptionManager
from src.notification import NotificationSystem
from src.report import ReportGenerator

def main():
    config = Config.load("config.yaml")
    scheduler = Scheduler(config)
    subscription_manager = SubscriptionManager(config)
    notification_system = NotificationSystem(config)
    report_generator = ReportGenerator(config)
    scheduler.start(subscription_manager, notification_system, report_generator)

if __name__ == "__main__":
    main()
