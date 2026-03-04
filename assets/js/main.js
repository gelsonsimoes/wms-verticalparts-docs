// TABS
document.querySelectorAll(".tab-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const card = btn.closest(".tutorial-card");
    card
      .querySelectorAll(".tab-btn")
      .forEach((b) => b.classList.remove("active"));
    card
      .querySelectorAll(".tab-content")
      .forEach((c) => c.classList.remove("active"));
    btn.classList.add("active");
    card.querySelector("#" + btn.dataset.tab).classList.add("active");
  });
});

// SCROLL SPY
const sideLinks = document.querySelectorAll(".sidebar a[href^='#']");
if (sideLinks.length) {
  const spy = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          sideLinks.forEach((l) => l.classList.remove("active"));
          const a = document.querySelector(
            `.sidebar a[href="#${e.target.id}"]`,
          );
          if (a) a.classList.add("active");
        }
      });
    },
    { rootMargin: "-25% 0px -65% 0px" },
  );
  document
    .querySelectorAll(".tutorial-card[id]")
    .forEach((el) => spy.observe(el));
}

// CURSOR ANIMADO
function runDemo(containerId, steps) {
  const box = document.getElementById(containerId);
  if (!box) return;
  box.style.position = "relative";
  const cur = document.createElement("div");
  cur.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24">
    <path fill="#f0a500" stroke="#000" stroke-width="1.2"
      d="M4 0 L4 18 L8 14 L11 20 L13 19 L10 13 L16 13 Z"/>
  </svg>`;
  cur.style.cssText =
    "position:absolute;pointer-events:none;z-index:99;transition:left .55s ease,top .55s ease;";
  box.appendChild(cur);
  let i = 0;
  (function tick() {
    if (i >= steps.length) i = 0;
    const s = steps[i++];
    cur.style.left = s.x + "px";
    cur.style.top = s.y + "px";
    if (s.click) {
      setTimeout(() => {
        cur.style.transform = "scale(0.65)";
        setTimeout(() => (cur.style.transform = "scale(1)"), 140);
      }, 480);
    }
    setTimeout(tick, s.pause || 1100);
  })();
}
