# Part 1: What do our deliveries cost?

You are building the cost tracker for a food delivery platform. Drivers are paid by the hour for the time they spend on deliveries, and finance wants to know what the deliveries recorded so far cost in total. `DeliveryCostTracker` in `tracker.py` has the methods stubbed out. Implement them.

- `add_driver(driver_id, usd_hourly_rate)` registers a driver and their hourly rate in US dollars.
- `record_delivery(delivery_id, driver_id, start_time, end_time)` records one delivery. Times are seconds since the epoch. The driver is paid for the time between `start_time` and `end_time` at their hourly rate.
- `update_driver_rate(driver_id, usd_hourly_rate, effective_time)` gives a driver a new rate. A delivery is paid at the rate in effect when it starts, so the new rate applies to deliveries that start at or after `effective_time`. The cost of a delivery is fixed when it is recorded.
- `get_total_cost()` returns the cost of every recorded delivery as a string with exactly two decimals, rounded half up to the cent, for example `"135.30"`. With nothing recorded it is `"0.00"`.

Rules from the operations team:

- Delivery ids are unique. Recording a delivery id that was already recorded is ignored.
- A delivery longer than 3 hours is a data error and is ignored. Exactly 3 hours is fine.
- Recording a delivery for an unknown driver, or one that ends before it starts, raises `ValueError`.

Example: a driver at $20.00 an hour who makes a 90-minute delivery and a 30-minute delivery costs `"40.00"`.

## Running the tests

The tests for this part are in `tests/test_costs.py` (the examples above) and `tests/test_costs_edge_cases.py`.

```bash
pytest tests/test_costs.py tests/test_costs_edge_cases.py
```

Run everything with:

```bash
pytest
```

## Ground rules

- Change `tracker.py` and add any modules you need. Do not edit the provided tests. You can add your own in new files.
- Use the AI assistant however you normally would at work.
- Talk through your design before you build it, and what you are trying as you go.
