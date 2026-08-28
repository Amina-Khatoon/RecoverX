from datetime import datetime


def decide_recovery_action(data, prediction):
    """
    Recovery decision engine for RecoverX.
    """

    probability = float(prediction["recovery_probability"])
    hardship_flag = int(data.get("hardship_flag", 0))
    days_overdue = int(data.get("days_overdue", 0))
    missed_payments = int(data.get("missed_payments", 0))

    # Stopping rule for hardship cases
    if hardship_flag == 1:
        return {
            "agent_decision": "HUMAN_REVIEW",
            "action": "Manual Review",
            "reason": "Hardship flag detected",
            "automation_allowed": False,
            "stop_reason": "Automated recovery stopped for hardship case",
        }

    # Escalation rule
    if days_overdue >= 120 or missed_payments >= 5:
        return {
            "agent_decision": "ESCALATE",
            "action": "Priority Recovery Follow-up",
            "reason": "High overdue duration or repeated missed payments",
            "automation_allowed": True,
            "stop_reason": None,
        }

    # High recovery probability
    if probability >= 75:
        return {
            "agent_decision": "RECOVER",
            "action": "High Priority Recovery Reminder",
            "reason": "High predicted recovery probability",
            "automation_allowed": True,
            "stop_reason": None,
        }

    # Medium probability
    if probability >= 50:
        return {
            "agent_decision": "FOLLOW_UP",
            "action": "Moderate Follow-up + Flexible Plan",
            "reason": "Medium predicted recovery probability",
            "automation_allowed": True,
            "stop_reason": None,
        }

    # Low probability
    return {
        "agent_decision": "ALTERNATIVE_STRATEGY",
        "action": "Alternative Recovery Strategy",
        "reason": "Low predicted recovery probability",
        "automation_allowed": True,
        "stop_reason": None,
    }


def create_audit_record(data, prediction, decision):
    """
    Creates an audit record for every agent decision.
    """

    return {
        "timestamp": datetime.now().isoformat(),
        "case_id": data.get("case_id"),
        "recovery_probability": prediction["recovery_probability"],
        "prediction": prediction["prediction"],
        "recovery_level": prediction["recovery_level"],
        "agent_decision": decision["agent_decision"],
        "action": decision["action"],
        "reason": decision["reason"],
        "automation_allowed": decision["automation_allowed"],
        "stop_reason": decision["stop_reason"],
    }