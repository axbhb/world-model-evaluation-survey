function setupEvents() {
  let searchTimer = null;
  els.search.addEventListener("input", () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      state.search = els.search.value.trim();
      els.searchClear.hidden = !state.search;
      updateUrl();
      renderAll();
    }, 120);
  });
  els.searchClear.addEventListener("click", () => {
    state.search = "";
    els.search.value = "";
    els.searchClear.hidden = true;
    updateUrl();
    renderAll();
    els.search.focus();
  });
  els.sort.addEventListener("change", () => {
    state.sort = els.sort.value;
    renderAll();
  });
  els.clearFilters.addEventListener("click", clearAll);
  els.emptyClear.addEventListener("click", clearAll);
  els.openFilters.addEventListener("click", openFilters);
  els.closeFilters.addEventListener("click", closeFilters);
  els.filterBackdrop.addEventListener("click", closeFilters);
  els.clearYear.addEventListener("click", () => {
    state.year = null;
    updateUrl();
    renderAll();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && document.body.classList.contains("filters-open")) closeFilters();
  });
  $$(".taxonomy-jump").forEach((button) => {
    button.addEventListener("click", () => document.getElementById(button.dataset.scrollTarget)?.scrollIntoView({ behavior: "smooth", block: "center" }));
  });
  els.copyCitation.addEventListener("click", async () => {
    const text = els.citation.innerText;
    try {
      await navigator.clipboard.writeText(text);
      const previous = els.copyCitation.textContent;
      els.copyCitation.textContent = "Copied";
      setTimeout(() => { els.copyCitation.textContent = previous; }, 1400);
    } catch {
      window.prompt("Copy this BibTeX:", text);
    }
  });
}

function setupNavObserver() {
  const links = $$(".primary-nav a");
  const sections = links.map((link) => document.querySelector(link.getAttribute("href"))).filter(Boolean);
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (!visible) return;
    links.forEach((link) => link.removeAttribute("aria-current"));
    const active = links.find((link) => link.getAttribute("href") === `#${visible.target.id}`);
    if (active) active.setAttribute("aria-current", "true");
  }, { rootMargin: "-25% 0px -65%", threshold: [0, .15, .4] });
  sections.forEach((section) => observer.observe(section));
}

async function init() {
  try {
    const dataFiles = [1, 2, 3, 4].map((index) => `assets/benchmarks-${index}.json`);
    const responses = await Promise.all([...dataFiles, "assets/metadata.json"].map((url) => fetch(url)));
    const failed = responses.find((response) => !response.ok);
    if (failed) throw new Error(`HTTP ${failed.status}`);
    const decoded = await Promise.all(responses.map((response) => response.json()));
    state.benchmarks = decoded.slice(0, 4).flat();
    state.metadata = decoded[4];
    readUrl();
    buildFilters();
    buildShortcuts();
    buildMatrix();
    setupEvents();
    setupNavObserver();
    renderAll();
  } catch (error) {
    console.error(error);
    els.grid.innerHTML = `<div class="empty-state"><h3>Benchmark data could not be loaded.</h3><p>${escapeHtml(error.message)}</p></div>`;
  }
}

init();
