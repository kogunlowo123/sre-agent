# SRE Agent Architecture

Site Reliability Engineering agent that defines and monitors SLOs/SLIs, manages error budgets, performs capacity planning, automates toil reduction, conducts chaos engineering experiments, and provides reliability scoring across services.

## Domain Tools

- **define_slo**: Define an SLO with SLIs and error budget
- **check_error_budget**: Check remaining error budget for a service
- **plan_capacity**: Forecast capacity needs based on growth trends
- **identify_toil**: Identify repetitive manual tasks that can be automated
- **run_chaos_experiment**: Run a controlled chaos engineering experiment
- **score_reliability**: Calculate reliability score for a service