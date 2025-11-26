from enum import Enum

class PolicyType(str, Enum):
    SECURITY = "security"
    COST = "cost"
    GOVERNANCE = "governance"


class CloudType(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
