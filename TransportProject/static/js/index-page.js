document.addEventListener("DOMContentLoaded", function () {
  const customButtons = document.querySelectorAll(".custom-button1");

  customButtons.forEach((customButton) => {
    const icon = customButton.querySelector("i");

    customButton.addEventListener("mouseover", function () {
      icon.classList.remove("fa-regular");
      icon.classList.add("fa-solid");
      icon.style.color = "red"; // Change the color to your desired hover color
    });

    customButton.addEventListener("mouseout", function () {
      icon.classList.remove("fa-solid");
      icon.classList.add("fa-regular");
      icon.style.color = "initial"; // Revert the color to its default
    });
  });
});
