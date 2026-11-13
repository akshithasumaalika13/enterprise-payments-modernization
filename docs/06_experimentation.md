# Product Experiment: Personalized Payment Reminder

## Hypothesis
A personalized reminder containing amount due and a direct payment CTA increases payment completion compared with a generic reminder.

## Design
- Control: generic reminder
- Treatment: personalized amount + direct CTA
- Primary metric: payment completion rate
- Secondary: time to payment
- Guardrails: unsubscribe rate, support-contact rate, notification opt-out rate

## Analysis
Use Python/SciPy for two-proportion significance testing, confidence intervals and effect size. Publish experiment output into `fct_experiment_results`.
