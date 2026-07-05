async function askAI() {

    const question = document.getElementById("question").value;

    if (question.trim() === "") {
        return;
    }

    const form = new FormData();

    form.append("report_id", REPORT_ID);
    form.append("question", question);

    document.getElementById("answer").innerHTML = "🤖 Thinking...";

    const response = await fetch("/ask", {
        method: "POST",
        body: form
    });

    const data = await response.json();

    document.getElementById("answer").innerHTML = data.answer;
}