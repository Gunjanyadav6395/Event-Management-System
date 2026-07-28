document.addEventListener("DOMContentLoaded", function () {

    const sidebar = document.getElementById("sidebar");
    const toggle = document.getElementById("toggleSidebar");

    if (toggle && sidebar) {

        toggle.addEventListener("click", function () {

            if (sidebar.style.display === "none") {
                sidebar.style.display = "block";
            } else {
                sidebar.style.display = "none";
            }

        });

    }

});