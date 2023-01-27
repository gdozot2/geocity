const button = document.getElementById("btn_accept_terms");
const checkbox = document.getElementById("chk_accept_terms");

checkbox.addEventListener("click", () => {
    button.toggleAttribute("disabled");
});
