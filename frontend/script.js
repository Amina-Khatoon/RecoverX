const form = document.getElementById("predictionForm");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "Predicting...";

    const data = {
        case_id: Number(document.getElementById("case_id").value),
        amount_due: Number(document.getElementById("amount_due").value),
        days_overdue: Number(document.getElementById("days_overdue").value),
        monthly_income: Number(document.getElementById("monthly_income").value),
        monthly_expense: Number(document.getElementById("monthly_expense").value),
        payment_history_score: Number(
            document.getElementById("payment_history_score").value
        ),
        missed_payments: Number(
            document.getElementById("missed_payments").value
        ),
        previous_recovery_rate: Number(
            document.getElementById("previous_recovery_rate").value
        ),
        contact_success_rate: Number(
            document.getElementById("contact_success_rate").value
        ),
        last_payment_days_ago: Number(
            document.getElementById("last_payment_days_ago").value
        ),
        account_age_days: Number(
            document.getElementById("account_age_days").value
        ),
        reminders_received: Number(
            document.getElementById("reminders_received").value
        ),
        digital_engagement: Number(
            document.getElementById("digital_engagement").value
        ),
        hardship_flag: Number(
            document.getElementById("hardship_flag").value
        ),
        recovery_days: Number(
            document.getElementById("recovery_days").value
        )
    };

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/api/predict/",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Prediction failed");
        }

        resultDiv.innerHTML = `
            <h2>Prediction Result</h2>

            <p>
                <strong>Recovery Probability:</strong>
                ${result.prediction.recovery_probability}%
            </p>

            <p>
                <strong>Prediction:</strong>
                ${result.prediction.prediction}
            </p>

            <p>
                <strong>Recovery Level:</strong>
                ${result.prediction.recovery_level}
            </p>

            <p>
                <strong>Recommended Action:</strong>
                ${result.prediction.recommended_action}
            </p>
        `;

    } catch (error) {
        console.error("Prediction error:", error);

        resultDiv.innerHTML = `
            <p style="color:red;">
                <strong>Error:</strong> ${error.message}
            </p>
        `;
    }
});