from dataclasses import dataclass
from math import sqrt
from scipy.stats import norm

@dataclass
class Variant:
    users: int
    conversions: int

    @property
    def rate(self) -> float:
        return self.conversions / self.users

def two_proportion_test(control: Variant, treatment: Variant) -> dict:
    pooled = (control.conversions + treatment.conversions) / (control.users + treatment.users)
    se = sqrt(pooled * (1-pooled) * (1/control.users + 1/treatment.users))
    z = (treatment.rate - control.rate) / se
    p = 2 * (1 - norm.cdf(abs(z)))
    diff = treatment.rate - control.rate
    se_diff = sqrt(control.rate*(1-control.rate)/control.users + treatment.rate*(1-treatment.rate)/treatment.users)
    ci = (diff - 1.96*se_diff, diff + 1.96*se_diff)
    return {"control_rate": control.rate, "treatment_rate": treatment.rate, "lift": diff, "z": z, "p_value": p, "ci_95": ci}

if __name__ == "__main__":
    print(two_proportion_test(Variant(10000, 6100), Variant(10000, 6550)))
