/* PERA menu — progressive enhancements. The menu works fully without this file. */
(function () {
  "use strict";
  var strings = window.PERA || {};
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Remember the chosen language so the QR code (which points at the root) opens it next time.
  document.querySelectorAll("a[data-lang]").forEach(function (link) {
    link.addEventListener("click", function () {
      try { localStorage.setItem("pera-lang", link.dataset.lang); } catch (e) {}
    });
  });

  var chips = Array.prototype.slice.call(document.querySelectorAll(".chips a"));
  var sections = Array.prototype.slice.call(document.querySelectorAll(".cat"));

  function setActive(id) {
    chips.forEach(function (chip) {
      var on = chip.dataset.target === id;
      if (on) {
        chip.setAttribute("aria-current", "true");
        var bar = chip.closest(".chips");
        var target = chip.offsetLeft - (bar.clientWidth - chip.offsetWidth) / 2;
        bar.scrollTo({ left: target, behavior: reduceMotion ? "auto" : "smooth" });
      } else {
        chip.removeAttribute("aria-current");
      }
    });
  }

  // Highlight the chip of the section currently in view.
  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    }, { rootMargin: "-35% 0px -60% 0px" });
    sections.forEach(function (s) { observer.observe(s); });
  }

  // Vegetarian-only filter.
  var toggle = document.querySelector(".veg-toggle");
  var live = document.getElementById("live");
  if (toggle) {
    toggle.hidden = false;
    toggle.addEventListener("click", function () {
      var on = toggle.getAttribute("aria-pressed") !== "true";
      toggle.setAttribute("aria-pressed", String(on));
      var shown = 0;
      sections.forEach(function (section) {
        if (!section.dataset.filterable) return;
        var visible = 0;
        section.querySelectorAll(".dish").forEach(function (dish) {
          var keep = !on || dish.dataset.veg === "1";
          dish.hidden = !keep;
          if (keep) visible++;
        });
        section.querySelectorAll(".subgroup").forEach(function (group) {
          group.hidden = !group.querySelector(".dish:not([hidden])");
        });
        section.hidden = visible === 0;
        var chip = document.querySelector('.chips a[data-target="' + section.id + '"]');
        if (chip) chip.parentElement.hidden = visible === 0;
        shown += visible;
      });
      if (live) {
        live.textContent = on
          ? (strings.veg_count || "{n}").replace("{n}", shown)
          : (strings.all_count || "");
      }
    });
  }
})();
