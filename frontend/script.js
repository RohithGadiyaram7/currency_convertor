async function convertCurrency() {

    const amount =
        document.getElementById("amount").value;

    const from_currency =
        document.getElementById("from_currency").value;

    const to_currency =
        document.getElementById("to_currency").value;

    const response = await fetch(
        "http://127.0.0.1:8000/convert",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                amount: parseFloat(amount),
                from_currency,
                to_currency
            })
        }
    );

    const data = await response.json();

    document.getElementById("result").innerHTML =
        `${amount} ${from_currency}
         =
         ${data.converted_amount.toFixed(2)} ${to_currency}`;

    loadHistory();
}


async function loadHistory() {

    const response = await fetch(
        "http://127.0.0.1:8000/history"
    );

    const data = await response.json();

    const tableBody =
        document.querySelector("#history_table tbody");

    tableBody.innerHTML = "";

    data.forEach(item => {

        tableBody.innerHTML += `
            <tr>
                <td>${item.id}</td>
                <td>${item.from_currency}</td>
                <td>${item.to_currency}</td>
                <td>${item.amount}</td>
                <td>${item.converted_amount.toFixed(2)}</td>
            </tr>
        `;
    });
}


loadHistory();

async function aiConvert() {

    const text =
        document.getElementById("ai_input").value;

    const response = await fetch(
        "http://127.0.0.1:8000/ai-convert",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text
            })
        }
    );

    const data = await response.json();

    if (data.error) {

        document.getElementById("result").innerHTML =
            data.error;

        return;
    }

    document.getElementById("result").innerHTML =
        `${data.amount} ${data.from_currency}
         =
         ${data.converted_amount.toFixed(2)}
         ${data.to_currency}`;

    loadHistory();
}