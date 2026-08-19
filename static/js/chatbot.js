document.addEventListener("DOMContentLoaded", function () {

    const chatbotWindow =
        document.getElementById("chatbot-window");

    const chatbotToggle =
        document.getElementById("chatbot-toggle");

    const chatbotClose =
        document.getElementById("chatbot-close");


    // ==========================
    // OPEN CHATBOT
    // ==========================

    chatbotToggle.addEventListener("click", function () {

        chatbotWindow.style.display = "flex";

    });


    // ==========================
    // CLOSE CHATBOT
    // ==========================

    chatbotClose.addEventListener("click", function () {

        chatbotWindow.style.display = "none";

    });

});