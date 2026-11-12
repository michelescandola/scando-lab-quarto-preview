/**
 * Shared navigation and publication filters for the multipage Quarto site.
 * Quarto renders the content; JavaScript adds only small interactions.
 * Original visual design: michelescandola/scando-lab, MIT License.
 */
"use strict";

(() => {
  const menuButton = document.querySelector(".menu-button");
  const navigation = document.querySelector(".nav-links");
  const navigationLinks = document.querySelectorAll(".nav-links a");
  const currentPage = document.body.dataset.page;

  // IDs come from _quarto.yml and each page's YAML front matter.
  navigationLinks.forEach((link) => {
    if (link.dataset.page === currentPage) link.setAttribute("aria-current", "page");
  });

  function setMenuOpen(isOpen) {
    menuButton.setAttribute("aria-expanded", String(isOpen));
    menuButton.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
    navigation.dataset.open = String(isOpen);
  }

  if (menuButton && navigation) {
    menuButton.addEventListener("click", () => {
      setMenuOpen(menuButton.getAttribute("aria-expanded") !== "true");
    });
    navigationLinks.forEach((link) => {
      link.addEventListener("click", () => setMenuOpen(false));
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
        setMenuOpen(false);
        menuButton.focus();
      }
    });
    document.addEventListener("click", (event) => {
      if (event.target instanceof Element && !event.target.closest(".site-header")) {
        setMenuOpen(false);
      }
    });
    window.matchMedia("(min-width: 951px)").addEventListener("change", (event) => {
      if (event.matches) setMenuOpen(false);
    });
  }

  const buttons = document.querySelectorAll(".filter-button");
  const publications = document.querySelectorAll(".publication");
  const status = document.querySelector(".filter-status");

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const topic = button.dataset.filter;
      let visibleCount = 0;
      buttons.forEach((candidate) => {
        candidate.setAttribute("aria-pressed", String(candidate === button));
      });
      publications.forEach((publication) => {
        // One record may belong to several topics; filtering never duplicates it.
        const topics = publication.dataset.topics.split(" ");
        publication.hidden = topic !== "all" && !topics.includes(topic);
        if (!publication.hidden) visibleCount += 1;
      });
      if (status) {
        status.textContent = visibleCount + " publications · " +
          (topic === "all" ? "All topics" : button.textContent.trim()) + " · Newest first";
      }
    });
  });
})();
