"""Delivery cost tracking for a food delivery platform.

Times are seconds since the epoch. Rates are US dollars per hour. Money is
returned as a string with exactly two decimals, for example "135.30".
"""


class DeliveryCostTracker:
    def add_driver(self, driver_id, usd_hourly_rate):
        """Register a driver who is paid usd_hourly_rate per hour of delivery."""
        raise NotImplementedError

    def update_driver_rate(self, driver_id, usd_hourly_rate, effective_time):
        """Change a driver's rate for deliveries that start at or after effective_time."""
        raise NotImplementedError

    def record_delivery(self, delivery_id, driver_id, start_time, end_time):
        """Record one delivery made by a registered driver."""
        raise NotImplementedError

    def get_total_cost(self):
        """Return the cost of every recorded delivery, for example "135.30"."""
        raise NotImplementedError
