from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import csv
import os

from .predict import predict_recovery
from .agent import decide_recovery_action, create_audit_record


@csrf_exempt
def predict_view(request):

    if request.method != "POST":
        return JsonResponse(
            {
                "error": "Only POST request is allowed"
            },
            status=405
        )

    try:
        data = json.loads(request.body)

        # Step 1: ML prediction
        prediction = predict_recovery(data)

        # Step 2: Agent decision
        decision = decide_recovery_action(
            data,
            prediction
        )

        # Step 3: Audit record
        audit_record = create_audit_record(
            data,
            prediction,
            decision
        )

        return JsonResponse(
            {
                "prediction": prediction,
                "agent": decision,
                "audit": audit_record
            },
            status=200
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "error": "Invalid JSON data"
            },
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            status=400
        )


def dashboard_view(request):

    csv_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "data",
            "recovery_data.csv"
        )
    )

    total_cases = 0
    recovered = 0
    not_recovered = 0
    total_amount_due = 0
    total_days_overdue = 0
    total_recovery_days = 0
    recovery_days_count = 0

    with open(csv_path, newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            total_cases += 1

            if row["recovered"] == "1":
                recovered += 1
            else:
                not_recovered += 1

            total_amount_due += float(row["amount_due"])
            total_days_overdue += float(row["days_overdue"])

            if row["recovery_days"]:
                total_recovery_days += float(row["recovery_days"])
                recovery_days_count += 1

    recovery_rate = (
        (recovered / total_cases) * 100
        if total_cases
        else 0
    )

    average_amount_due = (
        total_amount_due / total_cases
        if total_cases
        else 0
    )

    average_days_overdue = (
        total_days_overdue / total_cases
        if total_cases
        else 0
    )

    average_recovery_days = (
        total_recovery_days / recovery_days_count
        if recovery_days_count
        else 0
    )

    return JsonResponse({
        "dashboard": {
            "total_cases": total_cases,
            "recovered": recovered,
            "not_recovered": not_recovered,
            "recovery_rate": round(recovery_rate, 1),
            "average_amount_due": round(average_amount_due, 2),
            "average_days_overdue": round(average_days_overdue, 2),
            "average_recovery_days": round(average_recovery_days, 2)
        }
    })