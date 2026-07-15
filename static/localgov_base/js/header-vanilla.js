"""Vanilla JS header component adapted from LocalGov Base theme."""

(function () {
  const mobileBreakpoint = parseInt(
    document.body.dataset.mobileBreakpoint || "768",
    10,
  );

  function initHeader() {
    const headerSearchFormLabel = document.querySelector(
      ".lgd-region--search form label",
    );
    if (headerSearchFormLabel) {
      headerSearchFormLabel.classList.add("visually-hidden");
    }

    let secondaryMenuRegionIsOpen = false;
    const headerToggleSelector = ".lgd-header__toggle";
    const primaryToggleClass = "lgd-header__toggle--primary";
    const toggleActiveClass = "lgd-header__toggle--active";
    const regionActiveClass = "lgd-header__nav--active";
    const navInfo = {};
    let windowWidth = window.innerWidth;
    const headerToggles = document.querySelectorAll(headerToggleSelector);

    if (!headerToggles.length) {
      return;
    }

    function handleReset() {
      headerToggles.forEach((headerToggle) => {
        headerToggle.setAttribute("aria-expanded", "false");
        headerToggle.classList.remove(toggleActiveClass);
      });
      Object.keys(navInfo).forEach((nav) => {
        navInfo[nav].region.classList.remove(regionActiveClass);
      });
    }

    function handleEscKeyClick(buttonToFocus) {
      document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
          e.preventDefault();
          handleReset();
          buttonToFocus.focus();
        }
      });
    }

    headerToggles.forEach((toggle) => {
      const region = document.getElementById(toggle.getAttribute("aria-controls"));
      const nav = toggle.classList.contains(primaryToggleClass) ? "primary" : "secondary";
      if (region) {
        const links = region.querySelectorAll(".menu a");
        navInfo[nav] = {
          toggle,
          region,
          firstLink: links[0],
          lastLink: links[links.length - 1],
        };
      }
    });

    function handleToggleClick(toggleThatWasClicked) {
      const currentState = toggleThatWasClicked.getAttribute("aria-expanded") === "true";
      toggleThatWasClicked.setAttribute("aria-expanded", String(!currentState));
      toggleThatWasClicked.classList.toggle(toggleActiveClass);
    }

    function handlePrimaryMenuToggleClick() {
      handleToggleClick(navInfo.primary.toggle);
      handleEscKeyClick(navInfo.primary.toggle);
      navInfo.primary.region.classList.toggle(regionActiveClass);
      navInfo.secondary.region.classList.toggle(regionActiveClass);
    }

    function handleSecondaryMenuToggleClick() {
      handleToggleClick(navInfo.secondary.toggle);
      handleEscKeyClick(navInfo.secondary.toggle);
      navInfo.secondary.region.classList.toggle(regionActiveClass);
      if (navInfo.secondary.region.classList.contains(regionActiveClass)) {
        navInfo.secondary.firstLink.focus();
      }
      secondaryMenuRegionIsOpen = !secondaryMenuRegionIsOpen;
    }

    document.addEventListener("click", (e) => {
      if (
        !e.target.closest("#lgd-header__nav--secondary") &&
        !e.target.closest(".lgd-header__toggle--secondary") &&
        secondaryMenuRegionIsOpen
      ) {
        handleSecondaryMenuToggleClick();
      }
    });

    function handleWindowResized() {
      handleReset();
      if (window.innerWidth < mobileBreakpoint) {
        if (navInfo.secondary?.toggle) {
          navInfo.secondary.toggle.removeEventListener("click", handleSecondaryMenuToggleClick, true);
        }
        if (navInfo.primary?.toggle) {
          navInfo.primary.toggle.addEventListener("click", handlePrimaryMenuToggleClick);
        }
      } else {
        if (navInfo.primary?.toggle) {
          navInfo.primary.toggle.removeEventListener("click", handlePrimaryMenuToggleClick, true);
        }
        if (navInfo.secondary?.toggle) {
          navInfo.secondary.toggle.addEventListener("click", handleSecondaryMenuToggleClick);
        }
      }
    }

    function handleCheckIfWindowActuallyResized() {
      if (window.innerWidth !== windowWidth) {
        windowWidth = window.innerWidth;
        handleWindowResized();
      }
    }

    handleWindowResized();
    window.addEventListener("resize", () => {
      setTimeout(handleCheckIfWindowActuallyResized, 50);
    });
  }

  document.addEventListener("DOMContentLoaded", initHeader);
})();
