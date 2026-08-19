document.addEventListener("DOMContentLoaded", function () {

    // ==========================
    // Sidebar Toggle
    // ==========================

    const sidebar = document.getElementById("sidebar");
    const toggle = document.getElementById("toggleSidebar");

    if (toggle && sidebar) {

        toggle.addEventListener("click", function () {

            sidebar.style.display =
                sidebar.style.display === "none"
                    ? "block"
                    : "none";

        });

    }


    // ==========================
    // Theme Elements
    // ==========================

    const navbar =
        document.querySelector("nav.navbar");

    const sidebarPanel =
        document.getElementById("sidebar");


    // ==========================
    // Navbar Theme
    // ==========================

    document
        .querySelectorAll(".navbar-color")
        .forEach(function (button) {

            button.addEventListener("click", function () {

                const color =
                    this.dataset.color;

                if (navbar) {

                    navbar.classList.remove(
                        "bg-primary",
                        "bg-success",
                        "bg-danger",
                        "bg-warning",
                        "bg-dark"
                    );

                    navbar.classList.add(color);

                    localStorage.setItem(
                        "navbarColor",
                        color
                    );

                }

            });

        });


    // ==========================
    // Sidebar Theme
    // ==========================

    document
        .querySelectorAll(".sidebar-color")
        .forEach(function (button) {

            button.addEventListener("click", function () {

                const color =
                    this.dataset.color;

                if (sidebarPanel) {

                    sidebarPanel.classList.remove(
                        "bg-primary",
                        "bg-success",
                        "bg-danger",
                        "bg-warning",
                        "bg-dark"
                    );

                    sidebarPanel.classList.add(color);

                    localStorage.setItem(
                        "sidebarColor",
                        color
                    );

                }

            });

        });


    // ==========================
    // Load Saved Navbar
    // ==========================

    const savedNavbar =
        localStorage.getItem("navbarColor");

    if (savedNavbar && navbar) {

        navbar.classList.remove(
            "bg-primary",
            "bg-success",
            "bg-danger",
            "bg-warning",
            "bg-dark"
        );

        navbar.classList.add(savedNavbar);

    }


    // ==========================
    // Load Saved Sidebar
    // ==========================

    const savedSidebar =
        localStorage.getItem("sidebarColor");

    if (savedSidebar && sidebarPanel) {

        sidebarPanel.classList.remove(
            "bg-primary",
            "bg-success",
            "bg-danger",
            "bg-warning",
            "bg-dark"
        );

        sidebarPanel.classList.add(savedSidebar);

    }


    // ==========================
    // Card Style
    // ==========================

    const cardStyle =
        document.getElementById("cardStyle");

    const cards =
        document.querySelectorAll(".card");


    function applyCardStyle(style) {

        cards.forEach(function (card) {

            card.classList.remove(
                "card-rounded",
                "card-square",
                "card-glass"
            );

            if (style === "rounded") {

                card.classList.add(
                    "card-rounded"
                );

            }

            if (style === "square") {

                card.classList.add(
                    "card-square"
                );

            }

            if (style === "glass") {

                card.classList.add(
                    "card-glass"
                );

            }

        });

        localStorage.setItem(
            "cardStyle",
            style
        );

    }


    if (cardStyle) {

        const savedStyle =
            localStorage.getItem("cardStyle")
            || "rounded";

        cardStyle.value =
            savedStyle;

        applyCardStyle(
            savedStyle
        );

        cardStyle.addEventListener(
            "change",
            function () {

                applyCardStyle(
                    this.value
                );

            }
        );

    }


    // ==========================
    // Dark Mode
    // ==========================

    const darkMode =
        document.getElementById("darkMode");


    if (darkMode) {

        if (
            localStorage.getItem("darkMode")
            === "true"
        ) {

            document.body.classList.add(
                "dark-mode"
            );

            darkMode.checked = true;

        }


        darkMode.addEventListener(
            "change",
            function () {

                if (this.checked) {

                    document.body.classList.add(
                        "dark-mode"
                    );

                    localStorage.setItem(
                        "darkMode",
                        "true"
                    );

                } else {

                    document.body.classList.remove(
                        "dark-mode"
                    );

                    localStorage.setItem(
                        "darkMode",
                        "false"
                    );

                }

            }
        );

    }


    // ==========================
    // Dashboard Chart
    // ==========================

    const chartCanvas =
        document.getElementById("eventChart");


    if (
        chartCanvas &&
        typeof Chart !== "undefined"
    ) {

        new Chart(
            chartCanvas,
            {

                type: "bar",

                data: {

                    labels: [
                        "Jan",
                        "Feb",
                        "Mar",
                        "Apr",
                        "May",
                        "Jun",
                        "Jul"
                    ],

                    datasets: [{

                        label: "Events",

                        data: [
                            4,
                            8,
                            6,
                            10,
                            7,
                            12,
                            9
                        ],

                        borderWidth: 1

                    }]

                },

                options: {

                    responsive: true,

                    plugins: {

                        legend: {

                            display: false

                        }

                    },

                    scales: {

                        y: {

                            beginAtZero: true

                        }

                    }

                }

            }
        );

    }


    // ==========================
    // EVENTHUB AI CHATBOT
    // ==========================

    const chatbotToggle =
        document.getElementById(
            "chatbot-toggle"
        );

    const chatbotWindow =
        document.getElementById(
            "chatbot-container"
        );

    const chatbotClose =
        document.getElementById(
            "chatbot-close"
        );

    const chatbotInput =
        document.getElementById(
            "chatbot-input"
        );

    const chatbotSend =
        document.getElementById(
            "chatbot-send"
        );

    const chatbotMessages =
        document.getElementById(
            "chatbot-messages"
        );


    // ==========================
    // Check Chatbot Elements
    // ==========================

    console.log(
        "EventHub Chatbot:",
        {
            toggle: chatbotToggle,
            window: chatbotWindow,
            close: chatbotClose,
            input: chatbotInput,
            send: chatbotSend,
            messages: chatbotMessages
        }
    );


    // ==========================
    // Add Chat Message
    // ==========================

    function addChatMessage(
        message,
        type
    ) {

        if (!chatbotMessages) {
            return;
        }

        const messageDiv =
            document.createElement(
                "div"
            );

        messageDiv.className =
            "chatbot-message " +
            (
                type === "user"
                    ? "user-message"
                    : "bot-message"
            );

        messageDiv.textContent =
            message;

        chatbotMessages.appendChild(
            messageDiv
        );

        chatbotMessages.scrollTop =
            chatbotMessages.scrollHeight;

    }


    // ==========================
    // Send Chat Message
    // ==========================

    async function sendChatMessage() {

        if (!chatbotInput) {
            return;
        }

        const message =
            chatbotInput.value.trim();


        if (!message) {
            return;
        }


        // Show user message

        addChatMessage(
            message,
            "user"
        );

        chatbotInput.value = "";


        // Loading message

        const loading =
            document.createElement(
                "div"
            );

        loading.className =
            "chatbot-message bot-message";

        loading.textContent =
            "Thinking...";


        if (chatbotMessages) {

            chatbotMessages.appendChild(
                loading
            );

        }


        try {

            const csrfToken = document.querySelector(
    "[name=csrfmiddlewaretoken]"
)?.value;


const response =
    await fetch(
        "/chatbot/chat/",
        {

            method: "POST",

            headers: {

                "Content-Type":
                    "application/json",

                "X-CSRFToken":
                    csrfToken

            },

            body:
                JSON.stringify({
                    message:
                        message
                })

        }
    );


            const data =
                await response.json();


            loading.remove();


            if (!response.ok) {

                addChatMessage(
                    data.error ||
                    "Something went wrong.",
                    "bot"
                );

                return;

            }


            addChatMessage(
                data.response ||
                "I didn't receive a response.",
                "bot"
            );


        } catch (error) {

            loading.remove();


            addChatMessage(
                "Unable to connect to the server.",
                "bot"
            );


            console.error(
                "EventHub Chatbot Error:",
                error
            );

        }

    }


    // ==========================
    // Send Button
    // ==========================

    if (chatbotSend) {

        chatbotSend.addEventListener(
            "click",
            sendChatMessage
        );

    }


    // ==========================
    // Enter Key
    // ==========================

    if (chatbotInput) {

        chatbotInput.addEventListener(
            "keydown",
            function (event) {

                if (
                    event.key === "Enter"
                ) {

                    event.preventDefault();

                    sendChatMessage();

                }

            }
        );

    }

});